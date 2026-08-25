---
name: HAZOP Risk Matrix — PTT GC RAM W-(Q-MP)-002
tags: [hazop, risk-matrix, standard]
source: W-(Q-MP)-002_R2.pdf
governing_section: "§6.2.1.3.1 — RAM for Process Hazard Analysis (PHA)"
last_updated: 2026-06-17
---

# HAZOP Risk Matrix — PTT GC Operational RAM

> **Governing Document:** W-(Q-MP)-002 Rev.2 (10/09/2025) — PTT Global Chemical Operational Risk Assessment Matrix
> **Applicable Section:** §6.2.1.3.1 — RAM for Process Hazard Analysis (PHA)
> **Source file:** `raw/standards/W-(Q-MP)-002_R2.pdf`
> **Source summary:** [[wiki/sources/W-Q-MP-002]]
> **Independently corroborated by:** GC ePHA Template v5.0 (Risk Ranking) — `raw/standards/GC_ePHA_Template_v5.0(Risk Ranking).xlsm`. See [[wiki/sources/gc-epha-template-v5-risk-ranking]]. Core matrix, Likelihood, People, Environment, and Social tables match exactly between both sources; Economic table has a category-naming and value CONFLICT — see note in that section below.

This page is the **single authoritative risk ranking reference** for all HAZOP node analyses in this wiki. Per the Standards Primacy Rule in CLAUDE.md, all Severity, Likelihood, and Risk rankings must cite this page.

---

## Risk Assessment Process (per §6.2.1.1)

1. **Identify** potential Consequences for each deviation
2. **Estimate Severity** (1–5) for each consequence category (PEES)
3. **Estimate Likelihood** (1–5) — first WITHOUT safeguards (Initial Risk), then WITH safeguards (Mitigated Risk)
4. **Determine Risk Rating** from the 5×5 matrix below

> ⚠️ **Severity never changes** between Initial and Mitigated assessment. Only Likelihood changes when safeguards are applied.

---

## Likelihood Levels — PHA Application (§6.2.1.3.1)

[Confirmed: W-(Q-MP)-002_R2.pdf, GC_ePHA_Template_v5.0(Risk Ranking).xlsm]

| Level | Label | Frequency Basis |
|-------|-------|----------------|
| 5 | Frequent | Has happened **more than once per year** at the Location |
| 4 | Likely | Has happened **at the Location** OR more than once/year in PTTGC group |
| 3 | Possible | Has happened in the **PTTGC group** OR more than once/year in the Industry |
| 2 | Unlikely | **Possible to occur** in the Industry (or has occurred in Industry) |
| 1 | Improbable | **Unlikely to occur** in the Industry (or has not occurred) |

*Note: "Location" refers to the specific plant/site being studied.*

---

## Consequence Severity — People (§6.2.1.3.1)

[Confirmed: W-(Q-MP)-002_R2.pdf, GC_ePHA_Template_v5.0(Risk Ranking).xlsm]

| Level | Label | People Consequence |
|-------|-------|--------------------|
| 5 | Extreme | **More than one fatality**; High health effect; Employees or Contractors strike |
| 4 | High | **Single fatality** or Permanent Total Disability (PTD); High health effect; Protesters rally or official complaint |
| 3 | Medium | **Loss Time Injury (LTI)**; Medium health effect; Long-term morale impact |
| 2 | Low | **Medical treatment** or Restricted Work Case; Low health effect; Short-term morale impact |
| 1 | Very Low | **No injury** or First Aid Case; No or very low health effect; No or minimal morale impact |

---

## Consequence Severity — Environment (§6.2.1.3.1)

[Confirmed: W-(Q-MP)-002_R2.pdf, GC_ePHA_Template_v5.0(Risk Ranking).xlsm]

| Level | Label | Environment Consequence |
|-------|-------|------------------------|
| 5 | Extreme | **Massive Effect** — severe, wide-area, long-duration environmental impact |
| 4 | High | **Major Effect** |
| 3 | Medium | **Moderate Effect** |
| 2 | Low | **Minor Effect** |
| 1 | Very Low | **No / Slight Effect** |

---

## Consequence Severity — Economic (§6.2.1.3.1)

Economic thresholds vary by plant category. For HAZOP at PTT Phenol, apply the relevant category:

> ✅ **RESOLVED FOR PPCL (2026-06-17):** PPCL is classified **BU**. Use the **BU** economic thresholds from the GC ePHA Template v5.0 table below — Extreme(5) ≥100 M THB; High(4) 10–<100 M; Medium(3) 1–<10 M; Low(2) 0.1–<1 M; Very Low(1) <0.1 M. This governs all PPCL HAZOP node Economic severity scoring (first applied in [[wiki/hazop/nodes/cdn-N02]]). The category-naming conflict below is retained for reference; the BU column is the one in force for this study. Decision provided by the study owner.

> ⛔ **CONFLICT (historical reference — superseded for PPCL by the BU resolution above)** [W-(Q-MP)-002_R2.pdf vs GC_ePHA_Template_v5.0(Risk Ranking).xlsm]: the two governing sources use different category names AND, for two of three categories, different THB thresholds. W-(Q-MP)-002 R2 names categories **Upstream / Downstream / GC-S**; the GC ePHA Template v5.0 names categories **GPC / BU / Small BU**. The **Upstream** column matches **GPC** exactly. **Downstream** does **not** match **BU**, and **GC-S** does **not** match **Small BU** (see GPC/BU/Small BU table below). Resolve which category applies to PTT Phenol (PPCL) and which document's numbers govern before using Economic severity in any node worksheet. See [[wiki/sources/gc-epha-template-v5-risk-ranking]] for the full side-by-side comparison.

### Upstream Plant (O-P1, O-P2, O-P3, O-P4, U-P1, U-CM, R-P1, R-RM, A-P1, A-P2) — per W-(Q-MP)-002 R2
| Level | Label | Loss (THB) |
|-------|-------|-----------|
| 5 | Extreme | ≥ 300 M THB |
| 4 | High | 30 – < 300 M THB |
| 3 | Medium | 3 – < 30 M THB |
| 2 | Low | 0.3 – < 3 M THB |
| 1 | Very Low | < 0.3 M THB |

### Downstream Plant (P-HD1, P-LD1, P-LL1, P-LL2, PH-P1, PH-P2, EO/EG, EA, GCO, GCP, GGC, Vencorex) — per W-(Q-MP)-002 R2
| Level | Label | Loss (THB) |
|-------|-------|-----------|
| 5 | Extreme | ≥ 150 M THB |
| 4 | High | 15 – < 150 M THB |
| 3 | Medium | 1.5 – < 15 M THB |
| 2 | Low | 0.15 – < 1.5 M THB |
| 1 | Very Low | < 0.15 M THB |

### GC-S and Smaller Plants — per W-(Q-MP)-002 R2
| Level | Label | Loss (THB) |
|-------|-------|-----------|
| 5 | Extreme | ≥ 50 M THB |
| 4 | High | 5 – < 50 M THB |
| 3 | Medium | 0.5 – < 5 M THB |
| 2 | Low | 0.05 – < 0.5 M THB |
| 1 | Very Low | < 0.05 M THB |

### GPC / BU / Small BU — per GC ePHA Template v5.0 (Risk Ranking)
| Level | Label | GPC (THB) | BU (THB) | Small BU (THB) |
|-------|-------|-----------|----------|-----------------|
| 5 | Extreme | ≥ 300 M | ≥ 100 M | ≥ 10 M |
| 4 | High | 30 – < 300 M | 10 – < 100 M | 1 – < 10 M |
| 3 | Medium | 3 – < 30 M | 1 – < 10 M | 0.1 – < 1 M |
| 2 | Low | 0.3 – < 3 M | 0.1 – < 1 M | 0.01 – < 0.1 M |
| 1 | Very Low | < 0.3 M | < 0.1 M | < 0.01 M |

> **Note:** PTT Phenol (PPCL) plant classification (Upstream vs Downstream vs GPC/BU/Small BU) should be confirmed with the HAZOP team before applying economic thresholds. PH-P1/PH-P2 codes in the Downstream category may refer to phenol plants. **GPC = Upstream is the only confirmed equivalence; do not assume Downstream = BU or GC-S = Small BU.**

---

## Consequence Severity — Social (§6.2.1.3.1)

[Confirmed: W-(Q-MP)-002_R2.pdf, GC_ePHA_Template_v5.0(Risk Ranking).xlsm]

| Level | Label | Social / Reputational Consequence |
|-------|-------|----------------------------------|
| 5 | Extreme | International media coverage / Customer stops purchase |
| 4 | High | National media coverage / Customer reduces purchase |
| 3 | Medium | Regional media coverage / Official complaint from government |
| 2 | Low | Local media coverage / Verbal complaint from community |
| 1 | Very Low | No impact to public / No media coverage |

---

## PHA Risk Matrix — 5×5 (§6.2.1.3.1)

[Confirmed: W-(Q-MP)-002_R2.pdf, GC_ePHA_Template_v5.0(Risk Ranking).xlsm]

Use the **highest** severity across all four PEES categories to determine the row, then combine with Likelihood for the final risk level.

```
                  SEVERITY
                  (1)        (2)        (3)        (4)        (5)
                  Very Low   Low        Medium     High       Extreme
                  ─────────────────────────────────────────────────────
LIKELIHOOD  (5)   Low        Medium     High       Extreme    Extreme
Frequent    (4)   Low        Medium     High       High       Extreme
            (3)   Low        Low        Medium     High       High
            (2)   Very Low   Low        Low        Medium     Medium
Improbable  (1)   Very Low   Very Low   Low        Low        Low
```

### Full matrix in tabular form:

| Likelihood ↓ / Severity → | S1 Very Low | S2 Low | S3 Medium | S4 High | S5 Extreme |
|--------------------------|-------------|--------|-----------|---------|------------|
| **L5 Frequent** | Low | Medium | **High** | **Extreme** | **Extreme** |
| **L4 Likely** | Low | Medium | **High** | **High** | **Extreme** |
| **L3 Possible** | Low | Low | Medium | **High** | **High** |
| **L2 Unlikely** | Very Low | Low | Low | Medium | Medium |
| **L1 Improbable** | Very Low | Very Low | Low | Low | Low |

---

## Risk Action Requirements (§6.2.1.1)

| Risk Level | Color | Action Required |
|-----------|-------|----------------|
| **Extreme** | Dark Red | Serious risk — **action & risk reduction plan immediately** |
| **High** | Red | Unacceptable risk — **action & risk reduction plan immediately** |
| **Medium** | Orange | Medium risk — **require risk reduction plan** |
| **Low** | Yellow | Acceptable risk — **require review of control plan** |
| **Very Low** | Green | Very low risk — no immediate action required |

*Source: W-(Q-MP)-002 §6.2.1.1, Table 6.2.1-1*

---

## Thai Regulatory Compliance Note (DIW 4×4 RAM)

For PHA conducted to comply with Thai DIW (Department of Industrial Works) regulation, a 4×4 sub-matrix applies:
- **Consequence levels:** (1) to (4) only — Severity "Extreme (5)" not included
- **Likelihood levels:** "Improbable (1)" to "Likely (4)" only — "Frequent (5)" not included
- **Risk levels available:** Very Low, Low, Medium, High (no Extreme in this sub-matrix)

This 4×4 sub-matrix is a regulatory subset; it does not change the core 5×5 RAM used for this HAZOP study.

---

## How to Apply in HAZOP Worksheets

For each deviation row in a HAZOP node worksheet:

1. **State the consequence** clearly (people injury, environmental release, equipment damage, business loss)
2. **Determine Severity** (1–5) using the PEES tables above — use the HIGHEST category
3. **Assign Initial Likelihood** (1–5) assuming NO safeguards — justify with frequency basis
4. **Look up Initial Risk** in the 5×5 table above
5. **List existing safeguards** (instrumented trips, alarms, physical barriers, procedures)
6. **Re-assess Likelihood** (1–5) with safeguards — severity stays the same
7. **Look up Mitigated Risk** in the 5×5 table above
8. **Generate Rec# if Mitigated Risk ≥ Medium** (or per HAZOP lead judgment if risk is borderline)

> Always cite this page as: `[[wiki/hazop/risk-matrix]]` in node worksheets.

---

## References
- [[sources/W-Q-MP-002]] — Source page for this document
- [[sources/gc-epha-template-v5-risk-ranking]] — Corroborating source; Economic category conflict documented here
- [[sources/P-Q-MP-OEMS-005]] — HAZOP procedure that mandates use of this RAM
- [[hazop/study-info]] — Node status and study scope
