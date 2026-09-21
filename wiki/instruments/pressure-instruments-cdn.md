---
name: CDN Pressure Instrument Register
unit: CDN
tags: [instruments, pressure, PT, PI, PDT, PXT, CDN]
sources: ["14780-8120-PS-0032_PRESSURE INSTRUMENT PROCESS DATA SHEET (CDN)_Z1.pdf"]
last_updated: 2026-06-16
---

# CDN Pressure Instrument Register

**Source:** 14780-8120-PS-0032, Rev Z1 (AS-BUILT, May 2016), Refinery Phenol Train II, POSCO Engineering / UOP licensor basis. 40-page process specification covering pressure transmitters, differential pressure transmitters, and local pressure gauges across the CDN unit.

This is the consolidated reference for CDN pressure measurement devices. Individual equipment pages reference the relevant tags; this page holds the full sizing/range data.

---

## Pressure Transmitters (13 tags)

316SS or cadmium-plated CS/316SS wetted, 4–20 mA output, Honeywell/Rosemount (or equal). Two are absolute-pressure transmitters (vacuum service, mmHg(a)).

| Tag | Service | Calibrated Range | Process Temp | Process Press | Design P/T | Equipment |
|-----|---------|-------------------|--------------|----------------|------------|-----------|
| PT-23-0701 | S3 Steam to Flash Column Vaporizer | 0–3.5 kg/cm²(g) | 135°C | 1.8 kg/cm²(g) | 10.5 kg/cm²(g), FV / 195°C | [[equipment/E-2304]] |
| PXT-23-1201 | Process Water to Decomposer Feed | 3.52–21.0 kg/cm²(g) | 50°C | 5.4 kg/cm²(g) | 9.716 kg/cm²(g) / 120°C | Decomposer dilution water |
| PT-23-0501 | S1.5 Steam to Preflash Column Steam Heater | 0.3–1.85 kg/cm²(g) | 121°C | 0.7 kg/cm²(g) | 7.0 kg/cm²(g), FV / 195°C | [[equipment/E-2303]] |
| PT-23-1101 | Cumene Flush Drum | 0.3–1.85 kg/cm²(g) | 46°C | 0.7 kg/cm²(g) | 10.0 kg/cm²(g) / 120°C | [[equipment/D-2302]] |
| PT-23-1202 | Decomposer Feed Flush Drum | 0.3–1.85 kg/cm²(g) | 46°C | 0.7 kg/cm²(g) | 10.0 kg/cm²(g) / 120°C | [[equipment/D-2303]] |
| PT-23-0401 | Preflash Column Top | 15–75 mmHg(a) | 52°C | 15 mmHg(a) | 3.5 kg/cm²(g), FV / 250, 195°C | [[equipment/V-2301]] |
| PT-23-0402 | Preflash Column Bottom | 15–75 mmHg(a) | 70°C | 15 mmHg(a) | 3.5 kg/cm²(g), FV / 250, 195°C | V-2301 |
| PT-23-0801 | Flash Column Top | 15–75 mmHg(a) | 51°C | 15 mmHg(a) | 3.5 kg/cm²(g), FV / 250, 195°C | [[equipment/V-2302]] |
| PT-23-0802 | Flash Column Bottom | 30–150 mmHg(a) | 95°C | 30 mmHg(a) | 3.5 kg/cm²(g), FV / 250, 195°C | V-2302 |
| PXT-23-1001 | Preflash/Flash Overhead Vapor to Overhead Vapor Chiller | 8–50 mmHg(a) | 38°C | 8 mmHg(a) | 4.5 kg/cm²(g), FV / 120°C | [[equipment/E-2310]] |
| PT-23-1002 | Preflash/Flash Overhead Vapor to Overhead Vapor Chiller | 8–40 mmHg(a) | 38°C | 8 mmHg(a) | 4.5 kg/cm²(g), FV / 120°C | E-2310 |
| PT-23-1401 | Crude Product to Crude Product Cooler | 1.2–7.0 kg/cm²(g) | 140°C | 5.1 kg/cm²(g) | 21.0 kg/cm²(g) / 250°C | [[equipment/E-2309]] |
| PT-23-1301 | Decomposer Drum | 0.3–1.5 kg/cm²(g) | 60°C | 0.7 kg/cm²(g) | 11.0 kg/cm²(g) / 250°C | [[equipment/D-2304]] |

> **PT-23-0401/0402 and PT-23-0801/0802 are absolute-pressure transmitters** (316SS wetted, impulse piping 316SS) — confirms deep-vacuum operation of [[equipment/V-2301]] and [[equipment/V-2302]] consistent with the 18.5–19.5 mmHgA range already on those equipment pages.

## Differential Pressure Instruments (6 tags)

| Tag | Service | Calibrated Range | Process Temp | Process Press | Design P/T | Equipment |
|-----|---------|-------------------|--------------|----------------|------------|-----------|
| PDT-23-0301 | Preflash Column Feed Filters dP | 0–3 kg/cm² | 82°C | 8.5 kg/cm²(g) | 11.5 kg/cm²(g) / 120°C | [[equipment/X-2302AB]] — fouling dP, feeds PDAH-0301 |
| PDXT-23-1701A | Decomposer Cooler dP | 0–2 kg/cm² | 79°C | 3.7 kg/cm²(g) | 16.5 kg/cm²(g) / 250°C | [[equipment/E-2307]] |
| PDXT-23-1701B | Decomposer Cooler dP | 0–2 kg/cm² | 79°C | 3.7 kg/cm²(g) | 16.5 kg/cm²(g) / 250°C | E-2307 |
| PDXT-23-1701C | Decomposer Cooler dP | 0–2 kg/cm² | 79°C | 3.7 kg/cm²(g) | 16.5 kg/cm²(g) / 250°C | E-2307 |
| PDT-23-1902 | Direct Neutralization Static Mixers dP | 0–1.5 kg/cm² | 43°C | 4.3 kg/cm²(g) | 21.0 kg/cm²(g) / 250°C | [[equipment/X-2310AB]] |
| PDT-23-1401 | Dehydrator dP | 0–1.4 kg/cm² | 135°C | 6.2 kg/cm²(g) | 21.0 kg/cm²(g) / 250°C | [[equipment/E-2308AB]] |

> **PDXT-23-1701A/B/C** confirms the 2oo3 voting differential-pressure-high-high SIS instrumentation already recorded on [[equipment/E-2307]] (PDXSHH-1701A/B/C) — same tag family, X-prefix denotes the SIS-qualified instrument.

## Local Pressure Gauges (42 tags)

Direct-reading, 4-1/2" dial, 316SS wetted, Ashcroft (or equal), per UOP Std Dwg 6-101. Six gauges (P-2305A–F discharge) carry diaphragm seals + excess-flow checks + pulsation dampeners (Alloy 20 acid metering pump service).

| Tag | Service | Scale Range (kg/cm²g) | Equipment |
|-----|---------|------------------------|-----------|
| PI-23-0302 / 0303 / 0304 | Preflash Column Feed Filter A/B Inlet, Filters Outlet | Local | [[equipment/X-2302AB]] |
| PI-23-0403 / 0404 | Preflash Column Top / Bottom | Local | [[equipment/V-2301]] |
| PI-23-0502 / 0503 / 0504 | S1.5 Steam to E-2303; Condensate Pump A/B | Local | [[equipment/E-2303]] / [[equipment/P-2308AB]] |
| PI-23-0601 | Concentration Cumene Quench Drum | Local | [[equipment/D-2301]] |
| PI-23-0702 / 0703 / 0704 / 0705 | S3 Steam to E-2304; Sample Receiver Outlet; Condensate Pump A/B | Local | [[equipment/E-2304]] / [[equipment/P-2309AB]] |
| PI-23-0803 / 0804 / 0805 / 0806 | Flash Column Top/Bottom; Reliable CW from E-2306 / E-2301 | Local | V-2302 / [[equipment/E-2306]] |
| PI-23-0807 / 0808 | Preflash & Flash Overhead Pump A/B | Local | [[equipment/P-2307AB]] |
| PI-23-0901 / 0902 | Flash Column Bottoms Pump A/B | Local | [[equipment/P-2301AB]] |
| PI-23-1004 / 1005 / 1006 / 1007 | Overhead Vapor to E-2310; Chilled Water from E-2310/X-2301; N₂ Purge to X-2301 | Local | [[equipment/E-2310]] / [[equipment/X-2301]] |
| PI-23-1102 | Cumene Flush Drum | Local | [[equipment/D-2302]] |
| PI-23-1203 / 1204 | Decomposer Feed Flush Drum; Process Water to Decomposer Feed | Local | [[equipment/D-2303]] |
| PI-23-1302 / 1303 | Decomposer Drum (×2) | Local | [[equipment/D-2304]] |
| PI-23-1304 / 1305 | Decomposer Product Pump A/B | Local | [[equipment/P-2303AB]] |
| PI-23-1402 / 1403 | Crude Product to E-2309; CW from E-2309 | Local | [[equipment/E-2309]] |
| PI-23-1404 / 1405 / 1406 / 1407 | S4 Steam to Dehydrators; Dehydrator A/B Outlet; Dehydrators Inlet | Local | [[equipment/E-2308AB]] |
| PI-23-1504 / 1505 / 1601 / 1602 / 1603 / 1604 | Decomposer Acid Injection Pump A/B/C/D/E/F Discharge | 0–6, w/ diaphragm seal, excess-flow check, pulsation dampener | [[equipment/P-2305ABCDEF]] — Alloy 20 wetted, design 4.921/250°C each |
| PI-23-1702 / 1703 | Decomposer Circulation Pump A/B | Local | [[equipment/P-2302]] |
| PI-23-1704 | Reliable CW from Decomposer Coolers | Local | [[equipment/E-2307]] |
| PI-23-1801 / 1802 / 1803 / 1804 | Circ. Decomposer Liquid to/from Calorimeter No.1 / No.2 | Local | [[equipment/X-2308]] |
| PI-23-1903 / 1904 | Direct Neutralization Static Mixers Inlet/Outlet | Local | [[equipment/X-2310AB]] |
| PI-23-1905 / 1906 | Neutralizing Agent Injection Pump A/B | Local | [[equipment/P-2306AB]] |
| PI-23-2001 / 2002 / 2003 | Acid Aromatics KO Drum; Sump Pump Outlet; N₂ Purge to Sump | Local | [[equipment/D-2306]] / [[equipment/P-2304A]] |
| PI-23-0813 / 0907 / 0706 | SN-2301 / SN-2303 / SN-2310 sample points | Local | [[instruments/sampling-cdn]] |
| PI-23-2101 / 2301 | AD Funnel / CHD Funnel | Local | Drain headers |

## Open Items

- None — all tags extracted cleanly. Local gauge calibrated ranges are governed by the UOP Pressure Gauge Range Selection Guideline table (Std Dwg 6-101, Sheet 40) rather than tag-by-tag specification; consult that table if a specific gauge dial range is needed.

## References

- [[sources/ps-pressure-level-temp-instrument-cdn-batch-2026-06-16]] — source summary
- [[instruments/cause-effect-cdn]] — SIS-side pressure tags (PXSHH series)
- [[instruments/pressure-relief-valves-cdn]] — relief device register (separate from this process-measurement register)
- [[equipment/V-2301]], [[equipment/V-2302]], [[equipment/D-2304]], [[equipment/E-2307]], [[equipment/E-2308AB]], [[equipment/X-2302AB]], [[equipment/X-2310AB]], [[equipment/P-2305ABCDEF]] — equipment-level cross-references
