"""Cascading Document Deletion & Graph Tombstoning Engine."""

import datetime
from pathlib import Path
from typing import Dict, Any, List


class CascadeDeletionEngine:
    def __init__(self, db_instance, log_file: str = "wiki/log.md"):
        self.db = db_instance
        self.log_file = Path(log_file)

    def delete_document_cascade(self, doc_identifier: str) -> Dict[str, Any]:
        """Tombstones equipment/instruments associated with doc_identifier and severs edges."""
        dropped_equipment = []
        dropped_instruments = []
        dropped_edges = 0

        # 1. Identify and tombstone equipment referencing this doc
        for tag, eq in list(self.db.equipment.items()):
            if doc_identifier.lower() in (eq.markdown_uri or "").lower() or doc_identifier.lower() in eq.equipment_tag.lower():
                eq.is_deleted = True
                dropped_equipment.append(tag)

        # 2. Identify and drop instruments associated with dropped equipment
        for itag, inst in list(self.db.instruments.items()):
            if inst.equipment_tag in dropped_equipment:
                inst.is_deleted = True
                dropped_instruments.append(itag)

        # 3. Sever dangling flow edges
        initial_flows = len(self.db.equipment_flows)
        self.db.equipment_flows = [
            e for e in self.db.equipment_flows
            if e.from_equipment_tag not in dropped_equipment and e.to_equipment_tag not in dropped_equipment
        ]
        dropped_edges += initial_flows - len(self.db.equipment_flows)

        # 4. Sever dangling instrument actuation edges
        initial_acts = len(self.db.instrument_actuations)
        self.db.instrument_actuations = [
            a for a in self.db.instrument_actuations
            if a.initiator_instrument_tag not in dropped_instruments and a.target_equipment_tag not in dropped_equipment
        ]
        dropped_edges += initial_acts - len(self.db.instrument_actuations)

        # 5. Append to audit log
        log_entry = (
            f"\n## [{datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')}] Document Deletion: {doc_identifier}\n"
            f"- **Tombstoned Equipment:** {', '.join(dropped_equipment) if dropped_equipment else 'None'}\n"
            f"- **Tombstoned Instruments:** {', '.join(dropped_instruments) if dropped_instruments else 'None'}\n"
            f"- **Severed Graph Edges:** {dropped_edges}\n"
        )
        if self.log_file.parent.exists():
            with open(self.log_file, "a", encoding="utf-8") as f:
                f.write(log_entry)

        return {
            "status": "SUCCESS",
            "document": doc_identifier,
            "dropped_equipment": dropped_equipment,
            "dropped_instruments": dropped_instruments,
            "severed_edges": dropped_edges
        }
