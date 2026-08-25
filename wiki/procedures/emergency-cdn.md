---
name: CDN Section Emergency Procedures
type: Emergency
unit: CDN
tags: [procedure, emergency, CDN]
sources: [OM-Phenol Unit UOP-2015.pdf]
last_updated: 2026-06-13
---

# CDN Section Emergency Procedures

> ⚠️ CHP is a peroxide — thermal decomposition risk. See [[hazards/cumene-hydroperoxide]].
> ⚠️ The Decomposition section is the most dangerous section of the plant (UOP statement, GOM §XI.D).

**Authority:** UOP General Operating Manual, Rev 8, Section XI — Emergency Procedures.

---

## Scope

This page covers emergency procedures for the CDN (Concentration / Decomposition / Neutralization) section:
- **D. Decomposition Section** (GOM §XI.D) — primary and most critical
- **E. Neutralization Section** (GOM §XI.E)
- Service system failures affecting CDN (GOM §XI.I)
- Concentration/Decomposition shutdown logic (Table XI-1)

For concentration section emergencies: see [[procedures/emergency-concentration]].
For oxidation section emergencies: see [[procedures/emergency-oxi]] (referenced by GOM for explosion/fire/line rupture).

---

## A. "Ready for Feed In" — Prerequisite Conditions

Before restarting decomposer feed after ANY emergency or normal shutdown, ALL five conditions must be met:

| # | Parameter | Required Value |
|---|-----------|---------------|
| 1 | Decomposer Temperature | 70°C |
| 2 | H₂SO₄ (sulfuric acid) in circulating liquid (bulk) | 300 wt ppm minimum |
| 3 | Water concentration in circulating liquid | <2 wt% |
| 4 | Water injection rate | 0 kg/h (stopped) |
| 5 | Decomposer feed line | Flushed with fresh cumene |

> These conditions ensure the decomposition reaction is controlled before concentrated CHP enters the system. Do NOT attempt to restart with acid below 300 wt ppm.

[Source: OM-Phenol Unit UOP-2015.pdf, §XI.D, UOP licensor]

---

## B. Decomposition Section Emergencies

### B.1 Loss of Feed to Decomposer

**Situation:** Flash column bottoms pump lost — no feed to decomposer.

**Risk:** Low. Decomposer goes on internal recycle (dehydrator effluent returns to decomposer). Main risk is handled in concentration section emergency procedures.

**Response:**
1. Stop water injection immediately.
2. Maintain H₂SO₄ injection at current normal rate until bulk acid concentration reaches 300 wt ppm.
3. Increase decomposer temperature (via TIC) to 70°C.
4. Hold at "ready for feed in" conditions until feed is restored.

---

### B.2 Loss of Decomposer Circulation

**Situation:** Decomposer circulation pump failure.

**Automatic response sequence:**
1. Low circulation flow → spare decomposer circulation pump auto-starts (auto-start on low flow switch on elbow tap flow meter).
2. If spare fails and circulation continues to decrease → ESD triggers on low differential pressure across [[equipment/E-2307]] (Decomposer Cooler).
3. ESD shuts unit down immediately; flash column bottoms goes to oxidation section on long circulation.

**Operator response:**
- Return decomposition section to "ready for feed in" conditions.
- Investigate pump failure; restart when spare is available.

---

### B.3 Loss of or Excessive Calorimeter Delta T's

**Critical context:**
- Two calorimeters are installed: Calorimeter 1 and Calorimeter 2 ([[equipment/X-2308]])
- 1st stage (inlet) ΔT ∝ CHP concentration (~7.2°C per wt% CHP)
- 2nd stage (total) ΔT ∝ DCP + residual CHP
- H₂SO₄ at calorimeter 2nd stage must be 4000–6000 wt ppm (local) for full DCP conversion

> Any anomalous ΔT must be investigated immediately. Loss of ΔT can indicate a very dangerous situation.

Lab analysis of circulating liquid should be taken at first sign of any ΔT anomaly.

---

#### Scenario 3.4: Loss of 1st Stage ΔT — 2nd Stage Lost

**Diagnosis:** No reaction in calorimeters. Two possible causes:
- (a) Low/zero CHP and DCP in system (startup condition — not dangerous)
- (b) Decomposition reaction severely hindered (dangerous)

**Response:**
1. Check H₂SO₄ injection system is working. Confirm bulk acid ≥ 20 wt ppm.
2. Check decomposer liquid for residual CHP, DCP, and water concentration.
3. If acid OK and organics in range: check for excess water (reduce injection) or low feed CHP (increase flash column bottoms CHP concentration).
4. **If acid < 20 wt ppm:** STOP — see Section B.12 critical actions below. Do NOT add acid rapidly.

---

#### Scenario 3.5: Loss of 1st Stage ΔT — 2nd Stage OK

**Diagnosis:** Most common cause is unnoticed increase in acid concentration.

**Response:**
1. Confirm via laboratory analysis.
2. Check instrumentation.
3. Verify water concentration in circulating liquid is not excessive.
4. Carefully lower acid concentration to restore 1st stage ΔT to normal.

---

#### Scenario 3.6: Loss of 1st Stage ΔT — 2nd Stage Excessive

**Diagnosis:** H₂SO₄ in bulk is too low → residual CHP reaching 2nd stage with DCP.

**Risk:** HIGH

**Response:**
1. Gradually increase H₂SO₄ injection to raise bulk acid concentration.
2. Confirm with laboratory analyses before each operational action.
3. Note: this may also occur during startup if DCP is formed in excess — monitor and ensure CHP concentration reaches normal level quickly.

---

#### Scenario 3.7: 1st Stage ΔT OK — 2nd Stage Lost

**Diagnosis:** H₂SO₄ injection to calorimeter cut off (plug in line, flow meter error, pump failure).

**Response:**
1. Increase H₂SO₄ injection to bulk liquid to compensate.
2. Locate and rectify problem immediately (plug, flow meter, pump).
3. **Do not operate without calorimeters.** If calorimeter cannot be restored: shut down and restart when acid is available.

Note: could also indicate low DCP concentration in circulating liquid (low DMPC in feed from turndown) — monitor to confirm acid supply not cut off.

---

#### Scenario 3.8: 1st Stage ΔT OK — 2nd Stage Excessive

**Diagnosis:** High DMPC concentration in concentrated oxidizer product → high DCP in circulating liquid.

**Risk:** Low (not emergency, but monitor).

---

#### Scenario 3.9: Excessive 1st Stage ΔT — 2nd Stage Lost

**Diagnosis:** High CHP in circulating liquid (dangerous) + one acid injection point lost.

**Risk:** HIGH

**Response:**
1. Increase H₂SO₄ concentration in circulating liquid carefully.
2. Target: bring 1st stage ΔT down; bring 2nd stage ΔT up to normal.
3. Confirm all acid injection parameters are correct.

---

#### Scenario 3.10: Excessive 1st Stage ΔT — 2nd Stage OK

**Diagnosis:** CHP concentration in circulating liquid is increasing.

**Risk:** VERY SERIOUS

**Response:**
1. Check for excess water (analyze, reduce injection if necessary).
2. Check feed CHP concentration (analyze, increase if required).
3. If bulk acid is low (<20 wt ppm): **increase H₂SO₄ injection VERY GRADUALLY** to bring bulk acid to >40 wt ppm. Key: slow increase. Rapid acid addition with high CHP → relief event risk.

---

#### Scenario 3.11: Excessive 1st Stage ΔT — 2nd Stage Excessive

**Diagnosis:** Decomposition reaction not proceeding to completion. Unreacted CHP building up in system.

**Risk:** DANGEROUS

**Response:**
1. Slightly increase H₂SO₄ injection by 5–10% of current rate.
2. If acid <20 wt ppm: increase SLOWLY — risk of sudden uncontrolled decomposition of accumulated CHP.
3. Goal: gradually bring bulk acid to ≥40 wt ppm, which should restore normal ΔT pattern.

---

### B.12 Loss of Sulfuric Acid Injection

#### Partial Loss (to one calorimeter only)
- Increase H₂SO₄ injection to bulk liquid to compensate.
- Restore acid to affected calorimeter as soon as possible.
- Do not operate long-term with only bulk acid injection — CHP monitoring becomes impossible.

#### Complete Loss
- Automatic ESD initiates immediately.
- UOP recommendation: **Do not restart decomposer without at least one calorimeter online.**
- Go to "ready for feed in" conditions and await acid restoration.

> Running without calorimeters: circulating CHP concentration cannot be monitored. Upsets may not be visible until it is too late.

#### H₂SO₄ < 20 wt ppm — Critical Condition
If acid falls below 20 wt ppm and CHP is elevated:
1. Do NOT add acid rapidly — uncontrolled reaction/relief event risk.
2. Go on long recycle immediately.
3. Flush decomposer feed line.
4. Recalibrate H₂SO₄ flow meters and instruments.
5. SLOWLY return to "ready for feed in" conditions while instruments are repaired.

---

### B.13 Loss of Dehydrator Heating Media

**Two options based on duration:**

**Option A — Heating media unavailable short-term:**
- Put decomposition section on long recycle.
- Return decomposer circulating stream to "ready for feed in" conditions.
- Await return of heating media.

**Option B — Heating media unavailable for extended period:**
- Run decomposition in "complete conversion" mode (return to startup-like severity).
- Increase decomposition severity to reduce CHP to zero in circulating stream.
- Caution: residue make increases, economic performance decreases.

> ⚠️ **UNDER NO CIRCUMSTANCES SHOULD APPRECIABLE QUANTITIES OF CHP BE SENT TO THE FRACTIONATION SECTION.**

---

### B.14 Loss of Cooling Water to Dehydrator Cooler

**Risk:** High temperatures to direct neutralization section → increased byproduct make + yield loss (diamine reacts with acetone at elevated temperature). Increased organic losses from fractionation feed tank vent.

**Response:**
1. Stop feed to decomposition section.
2. Put synthesis section (oxidation) on long recycle.
3. Return decomposition section to "ready for feed in" conditions.
4. Await return of cooling water to dehydrator cooler.

---

### B.15 Explosion or Fire

Refer to oxidation section emergency procedures: [[procedures/emergency-oxi]].

### B.16 Line Rupture or Serious Leak

Refer to oxidation section emergency procedures: [[procedures/emergency-oxi]].

---

## C. Neutralization Section Emergencies

**General:** Neutralization is not subject to process emergencies except mechanical failure. Operational problems are not classified as emergencies, but lack of neutralization must not be ignored.

**Consequence of failed neutralization:** Excess yield loss + corrosion.

### C.1 Inability to Neutralize Crude Product

**Troubleshooting sequence:**
1. Check diamine injection pump — is it pumping correctly?
2. Check diamine tank — is it empty?
3. Calibrate the field pH transmitter.
4. Check H₂SO₄ concentration in crude product — is it higher than normal?

**If pH cannot be corrected despite all effort:**
- Stop feed to decomposition section.
- Put synthesis section on long recycle.
- Return decomposition to "ready for feed in" conditions.
- Await resolution.

### C.2 Explosion or Fire / C.3 Line Rupture or Serious Leak

Refer to [[procedures/emergency-oxi]].

---

## D. Service System Failures — CDN Impact

### D.1 Power Failure

**Emergency generator priority sequence for CDN:**

| Priority | Equipment | Reason |
|----------|-----------|--------|
| 1 | Oxidizer Circulation Pumps | CHP cooling — highest priority |
| 2 | Concentration Flash Column Bottoms Pumps | Prevents CHP holdup at high temperature |
| 3 | Oxidizer Fresh Feed Pumps | Dilution of CHP if needed |
| 4 | Emergency Cooling Water Supply | Oxidizer cooling backup |

**Notes:**
- Battery power maintains all electrical instrumentation automatically and instantaneously.
- Control room lighting should be on 24/7 — any flicker = check entire plant for tripped equipment immediately.
- After power blip: survey entire unit for isolated equipment. Fin-fan motor trips are not always alarmed.
- For extended power failure: use emergency power generator (usually auto-start) to restart above equipment in sequence.

### D.2 Loss of Chilled Water

**CDN impacts:**
- Preflash/Flash Column Vacuum System: may require turndown or shutdown if pressure rises and cuts heat to flash column → put synthesis on long recycle.
- FAC Venting: increased acetone losses to vent; possible vacuum system pressure control problems affecting fractionation.

### D.3 Steam Failure

**Critical for CDN:** Steam to concentration section ejectors — failure requires immediate shutdown of concentration section.

### D.4 Nitrogen Failure

- Does not directly interrupt CDN operation.
- Critical for purging during oxidation section emergencies — restore as soon as possible.

---

## E. Concentration/Decomposition Automatic Shutdown Logic (Table XI-1)

### Causes and Actions

| Cause Tag | Service | Actions Triggered |
|-----------|---------|------------------|
| FSLLA/B | Feed to Preflash Column | 1, 2, 3, 11 |
| TSHH | Preflash Column Feed-Oxidate Exchanger Tub Liquid | 1, 2, 3, 11 |
| TSHH | Preflash Column Steam Heater Tub Liquid | 1, 2, 3, 11 |
| TSHH | Preflash Column Bottoms | 1, 2, 3, 11 |
| LSHH | Flash Column Bottoms | 1, 2, 3, 11 |
| LSHH | Preflash Column Bottoms | 1, 2, 3, 11 |
| PSHH | Preflash/Flash Column Overhead Vapor | 4, 11 |
| TSHH | Flash Column Vaporizer Vapor Space/Outlet (1) | 1, 2, 3, 5, 6, 9, 11 |
| TSHH | Flash Column Vaporizer Vapor Space/Outlet (2) | 1, 2, 3, 5, 6, 8, 11 |
| TSHH | Flash Column Bottoms | 1, 2, 3, 5, 6, 7, 9, 11 |
| TSHH | Flash Column Bottoms Pump Suction | 1, 2, 3, 5, 6, 7, 11 |
| TSHH | Oxidizers (for cascaded reliable CW only) | 3, 10 |
| LSHH | Oxidation Decanter | 3 |
| HS | Concentration Section Emergency Shutdown | 1, 2, 3, 5, 6, 11 |
| FSLLA/B | Decomposer Feed | 12, 13 |
| LSHH | Decomposer | 12, 13 |
| TSHH | Decomposer | 12, 13 |
| TSLL | Decomposer | 12, 13 |
| TSHH | Dehydrator Effluent | 12, 13 |
| FSLLA/B | Acid Injection | 12, 13 |
| PDSLLA/B | Decomposer Cooler (Circulation) | 12, 13 |
| TDSHH | Calorimeter 1 Total Delta T | 12, 13 |
| TDSHH | Calorimeter 1 Inlet Delta T | 12, 13 |
| TDSHH | Calorimeter 2 Total Delta T | 12, 13 |
| TDSHH | Calorimeter 2 Inlet Delta T | 12, 13 |
| FSLLA/B | Circulating Liquid to Calorimeter Systems | 12, 13 |
| UC | Concentration Section Shutdown | 12, 13 |
| HS | Decomposition Section Shutdown (pushbutton) | 12, 13 |
| PSLL | Process Water to Decomposer | 14 |
| HS | Steam to Dehydrator Enable/Shutoff | 15 |

### Action Definitions

| Action | Description |
|--------|-------------|
| 1 | Stop feed to PFC; drain & flush upstream of PFC FCV; cumene quench to PFC heater tubs and FC vaporizer |
| 2 | After time delay: close cumene flush upstream of PFC FCV |
| 3 | Immediately: stop steam to PFC heater and FC vaporizer; vent steam/condensate from PFC heater and FC vaporizer; trip decomposition section. Vent condensate pot; stop condensate pump if applicable |
| 4 | After time delay: stop steam to PFC heater and FC vaporizer; vent steam/condensate; trip decomposition section. Vent condensate pot; stop condensate pump if applicable |
| 5 | Start cumene quench to flash column collector tray |
| 6 | After time delay: stop cumene quench to flash column collector tray |
| 7 | Start cumene quench to flash column bottoms |
| 8 | Immediately: start reliable CW quench to/from flash column vaporizer; close condensate from flash column vaporizer |
| 9 | After time delay: start reliable CW quench to/from flash column vaporizer; close condensate from flash column vaporizer |
| 10 | Stop reliable CW to concentration section |
| 11 | Trip oxidation section |
| 12 | Stop feed to decomposer; stop steam to dehydrator; divert dehydrator effluent back to decomposer; stop water to decomposer; divert recycle cumene and flash column to terminal oxidizer via long circulation line; stop cumene flush to long circulation line |
| 13 | After time delay: cumene flush to decomposer feed line; cumene flush of decomposer feed control valve between isolation valves |
| 14 | Close decomposer water injection isolation valve |
| 15 | Manually shut off steam to dehydrator (even when rest of logic allows it) |

[Source: OM-Phenol Unit UOP-2015.pdf, Table XI-1, UOP licensor]

---

## F. Decomposer-Specific ESD Hardware

- Two automatic shutdown valves isolate concentrated CHP feed from decomposer: one upstream and one downstream of decomposer feed FCV.
- On decomposer shutdown: CHP from flash column bottoms mixes with flash column overhead recycle cumene → circulates to terminal oxidizer.
- Cumene flush drum: flushes isolated piping around decomposer feed FCV back to terminal oxidizer via long circulation line. Also flushes long circulation line clear of CHP following startup.
- Decomposer water injection stops automatically on shutdown (excess water inhibits cleavage reaction).

**Decomposer auto-start:** Spare decomposer circulation pump starts automatically on low flow switch signal on decomposer circulation elbow tap flow meter.

---

## Alarms to Watch During CDN Emergency

| Alarm Tag | Parameter | Setpoint | Action |
|-----------|-----------|---------|--------|
| TSLL Decomposer | Decomposer temperature low | 57°C | Immediate ESD |
| TSHH Decomposer | Decomposer temperature high | TBC | Immediate ESD |
| TSHH Dehydrator Effluent | Dehydrator outlet temperature high | TBC | Decomposer ESD |
| TDSHH Cal 1 Total ΔT | Calorimeter 1 total delta T high | TBC | Decomposer ESD |
| TDSHH Cal 1 Inlet ΔT | Calorimeter 1 inlet delta T high | TBC | Decomposer ESD |
| TDSHH Cal 2 Total ΔT | Calorimeter 2 total delta T high | TBC | Decomposer ESD |
| TDSHH Cal 2 Inlet ΔT | Calorimeter 2 inlet delta T high | TBC | Decomposer ESD |
| FSLLA/B Acid | Acid injection low-low flow | TBC | Decomposer ESD |
| PDSLLA/B | Decomposer cooler DP low-low | TBC | Decomposer ESD |
| AAL-1701 | Low H₂SO₄ concentration (AT-1701) | TBC | Investigate immediately |

[TBC setpoints: obtain from plant instrument data sheets or SIS logic diagrams]

---

## References

- [[sources/om-phenol-uop-2015]] — UOP GOM Section XI (primary source)
- [[parameters/cdn-operating-windows]] — Operating limits referenced in this procedure
- [[units/cdn]] — CDN section overview
- [[equipment/D-2304]] — Decomposer Drum
- [[equipment/E-2307]] — Decomposer Cooler (PDXSLL ESD trigger)
- [[equipment/X-2308]] — Calorimeters
- [[equipment/V-2301]] — Flash Column
- [[instruments/sis-cdn]] — UC-2302 safety system
- [[hazards/cumene-hydroperoxide]]
- [[procedures/normal-shutdown-cdn]]
- [[procedures/emergency-oxi]] — Referenced for explosion/fire/line rupture
