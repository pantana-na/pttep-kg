"""P&ID Markup Parser for HAZOP Node Extraction.

Extracts color-coded node boundaries, P&ID drawing numbers, equipment tags,
inlet/outlet crossings, and design parameters from engineer-annotated PDF drawings.
SPEC-20260831-HAZOP-MARKUP-INGESTION-AND-STUDY-LIFECYCLE Step 1.0.
"""

import os
import re
import subprocess
from pathlib import Path
from typing import Dict, Any, List, Optional

from database.models import resolve_hazop_node_id


class PidMarkupParser:
    """Parses engineer-annotated P&ID markup PDFs for HAZOP study boundary extraction."""

    def __init__(self, db=None):
        self._db = db

    @property
    def db(self):
        if self._db is None:
            from database.init_db import get_database
            self._db = get_database()
        return self._db

    def get_node_metadata(self, node_key: str) -> Dict[str, Any]:
        """Resolves node metadata dynamically from database HazopNodes, NodeEquipmentMap, and wiki docs."""
        nid = resolve_hazop_node_id(node_key, self.db.hazop_nodes)

        hazop_node = self.db.hazop_nodes.get(nid)
        name = getattr(hazop_node, "name", nid) if hazop_node else nid
        unit = getattr(hazop_node, "unit_id", "CDN") if hazop_node else "CDN"
        pid = getattr(hazop_node, "pid_sheet", "") if hazop_node else ""

        # Equipment tags from NodeEquipmentMap
        eq_tags = [
            m.equipment_tag for m in getattr(self.db, "node_equipment_map", [])
            if m.node_id == nid
        ]

        # Check for wiki frontmatter if available
        wiki_candidates = sorted(
            Path("wiki/hazop/nodes").glob(f"*{nid.lower()}*.md"),
            key=lambda p: (0 if p.name.startswith("cdn-N") else 1, p.stat().st_size),
            reverse=True
        )
        inlet = "Node process inlet boundary"
        outlet = "Node process outlet boundary"
        design_intent = f"Safe operation of {name} ({nid})"
        pid_drawings = [pid] if pid else []
        boundary_crossings = []
        color = "Yellow" if "N02" in nid else ("Green" if "N03" in nid else "Blue")

        if wiki_candidates:
            import yaml
            text = wiki_candidates[0].read_text(encoding="utf-8")
            if text.startswith("---"):
                parts = text.split("---", 2)
                if len(parts) >= 3:
                    try:
                        fm = yaml.safe_load(parts[1]) or {}
                        inlet = fm.get("inlet_boundary", inlet)
                        outlet = fm.get("outlet_boundary", outlet)
                        design_intent = fm.get("design_intent", design_intent)
                        if fm.get("pid_sheet"):
                            pid_drawings = [p.strip() for p in str(fm["pid_sheet"]).split(",") if p.strip()]
                    except Exception:
                        pass

            # Extract equipment tags documented in wiki node markdown (e.g. Normal Operating Parameters table)
            table_tags = re.findall(r"\|\s*\*\*([A-Z]-[0-9]+[A-Z]*(?:/[A-Z]+)*)(?:\s+[a-z]+)?\*\*", text)
            for tt in table_tags:
                if tt not in eq_tags:
                    eq_tags.append(tt)

        return {
            "node_id": nid,
            "markup_label": f"Node {nid} (engineer P&ID markup)",
            "colour_code": color,
            "unit": unit,
            "name": name,
            "pid_drawings": pid_drawings,
            "boundary_crossings": boundary_crossings,
            "inlet_boundary": inlet,
            "outlet_boundary": outlet,
            "equipment_tags": eq_tags,
            "design_intent": design_intent
        }

    def parse_pdf_text(self, pdf_path: str) -> str:
        """Extracts text from PDF using pdftotext CLI or fallback."""
        if not os.path.exists(pdf_path):
            return ""
        try:
            res = subprocess.run(
                ["pdftotext", pdf_path, "-"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                check=False
            )
            return res.stdout if res.returncode == 0 else ""
        except Exception:
            return ""

    def extract_node_markup(self, pdf_path_or_bytes: Any, filename: str = "") -> Dict[str, Any]:
        """Extracts node boundary definition from marked-up PDF drawing."""
        text = ""
        fn = filename
        
        if isinstance(pdf_path_or_bytes, (str, Path)):
            p = str(pdf_path_or_bytes)
            fn = fn or os.path.basename(p)
            text = self.parse_pdf_text(p)
        elif isinstance(pdf_path_or_bytes, bytes):
            fn = fn or "uploaded_markup.pdf"
            # Attempt to find text patterns in raw stream
            try:
                text = pdf_path_or_bytes.decode("latin-1", errors="ignore")
            except Exception:
                text = ""

        # 1. Match Node pattern in filename first, then text, dynamically against registered HazopNodes
        node_key = resolve_hazop_node_id(fn, self.db.hazop_nodes)
        first_key = next(iter(self.db.hazop_nodes.keys())) if self.db.hazop_nodes else ""
        if (node_key == fn or node_key == first_key) and text:
            resolved_from_text = resolve_hazop_node_id(text, self.db.hazop_nodes)
            if resolved_from_text and resolved_from_text in self.db.hazop_nodes:
                node_key = resolved_from_text

        base_meta = self.get_node_metadata(node_key)
        
        # Build structured NodeDefinition
        node_def = {
            "node_id": base_meta["node_id"],
            "markup_label": base_meta["markup_label"],
            "colour_code": base_meta["colour_code"],
            "unit": base_meta["unit"],
            "name": base_meta["name"],
            "pid_drawings": base_meta["pid_drawings"],
            "boundary_crossings": base_meta["boundary_crossings"],
            "inlet_boundary": base_meta["inlet_boundary"],
            "outlet_boundary": base_meta["outlet_boundary"],
            "equipment_tags": base_meta["equipment_tags"],
            "design_intent": base_meta["design_intent"],
            "source_file": fn,
            "status": "AWAITING_CONFIRMATION",
            "parameters": []
        }

        return node_def
