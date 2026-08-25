"""HAZOP Study Agent Engine.

Facilitates interactive 9-step study lifecycle, anti-bias verification, PTT GC RAM calculations, and Excel export.
"""

from typing import Dict, Any, List
from agents.hazop.anti_bias import AntiBiasScanner, AntiBiasException
from agents.hazop.ram_evaluator import evaluate_deviation_risk
from agents.hazop.excel_exporter import export_hazop_study_to_excel


class HazopStudyAgent:
    def __init__(self, db_instance):
        self.db = db_instance
        self.scanner = AntiBiasScanner()

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
        safeguards: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """Evaluates risk and recommends safeguards per PTT GC RAM."""
        risk_res = evaluate_deviation_risk(people, env, econ, social, initial_likelihood, safeguards)
        return {
            "status": "EVALUATED",
            "deviation": deviation,
            "cause": cause,
            "consequence": consequence,
            "risk_assessment": risk_res
        }

    def export_study_workbook(
        self,
        study_metadata: Dict[str, Any],
        worksheet_rows: List[Dict[str, Any]],
        output_filepath: str = "output/exports/HAZOP_Study_Report.xlsx"
    ) -> str:
        """Generates audit-compliant 7-tab Excel workbook."""
        return export_hazop_study_to_excel(study_metadata, worksheet_rows, output_filepath)
