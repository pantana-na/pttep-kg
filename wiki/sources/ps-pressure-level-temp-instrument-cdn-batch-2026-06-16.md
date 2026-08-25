---
name: CDN Pressure, Level & Temperature Instrument Process Data Sheets
tags: [source, instruments, CDN]
sources: ["14780-8120-PS-0032_PRESSURE INSTRUMENT PROCESS DATA SHEET (CDN)_Z1.pdf", "14780-8120-PS-0033_LEVEL INSTRUMENT PROCESS DATA SHEET (CDN)_Z1.pdf", "14780-8120-PS-0034_TEMPERATURE INSTRUMENT PROCESS DATA (CDN)_Z1.pdf"]
last_updated: 2026-06-16
---

# CDN Pressure, Level & Temperature Instrument Process Data Sheets

**Documents:** 3 AS-BUILT (Rev Z1, May 10, 2016) UOP/POSCO process specifications for PTT Phenol Train II Project (Job No. 120117), CDN Unit, owner PTT Phenol Company Limited (PPCL).

| Doc No. | Title | Pages | Tag Count |
|---------|-------|-------|-----------|
| 14780-8120-PS-0032 | Pressure Instrument Process Data Sheet | 40 | 61 (13 PT, 6 PDT, 42 PI) |
| 14780-8120-PS-0033 | Level Instrument Process Data Sheet | 22 | 38 (21 LT/LXT, 1 radar, 1 switch, 13 LGR, 1 LS) |
| 14780-8120-PS-0034 | Temperature Instrument Process Data Sheet | 28 | 65+ (33 TE/TT, 13 RTD, 22 TXT, 1 special, 6 thermometer/output) |

**Source:** POSCO Engineering Co., Ltd. for PTT Phenol Train II Project. Original UOP LLC project specifications (963766 series) supplemented with PTT/Bechtel-format CDN-specific data sheets, dated 25 JUN 2012 (UOP base spec) through 10 MAY 2016 (As-Built finalization).

## Purpose

These three documents complete the CDN basic-process-measurement instrumentation picture, complementing the PSV/Flow/Control Valve/Analyzer batch ingested earlier on 2026-06-16 ([[sources/ps-prv-cdn-batch-2026-06-16]], [[sources/ps-flow-instrument-cdn-batch-2026-06-16]], [[sources/ps-control-valve-cdn-batch-2026-06-16]], [[sources/ps-analyzer-cdn-batch-2026-06-16]]). Together, all seven instrument data sheets (PS-0003, 0010, 0018, 0031, 0032, 0033, 0034) now give the CDN unit a fully documented field instrumentation basis.

## Wiki Pages Created

- [[instruments/pressure-instruments-cdn]] — 61 pressure tags (transmitters, dP transmitters, local gauges)
- [[instruments/level-instruments-cdn]] — 38 level tags (DP/capillary transmitters, radar, switch, gauges)
- [[instruments/temperature-instruments-cdn]] — 65+ temperature tags (thermocouples, RTDs, field transmitters, special in-tube assembly)

## Key Findings

1. **Calorimeter differential-temperature instrument ranges confirmed** (PS-0034) — closes the numeric-range portion of the gap flagged in [[wiki/index]] Gaps Item 7. Six distinct ΔT tags now documented with calibrated spans (0–40°C total system / 0–25°C calorimeter / 0–20°C inlet line), reconciled against the existing TDXSHH/TDXAHH SIS tags on [[equipment/X-2308]]. The exact numeric trip setpoint within each span remains a smaller residual gap.
2. **D-2304 (Decomposer Drum) carries three independent level transmitters** — LT-23-1301 (DCS) plus LXT-23-1302/1303 (SIS, feeding the already-known LXSHH-1302/1303 trips) — all sharing a Decomposer-liquid reference leg (SG 0.920).
3. **D-2307's "Radar Level" tag identified**: LT-23-2001, a Magnetrol (or equal) guided-wave radar measuring a 2100mm span across a mixed Acetone/Phenol/CHP/Cumene/H₂SO₄(trace)/H₂O fluid.
4. **Possible tag overlap flagged (not resolved):** LS-23-2005's data-sheet service description ties it to the Acid Aromatics Sump Pit ([[equipment/X-2321]]), while the existing wiki record (sourced from the equipment table) ties "LS-2005" to the LOW LEVEL STOP on [[equipment/P-2304A]] suction from [[equipment/D-2307]]. Flagged on both equipment pages for field-tag verification.
5. **V-2301 and V-2302 vacuum operation independently confirmed** by absolute-pressure transmitters (PT-23-0401/0402, PT-23-0801/0802) reading in the 15–150 mmHg(a) range.
6. **TE-23-0701 special instrument** — a vendor-engineered RTD thermowell assembly mounted *inside* an [[equipment/E-2304]] exchanger tube (24" / 600mm below the tube-bundle top), an unusually direct internal-tube temperature measurement.
7. No internal document conflicts or tag-naming inconsistencies were found in these three documents (contrast with the Flow Instrument batch, which had two).

## References

- [[instruments/pressure-instruments-cdn]]
- [[instruments/level-instruments-cdn]]
- [[instruments/temperature-instruments-cdn]]
- [[equipment/X-2308]] — Calorimeters (primary beneficiary of the ΔT range data)
- [[equipment/D-2304]] — Decomposer Drum
- [[equipment/D-2307]] — Acid Aromatics Sump
- [[equipment/X-2321]] — Acid Aromatics Sump Pit
- [[equipment/V-2301]], [[equipment/V-2302]] — Preflash/Flash Columns
- [[sources/ps-prv-cdn-batch-2026-06-16]], [[sources/ps-flow-instrument-cdn-batch-2026-06-16]], [[sources/ps-control-valve-cdn-batch-2026-06-16]], [[sources/ps-analyzer-cdn-batch-2026-06-16]] — companion instrument data sheet batch (same ingest day)
