---
name: GC HAZOP Leadership Training — Chapter 7: GC HAZOP Workflow
description: PHA document ecosystem and end-to-end GC HAZOP workflow (5 phases, 4 report statuses, action change process)
metadata:
  type: source
tags: [source, hazop, workflow, pha-documents]
sources: ["8. Chapter 7 - GC HAZOP Workflow.pdf"]
last_updated: 2026-06-14
---

# Source: GC HAZOP Leadership Training — Chapter 7: GC HAZOP Workflow

## Document Metadata

| Field | Value |
|-------|-------|
| Title | HAZOP Leadership Training for GC — Chapter 7: GC HAZOP Workflow |
| Author / Owner | Technical Safety Service Division (Q-TS-TS), PTT Global Chemical PCL |
| Date | 1–3 November 2021 |
| Format | PowerPoint slides (7 slides) |
| File | `raw/standards/8. Chapter 7 - GC HAZOP Workflow.pdf` |
| Series | Final chapter of the GC HAZOP Leadership Training Course (Intro + Ch.1–7) |

---

## Sub-chapter 7-1 — Related Documents for PHA Techniques in GC

The slide lists the full GC PHA document ecosystem by approach type.

### Qualitative Approach
| Document Code | Title |
|---------------|-------|
| P-(Q-TS)-OEMS-005 | HAZOP Study Procedure *(current governing version: P-(Q-MP)-OEMS-005 R4)* |
| SG-(Q-TS)-014 | HAZOP Study Guideline *(current governing version: SG-(Q-MP)-014 R3)* |
| SG-(Q-TS)-002 | HAZID Guideline |
| SG-(Q-TS)-011 | ENVID Guideline |
| F-(Q-TS)-OEMS-043 | Preliminary SHE Assessment and SHE Evaluation form |

> Note: Document codes use the 2021 Q-TS prefix. Current (2026) governing versions use the Q-MP prefix — P-(Q-MP)-OEMS-005 R4 and SG-(Q-MP)-014 R3 are the authoritative documents for this study. See [[sources/P-Q-MP-OEMS-005]] and [[sources/SG-Q-MP-014]].

### Quantitative / Semi-Quantitative Approach
| Document Code | Title |
|---------------|-------|
| SG-(Q-TS)-010 | Quantitative Risk Assessment (QRA) |
| — | Layer of Protection Analysis (LOPA) |

### Visualization Tools
| Document Code | Title |
|---------------|-------|
| SG-(Q-TS)-001 | Guideline for Bow-Tie Methodology |
| — | Guideline for Bow-Tie Validation |

---

## Sub-chapter 7-2 — GC HAZOP Workflow

The core content of this chapter: a flowchart defining the end-to-end GC HAZOP lifecycle from initiation through action close-out.

### Workflow Overview — Five Phases

| Phase | Owner | Key Output |
|-------|-------|-----------|
| 1. Initiating HAZOP | CRT | Decision that HAZOP is required |
| 2. HAZOP Preparation | HAZOP Coordinator | PSI and study information assembled |
| 3. HAZOP Study Workshop | HAZOP Team | Completed worksheets |
| 4. Report Preparation & Approval | Scribe → HAZOP Leader | Report progresses Draft → Submitted → Publish |
| 5. Action Close-out | Responsible Person + Action Approver (+ HAZOP Coordinator as Champion if action changes) | Report reaches status "Complete" |

### Report Status States (4 defined states)

| Status | Trigger | Owner |
|--------|---------|-------|
| **Draft** | Scribe prepares report after workshop | Scribe |
| **Submitted** | Scribe submits for Leader approval | Scribe |
| **Publish** | HAZOP Leader approves | HAZOP Leader |
| **Complete** | All actions closed out and approved | System |

If HAZOP Leader does NOT approve → report returns to Scribe for revision (Draft → Submitted loop).

### Action Change Process (Post-Publish)

After the report is published, each action is managed as follows:

```
Is action deviated from workshop?
  │
  ├── NO  → HAZOP Actions remain as per workshop outcome → Action Close-out
  │
  └── YES → HAZOP Coordinator (Champion) raises action change request
               → HAZOP team re-evaluates risk based on proposed action
               → Accept?
                    NO  → HAZOP Actions remain as per workshop outcome
                    YES → Revise action as agreed in system → Action Close-out
```

### Action Close-out Approval

```
Action Close-out (by Responsible Person)
  │
  └── Is action approved? (by Action Approver)
         NO  → Return to Action Close-out
         YES → Action Close-out Complete → HAZOP Report status "Complete"
```

### Roles in the Workflow

| Role | Responsibilities in Workflow |
|------|------------------------------|
| CRT | Triggers HAZOP initiation |
| HAZOP Coordinator | Prepares PSI; acts as Champion for action change requests |
| HAZOP Team | Conducts workshop; re-evaluates risk if action changes are proposed |
| Scribe | Prepares Draft report; submits for approval |
| HAZOP Leader | Approves report (Draft → Publish gate) |
| Responsible Person | Closes out individual actions |
| Action Approver | Approves action close-out |

---

## Key Takeaways for This Study

1. **CRT triggers HAZOP** — this is the formal initiation gate; not the HAZOP Leader or team.
2. **Scribe owns report status transitions** (Draft → Submitted) — requires a dedicated, technically competent scribe throughout the study.
3. **HAZOP Leader is the approval authority for the report** — not the HAZOP Coordinator or management. Report must not be published without Leader sign-off.
4. **Action deviation from workshop requires team re-evaluation** — responsible persons cannot unilaterally change HAZOP actions; the HAZOP Coordinator raises a formal change request and the team reassesses the risk. This preserves workshop integrity.
5. **"Complete" status is achieved only when all actions are closed and approved** — the study is not done at "Publish."

---

## References
- [[sources/P-Q-MP-OEMS-005]] — governing HAZOP procedure (current version)
- [[sources/SG-Q-MP-014]] — governing HAZOP guidance (current version)
- [[hazop/methodology]] — execution detail: 9-step method, guideword set, IPL credit tables, GC HAZOP workflow
- [[hazop/study-info]] — study scope, team, node status register
- [[hazop/action-register]] — where all HAZOP recommendations are tracked
