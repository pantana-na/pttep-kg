"""Unit and Property-Based Tests for Orchestrator Agent & Streaming Telemetry (Step 6.0).

Verifies semantic intent classification, HITL clarification cascades, and SSE event streaming.
"""

import pytest
import asyncio
from hypothesis import given, strategies as st
from database.init_db import init_local_mock
from agents.orchestrator.agent import OrchestratorAgent
from agents.orchestrator.clarification_sm import ClarificationManager, MAX_CLARIFICATION_DEPTH


# ==============================================================================
# 1. Deterministic Unit Tests
# ==============================================================================

@pytest.mark.asyncio
async def test_ut_orc_01_hazop_routing():
    """UT-ORC-01: Prompt: 'Run HAZOP on node CDN-N02' -> Routes to HazopStudyAgent."""
    db = init_local_mock("wiki")
    orc = OrchestratorAgent(db)
    
    events = []
    async for ev in orc.stream_orchestration("Run HAZOP review for high temperature deviation"):
        events.append(ev)
        
    event_names = [e["event"] for e in events]
    assert "thought" in event_names
    assert "subagent_dispatch" in event_names
    
    dispatch_event = next(e for e in events if e["event"] == "subagent_dispatch")
    assert dispatch_event["data"]["subagent_name"] == "HazopStudyAgent"


@pytest.mark.asyncio
async def test_ut_orc_clarify_01_ambiguous_query():
    """UT-ORC-CLARIFY-01: Ambiguous query triggers clarification_requested."""
    db = init_local_mock("wiki")
    orc = OrchestratorAgent(db)
    
    events = []
    async for ev in orc.stream_orchestration("show me interlocks on the pump"):
        events.append(ev)
        
    event_names = [e["event"] for e in events]
    assert "clarification_requested" in event_names
    clarify_data = next(e for e in events if e["event"] == "clarification_requested")["data"]
    assert clarify_data["type"] == "CLARIFICATION_REQUESTED"
    assert len(clarify_data["options"]) >= 3


def test_ut_orc_cascade_01_depth_fallback():
    """UT-ORC-CASCADE-01: 3-turn successive cascade triggers matrix fallback at depth > 3."""
    cm = ClarificationManager()
    candidates = [{"tag": "P-2301A/B", "name": "Pump 1"}, {"tag": "P-2303A/B", "name": "Pump 2"}]
    
    # Frame 1
    f1 = cm.create_clarification_request("Select Unit?", candidates, "Unit")
    assert f1["type"] == "CLARIFICATION_REQUESTED"
    assert f1["clarification_depth"] == 1
    
    # Frame 2
    f2 = cm.create_clarification_request("Select Node?", candidates, "Node")
    assert f2["type"] == "CLARIFICATION_REQUESTED"
    assert f2["clarification_depth"] == 2
    
    # Frame 3
    f3 = cm.create_clarification_request("Select Equipment?", candidates, "Equipment")
    assert f3["type"] == "CLARIFICATION_REQUESTED"
    assert f3["clarification_depth"] == 3
    
    # Frame 4 -> Circuit breaker triggers comparative matrix fallback
    f4 = cm.create_clarification_request("Select Interlock Loop?", candidates, "Loop")
    assert f4["type"] == "COMPARATIVE_MATRIX_FALLBACK"
    assert "matrix" in f4
    assert len(f4["matrix"]) == 2


@pytest.mark.asyncio
async def test_ut_stream_01_telemetry_ordering():
    """UT-STREAM-01: Verifies event streaming order (thought -> dispatch -> tool -> gql -> message)."""
    db = init_local_mock("wiki")
    orc = OrchestratorAgent(db)
    
    events = []
    async for ev in orc.stream_orchestration("What protects E-2303 from overheating?"):
        events.append(ev)
        
    names = [e["event"] for e in events]
    assert names[0] == "thought"
    assert "subagent_dispatch" in names
    assert "tool_invoked" in names
    assert "tool_result" in names
    assert "gql_executed" in names
    assert "message_delta" in names
    assert names[-1] == "message_done"


# ==============================================================================
# 2. Property-Based Invariant Tests (Hypothesis)
# ==============================================================================

@given(
    cascade_count=st.integers(min_value=4, max_value=10)
)
def test_pbt_orc_cascade_depth_bound_invariant(cascade_count):
    """PBT-ORC-CASCADE-01: Clarification depth is strictly bounded at <= 3."""
    cm = ClarificationManager()
    candidates = [{"tag": "EQ-1", "name": "Eq 1"}, {"tag": "EQ-2", "name": "Eq 2"}]
    
    final_type = ""
    for i in range(cascade_count):
        res = cm.create_clarification_request(f"Question {i+1}?", candidates, f"Breadcrumb {i+1}")
        final_type = res["type"]
        
    # Must have fallen back to matrix
    assert final_type == "COMPARATIVE_MATRIX_FALLBACK"
    assert len(cm.stack) <= MAX_CLARIFICATION_DEPTH
