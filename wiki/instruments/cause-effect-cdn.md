---
name: CDN Cause and Effect Table
unit: CDN
tags: [instruments, SIS, cause-effect, interlock, CDN, safety]
sources: [14780-8120-25-23-0002_Z1.pdf]
last_updated: 2026-06-06
---

# CDN Cause and Effect Table

**Source:** Drawing 14780-8120-25-23-0002, Rev Z1 As-Built  
**Licensor Basis:** UOP — STD DWG 963766-120-02-A1

> ⚠️ This is the authoritative shutdown logic document for CDN Unit 2300. See [[instruments/sis-cdn]] for architectural overview.

---

## SIS Tag Naming Convention

SIS instruments use the format **TXS**HH / **FXS**LL (note the **S** = Safety in the middle). These are **dedicated SIS transmitters** — separate hardware from DCS measurement instruments.

| SIS Format | DCS Equivalent | Meaning |
|-----------|---------------|---------|
| TXSHH | TAHH | Temperature transmitter (SIS), High-High |
| TXSLL | TALL | Temperature transmitter (SIS), Low-Low |
| FXSLL | FALL | Flow transmitter (SIS), Low-Low |
| LXSHH | LAHH | Level transmitter (SIS), High-High |
| LXSLL | LALL | Level transmitter (SIS), Low-Low |
| PDXSHH | PDAHH | Diff. Pressure transmitter (SIS), High-High |
| PXSLL | PALL | Pressure transmitter (SIS), Low-Low |
| TDXSHH | TDAHH | Diff. Temp transmitter (SIS), High-High |

> **Note:** Previous wiki entries in [[instruments/sis-cdn]] used DCS-format tags (TXAHH-23-xxxx). The C&E table and the SIS system use the TXSHH format. Both refer to the same physical SIS point.

---

## Effect Legend

| Symbol | Meaning |
|--------|---------|
| **C** | Close (valve) |
| **O** | Open (valve) |
| **S** | Stop (pump/motor) |
| **T** | Trip (motor) |
| **E** | Energize (solenoid/signal) |
| blank | No action |

---

## SIL Rating Column

| Value | Meaning |
|-------|---------|
| 1 | SIL 1 rated initiator |
| 2 | SIL 2 rated initiator |
| A | Assessed (analog SIS transmitter, SIL-rated) |
| S/C | Stop/Close (effect column designation) |

---

## UC-2301 — Concentration Section Shutdown

### Causes (Initiators)

| # | Cause Description | SIS Tag(s) | Voting | Time Delay | SIL |
|---|------------------|-----------|--------|-----------|-----|
| 1 | Feed to Preflash Column — Low-Low Flow | FXSLL-0401A/B/C | **2oo3** | YES | 1 |
| 2 | Preflash Column Feed-Oxidate Exchanger Vapor/Liquid High Temp | TXSHH-0501 | 1oo1 | YES | 1 |
| 3 | Preflash Column Steam Heater Tube Liquid High-High Temp | TXSHH-0502A, TXSHH-0502B | **1oo2** | YES | 1 |
| 4 | Preflash Column Bottom High Temp | TXSHH-0404 | 1oo1 | YES | 1 |
| 5 | Preflash Column Bottom High-High Level | LXSHH-0401 | 1oo1 | YES | — |
| 6 | Flash Column Bottom High-High Level | LXSHH-0802 | 1oo1 | YES | — |
| 7 | Flash Column Vapor Space High-High Pressure | PXSHH-0801 | 1oo1 | YES | 2 |
| 8 | Flash Column Vaporizer Vapor Space/Outlet High-High Temp | TXSHH-0701A, TXSHH-0702A | **1oo2** | YES | 2 |
| 9 | Flash Column Vaporizer Vapor Space/Outlet High-High Temp (second pair) | TXSHH-0701B, TXSHH-0702B | **1oo2** | YES | — |
| 10 | Flash Column Bottom High-High Temp | TXSHH-0805A, TXSHH-0805B | **1oo2** | YES | 2 |
| 11 | Flash Column Bottoms Pump Suction High-High Temp | TXSHH-0901A, TXSHH-0901B | **1oo2** | YES | — |
| 12 | Oxidation Section Shutdown — Oxidizers Shutdown | UC-2201 | Cross-trip | 1 min | — |
| 13 | Oxidation Section Shutdown System Trip — Decanter Shutdown | UC-2205 | Cross-trip | 1 min | — |
| 14 | Emergency Shutdown | HXS-0101 | Manual key | — | — |
| 15 | Preflash Column Feed Start ** | HXS-0102 | Manual (bypass) | — | — |

> **\*\* Note on HXS-0102:** Pressing this button BYPASSES (for a timed interval) the following interlocks: FXSLL-0401A/B/C (Feed to Preflash Column) and LXSHH-0802 (Flash Column Bottom level). Used during startup to allow column filling before level/flow interlocks become active.

### Effects (Actions)

*Effect columns in the C&E table (diagonal headers). Actions listed are for the UC-2301 Concentration Section Shutdown:*

| Effect Tag / Description | Cause 1 | Cause 2 | Cause 3 | Cause 5 | Cause 6 | Cause 7–11 | Cause 12/13 | Cause 14 (ESD) |
|--------------------------|---------|---------|---------|---------|---------|-----------|------------|----------------|
| Close UXV-0401 (Preflash Col. feed) | C | C | C | C | C | C | C | C |
| Close UXV-0501/0502 (Steam Heater) | C | C | C | C | C | C | C | C |
| Close UXV-0601 (Cumene Quench) | C | C | C | C | C | C | C | C |
| Close UXV-0701–0706 (Flash Vaporizer) | C | C | C | C | C | C | C | C |
| Close UXV-0802/0803 (Flash Column) | C | C | C | C | C | C | C | C |
| Close UXV-0803/0804/0805 (Overhead) | C | C | C | C | C | C | C | C |
| Stop P-2307A/B (Overhead Pumps) | S | S | S | S | S | S | S | S |
| Stop P-2308A/B (Steam Heater Condensate) | S | S | S | S | S | S | S | S |
| Stop P-2309A/B (Vaporizer Condensate) | S | S | S | S | S | S | S | S |
| Trigger UC-2302 (Cross-trip to Decomp.) | T | T | T | T | T | T | T | T |
| Open vent to atmosphere | O | O | O | O | O | O | O | O |

> **Note:** Exact cell values (which causes produce which effects) require verification against original drawing. Table above represents general pattern from C&E; individual cells may differ. Cause 15 (HXS-0102, startup) produces selective bypass not full shutdown.

---

## UC-2302 — Decomposition Section Shutdown

### Causes (Initiators)

> This is the most safety-critical table in CDN. Decomposer ESD has the most causes, the tightest voting logic, and the highest SIL ratings.

| # | Cause Description | SIS Tag(s) | Voting | Time Delay | SIL |
|---|------------------|-----------|--------|-----------|-----|
| 1 | Decomposer Feed — Low-Low Flow | FXSLL-1204A/B/C | **2oo3** | YES | **2** |
| 2 | Decomposer — High-High Level | LXSHH-1303, LXSHH-1302 | **1oo2** | YES | **2** |
| 3 | Decomposer — High-High Temperature | TXSHH-1301A, TXSHH-1301B | **1oo2** | YES | **2** |
| 4 | Decomposer — Low-Low Temperature | TXSLL-1301A, TXSLL-1301B | **1oo2** | YES | **2** |
| 5 | Dehydrator Outlet — High-High Temperature | TXSHH-1402 | 1oo1 | YES | **1** |
| 6 | Acid Injection — Low-Low Flow (2oo3) | FXSLL-1501, FXSLL-1601, FXSLL-1602 | **2oo3** | YES | **1** |
| 7 | Decomposer Cooler High-High Differential Pressure | PDXSHH-1701A/B/C | **2oo3** | YES | **2** |
| 8 | Calorimeter System 1 Total DT High-High (Cal 1 in service) | TDXSHH-1801 | 1oo1 | YES | **1** |
| 9 | Calorimeter System 1 Inlet DT High-High (Cal 1 in service) | TDXSHH-1802 | 1oo1 | YES | A |
| 10 | Calorimeter System 1 Total DT High-High (Cal 2 in service) | TDXSHH-1803 | 1oo1 | YES | A |
| 11 | Calorimeter System 2 Inlet DT High-High (Cal 2 in service) | TDXSHH-1804 | 1oo1 | YES | A |
| 12 | Failing Liquid to Calorimeter Systems — Low-Low Flow | FXSLL-1803, FXSLL-1804 | — | — | — |
| 13 | Decomposer Feed Flush Drum — Low-Low Level | LXSLL-1201 | 1oo1 | — | A |
| 14 | Concentration Section Shutdown (cross-trip from UC-2301) | UC-2301 | Cross-trip | — | — |
| 15 | Process Water to Decomposer — Low-Low Pressure | PXSLL-1201 | 1oo1 | — | — |
| 16 | Decomposer Shutdown | HXS-0104 | Manual ESD | — | — |
| 17 | Decomposer Feed Start | HXS-0105 | Manual (enable) | — | — |
| 18 | Cumene Flush to Decomposer Feed Line Start | HXS-0106 | Manual (enable) | — | — |
| 19 | Cumene Flush to Concentrate Long Circulation Line Start | HXS-0107 | Manual (key, 2-pos) | — | — |
| 20 | Steam to Dehydrator Enable/Shutoff ** | HXS-0108 | Manual | — | — |

> **\*\* Note on HXS-0108/0109:** When activated, bypasses (for a timed interval) all conditions that cause the Steam to Dehydrator Valve (UXV-1401) to close — except HXS-0104 (manual ESD). Also bypasses the Low Acid Injection Flow interlock. Used during dehydrator startup heat-up sequence.

### Effects (Actions) — UC-2302

| Effect Description | Notes |
|-------------------|-------|
| Close UXV-1201A/B | CHP feed to Decomposer — primary cutoff (BOTH valves close, SIL verified redundancy) |
| Close UXV-1301, UXV-1302 | Decomposer Drum feed isolation |
| Open Cumene Flush to Decomposer feed line | Purge CHP from feed lines |
| Open Cumene Flush to long circulation line | Purge CHP from concentrate circulation |
| Stop P-2303A/B (Decomposer Product Pumps) | Product extraction stops |
| Stop P-2305A/B/C/D/E/F (Acid Injection Pumps) | Acid injection stops |
| Close UXV-1401 (Steam to Dehydrator) | Prevent overheating dehydrators after shutdown |
| Close UXV-1402, UXV-1403 (Crude Product Cooler) | Isolate downstream |
| Signal to DCS | Annunciation UA-23-2302 |

> **Note on P-2302 (Decomposer Circulation):** The C&E table does NOT automatically stop P-2302 on all causes. The Decomposer Circulation Pumps **continue running** during and after many ESD events to maintain product dilution and heat removal. P-2302 only stops when specifically required (e.g., manual ESD or when all process fluid has been flushed). This is a critical operational point — do not stop P-2302 prematurely during an ESD.

---

## UC-2303 — Concentration Vacuum Producing Equipment Shutdown

### Causes

| # | Cause Description | SIS Tag | Voting | SIL |
|---|------------------|---------|--------|-----|
| 1 | Vacuum Equipment Separator — High-High Level | LXSHH-1006 | 1oo1 | S/C |
| 2 | Vacuum Equipment Spill-Back Control — High-High DP | PDXSHH-1012 | 1oo1 | S/C |
| 3 | Vacuum Equipment Sealant — Low-Low Flow | FXSLL-1008 | 1oo1 | S/C |
| 4 | Vacuum Equipment Inlet — High-High Temperature | TXSHH-1008 | 1oo1 | S/C |
| 5 | Vacuum Equipment Emergency Switch | HXS-1001 | Manual | S/C |

### Effects

| Effect | Action |
|--------|--------|
| Stop P-2316A/B (Vacuum System Pumps) | S |
| Stop P-2317A/B (Vacuum System Pumps) | S |
| Close associated vacuum system valves | C |

---

## Process Engineering Analysis — Key Safety Insights

### 1. Decomposer Cooler DP Shutdown (PDXSHH-1701A/B/C) — Critical, Often Overlooked
**SIL 2**, 2oo3 voting. If [[equipment/E-2307]] (Decomposer Cooler) develops high differential pressure — from fouling, cooling water blockage, or tube failure — the ESD triggers before the decomposer can overheat. From an operations standpoint: **rising DP on E-2307 is an early warning of approaching decomposer ESD**. Monitor CW flow and cooler DP closely during production.

### 2. Calorimeter Logic — Dual-Mode Safety
Each calorimeter provides TWO types of temperature differential signals:
- **Total DT (TDXSHH-xxxx)**: Overall temperature rise across the entire calorimeter — measures total heat release rate. SIL 1 (Cal 1), SIL A (Cal 2).
- **Inlet DT (TDXSHH-xxxx)**: Temperature rise at the inlet section — detects rapid initial heat release. SIL A.

The "in service" qualifier means: if Calorimeter No. 1 is in service (selected), then TDXSHH-1801/1802 are active. If Calorimeter No. 2 is selected, TDXSHH-1803/1804 are active. This prevents false trips when one calorimeter is taken out of service for maintenance.

**Calorimeter liquid feed flow (FXSLL-1803, FXSLL-1804)**: If the liquid feed to the calorimeters is lost (no sample flow), the calorimeter temperature measurement becomes unreliable. This triggers a UC-2302 action — the plant cannot safely continue if the primary safety sensor has lost its process connection.

### 3. Decomposer Temperature LL Shutdown — Counterintuitive but Critical
TXSLL-1301A/B (Low-Low temp, SIL 2, 1oo2): A falling decomposer temperature means the reaction is dying — acid has been diluted, or flow has reduced. Under these conditions, un-decomposed CHP can accumulate. Cutting the feed immediately is the correct response before the temperature rises again from accumulated CHP decomposing in a batch.

### 4. Cross-Trip Cascade
UC-2301 (Concentration ESD) → triggers UC-2302 (Decomposer ESD). The reverse is NOT true — a Decomposer ESD does NOT automatically shut down the Concentration section. This reflects the process logic: you can concentrate CHP without decomposing it (briefly, safely), but you cannot continue decomposition if concentration is interrupted.

### 5. Process Water to Decomposer (PXSLL-1201)
Loss of process water pressure to the decomposer triggers ESD. Process water is used for dilution control and as part of the decomposer heat management. This is a utility failure initiator — argues for monitoring instrument air and process water supply pressures carefully.

### 6. Acid Injection 2oo3 Voting (FXSLL-1501, 1601, 1602)
Three flow switches across the six acid injection pumps (two pumps per switch group, covering P-2305A/B, C/D, E/F). The 2oo3 design means losing one flow measurement does not cause a spurious ESD, but losing actual acid flow on two out of three circuits does — a robust design for this critical safety function.

---

## References

- [[sources/pid-cdn]] — Drawing 0002
- [[instruments/sis-cdn]] — SIS architecture (update pending — use this C&E as primary)
- [[equipment/D-2304]] — Decomposer Drum (primary UC-2302 protection target)
- [[equipment/E-2307]] — Decomposer Cooler (PDXSHH-1701 shutdown)
- [[equipment/X-2308]] — Calorimeters (TDXSHH-1801 through 1804 shutdown)
- [[equipment/P-2302]] — Decomposer Circulation Pumps (NOT auto-stopped by most ESD)
- [[hazards/cumene-hydroperoxide]]
