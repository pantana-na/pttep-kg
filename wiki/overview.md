---
name: Phenol Plant Process Overview
tags: [overview, synthesis]
last_updated: 2026-06-06
---

# Phenol Plant — Process Overview

**Plant:** Refinery Operations Ltd. — **Train II**  
**Location:** Hemaraj Eastern Industrial Estate, Map Ta Phut, Rayong, Thailand  
**Licensor:** UOP (Universal Oil Products) | **Engineer:** POSCO Engineering | **Project No.:** 120117  
**Reference:** [[project]]

## Plant Objective

Produce high-purity **Phenol (C₆H₅OH)** and co-product **Acetone (CH₃COCH₃)** from **Benzene (C₆H₆)** and **Propylene (C₃H₆)** feedstocks via the **Hock Process (Cumene Process)**.

---

## Chemistry

### Overall Reaction

```
C₆H₆  +  C₃H₆  →  C₆H₅OH  +  CH₃COCH₃
Benzene + Propylene → Phenol + Acetone
```

Phenol and Acetone are produced in an approximately **1:0.62 mass ratio** (stoichiometric).

### Step-by-Step Chemistry

**Step 1 — Alkylation** [[units/alkylation]]
```
C₆H₆  +  C₃H₆  →  C₆H₅CH(CH₃)₂
Benzene + Propylene → Cumene (Isopropylbenzene)
```
- Catalyst: Zeolite (modern plants) or AlCl₃/BF₃ (older plants)
- Side products: Diisopropylbenzene (DIPB), Polyisopropylbenzene (PIPB)
- DIPB is transalkylated back to Cumene to improve yield

**Step 2 — Oxidation** [[units/oxidation]]
```
C₆H₅CH(CH₃)₂  +  O₂  →  C₆H₅C(CH₃)₂OOH
Cumene + Air/O₂ → Cumene Hydroperoxide (CHP)
```
- Liquid-phase, non-catalytic, air oxidation
- Temperature ~110–130°C; CHP concentration typically 20–35 wt%
- Side products: Alpha-Methylstyrene (AMS), Acetophenone, DMBA
- CHP is a **peroxide — thermally unstable above ~100°C** [[hazards/cumene-hydroperoxide]]

**Step 3 — Cleavage / Decomposition** [[units/cleavage]]
```
C₆H₅C(CH₃)₂OOH  →  C₆H₅OH  +  CH₃COCH₃
CHP → Phenol + Acetone
```
- Acid-catalyzed (dilute H₂SO₄ or ion exchange resin)
- Highly exothermic — precise temperature and residence time control critical
- By-products: AMS, Acetophenone, Cumene (unreacted), Hydroxyacetone

**Step 4 — Distillation / Purification** [[units/distillation]]
- Neutralization of acid catalyst
- Multi-column distillation train:
  - Acetone column: Crude acetone → Refined acetone
  - Cumene column: Recycle cumene and AMS
  - Phenol column: Crude phenol → Refined phenol
  - Heavy ends: Tar, Acetophenone, Bisphenol-A precursors

---

## Process Block Diagram

```
BENZENE ──┐
           ├─→ [ALKYLATION] ─→ CUMENE ─→ [OXIDATION] ─→ CHP ─→ [CLEAVAGE] ─→ [DISTILLATION] ─→ PHENOL
PROPYLENE─┘                 ↑                                                        │             ACETONE
                    DIPB Transalkylation                                              └─ RECYCLE CUMENE/AMS
```

---

## Key Intermediates and Products

| Stream | Description | Typical Spec |
|--------|-------------|-------------|
| Benzene Feed | Polymer-grade benzene | ≥99.9 wt% |
| Propylene Feed | Chemical-grade propylene | ≥99.5 wt% |
| Cumene Product (internal) | Feed to oxidation | ≥99.5 wt% cumene |
| CHP Concentrate | Feed to cleavage | 80–88 wt% CHP |
| Refined Phenol | Product | ≥99.9 wt% phenol |
| Refined Acetone | Co-product | ≥99.5 wt% acetone |
| AMS | By-product (hydrogenated to cumene or sold) | — |

---

## Process Sections Summary

| Code | Section | Refinery Operations Ltd. Name | Purpose | Key Hazard |
|------|---------|-----------|---------|-----------|
| ALKY | Alkylation | *(TBC)* | Make Cumene | High-pressure, flammable hydrocarbons |
| OXI | Oxidation | Oxidation Section | Make CHP | Peroxide accumulation, thermal runaway |
| CDN | Concentration + Decomposition + Neutralization | CDN Section | Concentrate CHP → Make Phenol + Acetone → Neutralize | Exothermic decomposition, thermal runaway, acid |
| DIST | Distillation | Fractionation + Phenol Recovery | Purify products | Flammable vapors, phenol skin absorption |
| UT | Utilities | Utilities | Steam, cooling water, N₂, instrument air | — |
| ETP | Effluent Treatment | ETP | Treat phenolic wastewater | Phenol toxicity |

**Plant-specific note:** Refinery Operations Ltd. uses "CDN" for the combined Concentration + Decomposition + Neutralization section. This is a UOP-specific process design. See [[units/cdn]] for full plant data.

---

## Critical Process Constraints

1. **CHP Concentration (Oxidation)**: Must not exceed ~35 wt% — above this, thermal decomposition risk increases sharply. See [[hazards/cumene-hydroperoxide]]
2. **Cleavage Temperature**: Strictly controlled — runaway decomposition if temperature rises uncontrolled
3. **Phenol Handling**: Significant skin absorption hazard — refer to [[hazards/phenol]]
4. **Wastewater**: Phenolic water must be treated before discharge — [[units/etp]] *(pending)*

---

## Status of Wiki

This overview will be updated as source documents are ingested. Current state reflects general Hock Process knowledge. Plant-specific data (equipment tags, operating limits, exact specifications) will be integrated from PFDs, P&IDs, Data Sheets, and Operating Manuals.

See [[index]] for current wiki coverage.
