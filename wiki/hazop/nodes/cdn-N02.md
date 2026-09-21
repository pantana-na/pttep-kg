---
name: Preflash Column Feed-Heating / Steam-Condensate Circuit
node_id: CDN-N02
markup_label: "Node 23-02 (engineer P&ID markup)"
unit: CDN
pid_sheet: "14780-8120-25-23-0005, -0005A (primary); -0004 and -0007 (boundary crossings)"
pid_marked_up: "Node 23-02.pdf (user-supplied markup — recommend filing in raw/pid/)"
inlet_boundary: "Oxidate feed to E-2302A/B tube side (from feed filters X-2302A/B / Node 23-01) + hot OXI recirculate to E-2302A/B shell (from OXI Oxidizer No.2 pumps) + SC1.5 steam supply to E-2303 tube (via UXV-0501/0502)"
outlet_boundary: "Heated oxidate to V-2301 (Preflash Column) + OXI recirculate shell return to OXI + steam condensate from P-2308A/B to condensate return system (66-0056)"
tags: [hazop, node, CDN, preliminary]
last_updated: 2026-06-17
status: PRELIMINARY — boundaries CONFIRMED by engineer 2026-06-17; Economic=BU applied; worksheet for HAZOP team review/finalization
---

# HAZOP Node CDN-N02 — Preflash Column Feed-Heating / Steam-Condensate Circuit

> ⚠️ **PRELIMINARY DRAFT (2026-06-17).** Generated from the user-supplied "Node 23-02" P&ID markup + wiki PSI. This is a desktop first-pass to seed the facilitated workshop — **not** a completed, team-validated worksheet. Causes, consequences, safeguard adequacy, and risk rankings require confirmation by the HAZOP team per [[wiki/hazop/methodology]].

> ⚠️ CHP is a peroxide — thermal decomposition risk. The oxidate in this node is ~22.6 wt% CHP and is heated through the CHP decomposition-onset region. See [[wiki/hazards/cumene-hydroperoxide]].

> 🟨 **Markup label:** the engineer's drawings label this **"Node 23-02"**; filed here as **CDN-N02** per the skill's `<unit>-N<nn>` schema. Deviation references use `CDN-N02-#n`.

---

## Design Intent

This node is the **feed-heating train of the Preflash Column (V-2301)** plus its steam-condensate subsystem. Its purpose is to raise the CHP-containing oxidate feed coming from the Oxidation Section to the target Preflash Column feed temperature, recovering heat first and trimming with steam:

1. **E-2302A/B (Feed-Oxidate Exchangers)** preheat the cold fresh oxidate (tube side) against hot recirculating oxidate returning from the Oxidation Section (shell side) — energy integration. Two parallel units at 52.5% each.
2. **E-2303 (Preflash Column Steam Heater)** provides the final trim heat with **SC1.5 steam** (tube side) to the oxidate (shell side), under feed-forward control (FIC-0501) from OXI flow/temperature signals.
3. Heated oxidate is delivered to **V-2301** (Preflash Column), where excess cumene is flashed off under vacuum.
4. **D-2308 (Condensate Drum)** + **P-2308A/B (Condensate Pumps)** collect E-2303 steam condensate and return it to the condensate system (66-0056).

Normal flow is single-phase liquid oxidate on the process side; saturated steam → condensate on the utility side. Cite [[wiki/units/cdn]] (Concentration sub-section), [[wiki/equipment/E-2302AB]], [[wiki/equipment/E-2303]], [[wiki/equipment/D-2308]], [[wiki/equipment/P-2308AB]].

**Governing safety fact for this node:** CHP decomposition onset ≈ **80 °C** (worst-case PSS basis, SADT 60–80 °C — [[wiki/hazards/cumene-hydroperoxide]]). The oxidate feed is already ~82–83 °C and the heating medium (SC1.5 steam) is ~120–133 °C — well above onset. **Over-temperature of CHP-containing oxidate is the dominant hazard of this node.** This is why two independent SIL 1 SIFs (TXSHH-0501, TXSHH-0502A/B) and redundant steam isolation (UXV-0501/0502) protect it.

---

## Node Boundaries

> Per the **Node Boundary Rule**, boundaries are taken from the engineer's markup, not inferred. The core circuit is unambiguous in the markup (drawings 0005/0005A fully enclosed in yellow). Two points need engineer confirmation — flagged below.

**Inlet boundaries (into node):**
- **Process (cold feed):** Oxidate feed to E-2302A/B tube side — handed over from **Node 23-01** (feed filters X-2302A/B, Dwg 0003/0004). ⚠️ *Confirm exact N01↔N02 tie-in point on the markup.*
- **Process (hot side):** Recirculating oxidate to E-2302A/B shell, line 12"-CUL-23-011004 from **OXI Oxidizer No.2 pumps** (external battery limit).
- **Utility:** SC1.5 steam supply to E-2303 tube side, through the two SIS isolation valves **UXV-0501/0502** (external steam header battery limit).

**Outlet boundaries (out of node):**
- **Process:** Heated oxidate to **V-2301** Preflash Column — line 12"-CUL-23-005001 (stab-in). Hands over to the Preflash Column node (marked **Node 23-05**, blue, on Dwg 0004).
- **Process (hot side):** Shell-side recirculate return 16"-CUL-23-005001 to OXI Oxidizer No.2 Emergency Cooler (external battery limit).
- **Utility:** Steam condensate from P-2308A/B discharge, 4"-SCL.5-23-005006 to condensate system **66-0056** (external battery limit).

**✅ Confirmed by engineer (2026-06-17):** the boundary interpretation above is correct.
1. Inlet tie-in between Node 23-01 and Node 23-02 on the feed line — confirmed as recorded.
2. The short yellow segment on **Dwg 0007** (Flash Column Vaporizer) — confirmed as recorded; no change to node scope.

---

## Normal Operating Parameters (itemized per equipment tag)

| Tag | Stream / side | Design Condition | Operating Condition | Source |
|-----|---------------|------------------|---------------------|--------|
| **E-2302A/B** tube | Fresh oxidate feed (CHP ~22.6 wt%) | 12 kg/cm²g / FV @ 83→120 °C | ~82–83 °C; feed flow part of S229 1,076,643 kg/h total | [[wiki/equipment/E-2302AB]]; PFD-0001 |
| **E-2302A/B** shell | Hot OXI recirculate (CHP-containing) | 3.5 kg/cm²g / FV @ 195/250 °C | hot recirculate from OXI | [[wiki/equipment/E-2302AB]] |
| **E-2303** shell | Oxidate (process, CHP) | 3.5 kg/cm²g / FV @ 195/250 °C | in ~82 °C → out ~83 °C target to V-2301 | [[wiki/equipment/E-2303]] |
| **E-2303** tube | SC1.5 steam | 7 kg/cm²g / FV @ 120/195 °C | SC1.5 steam, ~120–133 °C sat. | [[wiki/equipment/E-2303]] |
| **D-2308** | Steam condensate | INT 7 kg/cm²g / FV @ 195 °C | 0.9 kg/cm²g / 117 °C; NLL 550 mm | [[wiki/equipment/D-2308]] |
| **P-2308A/B** | Condensate | 18.0 m³/h @ 1.53 kg/cm² ΔP | running/standby; FY-0502 auto-start | [[wiki/equipment/P-2308AB]] |

> ⚠️ **DATA CONFLICT to resolve before workshop:** [[wiki/units/cdn]] lists oxidate feed (S229) pressure as **78 kg/cm²G**, which is inconsistent with the E-2302A/B tube design pressure of **12 kg/cm²g** and the X-2302 filter design of 8 kg/cm²g. The "78" figure is almost certainly a transcription error (likely ~7.8 kg/cm²g or a mmHg value). **Verify the feed line design pressure / piping class** — it is material to the High Pressure deviation below. See deviation **CDN-N02-#7**.

---

## HAZOP Worksheet

> Risk rankings per [[wiki/hazop/risk-matrix]]. Safeguard adequacy per [[wiki/sources/P-Q-MP-OEMS-005]] and [[wiki/hazop/methodology]] Tables 6.4–6.6.
>
> ✅ **Economic severity category RESOLVED for this study (2026-06-17):** Refinery Operations Ltd. is classified **BU**. Apply the GC ePHA Template v5.0 **BU** economic thresholds — Extreme(5) ≥100 M THB; High(4) 10–<100 M; Medium(3) 1–<10 M; Low(2) 0.1–<1 M; Very Low(1) <0.1 M — per [[wiki/hazop/risk-matrix]]. Economic (Ec) severity is now scored below. Risk ranking uses the **highest** of People/Environment/Economic/Social. Production-loss Ec estimates (#2.1, #5.1) are first-pass values for team validation against actual rate-loss financials.
>
> Likelihood basis: [[wiki/hazop/methodology]] Table 6.3. IPL credit: Tables 6.4–6.6. SIL credit: SIL 1 = −1 level, SIL 2 = −2 levels.

### 1. Flow — No / Low Flow (process oxidate through E-2302A/B → E-2303)

**1.1 Cause:** Loss of oxidate feed from upstream — X-2302A/B feed-filter plugging (PDAH-0301), OXI feed-pump trip, or spurious closure of feed valve UXV-0401 — while SC1.5 steam to E-2303 remains on.

- **1.1.1 Consequence:** Process flow stalls but steam heat input continues → CHP-containing oxidate becomes stagnant and locally overheats in E-2303 (and E-2302 shell) above the ~80 °C decomposition onset → autocatalytic exothermic CHP decomposition → rapid heat + non-condensable (O₂) gas generation → exchanger/line overpressure and rupture → loss of containment of hot CHP → pool fire / vapour cloud explosion, potential multiple fatalities.
  - Without Safeguard — L: 4 | Severity P/En/Ec/S: 5/4/5/4 | **RR: Extreme**
  - Safeguards:
    - 1.1.1.1 **FXSLL-0401A/B/C** (2oo3, SIL 1) low-low feed flow → UC-2301 Concentration ESD: closes UXV-0401 (feed) **and UXV-0501/0502 (SC1.5 steam isolation)** — removes heat source on loss of flow. — IL/ESD: **Yes** — IPL=1 — [[wiki/instruments/cause-effect-cdn]] Cause 1
    - 1.1.1.2 **TXSHH-0502A/B** (1oo2, SIL 1) high-high steam-heater tube/oxidate temp → UC-2301 closes UXV-0501/0502 (independent backup catching the resulting overheat). — IL/ESD: **Yes** — IPL=1 — Cause 3
    - 1.1.1.3 PDAH-0301 filter high-ΔP DCS alarm (early warning of plugging) + operator response. — IL/ESD: No — IPL=1 (alarm + operator, >1 min safety time) [VERIFY response time vs CHP onset]
  - With Existing Safeguard — L: 2 | Severity P/En/Ec/S: 5/4/5/4 | **RR: Medium**
  - Recommendation: **R-001** (LOPA / SIF integrity confirmation for the S5 CHP-overheat consequence)
  - After Recommendation Comp. — *(fill at action close-out)*

**1.2 Cause:** Spurious UC-2301 trip closes UXV-0401 with no real demand (nuisance trip) — operability, not a new safety consequence (steam also isolated, safe direction). RR Low; no recommendation.

### 2. Flow — More Flow (process oxidate)

**2.1 Cause:** OXI throughput increase / feed control upset → higher oxidate mass flow through E-2302/E-2303.

- **2.1.1 Consequence:** Reduced heat input per unit mass → feed reaches V-2301 colder than target → poorer cumene flash, off-spec concentration, possible CHP carry-forward at lower concentration → production/operability impact; **no over-temperature hazard** (safe direction for CHP).
  - Without Safeguard — L: 3 | Severity P/En/Ec/S: 1/1/2/1 | **RR: Low** `[Ec: BU — production loss est. 0.1–<1 M THB → Ec 2]`
  - Safeguards: FIC-0501 feed-forward steam control raises duty with flow; downstream V-2301 temperature/level controls.
  - With Existing Safeguard — L: 2 | Severity: 1/1/2/1 | **RR: Low**
  - Recommendation: None — risk acceptable.

### 3. Flow — Reverse Flow

**3.1 Cause:** Reverse flow on the pumped, high-driving-pressure feed line.

- **3.1.1** N/A — not credible: feed is delivered under positive pump pressure from OXI; no credible downstream source to reverse the process flow within node boundaries. (Steam-condensate reverse flow addressed under #8/#9 level and #10 service failure.)

### 4. Temperature — More / High Temperature  ⭐ dominant node hazard

**4.1 Cause:** E-2303 steam control fails to maximum heat input — FIC-0501 / FXY-0501 malfunction or steam control valve fails open → excess SC1.5 steam.

- **4.1.1 Consequence:** Oxidate heated above CHP decomposition onset (~80 °C) → autocatalytic exothermic decomposition in E-2303 shell and downstream → heat + O₂ gas evolution → overpressure, exchanger/piping rupture, LOPC of hot CHP → fire / explosion, potential multiple fatalities.
  - Without Safeguard — L: 4 | Severity P/En/Ec/S: 5/4/5/4 | **RR: Extreme**
  - Safeguards:
    - 4.1.1.1 **TXSHH-0502A/B** (1oo2, SIL 1) high-high oxidate temp → UC-2301 closes UXV-0501/0502 (SC1.5 steam). — IL/ESD: **Yes** — IPL=1 — Cause 3
    - 4.1.1.2 **TXAHN-0502** DCS critical high-temp alarm → operator manually cuts steam / trips. — IL/ESD: No — IPL=1 (alarm + operator) [VERIFY transmitter independence from TXSHH-0502]
    - 4.1.1.3 **UXV-0501 + UXV-0502** redundant series steam isolation (final elements; redundant closure). — IL/ESD: **Yes** — credit embedded in 4.1.1.1
  - With Existing Safeguard — L: 2 | Severity: 5/4/5/4 | **RR: Medium**
  - Recommendation: **R-001**
  - After Recommendation Comp. — *(fill at action close-out)*

**4.2 Cause:** E-2302A/B shell-side hot OXI recirculate abnormally hot (upstream OXI temperature excursion) → over-preheat of feed before E-2303.

- **4.2.1 Consequence:** Same CHP over-temperature / decomposition chain as 4.1.1, initiated on the preheat side.
  - Without Safeguard — L: 3 | Severity: 5/4/5/4 | **RR: High**
  - Safeguards:
    - 4.2.1.1 **TXSHH-0501** (1oo1, SIL 1) high-high E-2302 oxidate outlet temp → UC-2301 Concentration ESD. — IL/ESD: **Yes** — IPL=1 — Cause 2
    - 4.2.1.2 **TXAHN-0501** DCS critical alarm + operator. — IL/ESD: No — IPL=1 [VERIFY independence]
    - 4.2.1.3 OXI section temperature control / OXI ESD (cross-trip UC-2201 → UC-2301, Cause 12) — IL/ESD: **Yes** — IPL=1 (1 min delay)
  - With Existing Safeguard — L: 1 | Severity: 5/4/5/4 | **RR: Low**
  - Recommendation: None at node level — but confirm TXSHH-0501 setpoint margin under R-001.

### 5. Temperature — Less / Low Temperature

**5.1 Cause:** Loss of SC1.5 steam (header loss, UXV-0501/0502 spurious close, FIC-0501 fails low) and/or loss of E-2302 preheat (OXI recirculate cold/lost).

- **5.1.1 Consequence:** Cold feed to V-2301 → poor cumene flash, off-spec concentration, column upset, production loss. **Safe direction for CHP** (no decomposition). Possible un-concentrated CHP carry-forward to Flash Column requiring downstream management.
  - Without Safeguard — L: 4 | Severity P/En/Ec/S: 1/1/2/1 | **RR: Medium** `[Ec: BU — production loss est. 0.1–<1 M THB → Ec 2; team to validate vs actual rate-loss financials]`
  - Safeguards: TI/TT-0505 temperature indication + control; downstream V-2301 controls and concentration analyzers.
  - With Existing Safeguard — L: 3 | Severity: 1/1/2/1 | **RR: Low**
  - Recommendation: None — residual Low after operator response; Economic estimate (Ec 2) to be validated by team.

### 6. Pressure — More / High Pressure

**6.1 Cause:** Process (oxidate) side blocked in (e.g., isolated for maintenance with residual CHP) with a heat source present (steam not isolated, fire case, or decomposition) → thermal expansion / decomposition-gas pressurisation of a liquid-full exchanger.

- **6.1.1 Consequence:** Process-side overpressure beyond E-2302 tube (12) / E-2303 shell (3.5 FV) rating → exchanger rupture → LOPC of CHP → fire/explosion.
  - Without Safeguard — L: 3 | Severity: 5/4/5/4 | **RR: High**
  - Safeguards:
    - 6.1.1.1 In normal lineup the process side is open to V-2301 and relieves via **PSV-23-0401A/B/C/D** on the column (set 2.10/2.205 kg/cm²g, DIERS runaway case). — IL/ESD: No — IPL=2 (PRV sized for scenario) — [[wiki/instruments/pressure-relief-valves-cdn]]
    - 6.1.1.2 High-temp SIFs (4.1.1.1 / 4.2.1.1) cut the heat source before decomposition-driven pressure develops. — IL/ESD: **Yes** — IPL=1
  - With Existing Safeguard — L: 2 | Severity: 5/4/5/4 | **RR: Medium**
  - **Gap:** No dedicated PSV identified on E-2302A/B or E-2303 process side for the **block-isolated maintenance case** (when isolated from V-2301's relief). Recommendation: **R-003**
  - After Recommendation Comp. — *(fill at action close-out)*

**6.2 Cause:** SC1.5 steam supply overpressure into E-2303 tube / condensate system (steam header excursion).

- **6.2.1 Consequence:** Steam-side (tube 7 kg/cm²g, D-2308 7 kg/cm²g) overpressure → tube or drum overpressure → LOPC of steam/condensate (low chemical hazard) but possible escalation to process side via tube failure (see #11).
  - Without Safeguard — L: 3 | Severity: 2/1/2/1 | **RR: Low**
  - Safeguards: **PSV-23-0501** on D-2308 (set 7.0 kg/cm²g, fire case, 157 kg/h) protects the condensate/tube circuit. — IL/ESD: No — IPL=2 — [[wiki/instruments/pressure-relief-valves-cdn]]
  - With Existing Safeguard — L: 1 | Severity: 2/1/2/1 | **RR: Very Low**
  - Recommendation: Confirm PSV-23-0501 relief path also covers a steam-supply overpressure (not only fire case) into the closed tube circuit — note under R-003.

### 7. Pressure — Less / Low Pressure / Vacuum

**7.1 Cause:** Steam-side vacuum on trip — sudden steam isolation (UXV-0501/0502 close) collapses steam in E-2303 tubes → vacuum / potential condensate-induced water hammer.

- **7.1.1 Consequence:** Vacuum collapse / water hammer in E-2303 tube bundle → tube mechanical damage → progression to tube leak (#11).
  - Without Safeguard — L: 3 | Severity: 2/1/2/1 | **RR: Low**
  - Safeguards: E-2303 tube rated for Full Vacuum (design FV); D-2308 design FV. — IPL: inherent design (not a creditable active IPL but eliminates the failure mode).
  - With Existing Safeguard — L: 2 | Severity: 2/1/2/1 | **RR: Low**
  - Recommendation: None — verify no vacuum-breaker requirement given FV-rated design.

**7.2** Process-side low pressure — covered by FV-rated design; not credible to damage. N/A.

### 8. Level — More / High Level (D-2308 condensate drum)

**8.1 Cause:** LIC-0502 / LV-0502 condensate return control fails closed, or condensate return header backpressure → D-2308 level rises.

- **8.1.1 Consequence:** Condensate backs up into E-2303 tube bundle → flooding → loss of steam heat-transfer area → erratic / low feed temperature to V-2301 (links to #5); potential condensate-induced water hammer.
  - Without Safeguard — L: 4 | Severity: 2/1/2/1 | **RR: Medium**
  - Safeguards: **LAH-0502** high-level DCS alarm + operator; LIC-0502 control; HLL 740 mm lockout reference. — IL/ESD: No — IPL=1 (alarm + operator)
  - With Existing Safeguard — L: 3 | Severity: 2/1/2/1 | **RR: Low**
  - Recommendation: None — risk acceptable.

### 9. Level — Less / Low Level (D-2308 condensate drum)

**9.1 Cause:** Excess condensate pump-out / loss of condensate make (steam off) / LV-0502 fails open → D-2308 level falls.

- **9.1.1 Consequence:** P-2308A/B lose suction (NPSH) → cavitation / steam blow-through to condensate return system; possible pump damage.
  - Without Safeguard — L: 4 | Severity: 2/1/2/1 | **RR: Medium**
  - Safeguards: **LAL-0502** low-level alarm + operator; LLL 260 mm reference; FY-0502 auto-start logic is for pump-fail (flow), not level. P-2308 sealless mag-drive (no seal leak path). — IL/ESD: No — IPL=1
  - With Existing Safeguard — L: 3 | Severity: 2/1/2/1 | **RR: Low**
  - Recommendation: None — risk acceptable. (Consider whether LALL/auto-stop on D-2308 is warranted to protect P-2308 — operability, defer to team.)

### 10. Service Failures — Loss of Utility

**10.1 Cause:** Loss of electrical power → P-2308A/B both stop.

- **10.1.1 Consequence:** Condensate accumulates in D-2308 → backs into E-2303 (as #8.1.1) → low/erratic feed temperature; no direct CHP hazard. P-2308 are not on reliable power (Type L, condensate service).
  - Without Safeguard — L: 4 | Severity: 2/1/2/1 | **RR: Medium**
  - Safeguards: LAH-0502 alarm; standby pump auto-start (FY-0502) — ineffective on total power loss; UC-2301 ESD on associated trips removes steam. — IPL=1 (alarm + operator)
  - With Existing Safeguard — L: 3 | Severity: 2/1/2/1 | **RR: Low**
  - Recommendation: None.

**10.2 Cause:** Loss of instrument air → FIC-0501 steam control valve and LV-0502 go to fail position.

- **10.2.1 Consequence:** Depends on fail-action. If steam valve fails open → High Temperature (#4.1). If fails closed → Low Temperature (#5.1).
  - **Action:** Confirm fail-safe action of the SC1.5 steam control valve (FV-0501) and LV-0502 on the control-valve register. — see **R-002 note / R-003**. [VERIFY fail action — [[wiki/instruments/control-valves-cdn]]]

**10.3 Cause:** Loss of SC1.5 steam — covered under #5.1 (Low Temperature).

### 11. Composition / As Well As — Tube Leak / Tube Rupture (exchanger-specific)

**11.1 Cause:** E-2303 tube leak/rupture between SC1.5 steam (tube) and oxidate (shell, CHP).

- **11.1.1 Consequence:** Process (oxidate, ~8 kg/cm²g) leaks into the lower-pressure steam-condensate side → **CHP migrates to the steam-condensate system (D-2308 → condensate return 66-0056), which is not rated/monitored for CHP** → uncontrolled CHP in a utility system, off-site migration, potential decomposition/fire; conversely water/steam ingress into CHP oxidate introduces contamination.
  - Without Safeguard — L: 3 | Severity P/En/Ec/S: 4/3/4/3 | **RR: High**
  - Safeguards: 304L SS tubes (corrosion resistant to CHP); helium leak test at construction (one-time, **not** an operating IPL → IPL=0); periodic inspection (non-IPL per Table 6.6). **No on-line CHP/hydrocarbon detection on D-2308 condensate identified.**
  - With Existing Safeguard — L: 3 | Severity: 4/3/4/3 | **RR: High**
  - Recommendation: **R-002** (condensate contamination detection)
  - After Recommendation Comp. — *(fill at action close-out)*

**11.2 Cause:** E-2302A/B tube leak/rupture between fresh oxidate (tube, 12 kg/cm²g) and hot OXI recirculate (shell, 3.5 FV).

- **11.2.1 Consequence:** HP tube side leaks to LP shell side → shell overpressure; both fluids CHP-containing (chemically similar, lower contamination concern) but pressure differential and CHP inventory mixing. Relief via shell-side path / V-2301 system.
  - Without Safeguard — L: 3 | Severity: 3/3/3/2 | **RR: Medium**
  - Safeguards: 304L SS tubes; shell relief path to OXI / column system; high-temp SIFs limit escalation.
  - With Existing Safeguard — L: 2 | Severity: 3/3/3/2 | **RR: Low**
  - Recommendation: None — confirm shell-side overpressure relief adequacy under R-003.

### 12. Composition — Other Than (Contamination)

**12.1 Cause:** Iron/transition-metal or acid contamination of the CHP oxidate (e.g., corrosion products, upstream carryover) — potent CHP decomposition catalysts.

- **12.1.1 Consequence:** Catalysed CHP decomposition at lower temperature than expected → localized exotherm → as #4.1.1.
  - Without Safeguard — L: 2 | Severity: 5/4/5/4 | **RR: Medium**
  - Safeguards: 304L SS wetted parts throughout node (no Cu/Cu-alloy, no carbon steel in CHP service per [[wiki/hazards/cumene-hydroperoxide]]); X-2302 feed filters remove particulates upstream (Node 23-01); high-temp SIFs. — IPL=1 (material selection is inherent/passive)
  - With Existing Safeguard — L: 1 | Severity: 5/4/5/4 | **RR: Low**
  - Recommendation: None — confirm condensate/contamination monitoring under R-002.

### 13. "Other" Checklist Items

| Topic | Preliminary finding |
|-------|---------------------|
| **Relief scenario** | E-2302A/B & E-2303 process side rely on V-2301 relief in normal lineup; **block-isolated maintenance case not covered by a dedicated PSV** → **R-003**. D-2308 has PSV-23-0501 (fire case) — confirm it also bounds steam-supply overpressure. |
| **Instrumentation** | Two independent SIL 1 SIFs on overheat (TXSHH-0501, TXSHH-0502A/B) — adequacy vs S5 consequence to be LOPA-confirmed (**R-001**). Confirm setpoints sit below 80 °C onset with margin. |
| **Sampling** | No process sample point inside node boundaries identified (SN-2303 etc. are in adjacent nodes). Confirm sampling adequacy with team. |
| **Corrosion** | CHP + Fe catalysis — 304L SS confirmed (process); KCS acceptable on condensate (low CHP) side. OK. |
| **Service failure** | Confirm steam control valve fail-action (#10.2) and P-2308 power supply classification. |
| **Maintenance** | One E-2302 train isolatable while online — confirm safe CHP draining/purging + relief during isolation (**R-003**). |
| **Start-up** | HXS-0102 bypasses FXSLL-0401 during startup — confirm overheat protection (TXSHH-0502) remains active when feed-flow trip is bypassed. **Important — review with team.** |
| **Human factor** | Feed-forward control complexity; alarm response time vs CHP onset (R-001). |

---

## Recommendations Generated (preliminary)

| Rec# | Deviation Row | Description | Risk Rank | Status |
|------|--------------|-------------|-----------|--------|
| R-001 | CDN-N02-#1.1.1, #4.1.1 | Perform LOPA / SIF verification confirming the combined overheat protection (TXSHH-0501 SIL 1 + TXSHH-0502A/B SIL 1 + redundant UXV-0501/0502) achieves tolerable risk for the S5 CHP-decomposition consequence; confirm all TXSHH setpoints sit below the 80 °C CHP decomposition onset with adequate margin and that startup bypass HXS-0102 does not disable temperature protection. | Medium | Open |
| R-002 | CDN-N02-#11.1.1 | Provide on-line detection of CHP/hydrocarbon carryover into the steam-condensate system (e.g., conductivity/pH or hydrocarbon analyzer with alarm, and/or condensate divert) at D-2308 / condensate return, to detect an E-2303 tube leak and prevent migration of CHP to the (unrated) utility condensate system. | High | Open |
| R-003 | CDN-N02-#6.1.1, #11.2.1, #13 | Review overpressure/thermal-relief protection for the E-2302A/B and E-2303 **process (CHP) side when block-isolated for maintenance** (no dedicated PSV identified once isolated from V-2301 relief), and confirm safe CHP draining/purging procedure for single-train isolation. | Medium | Open |
| R-004 | CDN-N02-#7 (Normal Params note) | Resolve the oxidate feed pressure data conflict (S229 listed as 78 kg/cm²G vs E-2302 tube design 12 kg/cm²g / X-2302 8 kg/cm²g) and confirm feed-line design pressure / piping class so the High Pressure deviation is correctly bounded. | Low | Open |

---

## References
- [[wiki/equipment/E-2302AB]], [[wiki/equipment/E-2303]], [[wiki/equipment/D-2308]], [[wiki/equipment/P-2308AB]] — equipment within node
- [[wiki/equipment/V-2301]] — downstream Preflash Column (outlet boundary)
- [[wiki/instruments/cause-effect-cdn]] — UC-2301 Causes 1/2/3 and effects (existing SIS safeguards)
- [[wiki/instruments/sis-cdn]] — SIS architecture
- [[wiki/instruments/pressure-relief-valves-cdn]] — PSV-23-0501 (D-2308), PSV-23-0401 (V-2301)
- [[wiki/instruments/control-valves-cdn]] — steam control valve fail-action (to verify)
- [[wiki/hazards/cumene-hydroperoxide]] — CHP decomposition onset / severity basis
- [[wiki/units/cdn]] — Concentration sub-section design intent and stream data
- [[wiki/hazop/risk-matrix]] — risk ranking criteria (Economic category conflict open)
- [[wiki/hazop/methodology]] — guideword set, IPL credit tables, likelihood guidance
- [[wiki/sources/P-Q-MP-OEMS-005]] — safeguard validation basis
