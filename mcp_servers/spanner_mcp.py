"""Model Context Protocol (MCP) Server for Cloud Spanner Graph & Tri-Hybrid Search.

Exposes spanner_keyword_search, spanner_graph_query, and spanner_vector_search.
"""

from typing import List, Dict, Any, Optional
from database.models import HybridSearchResult
from agents.database.spanner_sync import generate_pseudo_embedding


class SpannerMCPServer:
    def __init__(self, db_instance):
        self.db = db_instance

    def spanner_keyword_search(self, query_string: str, limit: int = 10) -> List[Dict[str, Any]]:
        """Executes full-text keyword search across EquipmentTokens and InstrumentTokens."""
        raw_results = self.db.keyword_search(query_string, limit=limit)
        formatted = []
        for tag, score, eq in raw_results:
            formatted.append({
                "tag": tag,
                "name": eq.name,
                "type": eq.type,
                "score": score,
                "summary": eq.description_summary or "",
                "markdown_uri": eq.markdown_uri or ""
            })
        return formatted

    def spanner_graph_query(self, target_tag: str, mode: str = "upstream", max_depth: int = 3) -> List[Dict[str, Any]]:
        """Executes ISO standard GQL graph traversal on PhenolProcessSafetyGraph."""
        if mode == "interlocks":
            return self.db.graph_find_interlocks(target_tag)
        else:
            return self.db.graph_traverse_upstream(target_tag, max_depth=max_depth)

    def spanner_vector_search(self, query_text: str, limit: int = 10) -> List[Dict[str, Any]]:
        """Executes vector cosine similarity search on 768-dim embeddings."""
        query_vec = generate_pseudo_embedding(query_text)
        raw_results = self.db.vector_search(query_vec, limit=limit)
        formatted = []
        for tag, sim, eq in raw_results:
            formatted.append({
                "tag": tag,
                "name": eq.name,
                "type": eq.type,
                "similarity": sim,
                "summary": eq.description_summary or "",
                "markdown_uri": eq.markdown_uri or ""
            })
        return formatted
