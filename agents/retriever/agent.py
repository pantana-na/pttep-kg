"""Retriever Agent Engine with Tri-Hybrid Search, Knowledge Catalog & GCS LLM-Wiki Reading.

Executes ISO standard GQL graph traversal, keyword search, vector search, Dataplex provenance, and GCS reading.
SPEC-20260824-MULTI-AGENT-CLOUD-ARCHITECTURE Section 4.1 & 4.2.
"""

import re
from typing import Dict, Any, List, Optional
from mcp_servers.spanner_mcp import SpannerMCPServer
from agents.retriever.rrf_fusion import compute_rrf_scores


class RetrieverAgent:
    def __init__(self, db_instance):
        self.db = db_instance
        self.mcp = SpannerMCPServer(db_instance)

    def search_tri_hybrid(self, query: str, limit: int = 5) -> Dict[str, Any]:
        """Executes Tri-Hybrid search, Knowledge Catalog queries, and GCS LLM-Wiki reading."""
        tag_match = re.search(r'\b([A-Z]-[0-9]{4}[A-Z/]*)\b', query)
        target_tag = tag_match.group(1) if tag_match else None
        q_lower = query.lower()

        # Check if query is asking for Knowledge Catalog / Provenance / Drawing Lineage
        if target_tag and any(k in q_lower for k in ["lineage", "provenance", "source", "drawing", "catalog", "pdf", "revision", "dataplex"]):
            prov = self.mcp.query_knowledge_catalog_provenance(target_tag)
            if prov["status"] == "FOUND":
                sources_str = ", ".join(f"`{s}`" for s in prov["source_documents"])
                summary_lines = [
                    f"### 📋 Dataplex Knowledge Catalog & Provenance Lineage: **{target_tag}**",
                    f"- **Equipment:** {prov['entity_name']}",
                    f"- **PSI Category:** {prov['psi_category']}",
                    f"- **Source Engineering Documents:** {sources_str}",
                    f"- **As-Built Revision Status:** `{prov['as_built_revision']}`",
                    f"- **Dataplex Entry Group:** `{prov['dataplex_entry_group']}`",
                    f"- **Catalog Governance Tags:** {', '.join(f'`{t}`' for t in prov['governance_tags'])}",
                    f"- **Last Verified Ingestion Date:** {prov['last_catalog_sync']}"
                ]
                return {
                    "status": "SUCCESS",
                    "query": query,
                    "detected_tag": target_tag,
                    "mode": "KNOWLEDGE_CATALOG_QUERY",
                    "provenance": prov,
                    "top_results": [],
                    "formatted_summary": "\n".join(summary_lines)
                }

        # Check if query is asking to read full GCS LLM-Wiki narrative or operating procedure
        if target_tag and any(k in q_lower for k in ["read", "procedure", "narrative", "full text", "wiki", "manual", "description", "details"]):
            doc = self.mcp.read_gcs_wiki_document(target_tag)
            if doc["status"] == "SUCCESS":
                summary_lines = [
                    f"### 📖 GCS LLM-Wiki Document Reader: **{target_tag}**",
                    f"**GCS URI:** `{doc['gcs_uri']}` ({doc['byte_size']} bytes)\n",
                    doc["full_content"]
                ]
                return {
                    "status": "SUCCESS",
                    "query": query,
                    "detected_tag": target_tag,
                    "mode": "GCS_WIKI_READING",
                    "wiki_doc": doc,
                    "top_results": [],
                    "formatted_summary": "\n".join(summary_lines)
                }

        # Standard Tri-Hybrid Search
        keyword_res = self.mcp.spanner_keyword_search(query, limit=10)
        vector_res = self.mcp.spanner_vector_search(query, limit=10)
        
        graph_res = []
        interlock_details = []
        if target_tag:
            interlock_details = self.mcp.spanner_graph_query(target_tag, mode="interlocks")
            graph_res = interlock_details if interlock_details else self.mcp.spanner_graph_query(target_tag, mode="upstream")

        fused_ranked = compute_rrf_scores(keyword_res, vector_res, graph_res)
        top_results = fused_ranked[:limit]

        summary_lines = [f"### Tri-Hybrid Process Safety Search Results for: '{query}'"]
        
        if "chp" in q_lower or "hydroperoxide" in q_lower or "decomposition" in q_lower:
            for h_id, haz in self.db.chemical_hazards.items():
                if "chp" in h_id.lower() or "cumene" in haz.chemical_name.lower():
                    summary_lines.append(f"- **Chemical Hazard ({haz.chemical_name}):** Decomposition onset temperature is **{haz.decomposition_onset_temp_celsius}°C**.")

        for r in top_results:
            summary_lines.append(f"- **{r.entity_tag}** ({r.name}) — RRF Score: `{r.rrf_score:.4f}`")
            if r.summary:
                summary_lines.append(f"  > {r.summary[:200]}...")

        if interlock_details:
            summary_lines.append("\n**Active SIS Interlocks & Trips:**")
            for inst in interlock_details:
                summary_lines.append(
                    f"- `{inst['instrument_tag']}` ({inst['type']}) — SIL Rating: **{inst['sil_rating']}**, Action: {inst['interlock_action']}"
                )

        return {
            "status": "SUCCESS",
            "query": query,
            "detected_tag": target_tag,
            "mode": "DIRECT_PARALLEL" if target_tag else "PIPELINED_RESOLUTION",
            "top_results": [r.model_dump() for r in top_results],
            "interlocks": interlock_details,
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
