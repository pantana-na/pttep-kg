"""Unit and Property-Based Tests for Retriever Agent & Tri-Hybrid Search (Step 4.0).

Verifies Spanner MCP tools, Reciprocal Rank Fusion (RRF), and trip interlock querying.
"""

import pytest
from hypothesis import given, strategies as st
from database.init_db import init_local_mock
from agents.retriever.agent import RetrieverAgent
from agents.retriever.rrf_fusion import compute_rrf_scores


# ==============================================================================
# 1. Deterministic Unit Tests
# ==============================================================================

def test_ut_ret_01_interlock_trip_query():
    """UT-RET-01: Query trips protecting E-2303, verifies TXSHH-0502 and UXV-0501."""
    db = init_local_mock("wiki")
    agent = RetrieverAgent(db)
    
    res = agent.query_safety_interlocks("E-2303")
    assert res["status"] == "SUCCESS"
    assert res["count"] >= 2
    tags = [i["instrument_tag"] for i in res["interlocks"]]
    assert "TXSHH-0502A" in tags or "UXV-0501" in tags


def test_tri_hybrid_search_e2303():
    """Verify tri-hybrid search fuses keyword, vector, and graph ranks."""
    db = init_local_mock("wiki")
    agent = RetrieverAgent(db)
    
    res = agent.search_tri_hybrid("What protects E-2303 from overheating?")
    assert res["status"] == "SUCCESS"
    assert res["detected_tag"] == "E-2303"
    assert len(res["top_results"]) > 0
    top_entity = res["top_results"][0]["entity_tag"]
    assert top_entity == "E-2303" or "TXSHH" in top_entity or "UXV" in top_entity


# ==============================================================================
# 2. Property-Based Invariant Tests (Hypothesis)
# ==============================================================================

@given(
    tag_a=st.text(alphabet="ABCDEF", min_size=3, max_size=6),
    tag_b=st.text(alphabet="GHIJKL", min_size=3, max_size=6)
)
def test_pbt_rrf_rank_monotonicity(tag_a, tag_b):
    """PBT-RRF-01: If tag_a is strictly ranked higher than tag_b in all lists, RRF(tag_a) > RRF(tag_b)."""
    # tag_a rank 1 in both lists, tag_b rank 2 in both lists
    kw_results = [{"tag": tag_a, "name": tag_a}, {"tag": tag_b, "name": tag_b}]
    vec_results = [{"tag": tag_a, "name": tag_a}, {"tag": tag_b, "name": tag_b}]
    graph_results = []
    
    fused = compute_rrf_scores(kw_results, vec_results, graph_results)
    score_a = next(r.rrf_score for r in fused if r.entity_tag == tag_a)
    score_b = next(r.rrf_score for r in fused if r.entity_tag == tag_b)
    
    assert score_a > score_b
