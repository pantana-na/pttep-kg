---
name: Oxidation Section
code: OXI
tags: [unit, oxidation]
sources: ["14780-8120-PS-D2201_D-2201 PROCESS DATA SHEET_Z1.pdf", "14780-8120-PS-D2202_D-2202 PROCESS DATA SHEET_Z1.pdf", "14780-8120-PS-D2203_D-2203 PROCESS DATA SHEET_Z1.pdf", "14780-8120-PS-D2204_D-2204 PROCESS DATA SHEET_Z1.pdf", "14780-8120-PS-D2205_D-2205 PROCESS DATA SHEET_Z1.pdf", "14780-8120-PS-D2206_D-2206 PROCESS DATA SHEET_Z1.pdf", "14780-8120-PS-D2207_D-2207 PROCESS DATA SHEET_Z1.pdf", "14780-8120-PS-D2208_D-2208 PROCESS DATA SHEET_Z1.pdf", "14780-8120-PS-D2211_D-2211 PROCESS DATA SHEET_Z1.pdf", "14780-8120-PS-OX2201_OX-2201 PROCESS DATA SHEET_Z1.pdf", "14780-8120-PS-OX2202_OX-2202 PROCESS DATA SHEET_Z1.pdf", "14780-8120-PS-V2201_V-2201 PROCESS DATA SHEET_Z1.pdf"]
last_updated: 2026-06-14
---

# OXI — Oxidation Section

> ⚠️ CHP is a peroxide — thermal decomposition risk. See [[hazards/cumene-hydroperoxide]].

## Purpose

Oxidize Cumene (C₉H₁₂) with air to produce Cumene Hydroperoxide (CHP, C₉H₁₂O₂), which is the feedstock for the Cleavage section. This is a **liquid-phase, non-catalytic, free-radical chain oxidation** process.

## Process Description

Cumene is fed to a series of **oxidation reactors (oxidizers)** — typically 3 to 6 bubble columns in series. Air (or oxygen-enriched air) is sparged into the liquid Cumene. The reaction is a free-radical chain mechanism initiated thermally.

```
Initiation:   CHP → R• + •OH  (thermal)
Propagation:  R• + O₂ → ROO•  →  CHP
```

**Key operating variables:**
- Temperature: ~110–130°C (balance between rate and CHP stability)
- CHP concentration: typically 20–35 wt% in reactor; concentrated in an **evaporator** to 80–88 wt% for cleavage feed
- Air flow: controlled to maintain dissolved oxygen and reactor temperature
- pH control: dilute Na₂CO₃ solution injected to neutralize acidic by-products (prevents CHP decomposition)

The **oxidized product** is a mixture of: Cumene (unreacted), CHP, AMS, Acetophenone, DMBA, and trace heavies.

**CHP concentration step:** Cumene is evaporated from the oxidized mixture under vacuum to produce concentrated CHP feed (~80–88 wt%) for the Cleavage section. Recovered cumene is recycled.

**Tail gas treatment:** Exhaust air from oxidizers contains Cumene vapors — recovered by condensation/scrubbing before vent to atmosphere.

## Key Equipment

| Tag | Description | Ref |
|-----|-------------|-----|
| OX-2201 | Oxidizer No. 1 (API-620, 21.7 m dia.) | [[equipment/OX-2201]] |
| OX-2202 | Oxidizer No. 2 (API-620, 21.7 m dia.) | [[equipment/OX-2202]] |
| V-2201 | Feed Wash Column (horizontal, 7-tray L-L extractor, caustic) | [[equipment/V-2201]] |
| D-2201 | Combined Feed Surge Drum (4900 mm ID, 304L) | [[equipment/D-2201]] |
| D-2202 | CHP Process Water Break Tank | [[equipment/D-2202]] |
| D-2203 | Oxidizer Chilled Vent Gas Separator (cold, MDMT −10°C) | [[equipment/D-2203]] |
| D-2204A/B/C | Charcoal Adsorbers (3 vessels, severe cyclic service) | [[equipment/D-2204ABC]] |
| D-2205 | Decanter (horizontal, hydrocarbon/water separation) | [[equipment/D-2205]] |
| D-2206 | CHP Sump (underground, secondary containment) | [[equipment/D-2206]] |
| D-2207 | Compressed Air Scrubber (4-tray, CS valve trays) | [[equipment/D-2207]] |
| D-2208 | Oxidizer Vent Gas Separator — Warm | [[equipment/D-2208]] |
| D-2211 | Charcoal Adsorber Cooldown KO Drum (cold, MDMT −10°C) | [[equipment/D-2211]] |
| *(pending)* | Air Compressor | — |
| *(pending)* | Oxidizer Feed Pumps | — |
| *(pending)* | Oxidizer Circulation Pumps | — |

## Operating Parameters

| Parameter | Normal | Min | Max | Unit | Source |
|-----------|--------|-----|-----|------|--------|
| OX-2201 Operating Temperature | 86 | — | — | °C | PS-OX2201 |
| OX-2202 Operating Temperature | 82 | — | — | °C | PS-OX2202 |
| Oxidizer Design Temperature | 130 | — | — | °C | PS-OX2201/2202 |
| Oxidizer Operating Pressure | 0.187 | — | 0.45 (design) | kg/cm²g | PS-OX2201 |
| Oxidizer SG (aerated, OX-2201) | 0.80 | — | — | — | PS-OX2201 |
| Oxidizer SG (aerated, OX-2202) | 0.81 | — | — | — | PS-OX2202 |
| Oxidizer Normal Liquid Level | 10,300 | — | — | mm above bottom | PS-OX2201 |
| D-2207 Operating Pressure | 1.5 | — | 3.5 (design) | kg/cm²g | PS-D2207 |
| D-2201 Operating Pressure | 0.7 | — | 3.5 (design) | kg/cm²g | PS-D2201 |
| D-2201 Operating Temperature | 39 | — | — | °C | PS-D2201 |
| V-2201 Operating Pressure (top) | 1.8 | — | 15.0 (design) | kg/cm²g | PS-V2201 |
| CHP Conc. in Oxidizer | 25–30 | 20 | 35 | wt% | General design |
| CHP Conc. to Cleavage | 80–85 | 78 | 88 | wt% | General design |

## Control Philosophy

*(Pending P&ID ingestion)*

Key loops expected:
- Temperature control per oxidizer (cooling water or air flow trim)
- Air-to-cumene flow ratio
- pH control (Na₂CO₃ dosing)
- CHP concentration analyser → evaporator control

## Interlocks and Alarms

*(Pending Operating Manual ingestion)*

Critical expected:
- **High CHP concentration in oxidizer** → alarm + reduce temperature / increase air purge
- **High oxidizer temperature** → emergency cooling + reduce air
- **Loss of air flow** → stop cumene feed (prevents accumulation of uninhibited CHP)
- **High CHP in evaporator** → alarm (decomposition risk at high temperature)

## Safety Constraints

> ⚠️ This section has the **highest safety criticality** in the plant.

- CHP decomposes exothermically above ~100°C if not controlled — thermal runaway possible
- CHP at high concentration (>88 wt%) is shock-sensitive
- Keep CHP concentration within specified limits at ALL times
- Emergency water deluge on oxidizers must be available
- Nitrogen blanketing of CHP storage and transfer systems
- Refer to [[hazards/cumene-hydroperoxide]] for full hazard data

## Known Issues / Observations

*(To be populated from Operating Manual)*

Common operational challenges:
- Fouling of spargers/dip tubes over time — monitor air distribution
- Inhibitor carryover from feedstock can suppress oxidation rate
- CHP analyser calibration critical — unreliable analysers are a safety risk

## References

- [[sources/ps-static-equipment-batch-2026-06-14]] — 12 OXI Process Data Sheets, Rev Z1 (As-Built, May 2016)
- [[equipment/OX-2201]] — Oxidizer No. 1
- [[equipment/OX-2202]] — Oxidizer No. 2
- [[equipment/V-2201]] — Feed Wash Column
- [[equipment/D-2201]] — Combined Feed Surge Drum
- [[equipment/D-2202]] — CHP Process Water Break Tank
- [[equipment/D-2203]] — Chilled Vent Gas Separator
- [[equipment/D-2204ABC]] — Charcoal Adsorbers
- [[equipment/D-2205]] — Decanter
- [[equipment/D-2206]] — CHP Sump
- [[equipment/D-2207]] — Compressed Air Scrubber
- [[equipment/D-2208]] — Warm Vent Gas Separator
- [[equipment/D-2211]] — Charcoal Adsorber Cooldown KO Drum
- [[hazards/cumene-hydroperoxide]] — CHP hazard data
