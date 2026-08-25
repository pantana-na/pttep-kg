---
name: CDN Pressure Relief Valves
unit: CDN
tags: [instruments, PSV, relief, safety, CDN]
sources: [14780-8120-PS-0018_Z1.pdf]
last_updated: 2026-06-16
---

# CDN Pressure Relief Valves (PSV) and Rupture Discs

**Source:** 14780-8120-PS-0018 (Pressure Relief Valve Process Datasheet, CDN Unit), Rev Z1 AS-BUILT, May 10, 2016 — UOP/POSCO Engineering.

> This closes the **PSV set pressure TBC item** flagged in [[hazop/study-info]] P&ID Readiness Checklist Item 7 — set pressures are now confirmed below.

---

## Summary Table — Spring-Loaded / Pilot-Operated PSVs

| Tag | Service | Type | Set Pressure (1st) | Design P/T | Relief Case | Orifice | Relief To |
|-----|---------|------|---------------------|-----------|-------------|---------|-----------|
| PSV-23-0401A/B/C/D | [[equipment/V-2301]] Preflash Column | Pilot-operated, modulating | 2.100 kg/cm²g | 3.5 kg/cm²g / 250°C | Self-Heating Reaction (DIERS, ω=2.222) | 754.06 cm² | Atmosphere, safe location |
| PSV-23-0501 | Preflash Steam Heater Condensate Drum [[equipment/D-2308]] | Spring, conventional | 7.000 kg/cm²g | 7.0 kg/cm²g / 195°C | External Fire | 0.71 cm² (Orifice D) | Atmosphere |
| PSV-23-0701 | Flash Col. Vaporizer Condensate Drum [[equipment/D-2309]] | Spring, conventional | 7.000 kg/cm²g | 7.0 kg/cm²g / 195°C | External Fire | 0.71 cm² (Orifice D) | Atmosphere |
| PSV-23-0801A/B/C/D/E | [[equipment/V-2302]] Flash Column | Pilot-operated, modulating | 2.100 kg/cm²g | 3.5 kg/cm²g / 250°C | Self-Heating Reaction (DIERS, ω=1.436) | 1005.42 cm² | Atmosphere, safe location |
| PSV-23-1403A/B/C | Dehydrator Reactor Loop X-2312 | Spring, balanced bellows | 20.50 kg/cm²g | 21.00 kg/cm²g / 250°C | Blocked-In Thermal Expansion | min (liquid trim) | Acid Aromatics Knockout Drum [[equipment/D-2306]] |
| PSV-23-1801A/B, 1802A/B | [[equipment/X-2309]] Calorimeters | Spring, balanced bellows | 9.50 kg/cm²g | 10.50 kg/cm²g / 250°C | Blocked-In Thermal Expansion / Blocked Outlet | min (liquid trim) | Acid Aromatics Knockout Drum |
| PSV-23-2001A/B | Acid Aromatic Sump [[equipment/D-2307]] | Spring, balanced bellows | 3.500 kg/cm²g | 3.5 kg/cm²g / 325°C | External Fire | 18.41 cm² (Orifice L) | Relief Header |

## Summary Table — Sized-Size / Block-Valve-Protection PSVs (Sheet 16–18)

| Tag | Service | Set Press. | Orifice (mm²) | Governing Case | Relief To |
|-----|---------|-----------|---------------|-----------------|-----------|
| PSV-23-0301A/B | [[equipment/X-2302AB]] Preflash Column Feed Filters | 11.0 kg/cm²g | 194.9 | External Fire | Decanter (ATM) |
| PSV-23-0802 | [[equipment/E-2306]] Flash Col. Bottoms Cooler (tube side) | 10.5 kg/cm²g | min | Thermal Expansion | ATM |
| PSV-23-0803 | [[equipment/E-2301]] Preflash/Flash Condenser (plate side) | 10.5 kg/cm²g | min | Thermal Expansion | ATM |
| PSV-23-1001 | [[equipment/E-2310]] Flash Col. Overhead Vapor Chiller (tube side) | 11.5 kg/cm²g | min | Thermal Expansion | ATM |
| PSV-23-1401A/B | [[equipment/E-2308AB]] Dehydrators (tube side) | 19.8 kg/cm²g | min | Thermal Expansion | HP Flare |
| PSV-23-1404 | [[equipment/E-2309]] Crude Product Cooler (shell side) | 16.5 kg/cm²g | 79.5 | External Fire | ATM |
| PSV-23-1406 | Dehydrator A shell side | 16.5 kg/cm²g | 70.1 | External Fire | ATM |
| PSV-23-1407 | Dehydrator B shell side | 16.5 kg/cm²g | 70.1 | External Fire | ATM |
| PSV-23-1701 | [[equipment/E-2307]] Decomposer Cooler (shell side) | 13.0 kg/cm²g | 283.0 | External Fire | ATM |
| PSV-23-1405A/B | E-2309 (tube side) | 20.5 kg/cm²g | 29.7 | External Fire | HP Flare |
| **PSV-23-1903A/B** | **[[equipment/D-2312]] Diamine Injection Tank** | 3.5 kg/cm²g | 338.5 | External Fire | HP Flare; **bellows type; key interlock added Rev F2** |

> ⚠️ PSV-23-1903A/B fluid is listed as **"DIAMINE"** vapor (MW 21.91 at relieving conditions — vapor mixture under fire case, not informative of base fluid identity). See [[hazards/diamine-tbc]] for the ongoing identity conflict (DIPA vs HMDA vs Dytek-A/MPMD).

## X-2311 Rupture Disc (Decomposer Drum Top)

| Parameter | Value |
|-----------|-------|
| Location | Top of [[equipment/D-2304]] Decomposer Drum |
| Quantity | 1 operating + 2 spares |
| Size | 24" |
| Type | B (BS&B nomenclature) |
| Normal Operating | 0.7 kg/cm²(g) at 60°C |
| Burst Pressure | MAWP of D-2304 at 60°C; not to exceed 11.0 kg/cm²(g) at 250°C; not less than 9.5 kg/cm²(g) at 225°C |
| Disc Material | 316 Stainless Steel |
| Liner (downstream/atmospheric) | Teflon or equal |
| Safety Head | FA-7R type, BS&B, 316SS inlet/outlet, jack screws required |
| Note 1 | 24" disc provided for pressure relief **in the unlikely event the safety instrumented system (UC-2302) fails** |
| Fluid handled | Nitrogen, acetone, phenol — discharged to atmosphere at a safe location |

> ⚠️ X-2311 is the last line of defense against decomposer runaway (CHP self-heating reaction) — backstop to UC-2302 SIS. See [[instruments/sis-cdn]] and [[hazards/cumene-hydroperoxide]].

## Key Revision History Notes

- PSV-23-1903A/B (Diamine Injection Tank) **added in Rev F2** — did not exist in earlier revisions; reflects late addition of D-2312 overpressure protection.
- Key interlock added for PSV-23-1405A/B in Rev F2.
- Burst pressure / back pressure values revised multiple times per FLARENET hydraulic calculation results (O2/A1/F1/F2 revisions) — current Z1 AS-BUILT values shown above are final.

## References
- [[hazop/study-info]] — P&ID Readiness Checklist Item 7 (PSV set pressures) — now CLOSED
- [[equipment/D-2304]] — Decomposer Drum, protected by X-2311 rupture disc
- [[equipment/D-2312]] — Diamine Injection Tank, protected by PSV-23-1903A/B
- [[hazards/diamine-tbc]] — fluid identity conflict
- [[hazards/cumene-hydroperoxide]] — CHP self-heating reaction basis for PSV-23-0401/0801 DIERS sizing
