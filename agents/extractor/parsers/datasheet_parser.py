"""Process Data Sheet Markdown Synthesizer & Parser."""

from typing import Dict, Any, List
import yaml

def format_datasheet_markdown(
    tag: str,
    name: str,
    eq_type: str,
    unit: str,
    design_data: Dict[str, Any],
    operating_data: Dict[str, Any],
    source_pdf: str
) -> str:
    frontmatter = {
        "name": name,
        "tag": tag,
        "type": eq_type,
        "unit": unit,
        "design": design_data,
        "operating": operating_data,
        "sources": [source_pdf],
        "tags": ["equipment", "data-sheet", unit]
    }
    fm_text = yaml.safe_dump(frontmatter, sort_keys=False).strip()
    
    lines = [
        f"---",
        fm_text,
        f"---",
        f"",
        f"# {tag} — {name}",
        f"",
        f"## Design Data",
        f"",
        f"| Parameter | Value | Unit |",
        f"|-----------|-------|------|"
    ]
    for k, v in design_data.items():
        lines.append(f"| {k} | {v} | — |")
        
    lines.extend([
        f"",
        f"## Operating Conditions",
        f"",
        f"| Parameter | Value | Unit |",
        f"|-----------|-------|------|"
    ])
    for k, v in operating_data.items():
        lines.append(f"| {k} | {v} | — |")
        
    return "\n".join(lines)
