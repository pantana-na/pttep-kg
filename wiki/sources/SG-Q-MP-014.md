---
name: SG-(Q-MP)-014 Guidance for Hazard and Operability Studies (HAZOP)
type: standard
tags: [source, standard, hazop, guidewords, methodology]
last_updated: 2026-06-13
---

# Source: SG-(Q-MP)-014 — Guidance for HAZOP Studies

**Issuer:** PTT Global Chemical Public Company Limited, GC Management System and Process Safety (Q-MP)
**Document No.:** SG-(Q-MP)-014
**Revision:** 3
**Date:** 26/05/2026
**Pages:** 61
**File:** `raw/standards/SG-(Q-MP)-014_R3.pdf`
**Created by:** Mr. Pongpasin Tanaruangarmorn, Senior Safety Engineer
**Approved by:** Mr. Warakorn Decha, Vice President
**Reviewed by:** Mr. Noraphol Sookkho, Division Manager Q-MP-TS

**Rev 3 change (vs Rev 2):** Added PSI Readiness detail (Table A6.2-2 and A6.2-3)

---

## Document Purpose

Detailed guidance for conducting HAZOP studies per P-(Q-MP)-OEMS-005. Covers methodology, team qualifications, node preparation, 9-step worksheet methodology, PSI readiness, guideword set, likelihood estimation, IPL credit evaluation, and documentation requirements.

---

## Key Pages Created from This Source

- [[wiki/hazop/methodology]] — 9-step HAZOP execution method, guideword table, likelihood table, IPL credit tables, acceptable risk rule
- [[wiki/hazop/risk-matrix]] — RAM confirmed: GC PHA RAM from W-(Q-MP)-002 is mandatory 1st priority
- [[wiki/sources/Table-A6.2-2-PSI-readiness-checklist]] — Table A6.2-2 formal PSI readiness checklist (ingested 2026-06-13 as standalone XLSX; 8 categories with review questions)

---

## Critical Rules Extracted

### Acceptable Risk
- **Acceptable risk level for GC = "Low" or "Very Low"**
- Mitigated risk ≥ Medium → **must generate a recommendation**
- May also recommend at Low/Very Low for voluntary improvement

### Severity Rule
- Severity **never changes** between Initial and Mitigated risk assessment

### Full Record Approach
- All deviations must be applied to each node
- If no credible cause: document "No credible cause was identified" or "N/A"
- Do NOT leave blank

### Safeguard Documentation
- Must include equipment tag + what protects + how it protects + set point where applicable
- Record prevention safeguards first, then mitigation safeguards
- Active fire protection and emergency response: generally NOT recorded as a safeguard (post-event, uncertain)

### Recommendation Wording
- Use action verbs: Add, Change, Configure, Provide, Update, Prepare
- Explain why the recommendation is needed

### Worksheet Reference
- Never use "See above", "Same as above", "Same as earlier node"
- Copy content from other nodes rather than cross-referencing node numbers

---

## PSI Requirements for Operation Phase HAZOP (§6.2 / Table A6.2-1)

**Essential (E) documents for Operation-phase HAZOP:**
- Operations and Maintenance philosophy
- Process and Chemistry Descriptions
- Process Control Narrative
- Reactive Hazard (if applicable)
- Material Safety Data Sheet
- Plot Plan
- General Equipment Arrangements & Elevations
- Electrical/Hazardous Area Classification Drawings
- Heat and Mass Balances
- Process Flow Scheme (PFD) and Utility Flow Scheme
- P&IDs and UEFS
- Line lists for piping & process equipment
- Equipment data sheets
- Process Safeguarding Flow Scheme
- Cause and Effect Diagrams
- SIL Study report
- Control valve turndown, RV, trip and alarm settings
- Latest as-built drawings
- Previous HAZID/HAZOP reports and Close-out reports
- Details of change since last PHA

**Desirable (D):**
- Other safety studies (Bow-tie analysis)

---

## P&ID Readiness Checklist (Table A6.2-3 — 10 items)

| No. | Checklist Item |
|-----|---------------|
| 1 | Latest revision issued & controlled |
| 2 | Scope completeness (systems, subsystems, boundaries — PFD not sufficient) |
| 3 | Equipment tags complete & consistent (no missing, duplicate, or wrong tags) |
| 4 | Line identification complete with correct direction, number, size, service, class |
| 5 | All instrumentation present correctly (no missing instrument, correct symbols, alarms L/LL/H/HH) |
| 6 | All control loops & interlocks present (no missing, fail positions shown) |
| 7 | Safety devices (PSVs, rupture discs) present with correct set pressures and destinations |
| 8 | Tie-in locations identified with isolation configuration |
| 9 | Block valves, blinds, NC/NO indication present and clearly understood |
| 10 | Continuation symbols between drawings correct and consistent |

**Conclusion:** All items available without deficiency, OR deficiencies can be solved with hand markup before HAZOP.

---

## Related Documents
- [[sources/P-Q-MP-OEMS-005]] — HAZOP Procedure (workflow, KPIs, roles)
- [[sources/W-Q-MP-002]] — Operational Risk Assessment Matrix (mandatory RAM)
- [[hazop/methodology]] — Full methodology wiki page from this source
- [[hazop/risk-matrix]] — Risk matrix in force for this study
