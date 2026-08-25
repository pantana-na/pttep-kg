---
name: Static Equipment Process Data Sheets — Batch 2026-06-14
type: source-summary
sources: [14780-8120-PS-D-2121.pdf, 14780-8120-PS-D-2122.pdf, 14780-8120-PS-D-2201.pdf, 14780-8120-PS-D-2202.pdf, 14780-8120-PS-D-2203.pdf, 14780-8120-PS-D-2204ABC.pdf, 14780-8120-PS-D-2205.pdf, 14780-8120-PS-D-2206.pdf, 14780-8120-PS-D-2207.pdf, 14780-8120-PS-D-2208.pdf, 14780-8120-PS-D-2211.pdf, 14780-8120-PS-OX-2201.pdf, 14780-8120-PS-OX-2202.pdf, 14780-8120-PS-V-2201.pdf, 14780-8120-PS-V-2301.pdf]
tags: [source, data-sheet, equipment, OXI, ALKY, CDN, static-equipment]
last_updated: 2026-06-14
---

# Source Summary — Static Equipment Process Data Sheets (Batch 2026-06-14)

## Overview

Fifteen (15) UOP process data sheets for static equipment (pressure vessels, columns, tanks, and sumps) from the PTT Phenol Train II Project (PPCL), Map Ta Phut, Thailand. Prepared by POSCO Engineering & Construction under UOP licence. Document numbering prefix: 14780-8120-PS-*.

These data sheets are the formal engineering basis for vessel design parameters. They establish the Process Safety Information (PSI) required under equipment data sheets (Table A6.2-2, Item 4 of the PSI Readiness Checklist).

## Document Format

Each data sheet is a multi-page UOP-standard package:
- **Page 1 — Cover Sheet**: Item number, description, service, project spec reference, revision record
- **Page 2 — UOP General Notes**: Design code, construction materials philosophy, internals standard drawings, spare nozzle policy
- **Page 3 — Vessel Data Sheet**: Design data table, nozzle schedule, accessories checklist
- **Page 4 (where applicable) — Tray / Packing / Bed Data Sheets**: Tray or packing operating conditions, phase data, ΔP, geometry

## Project Specifications Referenced

| Spec Number | Scope |
|-------------|-------|
| UOP 963764 | Alkylation Section (ALKY) — benzene+propylene → cumene fractionation |
| UOP 963765 | Oxidation Section (OXI) — cumene → CHP oxidation |
| UOP 963766 | CDN Section — CHP concentration, decomposition, neutralisation |

## Equipment Covered (15 items)

### ALKY Section (Project Spec 963764)

| Tag | Description | Wiki Page |
|-----|-------------|-----------|
| D-2121 | Cumene Column Reboiler Condensate Pot | [[equipment/D-2121]] |
| D-2122 | PIPB Column Reboiler Condensate Pot | [[equipment/D-2122]] |

### OXI Section (Project Spec 963765)

| Tag | Description | Wiki Page |
|-----|-------------|-----------|
| D-2201 | Combined Feed Surge Drum | [[equipment/D-2201]] |
| D-2202 | CHP Process Water Break Tank | [[equipment/D-2202]] |
| D-2203 | Oxidizer Chilled Vent Gas Separator | [[equipment/D-2203]] |
| D-2204A/B/C | Charcoal Adsorbers (3 required) | [[equipment/D-2204ABC]] |
| D-2205 | Decanter | [[equipment/D-2205]] |
| D-2206 | CHP Sump | [[equipment/D-2206]] |
| D-2207 | Compressed Air Scrubber | [[equipment/D-2207]] |
| D-2208 | Oxidizer Vent Gas Separator | [[equipment/D-2208]] |
| D-2211 | Charcoal Adsorber Blowdown Knockout Drum | [[equipment/D-2211]] |
| OX-2201 | Oxidizer No.1 | [[equipment/OX-2201]] |
| OX-2202 | Oxidizer No.2 | [[equipment/OX-2202]] |
| V-2201 | Feed Wash Column | [[equipment/V-2201]] |

### CDN Section (Project Spec 963766)

| Tag | Description | Wiki Page |
|-----|-------------|-----------|
| V-2301 | Preflash Column | [[equipment/V-2301]] |

## Key Technical Findings

### Design Standards
- Pressure vessels: **ASME Section VIII Division 1** with ASME B16.5 Class 150 or Class 300 flanges
- Large-volume oxidizers: **API 620** (API Standard for low-pressure large-capacity storage tanks), per UOP requirement for the two oxidizer tanks (OX-2201/2202)
- Vessels with caustic service: SA 240 Type 304L (stainless steel); plain KCS vessels only where no caustic or CHP contact (D-2121, D-2122, D-2202, D-2207)

### Dominant Design Conditions
| Parameter | OXI Pressure Vessels | ALKY Vessels | Oxidizer Tanks (API 620) |
|-----------|---------------------|--------------|--------------------------|
| Design pressure (INT) | 3.5 kg/cm²g @ 120°C | 50 kg/cm²g @ 300°C | 0.45 kg/cm²g @ 130°C |
| External vacuum design | Full vacuum @ 250°C | Full vacuum @ 120°C | 0.01 kg/cm²g |
| Material dominant | SA 240 Type 304L | Killed Carbon Steel | A240 Type 304/304L |
| Corrosion allowance | 1.5 mm | 3.0 mm | 1.5 mm |

### Subzero MDMT Equipment
Two vessels are rated for subzero Minimum Design Metal Temperature:

| Tag | MDMT | Service |
|-----|------|---------|
| D-2203 | −10°C | Chilled vent gas separator (5°C operating) |
| D-2211 | −10°C | Charcoal adsorber blowdown KO drum (5°C operating) |

> These vessels require low-temperature impact testing of materials per ASME VIII and must use impact-tested materials.

### Severe Cyclic Service
D-2204A/B/C Charcoal Adsorbers are classified as **Severe Cyclic** — the vessel cycles between 16°C and 120°C every 6 hours during normal adsorption–regeneration cycles. This requires fatigue analysis per ASME VIII Div.1 design rules.

### Caustic Service Vessels
The following vessels are in caustic (NaOH) service and require appropriate material selection and inspection protocols:

| Tag | Description |
|-----|-------------|
| D-2201 | Combined Feed Surge Drum |
| V-2201 | Feed Wash Column |

### CHP Hazard Vessels
> ⚠️ CHP is a peroxide — thermal decomposition risk. See [[hazards/cumene-hydroperoxide]].

The following vessels contain CHP (Cumene Hydroperoxide / C₉H₁₂O₂) or CHP-containing streams:

| Tag | CHP Presence |
|-----|-------------|
| D-2202 | CHP Process Water Break Tank — direct CHP contact |
| D-2206 | CHP Sump — collects CHP-containing spills/drains |
| V-2301 | Preflash Column feed contains CHP from oxidation section |

### Underground / Secondary Containment
D-2206 (CHP Sump) is a special underground vessel. Note 2 of the data sheet specifies secondary containment must comply with **US EPA Title 40 CFR Part 280** (Underground Storage Tank Regulations). A lined vault or double-wall vessel is required.

### Elevation Constraints
Several OXI vessels have mandatory relative elevation requirements:

| Vessel | Elevation Requirement |
|--------|----------------------|
| D-2203 | ≥ 2500 mm above top of D-2205 (Decanter) |
| D-2208 | ≥ 600 mm above top of D-2205 (Decanter) |
| D-2211 | ≥ 2500 mm above top of D-2205 (Decanter) |

These elevation constraints are gravity-driven: condensate from the vent gas separators must drain by gravity to the decanter.

## PSI Significance

These 15 data sheets directly address **Table A6.2-2 PSI Readiness Checklist, Item 4 — Equipment Data Sheets** for the OXI, ALKY, and CDN (partial) sections. Prior to this ingest, equipment data sheets were identified as Gap Item #6 in the PSI readiness review. This batch partially closes that gap:

- **OXI section**: 12 static equipment items now documented (all major static equipment from this batch)
- **ALKY section**: 2 items (reboiler condensate pots for Cumene and PIPB columns)
- **CDN section**: 1 item (V-2301 Preflash Column — updated with formal design data)

Remaining PSI data sheet gaps: rotating equipment (pumps, compressors), ALKY reactors, remaining CDN vessels not in this batch.

## References

- [[sources/Table-A6.2-2-PSI-readiness-checklist]] — PSI gap tracking
- [[units/oxi]] — OXI section process description
- [[hazards/cumene-hydroperoxide]] — CHP hazard data
