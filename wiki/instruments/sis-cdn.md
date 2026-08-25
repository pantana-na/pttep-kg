---
name: CDN Safety Instrumented System (SIS) Architecture
unit: CDN
tags: [instruments, SIS, safety, CDN, interlock]
sources: [14780-8120-25-23-0001_Z1.pdf, 14780-8120-25-23-0002_Z1.pdf, 14780-8120-25-23-0010_Z1.pdf, 14780-8120-25-23-0010A_Z1.pdf, 14780-8120-25-23-0012_Z1.pdf, 14780-8120-25-23-0012A_Z1.pdf, 14780-8120-25-23-0013_Z1.pdf, 14780-8120-25-23-0014_Z1.pdf, 14780-8120-25-23-0014A_Z1.pdf]
last_updated: 2026-06-07
---

# CDN Safety Instrumented System (SIS) Architecture

> ⚠️ CHP is a peroxide — all three SIS controllers below protect against CHP runaway. See [[hazards/cumene-hydroperoxide]].

**Sources:** Drawing 14780-8120-25-23-0001 (Unit Specific Details) + 0002 (Cause and Effect Table), Rev Z1 As-Built  
**Licensor:** UOP — basis STD DWG 963766-120-02-A1

> **SIS tag format note:** SIS initiators use the **XSHH / XSLL** format (e.g., TXSHH, FXSLL) — the **S** denotes a dedicated Safety transmitter, separate hardware from DCS (which uses XAHH/XALL). See [[instruments/cause-effect-cdn]] for complete cause-and-effect matrix.

---

## Overview

The CDN Unit has **three independent SIS Logic Controllers**, one per major hazard zone:

| Controller | Annunciator | Scope | Key Protection |
|-----------|------------|-------|----------------|
| **UC-2301** | UA-23-2301 | Concentration Section | CHP in high-temp evaporators; steam heater runaway |
| **UC-2302** | UA-23-2302 | Decomposition Section | Decomposer CHP runaway; loss of reaction control |
| **UC-2303** | UA-23-2303 | Vacuum Producing Equipment | Vacuum system failure; protection for P-2316/2317 |

Each controller has dedicated operator pushbuttons (HXS) and hardwired interlock outputs (HXL) for SIS-rated functions. DCS signals are connected in addition to the SIS for monitoring but are NOT substitutes for the hardwired SIS logic.

---

## UC-2301 — Concentration Section SIS

### Operator Interfaces
| Tag | Description |
|-----|-------------|
| HXS-0101 | **Emergency Shutdown** (key-operated) — Concentration Section |
| HXS-0102 | Feed to Preflash Column START |
| HXS-0103 | Cumene Quench RESET |

### Shutdown Trigger Inputs (cause) — from C&E Table, Drawing 0002

> See [[instruments/cause-effect-cdn]] for voting logic, time delays, and SIL ratings.

| SIS Tag | DCS Equivalent | Voting | Signal Type | Equipment | SIL |
|---------|---------------|--------|------------|-----------|-----|
| HXS-0101 | — | Manual | Emergency Shutdown key | — | — |
| FXSLL-0401A/B/C | FALL-0401 | **2oo3** | Flow LL | V-2301 feed | 1 |
| TXSHH-0501 | TAHH-0501 | 1oo1 | Temp HH | E-2302 Feed-Oxidate Exchanger vapor/liquid | 1 |
| TXSHH-0502A/B | TAHH-0502 | **1oo2** | Temp HH | E-2303 Steam Heater tube liquid | 1 |
| TXSHH-0404 | TAHH-0404 | 1oo1 | Temp HH | V-2301 bottom | 1 |
| LXSHH-0401 | LAHH-0401 | 1oo1 | Level HH | V-2301 | — |
| LXSHH-0802 | LAHH-0802 | 1oo1 | Level HH | V-2302 Flash Column bottom | — |
| PXSHH-0801 | PAHH-0801 | 1oo1 | Pressure HH | V-2302 vapor space | 2 |
| TXSHH-0701A/B, TXSHH-0702A/B | TAHH-0701/702 | **1oo2** | Temp HH | E-2304 Flash Vaporizer space/outlet | 2 |
| TXSHH-0805A/B | TAHH-0805 | **1oo2** | Temp HH | V-2302 Flash Column bottom | 2 |
| TXSHH-0901A/B | TAHH-0901 | **1oo2** | Temp HH | P-2301 Flash Bottoms Pump suction | — |
| UC-2201 | — | Cross-trip | Oxidizers Shutdown | From Oxidation Section | — |
| UC-2205 | — | Cross-trip | Decanter Shutdown | From Oxidation Section | — |

### Pumps Connected to UC-2301
| Pump | Service | Connection Type |
|------|---------|----------------|
| P-2308A | Preflash Steam Heater Condensate | SIS input + auto-start (FY-23-0502) |
| P-2308B | Preflash Steam Heater Condensate | SIS input + auto-start (FY-23-0502) |
| P-2309A | Flash Vaporizer Condensate | SIS input + auto-start (FY-23-0703) |
| P-2309B | Flash Vaporizer Condensate | SIS input + auto-start (FY-23-0703) |

### Safety Interlock Valves (UXVs) Controlled by UC-2301
| UXV | P&ID | Location |
|-----|------|----------|
| UXV-0302 | 0003 | Preflash Column Feed Filters |
| UXV-0401 | 0004 | Preflash Column (feed valve) |
| UXV-0501 | 0005 | Preflash Column Steam Heater |
| UXV-0502 | 0005 | Preflash Column Steam Heater (second) |
| UXV-0601 | 0006 | Concentration Cumene Quench Drum |
| UXV-0701 | 0007 | Flash Column Vaporizer |
| UXV-0702 | 0007 | Flash Column Vaporizer |
| UXV-0703 | 0007 | Flash Column Vaporizer |
| UXV-0704 | 0007 | Flash Column Vaporizer |
| UXV-0706 | 0007 | Flash Column Vaporizer |

---

## UC-2302 — Decomposition Section SIS

> ⚠️ This is the MOST CRITICAL SIS controller in CDN. Calorimeter temperature inputs are the primary safety signals for decomposer runaway prevention.

### Operator Interfaces
| Tag | Description |
|-----|-------------|
| HXS-0104 | **Decomposer Shutdown** (emergency) |
| HXS-0105 | Feed to Decomposer START |
| HXS-0106 | Cumene Flush to Decomposer Feed Line START |
| HXS-0107 | Cumene Flush to Concentrate Long Circulation Line START (key-operated, two-position) |
| HXS-0108 | Steam Enable/Shutoff |
| HXS-0109 | Decomposer Start-Up Bypass (bypass start-up interlock during commissioning/restart) |

### Shutdown Trigger Inputs (cause) — Decomposition — from C&E Table, Drawing 0002

> See [[instruments/cause-effect-cdn]] for full analysis. The C&E table is the authoritative source.

| SIS Tag | DCS Equivalent | Voting | Signal Type | Equipment | SIL |
|---------|---------------|--------|------------|-----------|-----|
| HXS-0104 | — | Manual ESD | Emergency Shutdown | — | — |
| FXSLL-1204 / FXSLL-1205 | FALL-1204 | **2oo3** | Flow LL (Thermal Mass) | **6"-CHP-23-012001 main CHP feed line** (confirmed on Drawing 0012) | **2** |
| LXSHH-1302, LXSHH-1303 | LAHH-1302/3 | **1oo2** | Level HH | D-2304 Decomposer — **confirmed Drawing 0013** | **2** |
| TXSHH-1301A, TXSHH-1301B | TAHH-1301 | **1oo2** | Temp HH | D-2304 Decomposer — **confirmed Drawing 0013** | **2** |
| TXSLL-1301A, TXSLL-1301B | TALL-1301 | **1oo2** | Temp LL | D-2304 Decomposer (reaction extinction) — **confirmed Drawing 0013** | **2** |
| TXSHH-1402 | TAHH-1402 | 1oo1 | Temp HH | E-2308A/B Dehydrator outlet — **confirmed Drawing 0014** (shown as TXAHH-1402 with CRIT label on P&ID; safety-dedicated hardware carries S prefix) | **1** |
| FXSLL-1501, FXSLL-1601, FXSLL-1602 | FALL-1501/1601/1602 | **2oo3** | Flow LL | P-2305 Acid Injection discharge | **1** |
| PDXSHH-1701A/B/C | PDAHH-1701 | **2oo3** | Diff Pressure HH | E-2307 Decomposer Cooler | **2** |
| **TDXSHH-1801** | TDAHH-1801 | 1oo1 | **Diff Temp HH (Cal.1 Total DT)** | X-2308A/X-2309A Cal.1 (when in service) | **1** |
| **TDXSHH-1802** | TDAHH-1802 | 1oo1 | **Diff Temp HH (Cal.1 Inlet DT)** | X-2308A/X-2309A Cal.1 (when in service) | A |
| **TDXSHH-1803** | TDAHH-1803 | 1oo1 | **Diff Temp HH (Cal.2 Total DT)** | X-2308B/X-2309B Cal.2 (when in service) | A |
| **TDXSHH-1804** | TDAHH-1804 | 1oo1 | **Diff Temp HH (Cal.2 Inlet DT)** | X-2308B/X-2309B Cal.2 (when in service) | A |
| FXSLL-1803, FXSLL-1804 | FALL-1803/4 | — | Flow LL | Liquid feed to Calorimeters | — |
| LXSLL-1201 | LALL-1201 | 1oo1 | Level LL | D-2303 Decomposer Feed Flush Drum | A |
| UC-2301 | — | Cross-trip | Concentration Section ESD | From UC-2301 | — |
| PXSLL-1201 | PALL-1201 | 1oo1 | Pressure LL | Process water to Decomposer | — |

> **New vs. previous wiki entries:** PDXSHH-1701A/B/C (Decomposer Cooler DP), FXSLL-1803/1804 (Calorimeter feed flow), LXSLL-1201 (Feed Flush Drum level LL), and PXSLL-1201 (Process water pressure) are NEW initiators identified from the C&E table that were not in the earlier SIS page from Drawing 0001 alone.

### Pumps Connected to UC-2302
| Pump | Service | Connection Type |
|------|---------|----------------|
| P-2302A | Decomposer Circulation | Auto-start permissive (FY-23-1702), SIS |
| P-2302B | Decomposer Circulation | Auto-start permissive (FY-23-1702), SIS |

### Safety Interlock Valves (UXVs) Controlled by UC-2302
| UXV | P&ID | Location |
|-----|------|----------|
| UXV-0801 | 0008B | Preflash/Flash Columns Overhead Pumps area |
| UXV-0802 | 0008 | Flash Column |
| UXV-0803 | 0008 | Flash Column |
| UXV-0804 | 0008B | Flash Column Overhead |
| UXV-0805 | 0008B | Flash Column Overhead |
| UXV-1001 | 0010 | Vacuum Producing Equipment — **DCS-only reset: HXS-23-1001** (Note 6 Dwg 0010; no field reset) |
| UXV-1201A | 0012 | Flash Column Bottoms Line — **Primary CHP feed cutoff valve** |
| UXV-1201B | 0012 | Flash Column Bottoms Line — **Second CHP cutoff valve** (SIL verification redundancy, Rev S3) |
| UXV-1201C | 0012 | Flash Column Bottoms Line — **Redundancy valve for UXV-1201A** (Note 6 Dwg 0012: "dead zone between inlet of UXV-1201C and connection point to be minimized") |
| UXV-1202 | 0012 | Flash Column Bottoms Line |
| UXV-1203 | 0012 | Flash Column Bottoms Line (Detail 'U' valve, per Note 3 Dwg 0012) |
| UXV-1204 | 0012A | Decomposer Feed Flush Drum D-2303 — CHP inlet side (per Drawing 0001 valve list) |
| UXV-1206 | 0012A | Decomposer Feed Flush Drum D-2303 — closes on Decomposer ESD; UXY-1206 solenoid |
| UXV-1207 | 0012A | Decomposer Feed Flush Drum D-2303 — **Note 4 Drawing 0012A: DISSIMILAR CHECK VALVE** (design diversity from UXV-1206); UXY-1207 solenoid |
| **UXV-1205** | **0012** | **CHP feed line — ALSO the CHP Nitrogen Header/Regular N₂ boundary valve.** Previously described as "UV-1205 (manual)"; confirmed on Drawing 0012 as UC-2302 SIS valve. Closes on Decomposer ESD, simultaneously isolating CHP feed AND sealing the CHP N₂ circuit. |
| UXV-1301A | 0013 | Decomposer Drum D-2304 — **PRIMARY CHP feed cutoff** (confirmed Drawing 0013) |
| UXV-1301B | 0013 | Decomposer Drum D-2304 — redundant CHP feed cutoff (confirmed Drawing 0013) |
| UXV-1302 | 0013 | Decomposer Drum D-2304 — additional SIS isolation (confirmed Drawing 0013) |
| UXV-1401 | 0014 | Dehydrators E-2308A/B — closes on Decomposer ESD (confirmed Drawing 0014) |
| UXV-1402 | 0014A | Crude Product Cooler E-2309 — Note 4: dissimilar check valve (confirmed Drawing 0014A) |
| UXV-1403 | 0014A | Crude Product Cooler E-2309 — Note 5: key interlocked on operating valve set (confirmed Drawing 0014A) |

### Process Engineering Note on UC-2302 Logic
The Decomposer low-low temperature shutdown (TXSLL-1301A/B, SIL 2, 1oo2) is counter-intuitive but critical: a falling decomposer temperature means the acid catalyst has been diluted or circulation has reduced. Under these conditions, CHP can **accumulate** in the loop rather than decompose. The correct response is to cut CHP feed immediately and flush with cumene.

The acid injection flow low-low (FXSLL-1501/1601/1602, 2oo3 voting) covers the scenario where acid injection pumps fail. Without acid, decomposition stops → CHP accumulates → eventual temperature surge. Cutting CHP feed before accumulation becomes dangerous is the correct response.

**New from C&E Table (Drawing 0002):** The Decomposer Cooler differential pressure (PDXSHH-1701A/B/C, SIL 2, 2oo3) is a critical pre-failure indicator. Rising DP on [[equipment/E-2307]] means reduced cooling effectiveness — an early warning of approaching ESD. This should be monitored closely during operation.

---

## UC-2303 — Vacuum Producing Equipment SIS

### Scope
Protects the Concentration Vacuum Producing Equipment (X-2301) and associated pumps.

### Causes — from C&E Table (Drawing 0002)
| SIS Tag | Voting | Signal Type | Equipment |
|---------|--------|------------|-----------|
| LXSHH-1006 | 1oo1 | Level HH | Vacuum Equipment Separator |
| PDXSHH-1012 | 1oo1 | Diff Pressure HH | Vacuum Equipment Spill-Back Control |
| FXSLL-1008 | 1oo1 | Flow LL | Vacuum Equipment Sealant flow |
| TXSHH-1008 | 1oo1 | Temp HH | Vacuum Equipment Inlet temperature |
| HXS-1001 | Manual | Emergency Switch | Operator ESD |

### Pumps Connected to UC-2303
| Pump | P&ID | Service |
|------|------|---------|
| P-2316A | 0010A | Liquid ring vacuum pump — motor trip on UC-2303 ESD |
| P-2316B | 0010A | Liquid ring vacuum pump — motor trip on UC-2303 ESD |
| P-2317A | 0010A | Sealant pump — motor trip on UC-2303 ESD |
| P-2317B | 0010A | Sealant pump — motor trip on UC-2303 ESD |

**Annunciator:** UA-23-2303

### SIS Valve Controlled by UC-2303
| UXV | P&ID | Description | Reset |
|-----|------|-------------|-------|
| UXV-1001 | 0010 | Vacuum system isolation valve | **DCS-only: HXS-23-1001** (Note 6 Dwg 0010) |

### DCS-Only Restart Requirement (Drawing 0010A Note 7)
> **"RESET HAND SWITCH (ONLY DCS S/W) FOR P-2316A/B, P-2317A/B: HXS-23-2316"**

After ANY UC-2303 trip, all four vacuum system pumps (P-2316A/B and P-2317A/B) require DCS software hand switch HXS-23-2316 before restart. **No field restart capability.** This ensures:
1. Root cause of UC-2303 trip is assessed at DCS before the vacuum system is restored
2. The correct restart sequence (sealant pumps P-2317A/B first, then vacuum pumps P-2316A/B) is enforced
3. Columns V-2301 and V-2302 are confirmed to be in safe state before vacuum is re-applied

UC-2303 trip allows columns to rise toward atmospheric pressure — controlled re-application of vacuum requires gradual approach to avoid column hydraulic upsets.

---

## Key Operational Notes

1. **Startup sequence matters**: UC-2302 requires CHP feed permissive (P-2302 running) before UXV-1301 opens. HXS-0105 ("Feed to Decomposer Start") enables this permissive.

2. **Cumene flush sequence**: When decomposer shuts down, HXS-0106 and HXS-0107 initiate cumene flush to clear CHP from feed lines and concentrate circulation line. This prevents CHP crystallization and heat-up in stagnant lines.

3. **Decomposer heat-up bypass**: HXS-0109 (key-operated) bypasses the start-up interlock during controlled heat-up. This key must be removed (interlock re-enabled) before normal operation. See HL-Q1089 (Heatup Override Enabled indicator).

4. **SIL Verification changes (Rev S3)**: Redundancy valve UXV-1201B added on CHP feed line per SIL verification result. LSL-23-1201 permissive signal added for decomposer start-up. These were late additions to ensure adequate SIL rating.

---

## References

- [[sources/pid-cdn]] — Drawing 0001 (Unit Specific Details) + Drawing 0002 (C&E Table)
- [[instruments/cause-effect-cdn]] — Complete C&E matrix: voting logic, SIL ratings, effects
- [[units/cdn]]
- [[equipment/D-2304]] — Decomposer Drum (UC-2302 primary protection target)
- [[equipment/E-2307]] — Decomposer Cooler (PDXSHH-1701 — SIL 2 initiator from C&E)
- [[equipment/X-2308]] — Calorimeters (TDXSHH-1801–1804 shutdown inputs)
- [[equipment/E-2303]] — Preflash Steam Heater (UC-2301 monitoring)
- [[hazards/cumene-hydroperoxide]]
