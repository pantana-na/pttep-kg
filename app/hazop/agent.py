"""HAZOP Study Agent Engine.

Facilitates interactive 9-step study lifecycle, anti-bias verification,
P&ID markup ingestion & node confirmation, 3-gate HITL risk evaluation,
and 7-tab audit-ready Excel exports.
SPEC-20260831-HAZOP-MARKUP-INGESTION-AND-STUDY-LIFECYCLE.
"""

import os
import re
import json
from pathlib import Path
from typing import Dict, Any, List, Optional
from datetime import datetime
import httpx

from app.hazop.anti_bias import AntiBiasScanner, AntiBiasException
from app.hazop.markup_parser import PidMarkupParser
from app.hazop.ram_evaluator import (
    evaluate_1st_risk,
    evaluate_2nd_risk,
    evaluate_deviation_risk,
    calculate_ipl_credit
)
from app.hazop.excel_exporter import export_hazop_study_to_excel
from database.models import resolve_hazop_node_id, resolve_equipment_tag_alias


class HazopStudyAgent:
    """Enterprise HAZOP facilitator governing Refinery OEMS-005 and RAM W-(Q-MP)-002 R2."""

    def __init__(self, db_instance):
        self.db = db_instance
        self.scanner = AntiBiasScanner()
        self.markup_parser = PidMarkupParser()
        self.api_key = os.getenv("GEMINI_API_KEY", "")
        self.model_name = os.getenv("DEFAULT_MODEL", "gemini-3.8-flash")
        self.use_vertex = os.getenv("GOOGLE_GENAI_USE_VERTEXAI", "").lower() in ("true", "1", "yes")
        self.project = os.getenv("GCP_PROJECT", "cs-poc-y03r7kmfyov4kilzg50fd7s")
        self.region = os.getenv("GCP_REGION", "asia-southeast1")

    def start_study_setup(self, node_id: str, raw_dir: str = "raw") -> Dict[str, Any]:
        """Validates Anti-Bias rule and initializes study session."""
        scan_res = self.scanner.scan_input_directory(raw_dir)
        if scan_res["status"] == "VIOLATION":
            return {
                "status": "HALT_ANTI_BIAS_VIOLATION",
                "error": scan_res["message"],
                "violating_files": scan_res["violating_files"]
            }

        return {
            "status": "READY",
            "node_id": node_id,
            "message": f"Anti-Bias scan passed cleanly. Ready to facilitate HAZOP for Node {node_id}."
        }

    def parse_markup_and_hydrate(self, pdf_path_or_bytes: Any, filename: str = "") -> Dict[str, Any]:
        """Parses marked-up P&ID PDF and hydrates side-by-side design/operating conditions from wiki."""
        node_def = self.markup_parser.extract_node_markup(pdf_path_or_bytes, filename)
        
        # 1. First check if node has a verified operating parameters table in its wiki document
        node_id = node_def.get("node_id", "")
        wiki_candidates = sorted(
            Path("wiki/hazop/nodes").glob(f"*{node_id.lower()}*.md"),
            key=lambda p: (0 if p.name.startswith("cdn-N") else 1, p.stat().st_size),
            reverse=True
        )
        wiki_params = []
        if wiki_candidates:
            text = wiki_candidates[0].read_text(encoding="utf-8")
            table_match = re.search(r"## Normal Operating Parameters[^\n]*\n+([\s\S]*?)(?:\n##|\Z)", text)
            if table_match:
                table_text = table_match.group(1).strip()
                for line in table_text.splitlines():
                    if not line.startswith("|") or "---" in line or "Stream" in line or "Design Condition" in line:
                        continue
                    cols = [c.strip() for c in line.split("|")[1:-1]]
                    if len(cols) >= 4:
                        raw_tag = cols[0].replace("**", "").strip()
                        stream = cols[1].strip()
                        design_cond = cols[2].strip()
                        oper_cond = cols[3].strip()
                        src = cols[4].strip() if len(cols) > 4 else "Wiki"
                        wiki_params.append({
                            "tag": raw_tag,
                            "stream": stream,
                            "design_condition": design_cond,
                            "operating_condition": oper_cond,
                            "source": src
                        })

        if wiki_params:
            params = wiki_params
        else:
            # 2. Hydrate operating parameters for included equipment tags directly from db.equipment
            params = []
            for tag in node_def["equipment_tags"]:
                eq = self.db.equipment.get(tag)
                if not eq:
                    resolved = resolve_equipment_tag_alias(tag, set(self.db.equipment.keys()))
                    eq = self.db.equipment.get(resolved)

                desc = getattr(eq, "name", tag) if eq else tag
                oper_t = getattr(eq, "operating_temp_celsius", None)
                oper_p = getattr(eq, "operating_pressure_barg", None)
                des_t = getattr(eq, "design_temp_celsius", None)
                des_p = getattr(eq, "design_pressure_barg", None)
                doc_src = getattr(eq, "markdown_uri", None) or f"Drawing / Wiki: {tag}"
                eq_type = getattr(eq, "type", "")

                oper_str = (
                    f"~{oper_t} °C @ {oper_p} barg"
                    if oper_t is not None and oper_p is not None
                    else (f"~{oper_t} °C" if oper_t is not None else "Normal operating envelope")
                )
                des_str = (
                    f"{des_p} barg / FV @ {des_t} °C"
                    if des_p is not None and des_t is not None
                    else (f"{des_p} barg" if des_p is not None else "Design limit per data sheet")
                )

                if eq_type == "HeatExchanger" or tag.startswith("E-"):
                    params.append({
                        "tag": f"{tag} tube",
                        "stream": f"{desc} (tube side)",
                        "design_condition": des_str,
                        "operating_condition": oper_str,
                        "source": doc_src
                    })
                    params.append({
                        "tag": f"{tag} shell",
                        "stream": f"{desc} (shell side)",
                        "design_condition": des_str,
                        "operating_condition": oper_str,
                        "source": doc_src
                    })
                else:
                    params.append({
                        "tag": tag,
                        "stream": desc,
                        "design_condition": des_str,
                        "operating_condition": oper_str,
                        "source": doc_src
                    })

        node_def["parameters"] = params
        return node_def

    def confirm_node_definition(self, node_def: Dict[str, Any]) -> Dict[str, Any]:
        """Saves confirmed node definition into wiki/hazop/nodes/<node_id>.md and updates study register."""
        node_id = node_def.get("node_id", "CDN-N02")
        node_def["status"] = "CONFIRMED"
        
        # Ensure wiki directory exists
        nodes_dir = Path("wiki/hazop/nodes")
        nodes_dir.mkdir(parents=True, exist_ok=True)
        
        # Write markdown node document
        node_file = nodes_dir / f"{node_id.lower()}.md"
        content = f"""---
name: {node_def.get('name', 'HAZOP Node')}
node_id: {node_id}
markup_label: "{node_def.get('markup_label', '')}"
unit: {node_def.get('unit', 'CDN')}
pid_sheet: "{', '.join(node_def.get('pid_drawings', []))}"
pid_marked_up: "{node_def.get('source_file', '')}"
inlet_boundary: "{node_def.get('inlet_boundary', '')}"
outlet_boundary: "{node_def.get('outlet_boundary', '')}"
tags: [hazop, node, {node_def.get('unit', 'CDN')}, confirmed]
last_updated: 2026-08-31
status: CONFIRMED by engineer; ready for interactive deviation review
---

# HAZOP Node {node_id} — {node_def.get('name', '')}

## Design Intent
{node_def.get('design_intent', '')}

## Node Boundaries
- **Inlet Boundary:** {node_def.get('inlet_boundary', '')}
- **Outlet Boundary:** {node_def.get('outlet_boundary', '')}

## Normal Operating Parameters
| Tag | Stream / Side | Design Condition | Operating Condition | Source |
|-----|---------------|------------------|---------------------|--------|
"""
        for p in node_def.get("parameters", []):
            content += f"| **{p.get('tag')}** | {p.get('stream')} | {p.get('design_condition')} | {p.get('operating_condition')} | {p.get('source')} |\n"

        content += "\n## HAZOP Worksheet\n"
        with open(node_file, "w", encoding="utf-8") as f:
            f.write(content)

        return {
            "status": "CONFIRMED",
            "node_id": node_id,
            "filepath": str(node_file),
            "message": f"Node {node_id} confirmed and registered. Ready for 14-parameter deviation analysis."
        }

    def evaluate_1st_risk_hitl(
        self,
        people: int,
        env: int,
        econ: int,
        social: int,
        initial_likelihood: int
    ) -> Dict[str, Any]:
        """HITL Gate 1: Proposes initial unmitigated risk for engineer review & adjustment."""
        return evaluate_1st_risk(people, env, econ, social, initial_likelihood)

    def propose_safeguards_hitl(
        self,
        equipment_tag: str,
        deviation_type: str = "Flow"
    ) -> List[Dict[str, Any]]:
        """HITL Gate 2: Proposes existing safeguards and calculated IPL credits directly from database."""
        # 1. Query interlocks from graph
        interlocks = self.db.graph_find_interlocks(equipment_tag)
        safeguards = []
        for it in interlocks:
            sil = it.get("sil_rating", "SIL 1")
            voting = it.get("voting_logic", "1oo1")
            act = it.get("interlock_action", "Trip")
            tag = it.get("instrument_tag", "")
            ipl_credit = 2 if "SIL 2" in sil else (1 if "SIL 1" in sil else 0)
            safeguards.append({
                "description": f"{tag} ({voting}, {sil}) {act}",
                "il_esd": "Yes",
                "sil_rating": sil,
                "is_ipl": ipl_credit > 0,
                "ipl_credit": ipl_credit
            })

        # 2. Query relational safeguards associated with equipment tag from causes/consequences
        matching_causes = [
            c for c in self.db.causes.values()
            if getattr(c, "equipment_tag", "") == equipment_tag
        ]
        seen_desc = set(s["description"] for s in safeguards)
        for c in matching_causes:
            c_conseqs = [cq for cq in self.db.consequences.values() if getattr(cq, "cause_id", "") == getattr(c, "cause_id", "")]
            for cq in c_conseqs:
                c_sgs = [sg for sg in self.db.safeguards.values() if getattr(sg, "consequence_id", "") == getattr(cq, "consequence_id", "")]
                for sg in c_sgs:
                    desc = getattr(sg, "description", "")
                    if desc and desc not in seen_desc:
                        seen_desc.add(desc)
                        is_esd = getattr(sg, "is_interlock_esd", False)
                        ipl = getattr(sg, "ipl_credit_level", 1 if is_esd else 0)
                        safeguards.append({
                            "description": desc,
                            "il_esd": "Yes" if is_esd else "No",
                            "sil_rating": "SIL 1" if is_esd else "None",
                            "is_ipl": ipl > 0,
                            "ipl_credit": ipl
                        })

        return safeguards

    def discover_node_risks(self, node_id: str, equipment_tags: Optional[List[str]] = None) -> List[Dict[str, Any]]:
        """Discovers and populates all candidate deviations, causes, and safeguards for a node directly from database."""
        # 1. Resolve normalized node ID dynamically against registered database HAZOP nodes
        target_nid = resolve_hazop_node_id(node_id, self.db.hazop_nodes)

        # 2. Query all Deviations for target node from db
        matching_devs = [
            d for d in self.db.deviations.values()
            if getattr(d, "node_id", "") == target_nid
        ]
        # If no deviations match exact target_nid, try fallback match on node_id substring or equipment tag map
        if not matching_devs:
            matching_devs = [
                d for d in self.db.deviations.values()
                if getattr(d, "node_id", "") in target_nid or target_nid in getattr(d, "node_id", "")
            ]

        matching_devs.sort(key=lambda d: getattr(d, "sequence_number", 0))

        discovered = []
        for dev in matching_devs:
            dev_id = getattr(dev, "deviation_id", "")
            param = getattr(dev, "parameter", "")
            dev_label = getattr(dev, "deviation_label", "")
            seq = getattr(dev, "sequence_number", 1)

            # Find Causes
            matching_causes = [
                c for c in self.db.causes.values()
                if getattr(c, "deviation_id", "") == dev_id
            ]

            cause_idx = 1
            for cause in matching_causes:
                c_id = getattr(cause, "cause_id", "")
                c_desc = getattr(cause, "description", "")
                c_eq = getattr(cause, "equipment_tag", "")

                # Find Consequences
                matching_conseqs = [
                    cq for cq in self.db.consequences.values()
                    if getattr(cq, "cause_id", "") == c_id
                ]

                conseq_idx = 1
                for cq in matching_conseqs:
                    cq_id = getattr(cq, "consequence_id", "")
                    chain = getattr(cq, "causal_chain", "")
                    p_sev = getattr(cq, "severity_people", 5)
                    en_sev = getattr(cq, "severity_environment", 4)
                    ec_sev = getattr(cq, "severity_economic", 5)
                    s_sev = getattr(cq, "severity_social", 4)
                    init_l = getattr(cq, "initial_likelihood", 4)

                    # Find Safeguards
                    matching_sgs = [
                        sg for sg in self.db.safeguards.values()
                        if getattr(sg, "consequence_id", "") == cq_id
                    ]

                    available_sgs = []
                    active_ipl_count = 0
                    for sg in matching_sgs:
                        is_esd = getattr(sg, "is_interlock_esd", False)
                        inst_tag = getattr(sg, "instrument_tag", "")
                        inst_obj = self.db.instruments.get(inst_tag)
                        sil = getattr(inst_obj, "sil_rating", "SIL 1") if is_esd else "None"
                        ipl = getattr(sg, "ipl_credit_level", 1 if is_esd else 0)

                        is_selected = True
                        if ipl > 0:
                            if active_ipl_count + ipl <= 2:
                                is_selected = True
                                active_ipl_count += ipl
                            else:
                                is_selected = False
                        else:
                            is_selected = True

                        available_sgs.append({
                            "description": getattr(sg, "description", ""),
                            "il_esd": "Yes" if is_esd else "No",
                            "sil_rating": sil,
                            "is_ipl": ipl > 0,
                            "ipl_credit": ipl,
                            "selected": is_selected
                        })

                    row = {
                        "ref": f"{seq}.{cause_idx}.{conseq_idx}",
                        "parameter": param,
                        "deviation": dev_label,
                        "cause": c_desc,
                        "consequence": chain,
                        "wo_p": p_sev,
                        "wo_en": en_sev,
                        "wo_ec": ec_sev,
                        "wo_s": s_sev,
                        "wo_l": init_l,
                        "available_safeguards": available_sgs
                    }
                    discovered.append(row)
                    conseq_idx += 1
                cause_idx += 1

        # Evaluate each row
        evaluated_rows = []
        for r in discovered:
            eval_res = self.evaluate_row(r)
            evaluated_rows.append(eval_res)

        return evaluated_rows

    def evaluate_row(self, row_data: Dict[str, Any]) -> Dict[str, Any]:
        """Evaluates a single worksheet row: computes initial risk, active IPLs, mitigated risk, and recommendation."""
        people = int(row_data.get("wo_p", 5))
        env = int(row_data.get("wo_en", 4))
        econ = int(row_data.get("wo_ec", 5))
        social = int(row_data.get("wo_s", 4))
        initial_l = int(row_data.get("wo_l", 4))

        # Initial 1st Risk evaluation
        first_risk = evaluate_1st_risk(people, env, econ, social, initial_l)

        # Filter active safeguards
        all_sgs = row_data.get("available_safeguards", row_data.get("safeguards", []))
        selected_sgs = [s for s in all_sgs if s.get("selected", True)]

        # Mitigated 2nd Risk evaluation
        second_risk = evaluate_2nd_risk(first_risk, selected_sgs, override_mitigated_likelihood=row_data.get("override_mitigated_likelihood"))

        # AI Recommendation
        dev = row_data.get("deviation", "Flow — No / Low Flow")
        cause = row_data.get("cause", "")
        conseq = row_data.get("consequence", "")
        rec_text = row_data.get("recommendation", "")

        if not rec_text or rec_text == "None — risk acceptable" or "Verify" in rec_text:
            if second_risk["requires_action"]:
                # Generate realistic recommendation
                param_name = dev.split("—")[0].strip()
                rec_text = f"Verify proof test interval and SIL compliance for credited {param_name} interlock safeguard."
                use_live = row_data.get("fetch_ai_recommendation", False) and (self.use_vertex or self.api_key) and not os.getenv("PYTEST_CURRENT_TEST")
                if use_live:
                    try:
                        prompt = (
                            f"As a Senior Process Safety Expert for Refinery Phenol Plant, formulate a concise, actionable HAZOP recommendation (format: [Action Verb] + [Specific Target Tag] + [Purpose]):\n"
                            f"Deviation: {dev}\nCause: {cause}\nConsequence: {conseq}\n"
                            f"Initial Risk: {first_risk['initial_risk_rating']} -> Mitigated Risk: {second_risk['mitigated_risk_rating']}\n"
                            f"Active Safeguards: {[s.get('description') for s in selected_sgs]}\n\n"
                            f"Provide one actionable engineering recommendation (max 2 sentences)."
                        )
                        if self.use_vertex:
                            from google import genai
                            client = genai.Client(vertexai=True, project=self.project, location=self.region)
                            resp = client.models.generate_content(model=self.model_name, contents=prompt)
                            if resp and resp.text:
                                rec_text = resp.text.strip()
                        elif self.api_key:
                            url = f"https://generativelanguage.googleapis.com/v1beta/models/{self.model_name}:generateContent?key={self.api_key}"
                            payload = {"contents": [{"parts": [{"text": prompt}]}]}
                            with httpx.Client(timeout=1.5) as client:
                                resp = client.post(url, json=payload)
                                if resp.status_code == 200:
                                    rec_text = resp.json()["candidates"][0]["content"]["parts"][0]["text"].strip()
                    except Exception as e:
                        pass
            else:
                rec_text = "None — risk acceptable"

        return {
            "ref": row_data.get("ref", "1.1.1"),
            "parameter": row_data.get("parameter", dev.split("—")[0].strip()),
            "deviation": dev,
            "cause": cause,
            "consequence": conseq,
            "wo_p": people,
            "wo_en": env,
            "wo_ec": econ,
            "wo_s": social,
            "wo_l": initial_l,
            "wo_s_overall": first_risk["overall_severity"],
            "wo_rr": first_risk["initial_risk_rating"],
            "available_safeguards": all_sgs,
            "safeguards": selected_sgs,
            "total_ipl_credits": second_risk["total_ipl_credits"],
            "w_p": people,
            "w_en": env,
            "w_ec": econ,
            "w_s": social,
            "w_l": second_risk["mitigated_likelihood"],
            "w_s_overall": second_risk["overall_severity"],
            "w_rr": second_risk["mitigated_risk_rating"],
            "recommendation": rec_text,
            "requires_action": second_risk["requires_action"]
        }

    def generate_scenario_row(
        self,
        node_id: str,
        equipment_tags: Optional[List[str]] = None,
        scenario_text: str = "",
        existing_rows_count: int = 5
    ) -> Dict[str, Any]:
        """Generates a complete structured HAZOP worksheet row from a natural language scenario using process knowledge."""
        text = scenario_text.lower().strip()
        tags = equipment_tags or ["E-2302A/B", "E-2303"]
        tags_str = ", ".join(tags)
        ref_num = f"1.{existing_rows_count + 1}.1"

        # Defaults
        param = "Service Failures"
        dev = "Loss of Utility"
        cause = f"Failure scenario: {scenario_text}"
        conseq = f"Unmitigated impact on {tags_str} leading to loss of process control"
        wo_p, wo_en, wo_ec, wo_s, wo_l = 4, 3, 4, 3, 3
        sgs = [
            {"description": "Standard SIS trip interlock with fail-safe position", "il_esd": "Yes", "sil_rating": "SIL 1", "is_ipl": True, "ipl_credit": 1, "selected": True},
            {"description": "DCS process alarm and operator manual intervention", "il_esd": "No", "sil_rating": "None", "is_ipl": False, "ipl_credit": 0, "selected": True}
        ]

        if "air" in text or "instrument" in text or "pneumatic" in text:
            param = "Service Failures"
            dev = "Loss of Utility — Instrument Air"
            cause = "Loss of instrument air supply -> SC1.5 steam control valve TV-0501 fails open to maximum heating"
            conseq = "Oxidate in E-2303 overheats >80°C -> accelerated CHP thermal decomposition and rapid vapor generation"
            wo_p, wo_en, wo_ec, wo_s, wo_l = 5, 4, 5, 4, 3
            sgs = [
                {"description": "TXSHH-0501 (1oo1, SIL 1) trips UC-2301 steam supply valve", "il_esd": "Yes", "sil_rating": "SIL 1", "is_ipl": True, "ipl_credit": 1, "selected": True},
                {"description": "TXSHH-0502A/B (1oo2, SIL 1) trips UXV-0501/0502 via spring-return fail-closed actuators", "il_esd": "Yes", "sil_rating": "SIL 1", "is_ipl": True, "ipl_credit": 1, "selected": True},
                {"description": "PA-0901 low instrument air header pressure alarm in DCS (BPCS)", "il_esd": "No", "sil_rating": "None", "is_ipl": False, "ipl_credit": 0, "selected": True}
            ]
        elif "power" in text or "electric" in text or "blackout" in text:
            param = "Service Failures"
            dev = "Loss of Utility — Power"
            cause = "Loss of electrical power supply -> P-2308A/B condensate return pumps trip / feed pumps trip"
            conseq = "E-2303 condensate flooding -> loss of heat transfer control & hydraulic overpressure risk"
            wo_p, wo_en, wo_ec, wo_s, wo_l = 4, 3, 4, 3, 3
            sgs = [
                {"description": "UXV-0501/0502 de-energize to trip steam supply (Fail-Closed spring-return)", "il_esd": "Yes", "sil_rating": "SIL 1", "is_ipl": True, "ipl_credit": 1, "selected": True},
                {"description": "UPS backup power for DCS and SIS instrumentation (30 min reserve)", "il_esd": "Yes", "sil_rating": "SIL 1", "is_ipl": True, "ipl_credit": 1, "selected": True},
                {"description": "Electrical substation bus-tie alarm in DCS", "il_esd": "No", "sil_rating": "None", "is_ipl": False, "ipl_credit": 0, "selected": True}
            ]
        elif "tube" in text or "leak" in text or "rupture" in text:
            param = "Composition / As Well As"
            dev = "Tube Leak / Rupture (E-2303)"
            cause = "E-2303 tube rupture between SC1.5 steam tube side and oxidate process shell side"
            conseq = "High pressure steam ingresses into CHP stream -> rapid overpressure and possible thermal decomposition"
            wo_p, wo_en, wo_ec, wo_s, wo_l = 5, 4, 5, 4, 2
            sgs = [
                {"description": "PSV-0501 thermal relief valve sized for tube rupture fire case", "il_esd": "Yes", "sil_rating": "SIL 1", "is_ipl": True, "ipl_credit": 1, "selected": True},
                {"description": "TXSHH-0501 high temperature trip on steam inlet to E-2303", "il_esd": "Yes", "sil_rating": "SIL 1", "is_ipl": True, "ipl_credit": 1, "selected": True},
                {"description": "D-2308 condensate collection drum high pressure monitor", "il_esd": "No", "sil_rating": "None", "is_ipl": False, "ipl_credit": 0, "selected": True}
            ]
        elif "acid" in text or "rust" in text or "contaminat" in text or "metal" in text or "iron" in text:
            param = "Composition"
            dev = "Other Than (Chemical Contamination)"
            cause = "Transition metal (Fe/Cu/Mn) or inorganic acid ingress upstream into oxidate feed stream"
            conseq = "Catalytic acceleration of CHP cleavage runaway decomposition -> catastrophic vessel rupture"
            wo_p, wo_en, wo_ec, wo_s, wo_l = 5, 5, 5, 5, 2
            sgs = [
                {"description": "Online pH and transition metal continuous analyzer at battery limits", "il_esd": "Yes", "sil_rating": "SIL 1", "is_ipl": True, "ipl_credit": 1, "selected": True},
                {"description": "Feed basket strainers X-2302A/B and 316L stainless metallurgy", "il_esd": "Yes", "sil_rating": "SIL 1", "is_ipl": True, "ipl_credit": 1, "selected": True},
                {"description": "Automated emergency feed diversion valve XV-0402 to slop tank", "il_esd": "Yes", "sil_rating": "SIL 1", "is_ipl": True, "ipl_credit": 1, "selected": True}
            ]
        elif "seal" in text or "flush" in text or "nitrogen" in text:
            param = "Service Failures"
            dev = "Loss of Utility — Seal Flush"
            cause = "Loss of cumene seal flush + N2 barrier to P-2308A/B pumps"
            conseq = "Mechanical seal dry running and failure -> hot hazardous material release to atmosphere"
            wo_p, wo_en, wo_ec, wo_s, wo_l = 4, 4, 3, 3, 3
            sgs = [
                {"description": "Dual pressurized mechanical seals with API Plan 53B barrier system", "il_esd": "Yes", "sil_rating": "SIL 1", "is_ipl": True, "ipl_credit": 1, "selected": True},
                {"description": "PDAH-0902 seal pot low pressure alarm in DCS", "il_esd": "No", "sil_rating": "None", "is_ipl": False, "ipl_credit": 0, "selected": True}
            ]
        elif "reverse" in text or "backflow" in text:
            param = "Flow"
            dev = "Flow — Reverse Flow"
            cause = "N/A — not credible: feed delivered under positive pump pressure from upstream Node 23-01"
            conseq = "No physical damage identified under normal operating forward pump pressure"
            wo_p, wo_en, wo_ec, wo_s, wo_l = 1, 1, 1, 1, 1
            sgs = [
                {"description": "Dual mechanical non-return check valves on pump discharge", "il_esd": "No", "sil_rating": "None", "is_ipl": False, "ipl_credit": 0, "selected": True}
            ]
        elif "low temp" in text or "cold" in text or "freeze" in text:
            param = "Temperature"
            dev = "Temperature — Low Temperature"
            cause = "Loss of SC1.5 steam supply to E-2303 heater / TV-0501 fails closed"
            conseq = "Oxidate temperature drops below 75°C -> suboptimal preflash column separation and increased cleavage viscosity"
            wo_p, wo_en, wo_ec, wo_s, wo_l = 2, 1, 3, 1, 3
            sgs = [
                {"description": "TAL-0501 low temperature alarm in DCS", "il_esd": "No", "sil_rating": "None", "is_ipl": False, "ipl_credit": 0, "selected": True},
                {"description": "Steam supply low header pressure alarm", "il_esd": "No", "sil_rating": "None", "is_ipl": False, "ipl_credit": 0, "selected": True}
            ]
        else:
            # General prompt scenario
            dev = f"Scenario — {scenario_text[:40]}"
            cause = scenario_text
            conseq = f"Deviation in {tags_str} leading to process upset and potential thermal/pressure escalation"
            wo_p, wo_en, wo_ec, wo_s, wo_l = 4, 3, 4, 3, 3

        row_raw = {
            "ref": ref_num,
            "parameter": param,
            "deviation": dev,
            "cause": cause,
            "consequence": conseq,
            "wo_p": wo_p,
            "wo_en": wo_en,
            "wo_ec": wo_ec,
            "wo_s": wo_s,
            "wo_l": wo_l,
            "available_safeguards": sgs,
            "recommendation": ""
        }

        # Evaluate and return complete row
        return self.evaluate_row(row_raw)

    def evaluate_2nd_risk_and_recommendation_hitl(
        self,
        deviation: str,
        cause: str,
        consequence: str,
        first_risk: Dict[str, Any],
        confirmed_safeguards: List[Dict[str, Any]],
        override_mitigated_likelihood: Optional[int] = None
    ) -> Dict[str, Any]:
        """HITL Gate 3: Evaluates 2nd Risk (Mitigated Risk) and generates AI Recommendation."""
        risk_res = evaluate_2nd_risk(first_risk, confirmed_safeguards, override_mitigated_likelihood)
        
        # Live Gemini AI Recommendation
        rec_text = "None — risk acceptable"
        discipline = "N/A"
        
        if risk_res["requires_action"]:
            rec_text = "Verify proof test interval for 1oo2 SIL 1 interlock."
            discipline = "Instrument / Process"
            
            use_live = (self.use_vertex or self.api_key) and not os.getenv("PYTEST_CURRENT_TEST")
            if use_live:
                try:
                    prompt = (
                        f"As a Senior Process Safety Expert for Refinery Phenol Plant, formulate a concise, actionable HAZOP recommendation (format: [Action Verb] + [Specific Target Tag] + [Purpose]):\n"
                        f"Deviation: {deviation}\nCause: {cause}\nConsequence: {consequence}\n"
                        f"Initial Risk: {risk_res['initial_risk_rating']} -> Mitigated Risk: {risk_res['mitigated_risk_rating']}\n"
                        f"Safeguards: {confirmed_safeguards}\n\n"
                        f"Provide one actionable engineering recommendation (max 2 sentences)."
                    )
                    if self.use_vertex:
                        from google import genai
                        client = genai.Client(vertexai=True, project=self.project, location=self.region)
                        resp = client.models.generate_content(model=self.model_name, contents=prompt)
                        if resp and resp.text:
                            rec_text = resp.text.strip()
                    elif self.api_key:
                        url = f"https://generativelanguage.googleapis.com/v1beta/models/{self.model_name}:generateContent?key={self.api_key}"
                        payload = {"contents": [{"parts": [{"text": prompt}]}]}
                        with httpx.Client(timeout=6.0) as client:
                            resp = client.post(url, json=payload)
                            if resp.status_code == 200:
                                rec_text = resp.json()["candidates"][0]["content"]["parts"][0]["text"].strip()
                except Exception as e:
                    print(f"[HAZOP LIVE GEMINI/VERTEX RECOMMENDATION FALLBACK] {e}")

        return {
            "status": "EVALUATED",
            "deviation": deviation,
            "cause": cause,
            "consequence": consequence,
            "risk_assessment": risk_res,
            "ai_recommendation": rec_text,
            "discipline": discipline
        }

    def evaluate_deviation(
        self,
        deviation: str,
        cause: str,
        consequence: str,
        people: int,
        env: int,
        econ: int,
        social: int,
        initial_likelihood: int,
        safeguards: List[Dict[str, Any]],
        override_mitigated_likelihood: Optional[int] = None
    ) -> Dict[str, Any]:
        """Unified deviation evaluation for backward compatibility and automated testing."""
        first = self.evaluate_1st_risk_hitl(people, env, econ, social, initial_likelihood)
        return self.evaluate_2nd_risk_and_recommendation_hitl(
            deviation=deviation,
            cause=cause,
            consequence=consequence,
            first_risk=first,
            confirmed_safeguards=safeguards,
            override_mitigated_likelihood=override_mitigated_likelihood
        )

    def export_study_workbook(
        self,
        study_metadata: Dict[str, Any],
        worksheet_rows: List[Dict[str, Any]],
        output_filepath: str = "output/exports/HAZOP_Study_Report.xlsx"
    ) -> str:
        """Generates audit-compliant 7-tab Excel workbook matching hazop-example/*.xlsx."""
        return export_hazop_study_to_excel(study_metadata, worksheet_rows, output_filepath)

    def finalize_study_and_sync(
        self,
        study_metadata: Dict[str, Any],
        worksheet_rows: List[Dict[str, Any]],
        output_filepath: str = ""
    ) -> Dict[str, Any]:
        """Finalizes HAZOP study: updates Wiki markdown, Spanner graph, and Dataplex Knowledge Catalog."""
        node_id = study_metadata.get("node_id", "CDN-N02")
        unit_id = study_metadata.get("unit", "CDN")
        node_name = study_metadata.get("name", "HAZOP Study Node")
        pid_drawings = study_metadata.get("pid_drawings", [])
        equipment_tags = study_metadata.get("equipment_tags", [])
        
        if not output_filepath:
            out_dir = Path("output/exports")
            out_dir.mkdir(parents=True, exist_ok=True)
            output_filepath = str(out_dir / f"{node_id}_HAZOP-worksheet.xlsx")

        # 1. Generate 7-Tab Excel Deliverable
        saved_excel_path = self.export_study_workbook(study_metadata, worksheet_rows, output_filepath)

        # 2. Update Wiki Markdown Node File
        node_wiki_file = Path("wiki/hazop/nodes") / f"{node_id.lower()}.md"
        if node_wiki_file.exists():
            content = node_wiki_file.read_text(encoding="utf-8")
            content = content.replace("status: CONFIRMED", "status: COMPLETE — Closed-out & certified")
            content = content.replace("status: PRELIMINARY", "status: COMPLETE — Closed-out & certified")
            
            # Append worksheet summary section if not already present
            if "## Finalized Worksheet Rows" not in content and worksheet_rows:
                content += "\n\n## Finalized Worksheet Rows\n"
                content += "| Ref | Parameter | Deviation | Cause | Consequence | Initial Risk | Mitigated Risk | Recommendation |\n"
                content += "|---|---|---|---|---|---|---|---|\n"
                for r in worksheet_rows:
                    ref = r.get("ref", "1.1.1")
                    param = r.get("parameter", "Flow")
                    dev = r.get("deviation", "")
                    cause = r.get("cause", "")
                    cons = r.get("consequence", "")
                    init_rr = r.get("wo_rr", r.get("initial_risk", "Extreme"))
                    mit_rr = r.get("w_rr", r.get("mitigated_risk", "High"))
                    rec = r.get("recommendation", r.get("rec_text", "N/A"))
                    content += f"| {ref} | {param} | {dev} | {cause} | {cons} | {init_rr} | {mit_rr} | {rec} |\n"
            
            node_wiki_file.write_text(content, encoding="utf-8")

        # 3. Synchronize Cloud Spanner Graph
        if hasattr(self.db, "hazop_nodes"):
            from database.models import HazopNodeModel, NodeEquipmentEdge
            self.db.hazop_nodes[node_id] = HazopNodeModel(
                node_id=node_id,
                unit_id=unit_id,
                name=node_name,
                pid_sheet=",".join(pid_drawings),
                status="COMPLETE"
            )
            for eq_tag in equipment_tags:
                self.db.node_equipment_map.append(NodeEquipmentEdge(
                    node_id=node_id,
                    equipment_tag=eq_tag
                ))

        # 4. Synchronize Google Cloud Dataplex Knowledge Catalog
        study_date = datetime.now().strftime("%Y%m%d")
        entry_id = f"hazop-{node_id.lower()}-{study_date}"
        recs = [r for r in worksheet_rows if r.get("recommendation") or r.get("rec_text")]
        
        catalog_entry_data = {
            "entry_id": entry_id,
            "entry_group": "projects/cs-poc-y03r7kmfyov4kilzg50fd7s/locations/asia-southeast1/entryGroups/phenol-psi",
            "display_name": f"HAZOP Study Worksheet — {node_id} ({node_name})",
            "description": f"Refinery Phenol Train II — Formal HAZOP Review for {node_id}. Governed by W-(Q-MP)-002 R2.",
            "psi_category": 6,  # Category 6: Process Hazard Analysis & HAZOP
            "status": "COMPLETE",
            "linked_drawings": pid_drawings,
            "linked_equipment": equipment_tags,
            "deliverable_uri": str(saved_excel_path),
            "aspects": {
                "oems_005_process_safety_aspect": {
                    "category_id": 6,
                    "unit_code": unit_id,
                    "study_status": "COMPLETE",
                    "governing_standard": "W-(Q-MP)-002 R2 (5x5 RAM)",
                    "active_recommendation_count": len(recs),
                    "linked_drawings": pid_drawings,
                    "linked_equipment": equipment_tags,
                    "as_built_certified": True,
                    "last_catalog_sync": datetime.now().strftime("%Y-%m-%d")
                }
            },
            "last_updated": datetime.now().strftime("%Y-%m-%d")
        }

        if hasattr(self.db, "register_knowledge_catalog_entry"):
            self.db.register_knowledge_catalog_entry(entry_id, catalog_entry_data)

        # 5. Append Activity Log
        log_file = Path("wiki/log.md")
        if log_file.exists():
            with open(log_file, "a", encoding="utf-8") as lf:
                lf.write(f"\n- **{datetime.now().strftime('%Y-%m-%d %H:%M')}**: HAZOP Study for Node **{node_id}** finalized. Registered in Dataplex Knowledge Catalog (`{entry_id}`) and Spanner Graph with {len(recs)} action items.\n")

        return {
            "status": "FINALIZED_AND_SYNCED",
            "node_id": node_id,
            "excel_deliverable": str(saved_excel_path),
            "wiki_node_path": str(node_wiki_file),
            "spanner_node_status": "COMPLETE",
            "knowledge_catalog_entry": f"projects/cs-poc-y03r7kmfyov4kilzg50fd7s/locations/asia-southeast1/entryGroups/phenol-psi/entries/{entry_id}",
            "dataplex_aspects": catalog_entry_data["aspects"],
            "recommendations_registered": len(recs),
            "message": f"Successfully finalized HAZOP study for {node_id}. Synced to Wiki, Spanner Graph, and Dataplex Knowledge Catalog."
        }
