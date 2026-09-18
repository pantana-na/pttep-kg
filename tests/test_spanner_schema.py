"""Unit and Property-Based Tests for Cloud Spanner Graph Schema & Models (Step 1.0).

Verifies DDL parsing, Pydantic entity fidelity, wiki seeding, and graph invariants.
"""

import pytest
from hypothesis import given, strategies as st
from database.init_db import load_ddl_statements, init_local_mock
from database.mock_spanner import MockSpannerDatabase, cosine_similarity
from database.models import (
    EquipmentModel, StreamModel, InstrumentModel, ChemicalHazardModel,
    HazopNodeModel, DeviationModel, CauseModel, ConsequenceModel,
    SafeguardModel, ActionItemModel, EquipmentFlowEdge
)


# ==============================================================================
# 1. Deterministic Unit Tests
# ==============================================================================

def test_ddl_statement_parsing():
    """Verify that database/spanner_schema.sql parses into valid DDL chunks."""
    statements = load_ddl_statements("database/spanner_schema.sql")
    assert len(statements) >= 15, f"Expected >= 15 DDL statements, got {len(statements)}"
    
    ddl_joined = " ".join(statements)
    for table in ["Units", "Equipment", "Streams", "Instruments", "ChemicalHazards",
                  "HazopNodes", "Deviations", "Causes", "Consequences", "Safeguards", "ActionItems"]:
        assert f"TABLE {table}" in ddl_joined or f"TABLE IF NOT EXISTS {table}" in ddl_joined
    assert "PROPERTY GRAPH PhenolProcessSafetyGraph" in ddl_joined
    assert "EquipmentKeywordSearchIndex" in ddl_joined
    assert "InstrumentsKeywordSearchIndex" in ddl_joined


def test_table_and_model_instantiation():
    """Verify Pydantic models initialize cleanly with required process safety fields."""
    eq = EquipmentModel(
        equipment_tag="E-2303",
        unit_id="CDN",
        name="Preflash Column Steam Heater",
        type="HeatExchanger",
        design_temp_celsius=195.0,
        design_pressure_barg=7.0,
        operating_temp_celsius=83.0,
        operating_pressure_barg=3.5
    )
    assert eq.equipment_tag == "E-2303"
    assert eq.operating_temp_celsius == 83.0

    inst = InstrumentModel(
        instrument_tag="TXSHH-0502A",
        equipment_tag="E-2303",
        type="SIS Temp HH",
        sil_rating="SIL 1",
        voting_logic="1oo2",
        is_sis_initiator=True
    )
    assert inst.sil_rating == "SIL 1"
    assert inst.is_sis_initiator is True


def test_mock_spanner_seeding_from_wiki():
    """Verify that local wiki markdown files seed successfully into the in-memory graph."""
    db = init_local_mock("wiki")
    assert len(db.equipment) >= 40, f"Expected >= 40 equipment, got {len(db.equipment)}"
    assert len(db.units) >= 3, f"Expected >= 3 units, got {len(db.units)}"
    assert len(db.chemical_hazards) >= 5, f"Expected >= 5 hazards, got {len(db.chemical_hazards)}"
    assert len(db.equipment_flows) >= 10, f"Expected >= 10 flow edges, got {len(db.equipment_flows)}"
    assert "E-2303" in db.equipment
    assert "CHP" in db.chemical_hazards or "cumene-hydroperoxide" in db.chemical_hazards or any("hydroperoxide" in k for k in db.chemical_hazards)


def test_e2303_interlock_and_upstream_topology():
    """Verify topological traversal and interlock lookups for E-2303."""
    db = init_local_mock("wiki")
    
    # 1. Check E-2303 Interlocks
    interlocks = db.graph_find_interlocks("E-2303")
    tags = [i["instrument_tag"] for i in interlocks]
    assert "TXSHH-0502A" in tags or "UXV-0501" in tags
    
    # 2. Check Keyword Search for E-2303
    search_res = db.keyword_search("E-2303 Steam Heater")
    assert len(search_res) > 0
    top_tag, top_score, _ = search_res[0]
    assert top_tag == "E-2303"


# ==============================================================================
# 2. Property-Based Invariant Tests (Hypothesis)
# ==============================================================================

@given(
    tag=st.text(alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-", min_size=2, max_size=32),
    name=st.text(min_size=1, max_size=64),
    temp=st.floats(min_value=-50.0, max_value=500.0, allow_nan=False),
    pressure=st.floats(min_value=0.0, max_value=100.0, allow_nan=False)
)
def test_pbt_equipment_model_roundtrip(tag, name, temp, pressure):
    """PBT Invariant: Any valid EquipmentModel serializes and deserializes identically."""
    eq = EquipmentModel(
        equipment_tag=tag,
        unit_id="U-2300",
        name=name,
        type="Pump",
        operating_temp_celsius=temp,
        operating_pressure_barg=pressure
    )
    dumped = eq.model_dump()
    reconstructed = EquipmentModel(**dumped)
    assert reconstructed == eq


@given(
    v1=st.lists(st.floats(min_value=-10.0, max_value=10.0, allow_nan=False), min_size=10, max_size=10),
    v2=st.lists(st.floats(min_value=-10.0, max_value=10.0, allow_nan=False), min_size=10, max_size=10)
)
def test_pbt_cosine_similarity_bounds(v1, v2):
    """PBT Invariant: Cosine similarity is always strictly within [-1.0, 1.0]."""
    sim = cosine_similarity(v1, v2)
    assert -1.0 <= sim <= 1.0
    # Self similarity of non-degenerate vector is 1.0
    if sum(x * x for x in v1) > 1e-4:
        self_sim = cosine_similarity(v1, v1)
        assert abs(self_sim - 1.0) < 1e-5


@given(
    nodes=st.lists(st.text(alphabet="ABCDEF", min_size=1, max_size=3), min_size=3, max_size=8, unique=True),
    max_depth=st.integers(min_value=1, max_value=4)
)
def test_pbt_graph_traversal_depth_bound(nodes, max_depth):
    """PBT Invariant: Graph traversal depth strictly never exceeds max_depth."""
    db = MockSpannerDatabase()
    for n in nodes:
        db.equipment[n] = EquipmentModel(equipment_tag=n, unit_id="U-2300", name=n, type="Vessel")
    
    # Create a linear chain: n[0] -> n[1] -> n[2] -> ...
    for i in range(len(nodes) - 1):
        db.equipment_flows.append(EquipmentFlowEdge(
            from_equipment_tag=nodes[i],
            to_equipment_tag=nodes[i+1],
            stream_id=f"S-{i}"
        ))
        
    target = nodes[-1]
    results = db.graph_traverse_upstream(target, max_depth=max_depth)
    for res in results:
        assert res["depth"] <= max_depth
