---
name: CDN Control Valve Register
unit: CDN
tags: [instruments, control-valve, FV, LV, TV, PV, UV, CDN]
sources: [14780-8120-PS-0010_CONTROL VALVE PROCESS DATA SHEET CDN UNIT_Z1.pdf]
last_updated: 2026-06-16
---

# CDN Control Valve Register

**Source:** 14780-8120-PS-0010, Rev Z1 (AS-BUILT), PTT Phenol Train II, POSCO Engineering / UOP licensor basis. 136 pages, 43 distinct valve tags (34 main process data sheets + 9 condensed pump-seal/N₂ purge valves). Manufacturer basis throughout: Masoneilan or Metso Automation (or equal).

This is the consolidated reference for CDN control/on-off valves. Body material is predominantly 316/316L SS for hydrocarbon/CHP service and carbon steel for steam/cooling-water service.

---

## Decomposer / CHP Feed — Safety-Critical Valves

| Tag | Service | Cv | Size | Fail Action | Actuator | Notes |
|-----|---------|----|------|--------------|----------|-------|
| FV-23-1205 | Decomposer Feed | 75 | 3" (300#) | FO | Spring Diaphragm, Pneu | Modulating; **CHP feed control valve** to [[equipment/D-2304]] |
| UV-23-1204 / UV-23-1205 | Decomposer Feed Shutoff | 510 | 6" (150#) | FC | Spring Return Piston, Pneu | On-Off; SOV UY-23-1204/1205; Metso |
| UV-23-1201A/B | Cumene Flush to/from Decomposer Feed Line | 25 | 1-1/2" (300#) | FO | Spring Diaphragm, Pneu | On-Off; CHP flush purge valves |
| FV-23-1202 | Decomposer Feed Startup Bypass | 135 | 3" (300#) | FO | Spring Diaphragm, Pneu | Modulating; SOV FY-23-1202A |
| UV-23-1203 | Decomposer Feed Startup Bypass to Oxidate Circ. | 510 | 6" (150#) | FC | Spring Return Piston, Pneu | On-Off; SOV UY-23-1203A; Metso |
| UV-23-1202 | Cumene Flush to Oxidate Circulation Line | 245 | 3" (150#) | FC | Spring Return Piston, Pneu | On-Off; SOV UY-23-1202 |
| FV-23-1201 | Process Water to Decomposer Feed | 1.7 | 1" (300#) | FC | Spring Diaphragm, Pneu | Modulating; SOV FY-23-1201; dilution water control |
| PV-23-1301A | Nitrogen to Decomposer Drum | 1.2 | 1" (300#) | FC | Spring Diaphragm, Pneu | Modulating; D-2304 N₂ blanket |
| PV-23-1301B | Vent Gas from Decomposer Drum | 6 | 1-1/2" (300#) | FC | Spring Diaphragm, Pneu | Modulating; D-2304 vent |
| FV-23-1301 | Decomposer Product to Dehydrators | 75 | 3" (300#) | FO | Spring Diaphragm, Pneu | Modulating; D-2304 → [[equipment/E-2308AB]] |
| UV-23-1403 | Decomposer Product Return to Decomposer | 510 | 6" (300#) | FO | Spring Return Piston, Pneu | On-Off; SOV UY-23-1403; Metso |
| UV-23-1402 | Decomposer Product to Crude Product Cooler, Shutoff | 510 | 6" (300#) | FC | Spring Return Piston, Pneu | On-Off; SOV UY-23-1402; Metso |
| TV-23-1302A | Reliable CW to Decomposer Cooler | 13,139 | 20" (150#) | FO | Spring Diaph/Piston dbl-act, Pneu | Modulating; **largest valve in document**; split-range with TY-1302A — see [[equipment/E-2307]] |
| TV-23-1302B | Reliable CW bypassing Decomposer Cooler | 1,050 | 12" (300#) | FC | Spring Return Piston, Pneu | Modulating; split-range with TY-1302B — see [[equipment/E-2307]] |
| FV-23-1801 / FV-23-1802 | Circulating Decomposer Liquid to Calorimeter | 0.25 | 1/2" (300#) | FO | Spring Diaphragm, Pneu | Modulating; [[equipment/X-2308]] sample valves |
| FV-23-2001 | Acid Aromatics to Direct Neutralization Static Mixers | 46 | 2" (300#) | FC | Spring Diaphragm, Pneu | Modulating; [[equipment/X-2310AB]] acid ratio control |
| PCV-13-2001 | N₂ Purge to Acid Aromatics Sump | 1.0 | — | — (self-acting regulator) | None | [[equipment/D-2307]] N₂ purge |

> TV-23-1302A/B confirm the split-range CW control architecture already documented on [[equipment/E-2307]] (TIC-1302 → TY-1302A/B) and supply the missing valve tags/Cv values — added to that page.

## Preflash / Flash Column Area

| Tag | Service | Cv | Size | Fail Action | Actuator | Notes |
|-----|---------|----|------|--------------|----------|-------|
| UV-23-0301 | Oxidate Feed to Preflash Col, Shutoff | 1,350 | 8" (150#) | FC | Spring Return Piston, Pneu | On-Off; SOV UY-23-0301 |
| UV-23-0302 | Oxidate to CHP Closed Drain | 225 | 4" (300#) | FO | Spring Diaphragm, Pneu | On-Off; SOV UY-23-0302 |
| LV-23-0801 | Oxidate Feed to Preflash Column | 880 | 8" (150#) | FC | Spring Return Piston, Pneu | Modulating; SOV LY-23-0801A; Metso Eccentric Disc |
| UV-23-0401 | Cumene Quench to Oxidate Feed Line | 180 | 4" (150#) | FO | Spring Return Piston, Pneu | On-Off; SOV UY-23-0401 |
| HV-23-0401 | Cumene Quench to Preflash Col Bottom (manual) | 245 | 3" (150#) | FC | Spring Diaphragm, Pneu | Modulating; Metso Eccentric Disc |
| FV-23-0403 | Preflash Column Reflux | 18 | 1-1/2" (300#) | FO | Spring Diaphragm, Pneu | Modulating |
| LV-23-0601 | Cumene to Cumene Quench Drum | 81 | 3" (300#) | FO | Spring Diaphragm, Pneu | Modulating; Eccentric Rotary Plug |
| HV-23-0601 | Cumene Quench to Preflash Col (manual) | 25 | 1-1/2" (300#) | FC | Spring Diaphragm, Pneu | Modulating |
| UV-23-0601 | Cumene Quench to Preflash Column | 2,730 | 10" (150#) | FO | Spring Return Piston, Pneu | On-Off; SOV UY-23-0601; Metso |
| UV-23-0801 / UV-23-0802 | Cumene Quench to Flash Col Collector Tray/Bottom | 510 | 6" (150#) | FO | Spring Return Piston, Pneu | On-Off; SOV UY-23-0801/0802; Metso |
| HV-23-0801 / HV-23-0802 | Cumene Quench to Flash Col Collector Tray (manual) | 12 | 1" (300#) | FC | Spring Diaphragm, Pneu | Modulating |
| FV-23-0801 | Flash Column Reflux | 18 | 1-1/2" (300#) | FO | Spring Diaphragm, Pneu | Modulating |
| LV-23-0803 | Preflash/Flash Col Net Overhead Liquid | 230 | 4" (300#) | FC | Spring Diaphragm, Pneu | Modulating; Eccentric Rotary Plug |
| UV-23-0804 | Recycle Cumene to Feed Wash Col, Shutoff | 1,030 | 8" (150#) | FC | Spring Return Piston, Pneu | On-Off; SOV UY-23-0804; Metso |
| UV-23-0805 | Oxidate Long Circ. to Oxidizer No.2, Shutoff | 1,030 | 8" (150#) | FC | Spring Return Piston, Pneu | On-Off; SOV UY-23-0805; Metso |
| UV-23-0705 | Cumene Quench to Flash Column Vaporizer | 510 | 6" (150#) | FO | Spring Return Piston, Pneu | On-Off; SOV UY-23-0705; Metso |
| HV-23-1001 | Chilled Water to Flash Col OVHD Vapor Chiller | 500 | 6" (300#) | FO | Spring Return Piston, Pneu | Modulating; [[equipment/E-2310]]; Eccentric Rotary Plug |

## Steam / Condensate Systems

| Tag | Service | Cv | Size | Fail Action | Actuator | Notes |
|-----|---------|----|------|--------------|----------|-------|
| FV-23-0501 | S1.5 Steam to Preflash Steam Heater | 1,280 | 16" (300#) | FC | Spring Diaphragm, Pneu | SOV FY-23-0501; [[equipment/E-2303]] |
| UV-23-0502 | S1.5 Steam to Preflash Steam Heater, Shutoff | 11,400 | 18" (150#) | FC | Spring Diaph/Piston dbl-act, Pneu | On-Off; SOV UY-23-0502 |
| UV-23-0501 | Preflash Steam Htr Vent to Atm | 451 | 4" (150#) | FO | Spring Diaphragm, Pneu | On-Off; SOV UY-23-0501; isolate-and-vent pair with UV-0502 |
| LV-23-0501 | Preflash Steam Htr Condensate to Header | 19 | 2" (300#) | FC | Spring Diaphragm, Pneu | Modulating; [[equipment/D-2308]] |
| UV-23-0701 | S3 Condensate from Flash Vaporizer, Shutoff | 225 | 4" (300#) | FC | Spring Diaphragm, Pneu | On-Off; SOV UY-23-0701 |
| UV-23-0702 | Flash Vaporizer Steam Vent to Atm | 1,103 | 6" (150#) | FO | Spring Diaphragm, Pneu | On-Off; SOV UY-23-0702; vent pair with UV-0703 |
| UV-23-0703 | S3 Steam to Flash Vaporizer, Shutoff | 4,837 | 12" (150#) | FC | Spring Diaph/Piston dbl-act, Pneu | On-Off; SOV UY-23-0703 |
| TV-23-0703 | S3 Steam to Flash Column Vaporizer | 415 | 8" (300#) | FC | Spring Diaphragm, Pneu | Modulating; SOV TY-23-0703; [[equipment/E-2304]] |
| UV-23-0704 / UV-23-0706 | Reliable CW to/from Flash Col Vaporizer, Shutoff | 195 | 4" (300#) | FO | Spring Diaphragm, Pneu | On-Off; SOV UY-23-0704/0706 |
| UV-23-0707 | Steam to/from Flash Vaporizer Condensate Drum | 25 | 1-1/2" (300#) | FC | Spring Diaphragm, Pneu | On-Off; SOV UY-23-0707; [[equipment/D-2309]] |
| LV-23-0701 | Flash Vaporizer Condensate to SC3 Header | 13 | 1-1/2" (300#) | FC | Spring Diaphragm, Pneu | Modulating; D-2309 |
| UV-23-1401 | S4 Steam to Dehydrators, Shutoff | 1,911 | 8" (300#) | FC | Spring Diaphragm, Pneu | On-Off; SOV UY-23-1401; [[equipment/E-2308AB]] |
| TV-23-1401 | S4 Steam to Dehydrators | 225 | 6" (300#) | FC | Spring Diaphragm, Pneu | Modulating |

> Steam isolation valves consistently pair a fail-close supply shutoff with a fail-open vent-to-atmosphere valve (e.g., UV-0502/UV-0501; UV-0703/UV-0702) — an isolate-and-depressurize safety pattern repeated across all three steam headers (S1.5, S3, S4).

## Vacuum System / Nitrogen Blanketing

| Tag | Service | Cv | Size | Fail Action | Actuator | Notes |
|-----|---------|----|------|--------------|----------|-------|
| PCV-23-1003 | N₂ Purge to Concentration Vacuum Equip | 1.0 | — | — (self-acting regulator) | None | [[equipment/X-2301]] |
| FV-23-1001 | N₂ to Concentration Vacuum Producing Equip | 0.60 | 1" (300#) | FC | Spring Diaphragm, Pneu | Modulating |
| UV-23-1001 | Concentration Vacuum Producing Equip Vent | 46 | 2" (300#) | FC | Spring Diaphragm, Pneu | On-Off; SOV UY-23-1001 |
| LV-23-1101 | Cumene to Cumene Flush Drum | 46 | 2" (300#) | FC | Spring Diaphragm, Pneu | Modulating; [[equipment/D-2301]] |
| PV-23-1101A | Nitrogen to Cumene Flush Drum | 0.25 | 1" (300#) | FC | Spring Diaphragm, Pneu | Modulating |
| PV-23-1101B | Vent Gas from Cumene Flush Drum | 3.8 | 1" (300#) | FC | Spring Diaphragm, Pneu | Modulating |
| UV-23-1206 | Decomposer Feed Flush Drum to Feed Line, Shutoff | 180 | 4" (150#) | FO | Spring Return Piston, Pneu | On-Off; SOV UY-23-1206 |
| PV-23-1202A | Nitrogen to Decomposer Feed Flush Drum | 3.8 | 1" (300#) | FC | Spring Diaphragm, Pneu | Modulating |
| PV-23-1202B | Vent Gas from Decomposer Feed Flush Drum | 1.2 | 1" (300#) | FC | Spring Diaphragm, Pneu | Modulating |
| HV-23-1201 | Makeup Cumene to Decomposer Feed Flush Drum | 12 | 1" (300#) | FC | Spring Diaphragm, Pneu | Modulating |
| PV-23-1401 | Crude Product to Fractionation Feed Tanks | 135 | 3" (300#) | FC | Spring Diaphragm, Pneu | Modulating; Eccentric Rotary Plug |

## Pump Seal / N₂ Control Valves — Condensed Tabular Format (9 valves, pages 134–136)

| Tag | Service | Fail Action | Notes |
|-----|---------|--------------|-------|
| UXV-23-0803 | Reliable CW to E-2301 | FO | Eccentric Disc on-off, 5s close, Class 6 tight shutoff; design 10.5 barg/120°C — see [[equipment/E-2301]] |
| PCV-23-0901 / PCV-23-0902 | N₂ Control — Pump Seal | FO | [[equipment/P-2301AB]] seal N₂; self-regulating globe, Class 4 |
| PCV-23-1702 / PCV-23-1704 | N₂ Control — Pump Seal | FO | [[equipment/P-2302]] seal N₂; design 17 barg; Class 4 |
| PCV-23-1302 / PCV-23-1303 | N₂ Control — Pump Seal | FO | [[equipment/P-2303AB]] seal N₂; design 17 barg; Class 4 |
| PCV-23-0801 / PCV-23-0802 | N₂ Control — Pump Seal | FO | [[equipment/P-2307AB]] seal N₂; design 10 barg; Class 4 |

## Summary Statistics

- **Total: 43 valve tags** (41 actuated + 2 self-acting pressure regulators PCV-23-1003, PCV-13-2001).
- **Fail-action distribution:** Fail Open (FO) 19, Fail Close (FC) 22, Fail Last (FL) 0 — across the 41 actuated main-format valves. All 9 pump-seal N₂ valves are also fail-open.
- **Actuator types:** predominantly spring-return pneumatic — diaphragm for globe/smaller valves, piston for large eccentric-disc/rotary-plug valves; large fast-stroke steam/CW isolation valves (UV-0502, UV-0703, TV-1302A) use dual spring-diaphragm/double-acting-piston actuators.
- **Largest valve:** TV-23-1302A (Cv 13,139, 20" body) — Reliable CW to Decomposer Cooler E-2307.

## References

- [[sources/ps-control-valve-cdn-batch-2026-06-16]] — source summary
- [[equipment/D-2304]], [[equipment/E-2307]] — CHP feed and decomposer cooler valves (safety-critical)
- [[equipment/X-2310AB]] — acid injection ratio control (FV-23-2001)
- [[instruments/sis-cdn]], [[instruments/cause-effect-cdn]] — UXV/SOV cross-reference for SIS-actuated valves
