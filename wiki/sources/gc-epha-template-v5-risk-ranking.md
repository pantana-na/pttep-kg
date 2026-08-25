---
name: GC ePHA Template v5.0 — Risk Ranking Matrix
type: standard
tags: [source, standard, risk-matrix, hazop, ephas]
last_updated: 2026-06-17
---

# Source: GC ePHA Template v5.0 (Risk Ranking)

**Issuer:** PTT Global Chemical Public Company Limited — official e-PHA recording template (SharePoint: `EHAZOP` site collection, host `spapps`, domain `PTTGC`)
**Files:**
- `raw/standards/GC_ePHA_Template_v5.0(Risk Ranking).xlsm` — full workbook (sheets: `metadata`, `RiskRank`, `Worksheet HAZOP-TPL_TLM`, `Worksheet HAZOP-TPL`, `Action Items-TPL`, `GWMaster`, `RiskMatrixMaster`, `Worksheet NoCode`, `P5-PID-Marked up Node`, `oldP6-Worksheet HAZOP-Node1`, `oldP7-Action Items`, `Risk Ranking`)
- `raw/standards/Risk Ranking Matrix.png` — image export of the `Risk Ranking` sheet (identical content to the xlsm sheet)

This is the live electronic recording tool referenced in [[wiki/hazop/methodology]] ("Recording tool: GC e-PHA online system or downloadable GC Excel template").

---

## Document Purpose

Official company HAZOP/PHA worksheet template (v5.0) used to record node worksheets, action items, and P&ID node markup directly into the GC e-PHA system. The `Risk Ranking` sheet embeds the company RAM as a reference tab inside the recording tool itself.

---

## Key Findings — Risk Ranking Sheet vs. existing [[wiki/hazop/risk-matrix]]

### Confirmed (matches W-(Q-MP)-002 R2 exactly)
- **5×5 Likelihood × Severity matrix** — `RiskMatrixMaster` sheet and `Risk Ranking` sheet values are identical to the matrix already in [[wiki/hazop/risk-matrix]]
- **Likelihood levels 1–5** (Improbable → Frequent) and frequency basis — identical wording
- **Severity — People** (1–5) — identical
- **Severity — Environment** (1–5) — identical
- **Severity — Social** (1–5) — identical
- **Risk level color/action bands** (Very Low → Extreme) — identical

→ Two independent company documents (W-(Q-MP)-002 R2 and this e-PHA template) now confirm the core RAM. [Confirmed: W-(Q-MP)-002_R2.pdf, GC_ePHA_Template_v5.0(Risk Ranking).xlsm]

### ⛔ CONFLICT — Severity Economic categories
The e-PHA template uses three economic-loss categories — **GPC**, **BU**, **Small BU** — with thresholds:

| Level | GPC (THB) | BU (THB) | Small BU (THB) |
|-------|-----------|----------|-----------------|
| 5 Extreme | ≥ 300 M | ≥ 100 M | ≥ 10 M |
| 4 High | 30 – < 300 M | 10 – < 100 M | 1 – < 10 M |
| 3 Medium | 3 – < 30 M | 1 – < 10 M | 0.1 – < 1 M |
| 2 Low | 0.3 – < 3 M | 0.1 – < 1 M | 0.01 – < 0.1 M |
| 1 Very Low | < 0.3 M | < 0.1 M | < 0.01 M |

The existing [[wiki/hazop/risk-matrix]] (from W-(Q-MP)-002 R2) uses three *differently named* categories — **Upstream**, **Downstream**, **GC-S** — with thresholds:

| Level | Upstream (THB) | Downstream (THB) | GC-S (THB) |
|-------|-----------------|--------------------|--------------|
| 5 Extreme | ≥ 300 M | ≥ 150 M | ≥ 50 M |
| 4 High | 30 – < 300 M | 15 – < 150 M | 5 – < 50 M |
| 3 Medium | 3 – < 30 M | 1.5 – < 15 M | 0.5 – < 5 M |
| 2 Low | 0.3 – < 3 M | 0.15 – < 1.5 M | 0.05 – < 0.5 M |
| 1 Very Low | < 0.3 M | < 0.15 M | < 0.05 M |

**GPC = Upstream** (numbers match exactly). **BU and Small BU do NOT match Downstream or GC-S** (BU thresholds are roughly double GC-S/Downstream's neighbor tier, no clean 1:1 mapping). [CONFLICT: W-(Q-MP)-002_R2.pdf names categories Upstream/Downstream/GC-S with one set of THB bands; GC_ePHA_Template_v5.0 names categories GPC/BU/Small BU with a different set of THB bands for two of the three tiers — resolve with HAZOP coordinator/safety engineer before applying economic severity at PTT Phenol]

PTT Phenol (PPCL) plant classification under either naming scheme has not yet been confirmed by the HAZOP team — this conflict compounds the existing open note in [[wiki/hazop/risk-matrix]] about classification.

### Additional content not yet incorporated into the wiki
- `GWMaster` sheet contains an expanded Parameter × Guideword deviation matrix (Flow, Pressure, Temperature, Level, Reaction, Mixing, Phase, Viscosity, Composition, Erosion, Corrosion, Service Failures, Sequence, Incident, Human, Other) — broadly consistent with Table 6.1 in [[wiki/hazop/methodology]] but more granular for some parameters (e.g., separate Erosion/Corrosion columns). Not ingested into methodology.md in this pass — flagged for future review.
- `Worksheet HAZOP-TPL`, `Action Items-TPL`, `P5-PID-Marked up Node` sheets define the official recording column layout for node worksheets and action items — useful for validating [[wiki/hazop/methodology]]'s "GC HAZOP Worksheet — Official Column Structure" section, but not cross-checked in this pass.
- `metadata` sheet confirms this is the live e-PHA SharePoint tool (`http://spapps/sites/EHAZOP`) — corroborates [[wiki/hazop/methodology]]'s GC HAZOP Workflow phases (Draft → Submitted → Publish → Complete) as the tool's actual status field options.

---

## Wiki Pages Updated From This Source
- [[wiki/hazop/risk-matrix]] — added "Confirmed by second source" notes to core matrix/People/Environment/Social tables; added CONFLICT flag to Economic severity table

## Related Documents
- [[wiki/sources/W-Q-MP-002]] — primary RAM source document (existing, now independently corroborated)
- [[wiki/hazop/methodology]] — references this template as the "GC Excel template" recording tool
