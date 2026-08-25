---
name: Alkylation Section
code: ALKY
tags: [unit, alkylation]
sources: ["14780-8120-PS-D2121_D-2121 PROCESS DATA SHEET_Z1.pdf", "14780-8120-PS-D2122_D-2122 PROCESS DATA SHEET_Z1.pdf"]
last_updated: 2026-06-14
---

# ALKY — Alkylation Section

## Purpose

Convert Benzene (C₆H₆) and Propylene (C₃H₆) into Cumene (Isopropylbenzene, C₉H₁₂), which is the feedstock for the Oxidation section. Also converts Di-Isopropylbenzene (DIPB) by-product back to Cumene via transalkylation to maximize yield.

## Process Description

Benzene and propylene feeds are combined and passed over a solid acid catalyst (zeolite or phosphoric acid on kieselguhr in older plants) in an **alkylation reactor**. The reaction is exothermic and proceeds at elevated temperature and pressure (vapor or liquid phase depending on plant design).

The reactor effluent contains Cumene (primary), unreacted Benzene, and Di-Isopropylbenzene (DIPB) and Polyisopropylbenzene (PIPB) by-products.

A **benzene–propylene ratio** is maintained in excess (typically 6–8:1 mol) to suppress poly-alkylation.

The reactor effluent is fractionated in a **distillation train**:
- **Benzene column**: overhead recovers recycle benzene
- **Cumene column**: overhead produces on-spec Cumene product
- **DIPB column**: separates DIPB for transalkylation feed

A **transalkylation reactor** converts DIPB + Benzene → Cumene, improving overall yield.

## Key Equipment

| Tag | Description | Ref |
|-----|-------------|-----|
| *(pending P&ID)* | Alkylation Reactor | — |
| *(pending P&ID)* | Transalkylation Reactor | — |
| *(pending P&ID)* | Benzene Column | — |
| *(pending P&ID)* | Cumene Column | — |
| *(pending P&ID)* | DIPB (PIPB) Column | — |
| D-2121 | Cumene Column Reboiler Condensate Pot | [[equipment/D-2121]] |
| D-2122 | PIPB Column Reboiler Condensate Pot | [[equipment/D-2122]] |

## Operating Parameters

| Parameter | Normal | Min | Max | Unit | Source |
|-----------|--------|-----|-----|------|--------|
| Alkylation Rx Temp | *(pending)* | — | — | °C | — |
| Alkylation Rx Press | *(pending)* | — | — | barg | — |
| Benzene:Propylene Ratio | ~7 | 6 | 8 | mol/mol | General design |
| Cumene Purity (to OXI) | ≥99.5 | — | — | wt% | General spec |

## Control Philosophy

*(Pending P&ID ingestion — instrument tags TBD)*

Key loops expected:
- Propylene feed flow control
- Reactor temperature control (feed temperature or inter-stage quench)
- Column reflux ratios

## Interlocks and Alarms

*(Pending Operating Manual ingestion)*

Expected critical interlocks:
- High reactor temperature → propylene feed cutoff
- Low benzene:propylene ratio → alarm / feed adjustment

## Safety Constraints

- Benzene and Propylene are flammable — maintain positive pressure, leak detection
- Benzene is a known carcinogen — refer to [[hazards/benzene]] *(page pending)*
- High-pressure system — all relief devices must be in service during operation

## Known Issues / Observations

*(To be populated from Operating Manual)*

## References

- [[sources/ps-static-equipment-batch-2026-06-14]] — D-2121 and D-2122 Process Data Sheets, Rev Z1 (As-Built, May 2016)
- [[equipment/D-2121]] — Cumene Column Reboiler Condensate Pot
- [[equipment/D-2122]] — PIPB Column Reboiler Condensate Pot
