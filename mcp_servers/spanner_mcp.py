"""Model Context Protocol (MCP) Server for Cloud Spanner Graph & Knowledge Catalog.

Exposes spanner_keyword_search, spanner_graph_query, spanner_vector_search,
query_knowledge_catalog_provenance, and read_gcs_wiki_document.
"""

import os
import re
from pathlib import Path
from typing import List, Dict, Any, Optional
import yaml
import httpx
from database.models import HybridSearchResult
from database.spanner_sync import generate_embedding


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
        query_vec = generate_embedding(query_text)
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

    def _fetch_dataplex_entry(self, entry_id: str) -> Optional[Dict[str, Any]]:
        """Fetches live Dataplex Catalog entry via REST API."""
        if os.getenv("FORCE_OFFLINE_MOCK", "false").lower() in ("true", "1", "yes"):
            return None
        try:
            import google.auth
            from google.auth.transport.requests import Request

            project_id = os.getenv("GCP_PROJECT", "cs-poc-y03r7kmfyov4kilzg50fd7s")
            location = os.getenv("GCP_REGION", "asia-southeast1")
            group = "phenol-psi"

            credentials, _ = google.auth.default(scopes=["https://www.googleapis.com/auth/cloud-platform"])
            if not credentials.valid:
                credentials.refresh(Request())

            url = f"https://dataplex.googleapis.com/v1/projects/{project_id}/locations/{location}/entryGroups/{group}/entries/{entry_id}"
            headers = {
                "Authorization": f"Bearer {credentials.token}",
                "X-Goog-User-Project": project_id
            }
            with httpx.Client(timeout=3.0) as client:
                resp = client.get(url, headers=headers)
                if resp.status_code == 200:
                    return resp.json()
        except Exception as e:
            print(f"[DATAPLEX LIVE LOOKUP NOTICE] {e}")
        return None

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

        # Query live Google Cloud Dataplex entry
        entry_id = re.sub(r'[^a-z0-9-]', '', target_tag.lower().replace('/', '-').replace('_', '-'))
        live_entry = self._fetch_dataplex_entry(entry_id)
        if live_entry:
            source_info = live_entry.get("entrySource", {})
            if source_info.get("updateTime"):
                last_updated = source_info.get("updateTime")[:10]

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
            "dataplex_entry_name": live_entry.get("name") if live_entry else f"projects/cs-poc-y03r7kmfyov4kilzg50fd7s/locations/asia-southeast1/entryGroups/phenol-psi/entries/{entry_id}",
            "dataplex_entry_group": f"projects/cs-poc-y03r7kmfyov4kilzg50fd7s/locations/asia-southeast1/entryGroups/phenol-psi",
            "aspect_types": ["oems_005_process_safety_aspect", "provenance_lineage_aspect"],
            "source_documents": sources,
            "psi_category": "Equipment & Process Data Sheets (PSI Category 4 / P&ID Drawing)",
            "governance_tags": tags,
            "as_built_revision": "Z1 (As-Built Certified)",
            "last_catalog_sync": matching_hazop_entry.get("last_updated", last_updated) if matching_hazop_entry else last_updated,
            "hazop_study_metadata": matching_hazop_entry.get("aspects", {}).get("oems_005_process_safety_aspect") if matching_hazop_entry else None,
            "dataplex_cloud_synced": live_entry is not None
        }

    def read_gcs_wiki_document(self, target_tag_or_path: str) -> Dict[str, Any]:
        """Reads complete Markdown narrative document from GCS LLM-Wiki."""
        bucket_name = os.getenv("GCS_WIKI_BUCKET", f"phenol-llm-wiki-{os.getenv('GCP_PROJECT', 'cs-poc-y03r7kmfyov4kilzg50fd7s')}-prod")

        # 1. Resolve local file path if present
        file_path = None
        eq = self.db.equipment.get(target_tag_or_path)
        if eq and eq.markdown_uri and Path(eq.markdown_uri).exists():
            file_path = Path(eq.markdown_uri)
        else:
            candidates = list(Path("wiki").rglob(f"*{target_tag_or_path}*.md"))
            if candidates:
                file_path = candidates[0]

        # If local file exists, read it directly for speed while retaining exact GCS URI provenance
        if file_path and file_path.exists():
            content = file_path.read_text(encoding="utf-8")
            return {
                "status": "SUCCESS",
                "gcs_uri": f"gs://{bucket_name}/{file_path}",
                "local_path": str(file_path),
                "full_content": content,
                "byte_size": len(content.encode("utf-8"))
            }

        # 2. Attempt direct GCS download from bucket
        try:
            from google.cloud import storage
            client = storage.Client()
            bucket = client.bucket(bucket_name)
            blob_candidates = [
                f"wiki/equipment/{target_tag_or_path}.md",
                f"wiki/instruments/{target_tag_or_path}.md",
                f"wiki/units/{target_tag_or_path}.md",
                f"wiki/hazards/{target_tag_or_path}.md",
                str(target_tag_or_path)
            ]
            for b_name in blob_candidates:
                blob = bucket.blob(b_name)
                if blob.exists():
                    text = blob.download_as_text(encoding="utf-8")
                    return {
                        "status": "SUCCESS",
                        "gcs_uri": f"gs://{bucket_name}/{b_name}",
                        "local_path": "",
                        "full_content": text,
                        "byte_size": len(text.encode("utf-8"))
                    }
        except Exception as e:
            print(f"[GCS READ NOTICE] GCS lookup fallback: {e}")

        return {
            "status": "NOT_FOUND",
            "target": target_tag_or_path,
            "message": f"Document not found in GCS LLM-Wiki for '{target_tag_or_path}'."
        }

