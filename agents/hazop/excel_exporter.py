"""PTT GC 7-Tab HAZOP Excel Workbook Exporter using openpyxl."""

import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from pathlib import Path
from typing import List, Dict, Any


def export_hazop_study_to_excel(
    study_metadata: Dict[str, Any],
    worksheet_rows: List[Dict[str, Any]],
    output_filepath: str
) -> str:
    wb = openpyxl.Workbook()
    
    # 1. Cover Page Tab
    ws_cover = wb.active
    ws_cover.title = "Cover Page"
    ws_cover["B2"] = "PTT GLOBAL CHEMICAL PUBLIC COMPANY LIMITED"
    ws_cover["B2"].font = Font(size=14, bold=True, color="1F4E78")
    ws_cover["B3"] = "Process Safety Management — HAZOP Study Report"
    ws_cover["B3"].font = Font(size=12, bold=True)
    ws_cover["B5"] = f"Unit: {study_metadata.get('unit', 'CDN')}"
    ws_cover["B6"] = f"Node: {study_metadata.get('node_id', 'CDN-N02')} — {study_metadata.get('node_name', 'Preflash Column')}"
    ws_cover["B7"] = f"Facilitator: AI HAZOP Study Agent (Gemini 3.7 Flash Reasoning)"
    ws_cover["B8"] = f"Standard: PTT GC W-(Q-MP)-002 R2 (5x5 RAM)"

    # 2. Executive Summary Tab
    ws_exec = wb.create_sheet(title="Executive Summary")
    ws_exec["A1"] = "Executive Summary & Risk Distribution"
    ws_exec["A1"].font = Font(size=12, bold=True)

    # 3. HAZOP Worksheet Tab (Primary Table with 3 Risk Blocks)
    ws_sheet = wb.create_sheet(title="HAZOP Worksheet")
    headers = [
        "Item #", "Deviation", "Cause", "Consequences",
        "P", "En", "Ec", "S", "L (Init)", "Initial Risk",
        "Safeguards (IPL)",
        "L (Mit)", "Mitigated Risk",
        "Recommendation #", "Recommendation Text"
    ]
    ws_sheet.append(headers)
    
    # Header styling
    header_fill = PatternFill(start_color="1F4E78", end_color="1F4E78", fill_type="solid")
    header_font = Font(color="FFFFFF", bold=True, size=10)
    for col_idx in range(1, len(headers) + 1):
        cell = ws_sheet.cell(row=1, column=col_idx)
        cell.fill = header_fill
        cell.font = header_font
        cell.alignment = Alignment(horizontal="center", vertical="center")

    # Populate rows
    for row_idx, row_data in enumerate(worksheet_rows, start=2):
        ws_sheet.append([
            row_data.get("item_no", row_idx - 1),
            row_data.get("deviation", ""),
            row_data.get("cause", ""),
            row_data.get("consequence", ""),
            row_data.get("p", 5),
            row_data.get("en", 3),
            row_data.get("ec", 4),
            row_data.get("s", 3),
            row_data.get("l_init", 4),
            row_data.get("initial_risk", "Extreme"),
            row_data.get("safeguards", ""),
            row_data.get("l_mit", 2),
            row_data.get("mitigated_risk", "Medium"),
            row_data.get("rec_no", "R-001"),
            row_data.get("rec_text", "")
        ])

    # 4. Recommendation Summary Tab
    ws_rec = wb.create_sheet(title="Recommendation Summary")
    ws_rec.append(["Rec #", "Node", "Deviation", "Recommendation", "Priority", "Owner", "Status"])

    # 5. Action Item Tracking Tab
    ws_action = wb.create_sheet(title="Action Item Tracking")
    ws_action.append(["Action ID", "Description", "Discipline", "Target Date", "Status"])

    # 6. RAM Definition Matrix Tab
    ws_ram = wb.create_sheet(title="RAM Definition Matrix")
    ws_ram["A1"] = "PTT GC 5x5 Risk Assessment Matrix (W-(Q-MP)-002 R2)"

    # 7. Document References & Provenance Tab
    ws_refs = wb.create_sheet(title="Document References")
    ws_refs.append(["Doc Code", "Title", "Revision", "Source File"])

    # Save to disk
    out_path = Path(output_filepath)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    wb.save(str(out_path))
    return str(out_path)
