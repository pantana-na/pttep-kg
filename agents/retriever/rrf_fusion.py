"""Reciprocal Rank Fusion (RRF) Ranking Engine for Tri-Hybrid Search.

Formula: RRF(d) = SUM_{m in M} (1 / (k + rank_m(d))), with k = 60.
SPEC-20260824-MULTI-AGENT-CLOUD-ARCHITECTURE Section 4.1.
"""

from typing import List, Dict, Any
from database.models import HybridSearchResult

RRF_K = 60


def compute_rrf_scores(
    keyword_results: List[Dict[str, Any]],
    vector_results: List[Dict[str, Any]],
    graph_results: List[Dict[str, Any]]
) -> List[HybridSearchResult]:
    """Combines Keyword, Vector, and Graph search ranks using Reciprocal Rank Fusion (k=60)."""
    scores: Dict[str, float] = {}
    details: Dict[str, Dict[str, Any]] = {}

    # 1. Score Keyword Results
    for rank, item in enumerate(keyword_results, start=1):
        tag = item.get("tag") or item.get("upstream_tag") or item.get("instrument_tag")
        if not tag:
            continue
        scores[tag] = scores.get(tag, 0.0) + (1.0 / (RRF_K + rank))
        if tag not in details:
            details[tag] = item

    # 2. Score Vector Results
    for rank, item in enumerate(vector_results, start=1):
        tag = item.get("tag") or item.get("upstream_tag") or item.get("instrument_tag")
        if not tag:
            continue
        scores[tag] = scores.get(tag, 0.0) + (1.0 / (RRF_K + rank))
        if tag not in details:
            details[tag] = item

    # 3. Score Graph Results
    for rank, item in enumerate(graph_results, start=1):
        tag = item.get("tag") or item.get("upstream_tag") or item.get("instrument_tag")
        if not tag:
            continue
        scores[tag] = scores.get(tag, 0.0) + (1.0 / (RRF_K + rank))
        if tag not in details:
            details[tag] = item

    # Sort descending by fused RRF score
    sorted_tags = sorted(scores.keys(), key=lambda t: scores[t], reverse=True)

    results: List[HybridSearchResult] = []
    for tag in sorted_tags:
        item = details[tag]
        results.append(HybridSearchResult(
            entity_tag=tag,
            entity_type=item.get("type", "Equipment"),
            name=item.get("name", item.get("equipment_name", tag)),
            rrf_score=scores[tag],
            summary=item.get("summary", item.get("interlock_action", "")),
            metadata=item
        ))
    return results
