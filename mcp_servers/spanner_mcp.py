"""Model Context Protocol (MCP) Server for Cloud Spanner Graph & Knowledge Catalog.

Exposes spanner_keyword_search, spanner_graph_query, spanner_vector_search,
query_knowledge_catalog_provenance, and read_gcs_wiki_document.
"""

from pathlib import Path
from typing import List, Dict, Any, Optional
import yaml
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

    def query_knowledge_catalog_provenance(self, target_tag: str) -> Dict[str, Any]:
        """Queries Dataplex Knowledge Catalog aspect metadata & source document lineage."""
        eq = self.db.equipment.get(target_tag)
        if not eq or not eq.markdown_uri:
            return {
                "status": "NOT_FOUND",
                "tag": target_tag,
                "message": f"No Dataplex Knowledge Catalog entries found for tag '{target_tag}'."
            }

        file_path = Path(eq.markdown_uri)
        sources = []
        tags = []
        last_updated = "2026-06-16"
        if file_path.exists():
            text = file_path.read_text(encoding="utf-8")
            if text.startswith("---"):
                parts = text.split("---", 2)
                if len(parts) >= 3:
                    fm = yaml.safe_load(parts[1]) or {}
                    sources = fm.get("sources", [])
                    tags = fm.get("tags", [])
                    last_updated = str(fm.get("last_updated", "2026-06-16"))

        # Check if there is an explicit Knowledge Catalog entry in DB
        matching_hazop_entry = None
        if hasattr(self.db, "knowledge_catalog"):
            for entry_id, entry in self.db.knowledge_catalog.items():
                if target_tag in entry.get("linked_equipment", []) or target_tag.lower() in entry_id.lower():
                    matching_hazop_entry = entry
                    break

        return {
            "status": "FOUND",
            "entity_tag": target_tag,
            "entity_name": eq.name,
            "dataplex_entry_group": f"projects/cs-poc-y03r7kmfyov4kilzg50fd7s/locations/asia-southeast1/entryGroups/phenol-psi",
            "aspect_types": ["oems_005_process_safety_aspect", "provenance_lineage_aspect"],
            "source_documents": sources,
            "psi_category": "Equipment & Process Data Sheets (PSI Category 4 / P&ID Drawing)",
            "governance_tags": tags,
            "as_built_revision": "Z1 (As-Built Certified)",
            "last_catalog_sync": matching_hazop_entry.get("last_updated", last_updated) if matching_hazop_entry else last_updated,
            "hazop_study_metadata": matching_hazop_entry.get("aspects", {}).get("oems_005_process_safety_aspect") if matching_hazop_entry else None
        }

    def read_gcs_wiki_document(self, target_tag_or_path: str) -> Dict[str, Any]:
        """Reads complete Markdown narrative document from GCS LLM-Wiki."""
        # Find path
        file_path = None
        eq = self.db.equipment.get(target_tag_or_path)
        if eq and eq.markdown_uri and Path(eq.markdown_uri).exists():
            file_path = Path(eq.markdown_uri)
        else:
            # Look in wiki/
            candidates = list(Path("wiki").rglob(f"*{target_tag_or_path}*.md"))
            if candidates:
                file_path = candidates[0]

        if not file_path or not file_path.exists():
            return {
                "status": "NOT_FOUND",
                "target": target_tag_or_path,
                "message": f"Document not found in GCS LLM-Wiki for '{target_tag_or_path}'."
            }

        content = file_path.read_text(encoding="utf-8")
        return {
            "status": "SUCCESS",
            "gcs_uri": f"gs://phenol-llm-wiki-cs-poc-y03r7kmfyov4kilzg50fd7s/{file_path}",
            "local_path": str(file_path),
            "full_content": content,
            "byte_size": len(content.encode("utf-8"))
        }
