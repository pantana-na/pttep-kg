"""Unit and Property-Based Tests for Consolidated Single Orchestrator Agent (SPEC-20260918-CONSOLIDATED-SINGLE-ORCHESTRATOR).

Validates:
1. Root OrchestratorAgent hierarchy, configuration, and tools.
2. ORCHESTRATOR_INSTRUCTION domain invariants and tool selection protocols.
3. Direct execution of all 6 process safety and HAZOP tools.
4. Generative Property-Based Tests (Hypothesis PBT) across tool inputs.
"""

import json
import pytest
from hypothesis import given, settings, strategies as st
from google.adk.agents import Agent
from app.agent import (
    root_agent,
    ORCHESTRATOR_INSTRUCTION,
    spanner_graph_query,
    spanner_keyword_search,
    spanner_vector_search,
    query_knowledge_catalog_provenance,
    read_gcs_wiki_document,
    evaluate_hazop_deviation,
    before_agent_guardrail,
)


# ==============================================================================
# 1. Deterministic Unit Tests
# ==============================================================================

def test_ut_orc_01_root_agent_structure():
    """UT-ORC-01: Verifies single root OrchestratorAgent with zero subagents and all 6 tools."""
    assert isinstance(root_agent, Agent)
    assert root_agent.name == "OrchestratorAgent"
    assert root_agent.sub_agents == []
    assert len(root_agent.sub_agents) == 0

    tool_names = [t.__name__ for t in root_agent.tools]
    assert len(tool_names) == 6
    expected_tools = [
        "spanner_graph_query",
        "spanner_keyword_search",
        "spanner_vector_search",
        "query_knowledge_catalog_provenance",
        "read_gcs_wiki_document",
        "evaluate_hazop_deviation",
    ]
    for tool_name in expected_tools:
        assert tool_name in tool_names


def test_ut_orc_02_instruction_standards_and_protocols():
    """UT-ORC-02: Verifies instruction contains explicit guidelines for all 6 tools and safety thresholds."""
    inst = ORCHESTRATOR_INSTRUCTION
    # Verify all 6 tools have documented invocation protocols
    assert "spanner_graph_query" in inst
    assert "spanner_keyword_search" in inst
    assert "spanner_vector_search" in inst
    assert "query_knowledge_catalog_provenance" in inst
    assert "read_gcs_wiki_document" in inst
    assert "evaluate_hazop_deviation" in inst

    # Process Safety Governance: Instruction mandates grounding on retrieved tool data
    assert "Ground all chemical safety limits" in inst
    assert "retrieved from tools" in inst

    # Voting logic guideline
    assert "1oo2" in inst


def test_ut_orc_03_hazop_deviation_evaluation():
    """UT-ORC-03: Verifies direct invocation of evaluate_hazop_deviation."""
    raw = evaluate_hazop_deviation(
        node_id="CDN-N02",
        parameter="Flow",
        deviation="Flow — No / Low Flow",
        cause="P-2301A/B pump trip on V-2302 bottoms suction",
    )
    res = json.loads(raw)
    assert "first_risk" in res
    assert "second_risk" in res
    assert res["first_risk"]["severity"] == 5
    assert res["first_risk"]["likelihood"] == 4
    assert res["first_risk"]["risk_rating"] == "Extreme"
    assert res["second_risk"]["mitigated_likelihood"] <= res["first_risk"]["likelihood"]
    assert res["second_risk"]["total_ipl_credits"] >= 1


def test_ut_orc_04_spanner_graph_interlocks_and_upstream():
    """UT-ORC-04: Verifies direct invocation of spanner_graph_query for interlocks and upstream."""
    raw_interlocks = spanner_graph_query("E-2303", mode="interlocks")
    interlocks = json.loads(raw_interlocks)
    assert isinstance(interlocks, list)
    assert len(interlocks) > 0
    assert any("TXSHH" in item.get("instrument_tag", "") for item in interlocks)
    assert any("1oo2" in item.get("interlock_action", "") or "UC-2301" in item.get("interlock_action", "") for item in interlocks)

    raw_upstream = spanner_graph_query("V-2301", mode="upstream")
    upstream = json.loads(raw_upstream)
    assert isinstance(upstream, list)
    assert len(upstream) > 0


def test_ut_orc_05_provenance_and_wiki_retrieval():
    """UT-ORC-05: Verifies direct invocation of query_knowledge_catalog_provenance and read_gcs_wiki_document."""
    raw_prov = query_knowledge_catalog_provenance("E-2303")
    prov = json.loads(raw_prov)
    assert prov["status"] == "FOUND"
    assert len(prov["source_documents"]) > 0
    assert "Z1" in prov["as_built_revision"]

    raw_wiki = read_gcs_wiki_document("E-2303")
    wiki = json.loads(raw_wiki)
    assert wiki["status"] == "SUCCESS"
    assert "Preflash Column Steam Heater" in wiki["full_content"]
    assert "80.0°C" in wiki["full_content"] or "80" in wiki["full_content"]


def test_ut_orc_06_keyword_and_vector_search():
    """UT-ORC-06: Verifies direct invocation of spanner_keyword_search and spanner_vector_search."""
    raw_kw = spanner_keyword_search("cumene hydroperoxide", limit=5)
    kw = json.loads(raw_kw)
    assert isinstance(kw, list)
    assert len(kw) > 0

    raw_vec = spanner_vector_search("thermal runaway risks", limit=5)
    vec = json.loads(raw_vec)
    assert isinstance(vec, list)
    assert len(vec) > 0


def test_ut_orc_07_ambiguity_clarification_instruction():
    """UT-ORC-07: Verifies prompt instruction mandates human-in-the-loop clarification on ambiguous queries."""
    inst = ORCHESTRATOR_INSTRUCTION
    assert "AMBIGUITY RESOLUTION & HUMAN-IN-THE-LOOP (HITL) CLARIFICATION MANDATE" in inst
    assert "clarification_requested" in inst
    assert "spanner_keyword_search" in inst
    assert "HALT further tool execution" in inst

    # Verify that searching for generic token 'pump' produces multiple candidates
    raw_kw = spanner_keyword_search("pump", limit=10)
    candidates = json.loads(raw_kw)
    assert isinstance(candidates, list)
    assert len(candidates) > 1
    tags = [c.get("tag") for c in candidates if isinstance(c, dict)]
    assert "P-2301A/B" in tags or any("P-" in t for t in tags)


# ==============================================================================
# 2. Property-Based Invariant Tests (Hypothesis)
# ==============================================================================

@settings(deadline=None, max_examples=10)
@given(
    target_tag=st.sampled_from(["E-2301", "E-2302", "E-2303", "V-2301", "P-2301A/B", "NON-EXISTENT-999"])
)
def test_pbt_orc_provenance_always_valid_json(target_tag):
    """PBT-ORC-PROV-01: Provenance lookup always returns valid JSON with required status field."""
    raw = query_knowledge_catalog_provenance(target_tag)
    res = json.loads(raw)
    assert "status" in res
    assert res["status"] in ("FOUND", "NOT_FOUND")


@settings(deadline=None, max_examples=10)
@given(
    cause=st.text(min_size=2, max_size=60),
    parameter=st.sampled_from(["Flow", "Temperature", "Pressure", "Level"])
)
def test_pbt_orc_hazop_mitigated_monotonicity(cause, parameter):
    """PBT-ORC-HAZOP-01: Invariant: Mitigated likelihood is always <= initial likelihood."""
    raw = evaluate_hazop_deviation(
        node_id="CDN-N02",
        parameter=parameter,
        deviation=f"{parameter} — High Deviation",
        cause=cause
    )
    res = json.loads(raw)
    assert res["second_risk"]["mitigated_likelihood"] <= res["first_risk"]["likelihood"]
