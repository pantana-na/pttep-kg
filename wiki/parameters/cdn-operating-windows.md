---
name: CDN Section Operating Windows
unit: CDN
tags: [parameters, CDN, operating-window, licensor]
sources: [OM-Phenol Unit UOP-2015.pdf]
last_updated: 2026-06-13
---

# CDN Operating Windows — Licensor Design Basis

> ⚠️ CHP is a peroxide — thermal decomposition risk. See [[hazards/cumene-hydroperoxide]].

**Authority:** All limits on this page are from the UOP General Operating Manual (GOM), Rev 8. These are licensor-specified values and supersede other sources where conflicts exist.

---

## A. Concentration Section (Preflash Column & Flash Column)

> Equipment: [[equipment/V-2301]] (Flash Column) and Preflash Column (tag TBC)

| Parameter | Normal | Alarm | ESD / Max | Unit | Notes | Source |
|-----------|--------|-------|-----------|------|-------|--------|
| Flash zone pressure | 22–27 | — | — | mmHg | Vacuum system | GOM §III |
| Flash column temperature | — | 110 | 120 (ESD) | °C | High temp = CHP decomp risk | GOM §XI.J |
| CHP in flash column bottoms | 80–84 | — | — | wt% | Target for decomposer feed | GOM §III |
| Min CHP for decomposer feed | 70 | — | — | wt% | Below this: do not feed decomposer | GOM §XI.D |
| Preflash column max temperature | — | TBC | TBC | °C | [Gap: not stated in extracted sections] | — |

**Cumene quench triggers (automatic):**
- High flash column temperature → cumene quench to collector tray and/or bottoms (fail-open valves)
- High flash column vaporizer temperature → reliable CW quench (2 switches: high with time delay + higher without delay)
- Flash column bottoms and preflash column bottoms LSHH → trip decomposer + put on long recycle

---

## B. Decomposition Section

> Equipment: [[equipment/D-2304]] (Decomposer Drum), [[equipment/E-2307]] (Decomposer Cooler), [[equipment/X-2308]] (Calorimeters)

### Temperature

| Parameter | Normal | Startup/Shutdown | Low ESD | High ESD | Unit | Source |
|-----------|--------|-----------------|---------|---------|------|--------|
| Decomposer temperature | 60 | 70 | 57 (TSLL) | TSHH (TBC) | °C | GOM §III, §XI.J |
| Dehydrator effluent temperature | 125–145 | — | 120 (min) | — | °C | GOM §III |

**Notes:**
- Normal operating target is 60°C. Below 57°C: automatic ESD (inhibits decomposition reaction).
- 70°C is the "ready for feed in" temperature — used for startup conditions and after any shutdown.
- Dehydrator minimum 120°C ensures DCP → phenol + acetone conversion; below 120°C conversion incomplete.

### Sulfuric Acid (H₂SO₄) Catalyst

| Parameter | Normal | Ready-for-Feed-In | Danger Threshold | Unit | Source |
|-----------|--------|------------------|-----------------|------|--------|
| H₂SO₄ in circulating liquid (bulk) | 40–60 | 300 | <20 | wt ppm | GOM §III, §XI.D |
| H₂SO₄ at Calorimeter 2nd stage (local) | 4000–6000 | — | — | wt ppm | GOM §XI.D |

**Critical rules:**
- Below 20 wt ppm H₂SO₄: **EXTREMELY DANGEROUS** — re-introducing acid to a system with elevated CHP can cause uncontrolled decomposition and relief event.
- 300 wt ppm must be confirmed before feeding the decomposer after any shutdown ("ready for feed in" requirement).
- Complete loss of H₂SO₄ → automatic ESD (cannot monitor CHP without calorimeter acid).
- UOP recommendation: **never operate decomposer without at least one calorimeter online**.

### CHP and DCP Concentrations in Circulating Liquid

| Parameter | Normal | Instability Warning | Action | Unit | Source |
|-----------|--------|-------------------|--------|------|--------|
| CHP in circulating liquid | 1–1.5 | >2 | Investigate immediately | wt% | GOM §III |
| DCP (Dicumylperoxide) in crude product | 100–300 | — | — | wt ppm | GOM §III |

**Notes:**
- CHP >2 wt% in the decomposer circulation = reaction incomplete or acid insufficient.
- DCP 100–300 wt ppm in crude product indicates normal dehydrator conversion level.

### Water Content

| Parameter | Target | Max | Action above Max | Unit | Source |
|-----------|--------|-----|-----------------|------|--------|
| Water in circulating liquid | 1–2 | 2 | Reduce water injection; instability risk | wt% | GOM §III |
| Water injection at "ready for feed in" | 0 | — | No water injection before restart | kg/h | GOM §XI.D |

**Notes:**
- Water >2 wt% inhibits the decomposition reaction (acid is diluted).
- During startup, water injection is zero until steady-state decomposition is established.

### "Ready for Feed In" Conditions (After Any Shutdown)

All five conditions must be met before restarting decomposer feed:

| # | Condition | Target |
|---|-----------|--------|
| 1 | Decomposer Temperature | 70°C |
| 2 | H₂SO₄ Concentration (bulk) | 300 wt ppm |
| 3 | Circulating liquid water content | <2 wt% |
| 4 | Water injection rate | 0 kg/h |
| 5 | Decomposer feed line | Flushed with cumene |

[Source: OM-Phenol Unit UOP-2015.pdf, GOM §XI.D, UOP licensor]

---

## C. Calorimeter ΔT Interpretation

> Equipment: [[equipment/X-2308]] (Calorimeters)

Each calorimeter has two measurement points:
- **1st stage (inlet) ΔT**: measures CHP in the feed to the calorimeter (7.2°C per wt% CHP — conversion factor)
- **2nd stage (total) ΔT**: measures DCP + residual CHP (full conversion at high local acid)

| Scenario | 1st Stage ΔT | 2nd Stage ΔT | Meaning | Risk Level |
|----------|-------------|-------------|---------|-----------|
| Normal operation | Normal | Normal | Balanced decomposition | Low |
| Loss of 1st, loss of 2nd | Low | Low | No reaction — check acid level; may indicate startup or low CHP | Medium–High |
| Loss of 1st, 2nd OK | Low | Normal | Excess acid inhibiting 1st stage | Low |
| Loss of 1st, 2nd excessive | Low | High | Low bulk acid + residual CHP seen at 2nd stage | HIGH |
| 1st OK, 2nd lost | Normal | Low | Acid injection to calorimeter cut off | Medium |
| 1st OK, 2nd excessive | Normal | High | High DMPC in feed (elevated DCP) | Low |
| Excessive 1st, 2nd lost | High | Low | High CHP in loop + one calorimeter acid injection lost | HIGH |
| Excessive 1st, 2nd OK | High | Normal | CHP building up — very serious | HIGH |
| Excessive 1st, 2nd excessive | High | High | Incomplete decomposition, CHP accumulating — dangerous | CRITICAL |

**If H₂SO₄ < 20 wt ppm and adding acid to correct excessive ΔT:** Increase acid injection SLOWLY (5–10% increments). Rapid acid addition can trigger sudden, uncontrolled decomposition.

[Source: OM-Phenol Unit UOP-2015.pdf, GOM §XI.D.3–11, UOP licensor]

---

## D. Neutralization Section

> Equipment: Neutralization vessel (tag TBC), inline pH measurement

| Parameter | Target | Min | Max | Unit | Source |
|-----------|--------|-----|-----|------|--------|
| Crude product pH | 2.3–2.7 | — | — | pH units | GOM §III |

**Notes:**
- Below pH range: insufficient diamine neutralization → excess H₂SO₄ → yield loss + corrosion.
- Above pH range: excess diamine → potential side reactions.
- pH controller references inline field pH transmitter; requires periodic calibration check.
- If unable to neutralize: stop CDN feed, put oxidation section on long recycle.

---

## E. CHP in Recycle Cumene (Flash Column Overhead)

| Parameter | Target | Max | ESD | Unit | Source |
|-----------|--------|-----|-----|------|--------|
| CHP in recycle cumene (overhead) | <1 | <4 | — | wt% | GOM §III |

**Notes:**
- Recycle cumene overhead contains CHP returning to oxidation.
- >4 wt% CHP in recycle cumene is abnormal — indicates either poor concentration or high decomposer back-mixing.

---

## F. Concentration/Decomposition ESD Actions Summary (Table XI-1)

| Action | Trigger | Effect |
|--------|---------|--------|
| 1 | Low feed to PFC (FSLLA/B) | Stop PFC feed, flush upstream of PFC FCV, cumene quench to PFC heater and FC vaporizer |
| 2 | After time delay (following Action 1) | Close cumene flush upstream of PFC FCV |
| 3 | Immediately (high temp conditions) | Stop steam to PFC heater and FC vaporizer; vent steam/condensate; TRIP decomposition section |
| 4 | After time delay (high pressure) | Stop steam to PFC and FC vaporizer; vent; trip decomposition section |
| 5 | FC vaporizer high temp | Start cumene quench to flash column collector tray |
| 6 | After time delay | Stop cumene quench to flash column collector tray |
| 7 | FC bottoms high temp | Start cumene quench to flash column bottoms |
| 8 | Immediately (very high temp) | Start reliable CW quench to/from FC vaporizer; close condensate from FC vaporizer |
| 9 | After time delay (high temp) | Start reliable CW quench to/from FC vaporizer; close condensate |
| 10 | Oxidizer high temp | Stop reliable CW to concentration section |
| 11 | Concentration section ESD (HS) | Trip oxidation section |
| 12 | Decomposer trip conditions | Stop feed to decomposer; stop steam to dehydrator; divert dehydrator effluent back to decomposer; stop water to decomposer; divert recycle cumene and flash column to terminal oxidizer via long circulation; stop cumene flush to long circulation |
| 13 | After time delay (following Action 12) | Cumene flush to decomposer feed line; cumene flush of decomposer FCV between isolation valves |
| 14 | Low process water to decomposer (PSLL) | Close decomposer water injection isolation valve |
| 15 | Manual (HS) | Shut off steam to dehydrator even when rest of logic allows it |

[Source: OM-Phenol Unit UOP-2015.pdf, Table XI-1, UOP licensor]

---

## Data Gaps

| Gap | Notes |
|-----|-------|
| Preflash column operating pressure | Not stated in extracted sections — check process data sheets |
| Decomposer TSHH (high ESD) setpoint | Referenced in Table XI-1 but exact value not in GOM text |
| Calorimeter 1st/2nd stage ΔT alarm setpoints | Plant-specific; not in GOM — check instrument data sheets |
| DCP measurement method | Referenced indirectly via calorimeter 2nd stage; lab analysis required |
| Diamine injection rate normal | Not specified in extracted sections |

## References
- [[sources/om-phenol-uop-2015]] — UOP GOM (primary source)
- [[units/cdn]]
- [[equipment/D-2304]] — Decomposer Drum
- [[equipment/V-2301]] — Flash Column
- [[equipment/E-2307]] — Decomposer Cooler
- [[equipment/X-2308]] — Calorimeters
- [[hazards/cumene-hydroperoxide]]
