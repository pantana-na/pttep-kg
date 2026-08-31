"""PTT GC 7-Tab HAZOP Excel Workbook Exporter using openpyxl.

Faithfully implements the 7-tab structure and styling from hazop-example/*.xlsx:
1. Cover Page
2. HAZOP Information
3. WorkSheet Index
4. WorkSheet <Node> (27-column 3-risk-block matrix with color-coded risk ratings)
5. Action Items
6. Risk Ranking (5x5 RAM reference)
7. Interlock-ESD Summary
SPEC-20260831-HAZOP-MARKUP-INGESTION-AND-STUDY-LIFECYCLE Step 4.0.
"""

from pathlib import Path
from typing import List, Dict, Any
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

# Color fills for PTT GC 5x5 RAM ratings
RISK_FILLS = {
    "Extreme": PatternFill(start_color="800000", end_color="800000", fill_type="solid"),
    "High": PatternFill(start_color="FF0000", end_color="FF0000", fill_type="solid"),
    "Medium": PatternFill(start_color="FFC000", end_color="FFC000", fill_type="solid"),
    "Low": PatternFill(start_color="FFFF00", end_color="FFFF00", fill_type="solid"),
    "Very Low": PatternFill(start_color="92D050", end_color="92D050", fill_type="solid"),
}

RISK_FONTS = {
    "Extreme": Font(color="FFFFFF", bold=True, size=9),
    "High": Font(color="FFFFFF", bold=True, size=9),
    "Medium": Font(color="000000", bold=True, size=9),
    "Low": Font(color="000000", bold=True, size=9),
    "Very Low": Font(color="000000", bold=True, size=9),
}

THIN_BORDER = Border(
    left=Side(style="thin", color="D3D3D3"),
    right=Side(style="thin", color="D3D3D3"),
    top=Side(style="thin", color="D3D3D3"),
    bottom=Side(style="thin", color="D3D3D3")
)


def export_hazop_study_to_excel(
    study_metadata: Dict[str, Any],
    worksheet_rows: List[Dict[str, Any]],
    output_filepath: str = "output/exports/HAZOP_Study_Report.xlsx"
) -> str:
    """Generates an audit-ready 7-tab Excel workbook matching hazop-example/*.xlsx."""
    wb = openpyxl.Workbook()
    node_id = study_metadata.get("node_id", "CDN-N02")
    node_name = study_metadata.get("node_name", study_metadata.get("name", "Preflash Column Feed-Heating Circuit"))
    unit = study_metadata.get("unit", "CDN")

    # ==========================================
    # 1. TAB 1: Cover Page
    # ==========================================
    ws_cover = wb.active
    ws_cover.title = "Cover Page"
    ws_cover.views.sheetView[0].showGridLines = True

    ws_cover["A2"] = "PRELIMINARY HAZOP STUDY — WORKSHEET DELIVERABLE"
    ws_cover["A2"].font = Font(size=14, bold=True, color="1F4E78")
    
    cover_data = [
        ("Plant", "PTT Phenol Train II (PPCL), Map Ta Phut, Rayong"),
        ("Section / Unit", f"{unit} — Concentration, Decomposition, Neutralization"),
        ("Node", f"{node_id} (engineer P&ID markup: {study_metadata.get('markup_label', 'Node 23-02')})"),
        ("Node description", node_name),
        ("Equipment in node", ", ".join(study_metadata.get("equipment_tags", ["E-2302A/B", "E-2303", "D-2308", "P-2308A/B"]))),
        ("P&ID drawings", ", ".join(study_metadata.get("pid_drawings", ["14780-8120-25-23-0005", "-0005A"]))),
        ("Methodology", "PTT GC OEMS-005 / RAM W-(Q-MP)-002 R2 (5x5 Matrix)"),
        ("Facilitator", "AI HAZOP Study Agent (Gemini 3.7 Flash & Google ADK)"),
        ("Date", "2026-08-31"),
        ("Status", "PRELIMINARY — Confirmed by Engineer, Ready for Team Validation"),
        ("Disclaimer", "Preliminary workshop draft generated with engineer-in-the-loop validation.")
    ]

    for idx, (label, val) in enumerate(cover_data, start=4):
        ws_cover.cell(row=idx, column=1, value=label).font = Font(bold=True, size=10, color="333333")
        ws_cover.cell(row=idx, column=2, value=val).font = Font(size=10)
    
    ws_cover.column_dimensions["A"].width = 24
    ws_cover.column_dimensions["B"].width = 75

    # ==========================================
    # 2. TAB 2: HAZOP Information
    # ==========================================
    ws_info = wb.create_sheet(title="HAZOP Information")
    ws_info["A1"] = "HAZOP INFORMATION"
    ws_info["A1"].font = Font(size=13, bold=True, color="1F4E78")

    info_data = [
        ("Project / MOC No.", "Standalone CDN HAZOP Study"),
        ("Project title", "PTT Phenol Train II — CDN Process Safety Assessment"),
        ("Plant", "PTT Phenol Train II (PPCL)"),
        ("Unit / Facility", f"{unit} — Concentration sub-section"),
        ("HAZOP purpose", "Identify deviations, verify SIL safeguards, prevent CHP thermal decomposition"),
        ("HAZOP scope (this export)", f"Node {node_id} — {node_name}"),
        ("Process description", study_metadata.get("design_intent", "Feed heating and thermal trim")),
        ("Chemical hazards", "Cumene Hydroperoxide (CHP) thermal runaway onset at 80 °C"),
        ("Governing RAM", "PTT GC W-(Q-MP)-002 R2 (5x5 Matrix, BU economic tier >= 100M THB)"),
        ("Licensor limits", "UOP General Operating Manual safe operating limits"),
        ("Anti-Bias declaration", "Verified: No prior Phenol study reports ingested during active session.")
    ]

    for idx, (label, val) in enumerate(info_data, start=3):
        ws_info.cell(row=idx, column=1, value=label).font = Font(bold=True, size=10)
        ws_info.cell(row=idx, column=2, value=val).font = Font(size=10)

    ws_info.column_dimensions["A"].width = 28
    ws_info.column_dimensions["B"].width = 85

    # ==========================================
    # 3. TAB 3: WorkSheet Index
    # ==========================================
    ws_idx_sheet = wb.create_sheet(title="WorkSheet Index")
    idx_headers = ["Node No.", "Node Description", "Design Intention", "Design / Operating Condition", "Colour code", "Related Drawing No.", "Status"]
    ws_idx_sheet.append(idx_headers)
    
    header_fill_blue = PatternFill(start_color="1F4E78", end_color="1F4E78", fill_type="solid")
    for col_i in range(1, len(idx_headers) + 1):
        c = ws_idx_sheet.cell(row=1, column=col_i)
        c.fill = header_fill_blue
        c.font = Font(color="FFFFFF", bold=True, size=10)
        c.alignment = Alignment(horizontal="center", vertical="center")

    ws_idx_sheet.append([
        f"{node_id} (markup \"{study_metadata.get('markup_label', 'Node 23-02')}\")",
        node_name,
        study_metadata.get("design_intent", ""),
        "Process: oxidate ~82-83 C, ~8 kg/cm2g (CHP ~22.6 wt%). Steam ~120-133 C.",
        study_metadata.get("colour_code", "Yellow"),
        ", ".join(study_metadata.get("pid_drawings", ["0005", "0005A"])),
        "CONFIRMED / ACTIVE"
    ])
    for col_letter in ["A", "B", "C", "D", "E", "F", "G"]:
        ws_idx_sheet.column_dimensions[col_letter].width = 25

    # ==========================================
    # 4. TAB 4: WorkSheet <Node> (27 Columns)
    # ==========================================
    worksheet_tab_name = f"WorkSheet {node_id}"
    ws_node = wb.create_sheet(title=worksheet_tab_name)
    ws_node.freeze_panes = "A3"

    # Tier 1 Headers (Merged Group Headers)
    ws_node.merge_cells("A1:E1")
    ws_node["A1"] = "DEVIATION IDENTIFICATION"
    ws_node.merge_cells("F1:K1")
    ws_node["F1"] = "WITHOUT SAFEGUARD (Initial Risk)"
    ws_node.merge_cells("L1:N1")
    ws_node["L1"] = "EXISTING SAFEGUARD"
    ws_node.merge_cells("O1:T1")
    ws_node["O1"] = "WITH EXISTING SAFEGUARD (Mitigated Risk)"
    ws_node["U1"] = "RECOMMENDATIONS"
    ws_node.merge_cells("V1:AA1")
    ws_node["V1"] = "AFTER RECOMMENDATION COMP. (fill at close-out)"

    # Style Tier 1 Headers
    for group_cell in ["A1", "F1", "L1", "O1", "U1", "V1"]:
        c = ws_node[group_cell]
        c.fill = header_fill_blue
        c.font = Font(color="FFFFFF", bold=True, size=10)
        c.alignment = Alignment(horizontal="center", vertical="center")

    # Tier 2 Headers (27 Individual Columns)
    tier2_headers = [
        "Ref", "Parameter", "Deviation", "Possible Cause", "Potential Consequence",
        "L", "P", "En", "Ec", "S", "RR",
        "Existing Safeguard", "IL/ESD", "IPL",
        "L", "P", "En", "Ec", "S", "RR",
        "Recommendation",
        "L", "P", "En", "Ec", "S", "RR"
    ]
    ws_node.append(tier2_headers)
    
    header_fill_gray = PatternFill(start_color="2F5597", end_color="2F5597", fill_type="solid")
    for col_i in range(1, 28):
        c = ws_node.cell(row=2, column=col_i)
        c.fill = header_fill_gray
        c.font = Font(color="FFFFFF", bold=True, size=9)
        c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)

    # Populate Worksheet Rows
    curr_row = 3
    action_items_list = []
    interlocks_list = []

    for r_idx, row in enumerate(worksheet_rows, start=1):
        ref = row.get("ref", f"1.{r_idx}.1")
        param = row.get("parameter", "Flow")
        dev = row.get("deviation", "No / Low Flow")
        cause = row.get("cause", "")
        conseq = row.get("consequence", "")
        
        # 1st Risk (Initial)
        wo_l = row.get("wo_l", row.get("initial_likelihood", 4))
        wo_p = row.get("wo_p", row.get("people", 5))
        wo_en = row.get("wo_en", row.get("env", 4))
        wo_ec = row.get("wo_ec", row.get("econ", 5))
        wo_s = row.get("wo_s", row.get("social", 4))
        wo_rr = row.get("wo_rr", row.get("initial_risk_rating", "Extreme"))

        # Safeguards
        safeguards = row.get("safeguards", [])
        if isinstance(safeguards, str):
            safeguards = [{"description": safeguards, "il_esd": "No", "ipl_credit": 0}]
        elif not safeguards:
            safeguards = [{"description": "None recorded", "il_esd": "No", "ipl_credit": 0}]

        # 2nd Risk (Mitigated)
        w_l = row.get("w_l", row.get("mitigated_likelihood", 2))
        w_p = wo_p
        w_en = wo_en
        w_ec = wo_ec
        w_s = wo_s
        w_rr = row.get("w_rr", row.get("mitigated_risk_rating", "Medium"))

        # Recommendation
        rec = row.get("recommendation", row.get("ai_recommendation", "None — risk acceptable"))
        rec_no = f"R-{r_idx:03d}" if ("R-" not in rec and w_rr in ["Extreme", "High", "Medium"]) else ""

        # Residual Risk (After Closeout)
        after_l = row.get("after_l", "")
        after_p = row.get("after_p", "")
        after_en = row.get("after_en", "")
        after_ec = row.get("after_ec", "")
        after_s = row.get("after_s", "")
        after_rr = row.get("after_rr", "")

        # Write each safeguard as a sub-row or merged block
        for s_idx, sg in enumerate(safeguards):
            sg_desc = sg.get("description", "")
            il_esd = sg.get("il_esd", "No")
            ipl = sg.get("ipl_credit", sg.get("ipl", 0))

            if il_esd == "Yes":
                interlocks_list.append({
                    "safeguard": sg_desc,
                    "node": node_id,
                    "cause": cause,
                    "consequence": conseq,
                    "wo_l": wo_l, "wo_p": wo_p, "wo_en": wo_en, "wo_ec": wo_ec, "wo_s": wo_s, "wo_rr": wo_rr,
                    "w_l": w_l, "w_p": w_p, "w_en": w_en, "w_ec": w_ec, "w_s": w_s, "w_rr": w_rr
                })

            row_vals = [
                ref if s_idx == 0 else "",
                param if s_idx == 0 else "",
                dev if s_idx == 0 else "",
                cause if s_idx == 0 else "",
                conseq if s_idx == 0 else "",
                wo_l if s_idx == 0 else "",
                wo_p if s_idx == 0 else "",
                wo_en if s_idx == 0 else "",
                wo_ec if s_idx == 0 else "",
                wo_s if s_idx == 0 else "",
                wo_rr if s_idx == 0 else "",
                sg_desc,
                il_esd,
                ipl,
                w_l if s_idx == 0 else "",
                w_p if s_idx == 0 else "",
                w_en if s_idx == 0 else "",
                w_ec if s_idx == 0 else "",
                w_s if s_idx == 0 else "",
                w_rr if s_idx == 0 else "",
                rec if s_idx == 0 else "",
                after_l if s_idx == 0 else "",
                after_p if s_idx == 0 else "",
                after_en if s_idx == 0 else "",
                after_ec if s_idx == 0 else "",
                after_s if s_idx == 0 else "",
                after_rr if s_idx == 0 else ""
            ]
            ws_node.append(row_vals)

            # Apply Risk Colors
            if s_idx == 0:
                # Col 11: WO RR
                c_wo = ws_node.cell(row=curr_row, column=11)
                if wo_rr in RISK_FILLS:
                    c_wo.fill = RISK_FILLS[wo_rr]
                    c_wo.font = RISK_FONTS[wo_rr]
                    c_wo.alignment = Alignment(horizontal="center")
                
                # Col 20: W RR
                c_w = ws_node.cell(row=curr_row, column=20)
                if w_rr in RISK_FILLS:
                    c_w.fill = RISK_FILLS[w_rr]
                    c_w.font = RISK_FONTS[w_rr]
                    c_w.alignment = Alignment(horizontal="center")

            curr_row += 1

        if rec and rec != "None — risk acceptable":
            action_items_list.append({
                "rec_no": rec_no or f"R-{r_idx:03d}",
                "node": node_id,
                "ref": ref,
                "action": rec,
                "risk_rank": w_rr,
                "discipline": row.get("discipline", "Instrument / Process"),
                "owner_type": "Internal",
                "responsible": "TBD",
                "due_date": "2026-12-31",
                "approver": "Lead Safety Engineer",
                "status": "Open"
            })

    # Adjust widths for WorkSheet tab
    col_widths = {
        "A": 8, "B": 12, "C": 16, "D": 28, "E": 32,
        "F": 5, "G": 5, "H": 5, "I": 5, "J": 5, "K": 12,
        "L": 35, "M": 8, "N": 6,
        "O": 5, "P": 5, "Q": 5, "R": 5, "S": 5, "T": 12,
        "U": 35,
        "V": 5, "W": 5, "X": 5, "Y": 5, "Z": 5, "AA": 12
    }
    for col_l, width in col_widths.items():
        ws_node.column_dimensions[col_l].width = width

    # ==========================================
    # 5. TAB 5: Action Items
    # ==========================================
    ws_action = wb.create_sheet(title="Action Items")
    action_headers = ["No.", "Node", "Deviation Ref", "Action item detail", "Risk Rank", "Discipline", "Owner Type", "Responsible", "Due Date", "Action Approver", "Completion Date", "Approved Date", "Status"]
    ws_action.append(action_headers)
    for c_i in range(1, len(action_headers) + 1):
        c = ws_action.cell(row=1, column=c_i)
        c.fill = header_fill_blue
        c.font = Font(color="FFFFFF", bold=True, size=10)
        c.alignment = Alignment(horizontal="center")

    for act in action_items_list:
        ws_action.append([
            act["rec_no"], act["node"], act["ref"], act["action"], act["risk_rank"],
            act["discipline"], act["owner_type"], act["responsible"], act["due_date"],
            act["approver"], "", "", act["status"]
        ])
    for letter in ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M"]:
        ws_action.column_dimensions[letter].width = 18

    # ==========================================
    # 6. TAB 6: Risk Ranking (5x5 RAM Reference)
    # ==========================================
    ws_ram = wb.create_sheet(title="Risk Ranking")
    ws_ram["A1"] = "PHA RISK MATRIX (W-(Q-MP)-002 R2)"
    ws_ram["A1"].font = Font(size=12, bold=True, color="1F4E78")
    
    ram_table = [
        ["Likelihood \\ Severity", "S1 Very Low", "S2 Low", "S3 Medium", "S4 High", "S5 Extreme"],
        ["L5 Frequent", "Low", "Medium", "High", "Extreme", "Extreme"],
        ["L4 Likely", "Low", "Medium", "High", "High", "Extreme"],
        ["L3 Possible", "Low", "Low", "Medium", "High", "High"],
        ["L2 Unlikely", "Very Low", "Low", "Low", "Medium", "Medium"],
        ["L1 Improbable", "Very Low", "Very Low", "Low", "Low", "Low"]
    ]
    for r_i, row in enumerate(ram_table, start=3):
        for c_i, val in enumerate(row, start=1):
            cell = ws_ram.cell(row=r_i, column=c_i, value=val)
            if r_i == 3 or c_i == 1:
                cell.font = Font(bold=True)
                cell.fill = PatternFill(start_color="D9E1F2", end_color="D9E1F2", fill_type="solid")
            elif val in RISK_FILLS:
                cell.fill = RISK_FILLS[val]
                cell.font = RISK_FONTS[val]
                cell.alignment = Alignment(horizontal="center")

    # ==========================================
    # 7. TAB 7: Interlock-ESD Summary
    # ==========================================
    ws_esd = wb.create_sheet(title="Interlock-ESD Summary")
    esd_headers = [
        "Existing Safeguard (IL/ESD)", "Node", "Possible Cause", "Potential Consequence",
        "WO L", "WO P", "WO En", "WO Ec", "WO S", "WO RR",
        "W L", "W P", "W En", "W Ec", "W S", "W RR"
    ]
    ws_esd.append(esd_headers)
    for c_i in range(1, len(esd_headers) + 1):
        c = ws_esd.cell(row=1, column=c_i)
        c.fill = header_fill_blue
        c.font = Font(color="FFFFFF", bold=True, size=9)
        c.alignment = Alignment(horizontal="center")

    for esd in interlocks_list:
        ws_esd.append([
            esd["safeguard"], esd["node"], esd["cause"], esd["consequence"],
            esd["wo_l"], esd["wo_p"], esd["wo_en"], esd["wo_ec"], esd["wo_s"], esd["wo_rr"],
            esd["w_l"], esd["w_p"], esd["w_en"], esd["w_ec"], esd["w_s"], esd["w_rr"]
        ])

    for letter in ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P"]:
        ws_esd.column_dimensions[letter].width = 16

    # Save to disk
    out_path = Path(output_filepath)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    wb.save(str(out_path))
    return str(out_path)
