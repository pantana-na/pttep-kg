---
name: CDN Normal Shutdown Procedure
type: Shutdown
unit: CDN
tags: [procedure, shutdown, CDN, concentration, decomposition, neutralization]
sources: [OM-Phenol Unit UOP-2015.pdf]
last_updated: 2026-06-13
---

# CDN Normal Shutdown Procedure

> ⚠️ CHP is a peroxide — thermal decomposition risk. See [[hazards/cumene-hydroperoxide]].
> ⚠️ Never leave stagnant CHP (>20 wt%) in lines for any length of time — flush with cumene immediately.

**Authority:** UOP General Operating Manual, Rev 8, Section X — Normal Shutdown.

---

## Scope

Normal shutdown sequence for the CDN section (Concentration, Decomposition, Neutralization). These procedures are for planned shutdowns, not emergencies. For emergency shutdown, see [[procedures/emergency-cdn]].

**Shutdown sequence priority (CDN within whole-plant shutdown):**
1. Reduce production rates (Oxidation)
2. Shut down Decomposition (and de-inventory)
3. Begin Oxidation shutdown
4. Shut down Concentration (and de-inventory)
5. Complete Oxidation shutdown
6. Neutralization shutdown (concurrent with Decomposition)

---

## Prerequisites / Pre-checks

- [ ] Notify other operating units and utility stations of shutdown
- [ ] Prepare tankage for plant inventories
- [ ] Confirm cumene flush system is available and pressurized
- [ ] Confirm quench drum level is adequate (D-2301 / cumene quench drum)
- [ ] Alert fractionation section operators — crude product will stop when decomposition shuts down; fractionation must be in process of shutting down or have sufficient inventory in fractionation feed tank

---

## Part 1: Reduce Production Rates (Before Decomposition Shutdown)

1. Reduce plant production rate to 60% of normal level.
   - Make reduction slowly: approximately 10% per hour.
   - Allow overall operation to stabilize at each step.
2. Reduce oxidation air rates proportionally (targeting ~60% of normal).
   - Maintain spent air oxygen concentration at 7 mol% throughout reduction.
3. Adjust oxidizer temperatures to maintain design CHP concentration.
4. Monitor H₂SO₄ concentration in decomposition section — maintain at normal concentration by reducing acid injection rate accordingly.
5. Confirm acid and CHP concentrations by laboratory analysis.

---

## Part 2: Decomposition Shutdown (Section X.C)

Assumes decomposition section is at 60% feed rate at start of this procedure.

**Step 1 — Personnel and safety briefing:**
- Ensure all personnel are familiar with decomposition safety systems.
- Alert fractionation section: crude product will stop after this section is shut down. PLAN fractionation shutdown timeline accordingly.

**Step 2 — Trip the decomposer feed:**
- Reduce decomposer feed flow past the low flow trip setpoint.
- Automatic isolation valves should close, isolating feed to the decomposer.
- Verify isolation valves have closed.
- Verify solenoid valve opening to route dehydrator effluent back to the decomposer (internal circulation).
- Flush the decomposer feed line with cumene immediately:
  - Flush duration: minimum 2–4 minutes
  - Flush flow rate: sufficient to flush feed line volume at least 10 times
  - This removes residual concentrated CHP from feed piping.

**Step 3 — Do NOT decrease decomposer temperature yet.** Take a sample of the decomposer circulating liquid and send to laboratory. Restart H₂SO₄ injection at the same rate as when feed was stopped.

**Step 4 — Increase decomposer temperature to 70°C:**
- Increase temperature to 70°C (160°F) within 30 minutes.
- Keep H₂SO₄ injection running throughout.
- Purpose: react all residual CHP and DCP in the decomposer inventory. Calorimeter ΔTs will decrease toward zero as reaction proceeds.
- Monitor calorimeters — both 1st and 2nd stage ΔTs should go to zero.

**Step 5 — Verify sulfuric acid concentration:**
- When H₂SO₄ in circulating liquid reaches **300 wt ppm minimum** (laboratory confirmed): acid injection may be stopped.
- **Important:** Do NOT stop acid injection based solely on zero calorimeter ΔT. Only stop when laboratory confirms ≥300 wt ppm H₂SO₄ AND calorimeter ΔTs are zero.

**Step 6 — Confirm CHP is zero:**
- When calorimeter ΔTs have gone to zero: take circulating liquid sample for laboratory analysis.
- Must confirm: CHP = nil (zero), H₂SO₄ ≥ 300 wt ppm.
- If CHP not nil: continue circulating until CHP is gone.

**Step 7 — Extended circulation:**
- After laboratory confirms CHP = zero: circulate for a minimum of **4 additional hours at 70°C**.
- This ensures complete removal of any residual CHP.

**Step 8 — Cool down:**
- Open cooling water flow control valve to decomposer cooler (E-2307) to decrease decomposer liquid temperature to cooling water temperature.
- Stop steam to dehydrator and isolate steam line.
- Allow entire system to cool.

**Step 9 — Short vs. long shutdown:**
- Short shutdown (equipment not to be opened): keep circulation pumps on; typically shut off after system cools.
- Long shutdown / equipment entry: shut off circulation pumps after cooldown. Follow standard refinery vessel entry safety procedures.

---

## Part 3: Neutralization Shutdown (Section X.D)

Performed concurrently with or immediately after Decomposition shutdown.

**Step 1:** Isolate the diamine injection pump when the decomposer is shut down.

**Step 2:** Take the H₂SO₄ analyzer (AT-1701) out of service and block it in.

**Step 3 (if required for maintenance):** If decomposer or associated equipment must be drained, pump out any inventory in the acid aromatics sump to the fractionation feed tank via the ion exchange chambers.

---

## Part 4: Concentration Section Shutdown (Section X.B)

Assumes: concentration section is on long recycle (initiated by decomposition section shutdown via decomposer shutdown switch). Feed rate is at 60% of normal.

**Step 1 — Stop heat:**
- Slowly stop heat to the preflash column steam exchanger (E-2303) and flash column vaporizer (E-2304).
- Maintain preflash column feed rate above the automatic low-flow shutdown setpoint (avoid FSLLA trip).
- Do not overload the bottoms pumps — high flash column bottoms level will also cause automatic shutdown.
- Block in the steam control valve; allow feed material to cool off the exchanger to terminal oxidizer temperature.
- Do NOT stop feed to the concentration section yet.

**Step 2 — Allow overhead cooling:**
- Terminal oxidizer effluent at ~80°C may provide enough heat for net overhead. If not sufficient: stop and isolate the net overhead pump; allow receiver to fill and back up into flash column (dilutes flash column bottoms).

**Step 3 — Clear flash column receiver:**
- Pump contents of flash column receiver to the CFSD (Combined Feed Surge Drum).
- Shut down flash column net overhead pump.

**Step 4 — Stop feed:**
- Reduce feed to flash column to minimum flow.
- Then stop feed to the preflash column. This action introduces cooling water to the flash column vaporizer.

**Step 5 — Cumene quench flush:**
- Use emergency shutdown button to initiate cumene quench to PFC and FC.
- Stop cooling water flow to the feed vaporizer after sufficient flushing (at least 2× exchanger volume).
- Open external drain valves on preflash column tubs to increase draining rate.

**Step 6 — Clear decanter:**
- Draw down hydrocarbon level in the decanter; stop decanter pump.

**Step 7 — Isolate vacuum system:**
- Shut down the concentration vacuum system (X-2301).
- When no more net water from decanter: shut down decanter water pump.
- Attach nitrogen hose to concentration section; pressurize PFC, FC and related equipment to slight positive pressure (0.2 kg/cm²g, 3 psig) to prevent air ingress during shutdown.

**Step 8 — Pump out flash column bottoms:**
- Pump flash column bottoms to the oxidation section via the long recycle line after flushing with cumene from quench drum (flush several times).
- Shut down FC bottoms pump when no longer needed.
- Drain remainder of PFC and FC bottoms to CHP sump.
- Pump CHP sump contents to oxidation section.

> **At this point:** concentration section is available for maintenance preparation. Flush equipment to be opened with treated water before steam-out. Leave vessels open to atmosphere for 24–48 hours before entry.

---

## Critical Safety Rules During CDN Shutdown

| Rule | Detail |
|------|--------|
| Never leave stagnant high-CHP liquid | Flush any lines containing >20 wt% CHP with cumene immediately |
| Acid must reach 300 wt ppm before stopping | Even if calorimeter ΔTs are zero — verify by laboratory |
| 4-hour hold after CHP = zero | Do not skip this hold at 70°C |
| Decomposer feed line must be flushed | Minimum 10× volume with cumene immediately after isolation valves close |
| Do not stop circulation until CHP is confirmed nil | Circulation maintains cooling even in internal recycle mode |

---

## Post-Shutdown Verification

- [ ] Decomposer temperature at cooling water temperature
- [ ] Calorimeter 1 and 2 ΔTs = 0
- [ ] H₂SO₄ in decomposer circulation: ≥300 wt ppm (laboratory confirmed)
- [ ] CHP in decomposer circulation: nil (zero) (laboratory confirmed)
- [ ] Steam to dehydrator stopped and isolated
- [ ] Diamine injection stopped and isolated
- [ ] Concentration section flushed and pressurized with N₂
- [ ] Flash column bottoms pumped out to oxidation section
- [ ] CHP sump emptied to oxidation section

---

## References

- [[sources/om-phenol-uop-2015]] — UOP GOM §X.B–D (primary source)
- [[parameters/cdn-operating-windows]] — Operating limits including "ready for feed in" conditions
- [[procedures/emergency-cdn]] — Emergency shutdown reference
- [[units/cdn]]
- [[equipment/D-2304]] — Decomposer Drum
- [[equipment/E-2307]] — Decomposer Cooler
- [[equipment/V-2301]] — Preflash Column
- [[equipment/V-2302]] — Flash Column
- [[equipment/D-2301]] — Concentration Cumene Quench Drum
- [[hazards/cumene-hydroperoxide]]
