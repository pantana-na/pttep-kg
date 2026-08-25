---
name: HAZOP Methodology — SG-(Q-MP)-014 R3
tags: [hazop, methodology, guidewords, ipl, workflow]
source: SG-(Q-MP)-014_R3.pdf
last_updated: 2026-06-14
---

# HAZOP Methodology — PTT GC Study Execution Guide

> **Governing Document:** SG-(Q-MP)-014 Rev.3 (26/05/2026) — Guidance for Hazard and Operability Studies
> **Source file:** `raw/standards/SG-(Q-MP)-014_R3.pdf`
> **Source summary:** [[wiki/sources/SG-Q-MP-014]]

This page captures the complete execution methodology from §5.3.3 plus all reference tables from §6.3 and §6.4. It is the primary reference during HAZOP node analysis.

---

## Team Requirements (§5.2.5)

| Role | Minimum Qualification |
|------|-----------------------|
| Leader | ≥ 8 years O&G/petrochemical experience; independent from design, EPC, and VP Operation management line |
| Scribe | Dedicated role — NOT a team member, NOT the leader |
| Process Engineer | Member — minimum requirement |
| Operations Supervisor | Member — minimum requirement |
| Maintenance Engineer | Member |
| Safety Engineer | Member |

---

## Risk Ranking Reference

**RAM:** Use [[wiki/hazop/risk-matrix]] for all Severity, Likelihood, and Risk rankings.
**Acceptable risk for GC:** Low or Very Low only.
**Mitigated risk ≥ Medium:** must generate a recommendation.

---

## HAZOP 9-Step Methodology (§5.3.3)

### Step 1 — Node Selection and Design Intention

- Node boundaries set exclusively by the experienced engineer's markup on the P&ID
- LLM reads the marked-up P&ID and faithfully records boundaries; never sets boundaries independently
- Agree design intention with team: normal flow, temperature, pressure, composition, phase
- Source design intent from: [[wiki/units/<unit>]] and [[wiki/streams/<id>]]

### Step 2 — Select the Deviation (Parameter-First Approach)

- Apply all parameters from Table 6.1 to each node
- For each parameter, apply all applicable guidewords
- **Full record approach**: if a deviation has no credible cause, record "No credible cause was identified" — do NOT leave blank

### Step 3 — Identify Possible Causes

- Identify causes **within the node boundaries** (first and last nodes may consider outside)
- Use specific equipment tags and instrument tag numbers (e.g., "Malfunction of 13TIC001 leading to fully closing of 13TV003")
- Consider: instrument/control failure, human error, equipment mechanical failure, loss of utilities, upstream/downstream upsets

### Step 4 — Develop Potential Consequence (Unmitigated)

- Describe consequence WITHOUT credit to any safeguard — as if no protection exists
- Describe "step by step" chain leading to final consequence using linking words (e.g., "leading to", "resulting in", "causing")
- Consequence endpoints: fatality, LTI, environmental release, fire/explosion, equipment damage, production loss

### Step 5 — Evaluate Initial Risk

- Assign Severity (1–5) per [[wiki/hazop/risk-matrix]] PEES categories
- Assign Likelihood (1–5) based on frequency of the CAUSE occurring — NO safeguard credit
- Use likelihood guidance in Table 6.3 below
- Look up Initial Risk in the 5×5 matrix

### Step 6 — Identify Existing Safeguards

- List all safeguards that Detect, Decide, or Act on the deviation
- Record **prevention safeguards first**, then mitigation safeguards
- For each safeguard record: equipment tag + what it does + how it protects + setpoint (if applicable)
- **Do NOT record** active fire protection (sprinklers, firewater) or emergency response as safeguards — these are generally post-event with uncertain effectiveness
- **IPL candidates** must be Effective, Independent, and Auditable — use Table 6.4/6.5 for credit

### Step 7 — Evaluate Mitigated Risk

- **Severity stays the same** — do not change from Step 5
- Re-assess Likelihood with safeguards applied — use IPL credit from Table 6.4 (Active) and Table 6.5 (Passive)
- Non-IPL safeguards per Table 6.6 receive NO likelihood reduction
- Look up Mitigated Risk in the 5×5 matrix

### Step 8 — Develop Recommendation

- If Mitigated Risk = Medium/High/Extreme → **must generate a recommendation** (Rec#)
- May also recommend at Low/Very Low (voluntary improvement, per HAZOP lead judgment)
- Wording: start with action verb (Add, Change, Configure, Provide, Update, Prepare) and explain why
- Record in [[wiki/hazop/action-register]]

### Step 9 — HAZOP Worksheet Reference

- Never use "See above", "Same as above", "Same as earlier node"
- Use specific reference numbers for previous deviations (e.g., CDN-N01-#3, CDN-N01-#7)
- Copy content rather than cross-referencing if content is substantially the same

---

## Node Preparation Guidance

### Node Size Trade-off
| Node Size | Pros | Cons |
|-----------|------|------|
| Big (broad boundary) | Saves study time | Team confusion; risk of missing hazards |
| Small (narrow boundary) | Easier hazard identification | Very time-consuming; data repetition; team fatigue |

Aim for nodes of roughly similar complexity. Good practice: nodes should not cross from one P&ID to the next.

### Causes NOT Considered Under HAZOP

> These are excluded by convention — do NOT record as HAZOP causes:

| Excluded Cause | Reason |
|----------------|--------|
| Design issues / concerns | Design basis is taken as given |
| PSV or SIF failure | Addressed in SIL assessment; not a HAZOP process cause |
| Pipe flange / gasket leak | Small leak — inspection/maintenance scope; not a deviation initiator |
| Closure of manual valves labelled LO/LC or CSO/CSC | Assumed locked correct per management system |

*Source: [[sources/hazop-leadership-training-ch4]]*

---

## Recording DO / DON'T (Good Practice)

### Causes
- **DO:** "Malfunction of FIC-1302 leading to FV-1302 fully open" / "Pump P-2301A/B stopped"
- **DON'T:** "Control fault" / "Pump faulty" / "No feed flow" (too vague — no equipment tag)

### Consequences
- **DO:** "Reaction runaway causing high pressure & temperature in D-2304 resulting in vessel rupture, LOPC, fire and explosion"
- **DON'T:** "Runaway" / "Overpressure" (no chain; no final outcome stated)

### Safeguards
- **DO:** "TXSHH-0701/0702 (1oo2 SIL 2) trips UXV-0701 to cut SC3 steam to E-2304 on high temperature"
- **DON'T:** "High temperature alarm" / "SIS trip" (no tag, no setpoint, no action)

### Recommendations
- **DO:** "Add independent high-high level transmitter at V-2302 with 1oo2 SIL 1 trip to prevent CHP carryover to P-2307A/B"
- **DON'T:** "Add level transmitter" (no purpose, no protection target stated)

*Source: [[sources/hazop-leadership-training-ch4]]*

---

## Table 6.1 — Parameter × Guideword Matrix (Applicable Deviations)

| Parameter | Guidewords | Deviation Label |
|-----------|-----------|----------------|
| **Flow** | No | No Flow |
| | More | More Flow |
| | Less | Less Flow |
| | Reverse | Reverse Flow |
| | Other than | Misdirected Flow |
| **Pressure** | More | High Pressure |
| | Less | Low Pressure |
| **Temperature** | More | High Temperature |
| | Less | Low Temperature |
| **Level** | No | No Level |
| | More | High Level |
| | Less | Low Level |
| **Reaction** | No / Less | No / Low Reaction |
| | More | Runaway Reaction |
| | Reverse | Reverse Reaction |
| | Other than | Side / Wrong Reaction |
| **Mixing** | No | No Mixing |
| | More | Excessive Mixing |
| | Less | Low Mixing |
| **Phase** | Other than | Phase Change |
| **Viscosity** | More | High Viscosity |
| | Less | Low Viscosity |
| **Composition** | Other than | Composition Change |
| **Erosion / Corrosion** | More | High Corrosion / Erosion |
| **Service Failures** | No / Less | Loss of Service |
| | More | Excess of Service |
| **Sequence** | Other than | Wrong Step |
| **Incidents** | — | Previous / Related Incident |
| **Human Factor** | — | Human Factor |

*Not every parameter applies to every node. If not applicable, record "N/A — not credible at this node" with brief justification.*

### Standard Deviation Set by Equipment Type

| # | Deviation | Column | Vessel | Line | Exchanger | Pump | Compressor |
|---|-----------|:------:|:------:|:----:|:---------:|:----:|:----------:|
| 1 | High Flow | | | ✓ | | ✓ | ✓ |
| 2 | High Level | ✓ | ✓ | | | | |
| 3 | High Interface | ✓ | ✓ | | | | |
| 4 | High Pressure | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 5 | High Temperature | ✓ | ✓ | ✓ | ✓ | | ✓ |
| 6 | High Concentration | ✓ | ✓ | ✓ | | | |
| 7 | Low / No Flow | | | ✓ | | ✓ | ✓ |
| 8 | Low Level | ✓ | ✓ | | | | |
| 9 | Low Interface | ✓ | ✓ | | | | |
| 10 | Low Pressure | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 11 | Low Temperature | ✓ | ✓ | ✓ | ✓ | | |
| 12 | Low Concentration | ✓ | ✓ | ✓ | | | |
| 13 | Reverse / Misdirected Flow | | | ✓ | | ✓ | ✓ |
| 14 | Tube Leak | | | | ✓ | | |
| 15 | Tube Rupture | | | | ✓ | | |
| 16 | Leak | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 17 | Rupture | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |

*Source: [[sources/hazop-leadership-training-ch4]]*

### HAZOP "Other" Checklist Words

In addition to parameter × guideword deviations, consider these at every node:

| Topic | What to Check |
|-------|--------------|
| Relief scenario | All credible overpressure scenarios covered by relief devices? |
| Instrumentation | Missing, incorrect, or mislocated instruments? |
| Sampling | Safe sampling provisions; sample representative? |
| Corrosion | Materials of construction adequate for service? |
| Leakage | Flange, valve, pump seal leak scenarios |
| Service failure | Loss of steam, CW, IA, N₂, power |
| Maintenance | Safe isolation, purging, blinding requirements |
| Start-up | Hazards specific to start-up mode |
| Spare equipment | Standby equipment correctly lined up? |
| Safety equipment | Fire/gas detection, ESD availability and adequacy |

*Source: [[sources/hazop-leadership-training-ch4]]*

---

## Table 6.2 — Cause Guidance by Deviation Type (§6.3, Appendix 6.3)

### No Flow / Low Flow
- Blocked line, plugged strainer/filter, blocked valve (CV or manual)
- Pump/compressor failure (mechanical, loss of suction, cavitation)
- Loss of driving pressure or utility (for flow-driven streams)
- Upstream vessel empty, downstream vessel full
- Instrument failure causing spurious valve closure (control or shutdown)
- Frozen line

### More Flow / High Flow
- CV malfunction (fail-open, or controller malfunction → CV opening)
- Instrument calibration error (low reading → controller opens CV)
- Higher driving pressure upstream
- Parallel line bypass opened
- Human error (operator opens wrong valve)

### Reverse Flow
- Pump failure with no check valve protection
- Upstream low pressure / downstream high pressure reversal
- Two-phase flow causing slug or reverse driving force
- Instrument failure on flow reversal safeguard

### Misdirected Flow
- Wrong valve opened (isolation or switching valve)
- Cross-contamination between lines sharing equipment
- CV on wrong line (incorrect instrument signal)

### High Pressure
- Loss of outlet flow (blocked discharge, closed valve downstream)
- High inlet pressure from upstream upset
- CV malfunction on pressure control loop (fail-closed)
- Tube rupture: high-pressure side to low-pressure side
- External heat source — fire, steam tracing fault, solar gain on blocked-in liquid
- Loss of cooling utility
- Runaway reaction generating non-condensable gas

### Low Pressure / Vacuum
- Condensation of vapor in vessel (loss of temperature → vacuum)
- Blocked inlet / pump failure → vacuum on suction side
- High outlet flow
- Loss of purge or blanket gas
- Instrument failure → draining faster than filling

### High Temperature
- Loss of cooling (utility failure, fouling)
- CV malfunction (cooling service valve fails closed / heating service valve fails open)
- Exothermic runaway reaction
- Excess steam, heat tracing, or fired heater failure
- Flash from hot upstream stream

### Low Temperature
- Loss of heating utility (steam failure, heat tracing failure)
- Cold utilities excessive (cryogenic service)
- Incoming cold stream upstream upset
- Phase change causing temperature drop (evaporation, expansion)

### High Level
- Loss of outlet flow (pump failure, closed valve)
- High inlet flow
- CV malfunction on level control (fail-closed outlet or fail-open inlet)
- Carry-over from upstream vessel
- Interface control failure (liquid carryover vs. vapor)

### Low Level / No Level
- Loss of inlet flow
- Excess outlet flow
- CV malfunction on level control (fail-open outlet or fail-closed inlet)
- Leakage from vessel or associated piping
- Drain valve accidentally opened

### No Reaction / Low Reaction
- Catalyst depletion, poisoning, or deactivation
- Off-spec feed (wrong composition, contaminants)
- Wrong temperature or pressure outside reaction envelope
- Insufficient mixing

### Runaway Reaction
- Loss of cooling / heat removal
- Catalyst over-activity (hot spots)
- Wrong inhibitor concentration or loss of inhibitor
- Off-spec feed (high concentration of reactive species)
- Contamination (water, acid, alkali, oxygen into peroxide systems)

### Reverse Reaction / Side Reaction / Wrong Reaction
- Off-spec feed or wrong composition
- Operating outside normal T, P, or concentration window
- Catalyst contamination or wrong catalyst

### Phase Change (unexpected)
- Pressure drop below bubble point → flashing
- Loss of heating → unexpected solidification or condensation
- High temperature → vaporisation in liquid-filled system → overpressure
- Two-phase flow onset in single-phase design

### Composition Change
- Off-spec feed from upstream process or tank
- Contamination from cross-connection or leaky valve
- Loss of mixing or reaction causing stratification
- Incorrect additive dosing

### High Corrosion / Erosion
- Off-spec pH (acid or caustic excursion)
- High velocity or two-phase flow
- Wrong material of construction or change in service
- Particulate carryover

### Loss of Service / Excess of Service
- Cooling water: fouling, pump failure, loss of supply header pressure
- Steam: header loss, trap failure
- Instrument air: compressor failure, air dryer failure
- Electrical power: power outage, partial load shedding
- Nitrogen: compressor failure, supply exhaustion

### Wrong Step (Sequence)
- Human error during startup/shutdown sequence
- Skipping a step (time pressure, habit, fatigue)
- Simultaneous activation of steps that should be sequential

### Previous / Related Incident
- Similar unit at another site experienced the same event
- Prior near-miss or incident at this plant related to this node

### Human Factor
- Task complexity, ambiguous labelling, alarm flood
- Inadequate training, poor procedure accessibility
- Time pressure, fatigue, simultaneous tasks

---

## Table 6.3 — Likelihood Guidance for Initiating Events (§6.4.2)

| Initiating Event Type | Typical PFD / Frequency | Guidance Likelihood Level |
|----------------------|------------------------|--------------------------|
| BPCS instrument loop (single, independent from cause) | 1 to 1/10 per year | **L4** |
| Human error — routine task (≥ once/week) | ~1 per year | **L5** |
| Human error — periodic task (once/year to once/week) | 1 to 1/10 per year | **L4** |
| Human error — infrequent task (< once/year) | 1/10 to 1/100 per year | **L3** |
| Pressure regulator failure | 1/10 to 1/50 per year | **L4** |
| Pump / fan / compressor mechanical failure | 1 to 1/10 per year | **L4** ¹ |
| Loss of supply (power, steam, cooling water, etc.) | 1 to 1/10 per year | **L4** |
| Site-wide power loss — no history at location | — | **L3** |
| Site-wide power loss — has occurred at location | — | **L4** |
| Site-wide power loss — > once/year at location | — | **L5** |
| Heat exchanger tube leak | 1/30 to 1/100 per year | **L3** |
| Heat exchanger shell leak | 1/3 to 1/10 per year | **L4** |
| Mechanical failure (no moving parts, no vibration, non-corrosive) | 1/50 to 1/100 per year | **L3** |
| Mechanical failure (operated with vibration) | 1 to 1/50 per year | **L4** |
| Partial plug — control valve (dirty fluid) | ~1/3 per year | **L4** |
| Partial plug — filter/strainer | ~1/21 per year | **L3–L4** |
| Partial plug — pipeline mixer | ~1/11 per year | **L4** |
| Partial plug — reboiler tubes | ~1/17 per year | **L4** |

*Use PTTGC location-specific incident history where available to adjust Likelihood per §6.2.1.3.1.*

¹ *Note: Training material [[sources/hazop-leadership-training-ch4]] (2021) assigns pump/compressor failure → L3 (1/10 to 1/100 per year). This governing table (SG-(Q-MP)-014 R3, 2026) assigns L4. Use L4 for this study.*

---

## Table 6.4 — Active IPL Likelihood Reduction Credit (§6.4.3)

| IPL Type | PFD | Likelihood Reduction |
|----------|-----|---------------------|
| BPCS independent loop (independent from cause & initial event) | 0.1 | **1 level** |
| SIF / SIL 1 (PFD 0.1–0.01) | 0.1–0.01 | **1 level** |
| SIF / SIL 2 (PFD 0.01–0.001) | 0.01–0.001 | **2 levels** |
| SIF / SIL 3 (PFD 0.001–0.0001) | 0.001–0.0001 | **3 levels** |
| Alarm + operator response (control room; process safety time > 1 min) | 0.1 | **1 level** |
| Manual field intervention (safety time > 10 min) | 0.1 | **1 level** |
| Routine operator surveillance (sufficient safety time; documented procedure) | 0.1 | **1 level** |
| Adjustable movement-limiting device | 0.1 | **1 level** |
| PRV — properly sized for the specific scenario | 0.01 | **2 levels** |
| PRV — block valve present without management program | 0.1 | **1 level** |
| 3 PRVs — 2 of 3 required for full relief; all valves connected simultaneously | 0.001 | **3 levels** |
| Multiple PRVs — each can independently relieve full load | 0.001 | **3 levels** |
| Multiple PRVs — staged (> 1 needed for full load) | 0.1 | **1 level** |
| Rupture disk | 0.01 | **2 levels** |
| PRV + rupture disk in series | 0.01 | **2 levels** |
| Conservation vent | 0.01 | **2 levels** |
| Vacuum breaker | 0.01 | **2 levels** |
| Pressure reducing regulator | 0.1 | **1 level** |
| Restrictive flow orifice (RFO) | 0.01 | **2 levels** |
| Check valve | 0.1 | **1 level** |
| Captive key / lock system | 0.01 | **2 levels** |
| Multiple mechanical pump seal with leak detection | 0.1 | **1 level** |
| Mechanical over-speed trip | 0.1 | **1 level** |

**IPL must be:** Effective (for this specific scenario), Independent (from cause and from other IPLs in the chain), and Auditable (can be tested to verify functionality).

Maximum combined credit: Likelihood cannot be reduced below Level 1 (Improbable).

---

## Table 6.5 — Passive IPL Likelihood Reduction Credit (§6.4.3)

| IPL Type | PFD | Likelihood Reduction |
|----------|-----|---------------------|
| Flame arrester — end-of-line | 0.01 | **2 levels** |
| Flame arrester — in-line, without temperature monitoring | 0.1 | **1 level** |
| Flame arrester — in-line, with temperature monitoring | 0.01 | **2 levels** |
| Dike / berm / bund (liquid containment) | 0.01 | **2 levels** |
| *Note: Dike is NOT IPL for fire/explosion scenarios* | — | — |
| Drainage to dike with remote impoundment | 0.01 | **2 levels** |
| Permanent mechanical stop (physical travel limit) | 0.01 | **2 levels** |
| Overflow line — no impediment to flow | 0.001 | **3 levels** |
| *Note: Overflow line NOT IPL for fire/explosion* | — | — |
| Overflow line with passive fluid seal or rupture disk | 0.01 | **2 levels** |
| Inherently safe design (elimination of hazard) | 0.01 | **2 levels** |

---

## Table 6.6 — Safeguards That Are NOT IPLs (§6.4.3)

These safeguards are real and should be listed in the worksheet, but they receive **zero likelihood reduction credit**:

| Non-IPL Safeguard | Reason |
|-------------------|--------|
| Training, certification, procedures | Not consistently effective; no PFD basis |
| Normal testing and inspection | Maintenance activity, not a protective function |
| Communications (radio, PA, phone) | Unreliable during emergencies |
| Signs and labels | Insufficient protection alone |
| Active fire protection (sprinklers, firewater deluge) | Generally post-event; does not prevent initiating event |
| Emergency response (fire brigade, ERT) | Post-event; uncertain availability |

---

## Recommendation Recording Format (§6.6)

| Field | Content |
|-------|---------|
| Rec# | Sequential: R-001, R-002, … |
| Node | Node ID |
| Deviation | Parameter + Guideword (e.g., "Temperature — More") |
| Cause | Specific cause from worksheet |
| Consequence | Final consequence from worksheet |
| Initial Risk | S × L before safeguards |
| Safeguards in Place | List from worksheet |
| Mitigated Risk | S × L after safeguards |
| Recommendation | Action verb + description + reason |
| Responsible | Discipline: Process / Instrument / Operations / Mechanical |
| Status | Open / In Progress / Closed / Rejected |

---

## GC HAZOP Worksheet — Official Column Structure

> Source: [[sources/hazop-leadership-training-ch5]] (Chapter 5-4)

The GC HAZOP worksheet uses **two parallel risk blocks** (Without Safeguard / With Existing Safeguard), each containing all four PEES severity sub-columns:

| Column | Sub-columns | Notes |
|--------|-------------|-------|
| Parameter | — | Flow, Temperature, Pressure, Level, Reaction, etc. |
| Deviation | — | e.g., "No Flow", "High Temperature" |
| Possible Cause | — | Root cause within node |
| Potential Consequence | — | Unmitigated consequence chain |
| **Without Safeguard** | L, P, En, Ec, S, RR | Initial risk — L = Likelihood; P/En/Ec/S = PEES severity; RR = Risk Ranking |
| **Existing Safeguard** | Detail | Description of all safeguards |
| **With Existing Safeguard** | L, P, En, Ec, S, RR | Mitigated risk — same columns; Severity unchanged from "Without Safeguard" |
| Recommendation | Detail | Required action if residual risk is Medium or higher |

**PEES severity columns:** P = People, En = Environment, Ec = Economic, S = Social — matches RAM categories in [[hazop/risk-matrix]] (W-(Q-MP)-002 R2).

**Recording tool:** GC e-PHA online system or downloadable GC Excel template. Scribe projects live recording so entire team can see what is recorded.

---

## Study Preparation and Scheduling

> Source: [[sources/hazop-leadership-training-ch5]] (Chapter 5-1)

### Session Planning Rules of Thumb
- Each HAZOP session = **~3.5 hours** (half working day, with breaks)
- One extra session at start for: team introductions + methodology/ground rules refreshment
- Then **one session per P&ID** of average complexity or per major unit operation/equipment piece
- SIL / LOPA assessment adds **~20%** to total analysis time

### P&ID Throughput Rates
| Drawing Type | Target Rate |
|-------------|------------|
| Process unit P&IDs (full, detailed) | 3 per day |
| Utility P&IDs | 4 per day |
| Similar/repetitive equipment or early-stage drawings | 4–5 per day |
| Duplicate trains or distribution drawings | Nominal time only |
| **Minimum acceptable (most projects)** | **3–4 P&IDs per day** |

### Cost Benchmarks (for reference only)
- HAZOP ≈ 0.2% of capital project cost (0.25–0.3% if regulatory)
- HAZOP ≈ 1% of design cost (1.3–1.5% if regulatory); more accurate than capital-cost basis
- Neither figure includes implementation of recommendations

### First Team Meeting Agenda
Before beginning formal node analysis, the Leader should address:
1. Team qualifications (confirm required disciplines present)
2. Documentation (confirm all PSI available, current, and "As-built" signed off)
3. Plant layout / brief process description / hazards of the chemicals
4. Previous incidents (relevant to plant/section)
5. HAZOP method (methodology refresher, guideword set, RAM)
6. Ground rules (attendance, decision authority, participation expectations)

---

---

## GC HAZOP Workflow (End-to-End)

> Source: [[wiki/sources/hazop-leadership-training-ch7]]

### Five Phases of the GC HAZOP Lifecycle

| Phase | Owner | Key Output |
|-------|-------|-----------|
| 1. Initiating HAZOP | CRT | Formal decision that HAZOP is required |
| 2. HAZOP Preparation | HAZOP Coordinator | PSI assembled; team scheduled |
| 3. HAZOP Study Workshop | HAZOP Team | Completed worksheets |
| 4. Report Preparation & Approval | Scribe → HAZOP Leader | Report: Draft → Submitted → Publish |
| 5. Action Close-out | Responsible Person + Action Approver | Report reaches status "Complete" |

### Report Status States

| Status | Trigger | Gatekeeper |
|--------|---------|-----------|
| **Draft** | Scribe prepares post-workshop | Scribe |
| **Submitted** | Scribe submits for approval | Scribe |
| **Publish** | HAZOP Leader approves | HAZOP Leader |
| **Complete** | All actions closed and approved | System |

If HAZOP Leader does NOT approve the Submitted report → returns to Scribe (Draft → revision loop).

### Action Change Process (Post-Publish)

After the report is published, if a Responsible Person proposes to implement an action differently from the workshop outcome:

1. **HAZOP Coordinator (Champion)** raises a formal action change request in the e-PHA system
2. **HAZOP Team re-evaluates risk** based on the proposed alternative action
3. If team **Accepts** → action is revised in system → proceeds to Action Close-out
4. If team does NOT Accept → original workshop action stands → proceeds to Action Close-out

> ⚠️ Responsible persons **cannot** unilaterally modify HAZOP actions. All changes require HAZOP team re-evaluation. This preserves the integrity of the workshop risk assessment.

### Action Close-out Approval Gate

- Responsible Person completes the action → submits for close-out approval
- **Action Approver** reviews and approves → Action Close-out Complete
- If not approved → returned for revision and resubmission
- When all actions are approved → HAZOP Report transitions to status **"Complete"**

### Roles Summary

| Role | Responsibility |
|------|---------------|
| CRT | Initiates HAZOP study (formal trigger) |
| HAZOP Coordinator | Prepares PSI; manages action change requests as Champion |
| HAZOP Team | Conducts workshop; re-evaluates risk on proposed action changes |
| Scribe | Prepares Draft; submits for approval; projects live recording |
| HAZOP Leader | Approves report (Draft → Publish gate) |
| Responsible Person | Implements and closes out actions |
| Action Approver | Approves action close-out |

---

## References
- [[wiki/sources/SG-Q-MP-014]] — Primary governing document: 9-step method, guideword table, IPL tables
- [[wiki/sources/hazop-leadership-training-ch4]] — Recording DO/DON'T, excluded causes, deviation set
- [[wiki/sources/hazop-leadership-training-ch5]] — Worksheet column structure, scheduling rules, team requirements
- [[wiki/sources/hazop-leadership-training-ch7]] — GC HAZOP Workflow (5 phases, 4 report statuses, action change process)
- [[wiki/hazop/risk-matrix]] — Full RAM for Severity × Likelihood rankings
- [[wiki/hazop/action-register]] — Where recommendations are recorded
- [[wiki/hazop/study-info]] — Node status, scope, team, governing documents
