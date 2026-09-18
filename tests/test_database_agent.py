"""Unit and Property-Based Tests for Database Agent & Graph Synchronization (Step 3.0).

Verifies Markdown parsing to GQL edges, cascading deletions, and graph topology invariants.
"""

import pytest
from pathlib import Path
from hypothesis import given, strategies as st
from database.mock_spanner import MockSpannerDatabase
from database.models import EquipmentModel, InstrumentModel, EquipmentFlowEdge
from agents.database.agent import DatabaseAgent


# ==============================================================================
# 1. Deterministic Unit Tests
# ==============================================================================

def test_ut_db_01_markdown_to_graph_edge(tmp_path):
    """UT-DB-01: Parse Markdown with equipment connections (E-2302A/B -> V-2301)."""
    db = MockSpannerDatabase()
    agent = DatabaseAgent(db)
    
    sample_md = """---
tag: E-2303
name: Preflash Column Steam Heater
type: HeatExchanger
unit: CDN
---
# E-2303
## Connections
E-2302A/B -> V-2301
| TXSHH-0502A | SIS Temp HH | UC-2301 ESD SIL 1 |
"""
    res = agent.sync_markdown_document(sample_md, file_uri="wiki/equipment/E-2303.md")
    assert res["status"] == "SUCCESS"
    assert "E-2303" in db.equipment
    assert "TXSHH-0502A" in db.instruments
    assert any(e.from_equipment_tag == "E-2302A/B" and e.to_equipment_tag == "V-2301" for e in db.equipment_flows)


def test_ut_db_02_cascade_deletion(tmp_path):
    """UT-DB-02: Delete 14780-8120-PS-0018, drops associated records and severs edges."""
    db = MockSpannerDatabase()
    log_path = tmp_path / "log.md"
    log_path.touch()
    
    # Pre-populate graph with equipment and connected flow
    db.equipment["PSV-0018"] = EquipmentModel(
        equipment_tag="PSV-0018",
        unit_id="CDN",
        name="Safety Relief Valve",
        type="PSV",
        markdown_uri="raw/14780-8120-PS-0018.pdf"
    )
    db.instruments["PSV-0018"] = InstrumentModel(
        instrument_tag="PSV-0018",
        equipment_tag="PSV-0018",
        type="PSV"
    )
    db.equipment_flows.append(EquipmentFlowEdge(
        from_equipment_tag="E-2303",
        to_equipment_tag="PSV-0018",
        stream_id="S-Relief"
    ))
    
    agent = DatabaseAgent(db)
    agent.deleter.log_file = log_path
    
    res = agent.delete_document("14780-8120-PS-0018")
    assert res["status"] == "SUCCESS"
    assert "PSV-0018" in res["dropped_equipment"]
    assert db.equipment["PSV-0018"].is_deleted is True
    assert res["severed_edges"] == 1
    assert len(db.equipment_flows) == 0


# ==============================================================================
# 2. Property-Based Invariant Tests (Hypothesis)
# ==============================================================================

@given(
    tag=st.text(alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", min_size=3, max_size=12)
)
def test_pbt_db_01_deletion_idempotence(tag):
    """PBT-DB-01: Graph Deletion Idempotence: Re-deleting an already deleted document is a no-op."""
    db = MockSpannerDatabase()
    agent = DatabaseAgent(db)
    agent.deleter.log_file = Path("/dev/null")
    
    db.equipment[tag] = EquipmentModel(
        equipment_tag=tag,
        unit_id="CDN",
        name=tag,
        type="Pump",
        markdown_uri=f"wiki/equipment/{tag}.md"
    )
    
    res1 = agent.delete_document(tag)
    assert tag in res1["dropped_equipment"]
    
    # Second deletion run
    res2 = agent.delete_document(tag)
    # Already marked deleted, no edges severed on second pass
    assert res2["severed_edges"] == 0


@given(
    chain_length=st.integers(min_value=2, max_value=5)
)
def test_pbt_gql_01_topology_roundtrip(chain_length):
    """PBT-GQL-01: Topology Round-trip: Linear graph A -> B -> C -> D reproduces upstream order."""
    db = MockSpannerDatabase()
    tags = [f"EQ-{i}" for i in range(chain_length)]
    
    for t in tags:
        db.equipment[t] = EquipmentModel(equipment_tag=t, unit_id="CDN", name=t, type="Vessel")
        
    for i in range(chain_length - 1):
        db.equipment_flows.append(EquipmentFlowEdge(
            from_equipment_tag=tags[i],
            to_equipment_tag=tags[i+1],
            stream_id=f"S-{i}"
        ))
        
    # Traverse upstream from the last node
    last_node = tags[-1]
    upstream = db.graph_traverse_upstream(last_node, max_depth=chain_length)
    found_tags = [u["upstream_tag"] for u in upstream]
    
    # All preceding nodes must be found
    expected_preceding = tags[:-1]
    for exp in expected_preceding:
        assert exp in found_tags
