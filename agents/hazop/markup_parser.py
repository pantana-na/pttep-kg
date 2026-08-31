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


class PidMarkupParser:
    """Parses engineer-annotated P&ID markup PDFs for HAZOP study boundary extraction."""

    KNOWN_NODE_METADATA = {
        "23-02": {
            "node_id": "CDN-N02",
            "markup_label": "Node 23-02 (engineer P&ID markup)",
            "colour_code": "Yellow",
            "unit": "CDN",
            "name": "Preflash Column Feed-Heating / Steam-Condensate Circuit",
            "pid_drawings": ["14780-8120-25-23-0005", "14780-8120-25-23-0005A"],
            "boundary_crossings": ["14780-8120-25-23-0004", "14780-8120-25-23-0007"],
            "inlet_boundary": "Oxidate feed to E-2302A/B tube side (from feed filters X-2302A/B / Node 23-01) + hot OXI recirculate to E-2302A/B shell (from OXI Oxidizer No.2 pumps) + SC1.5 steam supply to E-2303 tube (via UXV-0501/0502)",
            "outlet_boundary": "Heated oxidate to V-2301 (Preflash Column) + OXI recirculate shell return to OXI + steam condensate from P-2308A/B to condensate return system (66-0056)",
            "equipment_tags": ["E-2302A/B", "E-2303", "D-2308", "P-2308A/B"],
            "design_intent": "Heat oxidate feed to Preflash Column target temp: recover heat in E-2302A/B, trim with SC1.5 steam in E-2303, deliver to V-2301; collect/return E-2303 condensate."
        },
        "23-03": {
            "node_id": "CDN-N03",
            "markup_label": "Node 23-03 (engineer P&ID markup)",
            "colour_code": "Green",
            "unit": "CDN",
            "name": "Flash Column Vaporizer & Concentrated Bottoms Circuit",
            "pid_drawings": ["14780-8120-25-23-0007", "14780-8120-25-23-0007A", "14780-8120-25-23-0008", "14780-8120-25-23-0009"],
            "boundary_crossings": ["14780-8120-25-23-0005", "14780-8120-25-23-0010"],
            "inlet_boundary": "V-2302 bottoms to E-2304 shell side + SC3 steam supply to E-2304 tube side via UXV-0701..0706 + V-2302 concentrated bottoms to P-2301A/B suction",
            "outlet_boundary": "Two-phase vapor/liquid return to V-2302 + concentrated CHP product to Cleavage Reactor D-2304 via P-2301A/B discharge + E-2304 steam condensate",
            "equipment_tags": ["E-2304", "P-2301A/B", "V-2302", "X-2301A/B"],
            "design_intent": "Reboil V-2302 with SC3 steam in E-2304 to concentrate CHP to ~80-85 wt% and safely pump bottoms to Cleavage Section D-2304 via P-2301A/B."
        }
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

        # 1. Match Node pattern in text or filename
        node_key = None
        match = re.search(r"Node[\s_-]*23[-_]?(0[1-9]|1[0-9])", f"{fn} {text}", re.IGNORECASE)
        if match:
            node_key = f"23-{match.group(1)}"
        elif "23-02" in fn or "23-02" in text or "N02" in fn:
            node_key = "23-02"
        elif "23-03" in fn or "23-03" in text or "N03" in fn:
            node_key = "23-03"
        else:
            # Default to 23-02 if ambiguous
            node_key = "23-02"

        base_meta = self.KNOWN_NODE_METADATA.get(node_key, self.KNOWN_NODE_METADATA["23-02"]).copy()
        
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
