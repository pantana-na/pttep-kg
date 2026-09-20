"""In-memory Cloud Spanner Property Graph & Relational Mock for fast deterministic local testing.

Implements GQL graph traversal, keyword token search, vector distance scoring, and wiki markdown table parsing.
"""

import os
import re
import math
import yaml
from pathlib import Path
from typing import List, Dict, Any, Optional, Tuple
from database.models import (
    UnitModel, EquipmentModel, StreamModel, InstrumentModel,
    ChemicalHazardModel, HazopNodeModel, DeviationModel, CauseModel,
    ConsequenceModel, SafeguardModel, ActionItemModel,
    EquipmentFlowEdge, NodeEquipmentEdge, InstrumentActuationEdge,
    HybridSearchResult
)


def cosine_similarity(v1: List[float], v2: List[float]) -> float:
    if not v1 or not v2 or len(v1) != len(v2):
        return 0.0
    dot = sum(a * b for a, b in zip(v1, v2))
    sum_sq1 = sum(a * a for a in v1)
    sum_sq2 = sum(b * b for b in v2)
    if sum_sq1 <= 1e-20 or sum_sq2 <= 1e-20:
        return 0.0
    norm1 = math.sqrt(sum_sq1)
    norm2 = math.sqrt(sum_sq2)
    if norm1 == 0.0 or norm2 == 0.0:
        return 0.0
    res = dot / (norm1 * norm2)
    return max(-1.0, min(1.0, res))


def resolve_equipment_tag_alias(tag: str, known_tags: set) -> str:
    """Resolves compound tag variations (e.g. P-2301A -> P-2301A/B, E-2302B -> E-2302A/B)."""
    if not tag:
        return ""
    clean = tag.strip().upper()
    if clean in known_tags:
        return clean
    for k in known_tags:
        k_clean = k.replace("/", "")
        if clean == k_clean:
            return k
        if "/" in k:
            parts = k.split("/")
            prefix = parts[0]
            if clean == prefix or clean == prefix[:-1]:
                return k
            base = prefix[:-1] if prefix[-1].isalpha() else prefix
            if any(clean == f"{base}{s}" for s in [prefix[-1]] + parts[1:]):
                return k
            if clean.startswith(base):
                return k
    return clean


class MockSpannerDatabase:
    def __init__(self):
        # Relational Tables
        self.units: Dict[str, UnitModel] = {}
        self.equipment: Dict[str, EquipmentModel] = {}
        self.streams: Dict[str, StreamModel] = {}
        self.instruments: Dict[str, InstrumentModel] = {}
        self.chemical_hazards: Dict[str, ChemicalHazardModel] = {}
        self.hazop_nodes: Dict[str, HazopNodeModel] = {}
        self.deviations: Dict[str, DeviationModel] = {}
        self.causes: Dict[str, CauseModel] = {}
        self.consequences: Dict[str, ConsequenceModel] = {}
        self.safeguards: Dict[str, SafeguardModel] = {}
        self.action_items: Dict[str, ActionItemModel] = {}
        self.knowledge_catalog: Dict[str, Any] = {}

        # Edges
        self.equipment_flows: List[EquipmentFlowEdge] = []
        self.node_equipment_map: List[NodeEquipmentEdge] = []
        self.instrument_actuations: List[InstrumentActuationEdge] = []

    def clear(self):
        self.__init__()

    def register_knowledge_catalog_entry(self, entry_id: str, entry_data: Dict[str, Any]) -> Dict[str, Any]:
        """Registers or updates a Dataplex Knowledge Catalog entry and aspect metadata."""
        self.knowledge_catalog[entry_id] = entry_data
        return entry_data

    def get_knowledge_catalog_entry(self, entry_id: str) -> Optional[Dict[str, Any]]:
        """Retrieves Dataplex Knowledge Catalog entry by entry ID."""
        return self.knowledge_catalog.get(entry_id)

    # --- Ingestion & Seeding from Local Wiki ---
    def seed_from_wiki(self, wiki_dir: str):
        wiki_path = Path(wiki_dir)
        if not wiki_path.exists():
            return

        # 1. Ingest Units
        units_dir = wiki_path / "units"
        if units_dir.exists():
            for f in units_dir.glob("*.md"):
                self._parse_unit_file(f)

        # 2. Ingest Equipment & Connections
        equip_dir = wiki_path / "equipment"
        if equip_dir.exists():
            for f in equip_dir.glob("*.md"):
                self._parse_equipment_file(f)

        # 3. Ingest Instruments
        inst_dir = wiki_path / "instruments"
        if inst_dir.exists():
            for f in inst_dir.glob("*.md"):
                self._parse_instrument_file(f)

        # 4. Ingest Hazards
        hazards_dir = wiki_path / "hazards"
        if hazards_dir.exists():
            for f in hazards_dir.glob("*.md"):
                self._parse_hazard_file(f)

    def _extract_frontmatter(self, file_path: Path) -> Tuple[Dict[str, Any], str]:
        text = file_path.read_text(encoding="utf-8")
        if text.startswith("---"):
            parts = text.split("---", 2)
            if len(parts) >= 3:
                try:
                    fm = yaml.safe_load(parts[1]) or {}
                    return fm, parts[2].strip()
                except Exception:
                    pass
        return {}, text

    def _parse_unit_file(self, file_path: Path):
        fm, body = self._extract_frontmatter(file_path)
        unit_id = fm.get("unit_id", file_path.stem.upper())
        self.units[unit_id] = UnitModel(
            unit_id=unit_id,
            name=fm.get("name", file_path.stem),
            code=fm.get("code", "CDN"),
            description=body[:200] if body else None,
            sources=fm.get("sources", [])
        )

    def _parse_equipment_file(self, file_path: Path):
        fm, body = self._extract_frontmatter(file_path)
        tag = fm.get("tag", fm.get("equipment_tag", file_path.stem.upper()))
        unit_id = fm.get("unit", fm.get("unit_id", "U-2300"))
        name = fm.get("name", tag)
        eq_type = str(fm.get("type", "Equipment"))
        
        oper = fm.get("operating", {}) if isinstance(fm.get("operating"), dict) else {}
        design = fm.get("design", {}) if isinstance(fm.get("design"), dict) else {}
        
        eq = EquipmentModel(
            equipment_tag=tag,
            unit_id=unit_id,
            name=name,
            type=eq_type[:64],
            operating_temp_celsius=oper.get("temp_c"),
            operating_pressure_barg=oper.get("pressure_barg"),
            design_temp_celsius=design.get("temp_c"),
            design_pressure_barg=design.get("pressure_barg"),
            material=fm.get("material"),
            markdown_uri=str(file_path),
            description_summary=body[:300] if body else None
        )
        self.equipment[tag] = eq

        # Parse wikilinks for upstream/downstream connections in body
        for line in body.splitlines():
            up_match = re.search(r'\[\[equipment/([A-Za-z0-9_-]+)\]\].*Upstream', line, re.IGNORECASE)
            if up_match:
                up_tag = up_match.group(1).replace("AB", "A/B")
                self.equipment_flows.append(EquipmentFlowEdge(
                    from_equipment_tag=up_tag,
                    to_equipment_tag=tag,
                    stream_id=f"S-{up_tag}->{tag}"
                ))
            
            down_match = re.search(r'\[\[equipment/([A-Za-z0-9_-]+)\]\].*Downstream', line, re.IGNORECASE)
            if down_match:
                down_tag = down_match.group(1).replace("AB", "A/B")
                self.equipment_flows.append(EquipmentFlowEdge(
                    from_equipment_tag=tag,
                    to_equipment_tag=down_tag,
                    stream_id=f"S-{tag}->{down_tag}"
                ))
                
            from_table = re.search(r'From\s+([A-Z]-[0-9]+[A-Z/]*)', line, re.IGNORECASE)
            if from_table:
                source_tag = from_table.group(1)
                self.equipment_flows.append(EquipmentFlowEdge(
                    from_equipment_tag=source_tag,
                    to_equipment_tag=tag,
                    stream_id=f"S-{source_tag}->{tag}"
                ))
            to_table = re.search(r'To\s+([A-Z]-[0-9]+[A-Z/]*)', line, re.IGNORECASE)
            if to_table:
                dest_tag = to_table.group(1)
                self.equipment_flows.append(EquipmentFlowEdge(
                    from_equipment_tag=tag,
                    to_equipment_tag=dest_tag,
                    stream_id=f"S-{tag}->{dest_tag}"
                ))

            # Instrument tags in table (3 or 4 columns)
            cols = [c.strip() for c in line.split('|') if c.strip()]
            if len(cols) >= 3:
                possible_tag = cols[0]
                if re.match(r'^[A-Z]{2,5}-[0-9]{4}[A-Z]?$', possible_tag):
                    itype = cols[1]
                    idesc = cols[2] if len(cols) > 2 else ""
                    iaction = cols[3] if len(cols) > 3 else idesc
                    combined_text = f"{itype} {idesc} {iaction}"
                    
                    is_sis = "SIS" in combined_text or "ESD" in combined_text or "SIL" in combined_text
                    sil = "SIL 1" if "SIL 1" in combined_text else ("SIL 2" if "SIL 2" in combined_text else ("SIL 3" if "SIL 3" in combined_text else "None"))
                    
                    self.instruments[possible_tag] = InstrumentModel(
                        instrument_tag=possible_tag,
                        equipment_tag=tag,
                        type=itype[:64],
                        sil_rating=sil,
                        is_sis_initiator=is_sis
                    )
                    if is_sis:
                        self.instrument_actuations.append(InstrumentActuationEdge(
                            initiator_instrument_tag=possible_tag,
                            target_equipment_tag=tag,
                            interlock_action=f"{idesc} -> {iaction}"[:64]
                        ))

    def _parse_instrument_file(self, file_path: Path):
        fm, body = self._extract_frontmatter(file_path)
        for line in body.splitlines():
            cols = [c.strip() for c in line.split('|') if c.strip()]
            if len(cols) >= 3:
                possible_tag = cols[0]
                if re.match(r'^[A-Z]{2,5}-[0-9]{4}[A-Z]?$', possible_tag):
                    itype = cols[1]
                    if possible_tag not in self.instruments:
                        self.instruments[possible_tag] = InstrumentModel(
                            instrument_tag=possible_tag,
                            equipment_tag="E-2303",
                            type=itype[:64],
                            is_sis_initiator="SIS" in itype
                        )

    def _parse_hazard_file(self, file_path: Path):
        fm, _ = self._extract_frontmatter(file_path)
        haz_id = str(fm.get("hazard_id", file_path.stem))
        self.chemical_hazards[haz_id] = ChemicalHazardModel(
            hazard_id=haz_id,
            chemical_name=str(fm.get("chemical_name", fm.get("name", file_path.stem))),
            cas_number=str(fm.get("cas_number", "")),
            decomposition_onset_temp_celsius=float(fm.get("decomposition_onset_temp_c", 80.0)),
            sadt_temp_celsius=str(fm.get("sadt", "")),
            flash_point_celsius=float(fm.get("flash_point_c")) if fm.get("flash_point_c") is not None else None,
            ghs_classification=fm.get("ghs", []) if isinstance(fm.get("ghs"), list) else [],
            markdown_uri=str(file_path)
        )

    # --- Search Implementations ---
    def keyword_search(self, query: str, limit: int = 10) -> List[Tuple[str, float, EquipmentModel]]:
        query_tokens = re.findall(r'\w+', query.lower())
        results = []
        for tag, eq in self.equipment.items():
            if eq.is_deleted:
                continue
            text = f"{eq.equipment_tag} {eq.name} {eq.description_summary or ''}".lower()
            score = 0.0
            for t in query_tokens:
                if t in text:
                    score += 5.0 if t == eq.equipment_tag.lower() else 1.0
            if score > 0:
                results.append((tag, score, eq))
        results.sort(key=lambda x: x[1], reverse=True)
        return results[:limit]

    def vector_search(self, query_embedding: List[float], limit: int = 10) -> List[Tuple[str, float, EquipmentModel]]:
        results = []
        for tag, eq in self.equipment.items():
            if eq.is_deleted or not eq.embedding:
                continue
            sim = cosine_similarity(query_embedding, eq.embedding)
            if sim > 0:
                results.append((tag, sim, eq))
        results.sort(key=lambda x: x[1], reverse=True)
        return results[:limit]

    def graph_traverse_upstream(self, target_tag: str, max_depth: int = 3) -> List[Dict[str, Any]]:
        visited = set()
        queue = [(target_tag, 0, [])]
        results = []

        while queue:
            current, depth, path = queue.pop(0)
            if depth >= max_depth:
                continue
            
            for flow in self.equipment_flows:
                if flow.to_equipment_tag == current and flow.from_equipment_tag not in visited:
                    visited.add(flow.from_equipment_tag)
                    eq = self.equipment.get(flow.from_equipment_tag)
                    res = {
                        "upstream_tag": flow.from_equipment_tag,
                        "equipment_name": eq.name if eq else "",
                        "temp_celsius": eq.operating_temp_celsius if eq else None,
                        "depth": depth + 1,
                        "stream_id": flow.stream_id
                    }
                    results.append(res)
                    queue.append((flow.from_equipment_tag, depth + 1, path + [flow.from_equipment_tag]))
        return results

    def graph_find_interlocks(self, target_equipment_tag: str) -> List[Dict[str, Any]]:
        known_tags = set(self.equipment.keys()) | set(act.target_equipment_tag for act in self.instrument_actuations)
        resolved_tag = resolve_equipment_tag_alias(target_equipment_tag, known_tags)
        results = []
        for act in self.instrument_actuations:
            if act.target_equipment_tag in (target_equipment_tag, resolved_tag):
                inst = self.instruments.get(act.initiator_instrument_tag)
                results.append({
                    "instrument_tag": act.initiator_instrument_tag,
                    "type": inst.type if inst else "Unknown",
                    "sil_rating": inst.sil_rating if inst else "None",
                    "voting_logic": inst.voting_logic if inst else "1oo1",
                    "trip_setpoint": inst.trip_setpoint if inst else None,
                    "interlock_action": act.interlock_action
                })
        return results

    def graph_find_all_instruments(self, target_equipment_tag: str) -> Dict[str, Any]:
        """Queries full physical instrument inventory and active SIS interlocks for target equipment."""
        known_tags = set(self.equipment.keys()) | set(inst.equipment_tag for inst in self.instruments.values())
        resolved_tag = resolve_equipment_tag_alias(target_equipment_tag, known_tags)

        actuations_map = {}
        for act in self.instrument_actuations:
            if act.target_equipment_tag in (target_equipment_tag, resolved_tag):
                actuations_map[act.initiator_instrument_tag] = act.interlock_action

        instruments = []
        for inst in self.instruments.values():
            if inst.equipment_tag in (target_equipment_tag, resolved_tag):
                act_action = actuations_map.get(inst.instrument_tag)
                is_sis = bool(inst.is_sis_initiator or act_action)
                instruments.append({
                    "instrument_tag": inst.instrument_tag,
                    "equipment_tag": inst.equipment_tag,
                    "type": inst.type or "Instrument",
                    "calibrated_range": inst.calibrated_range,
                    "trip_setpoint": inst.trip_setpoint,
                    "sil_rating": inst.sil_rating or ("SIL 2" if is_sis else "None"),
                    "voting_logic": inst.voting_logic or ("1oo2" if is_sis else "1oo1"),
                    "is_sis_initiator": bool(inst.is_sis_initiator),
                    "is_interlock": is_sis,
                    "interlock_action": act_action or ("Active SIS Trip Initiator" if is_sis else "None")
                })
        sis_count = sum(1 for i in instruments if i["is_interlock"])
        return {
            "target_tag": target_equipment_tag,
            "equipment_tag": resolved_tag,
            "total_instruments_count": len(instruments),
            "sis_interlocks_count": sis_count,
            "instruments": instruments
        }

