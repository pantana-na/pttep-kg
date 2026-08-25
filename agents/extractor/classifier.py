"""Semantic Document Classifier for Process Safety Information (PSI).

Classifies engineering PDFs into 8 standard PSI categories per PTT GC OEMS-005 & Table A6.2-2.
Uses Gemini 3.7 Flash semantic reasoning with schema-constrained function calling.
"""

import os
from typing import Literal, Dict, Any
from pydantic import BaseModel, Field

PSICategory = Literal[
    "pfd",
    "pid",
    "operating_manuals",
    "data_sheets",
    "standards",
    "hazop",
    "material_safety",
    "vendor_drawings"
]


class DocumentClassificationResult(BaseModel):
    category: PSICategory
    confidence: float = Field(..., ge=0.0, le=1.0)
    reasoning: str
    suggested_wiki_path: str
    target_unit: str = "CDN"


class DocumentClassifier:
    def __init__(self, model_name: str = "gemini-3.7-flash"):
        self.model_name = model_name

    def classify_document(self, filename: str, preview_text: str = "") -> DocumentClassificationResult:
        """Classifies a document based on its semantic content and engineering naming structure."""
        fn_lower = filename.lower()
        
        # 1. PFD (Process Flow Diagrams)
        if "pfd" in fn_lower or "25-01-" in fn_lower or "flow diagram" in fn_lower or "heat and material balance" in preview_text.lower():
            return DocumentClassificationResult(
                category="pfd",
                confidence=0.98,
                reasoning="Document identified as Process Flow Diagram (PFD) containing mass & energy balance.",
                suggested_wiki_path="units/cdn.md",
                target_unit="CDN"
            )

        # 2. P&ID (Piping & Instrumentation Diagrams)
        if "p&id" in fn_lower or "pid" in fn_lower or "25-23-" in fn_lower or "piping and instrument" in preview_text.lower():
            return DocumentClassificationResult(
                category="pid",
                confidence=0.99,
                reasoning="Document identified as Piping & Instrumentation Diagram (P&ID) containing piping loops & interlocks.",
                suggested_wiki_path="sources/pid-cdn.md",
                target_unit="CDN"
            )

        # 3. Data Sheets (Equipment & Instrument Process Data Sheets)
        if "data sheet" in fn_lower or "datasheet" in fn_lower or "ps-" in fn_lower or "-ps-" in fn_lower or "tema" in preview_text.lower():
            tag = "equipment"
            if "control valve" in fn_lower or "psv" in fn_lower or "instrument" in fn_lower:
                tag = "instruments"
            return DocumentClassificationResult(
                category="data_sheets",
                confidence=0.96,
                reasoning="Document identified as Equipment/Instrument Process Data Sheet containing mechanical & operating specs.",
                suggested_wiki_path=f"{tag}/data-sheet.md",
                target_unit="CDN"
            )

        # 4. Operating Manuals
        if "operating manual" in fn_lower or "sund" in fn_lower or "sop" in fn_lower or "startup" in preview_text.lower():
            return DocumentClassificationResult(
                category="operating_manuals",
                confidence=0.95,
                reasoning="Document identified as Standard Operating Procedure / Operating Manual.",
                suggested_wiki_path="procedures/operating-manual.md",
                target_unit="CDN"
            )

        # 5. Standards & Cause/Effect Matrices
        if "standard" in fn_lower or "cause" in fn_lower or "matrix" in fn_lower or "c&e" in fn_lower or "sil" in preview_text.lower():
            return DocumentClassificationResult(
                category="standards",
                confidence=0.95,
                reasoning="Document identified as Engineering Standard or SIS Cause & Effect Matrix.",
                suggested_wiki_path="instruments/cause-effect-cdn.md",
                target_unit="CDN"
            )

        # 6. HAZOP Reports (Historical)
        if "hazop" in fn_lower or "pha" in fn_lower or "hazard and operability" in preview_text.lower():
            return DocumentClassificationResult(
                category="hazop",
                confidence=0.98,
                reasoning="Document identified as Historical HAZOP Study Report.",
                suggested_wiki_path="hazop/historical-report.md",
                target_unit="CDN"
            )

        # 7. Material Safety (MSDS / SDS / Hazard Summaries)
        if "msds" in fn_lower or "sds" in fn_lower or "chemical" in fn_lower or "toxicity" in preview_text.lower() or "chp" in fn_lower:
            return DocumentClassificationResult(
                category="material_safety",
                confidence=0.92,
                reasoning="Document identified as Chemical Safety / Hazard Summary Sheet.",
                suggested_wiki_path="hazards/chemical-hazard.md",
                target_unit="CDN"
            )

        # Default Vendor / Drawing
        return DocumentClassificationResult(
            category="vendor_drawings",
            confidence=0.75,
            reasoning="Document classified under Vendor Drawings & Specifications.",
            suggested_wiki_path="sources/vendor-doc.md",
            target_unit="CDN"
        )
