"""Markdown to Spanner Graph Model Parser.

Extracts structured relational entities, flow edges, and instrument interlocks from Markdown files.
"""

import re
import yaml
from pathlib import Path
from typing import Dict, Any, List, Tuple
from database.models import (
    EquipmentModel, UnitModel, InstrumentModel, ChemicalHazardModel,
    EquipmentFlowEdge, InstrumentActuationEdge
)


class MarkdownGraphParser:
    @staticmethod
    def parse_markdown_content(content: str, file_uri: str = "") -> Tuple[Dict[str, Any], List[Any]]:
        frontmatter = {}
        body = content
        if content.startswith("---"):
            parts = content.split("---", 2)
            if len(parts) >= 3:
                try:
                    frontmatter = yaml.safe_load(parts[1]) or {}
                    body = parts[2].strip()
                except Exception:
                    pass

        entities = []
        edges = []

        # 1. Equipment entity
        tag = frontmatter.get("tag", frontmatter.get("equipment_tag"))
        if tag:
            eq = EquipmentModel(
                equipment_tag=tag,
                unit_id=frontmatter.get("unit", "CDN"),
                name=frontmatter.get("name", tag),
                type=str(frontmatter.get("type", "Equipment"))[:64],
                markdown_uri=file_uri,
                description_summary=body[:300] if body else None
            )
            entities.append(eq)

        # 2. Connection tables & flows
        for line in body.splitlines():
            # Line connection: From A to B
            flow_match = re.search(r'([A-Z]-[0-9]{4}[A-Z/]*)\s*(?:->|to|feeds)\s*([A-Z]-[0-9]{4}[A-Z/]*)', line, re.IGNORECASE)
            if flow_match:
                src, dst = flow_match.group(1), flow_match.group(2)
                edges.append(EquipmentFlowEdge(
                    from_equipment_tag=src,
                    to_equipment_tag=dst,
                    stream_id=f"S-{src}->{dst}"
                ))

            # Instrument loops: | TXSHH-0502A | SIS Temp HH | UC-2301 |
            inst_match = re.search(r'\|\s*([A-Z]{2,5}-[0-9]{4}[A-Z]?)\s*\|\s*([^\|]+)\|\s*([^\|]+)\|', line)
            if inst_match and tag:
                itag = inst_match.group(1).strip()
                itype = inst_match.group(2).strip()
                iaction = inst_match.group(3).strip()
                is_sis = "SIS" in itype or "ESD" in iaction or "SIL" in iaction
                sil = "SIL 1" if "SIL 1" in iaction or "SIL 1" in itype else ("SIL 2" if "SIL 2" in iaction else "None")
                inst = InstrumentModel(
                    instrument_tag=itag,
                    equipment_tag=tag,
                    type=itype[:64],
                    sil_rating=sil,
                    is_sis_initiator=is_sis
                )
                entities.append(inst)
                if is_sis:
                    edges.append(InstrumentActuationEdge(
                        initiator_instrument_tag=itag,
                        target_equipment_tag=tag,
                        interlock_action=iaction[:64]
                    ))

        return frontmatter, entities + edges
