---
name: Table A6.2-3 P&ID Readiness Checklist for HAZOP Study (Final R1)
file: Table A6.2-3 PID readiness checklist (Fianl R1).xlsx
location: raw/standards/
type: standards
tags: [hazop, pid, readiness, standards]
last_updated: 2026-06-13
---

# Source: Table A6.2-3 — P&ID Readiness Checklist for HAZOP Study (Final R1)

## Document Identity

| Field | Value |
|-------|-------|
| Title | Table A6.2-3 P&ID Readiness Checklist for HAZOP Study |
| Revision | Final R1 |
| Organisation | PTT GC |
| Parent Standard | [[sources/SG-Q-MP-014]] — Appendix 6.2 |
| File | `raw/standards/Table A6.2-3 PID readiness checklist (Fianl R1).xlsx` |
| Sheets | Appendix 6.2 (phase matrix), Table A6.2-3 (checklist) |

## Purpose

This checklist governs the quality of P&IDs submitted for HAZOP review. It must be completed and endorsed by the HAZOP Coordinator **before any P&ID node analysis begins**. Submitting a deficient P&ID to a HAZOP session causes missed hazards, wasted team time, and incorrect risk rankings.

This document is a companion to [[sources/Table-A6.2-2-PSI-readiness-checklist]] which covers the full Process Safety Information package.

---

## Appendix 6.2 — Phase Requirements Matrix

This sheet defines which PSI documents are required at each project phase. Applies to all HAZOP types (Select, Define, Execute, Operation, Non-operation).

| Document | Select | Define | Execute | Operation | Non-operation |
|----------|--------|--------|---------|-----------|---------------|
| Operations and Maintenance philosophy | E | E | E | E | E |
| Process and Chemistry Descriptions | E | E | E | E | E |
| Process Control Narrative | D | E | E | E | E |
| Reactive Hazard (if applicable) | E | E | E | E | E |
| Material Safety Data Sheet | E | E | E | E | E |
| Plot Plan | E | E | E | E | E |
| General Equipment Arrangements & Elevations | — | E | E | E | E |
| Electrical / Hazardous Area Classification Drawings | — | E | E | E | E |
| Heat and Mass balances | D | E | E | E | E |
| Process Flow Scheme (PFD) and Utility Flow Scheme | E | E | E | E | E |
| P&IDs and UEFS (legend sheets) | D | D | E | E | E |
| Line lists for piping & process equipment | — | E | E | E | E |
| Equipment data sheet | — | D | E | E | E |
| Process Safeguarding Flow Scheme | D | E | E | E | E |
| Cause and Effect Diagrams | — | E | E | E | E |
| SIL Study report | — | — | E | E | E |
| Control valve turndown, RV, trip and alarm settings | — | E | E | E | E |
| Latest construction / as-built drawings | — | — | E | E | E |
| Previous HAZID/HAZOP reports and Close Out reports | — | D | E | E | E |
| Details of change since last PHA | — | D | E | E | E |
| Other safety studies (e.g., Bow-tie analysis) | — | — | D | E | E |

**Legend:** E = Essential, D = Desirable, — = Not required

> **HAZOP Anti-Bias Note:** "Previous HAZID/HAZOP reports" are listed as Essential for Operation phase HAZOPs — but per the [[HAZOP Anti-Bias Rule]], these must NOT be reviewed until after the current study worksheets are complete and signed off. They belong in `raw/hazop/archive/` for post-study gap comparison only.

---

## Table A6.2-3 — P&ID Readiness Checklist (13 Items)

Items 1–10 are **CRITICAL** (must be YES before HAZOP proceeds). Items 11–13 are desirable.

| No. | Checklist Item | Critical | What to Check |
|-----|---------------|----------|---------------|
| 1 | Latest revision issued & controlled | **YES** | HAZOP uses the most current approved revision. Old revision → missing design changes, irrelevant discussions. |
| 2 | Scope completeness (systems, subsystems, boundaries) | **YES** | P&ID covers all systems in HAZOP scope. PFD alone is NOT sufficient for HAZOP. Prevents omission of units or tie-ins. |
| 3 | Equipment tags complete & consistent | **YES** | No missing equipment; no incorrect sequence; no duplicated or incorrect tags. |
| 4 | Line identification | **YES** | All lines complete with correct flow direction; line identification complete (number, size, service, piping class). |
| 5 | Instrumentation (indicators, transmitters, alarms) | **YES** | All instruments present with correct symbols; no missing instruments; no missing/incorrect alarm indication (L, LL, H, HH). |
| 6 | Control loops & interlocks | **YES** | All control and interlock loops present correctly; connection to action elements clear; fail position of valves shown. |
| 7 | Safety devices (PSVs, rupture discs, etc.) | **YES** | No missing relief devices; correct destination; set pressure available. |
| 8 | Tie-ins location | **YES** | Tie-in locations identified; isolation configuration follows reference specification. |
| 9 | Isolation devices (block valves, blinds) | **YES** | Block valves, blinds, NC/NO indication present; operation sense clearly understood. |
| 10 | Consistency across multiple drawings | **YES** | Continuation symbols present with correct details across sheets. |
| 11 | Legend / symbols available | — | Legend sheet present; symbols applied correctly and aligned with plant standard. |
| 12 | Notes and references | — | Notes are present; no unexplained notes; no duplicate notes; notes at correct location. |
| 13 | Consistency with PFD, line list, equipment list | — | Information in P&ID consistent with PFD and equipment list. |

### Coordinator Conclusion
The HAZOP Coordinator must formally record YES/NO on the conclusion row before study begins. If any critical item is NO — HAZOP must not proceed until the deficiency is corrected or resolved by hand markup with HAZOP Coordinator endorsement.

---

## CDN P&ID Readiness Assessment Against Table A6.2-3

> Assessment performed 2026-06-13 based on wiki knowledge from [[sources/pid-cdn]] (Drawings 0000A–0023). This is an LLM-assisted pre-assessment; formal sign-off by HAZOP Coordinator is required.

| No. | Item | Status | Evidence / Notes |
|-----|------|--------|-----------------|
| 1 | Latest revision | ✅ YES | All 45 CDN P&ID drawings are Rev Z1 As-Built (latest approved revision). |
| 2 | Scope completeness | ✅ YES | 22 CDN process sheets (0002–0023) + 16 standard detail sheets (0000A–0001L) cover full CDN scope: Concentration, Decomposition, Neutralization, plus drain headers and relief header. |
| 3 | Equipment tags | ✅ YES | All equipment tags complete. One tag conflict resolved during ingest (X-2308A/B corrected to X-2309A/B per Drawing 0018). Open conflict P-2307A/B motor type (Drawing 0008B Note 2 vs 0001G) — requires field verification but does not affect tag identity. |
| 4 | Line identification | ⚠️ PARTIAL | Flow directions confirmed; main process lines numbered. Piping class/size not systematically recorded in wiki — verify that all lines carry class designation on P&IDs before HAZOP node analysis. |
| 5 | Instrumentation | ✅ YES | C&E Table (Drawing 0002) fully ingested. All SIS tags (UC-2301/2302/2303), DCS tags, analyzer tags, and alarm levels documented. |
| 6 | Control loops & interlocks | ✅ YES | Complete cause-and-effect matrix documented in [[instruments/cause-effect-cdn]]. SIS architecture in [[instruments/sis-cdn]]. Fail positions confirmed where documented. |
| 7 | Safety devices | ⚠️ PARTIAL | PSV tags visible on P&IDs (e.g., PSV-2001N/B on D-2307). However, PSV set pressures for V-2301 and V-2302 are noted as TBC in wiki. Confirm set pressures are printed on P&IDs or available in data sheets before HAZOP. |
| 8 | Tie-ins | ✅ YES | OXI → CDN feed tie-in (S229) documented. CDN → Fractionation outlet tie-in (crude product) documented. Acid aromatics to OWS and Sodium Phenate Tank tie-ins documented. |
| 9 | Isolation devices | ✅ YES | Block valves, SIS valves (UXVs), manual valves, and check valves shown throughout CDN P&IDs. UC-2301/2302/2303 valve lists complete. |
| 10 | Cross-drawing consistency | ✅ YES | Continuation symbols and sheet cross-references verified during P&ID ingest (2026-06-06/07). |
| 11 | Legend / symbols | ✅ YES | Standard detail sheets 0001–0001L provide all symbols, pump details, seal plans, and motor control schematics. |
| 12 | Notes and references | ✅ YES | Drawing notes documented during ingest; key notes captured in equipment pages. |
| 13 | Consistency with PFD | ✅ YES | PFD (0000–0006) and P&ID cross-referenced during ingestion. One tag discrepancy resolved (X-2308→X-2309). |

### Pre-HAZOP Action Items (from CDN Assessment)
| Item | Action | Priority |
|------|--------|----------|
| Item 4 — Line identification | Confirm piping class designation (e.g., CHD, CHP, HC class) is printed on all CDN P&ID lines; spot-check during node setup | Medium |
| Item 7 — PSV set pressures | Obtain PSV set pressures for V-2301 and V-2302 (from data sheets or instrument list) before node analysis covers those vessels | High — required per Table A6.2-3 Item 7 |
| Item 3 — P-2307A/B motor type conflict | Resolve drawing discrepancy (Type B vs Type D) by field verification or engineering query | Medium |
| Formal coordinator sign-off | HAZOP Coordinator to complete and sign Table A6.2-3 checklist for CDN P&IDs | **REQUIRED before node analysis** |

### Overall CDN P&ID Readiness Conclusion
- **Critical items (1–10):** 8 of 10 = YES; 2 of 10 = PARTIAL (Items 4 and 7)
- **Desirable items (11–13):** 3 of 3 = YES
- **Coordinator sign-off:** ❌ Not yet completed

> The two PARTIAL items do not necessarily block HAZOP — the standard allows items to be resolved by hand markup endorsed by the HAZOP Coordinator (see Conclusion row of Table A6.2-3). However, Item 7 (PSV set pressures) should be resolved before any node covering V-2301 or V-2302.

---

## References
- [[wiki/hazop/study-info]] — HAZOP study scope and node status register
- [[sources/Table-A6.2-2-PSI-readiness-checklist]] — companion PSI readiness checklist (8 categories)
- [[sources/SG-Q-MP-014]] — parent HAZOP guidance document (Appendix 6.2 source)
- [[sources/pid-cdn]] — CDN P&ID set assessed above
