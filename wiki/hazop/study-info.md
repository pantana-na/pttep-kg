---
name: HAZOP Study Info
tags: [hazop, study-info]
last_updated: 2026-06-14
---

# HAZOP Study Information

> **Status: SETUP COMPLETE — Awaiting expert-marked P&IDs with node boundaries**
>
> All four standards ingested (Procedure + Risk Matrix + HAZOP Guidance + P&ID Readiness Checklist). Node analysis cannot begin until an experienced engineer marks node boundaries on the CDN P&IDs and the HAZOP Coordinator formally signs off Table A6.2-3.

---

## Scope

- **Plant:** Refinery Phenol Train II, Map Ta Phut, Thailand
- **Licensor:** UOP / Honeywell
- **Engineer:** POSCO Engineering
- **Sections in scope:** CDN — Concentration, Decomposition, Neutralization (primary scope; initial study phase)
- **Trigger:** Process safety study (not under MoC; this is a standalone CDN section HAZOP)
- **Excluded:** Alkylation, Oxidation, Fractionation, Utilities, ETP (pending PSI availability)

---

## Governing Documents

| Document | Location | Purpose | Status |
|----------|----------|---------|--------|
| HAZOP Procedure | [[sources/P-Q-MP-OEMS-005]] | Methodology, roles, documentation requirements | ✅ Ingested |
| Risk Assessment Matrix | [[sources/W-Q-MP-002]] / [[hazop/risk-matrix]] | Severity × Likelihood criteria — **governs all risk rankings** | ✅ Ingested |
| HAZOP Guidance | [[sources/SG-Q-MP-014]] / [[hazop/methodology]] | Guideword set, 9-step method, IPL credit tables, PSI checklist | ✅ Ingested |
| PSI Readiness Checklist (Table A6.2-2) | [[sources/Table-A6.2-2-PSI-readiness-checklist]] | 8-category formal checklist for PSI completeness verification | ✅ Ingested |
| P&ID Readiness Checklist (Table A6.2-3) | [[sources/Table-A6.2-3-PID-readiness-checklist]] | 13-item checklist for P&ID quality before HAZOP — Items 1–10 CRITICAL | ✅ Ingested |

---

## Methodology Notes

- **9-step method**: per SG-(Q-MP)-014 §5.3.3 — see full detail at [[hazop/methodology]]
- **Guideword set**: Table 6.1 of SG-(Q-MP)-014 — 14 parameters × applicable guidewords — see [[hazop/methodology]]
- **Initial risk** = Severity × Likelihood WITHOUT safeguards — Severity is fixed at this stage
- **Mitigated risk** = Likelihood re-assessed WITH IPL-qualified safeguards — Severity never changes
- **Acceptable risk for GC** = Low or Very Low; Mitigated risk ≥ Medium → must generate recommendation
- **IPL credit**: Active (Table 6.4) and Passive (Table 6.5) from SG-(Q-MP)-014 — see [[hazop/methodology]]
- **RAM**: [[hazop/risk-matrix]] (W-(Q-MP)-002 §6.2.1.3.1) governs all rankings
- **Full record approach**: every deviation must be documented; if no credible cause, state "N/A — no credible cause"

---

## Study Team

| Role | Name / Discipline | Regulatory Basis | Status |
|------|-----------------|-----------------|--------|
| HAZOP Coordinator | TBD | GC | Pending |
| HAZOP Leader | TBD — min 8 yrs O&G/petrochem; independent from design/EPC/VP Operations | GC + IEAT PSM 2559 + DIW 2543 | Pending |
| HAZOP Scribe | TBD — dedicated role; technical background; NOT a team member; NOT the Leader | GC only (not required by IEAT/DIW) | Pending |
| Process Engineer | TBD | GC + IEAT + DIW | Pending |
| Operations Representative | TBD | GC + IEAT + DIW | Pending |
| Plant Safety Engineer | TBD | GC + IEAT + DIW | Pending |
| Site Maintenance Engineer | TBD | GC + DIW | Pending |
| Licensor / Specialist / Vendor | TBD (optional — depends on node) | GC: Y/N | Pending |

**Scribe note:** Scribe follows discussion without participating, projects the live recording file so all team can see. Uses GC HAZOP Template (Excel) or e-PHA online system. Source: [[sources/hazop-leadership-training-ch5]]

**Leader note:** Leader can request additional required member at any time if disciplines required for a specific node are absent.

---

## Session Management — Facilitation Guidance

> Source: [[sources/hazop-leadership-training-ch6]]

### Decision-Making Approach
Preferred approach: **Consensus** — team more committed to conclusions, fewer confrontations, no corridor politicking. Leader may use direct decision (levels 1–2) when the team is stuck or when procedural/ground-rule matters arise, but risk-ranking and recommendation decisions should always be consensus.

### HAZOP Ground Rules (to be agreed at first session)

**Core rules (Leader proposes; team helps finalize):**
1. Start on time and end on time
2. Take breaks regularly — maintain team energy
3. All ideas are worthy — no bad ideas
4. Safe environment — no personal attacks
5. Everyone contributes
6. **Do not design solutions in the HAZOP meeting** — raise a recommendation; solve it outside
7. Take conflicts outside the workshop
8. Phones on silent / vibrate / off
9. Advise of any absence in advance

**Supplementary rules:**
1. Diversity is good
2. Present your view but avoid arguing for it
3. Listen to others and look for compromise
4. Do not change your view simply to avoid conflict

### Progressive Leader Role (per session)
| Phase | Role | Key Behavior |
|-------|------|-------------|
| Session 1 opening | **Trainer** | Train team, let group create ground rules, phrase own contributions as questions |
| Early sessions | **Team Builder** | Go around room on causes; direct questions to specific expertise; maintain safe environment |
| Normal node analysis | **Facilitator** | Stay neutral; refer ideas to team not self; use parking lot; deal with difficult personalities |
| After node / report | **Editor** | Quality-check worksheet entries and recommendations |

---

## Anti-Bias Declaration

> ⚠️ **No previous HAZOP reports have been ingested into this wiki.** This study is conducted independently. No prior worksheets, revalidation reports, or recommendation registers are present in `raw/`. See HAZOP Anti-Bias Rule in `app/hazop/anti_bias.py` and `GEMINI.md`.

---

## PSI Readiness Status

Per formal **Table A6.2-2 PSI Readiness Checklist** (GC standard — [[sources/Table-A6.2-2-PSI-readiness-checklist]]):

| # | Category | Criticality | CDN Status | Gap / Notes |
|---|----------|-------------|-----------|-------------|
| 1 | Chemical and Reaction hazard (GHS-compliant SDS) | High | ✅ Complete | 15 GHS-compliant SDS ingested 2026-06-14 covering all CDN chemicals — [[sources/sds-psi-batch-2026-06-14]]. Hazard pages written for all 15 chemicals. Data quality flags: Diamine identity TBC ([[hazards/diamine-tbc]] — ⛔ PLACEHOLDER); DMBA CAS identity flag ([[hazards/dimethylbenzylcarbinol]]); CHP decomp onset CONFLICT (80°C SDS vs 100°C wiki); Phenol LEL/UEL CONFLICT (1.3/9.0% SDS vs 1.7/8.6% wiki). ECHA C&L verification recommended for cumene (Carc 1B), AMS (H304/H361), DIPB (H304/H411). |
| 2 | Process Flow Information (P&IDs, PFDs with H&M balance) | High | ✅ Complete | CDN PFDs (Dwg 0000–0006) + P&IDs (Dwg 0002–0023) all ingested; Table A6.2-3 P&ID readiness items satisfied or hand-markup resolvable |
| 3 | Process Description, Design Basis and Process chemistry | High | ✅ Complete | UOP GOM §II–XI ingested; CDN procedures, parameters, and operating windows in wiki |
| 4 | Equipment information (Equipment data sheets) | High | ❌ Missing | Equipment data sheets not ingested — design P&T, materials of construction TBC for all major CDN items |
| 5 | Operating Procedures (Normal / Startup / Shutdown / Emergency) | High | ✅ Complete | [[procedures/normal-operations-cdn]], [[procedures/normal-shutdown-cdn]], [[procedures/emergency-cdn]] — UOP GOM basis; cross-checked against C&E |
| 6 | Safety Systems & Safeguards (C&E, SIS/SIF data) | High | ⚠️ Partial | C&E table [[instruments/cause-effect-cdn]] + SIS architecture [[instruments/sis-cdn]] ingested; PSV setpoints for V-2301/V-2302 TBC; calorimeter ΔT alarm setpoints TBC |
| 7 | Relief & Flare Design (relief calc, flare hydraulics) | High | ⚠️ Partial | Relief header (Dwg 0022) ingested; formal relief load calculation and PSV sizing basis not available |
| 8 | Past Incidents (incident reports, industry databases) | Medium | ❌ Not ingested | Anti-Bias Rule governs — do not ingest previous HAZOP/incident reports until current study worksheets are complete |

**PSI readiness: ~65% complete (per formal Table A6.2-2 basis) — Item 1 SDS ✅ Complete**

**PSS data baseline confirmed (2026-06-14):**
- ✅ Diamine additive identity: confirmed as **DIPA (Diisopropanolamine, CAS 110-97-4)** — [[hazards/diamine-tbc]] updated
- ✅ CHP decomp onset conflict: **80°C adopted as worst-case PSS basis** (SDS value; previous 100°C superseded)
- ✅ Phenol LEL/UEL conflict: **1.3% / 9.0% adopted as worst-case PSS basis** (SDS value; previous 1.7%/8.6% superseded)
- ✅ ECHA precautionary classifications applied: Cumene (Carc 1B), AMS (H304/H361/Skin Sens 1B), DIPB (H304/H411), DMBA (H301 worst case, CAS 100-86-7 confirmed), Benzene (OEL 0.02 ppm precautionary)

**Outstanding blockers (all High criticality):**
1. ❌ Equipment data sheets — design P&T, material of construction for all major CDN tags
2. ⚠️ Alarm/trip settings — PSV set pressures V-2301/V-2302; calorimeter ΔT trips (ΔT setpoints)
3. ⚠️ Relief & flare design data — PSV sizing basis and relief scenario calculations

> Additional Operation-phase Essential items from Appendix 6.2 not yet ingested: Plot Plan, General Equipment Arrangements, Hazardous Area Classification drawings, Line lists, Process Safeguarding Flow Scheme, SIL Study report, as-built drawings.

---

## P&ID Readiness Status

Per formal **Table A6.2-3 P&ID Readiness Checklist** (GC standard — [[sources/Table-A6.2-3-PID-readiness-checklist]]):

> This checklist must be completed by the HAZOP Coordinator before any node analysis begins. Items 1–10 are CRITICAL.

| No. | Checklist Item | Critical | CDN P&ID Status | Notes |
|-----|---------------|----------|----------------|-------|
| 1 | Latest revision issued & controlled | **YES** | ✅ YES | All 45 CDN drawings at Rev Z1 As-Built |
| 2 | Scope completeness | **YES** | ✅ YES | Process sheets 0002–0023 + standard details 0001–0001L; all CDN sub-sections covered |
| 3 | Equipment tags complete & consistent | **YES** | ✅ YES | All tags confirmed; X-2308→X-2309 conflict resolved (Drawing 0018) |
| 4 | Line identification | **YES** | ⚠️ PARTIAL | Flow directions confirmed; piping class designation on lines to be spot-checked per drawing |
| 5 | Instrumentation (indicators, transmitters, alarms) | **YES** | ✅ YES | C&E table + all SIS/DCS/analyzer tags documented |
| 6 | Control loops & interlocks | **YES** | ✅ YES | UC-2301/2302/2303 complete; [[instruments/cause-effect-cdn]] and [[instruments/sis-cdn]] |
| 7 | Safety devices (PSVs, rupture discs) | **YES** | ⚠️ PARTIAL | PSV tags shown; set pressures for V-2301 and V-2302 TBC |
| 8 | Tie-ins location | **YES** | ✅ YES | OXI feed, Fractionation outlet, OWS tie-ins documented |
| 9 | Isolation devices (block valves, blinds) | **YES** | ✅ YES | All SIS valves, block valves, and check valves documented |
| 10 | Consistency across drawings | **YES** | ✅ YES | Cross-sheet continuity verified during P&ID ingest (2026-06-06/07) |
| 11 | Legend / symbols available | — | ✅ YES | Standard detail sheets 0001–0001L provide all symbols and schematics |
| 12 | Notes and references | — | ✅ YES | Drawing notes captured in equipment pages |
| 13 | Consistency with PFD | — | ✅ YES | PFD and P&ID cross-referenced; tag discrepancy resolved |

**Critical items 1–10:** 8 of 10 = ✅ YES | 2 of 10 = ⚠️ PARTIAL (Items 4 and 7)
**Desirable items 11–13:** 3 of 3 = ✅ YES
**HAZOP Coordinator formal sign-off:** ❌ Not yet completed

**Pre-HAZOP actions required:**

| Action | Priority | Blocks |
|--------|----------|--------|
| Confirm piping class designation on all CDN P&ID lines (Item 4) | Medium | Node analysis on any line-intensive nodes |
| Obtain PSV set pressures for V-2301 and V-2302 (Item 7) | **High** | Node analysis on Concentration nodes |
| Resolve P-2307A/B motor type conflict (Type B vs Type D) | Medium | Node analysis on overhead pump node |
| HAZOP Coordinator to formally sign off Table A6.2-3 | **REQUIRED** | All nodes |

---

## Node Status Register

> Nodes to be defined once expert-marked P&IDs are provided. CDN P&IDs 0002–0023 are available in `raw/pid/`. An experienced engineer should mark node boundaries on these drawings before node analysis begins.

| Node ID | Description | P&ID Sheet(s) | Status | Date Completed |
|---------|-------------|--------------|--------|---------------|
| CDN-N01 | Oxidate feed / Preflash Column Feed Filters (markup "Node 23-01") | 0003, 0004 | Pending — markup received | — |
| CDN-N02 | Preflash Column feed-heating / steam-condensate circuit — E-2302A/B, E-2303, D-2308, P-2308A/B (markup "Node 23-02") | 0005, 0005A (+ 0004/0007 crossings) | **PRELIMINARY DRAFT 2026-06-17** — desktop first-pass [[hazop/nodes/cdn-N02]]; boundaries + worksheet awaiting engineer/team confirmation | — |
| CDN-N03 | Flash Column Vaporizer & Concentrated-CHP Bottoms Pump-Out — E-2304, D-2309, P-2309A/B, V-2302 bottoms, P-2301A/B (markup "Node 23-03", green) | 0007, 0007A, 0008, 0009, 0012, 0012A | **PRELIMINARY DRAFT 2026-06-18** — desktop first-pass [[hazop/nodes/cdn-N03]]; Excel export `2026-06-18_CDN-N03_HAZOP-worksheet.xlsx`; R-005–R-009 generated; boundaries (handoffs to 23-04/23-05/Decomposer-feed) + worksheet awaiting engineer/team confirmation | — |
| CDN-N05 | (markup "Node 23-05" — Preflash/Flash Column body, Dwg 0004/0006/0007) | 0004, 0006, 0007 | Pending — markup received | — |
| CDN-N06 | (markup "Node 23-06" — Cumene Quench Drum area, Dwg 0006) | 0006 | Pending — markup received | — |

> **Node numbering note:** the engineer's markup labels nodes "Node 23-0x" (23 = CDN drawing series). Filed in the wiki as `CDN-N0x` per the skill's `<unit>-N<nn>` schema. The "Node 23-02.pdf" markup (supplied 2026-06-17) shows 23-01/02/03/05/06; the "Node 23-03.pdf" markup (supplied 2026-06-18, green highlight across Dwg 0007/0007A/0008/0009/0012/0012A) defines **CDN-N03**. **23-02** and **23-03** have been worked (preliminary). Recommend filing both markups in `raw/pid/` for the record.

**Suggested node breakdown** (preliminary — requires expert confirmation):
- Node 1: Oxidate Feed to CDN / Feed Filters (X-2302A/B) → Dwg 0003
- Node 2: Preflash Column (V-2301) + Steam Heater (E-2303) → Dwg 0004, 0005, 0005A
- Node 3: Flash Column (V-2302) + Vaporizer (E-2304) → Dwg 0007, 0008
- Node 4: Overhead System / Vacuum Producing Equipment (X-2301) → Dwg 0010, 0010A
- Node 5: Flash Column Bottoms / CHP Transfer to Decomposer → Dwg 0009, 0012
- Node 6: Decomposer Drum (D-2304) + Circulation (P-2302A/B) → Dwg 0013, 0017
- Node 7: Acid Injection System (D-2310/D-2311/P-2305A–F/X-2309A/B) → Dwg 0015, 0016, 0018
- Node 8: Dehydrators (E-2308A/B) + Crude Product Cooler (E-2309) → Dwg 0014, 0014A
- Node 9: Neutralization (X-2310A/B) + Diamine Injection → Dwg 0019
- Node 10: Acid Aromatics System (D-2306/D-2307/drain headers) → Dwg 0020, 0020A, 0021, 0022, 0023

---

## Prerequisites Before Starting Node Analysis

> ⛔ **DO NOT begin node analysis until ALL of the following are confirmed:**
>
> 1. ✅ HAZOP Procedure ingested — [[sources/P-Q-MP-OEMS-005]]
> 2. ✅ Risk Assessment Matrix ingested — [[hazop/risk-matrix]] from W-(Q-MP)-002 R2
> 3. ✅ HAZOP Guidance ingested — [[hazop/methodology]] from SG-(Q-MP)-014 R3
> 4. ✅ P&ID Readiness Checklist (Table A6.2-3) ingested — [[sources/Table-A6.2-3-PID-readiness-checklist]]
> 5. ❌ **Expert-marked P&IDs with node boundaries** placed in `raw/pid/` — **OUTSTANDING**
> 6. ❌ **HAZOP Coordinator formal sign-off on Table A6.2-3** — **OUTSTANDING**
> 7. ❌ **PSV set pressures for V-2301/V-2302** confirmed — **OUTSTANDING (Item 7 partial)**
> 8. ✅ No previous HAZOP report present in `raw/` — Anti-Bias Rule confirmed

---

## GC HAZOP Workflow — Study Phase Tracking

> Source: [[sources/hazop-leadership-training-ch7]] — GC HAZOP Workflow (Chapter 7-2)

| Workflow Phase | Status | Notes |
|----------------|--------|-------|
| Phase 1 — Initiating HAZOP (CRT trigger) | ⚠️ In progress | Study initiated informally; formal CRT trigger not confirmed |
| Phase 2 — HAZOP Preparation (Coordinator assembles PSI) | ⚠️ Partial | Standards ingested ✅; equipment data sheets ❌; node markup ❌ |
| Phase 3 — HAZOP Study Workshop | ❌ Not started | Awaiting Phase 2 completion |
| Phase 4 — Report Preparation & Approval (Draft → Submitted → Publish) | ❌ Not started | — |
| Phase 5 — Action Close-out (Complete) | ❌ Not started | — |

**Current report status:** N/A — workshop not yet commenced

**Action change protocol:** Any deviation from workshop actions requires HAZOP Coordinator to raise a formal change request; HAZOP Team re-evaluates risk before any action revision is accepted. See [[hazop/methodology]] (GC HAZOP Workflow section).

---

## References
- [[sources/P-Q-MP-OEMS-005]] — governing HAZOP procedure
- [[sources/W-Q-MP-002]] — risk matrix source
- [[sources/SG-Q-MP-014]] — HAZOP guidance source
- [[sources/Table-A6.2-2-PSI-readiness-checklist]] — PSI completeness (8 categories)
- [[sources/Table-A6.2-3-PID-readiness-checklist]] — P&ID quality checklist (13 items, Items 1–10 critical)
- [[sources/hazop-leadership-training-ch7]] — GC HAZOP Workflow: 5 phases, 4 report statuses, action change process
- [[hazop/risk-matrix]] — risk ranking (W-(Q-MP)-002 §6.2.1.3.1)
- [[hazop/methodology]] — 9-step execution method, guideword table, IPL tables, full workflow
- [[hazop/action-register]] — all recommendations
