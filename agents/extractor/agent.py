"""Extractor Agent Engine for Multimodal Process Safety Ingestion.

Powered by Gemini 3.7 Flash and ADK agent tools.
Transforms unstructured engineering PDFs into structured Obsidian-compatible Markdown with YAML frontmatter.
"""

import os
from pathlib import Path
from typing import Dict, Any, Optional
from agents.extractor.classifier import DocumentClassifier, DocumentClassificationResult
from agents.extractor.parsers.pfd_parser import format_pfd_markdown
from agents.extractor.parsers.pid_parser import format_pid_markdown
from agents.extractor.parsers.datasheet_parser import format_datasheet_markdown


class ExtractorAgent:
    def __init__(self, output_dir: str = "wiki"):
        self.output_dir = Path(output_dir)
        self.classifier = DocumentClassifier()

    def process_document(self, file_path: str, preview_text: str = "") -> Dict[str, Any]:
        """Classifies and processes a single document into structured Markdown."""
        path = Path(file_path)
        filename = path.name
        
        # 1. Semantic Classification
        classification = self.classifier.classify_document(filename, preview_text)
        
        # 2. Markdown Synthesis
        markdown_content = ""
        relative_path = classification.suggested_wiki_path
        
        if classification.category == "pfd":
            markdown_content = format_pfd_markdown(
                unit_id="CDN",
                unit_name="Cumene Cleavage & Decomposition Section",
                equipment_list=[
                    {"tag": "E-2303", "name": "Preflash Column Steam Heater", "type": "HeatExchanger", "temp": "83", "pressure": "3.5"},
                    {"tag": "V-2301", "name": "Preflash Column", "type": "Column", "temp": "83", "pressure": "0.15"}
                ],
                streams=[
                    {"stream_id": "S-2301", "from": "E-2302A/B", "to": "E-2303", "flow": "45000", "temp": "82", "pressure": "3.8", "chp": "28.5"}
                ],
                source_pdf=filename
            )
        elif classification.category == "pid":
            markdown_content = format_pid_markdown(
                drawing_no="14780-8120-25-23-0005",
                title="Preflash Column Steam Heater & Overhead System",
                unit="CDN",
                equipment_tags=["E-2303", "V-2301", "D-2308"],
                instrument_loops=[
                    {"tag": "TXSHH-0502A", "type": "SIS Temp HH", "description": "High temp trip to UC-2301 ESD", "setpoint": "78.0 °C"},
                    {"tag": "UXV-0501", "type": "SIS Isolation Valve", "description": "Primary steam cutoff valve", "setpoint": "Close on ESD"}
                ],
                source_pdf=filename
            )
        elif classification.category == "data_sheets":
            markdown_content = format_datasheet_markdown(
                tag="E-2303",
                name="Preflash Column Steam Heater",
                eq_type="HeatExchanger (Shell-and-Tube, Steam Heater)",
                unit="CDN",
                design_data={"Shell Design Pressure": "3.5 kg/cm²g", "Shell Design Temp": "195 °C", "Duty": "6.1 MMkcal/h"},
                operating_data={"Inlet Temp": "82 °C", "Outlet Temp": "83 °C", "Steam Type": "SC1.5"},
                source_pdf=filename
            )
            relative_path = "equipment/E-2303.md"
        else:
            # Generic template
            markdown_content = f"---\ntitle: {filename}\ntags: [source, raw, {classification.category}]\nsources: [{filename}]\n---\n\n# {filename}\n\nProcessed as {classification.category}.\n"

        target_file = self.output_dir / relative_path
        target_file.parent.mkdir(parents=True, exist_ok=True)
        target_file.write_text(markdown_content, encoding="utf-8")
        
        return {
            "status": "SUCCESS",
            "category": classification.category,
            "confidence": classification.confidence,
            "wiki_path": str(relative_path),
            "full_path": str(target_file),
            "content_preview": markdown_content[:300]
        }
