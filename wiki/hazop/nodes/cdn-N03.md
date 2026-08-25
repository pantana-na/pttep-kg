---
name: Flash Column Vaporizer & Concentrated-CHP Bottoms Pump-Out
node_id: CDN-N03
markup_label: "Node 23-03 (engineer P&ID markup, green highlight)"
unit: CDN
pid_sheet: "14780-8120-25-23-0007, -0007A (vaporizer + condensate); -0008 (Flash Column bottoms draw); -0009 (bottoms pumps); -0012, -0012A (CHP transfer to Decomposer feed)"
pid_marked_up: "Node 23-03.pdf (user-supplied markup — recommend filing in raw/pid/)"
inlet_boundary: "SC3 steam supply to E-2304 shell (via UXV-0701-0706); concentrated CHP from V-2302 bottoms into E-2304 tube circuit and into P-2301A/B suction (downstream of E-2306 bottoms cooler / Node 23-04); cumene flush/seal supply (22-0027) to P-2301"
outlet_boundary: "Concentrated CHP (~80-85 wt%) to Decomposer feed system, line 6\"-CHP-23-009002/003 (hands over to Decomposer Feed node at D-2303 area, Dwg 0012A); SC3 condensate from P-2309A/B to condensate return (68-0056); cumene vapor-liquid return from E-2304 to V-2302 (handover to column body Node 23-05)"
tags: [hazop, node, CDN, preliminary]
last_updated: 2026-06-18
status: PRELIMINARY DRAFT 2026-06-18 — desktop first-pass; boundaries (esp. handoffs to Nodes 23-04/23-05 and the Decomposer-feed node) and worksheet require engineer/team confirmation
---

# HAZOP Node CDN-N03 — Flash Column Vaporizer & Concentrated-CHP Bottoms Pump-Out

> ⚠️ **PRELIMINARY DRAFT (2026-06-18).** Generated from the user-supplied "Node 23-03" P&ID markup (green highlight) + wiki PSI. This is a desktop first-pass to seed the facilitated workshop — **not** a completed, team-validated worksheet. Causes, consequences, safeguard adequacy, and risk rankings require confirmation by the HAZOP team per [[wiki/hazop/methodology]].

> ⚠️ **CHP is a peroxide — thermal decomposition risk. This node carries the HIGHEST CHP concentration in the entire Concentration sub-section (~80-85 wt%, V-2302 bottoms).** Per [[wiki/hazards/cumene-hydroperoxide]], concentrated CHP (>50 wt%) at elevated temperature can **deflagrate or detonate** under runaway. Decomposition onset ≈ **80 °C**; SADT 60-80 °C. Over-temperature and loss-of-removal of concentrated CHP are the dominant hazards of this node.

> 🟢 **Markup label:** the engineer's drawing labels this **"Node 23-03"** (green); filed here as **CDN-N03** per the skill's `<unit>-N<nn>` schema. Deviation references use `CDN-N03-#n`.

---

## Design Intent

This node is the **reboil-and-removal circuit for the Flash Column (V-2302) concentrated CHP bottoms** — the deepest concentration step in the CDN Concentration sub-section. Its purpose:

1. **E-2304 (Flash Column Vaporizer)** is the column reboiler. **SC3 steam** on the shell side partially vaporizes the concentrated CHP bottoms circulating on the tube side (thermosyphon); the vapour-liquid mixture returns to V-2302. This drives the second-stage cumene evaporation, concentrating CHP from ~40 wt% (Preflash bottoms) to **~80-85 wt%** (Flash Column bottoms). Tube design FV/4 kg/cm²g @ 250 °C; shell design FV/10.5 kg/cm²g (uprated to permit emergency CW/firewater coolant).
2. **D-2309 (Vaporizer Condensate Drum) + P-2309A/B (Condensate Pumps)** collect E-2304 SC3 condensate and return it to the SC3 condensate system (68-0056). D-2309 at 2.3 kg/cm²g / 135 °C; PSV-23-0701 (fire case, 7.0 kg/cm²g).
3. **V-2302 bottoms draw + split-range level control (LIC-0802 / LY-0801)** removes net concentrated CHP from the column sump.
4. **P-2301A/B (Flash Column Bottoms Pumps)** pump the concentrated CHP (~60,873 kg/h, 105 m³/h pumps, **on Reliable/emergency power**, dual mechanical seal API Plan 53A with N₂ barrier) to the Decomposer feed system via 6"-CHP-23-009002/003. This is the critical Concentration→Decomposition handoff. AT-0901 monitors CHP concentration.

Normal process fluid is single-phase liquid concentrated CHP under deep vacuum (Flash Column operates ~17-150 mmHgA); SC3 saturated steam → condensate on the utility side. Cite [[wiki/units/cdn]], [[wiki/equipment/E-2304]], [[wiki/equipment/D-2309]], [[wiki/equipment/P-2309AB]], [[wiki/equipment/V-2302]], [[wiki/equipment/P-2301AB]].

**Governing safety fact for this node:** the concentrated CHP here (~80-85 wt%) is the most decomposition-prone, deflagration/detonation-capable inventory in the section. The SIS reflects this: E-2304 carries **four** temperature initiators (TXSHH-0701A/0702A SIL 2 with time delay = UC-2301 Cause 8; TXSHH-0701B/0702B immediate = Cause 9); the column bottom carries TXSHH-0805A/B (SIL 2, Cause 10); the bottoms-pump suction carries TXSHH-0901A/B (Cause 11); and the bottoms level carries LXSHH-0802 (Cause 6). The DIERS runaway-relief train PSV-23-0801A/B/C/D/E (sized 1005.42 cm² effective orifice) is the largest in the unit.

---

## Node Boundaries

> Per the **Node Boundary Rule**, boundaries are taken from the engineer's green markup, not inferred. The green highlight on **Node 23-03.pdf** spans six drawings (0007, 0007A, 0008, 0009, 0012, 0012A) — the vaporizer/condensate circuit plus the concentrated-CHP bottoms pump-out to the Decomposer feed. **Three handoffs need engineer confirmation — flagged below.**

**Inlet boundaries (into node):**
- **Utility:** SC3 steam supply to E-2304 shell, through the SIS isolation valves **UXV-0701-0706** (external steam header battery limit).
- **Process (CHP):** Concentrated CHP from **V-2302 bottoms** — into the E-2304 thermosyphon tube circuit, and into **P-2301A/B suction** (10"-CHP-23-008004) **downstream of the E-2306 Flash Column Bottoms Cooler**. ⚠️ *E-2306 is marked **Node 23-04** (cyan); confirm the 23-03 ↔ 23-04 tie-in is at the E-2306 outlet / pump suction.*
- **Process (flush):** Cumene flush + N₂ seal barrier (header 22-0027) to P-2301 seals and the startup recirculation line.

**Outlet boundaries (out of node):**
- **Process (CHP):** Concentrated CHP to the **Decomposer feed system**, line 6"-CHP-23-009002/003-L1A1-NI, "MIN DISTANCE TO UV-1204". ⚠️ *Confirm the 23-03 ↔ Decomposer-feed-node (markup 23-11/23-12/23-07 on Dwg 0012/0012A) handover point — provisionally taken at the D-2303 Decomposer Feed Flush Drum tie-in / UV-1204.*
- **Process (reboil return):** Vapour-liquid return from E-2304 to **V-2302** — handover to the Flash Column body node (marked **Node 23-05**, blue, on Dwg 0008). ⚠️ *Confirm whether V-2302 sump/level instruments (LXSHH-0802, TXSHH-0805) belong to 23-03 or 23-05 — recorded here as safeguards because the bottoms inventory is the node's dominant hazard.*
- **Utility:** SC3 condensate from P-2309A/B discharge, 4"-SC3-23-007007 to condensate system **68-0056** (external battery limit).

---

## Normal Operating Parameters (itemized per equipment tag)

| Tag | Stream / side | Design Condition | Operating Condition | Source |
|-----|---------------|------------------|---------------------|--------|
| **E-2304** tube | Concentrated CHP (~80-85 wt%) thermosyphon | FV / 4 kg/cm²g @ 195/250 °C | ~70 °C in (S320), ~97 °C vaporized out (S3241); 97,806 kg/h in, 35,838 kg/h vaporized; under column vacuum | [[wiki/equipment/E-2304]]; PFD-0002 |
| **E-2304** shell | SC3 steam (heating medium) | FV / 10.5 kg/cm²g @ 195 °C | SC3 steam 7,947 kg/h; emergency CW/firewater coolant connection | [[wiki/equipment/E-2304]] |
| **D-2309** | SC3 steam condensate | INT 7.0 / EXT FV @ 195 °C | 2.3 kg/cm²g / 135 °C; NLL 550 mm (HLL 790 / LLL 310) | [[wiki/equipment/D-2309]] |
| **P-2309A/B** | SC3 condensate | 15.3 m³/h @ 1.58 kg/cm² ΔP; sealless mag-drive | running/standby; FY-0703 auto-start; min autostart static 3.80 kg/cm² | [[wiki/equipment/P-2309AB]] |
| **V-2302** bottoms | Concentrated CHP (~80-85 wt%) | FV / 3.5 kg/cm²g @ 195/200 °C | bottoms ~60 °C, 60,873 kg/h (S372); deep vacuum 17-150 mmHgA | [[wiki/equipment/V-2302]] |
| **P-2301A/B** | Concentrated CHP to Decomposer | 105 m³/h @ 3.7 kg/cm² ΔP; **Reliable Power**; Plan 53A dual seal, N₂ @ 7 kg/cm² | ~60 °C suction; 81 mol% CHP basis; AT-0901 concentration | [[wiki/equipment/P-2301AB]] |

> **DATA NOTES for team:**
> - P-2309 capacity CONFLICT: PS-P2309 rated 13.3 m³/h vs P&ID-derived 15.3 m³/h ([[wiki/equipment/P-2309AB]]). Minor; not safety-controlling.
> - AT-0901 CHP concentration is an **inferential density-proxy** measurement — routine lab CHP analysis required for verification ([[wiki/instruments/analyzers-cdn]]).
> - E-2304 has **no dedicated PSV on the process (CHP) tube side**; in normal lineup it relieves through V-2302's PSV-23-0801 train. The block-isolated case is a gap (see #6.1).

---

## HAZOP Worksheet

> Risk rankings per [[wiki/hazop/risk-matrix]]. Safeguard adequacy per [[wiki/sources/P-Q-MP-OEMS-005]] and [[wiki/hazop/methodology]] Tables 6.4-6.6.
>
> ✅ **Economic severity:** PPCL classified **BU** (resolved 2026-06-17) — Extreme(5) ≥100 M THB; High(4) 10–<100 M; Medium(3) 1–<10 M; Low(2) 0.1–<1 M; Very Low(1) <0.1 M, per [[wiki/hazop/risk-matrix]]. Risk uses the **highest** of People/Environment/Economic/Social. Production-loss Ec estimates are first-pass for team validation.
>
> Likelihood basis: [[wiki/hazop/methodology]] Table 6.3. IPL credit: Tables 6.4-6.6. SIL credit: SIL 1 = −1 level, SIL 2 = −2 levels.

### 1. Flow — No / Low Flow (concentrated-CHP bottoms removal + E-2304 reboil circulation)

**1.1 Cause:** Both P-2301A/B stop — mechanical failure, operator fails to start the standby (Type B manual control, no hardwired auto-start), or loss of suction — so net concentrated CHP is no longer removed from the V-2302 sump while E-2304 continues to supply reboiler heat.

- **1.1.1 Consequence:** Concentrated CHP (~80-85 wt%) accumulates in the V-2302 sump and E-2304 tube circuit with continued vaporizer heat → bulk temperature rises above the ~80 °C decomposition onset → autocatalytic exothermic decomposition → DIERS self-heating runaway → rapid heat + O₂ + overpressure → column/vaporizer relief or rupture → LOPC of concentrated CHP, fire/explosion (deflagration/detonation potential), potential multiple fatalities.
  - Without Safeguard — L: 4 | Severity P/En/Ec/S: 5/4/5/4 | **RR: Extreme**
  - Safeguards:
    - 1.1.1.1 **LXSHH-0802** (1oo1) Flash Column bottom high-high level → UC-2301 Concentration ESD: closes **UXV-0701-0706** (cuts SC3 steam to E-2304) + cross-trips UC-2302 — IL/ESD: **Yes** — IPL=1 — [[wiki/instruments/cause-effect-cdn]] Cause 6
    - 1.1.1.2 **TXSHH-0805A/B** (1oo2, SIL 2) Flash Column bottom high-high temp → UC-2301 ESD cuts steam — IL/ESD: **Yes** — IPL=2 — Cause 10
    - 1.1.1.3 **TXSHH-0901A/B** (1oo2) bottoms-pump suction high-high temp → UC-2301 ESD — IL/ESD: **Yes** — IPL=1 — Cause 11
    - 1.1.1.4 P-2301A/B on **Reliable Power** + standby (Motor Note M13 independent supply); FAL-0901 low-flow alarm + operator starts standby — IL/ESD: No — IPL=1
    - 1.1.1.5 **PSV-23-0801A/B/C/D/E** DIERS self-heating-reaction relief on V-2302 (set 2.10/2.205 kg/cm²g, 327,745 kg/h) — IL/ESD: No — IPL=2 — [[wiki/instruments/pressure-relief-valves-cdn]]
  - With Existing Safeguard — L: 2 | Severity P/En/Ec/S: 5/4/5/4 | **RR: Medium**
  - Recommendation: **R-005** (LOPA / SIF integrity confirmation for the concentrated-CHP overheat consequence)
  - After Recommendation Comp. — *(fill at action close-out)*

**1.2 Cause:** Loss of E-2304 thermosyphon circulation — tube fouling, vapour blanketing, or low column level starving the reboiler.

- **1.2.1 Consequence:** Reduced vaporization → poorer cumene removal → under-concentrated bottoms; **safe direction for CHP** (lower temperature, lower concentration). Localized stagnant CHP in fouled tubes could still overheat (minor). Production/operability.
  - Without Safeguard — L: 3 | Severity P/En/Ec/S: 2/1/2/1 | **RR: Low**
  - Safeguards: TIC-0703 vaporizer temperature control; bottom-temp/concentration monitoring (AT-0901); high-temp SIFs catch local overheat.
  - With Existing Safeguard — L: 2 | Severity: 2/1/2/1 | **RR: Low**
  - Recommendation: None — risk acceptable.

### 2. Flow — More Flow (concentrated CHP to Decomposer)

**2.1 Cause:** P-2301 discharge flow high / LIC-0802 bottoms-level control upset → excess concentrated CHP pumped to the Decomposer feed.

- **2.1.1 Consequence:** Higher concentrated-CHP feed rate to the Decomposer; if the acid-injection cascade (FY-1201B High-Signal-Selector → multiplier FY-0012) fails to track, under-acidified concentrated CHP reaches the Decomposer → decomposer upset / runaway risk (downstream node). Within node: lower V-2302 level → P-2301 cavitation. Production/operability + downstream handoff.
  - Without Safeguard — L: 3 | Severity P/En/Ec/S: 2/1/2/1 | **RR: Low** `[within-node consequence; the CHP-to-decomposer runaway path is ranked in the Decomposer node]`
  - Safeguards: FY-1201B/FY-0012 flow-to-acid multiplier cascade (acid injection proportional to bottoms flow, conservative high-selector); FE/FT-0901 + FAL-0901; LIC-0802 level control; AT-0901 CHP analyzer.
  - With Existing Safeguard — L: 2 | Severity: 2/1/2/1 | **RR: Low**
  - Recommendation: None at node level — **flag** acid-cascade (FY-1201B/FY-0012) integrity for the Decomposer-feed node analysis.

### 3. Flow — Reverse Flow

**3.1 Cause:** P-2301A/B trip with the Decomposer-feed system at higher pressure / static head → reverse flow of decomposer-side material back toward the Flash Column bottoms.

- **3.1.1 Consequence:** Backflow of acidified / partially-decomposed material (sulphuric acid is a **potent CHP decomposition catalyst** — [[wiki/hazards/cumene-hydroperoxide]]) from the Decomposer feed into the concentrated CHP at V-2302 → acid-catalysed decomposition at low temperature → runaway → rupture, fire/explosion.
  - Without Safeguard — L: 3 | Severity P/En/Ec/S: 5/4/5/4 | **RR: High**
  - Safeguards:
    - 3.1.1.1 Check valve(s) on P-2301 discharge (6"-CHP-23-009002/003) — IL/ESD: No — IPL=1 [VERIFY presence/independence on P&ID 0009/0012]
    - 3.1.1.2 **UXV-0802/0803** close on UC-2302 Decomposition ESD — isolate Flash Column bottoms-to-Decomposer — IL/ESD: **Yes** — IPL=1 — [[wiki/instruments/cause-effect-cdn]] UC-2302
    - 3.1.1.3 "MIN DISTANCE TO UV-1204" pipe-volume buffer before the Decomposer feed control zone
  - With Existing Safeguard — L: 2 | Severity: 5/4/5/4 | **RR: Medium**
  - Recommendation: **R-009** (confirm check-valve adequacy against acid backflow)
  - After Recommendation Comp. — *(fill at action close-out)*

### 4. Temperature — More / High Temperature  ⭐ dominant node hazard

**4.1 Cause:** E-2304 SC3 steam control fails to maximum heat input — TIC-0703 / steam control valve fails open, or SC3 header over-temperature → vaporizer over-heats the concentrated CHP above the ~80 °C decomposition onset.

- **4.1.1 Consequence:** Autocatalytic exothermic decomposition of ~80-85 wt% CHP in the E-2304 tubes and V-2302 sump → DIERS self-heating runaway → rapid heat + O₂ + overpressure → column/vaporizer rupture or relief → LOPC of concentrated CHP → fire/explosion, **deflagration/detonation potential**, multiple fatalities.
  - Without Safeguard — L: 4 | Severity P/En/Ec/S: 5/4/5/4 | **RR: Extreme**
  - Safeguards:
    - 4.1.1.1 **TXSHH-0701A/0702A** (1oo2, SIL 2, time-delay "A") vaporizer vapour-space/outlet high-high temp → UC-2301 closes UXV-0701-0706 (SC3 steam) — IL/ESD: **Yes** — IPL=2 — Cause 8
    - 4.1.1.2 **TXSHH-0701B/0702B** (1oo2, immediate, no delay) second pair → UC-2301 — IL/ESD: **Yes** — IPL=1 (unrated, immediate backup) — Cause 9
    - 4.1.1.3 **TXSHH-0805A/B** (1oo2, SIL 2) Flash Column bottom high-high temp → UC-2301 (independent bottom location) — IL/ESD: **Yes** — IPL=2 — Cause 10
    - 4.1.1.4 **TXAHH-0701/0702 (CRIT)** DCS critical high-temp alarms + operator cuts steam — IL/ESD: No — IPL=1 [VERIFY independence from TXSHH transmitters]
    - 4.1.1.5 Emergency CW/firewater coolant to E-2304 shell (design provision; drove shell uprate to 10.5) — emergency mitigation, **not a creditable IPL** per Table 6.6 — IPL=0
    - 4.1.1.6 **PSV-23-0801A/B/C/D/E** DIERS runaway relief on V-2302 — IL/ESD: No — IPL=2
  - With Existing Safeguard — L: 2 | Severity: 5/4/5/4 | **RR: Medium**
  - Recommendation: **R-005**
  - After Recommendation Comp. — *(fill at action close-out)*

**4.2 Cause:** Loss of Flash Column Bottoms Cooler **E-2306** duty (Node 23-04) / cooling-water loss → hot concentrated CHP to P-2301 suction.

- **4.2.1 Consequence:** Concentrated CHP at the pump suction overheats above onset → decomposition at the pump / suction line → LOPC, fire/explosion. *(initiating cause is in Node 23-04; consequence manifests at P-2301 within this node.)*
  - Without Safeguard — L: 3 | Severity: 5/4/5/4 | **RR: High**
  - Safeguards:
    - 4.2.1.1 **TXSHH-0901A/B** (1oo2) pump-suction high-high temp → UC-2301 ESD — IL/ESD: **Yes** — IPL=1 — Cause 11
    - 4.2.1.2 TAH-0901A/B DCS temp alarms + operator — IL/ESD: No — IPL=1
  - With Existing Safeguard — L: 1 | Severity: 5/4/5/4 | **RR: Low**
  - Recommendation: None at node level — confirm TXSHH-0901 setpoint margin under R-005; coordinate E-2306 cooling reliability with Node 23-04.

### 5. Temperature — Less / Low Temperature

**5.1 Cause:** Loss of SC3 steam to E-2304 — header loss, UXV-0701-0706 spurious closure, or TIC-0703 fails low.

- **5.1.1 Consequence:** Loss of reboil → poor cumene flash → under-concentrated CHP bottoms to the Decomposer (off-spec, lower concentration). **Safe direction for CHP** (no decomposition). Decomposer feed concentration low → downstream control/operability impact; production loss.
  - Without Safeguard — L: 4 | Severity P/En/Ec/S: 1/1/2/1 | **RR: Medium** `[Ec: BU — production loss est. 0.1–<1 M THB → Ec 2; team to validate]`
  - Safeguards: TIC-0703 temperature control; AT-0901 CHP concentration analyzer + operator; downstream Decomposer feed controls; column bottom temp indication.
  - With Existing Safeguard — L: 3 | Severity: 1/1/2/1 | **RR: Low**
  - Recommendation: None — residual Low after operator response; Ec estimate to validate.

### 6. Pressure — More / High Pressure

**6.1 Cause:** Concentrated-CHP system blocked in — P-2301 discharge blocked (UXV-0802/0803 close on a UC-2302 trip while P-2301 keeps running on Reliable Power; downstream block; or maintenance isolation) → deadhead / thermal expansion / decomposition-gas pressurisation of the liquid-full concentrated-CHP system (E-2304 tube FV/4, pump casing, bottoms line).

- **6.1.1 Consequence:** Overpressure beyond the E-2304 tube (FV/4 kg/cm²g) / pump / piping rating → rupture → LOPC of concentrated CHP → fire/explosion. **Note:** P-2301 is on Reliable Power and is **not** stopped by UC-2301/UC-2302 — it can deadhead against closed UXV-0802/0803.
  - Without Safeguard — L: 3 | Severity P/En/Ec/S: 5/4/5/4 | **RR: High**
  - Safeguards:
    - 6.1.1.1 Minimum-flow / startup recirculation 4"-CHP-23-009004 back to V-2302 — IL/ESD: No — IPL=1 [VERIFY whether continuous min-flow or startup-only — if startup-only, no credit on a running-deadhead case]
    - 6.1.1.2 In normal lineup the CHP side relieves via **PSV-23-0801A-E** on V-2302 — IL/ESD: No — IPL=2
    - 6.1.1.3 High-temp SIFs (TXSHH-0701/0702/0805) cut steam before decomposition pressure develops — IL/ESD: **Yes** — IPL=1
    - 6.1.1.4 **GAP:** no dedicated PSV / thermal relief on the E-2304 tube side or P-2301 discharge when isolated from V-2302 relief (UXV-0802/0803 closed) — IPL=0
  - With Existing Safeguard — L: 2 | Severity: 5/4/5/4 | **RR: Medium**
  - Recommendation: **R-006**
  - After Recommendation Comp. — *(fill at action close-out)*

**6.2 Cause:** SC3 steam supply overpressure into the E-2304 shell / D-2309 condensate system (steam header excursion).

- **6.2.1 Consequence:** Steam-side overpressure (E-2304 shell design 10.5, D-2309 design 7.0 kg/cm²g) → tube/drum overpressure → LOPC of steam/condensate (low chemical hazard); possible escalation to the CHP tube side via tube failure (see #11.1).
  - Without Safeguard — L: 3 | Severity: 2/1/2/1 | **RR: Low**
  - Safeguards: **PSV-23-0701** on D-2309 (set 7.0 kg/cm²g, fire case, 157 kg/h) — IL/ESD: No — IPL=2; E-2304 shell rated 10.5 (emergency-coolant uprate).
  - With Existing Safeguard — L: 1 | Severity: 2/1/2/1 | **RR: Very Low**
  - Recommendation: Confirm PSV-23-0701 also bounds the steam-supply overpressure case (note under R-006).

### 7. Pressure — Less / Vacuum

**7.1 Cause:** Steam-side vacuum on trip — sudden SC3 isolation (UXV-0701-0706 close) collapses steam in the E-2304 shell → vacuum / condensate-induced water hammer. (Process tube side already operates under deep column vacuum by design.)

- **7.1.1 Consequence:** Vacuum collapse / water hammer in the E-2304 shell → tube mechanical damage → progression to tube leak (#11.1).
  - Without Safeguard — L: 3 | Severity: 2/1/2/1 | **RR: Low**
  - Safeguards: E-2304 shell **and** tube rated Full Vacuum; D-2309 design FV (inherent design — eliminates the failure mode, not a creditable active IPL).
  - With Existing Safeguard — L: 2 | Severity: 2/1/2/1 | **RR: Low**
  - Recommendation: None — confirm no vacuum-breaker requirement given FV-rated design.

### 8. Level — More / High Level (D-2309 condensate drum)

**8.1 Cause:** LIC-0701 / LV-0701 condensate-return control fails closed, or SC3 condensate-return backpressure → D-2309 level rises.

- **8.1.1 Consequence:** Condensate backs into the E-2304 shell → flooding → loss of steam heat-transfer area → erratic/low reboil → low concentration (links #5.1); potential condensate-induced water hammer.
  - Without Safeguard — L: 4 | Severity: 2/1/2/1 | **RR: Medium**
  - Safeguards: **LAH-0701** high-level DCS alarm + operator; LIC-0701 control; HLL 790 mm reference — IL/ESD: No — IPL=1.
  - With Existing Safeguard — L: 3 | Severity: 2/1/2/1 | **RR: Low**
  - Recommendation: None — risk acceptable.

### 9. Level — Less / Low Level (D-2309 condensate drum)

**9.1 Cause:** Excess condensate pump-out / loss of condensate make (steam off) / LV-0701 fails open → D-2309 level falls.

- **9.1.1 Consequence:** P-2309A/B lose suction (NPSH; min autostart static 3.80 kg/cm²) → cavitation / steam blow-through to the condensate-return system; possible pump damage.
  - Without Safeguard — L: 4 | Severity: 2/1/2/1 | **RR: Medium**
  - Safeguards: **LAL-0701** low-level alarm + operator; LLL 310 mm reference; FY-0703 standby auto-start (flow-based); P-2309 sealless mag-drive (no seal leak path) — IL/ESD: No — IPL=1.
  - With Existing Safeguard — L: 3 | Severity: 2/1/2/1 | **RR: Low**
  - Recommendation: None — risk acceptable.

### 10. Service Failures — Loss of Utility

**10.1 Cause:** Loss of electrical power → P-2309A/B (Type L) stop; **P-2301A/B remain running on Reliable Power** (emergency bus + Motor Note M13 independent standby supply).

- **10.1.1 Consequence:** Concentrated-CHP removal is **maintained** by P-2301 (intended safety design). P-2309 stop → condensate backs into E-2304 (as #8.1.1) → reduced reboil; no direct CHP hazard. **If Reliable Power is also lost** → P-2301 stop → loss of CHP removal (refer #1.1.1).
  - Without Safeguard — L: 3 | Severity: 2/1/2/1 | **RR: Low**
  - Safeguards: P-2301 Reliable-Power + independent standby (M13); LXSHH-0802 / high-temp SIFs cut SC3 steam on any accumulation (refer #1.1).
  - With Existing Safeguard — L: 2 | Severity: 2/1/2/1 | **RR: Low**
  - Recommendation: None — total-power case bounded by #1.1.1 / R-005.

**10.2 Cause:** Loss of instrument air → TIC-0703 SC3 steam valve and LV-0701/LV-0802 go to fail position.

- **10.2.1 Consequence:** If the SC3 steam valve fails **open** → High Temperature (refer #4.1.1, CHP decomposition). If **closed** → Low Temperature (refer #5.1.1). Outcome depends on fail-action (to confirm).
  - **Action:** Confirm fail-safe action of TIC-0703 SC3 steam valve (should be fail-closed = safe) and LV-0701/LV-0802. — note under **R-006**. [VERIFY — [[wiki/instruments/control-valves-cdn]]]

**10.3 Cause:** Loss of cumene flush + N₂ seal barrier (header 22-0027) to the P-2301A/B Plan 53A dual mechanical seals.

- **10.3.1 Consequence:** Concentrated CHP contacts the seal faces without flush/barrier → seal degradation/failure → LOPC of ~80-85 wt% concentrated CHP at the pump → fire / corrosive exposure (CHP H314/H331) / localized decomposition.
  - Without Safeguard — L: 3 | Severity P/En/Ec/S: 4/3/3/3 | **RR: High**
  - Safeguards: Plan 53A pressurized dual seal, N₂ barrier @ 7 kg/cm² with seal-gas panel **low-pressure / high-flow alarms** (PS-P2301 Note 2) — IL/ESD: No — IPL=1; CHP Closed Drain Header (STD DWG 8-137) captures seal leakage.
  - With Existing Safeguard — L: 2 | Severity: 4/3/3/3 | **RR: Medium**
  - Recommendation: **R-007** (confirm seal barrier/flush alarm + operator response adequacy)
  - After Recommendation Comp. — *(fill at action close-out)*

### 11. Composition / As Well As — Tube Leak / Rupture (E-2304)

**11.1 Cause:** E-2304 tube leak/rupture between SC3 steam (shell, ~3 kg/cm²g, or emergency CW/firewater) and concentrated CHP (tube, under deep vacuum).

- **11.1.1 Consequence:** Higher-pressure shell fluid (steam, or emergency CW/firewater) leaks **into** the lower-pressure (vacuum) concentrated-CHP tube side → water ingress into ~80-85 wt% CHP (contamination, corrosion, runaway-transition risk). Conversely, on pressure reversal / loss of vacuum, concentrated CHP migrates to the SC3 steam-condensate system (D-2309 → condensate return 68-0056), which is **not rated/monitored for CHP** → uncontrolled CHP in a utility system, off-site migration, potential decomposition/fire.
  - Without Safeguard — L: 3 | Severity P/En/Ec/S: 4/3/4/3 | **RR: High**
  - Safeguards: 304L SS tubes (CHP-compatible) — IPL=0; construction-stage helium leak test (one-time, not an operating IPL) — IPL=0; periodic inspection (non-IPL per Table 6.6). **No on-line CHP/HC detection on the D-2309 condensate identified.**
  - With Existing Safeguard — L: 3 | Severity: 4/3/4/3 | **RR: High**
  - Recommendation: **R-008** (condensate contamination / CHP-migration detection)
  - After Recommendation Comp. — *(fill at action close-out)*

### 12. Composition — Other Than (Contamination)

**12.1 Cause:** Iron / transition-metal (Cu, Fe, Mn) or acid contamination of the concentrated CHP — corrosion products, copper ingress, or acid carryback from the Decomposer via reverse flow (#3.1) — all potent CHP decomposition catalysts; effect is magnified at ~80-85 wt%.

- **12.1.1 Consequence:** Catalysed CHP decomposition at lower-than-expected temperature → localized exotherm → runaway as #4.1.1 → rupture, fire/explosion.
  - Without Safeguard — L: 3 | Severity P/En/Ec/S: 5/4/5/4 | **RR: High**
  - Safeguards: 316 SS (P-2301) / 304L SS (E-2304, V-2302) wetted parts — no Cu/Cu-alloy, no carbon steel in CHP service per [[wiki/hazards/cumene-hydroperoxide]] — IPL=1 (inherent/passive); AT-0901 CHP concentration/density analyzer + lab verification; high-temp SIFs (TXSHH-0701/0702/0805/0901); check valves prevent acid backflow (#3.1).
  - With Existing Safeguard — L: 2 | Severity: 5/4/5/4 | **RR: Medium**
  - Recommendation: None new — covered by **R-009** (acid backflow) and **R-005**; confirm AT-0901 reliability (inferential density proxy) with the team.

### 13. "Other" Checklist Items

| Topic | Preliminary finding |
|-------|---------------------|
| **Relief scenario** | DIERS runaway relief PSV-23-0801A-E on V-2302 (largest train in unit, 1005.42 cm²) covers the column/vaporizer in normal lineup. **E-2304 tube side and P-2301 discharge have no dedicated relief when block-isolated** → **R-006**. D-2309 PSV-23-0701 (fire case) — confirm it also bounds steam-supply overpressure. E-2306 (Node 23-04) has PSV-23-0802 (thermal-expansion, CW side only). |
| **Instrumentation** | Four temperature SIFs on the vaporizer/column (TXSHH-0701A/0702A SIL 2 Cause 8; -0701B/0702B Cause 9; TXSHH-0805A/B SIL 2 Cause 10; TXSHH-0901A/B Cause 11) + LXSHH-0802 (Cause 6). LOPA confirmation of combined coverage for the S5 concentrated-CHP consequence → **R-005**. Confirm time-delay "A" architecture does not delay protection past runaway onset for ~80-85 wt% CHP. |
| **Sampling** | **SN-2303 (Type A-CH) on P-2301 is the HIGHEST-hazard sample point in CDN** (~80-85 wt% concentrated CHP) — specialized CHP procedure with cumene pre/post-flush mandatory; never sample alone; full PPE. SN-2310 on the vaporizer line (Type B-CH). Confirm sampling provisions with team — [[wiki/instruments/sampling-cdn]]. |
| **Corrosion** | CHP + Fe/Cu catalysis — 316 SS (P-2301) / 304L SS (E-2304, V-2302) confirmed; KCS acceptable on the SC3 condensate (non-CHP) side. OK; confirm no carbon steel in any CHP-wetted line. |
| **Service failure** | Confirm SC3 steam control-valve fail-action (#10.2); P-2301 Reliable-Power classification verified (M13); P-2309 Type L (non-reliable). Loss of cumene seal flush → **R-007**. |
| **Maintenance** | P-2301 single-train isolatable while online — confirm safe **concentrated-CHP draining/purging** to the CHP Closed Drain Header and relief during isolation (**R-006**). Highest-concentration CHP in section — most stringent isolation precautions. |
| **Start-up** | **HXS-0102 bypasses LXSHH-0802** (Flash Column bottom level) during startup — confirm the high-temperature protection (TXSHH-0701/0702/0805) remains active when the level interlock is bypassed. **Important — review with team.** |
| **Human factor** | Type B manual standby start on P-2301 (no auto-start) — operator must act on FAL-0901; concentrated-CHP sampling complexity (SN-2303); alarm response time vs CHP runaway onset (R-005). |

---

## Recommendations Generated (preliminary)

| Rec# | Deviation Row | Description | Risk Rank | Status |
|------|--------------|-------------|-----------|--------|
| R-005 | CDN-N03-#1.1.1, #4.1.1 | Perform LOPA / SIF verification that the combined over-temperature protection (TXSHH-0701A/0702A SIL 2 Cause 8 + TXSHH-0701B/0702B Cause 9 + TXSHH-0805A/B SIL 2 Cause 10 + TXSHH-0901A/B Cause 11 + LXSHH-0802 Cause 6, all → UC-2301 closing UXV-0701-0706) achieves tolerable risk for the S5 concentrated-CHP (~80-85 wt%) decomposition/runaway consequence; confirm all TXSHH setpoints sit below the 80 °C decomposition onset with adequate margin; confirm the time-delay "A" architecture does not delay protection past runaway onset; confirm the HXS-0102 startup bypass of LXSHH-0802 does not disable temperature protection. | Medium | Open |
| R-006 | CDN-N03-#6.1.1, #6.2.1, #10.2 | Review overpressure / thermal-relief protection for the **E-2304 tube side and P-2301A/B discharge when block-isolated** (no dedicated PSV once UXV-0802/0803 closed and isolated from V-2302's PSV-23-0801 relief), including the P-2301 deadhead case (pump on Reliable Power not stopped by ESD); confirm whether the 4"-CHP-23-009004 recirculation provides continuous minimum flow or is startup-only; confirm safe concentrated-CHP draining/purging for single-train isolation; confirm SC3 steam control-valve fail-closed action. | High | Open |
| R-007 | CDN-N03-#10.3.1 | Confirm the P-2301A/B Plan 53A dual-seal cumene-flush / N₂-barrier (22-0027) low-pressure/high-flow alarm coverage and operator response are adequate to detect loss of seal flush before concentrated CHP attacks the seal and causes LOPC; verify barrier-fluid integrity monitoring and auto-response. | Medium | Open |
| R-008 | CDN-N03-#11.1.1 | Provide on-line detection of CHP/hydrocarbon carryover into the SC3 steam-condensate system (conductivity/pH or hydrocarbon analyzer with alarm and/or condensate divert) at D-2309 / condensate return, to detect an E-2304 tube leak and prevent migration of concentrated CHP to the unrated utility condensate system; given the emergency CW/firewater coolant connection on the E-2304 shell, also address water-into-CHP ingress detection. | High | Open |
| R-009 | CDN-N03-#3.1.1 | Confirm independent check-valve protection (presence, type, testability) on the P-2301A/B discharge (6"-CHP-23-009002/003) prevents reverse flow of acidified/partially-decomposed material from the Decomposer feed back into the concentrated CHP at V-2302, since acid backflow is a potent CHP decomposition catalyst. | Medium | Open |

---

## References
- [[wiki/equipment/E-2304]], [[wiki/equipment/D-2309]], [[wiki/equipment/P-2309AB]], [[wiki/equipment/V-2302]], [[wiki/equipment/P-2301AB]] — equipment within node
- [[wiki/equipment/E-2306]] — Flash Column Bottoms Cooler (Node 23-04; suction-boundary handoff, #4.2)
- [[wiki/equipment/D-2304]] — Decomposer Drum (downstream destination of the concentrated CHP)
- [[wiki/instruments/cause-effect-cdn]] — UC-2301 Causes 6/8/9/10/11; UC-2302 UXV-0802/0803; existing SIS safeguards
- [[wiki/instruments/sis-cdn]] — SIS architecture
- [[wiki/instruments/pressure-relief-valves-cdn]] — PSV-23-0701 (D-2309), PSV-23-0801A-E (V-2302 DIERS), PSV-23-0802 (E-2306)
- [[wiki/instruments/analyzers-cdn]] — AT/AY-23-0901 CHP concentration (inferential density proxy)
- [[wiki/instruments/sampling-cdn]] — SN-2303 (highest-hazard CHP sample), SN-2310
- [[wiki/instruments/control-valves-cdn]] — SC3 steam control-valve fail-action (to verify)
- [[wiki/hazards/cumene-hydroperoxide]] — CHP decomposition onset / deflagration-detonation / catalyst sensitivity basis
- [[wiki/units/cdn]] — Concentration sub-section design intent and stream data
- [[wiki/hazop/risk-matrix]] — risk ranking criteria (Economic = BU)
- [[wiki/hazop/methodology]] — guideword set, IPL credit tables, likelihood guidance
- [[wiki/sources/P-Q-MP-OEMS-005]] — safeguard validation basis
