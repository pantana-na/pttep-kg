---
name: CDN Start-up Procedure (Initial and Normal)
type: Startup
unit: CDN
tags: [procedure, startup, CDN, concentration, decomposition, neutralization]
sources: [OM-Phenol Unit UOP-2015.pdf]
last_updated: 2026-06-16
---

# CDN Start-up Procedure (Initial and Normal)

> ⚠️ CHP is a peroxide — thermal decomposition risk. See [[hazards/cumene-hydroperoxide]].
> ⚠️ **The decomposer feed-in step (Part 3 below) is the single highest-risk operation in CDN start-up.** Injecting sulfuric acid into an acid-starved system with CHP concentration above 0.2 wt% risks runaway decomposition and possible explosion. Lab verification is mandatory before any acid rate increase — see Critical Safety Rule below.

**Authority:** UOP General Operating Manual, Rev 8, Section VI — Start-up (§VI.A "Initial Start-up" and §VI.B "Normal Start-up").

---

## Scope

Brings the CDN section (Concentration, Decomposition, Neutralization) from a pre-commissioned/de-inventoried state into production. Two cases are covered by the source and both are captured here:

- **Initial Start-up (§VI.A):** new plant, or a unit completely shut down and de-inventoried. Includes oxidizer seeding/passivation steps (Concentration/Decomposition/Neutralization portions only — see [[units/oxidation]] for full oxidizer seeding procedure, outside CDN scope).
- **Normal Start-up (§VI.B):** restart after a shutdown where most/all of the plant remained inventoried (e.g., following [[procedures/emergency-cdn]] or [[procedures/normal-shutdown-cdn]]). Which steps apply depends on what was de-inventoried.

Prerequisite: [[procedures/precommissioning-cdn]] must be complete. For oxidation section startup context (feeds CDN via terminal oxidizer effluent), see [[units/oxidation]].

---

## Prerequisites / Pre-checks

- [ ] All pre-commissioning procedures complete — trips and bypasses verified in normal operating position ([[procedures/precommissioning-cdn]])
- [ ] Cooling water in service to all CDN exchangers
- [ ] Cumene flush drums (D-2302, D-2303) filled
- [ ] Concentration vacuum system stable (re-verify per pre-commissioning if vacuum was lost)
- [ ] Neutralization section ready to receive crude product **before** decomposer feed-in is attempted
- [ ] Fractionation section ready to receive crude product (or sufficient feed-tank inventory/synthesized mixture available)
- [ ] Operations personnel briefed and aware of responsibilities — UOP GOM stresses safety training before commencing, given CHP heating hazard

---

## Part 1: Concentration Section Start-up

### Pre-commissioning status check
Verify all trips/bypasses normal; cooling water started to all exchangers in the section.

### Cumene quench system check (safety-critical — do this before introducing CHP)
1. Line up cumene quench to D-2301 (Cumene Quench Drum); fill on automatic level control. Verify the level control valve action is fast (near on/off) — it must refill the drum quickly in an emergency quench event.
2. Trip-simulate each quench valve individually: verify full open without binding, confirm quench flow by observing downstream vessel level rise, then close.
3. Commission the corresponding emergency quench circuitry after each valve check.
4. Note: all cumene dumped into the flash columns during a quench event recycles back to oxidizer #2 — this adds to its inventory and must be accounted for.

### Establish circulation (long circulation)
1. With no heat to the PFC steam heater (E-2303) or FC vaporizer (E-2304): press "Cumene Quench Reset", then "Feed to Preflash Column Start", then "Oxidate Feed Reset".
2. Begin circulating terminal oxidizer effluent → PFC (V-2301) → FC vaporizer (E-2304) → FC (V-2302) → FC bottoms.
3. Time-delayed bypasses (30 sec–2 min) suspend the low feed flow shutdown and flash column bottoms high-level shutdown during this establishment phase — be prepared, as these delays are short.
4. When a level appears in FC bottoms, start a flash column bottoms pump (P-2301A/B) and route to decomposition, joining the long circulation line back to the terminal oxidizer.
5. Use this cold/dilute circulation period to verify flow meters, pumps, and temperature indicators before introducing concentrated CHP.

### Heat-up
1. Once long circulation is established and the terminal oxidizer reaches the desired CHP concentration, set the decomposer feed bypass FIC to automatic/cascade at 70–100% of design.
2. Begin heating the PFC feed via steam reboiler and FC vaporizer; increase temperature slowly to ~10°C below design (columns run more efficiently at lower flash-zone pressure during start-up).
3. Establish design reflux/feed ratio once sufficient cumene is flashing overhead.
4. Target for PFC: 60 wt% CHP. Expect repeated feed filter (X-2302A/B) plugging during initial operation after oxidizer cleaning — this is normal during this phase.
5. Concentration section is ready to support decomposition start-up when FC bottoms reaches **80–84 wt% CHP** (lab-confirmed) with stable temperature, flow, and flash column top pressure control.

---

## Part 2: Decomposition Section — Pre-feed Preparation

### Pre-commissioning status check
Verify all trips/bypasses normal; cooling water in service. Fill flush drums with cumene.

### Decomposer inventory (Initial Start-up only)
- Inventory D-2304 with crude product (if available) **or an equal-molar (50 mol%/50 mol%) mixture of phenol and acetone**. Pure acetone, cumene, or phenol alone is not suitable.
- As level approaches 80%, bump-test circulation pump(s) (P-2302A/B), simulate low-cooling-flow trips and auto-start, then establish circulation through the calorimeters (X-2309A/B) and dehydrator (E-2308A/B) back to the decomposer.

### Decomposer heat-up and trip verification
1. Line up steam to the dehydrator and circulate to heat the decomposer.
2. Simulate temperature trips by allowing drum temperature to fluctuate to trip points; verify correct system response.
3. Simulate low cooling water flow and high temperature conditions; verify TIC-1302 controls drum temperature correctly when placed in auto.
4. After verification, cut dehydrator steam and cool the circulating material back to cooling water temperature.

### Final pre-feed commissioning checklist
- [ ] Sulfuric acid injection lines verified and ready (to calorimeters + decomposer circulation)
- [ ] Decomposition material composition (H₂O, CHP, H₂SO₄) verified by laboratory
- [ ] System heated to target
- [ ] Decomposer feed line flushed with cumene

---

## Part 3: Decomposer Feed-in — Start of Production

> This is the start of production for the **entire unit**. Crude product first forms here. UOP GOM: "safety is the key word."

### Step 1 — Sulfuric acid injection (build acid inventory before feed)
- Sulfuric acid enters via three routes: two to the calorimeters, one to decomposer circulation effluent.
- Verify flow at all three points, then start injection at the normal rate (≈40 wt ppm of anticipated feed rate).
- **Objective: raise decomposer liquid H₂SO₄ to 300 wt ppm (lab-verified)** before feed-in. Because injection pumps (P-2305A–F) are small, this may take several hours.
- ⚠️ **Do not overshoot.** Excess acid causes CHP to react too fast on feed-in, producing high temperatures at the circulation pump suction and risking pump cavitation → decomposer shutdown.
- Verify calorimeter flow controllers respond correctly; set calorimeter feed flow to design — the **36-second residence time** in calorimeter piping is sized to tight tolerances and must be maintained for correct calorimeter function.
- Lab must confirm before feed-in: **<2 wt% H₂O and ~300 wt ppm H₂SO₄** in circulating liquid.

### Step 2 — Final decomposer heat-up to feed-in temperature
1. Heat via dehydrator recirculation (decomposer → dehydrator → decomposer). Depress decomposer low-temperature bypass switch and dehydrator "Steam Enable" switch.
2. Set dehydrator feed flow to ~25% of scale; put decomposer TIC in auto at **70°C (160°F)**; target dehydrator outlet **135°C (275°F)**.
3. At 70°C, increase dehydrator flow to 70% of design, holding outlet at 135°C.
4. Verify decomposer cooler (E-2307A/B) can control temperature: temporarily lower TIC setpoint to 60°C and confirm quick response (overshoot is expected and acceptable at this low heat load — current load is far below what full CHP decomposition will produce). Return setpoint to 70°C.
5. **Verify good control here is required** — the low-temperature ESD trips at 55°C, and this is the most likely automatic safeguard to trip if the decomposition reaction is lost.
6. Re-confirm by lab: H₂SO₄ at least 300 wt ppm. Stop acid injection once confirmed.
7. ⚠️ **ENSURE NEUTRALIZATION IS READY FOR CRUDE PRODUCT BEFORE PROCEEDING.**
8. Confirm concentration section is stable. Unit is now ready for start of production.

### Step 3 — Flush the decomposer feed line
- Flush with cumene ("Cumene Flush to Decomposer Feed Line Start" button) to clear any acid or material that could promote premature cleavage — particularly important after a restart that has waited hours/days.
- Flush rate/time: flush the affected piping volume **twice in one minute**. Only the standing liquid volume down to the end of the feed distributor needs double-flushing (not the entire pipe run) for a quick restart; use the full piping volume for normal-shutdown restarts.

### Step 4 — Feed-in (commissioning the decomposition section)
Pre-feed-in state: FC bottoms (80–84 wt% CHP) bypassing to long circulation; both automatic block valves closed on the feed line; automatic drain valve open to sump.

1. Set the decomposer feed FIC to automatic/cascade with setpoint equal to the long-circulation FIC.
2. Press **"Decomposition Feed Start"** — opens the two automatic block valves (UXV-1201A/B/C), closes the flush and bleeder valves, opens the dehydrator effluent valve to neutralization, closes the decomposer recirculation valve.
3. A ramp function automatically closes the long-circulation FIC over <5 minutes while opening the decomposer feed valve to hold total FC bottoms flow constant. **CHP must be pushed forward quickly enough to sustain the reaction** — if not, decomposer temperature drops and the unit shuts down on TSLL (55°C).

**Verify before pressing the ramp start:**
| Parameter | Required value |
|-----------|----------------|
| Circulating decomposer inventory temperature | 70°C (160°F) |
| Circulating decomposer inventory H₂SO₄ | ~300 wt ppm |
| Circulating decomposer inventory H₂O | <2 wt% |
| Sulfuric acid injection rate (set, ready) | 40 wt ppm of incoming feed rate |
| Dehydrator outlet temperature | ~135°C (275°F) |
| Cooling water to dehydrator product cooler | Online, instrumentation ready |
| Neutralization section | Ready for crude product |
| FC bottoms CHP concentration | ≥80 wt% |

4. Begin the decomposer feed ramp immediately once verified. Expect decomposer temperature to increase (followed by cooling water flow increase as TIC holds 70°C) within seconds of feed arrival. If feed arrives slowly, a brief temperature *decrease* may appear first.
5. Put the decomposer level controller on cascade — sends crude product to the dehydrator and forward.

#### If there is no visible exothermic response to feed
⛔ **STOP FEED. Flush the feed line. Sample and lab-verify decomposer contents before any further action.**

Most likely causes, in order to check:
- Insufficient temperature
- Insufficient acid concentration
- Low CHP concentration in the feed
- High cumene concentration in decomposer circulating liquid

> ⛔ **CRITICAL SAFETY RULE:** IF THERE IS NO REACTION TO INJECTED CHP, DO NOT, UNDER ANY CIRCUMSTANCES, ARBITRARILY INCREASE SULFURIC ACID INJECTION WITHOUT FIRST SAMPLING THE CIRCULATING LIQUID AND CONFIRMING CHP CONCENTRATION IS BELOW 0.2 WT%. Injecting acid into an acid-starved system with CHP above this level risks **runaway decomposition and possible explosion of the decomposer contents.** Get lab verification of both CHP and acid concentration before proceeding.

### Step 5 — Ramp to full feed and normalize
1. Over <5 minutes, reduce long-circulation flow to zero; close the upstream UV block valve once the bypass FIC valve is fully closed.
2. Target conditions once full FC bottoms is feeding the decomposer:

| Parameter | Target |
|-----------|--------|
| Temperature | 70°C (160°F) |
| H₂SO₄ injection | 40 wt ppm of fresh feed |
| Water injection | Zero (for now) |
| Dehydrator outlet | 135°C (275°F) |
| Crude product temperature | 38°C (100°F) |
| Amine neutralization pH | 2.3–2.7 |

3. Concurrently: depress "Cumene Flush to Long Circulation Line Start" (HIC + flush valve open ~30 min, indicator light on); confirm automatic rerouting of PFC/FC net overhead cumene to the oxidation feed wash column; verify neutralization, concentration, and oxidation sections are unaffected by the production start.
4. Calorimeter ΔTs will read near-zero at this high-acid/high-temperature condition — **this is normal**, not a fault, as long as decomposer cooling water flow confirms CHP is decomposing.

### Step 6 — Optimize toward design operating point
As acid concentration declines toward the 40 wt ppm normal operating target (exponential decline — decomposer behaves as a CSTR), calorimeter ΔTs begin reading non-zero (1st stage = residual CHP signal; 2nd stage = DCP signal, which typically appears first since DCP is harder to decompose by acid than CHP).

1. Sample every 30 minutes (or per verified online analyzer, cross-checked periodically by lab) as acid approaches 40 wt ppm.
2. Once calorimeter ΔTs stabilize, step the decomposer temperature down from 70°C to the design 60°C, **1°C at a time with ≥15 minutes between moves**, monitoring 1st-stage calorimeter ΔT response. Confirm by lab sample at 60°C.
   - 60°C is the design optimum (best selectivity while close enough to the 55°C ESD trip to shut down safely if the reaction is lost). 70°C was used at feed-in only to guarantee complete reaction.
3. Start water injection (design ≈0.6 wt% of fresh feed; target 1–1.5 wt% at dehydrator outlet) carefully, in small increments, allowing equilibration between steps. **Water >2 wt% retards the decomposition reaction — a dangerous condition.**

#### Diagnosing insufficient acid during optimization
If acid injection is reduced too far during optimization, CHP can build up. Diagnostic signature: **decreasing/stable 1st-stage calorimeter ΔT + increasing 2nd-stage ΔT + decreasing dehydrator steam usage** — together these indicate insufficient CHP reaction and require immediate correction:
- Reverse any recent optimization step suspected of causing it.
- If acid is confirmed adequate (40 wt ppm), check and reduce water injection if excessive.
- If acid is genuinely low, **increase the injection rate by no more than 5% of current rate per step**, evaluating between each increment.
- ⛔ Never increase acid quickly when CHP build-up is suspected — repeats the Step 4 runaway-decomposition risk. UOP design relies on the 2nd-stage calorimeter high-ΔT shutdown and the decomposer 55°C TIC trip as the backstops here.

---

## Part 4: Neutralization Start-up

Simple relative to Decomposition — minimal control/instrumentation, diamine flow should already be lined up.

1. Establish ratio control of diamine injection to crude product flow, targeting **pH 2.3–2.7** (lab-measured).
2. Adjust the ratio downward frequently as decomposer H₂SO₄ falls toward its 40 wt ppm normal operating value (less acid carryover to neutralize over time).

---

## Critical Safety Rules — CDN Start-up

| Rule | Detail |
|------|--------|
| Never increase acid into a no-reaction system without lab verification | CHP must be confirmed <0.2 wt% first — risk of runaway decomposition / explosion otherwise |
| Build acid to 300 wt ppm before feed-in | Do not overshoot — risk of pump cavitation from too-fast reaction on feed-in |
| Neutralization must be ready before decomposer feed-in | Crude product has nowhere safe to go otherwise |
| Decomposer feed line must be flushed with cumene before feed-in | Removes acid/contaminants that could cause premature cleavage |
| Temperature step-down 60°C target: 1°C per move, ≥15 min apart | Avoid destabilizing the reaction during optimization |
| Acid rate increases during optimization: ≤5% per step | Same runaway-decomposition risk as initial feed-in |
| Water injection: increase carefully, monitor dehydrator outlet | >2 wt% water retards reaction — also dangerous |
| Zero calorimeter ΔT at feed-in is normal | Not a fault indicator at high-acid/high-temperature startup condition — do not misread as "no reaction" without checking cooling water response |

---

## Alarms to Watch

| Tag / System | Setpoint | Significance during start-up |
|--------------|----------|------------------------------|
| Decomposer TSLL (low temperature ESD) | 55°C | Primary automatic backstop if reaction is lost |
| 2nd-stage calorimeter high ΔT | Per [[instruments/cause-effect-cdn]] | Backstop against CHP/DCP build-up from acid starvation |
| FC bottoms / decomposer feed low-flow shutdown | Time-delayed during long-circulation establishment | Bypassed 30 sec–2 min during Part 1 circulation start — re-arms automatically |
| Flash column bottoms high level shutdown | — | Active during Part 1 — do not overload bottoms pump capacity |

---

## Post-completion Verification

- [ ] Decomposer at design 60°C, stable
- [ ] H₂SO₄ injection at 40 wt ppm of fresh feed, stable
- [ ] Water injection tuned (1–1.5 wt% at dehydrator outlet)
- [ ] Calorimeter ΔTs reading normally (non-zero, stable) and consistent with CHP/DCP feed composition
- [ ] Crude product to Neutralization on level control, pH 2.3–2.7
- [ ] FC bottoms CHP concentration confirmed ≥80 wt% feeding decomposer continuously (long circulation fully closed)
- [ ] Cumene flush to long-circulation line completed and valves returned to normal
- [ ] PFC/FC net overhead cumene rerouted to oxidation feed wash column
- [ ] Oxidation section parameters re-adjusted for steady-state CHP production matching decomposer feed demand

---

## References

- [[sources/om-phenol-uop-2015]] — UOP GOM §VI.A (Initial Start-up, steps 7–9), §VI.B (Normal Start-up, steps 2–4) (primary source)
- [[procedures/precommissioning-cdn]] — required prerequisite stage
- [[procedures/normal-operations-cdn]] — steady-state operations following start-up
- [[procedures/normal-shutdown-cdn]] / [[procedures/emergency-cdn]] — the shutdowns this procedure restarts from
- [[parameters/cdn-operating-windows]] — operating limits referenced throughout
- [[equipment/D-2304]] — Decomposer Drum
- [[equipment/E-2307]] — Decomposer Cooler
- [[equipment/X-2309]] — Calorimeters
- [[equipment/V-2301]] / [[equipment/V-2302]] — Preflash / Flash Columns
- [[equipment/D-2301]] — Cumene Quench Drum
- [[instruments/sis-cdn]] / [[instruments/cause-effect-cdn]]
- [[hazards/cumene-hydroperoxide]] / [[hazards/sulfuric-acid]]
