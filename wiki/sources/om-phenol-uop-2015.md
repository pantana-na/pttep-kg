---
name: UOP Phenol Process General Operating Manual
filename: OM-Phenol Unit UOP-2015.pdf
type: operating_manual
unit: ALL
tags: [source, operating-manual, UOP, licensor]
ingested: 2026-06-13
pages: 388
---

# Source: OM-Phenol Unit UOP-2015.pdf

## Document Identity

| Field | Value |
|-------|-------|
| Title | UOP Phenol Process with Hüls MSHP™ Process — Process Technology Manual |
| Document No. | UOP 147086, Rev 8 (also referenced as 147086-6) |
| Licensor | UOP (A Honeywell Company) |
| Confidentiality | Confidential — UOP written permission required for disclosure |
| Pages | 388 |
| Location | `raw/operating_manuals/OM-Phenol Unit UOP-2015.pdf` |

## Coverage

This is the **licensor's General Operating Manual (GOM)** for the UOP Phenol Process. It is the primary and highest-authority operating reference document. It covers all process sections:

| Section | GOM Sections |
|---------|-------------|
| Alkylation (ALKY) | Section V |
| Oxidation (OXI) | Sections II, III, VII, X, XI |
| Concentration/Decomposition/Neutralization (CDN) | Sections II, III, VII, IX, X, XI |
| Distillation/Fractionation (DIST) | Sections II, III, VII, X, XI |
| AMS Hydrogenation (Hüls MSHP) | Sections III, VII, X, XI |
| Phenol Recovery Unit (PRU) | Section XI |

## Sections Extracted (CDN Focus)

| GOM Section | Pages (PDF) | Content | Extracted |
|-------------|-------|---------|-----------|
| II — Process Description | 24–70 | Chemical basis, stream tables, process chemistry, CDN design basis | Yes |
| III.B–D — Process Parameters | ~80–120 | CDN operating windows: concentration, decomposition, neutralization | Yes |
| **V — Pre-commissioning** | **157–178** | **Equipment inspection, hydrostatic/leak/vacuum testing, line flushing, pump run-in, instrument calibration, plant services commissioning, ejector/vacuum system commissioning, air-freeing — CDN-relevant items extracted** | **Yes (2026-06-16)** |
| **VI.A/B — Start-up (Initial + Normal)** | **179–232** (CDN: 197–202, 215–225) | **Concentration/Decomposition/Neutralization start-up sequence, including the decomposer feed-in safety sequence (acid build-up, feed-in verification, runaway-decomposition warning, post-feed-in optimization)** | **Yes (2026-06-16)** |
| VII.2–4 — Normal Operations | ~220–260 | CDN normal operations procedures: concentration, decomposition, neutralization | Yes |
| IX — Troubleshooting | ~290–320 | CDN troubleshooting: poor AMS yield, high acidity, dehydrator plugging | Yes |
| X.B–D — Normal Shutdown | ~330–340 | CDN normal shutdown procedures | Yes |
| XI.A–H — Emergency Procedures | 340–362 | CDN + service system emergency procedures; shutdown logic Table XI-1 | Yes |

## Key Findings

### CDN Operating Windows (Licensor Authority)
See [[parameters/cdn-operating-windows]] for compiled limits.

**Concentration Section:**
- Flash zone pressure: 22–27 mmHg
- Flash column max temperature: 110°C (alarm), 120°C (ESD)
- CHP concentration in flash column bottoms: 80–84 wt% target

**Decomposition Section:**
- Decomposer temperature: 60°C normal; 70°C for startup/shutdown; ESD trip at 57°C low
- H₂SO₄ in circulation: 40–60 wt ppm normal; 300 wt ppm minimum before restart
- CHP in circulating liquid: 1–1.5 wt% normal; >2 wt% → instability warning
- Water in circulating liquid: 1–2 wt% target; >2 wt% → reaction inhibition
- Dehydrator effluent temperature: 125–145°C; minimum 120°C (ESD)
- DCP in crude product: 100–300 wt ppm target

**Neutralization:**
- pH of crude product: 2.3–2.7

**Critical Calorimeter Parameters:**
- First stage ΔT: ~7.2°C per wt% CHP (conversion factor)
- Operating range: Specific values per plant design (see plant data sheets)
- H₂SO₄ at calorimeter 2nd stage local: 4000–6000 wt ppm normal
- Danger threshold: <20 wt ppm H₂SO₄ in bulk circulation = dangerous condition

### Emergency Procedure Highlights
- "Ready for Feed In" conditions: 70°C, 300 ppm H₂SO₄, <2 wt% water, 0 kg/h water injection
- Loss of H₂SO₄ below 20 ppm: EXTREMELY DANGEROUS — re-introduction risk of uncontrolled decomposition
- Complete loss of H₂SO₄ → automatic ESD
- UOP recommends never operating decomposer without at least one calorimeter in service
- Minimum CHP concentration for decomposer feed (from flash column): 70 wt%

### Shutdown Interlock Logic (Table XI-1)
Concentration/Decomposition interlock table covers 15 actions with full cause-and-effect matrix. See [[procedures/emergency-cdn]] for complete matrix.

### Troubleshooting Findings
CDN-specific issues documented: Poor AMS yield, high acidity in flash column, dehydrator plugging.

### Start-up / Pre-commissioning Highlights (added 2026-06-16)
- **Decomposer feed-in is the highest-risk single operation in CDN start-up**: acid must reach 300 wt ppm before feed-in (without overshoot — risk of pump cavitation from too-fast reaction); if no exothermic response is seen after feed-in, CHP must be lab-confirmed <0.2 wt% before any acid increase — otherwise risk of runaway decomposition/explosion.
- Calorimeter zero ΔT at feed-in (high-acid/high-temp condition) is **normal**, not a fault — must not be misread as "no reaction."
- Post-feed-in temperature step-down to design 60°C must be done 1°C at a time, ≥15 min apart; acid rate increases during optimization capped at ≤5% per step — same runaway risk applies during optimization as at initial feed-in.
- Decomposer feed line must always be flushed with cumene before feed-in (twice the standing volume at the distributor, minimum).
- Pre-commissioning of the concentration vacuum system (X-2301 ejectors + P-2316A/B) requires steam-line cleaning before first use (jets are only a few mm — debris causes repeated capacity loss) and a 1-hour vacuum leak-test hold with no pressure change before hydrocarbon introduction.
- CHP and acid aromatics drain routing must be leak-tested and individually verified at commissioning — not assumed correct from the P&ID — given the strict separation requirement between the two systems.

## Pages Created / Updated from This Source

### Pages Created
- [[parameters/cdn-operating-windows]] — Full CDN operating window table
- [[procedures/emergency-cdn]] — CDN emergency procedures (Sections XI.D–E + Table XI-1)
- [[procedures/normal-shutdown-cdn]] — CDN normal shutdown (Section X.B–D)
- [[procedures/normal-operations-cdn]] — CDN normal operations (Section VII.2–4)
- [[procedures/precommissioning-cdn]] — CDN pre-commissioning/commissioning (Section V; added 2026-06-16)
- [[procedures/startup-cdn]] — CDN initial and normal start-up (Section VI.A/B; added 2026-06-16)
- [[troubleshooting/cdn-poor-ams-yield]] — Section IX troubleshooting
- [[troubleshooting/cdn-high-acidity-flash-column]] — Section IX troubleshooting
- [[troubleshooting/cdn-dehydrator-plugging]] — Section IX troubleshooting
- [[sources/om-phenol-uop-2015]] — This page

### Pages Updated
- [[units/cdn]] — Added GOM operating parameters and licensor design basis
- [[equipment/D-2304]] — Added licensor operating parameters
- [[equipment/V-2301]] — Added CHP concentration targets and temperature limits

## Confidence Note
All data in pages sourced from this document is licensor-specified. Mark as:
`[Source: OM-Phenol Unit UOP-2015.pdf, UOP licensor]`
This supersedes general chemical engineering knowledge wherever it conflicts.

## References
- [[units/cdn]]
- [[parameters/cdn-operating-windows]]
- [[procedures/emergency-cdn]]
- [[procedures/normal-shutdown-cdn]]
- [[procedures/normal-operations-cdn]]
- [[hazards/cumene-hydroperoxide]]
