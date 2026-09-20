"""Anti-Bias Safety Engine.

Prevents anchoring bias by strictly halting fresh HAZOP studies if historical HAZOP reports are found in raw input.
"""

from pathlib import Path
from typing import List, Dict, Any


class AntiBiasException(Exception):
    pass


class AntiBiasScanner:
    @staticmethod
    def scan_input_directory(raw_dir: str = "raw") -> Dict[str, Any]:
        raw_path = Path(raw_dir)
        if not raw_path.exists():
            return {"status": "PASSED", "violating_files": []}

        violating_files: List[str] = []
        for file in raw_path.rglob("*"):
            if file.is_file():
                fn_lower = file.name.lower()
                if "hazop" in fn_lower or "pha_report" in fn_lower or "hazard_study" in fn_lower:
                    # Ignore template or standard files
                    if "template" not in fn_lower and "standard" not in fn_lower:
                        violating_files.append(str(file))

        if violating_files:
            return {
                "status": "VIOLATION",
                "message": (
                    f"ANTI-BIAS HALT: Found {len(violating_files)} historical HAZOP report(s) in '{raw_dir}'. "
                    f"To ensure an independent fresh study, historical reports must be moved to an archive directory before setup."
                ),
                "violating_files": violating_files
            }

        return {"status": "PASSED", "violating_files": []}
