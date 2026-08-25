"""Process Flow Diagram (PFD) Markdown Synthesizer & Parser."""

from typing import Dict, Any, List
import yaml

def format_pfd_markdown(
    unit_id: str,
    unit_name: str,
    equipment_list: List[Dict[str, Any]],
    streams: List[Dict[str, Any]],
    source_pdf: str
) -> str:
    frontmatter = {
        "unit_id": unit_id,
        "name": unit_name,
        "type": "unit-summary",
        "sources": [source_pdf],
        "tags": ["unit", "pfd", unit_id]
    }
    fm_text = yaml.safe_dump(frontmatter, sort_keys=False).strip()
    
    lines = [
        f"---",
        fm_text,
        f"---",
        f"",
        f"# {unit_name} ({unit_id}) — Process Flow Overview",
        f"",
        f"## Major Equipment",
        f"",
        f"| Tag | Name | Type | Operating Temp (°C) | Operating Pressure (barg) |",
        f"|-----|------|------|----------------------|----------------------------|"
    ]
    for eq in equipment_list:
        lines.append(f"| {eq.get('tag')} | {eq.get('name')} | {eq.get('type')} | {eq.get('temp', '—')} | {eq.get('pressure', '—')} |")
        
    lines.extend([
        f"",
        f"## Heat & Material Balances",
        f"",
        f"| Stream | From | To | Flow (kg/h) | Temp (°C) | Pressure (barg) | CHP (wt%) |",
        f"|--------|------|----|-------------|-----------|-----------------|-----------|"
    ])
    for s in streams:
        lines.append(f"| {s.get('stream_id')} | {s.get('from')} | {s.get('to')} | {s.get('flow', '—')} | {s.get('temp', '—')} | {s.get('pressure', '—')} | {s.get('chp', '—')} |")
        
    return "\n".join(lines)
