---
name: Distillation / Purification Section
code: DIST
tags: [unit, distillation]
sources: []
last_updated: 2026-06-06
---

# DIST — Distillation / Purification Section

## Purpose

Separate and purify Phenol and Acetone from the cleavage product mixture. Recover and recycle Cumene and AMS. Produce on-specification products for sale.

## Process Description

The neutralized cleavage product from [[units/cleavage]] contains: Phenol, Acetone, Cumene, AMS, Acetophenone, DMBA, water, and heavy ends (tars).

The distillation train typically includes the following columns in sequence:

### Column 1 — Crude Acetone Column (Deacetoner)
- **Feed**: Cleavage product (aqueous phase + organic)
- **Overhead**: Crude acetone + water + light impurities
- **Bottoms**: Crude phenol + cumene + heavies
- Acetone is taken overhead because it is lighter than phenol and cumene

### Column 2 — Acetone Refining Column
- **Feed**: Crude acetone from Column 1
- **Overhead**: Refined Acetone (product)
- **Bottoms**: Heavy acetone impurities (Hydroxyacetone, Mesityl oxide) → to ETP or slops
- Overhead must meet refined acetone spec: ≥99.5 wt% acetone, low aldehyde content

### Column 3 — Cumene Recovery Column
- **Feed**: Bottoms from Column 1
- **Overhead**: Cumene + AMS (recycled to Oxidation or AMS recovery)
- **Bottoms**: Crude Phenol + Acetophenone + heavies
- AMS may be hydrogenated back to Cumene [[units/alkylation]] or extracted as a separate product

### Column 4 — Phenol Finishing Column
- **Feed**: Crude phenol from Column 3 bottoms
- **Overhead / Side draw**: Refined Phenol (product)
- **Bottoms**: Tar, Acetophenone, Cumylphenols → heavy ends
- Side draw location is critical — minimizes Acetophenone in product

### Heavy Ends Recovery (optional)
- Heavies column or vacuum still to recover residual Phenol and Acetophenone from tar
- Tar to fuel or incineration

## Key Equipment

| Tag | Description | Ref |
|-----|-------------|-----|
| *(pending P&ID)* | Crude Acetone Column | — |
| *(pending P&ID)* | Acetone Refining Column | — |
| *(pending P&ID)* | Cumene Recovery Column | — |
| *(pending P&ID)* | Phenol Finishing Column | — |
| *(pending P&ID)* | Column Condensers (multiple) | — |
| *(pending P&ID)* | Column Reboilers (multiple) | — |
| *(pending P&ID)* | Product Phenol Tank | — |
| *(pending P&ID)* | Product Acetone Tank | — |

## Operating Parameters

| Parameter | Normal | Min | Max | Unit | Source |
|-----------|--------|-----|-----|------|--------|
| Phenol Product Purity | ≥99.9 | 99.8 | — | wt% | General spec |
| Acetone Product Purity | ≥99.5 | 99.0 | — | wt% | General spec |
| Acetophenone in Phenol | *(pending)* | — | — | ppm | — |
| AMS in Cumene recycle | *(pending)* | — | — | wt% | — |
| Phenol Finishing Temp | *(pending)* | — | — | °C | — |

## Control Philosophy

*(Pending P&ID ingestion)*

Key loops expected:
- Each column: reflux ratio, reboiler duty, pressure control
- Phenol finishing column: side draw rate control linked to Acetophenone analyser
- Product quality analysers: online GC or NIR on phenol and acetone products

## Interlocks and Alarms

*(Pending Operating Manual ingestion)*

Critical expected:
- Low reflux on phenol column → product quality alarm
- High reboiler temperature → alarm (phenol degradation risk at very high temp)
- Product off-spec → divert to slops tank

## Safety Constraints

- **Phenol**: solid below 41°C — heat tracing required on product lines. Severe skin absorption hazard. Refer to [[hazards/phenol]]
- All columns handling phenol-containing streams: trace-heat all low points and drains
- Acetone: flammable, low flash point — explosion-proof electrical in area
- Heavy ends tars: phenolic content — manage as hazardous waste, route to [[units/etp]] or incineration

## Known Issues / Observations

*(To be populated from Operating Manual)*

Common operational challenges:
- Acetophenone accumulation: if not properly removed, contaminates phenol product
- Phenol solidification in cold weather — check all heat tracing before winter
- AMS polymerization in lines if temperature too low — monitor warm-up during startup

## References

*(No sources ingested yet)*
