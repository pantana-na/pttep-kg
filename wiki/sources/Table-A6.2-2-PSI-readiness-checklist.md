---
name: Table A6.2-2 Process Safety Information (PSI) Readiness Checklist for HAZOP Study
type: standard-form
tags: [source, standard, hazop, psi, readiness-checklist]
sources: [Table A6.2-2 PSI readiness checklist (Final R1).xlsx]
last_updated: 2026-06-13
---

# Source: Table A6.2-2 — PSI Readiness Checklist for HAZOP Study

**Issuer:** Refinery Petrochemical Corporation, GC Management System and Process Safety (Q-MP)
**Reference in parent standard:** SG-(Q-MP)-014 R3 §6.2 / Table A6.2-2
**Revision:** Final R1
**Format:** XLSX (2 sheets)
**File:** `raw/standards/Table A6.2-2 PSI readiness checklist (Final R1).xlsx`

---

## Purpose

Formal readiness checklist used to verify that all Process Safety Information (PSI) required for a HAZOP study is available, accurate, and complete before node analysis begins. Directly referenced by SG-(Q-MP)-014 R3 and must be completed as part of the HAZOP-SETUP step per [[sources/SG-Q-MP-014]].

---

## Sheets

### Sheet 1 — Appendix 6.2: Typical PSI Required by Project Phase

Governs which documents are Essential (E) or Desirable (D) by project phase.

| Document / Information | Select | Define | Execute | Operation | Non-operation |
|------------------------|--------|--------|---------|-----------|---------------|
| Operations and Maintenance philosophy | E | E | E | E | E |
| Process and Chemistry Descriptions | E | E | E | E | E |
| Process Control Narrative | D | E | E | E | E |
| Reactive Hazard (if applicable) | E | E | E | E | E |
| Material Safety Data Sheet | E | E | E | E | E |
| Plot Plan | E | E | E | E | E |
| General Equipment Arrangements & Elevations | — | E | E | E | E |
| Electrical / Hazardous Area Classification Drawings | — | E | E | E | E |
| Heat and Mass Balances | D | E | E | E | E |
| Process Flow Scheme (PFD) and Utility Flow Scheme | E | E | E | E | E |
| P&IDs and UEFS | D | D | E | E | E |
| Line lists for piping & process equipment | — | E | E | E | E |
| Equipment data sheet | — | D | E | E | E |
| Process Safeguarding Flow Scheme | D | E | E | E | E |
| Cause and Effect Diagrams | — | E | E | E | E |
| SIL Study report | — | — | E | E | E |
| Control valve turndown, RV, trip and alarm settings | — | E | E | E | E |
| Latest construction / as-built drawings | — | — | E | E | E |
| Previous HAZID/HAZOP reports and Close-out reports | — | D | E | E | E |
| Details of change since last PHA | — | D | E | E | E |
| Other safety studies (Bow-tie analysis) | — | — | D | E | E |

**Applicable phase for CDN HAZOP:** Operation — therefore all items marked E are **Essential**.

> ⚠️ Note: "Previous HAZID/HAZOP reports and Close-out reports" is listed as Essential for Operation phase. **However**, per the HAZOP Anti-Bias Rule (`app/hazop/anti_bias.py`), this must NOT be ingested until all node worksheets are signed off. The Anti-Bias Rule supersedes this checklist item during active node analysis. After study completion, archive documents may be reviewed for gap comparison per the Anti-Bias Rule procedure.

---

### Sheet 2 — Table A6.2-2: PSI Readiness Checklist (8 Categories)

Structure: Category | Document/Information | Criticality | Review Questions | Review (YES / NO / Not Related) | Remark

| # | Category | Key Documents | Criticality | Review Questions |
|---|----------|--------------|-------------|-----------------|
| 1 | Chemical and Reaction hazard | GHS-compliant SDS | High | SDS for all chemicals comply with GHS and are available. Focus: Section 2 (Hazard ID), Section 7 (Handling/storage), Section 9 (Physical/chemical properties), Section 10 (Stability/reactivity) |
| 2 | Process Flow Information | P&IDs, PFDs with H&M balance | High | Latest revision of PFD and P&IDs approved for HAZOP. Vendor package P&IDs available. P&ID readiness checklist (Table A6.2-3) complete without deficiency (or deficiencies resolved by hand markup). |
| 3 | Process Description, Design Basis and Process chemistry | Overall process description, design intent, operating envelope, mode of operation, reaction information | High | Process description / design intent for all operating modes available. Operating envelope (new/updated/current) available and aligned with design basis. Process chemistry information available (reactions, side reactions, rates, P&T profiles). |
| 4 | Equipment information | Equipment data sheets | High | For existing facilities: no differentiation from P&ID. Vendor package data including design limits (design P&T) available and aligned. |
| 5 | Operating Procedures | Normal / Startup / Shutdown / Emergency procedures | High | Procedures reflect actual plant practice and include abnormal operations. Procedures cross-checked with control logic and interlocks (no conflict). |
| 6 | Safety Systems & Safeguards | Cause and Effect diagram, SIS/SIF data/report | High | Alarm information with updated setpoints available. C&E information available. Existing SIS/SIF information available (design intent, SIL level — target and verification). |
| 7 | Relief & Flare Design | Relief load calculation, flare hydraulics, dispersion study | High | Relief and vent system information (relief scenario and capacity) verified and available. |
| 8 | Past Incidents | Incident reports, industry databases | Medium | Relevant incidents included; root causes considered; recommendations closed. |

---

## CDN HAZOP Readiness Assessment (This Study)

> Status mapped against Table A6.2-2 categories. See [[wiki/hazop/study-info]] for living readiness table.

| Category | Criticality | CDN Status | Notes |
|----------|-------------|-----------|-------|
| Chemical and Reaction hazard | High | ⚠️ Partial | Hazard pages exist ([[hazards/cumene-hydroperoxide]], [[hazards/phenol]]); GHS-compliant SDS not yet ingested |
| Process Flow Information | High | ✅ Available | CDN PFDs (Dwg 0000–0006) + P&IDs (Dwg 0002–0023) complete; Table A6.2-3 checklist items met with hand markup capability |
| Process Description, Design Basis and Process chemistry | High | ✅ Available | UOP GOM §II–XI ingested; CDN procedures, parameters, operating windows all in wiki |
| Equipment information | High | ❌ Missing | Equipment data sheets not yet ingested — design P&T, materials of construction TBC for most items |
| Operating Procedures | High | ✅ Available | [[procedures/normal-operations-cdn]], [[procedures/normal-shutdown-cdn]], [[procedures/emergency-cdn]] — UOP GOM basis; cross-checked against C&E |
| Safety Systems & Safeguards | High | ⚠️ Partial | C&E table ingested [[instruments/cause-effect-cdn]]; SIS architecture [[instruments/sis-cdn]]; some alarm setpoints still TBC |
| Relief & Flare Design | High | ⚠️ Partial | Relief header (Dwg 0022) ingested; PSV set pressures for V-2301/V-2302 TBC; formal relief load calc not available |
| Past Incidents | Medium | ❌ Not available | No incident reports ingested — Anti-Bias Rule governs |

**Overall CDN PSI readiness: ~60% complete (formal checklist basis)**

**Blockers before node analysis:**
1. Equipment data sheets (Category 4) — all major CDN equipment; PSI-essential
2. GHS-compliant SDS for CHP, H₂SO₄, Phenol, Diamine (Category 1)
3. Alarm setpoints TBC (Category 6) — PSV set pressures; calorimeter ΔT alarms
4. Relief & flare design data (Category 7) — PSV sizing basis

---

## Related Documents

- [[sources/SG-Q-MP-014]] — parent standard that references this checklist
- [[sources/P-Q-MP-OEMS-005]] — HAZOP procedure that mandates PSI readiness check
- [[wiki/hazop/study-info]] — living readiness status for CDN HAZOP
- [[hazop/methodology]] — full study methodology
