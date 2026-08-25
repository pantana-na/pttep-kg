#!/usr/bin/env python3
"""
Phenol Agent — Input File Classifier

Scans the input/ folder and classifies files into the correct raw/ subfolder
based on filename and content keywords. Can be run standalone or called by
the LLM assistant as a first-pass classifier.

Usage:
    python sort_input.py [--dry-run] [--verbose]

Flags:
    --dry-run   Show what would move without actually moving files
    --verbose   Print detailed classification reasoning
"""

import os
import sys
import shutil
import re
from pathlib import Path

BASE_DIR = Path(__file__).parent
INPUT_DIR = BASE_DIR / "input"
RAW_DIR = BASE_DIR / "raw"

DESTINATIONS = {
    "pfd":               RAW_DIR / "pfd",
    "pid":               RAW_DIR / "pid",
    "data_sheets":       RAW_DIR / "data_sheets",
    "operating_manuals": RAW_DIR / "operating_manuals",
    "assets":            RAW_DIR / "assets",
}

# --- Classification rules (checked in order; first match wins) ---

# Filename keyword rules — patterns matched against the full filename (case-insensitive)
FILENAME_RULES = [
    # PFD
    (r"\bpfd\b|process.flow.diagram|flow.diagram|block.flow",           "pfd"),
    # P&ID
    (r"\bpid\b|p&id|p_id|piping.and.instrument|piping.*instrument|instrument.*diagram",
                                                                         "pid"),
    # Data Sheets
    (r"data.sheet|datasheet|equipment.spec|spec.sheet|process.data|"
     r"heat.exchanger.*data|vessel.*data|pump.*data|compressor.*data|"
     r"column.*data|reactor.*data|ds[-_]\d",                            "data_sheets"),
    # Operating Manuals / Procedures
    (r"operating.manual|operation.manual|op.manual|startup|start.up|"
     r"shutdown|shut.down|emergency|procedure|sop|work.instruction|"
     r"maintenance.*manual|troubleshoot",                               "operating_manuals"),
    # Assets (images, drawings without other keywords)
    (r"\.(png|jpg|jpeg|gif|bmp|tiff|svg|dwg|dxf)$",                    "assets"),
]

# Content keyword rules — text scanned inside the file (plaintext only)
CONTENT_RULES = [
    (["process flow diagram", "pfd", "stream table", "mass balance",
      "heat and material balance", "h&mb"],                             "pfd"),
    (["piping and instrumentation", "p&id", "instrument list",
      "control valve", "safety valve", "psv", "prv",
      "interlock", "cause and effect"],                                 "pid"),
    (["data sheet", "design data", "operating conditions",
      "design pressure", "design temperature", "nozzle schedule",
      "heat duty", "tube side", "shell side", "impeller",
      "motor power", "npsh"],                                           "data_sheets"),
    (["operating procedure", "standard operating", "step 1", "step 2",
      "pre-startup", "post-startup", "normal operation",
      "emergency shutdown", "esd", "permit to work",
      "startup sequence", "shutdown sequence"],                         "operating_manuals"),
]

SKIP_FILES = {"DROP_FILES_HERE.md", ".DS_Store", "Thumbs.db", ".gitkeep"}

TEXT_EXTENSIONS = {".md", ".txt", ".csv", ".pdf", ".doc", ".docx", ".html", ".htm"}


def read_text_preview(path: Path, max_chars: int = 4000) -> str:
    """Return a lowercase text preview for content matching. Skips binary files."""
    if path.suffix.lower() not in TEXT_EXTENSIONS:
        return ""
    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            return f.read(max_chars).lower()
    except Exception:
        return ""


def classify(path: Path, verbose: bool = False) -> tuple[str | None, str]:
    """
    Returns (destination_key, reason) or (None, reason) if unclassified.
    destination_key is one of: pfd, pid, data_sheets, operating_manuals, assets
    """
    name_lower = path.name.lower()

    # 1. Filename rules
    for pattern, dest in FILENAME_RULES:
        if re.search(pattern, name_lower):
            reason = f"filename matched '{pattern}'"
            if verbose:
                print(f"  [filename] '{path.name}' → {dest} ({reason})")
            return dest, reason

    # 2. Content rules (text files only)
    content = read_text_preview(path)
    if content:
        scores: dict[str, int] = {}
        for keywords, dest in CONTENT_RULES:
            hits = sum(1 for kw in keywords if kw in content)
            if hits > 0:
                scores[dest] = scores.get(dest, 0) + hits

        if scores:
            best = max(scores, key=lambda k: scores[k])
            reason = f"content matched {scores[best]} keyword(s) for '{best}'"
            if verbose:
                print(f"  [content]  '{path.name}' → {best} ({reason})")
            return best, reason

    # 3. Image/binary fallback
    if path.suffix.lower() in {".png", ".jpg", ".jpeg", ".gif", ".bmp",
                                ".tiff", ".svg", ".dwg", ".dxf"}:
        return "assets", "image/drawing file extension"

    return None, "no classification rule matched"


def sort_input(dry_run: bool = False, verbose: bool = False) -> list[dict]:
    """
    Scan input/ and classify/move files. Returns a results list.
    Each entry: {file, destination, reason, status}
    """
    results = []

    files = [f for f in INPUT_DIR.iterdir()
             if f.is_file() and f.name not in SKIP_FILES]

    if not files:
        print("input/ is empty — nothing to sort.")
        return results

    print(f"Found {len(files)} file(s) in input/\n")

    for f in sorted(files):
        dest_key, reason = classify(f, verbose=verbose)

        if dest_key is None:
            status = "UNCLASSIFIED"
            dest_path = None
            print(f"  ? {f.name}")
            print(f"    → UNCLASSIFIED ({reason})")
            print(f"    → Ask the user where this file belongs\n")
        else:
            dest_dir = DESTINATIONS[dest_key]
            dest_path = dest_dir / f.name

            if dest_path.exists():
                # Avoid overwriting — add a suffix
                stem = f.stem
                suffix = f.suffix
                i = 1
                while dest_path.exists():
                    dest_path = dest_dir / f"{stem}_{i}{suffix}"
                    i += 1

            if dry_run:
                status = "DRY-RUN"
                print(f"  [DRY-RUN] {f.name}")
                print(f"    → raw/{dest_key}/{dest_path.name}")
                print(f"    reason: {reason}\n")
            else:
                shutil.move(str(f), str(dest_path))
                status = "MOVED"
                print(f"  MOVED: {f.name}")
                print(f"    → raw/{dest_key}/{dest_path.name}")
                print(f"    reason: {reason}\n")

        results.append({
            "file": f.name,
            "destination": f"raw/{dest_key}/{dest_path.name}" if dest_path else None,
            "reason": reason,
            "status": status,
        })

    return results


def print_summary(results: list[dict]) -> None:
    moved = [r for r in results if r["status"] == "MOVED"]
    unclassified = [r for r in results if r["status"] == "UNCLASSIFIED"]

    print("=" * 50)
    print(f"Summary: {len(moved)} moved, {len(unclassified)} unclassified")

    if unclassified:
        print("\nUnclassified files (manual action required):")
        for r in unclassified:
            print(f"  - {r['file']}")
        print("\nTell the assistant which folder each unclassified file belongs to,")
        print("or move them manually to raw/pfd/, raw/pid/, raw/data_sheets/,")
        print("raw/operating_manuals/, or raw/assets/")

    if moved:
        print("\nNext step: tell the assistant:")
        for r in moved:
            print(f"  Ingest {r['destination']}")


if __name__ == "__main__":
    dry_run = "--dry-run" in sys.argv
    verbose = "--verbose" in sys.argv

    if dry_run:
        print("DRY RUN MODE — no files will be moved\n")

    results = sort_input(dry_run=dry_run, verbose=verbose)
    if results:
        print_summary(results)
