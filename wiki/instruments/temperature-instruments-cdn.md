---
name: CDN Temperature Instrument Register
unit: CDN
tags: [instruments, temperature, TE, TT, TXT, TDT, RTD, thermocouple, calorimeter, CDN]
sources: ["14780-8120-PS-0034_TEMPERATURE INSTRUMENT PROCESS DATA (CDN)_Z1.pdf"]
last_updated: 2026-06-16
---

# CDN Temperature Instrument Register

**Source:** 14780-8120-PS-0034, Rev Z1 (AS-BUILT, May 2016), Refinery Phenol Train II, POSCO Engineering / UOP licensor basis. 28-page process specification covering thermocouples/wells, RTD elements/wells, field temperature transmitters, one special in-tube RTD assembly, local thermometers/wells, and one field output indicator.

> ⚠️ Several of these instruments measure CHP-bearing streams (Decomposer circulation, calorimeters). See [[hazards/cumene-hydroperoxide]].

---

## Calorimeter Differential Temperature Instruments — Closes Numeric-Setpoint Gap (6 tags)

**This section closes the gap flagged in [[wiki/index]] Gaps list Item 7**: "Calorimeter ΔT alarm/trip setpoints (TDXSHH-1801/1803 etc.) remain qualitative SIS tags ... exact numeric setpoints still not sourced from a dedicated instrument data sheet." PS-0034 provides the **calibrated ranges** for the transmitters that generate those SIS signals (RTD type, per [[equipment/X-2308]]):

| Tag | Service | Type | Calibrated Range | Feeds |
|-----|---------|------|---------------------|-------|
| TDXT-23-1801 | Calorimeter No. 1 Total System Differential Temperature | RTD | 0–40°C | **TDXSHH-1801** (SIS HH, UC-2302 ESD) |
| TDT-23-1806 | Calorimeter No. 1 Differential Temperature | RTD | 0–25°C | TDT-1802 (reactivity signal on [[equipment/X-2308]]) |
| TDXT-23-1802 | Calorimeter No. 1 Inlet Line Differential Temperature | RTD | 0–20°C | **TDXAHH-1802** (DCS critical alarm) |
| TDXT-23-1803 | Calorimeter No. 2 Total System Differential Temperature | RTD | 0–40°C | **TDXSHH-1803** (SIS HH, UC-2302 ESD) |
| TDT-23-1809 | Calorimeter No. 2 Differential Temperature | RTD | 0–25°C | TDT-1804 (reactivity signal) |
| TDXT-23-1804 | Calorimeter No. 2 Inlet Line Differential Temperature | RTD | 0–20°C | **TDXAHH-1804** (DCS critical alarm) |

**Reconciling three distinct ΔT measurements per calorimeter:**
1. **Total System ΔT** (0–40°C span) — broadest measurement, feeds the SIS high-high trip that initiates UC-2302 ESD. The widest span reflects its role as the final safety barrier — must remain valid across the full credible excursion range.
2. **Calorimeter ΔT** (0–25°C span) — measured directly across the calorimeter vessel itself; this is the primary reactivity signal used by the acid-injection ratio controller (XC-1604).
3. **Inlet Line ΔT** (0–20°C span) — measured across the inlet piping only, feeding a DCS-level critical alarm (not a SIS trip) — likely an early-warning signal for upstream reactivity changes before the calorimeter total-system trip would actuate.

**Note on residual gap:** this data sheet confirms instrument *type and calibrated range*, not the *numeric alarm/trip setpoint value* within that range (e.g., "trips at X°C within the 0–40°C span"). The exact trip setpoints would need to come from the DCS/SIS configuration database or the cause-and-effect engineering package, not this process data sheet. Partial gap closure — flag remains open for the precise trip value.

## Thermocouples and Wells (33 tags)

UOP Std Dwg 6-105/6-107/6-108. Type E (Chromel-Constantan), grounded junction preferred, flanged thermowell, 316/304L SS construction per service.

| Tag | Service | Well/Flange | Length | Operating Temp/Press | Design Temp/Press | Equipment |
|-----|---------|-------------|--------|------------------------|----------------------|-----------|
| TE/TT-23-0601 | Concentration Cumene Quench Drum | 2", 300# | 600mm | 38°C / 0.06 kg/cm²(g) | 120°C / 3.5 kg/cm²(g) | [[equipment/D-2301]] |
| TE/TT-23-1704 | Reliable CW to Decomposer Cooler | 1-1/2", 150# | 300mm | 37.4°C / 4.71 kg/cm²(g) | 120°C / 13.0 kg/cm²(g) | [[equipment/E-2307]] |
| TE/TT-23-1703 | Reliable CW from Decomposer Cooler | 1-1/2", 150# | 300mm | 43°C / 2.5 kg/cm²(g) | 120°C / 13.0 kg/cm²(g) | E-2307 |
| TE/TT-23-0301 | Oxidate Feed to Preflash Column | 1-1/2", 150# | 300mm | 82°C / 5.5 kg/cm²(g) | 120°C / 11.5 kg/cm²(g), FV | [[equipment/V-2301]] inlet |
| TE/TT-23-0402 | Preflash Column Overhead Vapor | 1-1/2", 150# | 300mm | 52°C / -1.0 kg/cm²(g) | 250°C / 3.5 kg/cm²(g), FV | V-2301 |
| TE/TT-23-0403 | Preflash Column Bottoms | 1-1/2", 150# | 300mm | 70°C / -1.0 kg/cm²(g) | 250°C / 3.5 kg/cm²(g), FV | V-2301 |
| TE-23-0404 | Preflash Column Bottoms | 1-1/2", 150# | 300mm | 70°C / -1.0 kg/cm²(g) | 250°C / 3.5 kg/cm²(g), FV | V-2301 (304L SS) |
| TE/TT-23-0506 | Circulating Oxidate from Feed-Oxidate Exchangers | 1-1/2", 150# | 300mm | 75°C / 3.1 kg/cm²(g) | 120°C / 12.0 kg/cm²(g), FV | [[equipment/E-2302AB]] |
| TE/TT-23-0507 | Circulating Oxidate from Feed-Oxidate Exchangers | 1-1/2", 150# | 300mm | 75°C / 3.1 kg/cm²(g) | 120°C / 12.0 kg/cm²(g), FV | E-2302AB |
| TE-23-0501 | Preflash Column Feed-Oxidate Exchanger Tube Liquid | 2", 300# | 600mm | 58°C / -1.0 kg/cm²(g) | 250°C / 3.5 kg/cm²(g), FV | E-2302AB |
| TE-23-0502A | Preflash Column Steam Heater Tube Liquid | 2", 300# | 600mm | 70°C / -1.0 kg/cm²(g) | 250°C / 3.5 kg/cm²(g), FV | [[equipment/E-2303]] |
| TE-23-0502B | Preflash Column Steam Heater Tube Liquid | 2", 300# | 600mm | 70°C / -1.0 kg/cm²(g) | 250°C / 3.5 kg/cm²(g), FV | E-2303 |
| TE/TT-23-0505 | Preflash Column Steam Heater Tube Liquid | 2", 300# | 600mm | 70°C / -1.0 kg/cm²(g) | 250°C / 3.5 kg/cm²(g), FV | E-2303 |
| TE/TT-23-0803 | Flash Column Liquid Circulation to Vaporizer | 1-1/2", 150# | 250mm | 76°C / -0.92 kg/cm²(g) | 250°C / 3.5 kg/cm²(g), FV | [[equipment/E-2304]] |
| TE-23-0805A | Flash Column Bottom | 2", 300# | 600mm | 60°C / -0.341 kg/cm²(g) | 250°C / 3.5 kg/cm²(g), FV | [[equipment/V-2302]] |
| TE-23-0805B | Flash Column Bottom | 2", 300# | 600mm | 60°C / -0.341 kg/cm²(g) | 250°C / 3.5 kg/cm²(g), FV | V-2302 |
| TE/TT-23-0802 | Flash Column Overhead Vapor | 1-1/2", 150# | 300mm | 51°C / -1.0 kg/cm²(g) | 250°C / 3.5 kg/cm²(g), FV | V-2302 |
| TE/TT-24-0808 | Preflash & Flash Columns Overhead Pumps Suction | 1-1/2", 150# | 300mm | 38°C / -0.4321 kg/cm²(g) | 250°C / 4.167 kg/cm²(g), FV | [[equipment/P-2307AB]] |
| TE/TT-23-0809 | Oxidate Long Circulation to Oxidizer No.2 (OXI) | 1-1/2", 150# | 300mm | 38°C / 2.36 kg/cm²(g) | 250°C / 13.55 kg/cm²(g) | P-2307AB long circulation |
| TE-23-0901A | Flash Column Bottoms Pumps Suction | 1-1/2", 150# | 300mm | 60°C / -0.341 kg/cm²(g) | 195°C / 4.231 kg/cm²(g), FV | [[equipment/P-2301AB]] |
| TE-23-0901B | Flash Column Bottoms Pumps Suction | 1-1/2", 150# | 300mm | 60°C / -0.341 kg/cm²(g) | 195°C / 4.231 kg/cm²(g), FV | P-2301AB |
| TE/TT-23-1001 | Flash Column Overhead Chiller Vent to Vacuum Equipment | 1-1/2", 150# | 300mm | 5°C / -1.0 kg/cm²(g) | 120°C / 4.5 kg/cm²(g), FV | [[equipment/X-2301]] |
| TE-23-1301A | Decomposer Drum | 2", 300# | 600mm | 60°C / 0.7 kg/cm²(g) | 250°C / 11 kg/cm²(g), FV | [[equipment/D-2304]] |
| TE-23-1301B | Decomposer Drum | 2", 300# | 600mm | 60°C / 0.7 kg/cm²(g) | 250°C / 11 kg/cm²(g), FV | D-2304 |
| TE-23-1302 | Decomposer Drum | 2", 300# | 600mm | 60°C / 0.7 kg/cm²(g) | 250°C / 11 kg/cm²(g), FV | D-2304 |
| TE/TT-23-1303 | Decomposer Product Pumps Discharge | 1-1/2", 300# | 250mm | 60°C / 0.7 kg/cm²(g) | 250°C / 21, FV kg/cm²(g) | [[equipment/P-2303AB]] |
| TE-23-1402 | Decomposer Product from Dehydrators | 1-1/2", 300# | 250mm | 140°C / 4.9 kg/cm²(g) | 250°C / 21, FV kg/cm²(g) | [[equipment/E-2308AB]] |
| TE-23-1401 | Decomposer Product from Dehydrators | 1-1/2", 300# | 250mm | 140°C / 4.9 kg/cm²(g) | 250°C / 21, FV kg/cm²(g) | E-2308AB |
| TE/TT-23-1403 | Decomposer Product to Crude Product Cooler | 1-1/2", 300# | 250mm | 140°C / 4.9 kg/cm²(g) | 250°C / 21, FV kg/cm²(g) | [[equipment/E-2309]] |
| TE-23-1404 | Crude Product from Crude Product Cooler | 1-1/2", 300# | 250mm | 31°C / 4.4 kg/cm²(g) | 250°C / 21, FV kg/cm²(g) | E-2309 |
| TE/TT-23-1702 | Circulating Decomposer Liquid from Decomposer Cooler | 1-1/2", 300# | 300mm | 58°C / 4.64 kg/cm²(g) | 250°C / 16.5, FV kg/cm²(g) | [[equipment/E-2307]] — high velocity, additional well support |
| TE/TT-23-1701 | Circulating Decomposer Liquid to Decomposer Cooler | 1-1/2", 300# | 300mm | 72°C / 4.64 kg/cm²(g) | 250°C / 16.5, FV kg/cm²(g) | E-2307 — high velocity, additional well support |
| TE-23-1901 | Crude Product to Direct Neutralization Static Mixer | 1-1/2", 300# | 250mm | 31°C / 4.4 kg/cm²(g) | 250°C / 21, FV kg/cm²(g) | [[equipment/X-2310AB]] |
| TE-23-2001 | Acid Aromatics Sump | 2", 300# | by contractor (tip 150mm from sump bottom) | 38°C / 0.01 kg/cm²(g) | 325°C / 3.5, FV kg/cm²(g) | [[equipment/D-2307]] |

## Resistance Elements (RTD) and Wells (13 tags)

UOP Std Dwg 6-105/6-107/6-108. Platinum 100Ω @ 0°C, minimum 3-wire, 304L/316 SS sheath, magnesium oxide insulation.

| Tag | Service | Quantity/Notes | Operating Temp/Press | Design Temp/Press | Equipment |
|-----|---------|-----------------|------------------------|----------------------|-----------|
| TE-23-0702 | Flash Column Vaporizer Outlet | flanged, 300mm, 2" 300# | 97°C / -1.0 kg/cm²(g) | 250°C / 4.0, FV kg/cm²(g) | [[equipment/E-2304]] |
| TE-23-0703 | Flash Column Vaporizer Outlet | flanged, 300mm, 2" 300# | 97°C / -1.0 kg/cm²(g) | 250°C / 4.0, FV kg/cm²(g) | E-2304 |
| TE/TT-23-1807 | Circ. Decomposer Liquid from Calorimeter No.1 | single RTD | 79°C / 4.46 kg/cm²(g) | 250°C / 10.5, FV kg/cm²(g) | [[equipment/X-2308]] Cal 1 |
| TE-23-1806B/1801B | Circ. Decomposer Liquid from Calorimeter No.1 | duplex RTD, tee assembly per Sketch B | 79°C / 4.46 kg/cm²(g) | 250°C / 10.5, FV kg/cm²(g) | X-2308 Cal 1 |
| TE-23-1806A/1802B | Circ. Decomposer Liquid to Calorimeter No.1 Inlet | duplex RTD | 79°C / 4.46 kg/cm²(g) | 250°C / 10.5, FV kg/cm²(g) | X-2308 Cal 1 |
| TE/TT-23-1805 | Circ. Decomposer Liquid to Calorimeter No.1 Inlet | single RTD | 79°C / 4.46 kg/cm²(g) | 250°C / 10.5, FV kg/cm²(g) | X-2308 Cal 1 |
| TE-23-1802A/1801A | Circ. Decomposer Liquid to Cal No.1 Line Beginning Inlet | duplex RTD | 79°C / 4.46 kg/cm²(g) | 250°C / 16.5, FV kg/cm²(g) | X-2308 Cal 1 |
| TE-23-1804A/1803A | Circ. Decomposer Liquid to Cal No.2 Line Beginning Inlet | duplex RTD | 79°C / 4.46 kg/cm²(g) | 250°C / 16.5, FV kg/cm²(g) | X-2308 Cal 2 |
| TE/TT-23-1808 | Circ. Decomposer Liquid to Calorimeter No.2 Inlet | single RTD | 79°C / 4.46 kg/cm²(g) | 250°C / 10.5, FV kg/cm²(g) | X-2308 Cal 2 |
| TE-23-1804B/1809A | Circ. Decomposer Liquid to Calorimeter No.2 Inlet | duplex RTD | 79°C / 4.46 kg/cm²(g) | 250°C / 10.5, FV kg/cm²(g) | X-2308 Cal 2 |
| TE-23-1809B/1803B | Circ. Decomposer Liquid from Calorimeter No.2 | duplex RTD | 79°C / 4.46 kg/cm²(g) | 250°C / 10.5, FV kg/cm²(g) | X-2308 Cal 2 |
| TE/TT-23-1810 | Circ. Decomposer Liquid from Calorimeter No.2 | single RTD | 79°C / 4.46 kg/cm²(g) | 250°C / 10.5, FV kg/cm²(g) | X-2308 Cal 2 |

> Duplex RTD elements are installed via a 1/4" compression fitting centered in a 1/2" class 3000 socket-weld tee on 3/4" Schedule 80 pipe (Sketch B) — these are the calorimeter loop's redundant inlet/outlet temperature pairs feeding the differential-temperature transmitters in the section above.

## Field Temperature Transmitters (22 tags)

Rosemount / Foxboro (or equal). Type E unless noted RTD. All confirm corresponding TE/TT element tags above with calibrated ranges.

| Tag | Service | Type | Calibrated Range | Remarks |
|-----|---------|------|---------------------|---------|
| TXT-23-0404 | Preflash Column Bottoms | E | 0–200°C | [[equipment/V-2301]] |
| TXT-23-0501 | Preflash Column Feed-Oxidate Exchanger Tube Liquid | E | 0–200°C | [[equipment/E-2302AB]] |
| TXT-23-0502A/B | Preflash Column Steam Heater Tube Liquid | E | 0–200°C | [[equipment/E-2303]] |
| TXT-23-0701 | Flash Column Vaporizer Outlet Elbow | RTD | 0–200°C | [[equipment/E-2304]] |
| TXT-23-0702 | Flash Column Vaporizer Outlet | RTD | 0–200°C | E-2304 |
| TT-23-0703 | Flash Column Vaporizer Outlet | RTD | 60–120°C | E-2304 — narrow operating-range display |
| TXT-23-0805A/B | Flash Column Bottom | E | 0–200°C | [[equipment/V-2302]] |
| TXT-23-0901A/B | Flash Column Bottoms Pumps Suction | E | 0–200°C | [[equipment/P-2301AB]] |
| TXT-23-1301A/B | Decomposer Drum | E | 0–200°C | [[equipment/D-2304]] |
| TT-23-1302 | Decomposer Drum | E | 40–90°C | D-2304 — narrow operating-range display |
| TXT-23-1402 | Decomposer Product from Dehydrators | E | 0–200°C | [[equipment/E-2308AB]] |
| TT-23-1401 | Decomposer Product from Dehydrators | E | 0–200°C | E-2308AB |
| TT-23-1404 | Crude Product from Crude Product Cooler | E | 0–100°C | [[equipment/E-2309]]; TI-23-1404B output must be readable from valve |
| TDXT-23-1801 | Calorimeter No.1 Total System Differential Temperature | RTD | 0–40°C | See Calorimeter section above |
| TDT-23-1806 | Calorimeter No.1 Differential Temperature | RTD | 0–25°C | See Calorimeter section above |
| TDXT-23-1802 | Calorimeter No.1 Inlet Line Differential Temperature | RTD | 0–20°C | See Calorimeter section above |
| TDXT-23-1804 | Calorimeter No.2 Inlet Line Differential Temperature | RTD | 0–20°C | See Calorimeter section above |
| TDT-23-1809 | Calorimeter No.2 Differential Temperature | RTD | 0–25°C | See Calorimeter section above |
| TDXT-23-1803 | Calorimeter No.2 Total System Differential Temperature | RTD | 0–40°C | See Calorimeter section above |

## Special Temperature Detection Instrument (1 tag)

| Tag | Service | Description |
|-----|---------|-------------|
| TE-23-0701 | Flash Column Vaporizer Tube | Flanged thermowell assembly (2" Class 300 RF, 304L SS) with internal RTD positioned **24 inches (600mm) below the top of the tube bundle, inside an exchanger tube** of [[equipment/E-2304]]. Three radial guide wires (120° apart) center the thermowell in the tube. Process: 97°C / Full Vacuum; design 4.0 kg/cm²(g) @ 250°C. Thermowell pressure-tested to 170 psig (12.0 kg/cm²(g)) minimum. |

This is an unusual, vendor-engineered installation — direct tube-bundle internal temperature measurement rather than a standard nozzle-mounted thermowell, reflecting the importance of monitoring the vaporizer tube-side condition closely.

## Thermometers and Wells — Local (5 tags, 1 deleted)

| Tag | Service | Design Press/Temp | Equipment |
|-----|---------|----------------------|-----------|
| TI-23-0807 | Reliable CW from Flash Column Bottoms Cooler | 10.5 kg/cm²(g) / 120°C | [[equipment/E-2306]] |
| TI-23-0808 | HP Reliable CW to Preflash & Flash Columns Condenser | 10.5 kg/cm²(g) / 120°C | [[equipment/E-2301]] |
| TI-23-1002 | Chilled Water from Flash Column Overhead Vapor Chiller | 11.5 kg/cm²(g) / 120°C | [[equipment/E-2310]] |
| TI-23-1405 | Cooling Water from Crude Product Cooler | 7 kg/cm²(g) / 120°C | [[equipment/E-2309]] |
| ~~TI-23-0704~~ | SN-2310 | DELETED (per P&ID; was 4/FV kg/cm²(g) / 250°C) | sample point |

## Field Output Indicator (1 tag)

| Tag | Service | Scale |
|-----|---------|-------|
| TI-23-1404B | Crude Product from Crude Product Cooler | 0–100°C — electronic indicator from 4–20mA signal, must be readable from the associated valve |

## References

- [[sources/ps-pressure-level-temp-instrument-cdn-batch-2026-06-16]] — source summary
- [[equipment/X-2308]] — Calorimeters (differential temperature setpoint gap closure — primary cross-reference)
- [[instruments/cause-effect-cdn]] — SIS-side temperature tags (TXSHH, TDXSHH series)
- [[instruments/sis-cdn]] — UC-2301/2302 architecture
- [[equipment/D-2304]], [[equipment/V-2301]], [[equipment/V-2302]], [[equipment/E-2304]], [[equipment/E-2307]] — equipment-level cross-references
- [[wiki/index]] — Gaps list Item 7 (closure status)
