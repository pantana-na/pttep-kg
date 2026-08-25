"""Retriever Agent Engine with Tri-Hybrid Search & RRF Fusion.

Executes ISO standard GQL graph traversal, keyword full-text search, and vector search.
SPEC-20260824-MULTI-AGENT-CLOUD-ARCHITECTURE Section 4.1 & 4.2.
"""

import re
import asyncio
from typing import Dict, Any, List, Optional
from mcp_servers.spanner_mcp import SpannerMCPServer
from agents.retriever.rrf_fusion import compute_rrf_scores


class RetrieverAgent:
    def __init__(self, db_instance):
        self.mcp = SpannerMCPServer(db_instance)

    def search_tri_hybrid(self, query: str, limit: int = 5) -> Dict[str, Any]:
        """Executes Tri-Hybrid search with Reciprocal Rank Fusion (RRF)."""
        # 1. Detect if primary equipment tag is present (Direct Parallel Mode vs Pipelined Mode)
        tag_match = re.search(r'\b([A-Z]-[0-9]{4}[A-Z/]*)\b', query)
        target_tag = tag_match.group(1) if tag_match else None

        # Mode 1: Direct Parallel Execution
        keyword_res = self.mcp.spanner_keyword_search(query, limit=10)
        vector_res = self.mcp.spanner_vector_search(query, limit=10)
        
        graph_res = []
        if target_tag:
            # Traversal + Interlocks
            graph_res = self.mcp.spanner_graph_query(target_tag, mode="interlocks")
            if not graph_res:
                graph_res = self.mcp.spanner_graph_query(target_tag, mode="upstream")

        # Combine ranks using RRF (k=60)
        fused_ranked = compute_rrf_scores(keyword_res, vector_res, graph_res)
        top_results = fused_ranked[:limit]

        # Construct synthesised response
        summary_lines = [f"### Tri-Hybrid Process Safety Search Results for: '{query}'"]
        for r in top_results:
            summary_lines.append(f"- **{r.entity_tag}** ({r.name}) — RRF Score: `{r.rrf_score:.4f}`")
            if r.summary:
                summary_lines.append(f"  > {r.summary[:150]}...")

        return {
            "status": "SUCCESS",
            "query": query,
            "detected_tag": target_tag,
            "mode": "DIRECT_PARALLEL" if target_tag else "PIPELINED_RESOLUTION",
            "top_results": [r.model_dump() for r in top_results],
            "formatted_summary": "\n".join(summary_lines)
        }

    def query_safety_interlocks(self, equipment_tag: str) -> Dict[str, Any]:
        """Returns all trip interlocks, SIF logic, and SIL ratings protecting equipment_tag."""
        interlocks = self.mcp.spanner_graph_query(equipment_tag, mode="interlocks")
        return {
            "status": "SUCCESS",
            "equipment_tag": equipment_tag,
            "interlocks": interlocks,
            "count": len(interlocks)
        }
