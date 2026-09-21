---
name: GC HAZOP Worksheet Template — Column Structure
tags: [hazop, template, worksheet-structure]
source: O-P3-PHA-2026_005.xlsx (P5-WorkSheet blank template tab; P6/P7 tabs)
last_updated: 2026-06-17
---

# GC HAZOP Worksheet Template — Column Structure

> Structural reference only. Extracted from the **blank template tabs** of a real GC HAZOP report workbook (`raw/hazop/example/O-P3-PHA-2026_005.xlsx`). Contains **no findings content** — no causes, consequences, safeguards, or risk scores from any actual study. Safe to use as a layout reference for our Phenol CDN HAZOP without anti-bias concerns.
>
> For the filled example version (causes/consequences/safeguards/recommendations from a real, unrelated unit), see [[wiki/hazop/examples/o-p3-fractionation-2026-005]] — that page carries the anti-bias caution, this one does not.

---

## Report-Level Structure (Sheet Tabs)

| Tab | Purpose |
|-----|---------|
| Cover Page | Title, MOC/Project No., PHA No., Facility Location, Revision/Date/Prepared-by/Approved-by/Report status |
| Name List | HAZOP attendance list: Employee ID, Name, Department code, Role (Leader/Scribe/Member) |
| HAZOP Information | MOC/Project No., Project Title, Plant, Unit/Facility, PHA No., HAZOP Purpose (e.g. Revalidation), HAZOP Scope, Process description, Chemicals, HAZOP Assumptions, General Notes |
| WorkSheet Index | One row per node: Node No., Node Description, Design Intention, Design Condition, Operating Condition, Color code, Related Drawing No. |
| WorkSheet (per node) | The deviation-by-deviation HAZOP table — see column structure below |
| Action Items | Consolidated recommendations across all nodes — see structure below |
| Risk Ranking | Embedded RAM reference (same content type as [[wiki/hazop/risk-matrix]]) |
| Interlock/ESD Summary | Cross-node rollup of every safeguard tagged as Interlock/ESD — see structure below |

This maps directly onto our schema's `wiki/hazop/study-info.md` (HAZOP Information), `wiki/hazop/nodes/<id>.md` (WorkSheet), and `wiki/hazop/action-register.md` (Action Items) — confirms our existing page split is consistent with company practice. The **Interlock/ESD Summary** is a structure **we do not currently have a dedicated wiki page for** — worth adding as a cross-node SIS/ESD rollup view (candidate: `wiki/hazop/interlock-esd-summary.md`, populated as nodes are completed).

---

## Per-Node Worksheet Header Block

Each node's worksheet tab opens with a fixed header before the deviation table:

```
Node No: <n>          Node Description: <text>
Design Intention: <narrative — process objective in plain language>
Design Condition: <equipment-by-equipment design T/P/flow>
Operating Condition: <equipment-by-equipment normal operating T/P/flow>
```

This is a superset of our node page's "Design Intent" + "Normal Operating Parameters" sections in [[wiki/hazop/nodes]] template — their template lists conditions **per equipment item within the node** rather than a single aggregated table. Worth adopting: list design AND operating condition side by side per equipment tag, not just normal operating value.

---

## Deviation Table — Column Structure (3 Risk Blocks)

The worksheet uses **three parallel risk blocks**, extending the baseline node-page template (which had two: Without/With safeguard):

| Block | Columns | Notes |
|-------|---------|-------|
| **(fixed, left)** | Parameter, Deviation, Possible Cause, Potential Consequence | Same for all three risk blocks |
| **Without Safeguard** | L, Severity (P / En / Ec / S), RR | Initial/unmitigated risk |
| **Existing Safeguard** | Detail, IL/ESD (Yes/No flag) | Each safeguard is its own row; `IL/ESD` flags whether it is an Interlock/ESD (vs. alarm/procedure/other) |
| **With Existing Safeguard** | L, Severity (P / En / Ec / S), RR | Mitigated risk — Severity unchanged from "Without Safeguard" |
| **Recommendation** | Detail | Free text |
| **After Recommendation Comp.** | L, Severity (P / En / Ec / S), RR | **Third risk block** — re-assessed risk AFTER the recommendation is implemented and closed. Not present in our current template. |

### Recommended addition to our schema
Our [[wiki/hazop/methodology]] "GC HAZOP Worksheet — Official Column Structure" section and the baseline node-page worksheet table currently only carry Initial Risk + Mitigated Risk. The real company template carries a **third, post-closure risk block** ("After Recommendation Comp.") populated once a recommendation is implemented — this is the mechanism by which residual risk is formally re-verified at action close-out, consistent with [[wiki/hazop/methodology]]'s Phase 5 (Action Close-out). Consider adding an "After Recommendation Risk" column to the node worksheet table for completed recommendations.

### IL/ESD flag
Each safeguard row carries a `Yes`/`No` flag for whether it is an Interlock or ESD action (as opposed to an alarm, procedure, or other non-IPL safeguard). This is a cheap, useful field to add to our safeguard recording convention in [[wiki/hazop/methodology]] (DO/DON'T safeguard examples) — it makes the Interlock/ESD Summary rollup possible.

---

## Action Items Tab — Column Structure

| Column | Notes |
|--------|-------|
| No. | Sequential |
| Action item detail | Free text recommendation |
| Node | Which node it came from |
| Complete with MoC Part | For MOC-driven PHAs only — N/A for routine revalidation |
| Action by — Responsible Person | Employee ID + Name (internal GC staff) OR External Party |
| Due Date for close-out | |
| Approver for action approval | |
| Completion Date | If already closed |
| Approved Date | If already approved |

Maps closely to our [[wiki/hazop/action-register]] (Rec# / Node / Risk / Owner / Status) — the real template additionally splits Owner into Employee ID + Name and distinguishes internal staff vs. external party, and separates "Completion Date" from "Approved Date" (two-step close-out, consistent with [[wiki/hazop/methodology]]'s Action Close-out Approval Gate). Consider adding Completion Date / Approved Date as separate fields to our action-register schema.

---

## Interlock/ESD Summary Tab — Column Structure

| Column | Notes |
|--------|-------|
| Existing Safeguard | The IL/ESD description |
| Node | Source node |
| Possible Cause | Carried from the worksheet row |
| Potential Consequence | Carried from the worksheet row |
| Without Safeguard: L, Severity (P/En/Ec/S), RR | |
| With Existing Safeguard: L, Severity (P/En/Ec/S), RR | |

A flat rollup of every row across all nodes where the safeguard's IL/ESD flag = Yes. Useful as a cross-check against our [[wiki/instruments/cause-effect-cdn]] and [[wiki/instruments/sis-cdn]] pages once CDN node analysis begins — every SIS trip credited in a node worksheet should also appear in this rollup.

---

## References
- [[wiki/hazop/examples/o-p3-fractionation-2026-005]] — filled example (content, not just structure) from the same source workbook
- [[wiki/hazop/methodology]] — our existing 9-step methodology and worksheet column reference (SG-(Q-MP)-014 R3 based)
- [[wiki/hazop/action-register]] — our action register schema, candidate for the field additions noted above
- `raw/hazop/example/O-P3-PHA-2026_005.xlsx` — source workbook
