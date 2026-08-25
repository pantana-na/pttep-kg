---
name: CDN Analyzer Register
unit: CDN
tags: [instruments, analyzer, AT, AY, CHP, H2SO4, O2, CDN]
sources: [14780-8120-PS-0003_ANALYZER PROCESS DATA SHEET CDN SECTION_Z1.pdf]
last_updated: 2026-06-16
---

# CDN Analyzer Register

**Source:** 14780-8120-PS-0003, Rev Z1 (AS-BUILT), PTT Phenol Train II, POSCO Engineering / UOP licensor basis. 5 analyzer systems across 12 pages.

> **Tag-format note:** every tag in this source carries the "23-" area prefix and is dual-labeled **AT/AY** (transmitter + relay/converter), e.g. `AT/AY-23-0801`, whereas earlier wiki ingests recorded these as bare `AI-0801A/B`. Cross-checked below — in the two CHP cases this is a **naming-convention difference, not a real instrument discrepancy**: each is a single density-measuring transmitter with two simultaneous 4–20 mA outputs (density span + converted CHP wt%), which is exactly what the wiki's "A/B" pair represented. The two acid analyzers and the O₂ analyzer match the wiki's existing tags directly once the prefix is normalized.

---

## CHP Concentration (Density-Based) Transmitters

| Tag | Location | Density Span | CHP Range (converted) | Normal Conditions | Wetted Materials | Supplier |
|-----|----------|--------------|------------------------|---------------------|-------------------|----------|
| AT/AY-23-0801 | Preflash and Flash Columns Overhead Liquid | 700–1000 kg/m³ | 0–10 wt% CHP | 7.394 kg/cm²(g), 39°C (range 30–80°C), SG 0.848 | 316 SS body, 1" Cl.150 RF, built-in Pt RTD | Thermo Fisher Scientific (Sarasota) |
| AT/AY-23-0901 | Flash Column Bottoms | 800–1100 kg/m³ | 50–90 wt% CHP | 3.384 kg/cm²(g), 60°C (range 40–90°C), SG 0.972 | 316 SS body, 1" Cl.150 RF, built-in Pt RTD | Thermo Fisher Scientific (Sarasota) |

Both use a shared density-vs-temperature-vs-CHP% lookup table (full table transcribed in source, 20–100°C × 0–90 wt% CHP — available on request if needed for parameter pages). Accuracy ±0.0001 g/cm³; output 4–20 mA dual (density span + CHP wt%).

> ⚠️ Source explicitly warns: "Actual CHP concentration may be different than the indicated value of the on-stream monitor... Lab analysis for CHP concentration should be routinely submitted for verification." This online analyzer is an inferential measurement (density proxy), not a direct CHP assay — treat as a control input, not a definitive safety measurement, without periodic lab cross-check.

**Reconciliation with existing wiki tags:**
- [[equipment/P-2307AB]] **AI-0801A** (CHP conc.) / **AI-0801B** (density) = the two simultaneous outputs of **AT/AY-23-0801**. Service description ("Preflash and Flash Columns Overhead Liquid") is the condenser sump liquid that P-2307A/B pump onward — consistent with the wiki's framing of this as the CHP "safety gate" on recycle cumene to OXI.
- [[equipment/P-2301AB]] **AI-0901A/B** = the two outputs of **AT/AY-23-0901** on Flash Column Bottoms — consistent with wiki's description (CHP % feeding the Decomposer via P-2301A/B).

## Sulfuric Acid (Colorimetric Titration) Analyzers

| Tag | Location | Range | Normal | Composition (wt%) | Equipment |
|-----|----------|-------|--------|---------------------|-----------|
| AT/AY-23-1701 | Decomposer Circulating Liquid | 0–350 wt ppm H₂SO₄ | 40 ppm (300 ppm during start-up) | Phenol 48.94, Acetone 30.25, Cumene 12.54, Dicumylperoxide 3.91, CHP 1.87, Water 0.93 | [[equipment/E-2307]] / [[equipment/D-2304]] loop |
| AT/AY-23-1901 | Crude Product to Fractionation Feed Tanks | 20–60 wt ppm H₂SO₄ | 38 ppm | Phenol 51.31, Acetone 30.76, Cumene 13.48, AMS 2.05, Water 1.11, Cumyl Phenols 0.48 | [[equipment/X-2310AB]] downstream |

Method: acid-base titration against known caustic, fixed pH endpoint. Analysis frequency programmable (initial 15 min), automatic/menu-driven calibration. **Reaction cup material shall NOT be PTFE** (explicit exclusion in both data sheets — material compatibility note). Fast-loop sample piping max 12" (300mm) from tap to conditioning system; drains route to both Acid Aromatics Sump and Phenolic Waste Water Sump.

> ⚠️ **Start-up acid spike:** AT/AY-23-1701 design basis explicitly allows up to **300 wt ppm H₂SO₄** during start-up vs. 40 ppm normal operation — a ~7.5× transient increase. This should be cross-checked against Decomposer/E-2307 corrosion allowances and acid-injection ratio control safeguards during any HAZOP startup-deviation analysis.

**Reconciliation with existing wiki tags:** matches [[equipment/E-2307]] **AT-1701** and [[equipment/X-2310AB]] **AT-1901** directly (tag numbers identical once the "23-" prefix is dropped); service descriptions consistent (AT-1901 sits on the crude product line downstream of the static mixers, en route to Fractionation feed tanks, which is exactly where the wiki already places it).

## Oxygen Analyzer

| Tag | Location | Type | Range | Normal Composition (mol%) | Destination |
|-----|----------|------|-------|------------------------------|--------------|
| AT-23-1001 | Concentration Vacuum Producing Equipment Vent | Paramagnetic O₂, with sample/calibration gas selector panel | 0–10% O₂ (±2% of range) | O₂ 4.97, N₂ 92.51, H₂O 2.17, Cumene 0.31, Acetone/Formic acid trace | Charcoal Adsorber System (not direct atmospheric vent) |

Sample conditioning: regulator → filter/moisture separator → sample pump → analyzer. All sample-wetted metal parts 316 SS. Supplier: Teledyne Analytical Instruments (or equal).

**Reconciliation with existing wiki tag:** matches [[equipment/X-2301]] **AI-1001**. Service and routing (vacuum equipment vent → Charcoal Adsorber) are consistent with the existing page. No explicit "<5% O₂" alarm setpoint appears in *this* data sheet — that target figure is sourced separately from the PS-X2301 vendor spec already cited on the X-2301 page; this analyzer's own range is simply 0–10% O₂ with no discrete setpoint configured in the transmitter data sheet itself.

## Utilities (shared across analyzer systems)

| System | Electrical | Air | Other |
|--------|-----------|-----|-------|
| Acid analyzers (1701/1901) | 220V/50Hz | 7.0 kg/cm²(g) @ 38°C | Process Water 5.0 kg/cm²(g) @ 50°C; N₂ 7.0 kg/cm²(g) @ 38°C; Steam 135°C @ 1.5 kg/cm²(g) |
| O₂ analyzer (1001) | 220V/50Hz | — | Cooling Water 33°C @ 3.9 kg/cm²(g); ambient design 15–40°C |

## References

- [[sources/ps-analyzer-cdn-batch-2026-06-16]] — source summary
- [[equipment/P-2307AB]], [[equipment/P-2301AB]] — CHP concentration analyzers
- [[equipment/E-2307]], [[equipment/X-2310AB]] — acid analyzers
- [[equipment/X-2301]] — oxygen analyzer
- [[hazards/cumene-hydroperoxide]] — CHP safety basis for density/CHP transmitters
