---
name: Decomposer Acid Injection Pumps
tag: P-2305A/B/C/D/E/F
type: Metering Pump
unit: CDN
tags: [equipment, pump, decomposition, CDN, acid, metering]
sources: [14780-8120-25-23-0015_Z1.pdf, 14780-8120-25-23-0016_Z1.pdf, 14780-8120-PS-P2305_Z1.pdf]
last_updated: 2026-06-16
---

# P-2305A/B/C/D/E/F — Decomposer Acid Injection Pumps

> ⚠️ CHP is a peroxide — thermal decomposition risk. See [[hazards/cumene-hydroperoxide]].
> ⚠️ **98% Sulfuric acid — severe contact hazard. Metering pumps must be confirmed running before acid injection begins.**

## Function

Six metering pumps (P-2305A through F) inject 98% H₂SO₄ catalyst from [[equipment/D-2310]] into the Decomposer loop. Sulfuric acid catalyses the decomposition of Cumene Hydroperoxide (CHP) to Phenol and Acetone in [[equipment/D-2304]]. The acid injection rate is **ratio-controlled** to the decomposer feed flow — maintaining the correct catalyst concentration is critical to both reaction efficiency and safety.

Acid from these pumps feeds the [[equipment/X-2308]] Calorimeters (Drawings 23-0018), not directly to the Decomposer. The calorimeter measures reactivity and provides the primary feedback for acid dose adjustment.

## Design and Operating Data

| Parameter | Value | Unit | Source |
|-----------|-------|------|--------|
| Service | Decomposer Acid Injection | — | Dwg 0015/0016 |
| Fluid | 98% Sulfuric Acid | — | |
| Specific Gravity @ Pumping Temp | 1.715 | — | Dwg 0015/0016 |
| Design Capacity (each pump) | 0.95 | liter/hr | Dwg 0015/0016 |
| Differential Pressure | 3.16 | kg/cm² | Dwg 0015/0016 |
| Motor Power | 0.2 | kW | Dwg 0015/0016 |
| Motor Control Type | **B** | — | Dwg 0015/0016 Note 4/5 |
| Insulation | NI | — | |
| Number | 6 (A/B on Dwg 0015; C/D/E/F on Dwg 0016) | — | |

**Note on pump capacity:** 0.95 liter/hr is an extremely small flow — these are precision metering (plunger) pumps. Total combined maximum injection rate (all 6) ≈ 5.7 liter/hr. The actual operating rate is much lower, set by the ratio controller.

## Pump Grouping

| Pumps | P&ID Drawing | Flow Meter | Notes |
|-------|-------------|-----------|-------|
| P-2305A, P-2305B | Drawing 0015 | FXT-1501 (Coriolis, shared) | Upstream of main ratio system; signal feeds to Drawing 0016 |
| P-2305C, P-2305D | Drawing 0016 | FXT-1601 (Coriolis, shared) | **Lead pumps** — ratio controller increases stroke first |
| P-2305E, P-2305F | Drawing 0016 | FXT-1602 (Coriolis, shared) | **Lag pumps** — ratio controller increases stroke last |

## Ratio Control System (Drawing 0016)

The acid injection rate is maintained at a fixed ratio to the Decomposer feed flow:

```
Decomposer Feed Flow (FT from OXI section)
    → Multiplier XY-1604A
        → Ratio Controller XC-1604 (Total Acid / Decomposer Feed Ratio)
            ↓
     Split Range Output:
     XY-16040 → P-2305C/D (LEAD — increases stroke first when ratio is LOW)
     XY-16049 → P-2305E/F (LAG — increases stroke last)
```

Split-range staging: At low acid demand, only C/D increase. At high demand, E/F also ramp up. This provides turndown control without running all 6 pumps at minimum stroke (which degrades metering accuracy).

P-2305A/B flow is measured separately by FXT-1501 on Drawing 0015 and their signal is fed into Drawing 0016 for the combined acid flow total.

## Associated Instruments

| Tag | Location | Description |
|-----|----------|-------------|
| FXT-1501 | Dwg 0015 | Coriolis flowmeter — P-2305A/B combined discharge |
| FR-1502 | Dwg 0015 | Flow recorder — acid flow A/B |
| FY-1502 | Dwg 0015 | Flow signal element |
| FAL-1501 | Dwg 0015 | Flow alarm low — P-2305A/B |
| FXT-1601 | Dwg 0016 | Coriolis flowmeter — P-2305C/D combined |
| FAL-1601 | Dwg 0016 | Flow alarm low — P-2305C/D |
| FXT-1602 | Dwg 0016 | Coriolis flowmeter — P-2305E/F combined |
| FAL-1602 | Dwg 0016 | Flow alarm low — P-2305E/F |
| FXSLL | Dwg 0016 | SIS low-low acid flow → UC-2302 ESD trigger |
| FXALL (CRIT) | Dwg 0016 | DCS low-low alarm (critical) |
| XC-2305 | Dwg 0015/0016 | Common pump alarm |
| XC-1604 | Dwg 0016 | Acid/Decomposer Feed Ratio Controller |
| XY-1604A | Dwg 0016 | Ratio multiplier |
| XY-16040 | Dwg 0016 | Split-range output to P-2305C/D (lead) |
| XY-16049 | Dwg 0016 | Split-range output to P-2305E/F (lag) |
| PSV-1501 | Dwg 0015 | Relief valve on P-2305A/B discharge |
| PSV-1601/1602 | Dwg 0016 | Relief valves on P-2305C/D and E/F discharge |

**Flowmeters:** Coriolis type (high accuracy for small flows). Each Coriolis meter has an upstream filter (Note 2 on Dwg 0015: "Filter to prevent particles > 0.5mm from plugging flowmeter"). Meters must be located in vertical orientation (Note: "Locate in Vertical").

## SIS Integration (UC-2302)

| Instrument | Action | Reference |
|-----------|--------|-----------|
| FXSLL (acid flow LL) | → UC-2302 ESD | Dwg 0016; C&E Drawing 0002 |
| FXALL-1803 (Cal 1 feed flow LL) | → UC-2302 ESD | C&E Drawing 0002 |
| FXALL-1804 (Cal 2 feed flow LL) | → UC-2302 ESD | C&E Drawing 0002 |

Loss of acid injection (FXSLL trigger) → UC-2302 trips → Decomposer ESD. Without acid, CHP decomposition stops → CHP accumulates at full concentration → severe runaway risk when acid is reintroduced.

**Note:** These pumps have **no auto-start** (Type B motor control — DCS low-flow start capability only; no permissive-based auto-start from standby). Operator attention is required if a pump trips.

## Process Data Sheet Confirmation (PS-P2305, As-Built Z1)

UOP Project Spec 963766-503 (API 675 controlled-volume proportioning pump data sheet) confirms the design data above and adds construction detail:

| Parameter | Value | Source |
|-----------|-------|--------|
| Standard | API 675 — Positive Displacement Pumps, Controlled Volume | PS-P2305 |
| Capacity, Rated | 0.95 l/h (max), 3.0+ turndown ratio | PS-P2305 — confirms wiki's 0.95 liter/hr |
| Differential Pressure | 3.16 kg/cm² max | PS-P2305 — confirms wiki's 3.16 kg/cm² |
| Specific Gravity | 1.715 | PS-P2305 — confirms |
| Viscosity | 14.286 cP | PS-P2305 |
| Liquid End Type | Hydraulic diaphragm, PTFE diaphragm | PS-P2305 |
| Liquid End / Valve / Seat / Guide / Body Material | **Alloy 20** | PS-P2305 — corrosion-resistant alloy for 98% H₂SO₄ service |
| Min Design Metal Temp | 15°C | PS-P2305 |
| Control | Automatic, remote, electronic signal (4–20 mA) | PS-P2305 |
| Relief Valve Setting | 4.921 kg/cm²g (external, vendor-furnished) | PS-P2305 |
| Material Revision | Materials revised per UOP-Refinery Operations Ltd.-SPOT RELEASE-T170 | PS-P2305 Record of Revision A2 |

**Alloy 20 construction** is notable — selected specifically for resistance to concentrated sulfuric acid, distinct from the 316 SS used on the centrifugal pumps elsewhere in CDN.

## Connections

- **Suction:** [[equipment/D-2310]] (Acid Injection Tank) — via 3/8" sulfuric acid lines
- **Discharge:** To [[equipment/X-2308]] Calorimeter No. 1 and No. 2 (via Drawing 23-0018):
  - ¾"-SA-23-016002-L1A1-NI → Calorimeter No. 1
  - ¾"-SA-23-016008-L1A1-NI → Calorimeter No. 2
- **Drain:** Pump drains to [[equipment/X-2320]] (Acid Neutralization System)

## References

- [[sources/pid-cdn]] — Drawings 14780-8120-25-23-0015 (A/B) and 0016 (C/D/E/F)
- [[equipment/D-2310]] — Acid Injection Tank (supply)
- [[equipment/X-2308]] — Calorimeters (acid discharge destination)
- [[equipment/D-2304]] — Decomposer Drum (ultimate acid consumer)
- [[instruments/sis-cdn]] — UC-2302 (FXSLL ESD trigger)
- [[instruments/cause-effect-cdn]] — C&E entries for acid flow low
- [[instruments/motor-control]] — Type B motor control
- [[units/cdn]]
- [[hazards/cumene-hydroperoxide]]
