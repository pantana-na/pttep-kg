---
name: CDN Static Vessel Process Data Sheets (11 sheets)
tags: [source, data-sheet, vessel, CDN]
last_updated: 2026-06-16
---

# Source: CDN Static Vessel Process Data Sheets — D-2301 to D-2312 (11 sheets)

> **Bookkeeping note (2026-06-16):** Ten of these eleven data sheets (D-2301, D-2302, D-2303, D-2304, D-2306, D-2307, D-2308, D-2309, D-2310, D-2311) were read and their content merged into the corresponding [[equipment/]] pages in an earlier pass (pages carry `last_updated: 2026-06-14`), but this source summary page was never written and the ingestion was never logged in `wiki/log.md` or `wiki/index.md`. This page completes that bookkeeping retroactively. The eleventh sheet, **D-2312 (Diamine Injection Tank)**, was not previously touched and is newly ingested as of 2026-06-16 — see the identity conflict it raised, below.

## Documents

| Doc No. | Item | Title | Rev | Date |
|---------|------|-------|-----|------|
| 14780-8120-PS-D2301 | D-2301 | Concentration Cumene Quench Drum | Z1 (AS BUILT) | 2016-05-10 |
| 14780-8120-PS-D2302 | D-2302 | Cumene Flush Drum | Z1 (AS BUILT) | 2016-05-10 |
| 14780-8120-PS-D2303 | D-2303 | Decomposer Feed Flush Drum | Z1 (AS BUILT) | 2016-05-10 |
| 14780-8120-PS-D2304 | D-2304 | Decomposer Drum | Z1 (AS BUILT) | 2016-05-10 |
| 14780-8120-PS-D2306 | D-2306 | Acid Aromatics Knockout Drum | Z1 (FINAL ISSUE) | 2016-05-10 |
| 14780-8120-PS-D2307 | D-2307 | Acid Aromatics Sump | Z1 (AS BUILT) | 2016-05-11 |
| 14780-8120-PS-D2308 | D-2308 | Preflash Column Steam Heater Condensate Drum | Z1 (AS BUILT) | 2016-05-11 |
| 14780-8120-PS-D2309 | D-2309 | Flash Column Vaporizer Condensate Drum | Z1 (AS BUILT) | 2016-05-11 |
| 14780-8120-PS-D2310 | D-2310 | 98% Sulfuric Acid Injection Tank | Z1 (AS BUILT) | 2016-05-10 |
| 14780-8120-PS-D2311 | D-2311 | 98% Sulfuric Acid Refill Tank | Z1 (AS BUILT) | 2016-05-10 |
| 14780-8120-PS-D2312 | D-2312 | Diamine Injection Tank | Z1 (AS BUILT) | 2016-05-10 |

Source: POSCO Engineering & Construction for PTT Phenol Train II (PPCL), Project No. 120117. Licensor: UOP/Honeywell. All vessel sheets co-stamped Bechtel and reference UOP Project Specification 963766-301 (Vessels) and UOP Standard Specification 3-11/3-15.

**Purpose:** Provides mechanical/material design data (shell/head material, corrosion allowance, MDMT, design pressure/temperature, specific gravity/density, nozzle schedules) for all remaining CDN static vessels not yet covered by heat exchanger or rotating equipment data sheet batches. Closes PSI Readiness Category 6 (Equipment Data Sheets) for the CDN section's static vessel population (D-2301 through D-2312, less D-2305 which does not exist as a tag).

## Key Findings

- **D-2304 (Decomposer Drum)** confirmed SA 240 Type 304L stainless steel construction (not carbon steel) — consistent with H₂SO₄/CHP decomposition service; CA only 1.5mm reflecting SS corrosion resistance vs 3mm for CS vessels.
- **D-2307 (Acid Aromatics Sump)** is an **existing Train I vessel** (original fabrication drawing 13850-8430-13-1307, 2007) — no modifications required for Train II; vessel is shared between trains. Operating pressure corrected from 0.01 to 0.10 kg/cm²g (HP flare header backpressure basis).
- **D-2308 operating temperature corrected from 63°C to 117°C** — consistent with SC1.5 steam condensate near saturation at 0.9 kg/cm²g; previous P&ID-derived figure was a transcription error.
- **D-2309 insulation corrected from H(80) to H(90)**.
- **D-2310/D-2311 (98% H₂SO₄ tanks)**: both confirmed SA 240 Type 304L, MDMT 15°C, density 1728.7 kg/m³; readymade totes acceptable (0.55 m³ operating volume).
- **D-2312 (Diamine Injection Tank) — ⛔ CRITICAL IDENTITY CONFLICT:** the data sheet's Fluid Name field reads **"DIAMINE(HMDA)"**, i.e. Hexamethylenediamine (CAS 124-09-4), density 914 kg/m³, Amine service = YES. This conflicts with [[hazards/diamine-tbc]], which previously "confirmed" the additive as DIPA (Diisopropanolamine, CAS 110-97-4) based on an SDS file literally named with "placeholder" in it. DIPA's typical density (~1010 kg/m³) does not match the DS value (914 kg/m³); HMDA is the better fit. **This as-built engineering document takes primacy over the placeholder SDS match per the Standards Primacy Rule — flagged in both [[equipment/D-2312]] and [[hazards/diamine-tbc]]. A genuine HMDA-specific SDS must be sourced before HAZOP touches this node.**

## Pages Updated

- [[equipment/D-2301]], [[equipment/D-2302]], [[equipment/D-2303]], [[equipment/D-2304]], [[equipment/D-2306]], [[equipment/D-2307]], [[equipment/D-2308]], [[equipment/D-2309]], [[equipment/D-2310]], [[equipment/D-2311]] — mechanical data merged 2026-06-14 (bookkeeping completed 2026-06-16)
- [[equipment/D-2312]] — mechanical data + fluid identity conflict added 2026-06-16
- [[hazards/diamine-tbc]] — identity conflict flag added 2026-06-16

## References

- [[units/cdn]]
- [[hazop/study-info]]
