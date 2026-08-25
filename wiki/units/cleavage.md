---
name: Cleavage / Decomposition Section
code: CLP
tags: [unit, cleavage]
sources: []
last_updated: 2026-06-06
---

# CLP — Cleavage / Decomposition Section

> ⚠️ CHP is a peroxide — thermal decomposition risk. See [[hazards/cumene-hydroperoxide]].

## Purpose

Decompose Cumene Hydroperoxide (CHP) into Phenol and Acetone via acid-catalyzed cleavage. This is the most exothermic step in the process and requires precise temperature control to prevent runaway decomposition.

## Process Description

Concentrated CHP (~80–88 wt%) from the Oxidation section is fed to a **cleavage reactor**. The reaction is catalyzed by **dilute sulfuric acid (H₂SO₄)** or, in some designs, a solid acid resin.

```
C₆H₅C(CH₃)₂OOH  →  C₆H₅OH  +  CH₃COCH₃     ΔH ≈ −250 kJ/mol
        CHP              Phenol     Acetone
```

**The cleavage reaction is highly exothermic.** Temperature must be controlled within a tight window — typically **50–70°C**:
- Too cold: reaction too slow, CHP accumulates (inventory risk)
- Too hot: uncontrolled decomposition → runaway → explosion risk

The reactor is typically a **loop reactor (Venturi/jet mixer)** with a large recirculation flow to dilute CHP and control temperature. Fresh CHP feed is mixed into a large pool of already-reacted cleavage product, keeping CHP concentration low at any point.

**Cleavage product** composition: Phenol (~47 wt%), Acetone (~28 wt%), Cumene (~15 wt%), AMS (~5 wt%), Acetophenone, DMBA, H₂SO₄ (trace), water.

After cleavage, the product is:
1. **Neutralized** — H₂SO₄ removed with NaOH or Na₂CO₃
2. **Phase separated** — aqueous phase (acetone-rich) from organic phase (phenol/cumene-rich)
3. Sent to [[units/distillation]] for product purification

## Key Equipment

| Tag | Description | Ref |
|-----|-------------|-----|
| *(pending P&ID)* | Cleavage Reactor (loop type) | — |
| *(pending P&ID)* | Cleavage Cooler / Heat Exchanger | — |
| *(pending P&ID)* | Neutralization Vessel | — |
| *(pending P&ID)* | Phase Separator | — |
| *(pending P&ID)* | Cleavage Product Pump | — |

## Operating Parameters

| Parameter | Normal | Min | Max | Unit | Source |
|-----------|--------|-----|-----|------|--------|
| Cleavage Temperature | 55–65 | 50 | 70 | °C | General design |
| CHP Conc. in Reactor | ~1–3 | — | <5 | wt% | General design |
| H₂SO₄ Concentration | *(pending)* | — | — | wt% | — |
| Residence Time | *(pending)* | — | — | min | — |
| Neutralization pH | 6.5–7.5 | 6 | 8 | — | General design |

## Control Philosophy

*(Pending P&ID ingestion)*

Key loops expected:
- **CHP feed flow control** — primary rate handle
- **Reactor temperature control** — most critical loop; cooling water flow or recirculation rate
- **Recirculation pump** — must be running before CHP feed is opened
- **Acid catalyst injection rate** — controls reaction intensity
- **Neutralization pH control** — NaOH/Na₂CO₃ dosing

## Interlocks and Alarms

*(Pending Operating Manual ingestion)*

Critical expected:
- **High reactor temperature** → immediate CHP feed cutoff + increase cooling
- **Loss of recirculation pump** → immediate CHP feed cutoff (highest priority interlock)
- **High CHP in reactor** → alarm (accumulation indicates low catalyst activity or low temperature)
- **Loss of cooling water** → CHP feed cutoff

## Safety Constraints

> ⚠️ This section has **critical safety requirements**. Loss of cooling or recirculation with CHP present can lead to rapid thermal runaway.

- Cleavage reactor must NEVER receive CHP feed without recirculation pump running
- Temperature rise above 70°C is an emergency — follow [[procedures/emergency-shutdown-cleavage]] *(pending)*
- Minimize CHP inventory in the section at all times
- Emergency dump system to quench tank (if provided) must be tested per [[procedures/maintenance-interlock-test]] *(pending)*
- Personnel must wear phenol-resistant PPE when working in CLP area — refer to [[hazards/phenol]]

## Known Issues / Observations

*(To be populated from Operating Manual)*

Common operational challenges:
- Catalyst deactivation (for resin systems) — monitor by CHP conversion rate
- Neutralization salt (Na₂SO₄) buildup — check for plugging in downstream separators
- AMS hydrogenation (in some plants) — AMS is recycled to cumene via catalytic hydrogenation

## References

*(No sources ingested yet)*
