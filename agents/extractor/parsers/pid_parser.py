"""Piping & Instrumentation Diagram (P&ID) Markdown Synthesizer & Parser."""

from typing import Dict, Any, List
import yaml

def format_pid_markdown(
    drawing_no: str,
    title: str,
    unit: str,
    equipment_tags: List[str],
    instrument_loops: List[Dict[str, Any]],
    source_pdf: str
) -> str:
    frontmatter = {
        "title": title,
        "type": "source-summary",
        "drawing_number": drawing_no,
        "unit": unit,
        "equipment": equipment_tags,
        "sources": [source_pdf],
        "tags": ["pid", "drawing", unit]
    }
    fm_text = yaml.safe_dump(frontmatter, sort_keys=False).strip()
    
    lines = [
        f"---",
        fm_text,
        f"---",
        f"",
        f"# P&ID: {drawing_no} — {title}",
        f"",
        f"**Unit:** {unit} | **Drawing:** `{drawing_no}`",
        f"",
        f"## Equipment Shown",
        f""
    ]
    for tag in equipment_tags:
        lines.append(f"- [[equipment/{tag}]]")
        
    lines.extend([
        f"",
        f"## Key Instrument & Control Loops",
        f"",
        f"| Tag | Type | Description | Interlock / Setpoint |",
        f"|-----|------|-------------|----------------------|"
    ])
    for inst in instrument_loops:
        lines.append(f"| {inst.get('tag')} | {inst.get('type')} | {inst.get('description')} | {inst.get('setpoint', '—')} |")
        
    return "\n".join(lines)
