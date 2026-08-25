"""Two-Tier Human-in-the-Loop Clarification State Machine & Cascade Manager.

Implements N-Turn Progressive Disambiguation, Context Frame Stacking, and MAX_DEPTH=3 Fallback.
SPEC-20260824-MULTI-AGENT-CLOUD-ARCHITECTURE Section 2.2 & 2.2.2.
"""

from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field

MAX_CLARIFICATION_DEPTH = 3


class ClarificationOption(BaseModel):
    id: str
    label: str
    description: str
    target_tag: str


class ClarificationFrame(BaseModel):
    depth: int = Field(..., ge=1, le=MAX_CLARIFICATION_DEPTH)
    question: str
    options: List[ClarificationOption]
    breadcrumbs: List[str] = Field(default_factory=list)
    allow_write_in: bool = True
    context_data: Dict[str, Any] = Field(default_factory=dict)


class ClarificationManager:
    def __init__(self):
        self.stack: List[ClarificationFrame] = []

    def get_current_depth(self) -> int:
        return len(self.stack)

    def create_clarification_request(
        self,
        question: str,
        candidates: List[Dict[str, Any]],
        current_breadcrumb: str,
        context_data: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Creates a new clarification frame or triggers the matrix fallback at depth >= 3."""
        next_depth = len(self.stack) + 1

        # Breadcrumbs trail
        prev_breadcrumbs = self.stack[-1].breadcrumbs if self.stack else ["Plant-Wide"]
        new_breadcrumbs = prev_breadcrumbs + [current_breadcrumb]

        # Circuit Breaker: Depth Limit Reached -> Comparative Matrix Fallback
        if next_depth > MAX_CLARIFICATION_DEPTH:
            matrix_data = self._generate_comparative_matrix(candidates)
            return {
                "type": "COMPARATIVE_MATRIX_FALLBACK",
                "message": (
                    f"Maximum clarification depth ({MAX_CLARIFICATION_DEPTH}) reached. "
                    "Displaying comparative overview of all candidate equipment side-by-side."
                ),
                "breadcrumbs": new_breadcrumbs,
                "matrix": matrix_data
            }

        # Convert candidates to option pills
        options = []
        for c in candidates:
            tag = c.get("tag") or c.get("equipment_tag") or c.get("id", "UNKNOWN")
            name = c.get("name", tag)
            desc = c.get("summary", c.get("type", "Equipment"))
            options.append(ClarificationOption(
                id=tag,
                label=tag,
                description=f"{name} ({desc})",
                target_tag=tag
            ))

        frame = ClarificationFrame(
            depth=next_depth,
            question=question,
            options=options,
            breadcrumbs=new_breadcrumbs,
            context_data=context_data or {}
        )
        self.stack.append(frame)

        return {
            "type": "CLARIFICATION_REQUESTED",
            "clarification_depth": frame.depth,
            "max_depth": MAX_CLARIFICATION_DEPTH,
            "question": frame.question,
            "options": [opt.model_dump() for opt in frame.options],
            "breadcrumbs": frame.breadcrumbs,
            "allow_write_in": frame.allow_write_in
        }

    def resolve_clarification(self, selected_option_id: str) -> Dict[str, Any]:
        """Applies chosen primary key and resumes execution."""
        if not self.stack:
            return {"status": "ERROR", "message": "No active clarification frame on stack."}
        current_frame = self.stack[-1]
        return {
            "status": "RESOLVED",
            "selected_tag": selected_option_id,
            "frame_depth": current_frame.depth,
            "preserved_context": current_frame.context_data
        }

    def rewind_to_breadcrumb_index(self, index: int):
        """Rewinds the clarification context stack to an earlier decision frame."""
        if 0 <= index < len(self.stack):
            self.stack = self.stack[:index + 1]

    def _generate_comparative_matrix(self, candidates: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        matrix = []
        for c in candidates:
            tag = c.get("tag") or c.get("equipment_tag", "UNKNOWN")
            matrix.append({
                "tag": tag,
                "name": c.get("name", tag),
                "type": c.get("type", "Equipment"),
                "operating_temp": c.get("operating_temp_celsius", "—"),
                "operating_pressure": c.get("operating_pressure_barg", "—"),
                "summary": c.get("description_summary", "")[:200]
            })
        return matrix
