"""Cloud Spanner Graph Ingestion & Synchronization Engine."""

import hashlib
from typing import List, Any
from database.models import (
    EquipmentModel, UnitModel, InstrumentModel, ChemicalHazardModel,
    EquipmentFlowEdge, InstrumentActuationEdge
)


def generate_pseudo_embedding(text: str, dim: int = 768) -> List[float]:
    """Generates a deterministic 768-dim pseudo-embedding for testing when offline."""
    hasher = hashlib.sha256(text.encode("utf-8"))
    digest = hasher.digest()
    vec = []
    for i in range(dim):
        byte_val = digest[i % len(digest)]
        val = (byte_val / 255.0) * 2.0 - 1.0
        vec.append(val)
    # Normalize vector to unit length
    norm = sum(x * x for x in vec) ** 0.5
    return [x / norm for x in vec] if norm > 0 else vec


class SpannerGraphSyncer:
    def __init__(self, db_instance=None):
        self.db = db_instance

    def sync_entities(self, items: List[Any]) -> int:
        """Inserts or updates entities and edges in Cloud Spanner / Mock Graph."""
        count = 0
        if not self.db:
            return count

        for item in items:
            if isinstance(item, EquipmentModel):
                if not item.embedding and item.name:
                    item.embedding = generate_pseudo_embedding(f"{item.equipment_tag} {item.name} {item.description_summary or ''}")
                self.db.equipment[item.equipment_tag] = item
                count += 1
            elif isinstance(item, InstrumentModel):
                self.db.instruments[item.instrument_tag] = item
                count += 1
            elif isinstance(item, UnitModel):
                self.db.units[item.unit_id] = item
                count += 1
            elif isinstance(item, ChemicalHazardModel):
                self.db.chemical_hazards[item.hazard_id] = item
                count += 1
            elif isinstance(item, EquipmentFlowEdge):
                # Avoid duplicate edges
                if not any(e.from_equipment_tag == item.from_equipment_tag and e.to_equipment_tag == item.to_equipment_tag for e in self.db.equipment_flows):
                    self.db.equipment_flows.append(item)
                    count += 1
            elif isinstance(item, InstrumentActuationEdge):
                if not any(e.initiator_instrument_tag == item.initiator_instrument_tag and e.target_equipment_tag == item.target_equipment_tag for e in self.db.instrument_actuations):
                    self.db.instrument_actuations.append(item)
                    count += 1
        return count
