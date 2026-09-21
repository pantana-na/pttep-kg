---
name: HAZOP Leadership Training for GC — Chapter 2: Overview PHA Techniques
file: "3. Chapter 2 - Overview PHA techniqes.pdf"
location: raw/standards/
type: training
tags: [hazop, training, pha, standards]
last_updated: 2026-06-13
---

# Source: HAZOP Leadership Training — Chapter 2: Overview PHA Techniques

## Document Identity

| Field | Value |
|-------|-------|
| Title | HAZOP Leadership Training for GC — Chapter 2: Overview PHA Techniques |
| Organisation | Refinery Petrochemical Corporation — Technical Safety Service Division (Q-TS-TS) |
| Instructor | Mr. Noraphol Sookkho, Division Manager, Q-TS-TS |
| Date | 1–3 November 2021 |
| File | `raw/standards/3. Chapter 2 - Overview PHA techniqes.pdf` |
| Parent course | [[sources/hazop-leadership-training-intro]] |

## Purpose

Training material giving a structured comparison of Process Hazard Analysis (PHA) techniques used in the Refinery Group / industry context. Provides the basis for selecting the right PHA tool for each project phase and complexity level. Also includes the IEAT (Thai regulatory) approved PHA method list and the Preliminary SHE Assessment form used for MOC review.

---

## PHA Technique Historical Timeline

| Period | Technique | Description |
|--------|-----------|-------------|
| 1960–2001 | Safety Review / Walk-Through / Inspection / Checklist | Oldest methods; historical lists; yes/no answers |
| 1965–2001 | Relative Ranking | ICI Mond Index, Dow Fire & Explosion Index |
| 1970–2001 | Preliminary Hazard Analysis (PHA) | Identifies hazardous materials and operations |
| 1972–2001 | What-if | Brainstorming approach |
| 1974–2001 | HAZOP | Hazards and Operability Study — line-by-line deviation analysis |

---

## PHA Techniques — Summary

### 1. Checklist
- **Specific (standards-based):** Developed from broad experience or industry standards/codes. Used by individual analyst. Little creativity required from reviewer.
- **Open (experience-based):** Relies heavily on reviewer experience. Appropriate for multi-disciplined team. Requires creativity.

### 2. What-if Study
- Brainstorming approach; team formulates questions answered by members or SMEs.
- Questions target: specific component failure, abnormal process parameter, incorrect operator/maintenance action, external event.
- **Advantages:** Extremely flexible and easy to apply.
- **Limitation:** Requires experienced leader to facilitate and prepare the question list.
- Cited in OSHA 1910.119 as an acceptable PHA method.

### 3. What-if / Checklist (Combination)
- Combines brainstorming (What-if) with structured categories (Checklist) to reduce gaps.
- Study can begin with a checklist, then What-if fills out coverage.

### 4. Failure Mode and Effects Analysis (FMEA)
- Component-by-component assessment of failure modes and their effects on system operation.
- **Process:** Select component → specify function → identify operational phases → identify failure modes → for each phase and mode: identify causes, effects, safeguards, recommendations.
- Systematic and bottom-up in nature.

### 5. Fault Tree Analysis (FTA)
- Graphical top-down method: starts from an undesirable top event (e.g., pipe rupture) and traces causes using Boolean logic.
- Shows possible order of events leading to an accident.
- Common in accident investigations to determine probable causes.

---

## IEAT PSM Allowable PHA Techniques (Thai Regulatory Requirement)

Per Thai Department of Industrial Works (IEAT/DIW) Process Safety Management regulations, the following PHA techniques are approved:

1. What-if
2. Checklist
3. What-if / Checklist (combination)
4. **HAZOP** ← selected method for this CDN study
5. FMEA
6. Fault Tree Analysis
7. Other equivalent techniques

> The HAZOP method used in this study complies with IEAT PSM requirements.

---

## Project Phase Applicability Matrix

| Project Phase | Checklist | What-If | HAZOP | FMEA |
|---------------|-----------|---------|-------|------|
| R&D | ✓ | ✓ | | |
| Conceptual | ✓ | ✓ | ✓ | |
| Pilot plant operation | ✓ | ✓ | ✓ | ✓ |
| Detail engineering | ✓ | ✓ | ✓ | ✓ |
| Construction / Start-up | ✓ | ✓ | ✓ | ✓ |
| **Routine operation** | ✓ | ✓ | **✓** | ✓ |
| Expansion or Modification | ✓ | ✓ | ✓ | ✓ |
| Incident investigation | ✓ | ✓ | ✓ | ✓ |
| Decommissioning | ✓ | ✓ | | |

*HAZOP is broadly applicable from conceptual through routine operation — this study falls under "Routine operation" HAZOP.*

---

## Preliminary SHE Assessment Form (MOC Context)

The chapter includes the full **Preliminary SHE Assessment** form used by Refinery Group for Management of Change (MOC) screening. Key structure:

| Part | Content |
|------|---------|
| 1A | Team members |
| 1B | Change description and alternatives |
| 1C | Available PSI for assessment (SDS, P&IDs, PFDs, procedures, alarm/ESD logic, etc.) |
| 2A | Hazard sources (flammable, toxic) |
| 2B | Hazard index: Inventory / Temperature / Pressure / Flash Point / Explosiveness / Toxicity (0–5 scale each) |
| 3A–3D | Causes, consequences, recommendations, proposed actions |
| 4 | Further PHA decision (8 trigger questions) |
| 5 | Risk rating if no further PHA required (Consequence × Likelihood → Severity) |

**Further PHA is required if:**
- Any "Yes" to Questions 1–3 (multiple P&IDs/equipment, process outside operating windows, significant toxic/flammable inventory change)
- OR 2 or more "Yes" to Questions 4–8 (energy balance, safety device impact, reordered sequence, significant training, significant energy source)

**Severity thresholds:**
- Severity 5 (Extreme) → Plant change must stop
- Severity 4 (High) → Plant change must stop
- Severity 3 (Medium) → Action must be proposed

### Chemical Hazard Index Table (for Prelim SHE Part 2B)

| Score | Inventory (t or t/h) | Temp (°C) | Pressure (barg) | Flash Point (°C) | Explosiveness (UEL–LEL %v) | Toxicity (TLV ppm) |
|-------|----------------------|-----------|-----------------|------------------|----------------------------|--------------------|
| 0 | 0–1 | 0–70 | 0–5 | Non-flammable | Non-explosive | >1000 |
| 1 | 1–10 | <0 or >70–150 | <0 or >5–25 | >55 | 0–20 | 100–1000 |
| 2 | 10–50 | >150–300 | >25–50 | >21–55 | >20–45 | 10–100 |
| 3 | 50–200 | >300–600 | >50–200 | 0–21 | >45–70 | 1–10 |
| 4 | 200–500 | >600 | >200–1000 | <0 | >70–100 | 0.1–1 |
| 5 | 500–1000 | | >1000 | | | <0.1 |
| 6 | >1000 | | | | | |

*Note: Total Index (sum of all categories) indicates overall hazard level for chemical comparison.*

---

## Relevance to This HAZOP Study

- Confirms that **HAZOP is the appropriate method** for routine operation review (current study context).
- Confirms Thai IEAT PSM compliance — HAZOP is listed as approved.
- Prelim SHE Assessment form provides MOC screening context; not directly used in this HAZOP but relevant to [[wiki/procedures/]] if any concurrent MOC activities apply.
- The project phase table confirms full applicability of HAZOP at the "Routine operation" phase for the CDN section.

---

## References
- [[sources/hazop-leadership-training-intro]] — Course introduction (same series)
- [[sources/hazop-leadership-training-ch1]] — Chapter 1: Hazard and Risk Concepts
- [[sources/P-Q-MP-OEMS-005]] — Refinery Group governing HAZOP procedure
- [[hazop/methodology]] — Full HAZOP method detail per SG-(Q-MP)-014
- [[hazop/study-info]] — CDN HAZOP study scope and status
