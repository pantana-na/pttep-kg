---
name: HAZOP Leadership Training for GC — Chapter 1: Hazard and Risk Concept
file: "2. Chapter 1 - Hazard and Risk concept.pdf"
location: raw/standards/
type: training
tags: [hazop, training, risk-matrix, standards]
last_updated: 2026-06-13
---

# Source: HAZOP Leadership Training — Chapter 1: Hazard and Risk Concept

## Document Identity

| Field | Value |
|-------|-------|
| Title | HAZOP Leadership Training for GC — Chapter 1: Hazard and Risk Concept |
| Organisation | PTT Global Chemical PCL — Technical Safety Service Division (Q-TS-TS) |
| Instructor | Mr. Noraphol Sookkho, Division Manager, Q-TS-TS |
| Date | 1–3 November 2021 |
| File | `raw/standards/2. Chapter 1 - Hazard and Risk concept.pdf` |
| Parent course | [[sources/hazop-leadership-training-intro]] |

## Purpose

Training material presenting the PTT GC risk and hazard conceptual framework used as the basis for HAZOP and PHA activities. Contains definitions, risk assessment process, acceptable risk concept, and GC Master Risk Matrix severity tables for all four PEES categories.

---

## Key Definitions

| Term | Definition |
|------|-----------|
| **Hazard** | A physical or chemical condition that has the potential for causing harm to people, property, or the environment. Hazards are intrinsic to a material or its conditions of use. |
| **Harm** | Injury or damage to the health of people, or damage to property/asset or the environment. |
| **Risk** | Product of probability and consequence: **RISK = Frequency × Consequence** |

---

## Three Types of Risk Determination

| Type | Method | PTT GC Application |
|------|--------|--------------------|
| **Qualitative** | Risk matrix (colour/level) | HAZOP — governs this study via [[hazop/risk-matrix]] |
| **Semi-Quantitative** | Layer of Protection Analysis (LOPA) | Used for SIL verification |
| **Quantitative** | Quantitative Risk Assessment (QRA) | Major projects/complex scenarios |

---

## Risk Assessment Process

1. **Risk Identification** — Find hazard source; identify potential consequences
2. **Risk Evaluation** — Evaluate risk level; determine risk acceptability vs. tolerance criteria
3. **Risk Control** — Eliminate activity OR propose/implement risk reduction measures
4. **Monitor & Review** — Ongoing verification

**Decision flow:**
- Is risk tolerably low? → If Yes: acceptable with control plan
- If No: Can risk be economically reduced? → If Yes: implement measures; If No: eliminate activity

---

## GC Master Risk Matrix — PEES Severity Summary

This training cross-references the same GC RAM as [[hazop/risk-matrix]] (W-(Q-MP)-002). Below is the detail from this training source for cross-verification.

### People Severity

| Level | Label | Definition |
|-------|-------|-----------|
| 5 | Extreme | More than one fatality; major fire/explosion with >1 fatality; very high health effect |
| 4 | High | Single fatality or Permanent Total Disability; high health effect (burns, cancer); LOPC above API RP 754 Table 1 threshold; protesters rally or official complaint |
| 3 | Medium | Loss Time Injury; medium health effect (sensitization, noise-induced hearing loss); LOPC above API RP 754 Table 2 but below Table 1 |
| 2 | Low | Medical treatment or Restricted Work Case; low health effect; LOPC below API RP 754 Table 2 threshold |
| 1 | Very Low | No injury or First Aid Case; no/very low health effect; no or minimal morale impact |

*Note: LOPC = Loss of Primary Containment. API RP 754 Table 1 and Table 2 define threshold quantities for Tier 1 and Tier 2 process safety events.*

### Environmental Severity

| Level | Label | Definition |
|-------|-------|-----------|
| 5 | Extreme | Massive, wide-area, persistent environmental impact; spillage >100 bbl into sensitive environment; financial statement reportable |
| 4 | High | Severe environmental damage requiring extensive restoration; oil spill reaching beaches; off-site groundwater contamination over large area; spill >50 bbl reaching environment |
| 3 | Medium | Limited environmental damage persisting or requiring clean-up; observed off-site effects; >10 community complainants; spill >1 bbl reaching environment |
| 2 | Low | Minor environmental damage, no lasting effect; on-site groundwater contamination; spill ≤1 bbl reaching environment |
| 1 | Very Low | No/slight effect; small spill in process area that readily evaporates; minor off-site seepage |

### Economic Severity

| Level | Label | Downstream Plant (PTT Phenol applies here) |
|-------|-------|-------------------------------------------|
| 5 | Extreme | ≥ 150 M THB |
| 4 | High | 15 – < 150 M THB |
| 3 | Medium | 1.5 – < 15 M THB |
| 2 | Low | 0.15 – < 1.5 M THB |
| 1 | Very Low | < 0.15 M THB |

*Economic loss includes: product loss, opportunity loss, asset damage, and clean-up cost.*

*PTT Phenol category classification:* PH-P1/PH-P2 codes listed under Downstream Plant in training slides — confirms Downstream thresholds apply. Note: per [[hazop/risk-matrix]], the plant's specific classification should be confirmed with the HAZOP team.

### Social Severity

| Level | Label | Definition |
|-------|-------|-----------|
| 5 | Extreme | International media coverage; high-level government involvement; customer stops purchase; company subject to court dissolution order |
| 4 | High | National media coverage; national government/NGO involvement; customer reduces purchase; temporary suspension order to operate |
| 3 | Medium | Regional concern; extensive local media + some regional; official complaint from customer; non-compliance with laws and legal action |
| 2 | Low | Local concern; local media coverage; verbal customer complaints; partial non-compliance managed |
| 1 | Very Low | Local awareness but no discernible concern; no media coverage; no or slight customer impact; no or insignificant legal fault |

---

## Acceptable Risk Concept

Key principle from training: *"You want a valve that doesn't leak, and you try everything possible to develop one. But the world provides you with a leaking valve. You have to determine how much leakage you can tolerate."* — NASA senior scientist

Acceptable risk in PTT GC context: governed by the RAM action thresholds in [[hazop/risk-matrix]]:
- **Low / Very Low** = acceptable risk (control plan required)
- **Medium and above** = risk reduction required

---

## Relevance to This HAZOP Study

This document confirms and cross-validates the PTT GC risk framework applied in this wiki:
- PEES severity tables here are consistent with [[hazop/risk-matrix]] (W-(Q-MP)-002 R2)
- Three-type risk determination hierarchy confirms that this HAZOP uses qualitative RAM, not QRA
- Economic thresholds confirm PH-P1/PH-P2 codes are Downstream Plant category → apply Downstream thresholds

> **Note:** W-(Q-MP)-002 R2 (the governing standard) supersedes this training material where any discrepancy exists. See [[hazop/risk-matrix]] for the authoritative tables.

---

## References
- [[hazop/risk-matrix]] — Authoritative risk matrix for this study (W-(Q-MP)-002 R2)
- [[sources/W-Q-MP-002]] — Governing risk assessment matrix document
- [[sources/hazop-leadership-training-intro]] — Course introduction (same series)
- [[sources/SG-Q-MP-014]] — HAZOP guidance document
- [[hazop/study-info]] — HAZOP study scope
