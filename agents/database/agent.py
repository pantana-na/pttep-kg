"""Database Subagent Engine.

Manages ingestion of Markdown files into Cloud Spanner Graph and executes cascading deletions.
"""

from typing import Dict, Any
from agents.database.markdown_parser import MarkdownGraphParser
from agents.database.spanner_sync import SpannerGraphSyncer
from agents.database.cascade_delete import CascadeDeletionEngine


class DatabaseAgent:
    def __init__(self, db_instance):
        self.db = db_instance
        self.parser = MarkdownGraphParser()
        self.syncer = SpannerGraphSyncer(db_instance)
        self.deleter = CascadeDeletionEngine(db_instance)

    def sync_markdown_document(self, content: str, file_uri: str = "") -> Dict[str, Any]:
        """Parses Markdown content and updates Spanner Graph."""
        fm, items = self.parser.parse_markdown_content(content, file_uri)
        count = self.syncer.sync_entities(items)
        return {
            "status": "SUCCESS",
            "file_uri": file_uri,
            "synced_items": count
        }

    def delete_document(self, doc_identifier: str) -> Dict[str, Any]:
        """Cascades deletion across Spanner Graph and updates audit log."""
        return self.deleter.delete_document_cascade(doc_identifier)
