---
name: CDN Flow Instrument Register
unit: CDN
tags: [instruments, flow, FE, FT, FXT, restriction-orifice, CDN]
sources: [14780-8120-PS-0031_FLOW INSTRUMENT (CDN)_Z1.pdf]
last_updated: 2026-06-16
---

# CDN Flow Instrument Register

**Source:** 14780-8120-PS-0031, Rev Z1 (AS-BUILT), Refinery Phenol Train II, POSCO Engineering / UOP licensor basis. 53 instrument data sheets across 6 instrument families.

This is the consolidated reference for CDN flow measurement devices — differential-pressure transmitters, primary flow elements (orifice plates), Coriolis mass flow meters, thermal mass flow instruments/switches, restriction orifices, and one rotameter. Individual equipment pages reference the relevant tags; this page holds the full sizing/range data.

---

## Differential-Pressure Flow Transmitters (27 tags)

All 316SS wetted, 4–20 mA output, Honeywell/Rosemount (or equal), per UOP Std Dwg 6-116.

| Tag | Service | Calibrated Range | Process Temp | Process Press (kg/cm²g) | Equipment |
|-----|---------|-------------------|--------------|---------------------------|-----------|
| FT-23-0401D | Oxidate Feed to Preflash Column | 0–125 mBar | 82°C | 7.0 | [[equipment/V-2301]] inlet |
| FXT-23-0401A/B/C | Oxidate Feed to Preflash Column | 0–500 mBar | 82°C | 7.0 | [[equipment/V-2301]] inlet (renamed from FT- per P&ID clarification) |
| FT-23-0403 | Preflash Column Reflux | 0–250 mBar | 39°C | 7.2 | [[equipment/V-2301]] |
| FT-23-0702 | Preflash Bottoms to Flash Vaporizer | 0–125 mBar | 70°C | -0.6 | V-2301→V-2302 train |
| FT-23-0801 | Flash Column Reflux | 0–250 mBar | 39°C | 7.2 | [[equipment/V-2302]] |
| FT-23-0803 | Preflash/Flash Net Overhead Liquid | 0–250 mBar | 39°C | 7.2 | V-2301/V-2302 overhead |
| FT-23-0802 | Preflash/Flash Total Overhead Liquid | 0–250 mBar | 39°C | 7.4 | V-2301/V-2302 overhead |
| FT-23-0901 | Flash Column Bottoms Pump Spillback | 0–250 mBar | 60°C | 3.5 | [[equipment/P-2301AB]] spillback |
| FT-23-1202 | Decomposer Feed Startup Bypass | 0–250 mBar | 60°C | 3.4 | Decomposer feed startup |
| FT-23-1205 / FXT-23-1204A/B/C | Flash Column Bottoms to Decomposer Drum | 0–125 mBar | 60°C | 3.4 | V-2302 → [[equipment/D-2304]] |
| FT-23-1301 | Decomposer Product to Dehydrators | 0–250 mBar | 83°C | 9.0–9.3 | D-2304 → [[equipment/E-2308AB]] |
| FT-23-1702 | Decomposer Circulation Loop Elbow | 0–293 mBar | 58°C | 2.7 | [[equipment/E-2307]] loop (elbow-tap meter) |
| FT-23-1801 / FXT-23-1803 | Decomposer Circ. Liquid to Calorimeter No.1 | 0–250 mBar | 79°C | 3.9 | [[equipment/X-2308]] Cal 1 |
| FT-23-1802 / FXT-23-1804 | Decomposer Circ. Liquid to Calorimeter No.2 | 0–250 mBar | 79°C | 3.9 | [[equipment/X-2308]] Cal 2 |
| FT-23-2001 | Acid Aromatics to Direct Neutralizer Static Mixer | 0–250 mBar | 38°C | 6.3 | [[equipment/X-2310AB]] |
| FT-23-0501 | S1.5 Steam to Preflash Steam Heater | 0–62.5 mBar | 135°C | 1.5 | [[equipment/E-2303]] |
| FT-23-0502 | Preflash Steam Heater Condensate Pumps Discharge | 0–250 mBar | 117°C | 2.8 | [[equipment/P-2308AB]] |
| FT-23-0701 | S3 Steam to Flash Vaporizer | 0–125 mBar | 148°C | 2.7 | [[equipment/E-2304]] |
| FT-23-0703 | Flash Vaporizer Condensate Pumps Discharge | 0–250 mBar | 135°C | 4.1 | [[equipment/P-2309AB]] |
| FT-23-1201 | Process Water to Decomposer Feed | 0–250 mBar | 50°C | 5.4 | Decomposer feed dilution water |
| FT-23-1401 | S4 Steam to Dehydrators | 0–125 mBar | 160°C | 4.0 | [[equipment/E-2308AB]] |
| FT-23-1701 | Reliable CW to Decomposer Cooler | 255 mBar (vendor TBD) | 37°C | 4.9 | [[equipment/E-2307]] — insertion Annubar type |

> Also bundled in the same DP-transmitter spec group but measuring **level, not flow**: LT-23-0501 (D-2308), LT-23-0701 (D-2309), LT-23-1101 (D-2301 area), LT-23-1201 (D-2303). Retained here only as a cross-reference note — see respective equipment pages for level data.

## Primary Flow Elements — Orifice Plates (19 tags)

304/316SS orifice plates, 300# RF flanged unless noted. Calculation basis: liquid 15°C, vapor 1.033 kg/cm²(a) @ 0°C.

| Tag | Service | Meter Max | Normal Flow | SG | Viscosity (cP) | Line/Conn | Bore | Equipment |
|-----|---------|-----------|-------------|----|-----------------|-----------|------|-----------|
| FE-23-0401 | Oxidate Feed to Preflash Column | 260 m³/h | 225.9 m³/h | 0.846 | 0.607 | 8" Cl.300 | Eccentric | [[equipment/V-2301]] |
| FE-23-0403 | Preflash Column Reflux | 30 m³/h | 22.4 m³/h | 0.848 | 0.622 | 3" Cl.300 | Concentric | V-2301 |
| FE-23-0501 | S1.5 Steam to Preflash Steam Heater | 15,000 kg/h | 11,388 kg/h | — | 0.014 (vapor) | 18" Cl.300 | Concentric | [[equipment/E-2303]] |
| FE-23-0502 | Preflash Condensate Pumps Discharge | 20 m³/h | 15.9 m³/h | 0.947 | 0.239 | 3" Cl.300 | Concentric | [[equipment/P-2308AB]] |
| FE-23-0701 | S3 Steam to Flash Vaporizer | 10,500 kg/h | 7,947 kg/h | — | 0.014 (vapor) | 12" Cl.300 | Concentric | [[equipment/E-2304]] |
| FE-23-0702 | Preflash Bottoms to Flash Vaporizer | 120 m³/h | 88.0 m³/h | 0.916 | 1.507 | 8" Cl.300 | Eccentric | V-2301→V-2302 |
| FE-23-0703 | Flash Vaporizer Condensate Pumps Discharge | 15 m³/h | 11.6 m³/h | 0.931 | 0.204 | 3" Cl.300 | Concentric | [[equipment/P-2309AB]] |
| FE-23-0801 | Flash Column Reflux | 28 m³/h | 21.4 m³/h | 0.848 | 0.622 | 3" Cl.300 | Concentric | V-2302 |
| FE-23-0803 | Preflash/Flash Net Overhead Liquid | 215 m³/h | 162.6 m³/h | 0.848 | 0.622 | 8" Cl.300 | Concentric | V-2301/V-2302 |
| FE-23-0802 | Preflash/Flash Total Overhead Liquid | 275 m³/h | 206.4 m³/h | 0.848 | 0.622 | 8" Cl.300 | Concentric | V-2301/V-2302 |
| FE-23-0901 | Flash Column Bottoms Pump Spillback | 40 m³/h | 31.5 m³/h | 0.972 | 3.432 | 4" Cl.300 | Concentric | [[equipment/P-2301AB]]; "Contractor to confirm normal spillback flowrate based on pump purchased" |
| FE-23-1202 | Decomposer Feed Startup Bypass | 80 m³/h | 59.9 m³/h | 0.972 | 3.432 | 6" Cl.300 | Eccentric | Decomposer feed bypass |
| FE-23-1205 | Flash Column Bottoms to Decomposer Drum | 80 m³/h | 59.9 m³/h | 0.972 | 3.432 | 6" Cl.300 | Eccentric | V-2302 → D-2304 |
| FE-23-1201 | Process Water to Decomposer Feed | 0.8 m³/h | 0.38 m³/h | 0.989 | 0.547 | 1" Cl.150 | Honed/concentric | Decomposer dilution water; Daniel (or equal) |
| FE-23-1301 | Decomposer Product to Dehydrators | 85 m³/h | 64.6 m³/h | 0.892 | 0.532 | 6" Cl.300 | Concentric | D-2304 → [[equipment/E-2308AB]]; inlet press 9.3 kg/cm²g per rev.1 |
| FE-23-1401 | S4 Steam to Dehydrators | 4,500 kg/h | 3,421 kg/h | — | 0.015 (vapor) | 8" Cl.300 | Concentric | E-2308AB |
| FE-23-1701 | Reliable CW to Decomposer Cooler | 4,500 m³/h (design) | 3,370 m³/h | 0.994 | 0.692 | 24" pipe | Annubar (insertion) | [[equipment/E-2307]]; Dieterich Standard (or equal), ±1% accuracy |
| FE-23-1801 / FE-23-1802 | Decomposer Circ. Liquid to Calorimeters | 0.18 m³/h | 0.144 m³/h | 0.898 | 0.571 | 3/4" Cl.300 honed | Concentric | [[equipment/X-2308]]; includes 316L Y-strainer; Daniel (or equal) |
| FE-23-2001 | Acid Aromatics to Direct Neutralizer Static Mixer | 30 m³/h | 21.6 m³/h | 0.939 | 1.160 | 3" Cl.300 | Concentric | [[equipment/X-2310AB]] |

## Coriolis Mass Flow Meters (7 tags)

Micro Motion / Endress+Hauser (or equal).

| Tag | Service | Normal Flow | Meter Max | Fluid | SG | Conn | Allow. ΔP | Equipment |
|-----|---------|-------------|-----------|-------|----|------|-----------|-----------|
| FT-23-1003 | Sealant Return from Vacuum Equipment | 1,791 kg/h | 2,300 kg/h | Water | 0.997 | 1/2" 150 RF | 0.49 kg/cm² | [[equipment/X-2301]] |
| FT-23-1002 | Process Water to Vacuum Equipment | 227 kg/h | 300 kg/h | Water | 0.969 | 1/2" 150 RF | 0.49 kg/cm² | X-2301 |
| FXT-23-1501 / FXT-23-1601 / FXT-23-1602 | Decomposer Acid Injection (×3 identical) | 0.82 kg/h | 2.0 kg/h | Conc. H₂SO₄ | 1.715 | 1/4" compression | 0.49 kg/cm² | [[equipment/P-2305ABCDEF]] |
| FT-23-1903 | Diamine Injection to Static Mixer | 3 kg/h | 6 kg/h | Diamine — Dytek(A) | 0.856 | 1/2" 150 RF | 0.49 kg/cm² | [[equipment/D-2312]] / [[equipment/P-2306AB]] |

> **Tag-naming note:** revision log (Rev O1, item 9) states FT-23-1501/1601/1602 were renamed to **FXT-**23-1501/1601/1602 per P&ID clarification — the index reflects this rename, but the data-sheet body text (page 40) was not updated to match. Use FXT- as the current tag.

## Thermal Mass Flow Instruments / Flow Switches (5 tags)

| Tag | Type | Service | Normal Flow | Fluid | Switch Point | Equipment |
|-----|------|---------|-------------|-------|---------------|-----------|
| FT-23-1001 | In-line thermal convective mass flow meter | N₂ to Vacuum Equipment | 29 Nm³/h (0–40 range) | Nitrogen | — | [[equipment/X-2301]]; Kurz Instruments (or equal) |
| FT-23-1004 | In-line thermal convective mass flow meter | Non-Condensable Vapor / Vacuum Equipment Vent | 73 Nm³/h (0–100 range) | N₂ + trace HC | — | X-2301; Kurz (or equal) |
| FXSL-23-1203 | Insertion thermal dispersion switch | Cumene Flush to Oxidate Long Circ. | 13,150 kg/h | Cumene | 2,630 kg/h | [[equipment/P-2307AB]] long circ.; renamed from FSL- |
| FXSL-23-1206 | Insertion thermal dispersion switch | Cumene Flush to Decomposer Feed | 3,150 kg/h | Cumene | 630 kg/h | Decomposer feed flush; renamed from FSL- |
| FSL-23-1202 | Insertion thermal dispersion switch | Process Water to Decomposer Feed | 375 kg/h | Water | 75 kg/h | Decomposer dilution water |

> ⚠️ **Internal document conflict:** the document index (p.4/5) lists this last service under tag **"FSL-23-1207"**, but the data-sheet body (p.45) reads **"FSL-23-1202"** for the identical service. One is a typo in the source document — flag for verification against the physical P&ID/field tag before using either in HAZOP or SIS work.

## Restriction Orifices (12 tags)

All sized per UOP hydraulic study; revised RO-23-0501/0701/0801/0901 per rev F2 hydraulic study, RO-23-2001 revised 6.72→3.3 m³/h per vendor info (rev F1).

| Tag | Service | Line Size | Fluid | Orifice (mm) | Normal Flow | Design Press/Temp | Equipment |
|-----|---------|-----------|-------|----------------|-------------|---------------------|-----------|
| RO-23-0501 | Preflash Steam Htr Condensate Pump Min-Flow | 1-1/2" | Condensate | 3 | 3.30 m³/h | 9.233 kg/cm²G / 195°C | [[equipment/P-2308AB]] |
| RO-23-0601 | Cumene to Cumene Quench Drum | 2" | Cumene | 6 | 1.46 m³/h | 10.59 kg/cm²G / 120°C | [[equipment/D-2301]] |
| RO-23-0701 | Flash Vaporizer Condensate Pump Min-Flow | 1-1/2" | Condensate | 2 | 1.75 m³/h | 9.233 kg/cm²G / 195°C | [[equipment/P-2309AB]] |
| RO-23-0801 | Preflash/Flash Overhead Pumps Startup | 6" | Cumene | 11 | 66.00 m³/h | 13.55 kg/cm²G(FV) / 120°C | [[equipment/P-2307AB]] |
| RO-23-0901 | Flash Column Bottoms Pump Spillback | 4" | CHP | 10 | 34.80 m³/h | 10 kg/cm²G(FV) / 250°C | [[equipment/P-2301AB]] |
| RO-23-1001 | N₂ to Vacuum Equipment | 1" | N₂ | 2 | 16.05 Nm³/h | 10 kg/cm²G / 120°C | [[equipment/X-2301]] |
| RO-23-1201 | CHP Line Cumene Flush | 3" | Cumene | 25 | 5.83 m³/h | 10 kg/cm²G / 120°C | Decomposer feed flush |
| RO-23-1202 | CHP Line Drain | 1-1/2" | CHP | 12 | (not legibly extracted) | 13.55 kg/cm²G / 250°C | Decomposer feed |
| RO-23-1203 | Process Water to Decomposer Drum | 1" | Process Water | 7 | 0.8 m³/h | 10.5 kg/cm²G / 120°C | [[equipment/D-2304]] |
| RO-23-2001 | Acid Aromatics Sump Pumps Min-Flow | 2" | HC | vendor | 3.30 m³/h | 13.06 kg/cm²G / 325°C | [[equipment/P-2304A]] |
| RO-23-2002 | N₂ to Acid Aromatics Sump | 1" | N₂ | 3 | 6.00 Nm³/h | 10 kg/cm²G / 120°C | [[equipment/D-2307]] |
| RO-23-2201 | N₂ to Acid Aromatics Sub Header Purge | 1" | N₂ | 3 | 6.00 Nm³/h | 10 kg/cm²G / 120°C | Acid aromatics relief sub-header |

## Rotameter (1 tag)

| Tag | Service | Line | Fluid | Flow | Design Press/Temp | Notes |
|-----|---------|------|-------|------|---------------------|-------|
| FIF-23-2201 | N₂ to Aromatics Relief Sub Header | 1" | Nitrogen | 6.00 Nm³/h | 10.5 kg/cm²G / 120°C | Allowable ΔP 0.14 kg/cm² at normal flow |

## Open Items

- **FSL-23-1207 vs FSL-23-1202** — internal document tag conflict, see Flow Switches section above.
- **RO-23-1202 normal flow value** — not cleanly extracted from source table formatting; design press/temp and orifice size (12mm) extracted cleanly. Recommend manual verification if exact m³/h figure is needed.

## References

- [[sources/ps-flow-instrument-cdn-batch-2026-06-16]] — source summary
- [[instruments/cause-effect-cdn]] — SIS-side flow tags (FXSLL series)
- [[equipment/V-2301]], [[equipment/V-2302]], [[equipment/D-2304]], [[equipment/X-2308]], [[equipment/X-2301]], [[equipment/X-2310AB]] — equipment-level cross-references
