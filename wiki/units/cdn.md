---
name: CDN — Concentration, Decomposition, and Neutralization Section
code: CDN
tags: [unit, concentration, decomposition, neutralization, cleavage]
sources: [14780-8120-20-23-0001_Z1.pdf, 14780-8120-20-23-0002_Z1.pdf, 14780-8120-20-23-0003_Z1.pdf, 14780-8120-20-23-0004_Z1.pdf, 14780-8120-20-23-0005_Z1.pdf, 14780-8120-20-23-0006_Z1.pdf, 14780-8120-25-23-0001_Z1.pdf, 14780-8120-25-23-0002_Z1.pdf, 14780-8120-25-23-0003_Z1.pdf, 14780-8120-25-23-0004_Z1.pdf, 14780-8120-25-23-0005_Z1.pdf, 14780-8120-25-23-0005A_Z1.pdf, 14780-8120-25-23-0006_Z1.pdf, 14780-8120-25-23-0007_Z1.pdf, 14780-8120-25-23-0007A_Z1.pdf, 14780-8120-25-23-0008_Z1.pdf, 14780-8120-25-23-0008A_Z1.pdf, 14780-8120-25-23-0008B_Z1.pdf, 14780-8120-25-23-0009_Z1.pdf, 14780-8120-25-23-0010_Z1.pdf, 14780-8120-25-23-0010A_Z1.pdf, 14780-8120-25-23-0011_Z1.pdf, 14780-8120-25-23-0012_Z1.pdf, 14780-8120-25-23-0012A_Z1.pdf, 14780-8120-25-23-0013_Z1.pdf, 14780-8120-25-23-0014_Z1.pdf, 14780-8120-25-23-0014A_Z1.pdf, OM-Phenol Unit UOP-2015.pdf]
last_updated: 2026-06-13
---

# CDN — Concentration, Decomposition, and Neutralization Section

> ⚠️ CHP is a peroxide — thermal decomposition risk in all three sub-sections. See [[hazards/cumene-hydroperoxide]].

**Technology Licensor:** UOP (Universal Oil Products) — Basis documents: 963766-110-01 to 06-A1  
**Plant:** PTT Phenol Train II (PPCL) — [[project]]

## Purpose

The CDN section converts dilute oxidate (Cumene Hydroperoxide ~22.6 wt% in Cumene) from the Oxidation Section into crude product (Phenol + Acetone mixture) ready for fractionation. It has three sequential sub-sections:

1. **Concentration** — remove excess Cumene from oxidate to produce concentrated CHP (~80–85 wt%) for the Decomposer
2. **Decomposition** — acid-catalyzed conversion of CHP to Phenol and Acetone in a high-recirculation loop reactor
3. **Neutralization** — neutralize residual acid catalyst and separate acid aromatics before sending crude product to Fractionation

---

## Sub-Section 1: Concentration

### Purpose
Remove ~95% of the Cumene from the oxidate feed, concentrating CHP from ~22.6 wt% to ~80–85 wt%. Recovered Cumene is recycled to the Oxidation Section feed wash column.

### Process Description
Oxidate from the Oxidation Section (Stream 229, ~1,076,643 kg/h at 83°C) is preheated in the **Feed-Oxidate Exchangers (E-2302A/B)** and passed through **Preflash Column Feed Filters (X-2302A/B)** before entering the **Preflash Column (V-2301)**.

**Preflash Column (V-2301):** First-stage vacuum evaporator. Steam heating provided by **Preflash Column Steam Heater (E-2303)**. Overhead vapors (mainly Cumene) are condensed in the **Preflash and Flash Columns Condenser (E-2301)** and returned as recycle Cumene. The partially concentrated oxidate leaves as column bottoms.

**Flash Column (V-2302):** Second-stage vacuum evaporator. Operates under deeper vacuum maintained by the **Concentration Vacuum Producing Equipment (X-2301)**. Heat input from the **Flash Column Vaporizer (E-2304)**. Overhead Cumene vapors condensed in E-2301 and further chilled in **Flash Column Overhead Vapor Chiller (E-2310)**. Overhead condensate pumped by **Preflash and Flash Columns Overhead Pumps (P-2307A/B)**; net overhead is recycle Cumene (Stream 350) back to Oxidation Section.

**Flash Column Bottoms (Stream 372, ~60,873 kg/h at 60°C):** This is the concentrated CHP stream, pumped by **Flash Column Bottoms Pumps (P-2301A/B)** to the **Concentration Cumene Quench Drum (D-2301)** and then to the Decomposition sub-section.

**Recycle Cumene (Stream 350, ~140,798 kg/h):** Returned to Feed Wash Column V-2201 at Oxidation Section.

### Key Equipment — Concentration
| Tag | Description |
|-----|-------------|
| V-2301 | Preflash Column | [[equipment/V-2301]] |
| V-2302 | Flash Column | [[equipment/V-2302]] |
| E-2306 | Flash Column Bottoms Cooler (0.75 MM kcal/h) | [[equipment/E-2306]] |
| D-2309 | Flash Column Vaporizer Condensate Drum | [[equipment/D-2309]] |
| P-2309A/B | Flash Column Vaporizer Condensate Pumps | [[equipment/P-2309AB]] |
| D-2301 | Concentration Cumene Quench Drum | [[equipment/D-2301]] |
| D-2309 | Flash Column Condensate Drum | |
| E-2301 | Preflash and Flash Columns Condenser (16.52 MM kcal/h) | |
| E-2302A/B | Feed-Oxidate Exchangers (3.99 MM kcal/h total) | [[equipment/E-2302AB]] |
| E-2303 | Preflash Column Steam Heater (6.10 MM kcal/h) | [[equipment/E-2303]] |
| E-2304 | Flash Column Vaporizer (4.15 MM kcal/h) | [[equipment/E-2304]] |
| E-2310 | Flash Column Overhead Vapor Chiller (0.29 MM kcal/h); 224.4 m²; C(50)/C(50) cold insulation; 125m pipe limit from E-2301 | [[equipment/E-2310]] |
| X-2301 | Concentration Vacuum Producing Equipment (two-stage: ejectors J-2301/J-2302A/B + liquid ring pumps P-2316A/B); AI-1001 O2 analyzer; non-condensibles to charcoal adsorber; UC-2303 SIS; DCS-only restart HXS-23-2316 | [[equipment/X-2301]] |
| P-2316A/B | Liquid Ring Vacuum Pumps (55 kW, Ex nA, 79.7→804 mmHgA); UC-2303 SIS; DCS-only restart | [[equipment/P-2316AB]] |
| P-2317A/B | Sealant Pumps for vacuum system (3.35 m³/hr, 1.85 kW); UC-2303 SIS; DCS-only restart | [[equipment/P-2317AB]] |
| P-2301A/B | Flash Column Bottoms Pumps — **Reliable Power Supply; TXSHH-0901A/B SIS at suction; SN-2303 CHP sample** | [[equipment/P-2301AB]] |
| P-2307A/B | Preflash and Flash Columns Overhead Pumps — CHP analyzer AI-0801A/B on discharge; UXV-0804/0805 UC-2302 SIS | [[equipment/P-2307AB]] |
| D-2308 | Preflash Column Steam Heater Condensate Drum | [[equipment/D-2308]] |
| P-2308A/B | Preflash Column Steam Heater Condensate Pumps | [[equipment/P-2308AB]] |
| X-2302A/B | Preflash Column Feed Filters | [[equipment/X-2302AB]] |
| P-2309A/B | Flash Column Vaporizer Condensate Pumps | |
| P-2316A/B | Vacuum System Pumps (on P&ID 0010A) | |
| P-2317A/B | Vacuum System Pumps (on P&ID 0010A) | |
| X-2301 | Concentration Vacuum Producing Equipment | |

### Concentration Operating Parameters
| Parameter | Value | Unit | Stream | Source |
|-----------|-------|------|--------|--------|
| Oxidate Feed Temperature | 83 | °C | S229 | PFD-0001 |
| Oxidate Feed Flow | 1,076,643 | kg/h | S229 | PFD-0001 |
| Oxidate Feed Pressure | 78 | kg/cm²G | S229 | PFD-0001 |
| Oxidate CHP Content | ~22.6 | wt% | S229 | MB PFD-0006 |
| Recycle Cumene Flow (to OXI) | 140,798 | kg/h | S350 | PFD-0003 |
| Concentrated CHP (Flash Col. Bottoms) | 60,873 | kg/h | S372 | PFD-0004 |
| Flash Col. Bottoms Temperature | 60 | °C | S372 | PFD-0004 |
| Flash Column Operating Pressure | ~(17.0) | mm Hg vacuum | S336 | PFD-0003 |
| SC1.5 Steam (Preflash) | used | — | — | PFD-0001 |
| SC3 Steam (Flash Vaporizer) | used | — | — | PFD-0002 |

---

## Sub-Section 2: Decomposition

> ⚠️ This is the highest-hazard sub-section. CHP decomposition is highly exothermic. Loss of recirculation with CHP present can cause thermal runaway. See [[hazards/cumene-hydroperoxide]].

### Purpose
Convert concentrated CHP to Phenol and Acetone using dilute acid catalyst (H₂SO₄) in a high-recirculation loop reactor (Decomposer Drum D-2304).

### Process Description
Concentrated CHP from the Concentration sub-section passes through the **Cumene Flush Drum (D-2302)** and **Decomposer Feed Flush Drum (D-2303)** before entering the **Decomposer Drum (D-2304)**.

**Calorimeters (X-2308A/B):** Two small test reactors that continuously measure the decomposition reactivity of the incoming CHP stream. Their output (decomposition rate signal) feeds a **High Signal Selector** which determines the required acid injection rate and/or decomposer conditions. This is the primary process control mechanism for decomposition intensity.

**Decomposer Drum (D-2304):** Large loop reactor with **very high recirculation ratio (~30:1)** maintained by **Decomposer Circulation Pumps (P-2302A/B)**. The high dilution ratio keeps instantaneous CHP concentration extremely low (~1–3 wt%) at any point in the reactor, which is the primary safety mechanism.

```
CHP Feed (S379): 61,248 kg/h
Circulation (S380): 1,887,481 kg/h
Recirculation Ratio: ~30.8 : 1
```

**Acid injection:** Dilute H₂SO₄ injected via **Decomposer Acid Injection Pumps (P-2305A/B/C/D/E/F)** into the Decomposer. Injection rate controlled by Ratio Controller linked to Calorimeter signal.

**Temperature profile:**
- Decomposer inlet (S380): ~60°C
- After reaction zone (S384): ~72°C → temperature rise ~12°C (exotherm)
- After Decomposer Cooler (S387): ~58°C

**Decomposer Cooler (E-2307, 18.59 MM kcal/h):** Removes decomposition heat from the recirculating product. This is the largest heat exchanger duty in the CDN section.

**Dehydrators (E-2308A/B) and Dehydrator Reactor Loop (X-2312):** After the Decomposer, crude product passes through Dehydrators operating at **135–145°C** with **S4 Steam**. Purpose: convert DMBA (Dimethylbenzylcarbinol) to AMS + water, complete residual CHP decomposition, and remove water. Design temperature: 140–145°C, design pressure: 5.5 kg/cm²G.

**Crude Product Cooler (E-2309, with E-2309A/B):** Cools crude product from ~43°C for sending to Neutralization.

### Key Equipment — Decomposition
| Tag | Description |
|-----|-------------|
| X-2308A/B | Calorimeters (control instrument reactors) | [[equipment/X-2308]] |
| D-2302 | Cumene Flush Drum — cumene supply for line flushing (NOT in CHP flow path); 1500×4500mm; 0.7 kg/cm²g / 38°C op.; CHP N2 Header | [[equipment/D-2302]] |
| D-2303 | Decomposer Feed Flush Drum — 24"OD×1800mm; 0.7/38°C op.; LXSLL-1201 startup permissive (>85% span); UXV-1204/1206/1207 UC-2302; process water XY-1201 ratio | [[equipment/D-2303]] |
| D-2304 | Decomposer Drum (loop reactor) — 1900×4800mm; FV/11/250°C; X-2311 rupture disc 12.16 kg/cm²g; 3000mm safety elevation; TXSHH-1301A/B + TXSLL-1301A/B + LXSHH-1302/1303 SIS confirmed P&ID 0013 | [[equipment/D-2304]] |
| E-2307 | Decomposer Cooler (18.59 MM kcal/h) | [[equipment/E-2307]] |
| E-2308A/B | Dehydrators — 760×6096mm; 170 m²; 1 op+1 stdby; SC3 steam; H(50)/H(80); TXSHH-1402 SIS; UXV-1401; SN-2304 sample | [[equipment/E-2308AB]] |
| E-2309 | Crude Product Cooler — 860×6096mm; 227 m²; CWS Unit 61; UXV-1402/1403 UC-2302; SN-2309 sample | [[equipment/E-2309]] |
| X-2312 | Dehydrator Reactor Loop — 0.48 m³ total volume (flange to flange); middle loop = 0.24 m³ (Note 3 Dwg 0014A); residence time restricted (Spec 963766-840) | (data in [[equipment/E-2309]]) |
| P-2302A/B | Decomposer Circulation Pumps | [[equipment/P-2302]] |
| P-2303A/B | Decomposer Product Pumps — 75.1 m³/hr; 37 kW; Type B; API Plan 2/53A; Acid Aromatics Closed Drain Header | [[equipment/P-2303AB]] |
| P-2305A/B/C/D/E/F | Decomposer Acid Injection Pumps | |

### Decomposition Operating Parameters
| Parameter | Value | Unit | Stream | Source |
|-----------|-------|------|--------|--------|
| CHP Feed to Decomposer | 61,248 | kg/h | S379 | PFD-0004/0005 |
| CHP Feed Temperature | 60 | °C | S379 | PFD-0004 |
| Decomposer Circulation Flow | 1,887,481 | kg/h | S380 | PFD-0005 |
| Recirculation Ratio | ~30.8 | — | — | Calculated |
| Temp after Reaction Zone | 72 | °C | S384 | PFD-0005 |
| Temp after Decomposer Cooler | 58 | °C | S387 | PFD-0005 |
| Decomposer Cooler Duty | 18.59 | MM kcal/h | E-2307 | PFD-0005 |
| Dehydrator Temperature (normal) | 135 | °C | S416 | PFD-0005 |
| Dehydrator Temperature (design) | 140–145 | °C | S2414/2415 | PFD-0005 |
| Dehydrator Pressure (design) | 5.5 | kg/cm²G | S2415 | PFD-0005 |
| Dehydrator Duty (E-2308A/B) | 1.29 | MM kcal/h each | — | PFD-0005 |
| Dehydrator Reactor Loop Duty | 3.18 | MM kcal/h | X-2312 | PFD-0005 |
| Decomposer Acid Catalyst | Dilute H₂SO₄ | — | — | MB PFD-0006 |

### Safety Features — Decomposer
- **Safety Head (Bursting Disc)** on D-2304 — primary overpressure protection
- **Nitrogen blanketing** on D-2304 — inert atmosphere, pressure control
- **Calorimeter control** — measures decomposition reactivity to set acid dose; "High Signal Selector" picks highest calorimeter reading for conservative control
- **Auto/Start interlock** on Decomposer Circulation Pumps — must be running before CHP feed is admitted
- **CHP Nitrogen** blanketing on Cumene Flush Drum (D-2302)
- Decomposer drum vents "Absorbed Nitrogen" to Acid Aromatics Knockout Drum (D-2306)

---

## Sub-Section 3: Neutralization

### Purpose
Neutralize residual H₂SO₄ catalyst in crude product, separate acid aromatics, and send neutralized crude product to the Fractionation Section.

### Process Description
Crude product from the Decomposer passes through **Direct Neutralization Static Mixers (X-2310A/B)** where neutralizing agent is injected. Neutralizing agent sources:
- **Amine** (from Amine Tote via **Neutralizing Agent Injection Pumps P-2306A/B**)
- **Diamine** from Chemical Injection Treatment Tank (D-2408) at Fractionation Section

A **Ratio/Bias controller** combined with a **Signal Summing Device** maintains the correct neutralizing agent dose relative to the acid injection rate.

Stream 433 (neutralizing agent, 31°C, 2.8 kg/cm²G) is injected through Direct Neutralization Static Mixers (X-2310A/B).

Neutralized crude product passes through a **Sprung Phenol Coalescer (X-2508)** at the Phenol Recovery Section (see DWG 14780-8120-20-25-0003) before reaching **Fractionation Feed Tanks (TK-2401A/B)** at the Fractionation Section (DWG 14780-8120-20-24-0001).

**Acid Aromatics Knockout Drum (D-2306):** Receives relief and vent streams from the Decomposition Section. Separates acid aromatics from gas phase. Nitrogen blanketing maintained.

**Acid Aromatics Sump (D-2307):** Collects acid aromatics liquids. Pumped by **Acid Aromatics Sump Pump (P-2304A)** to Acid Aromatics Tank (TK-2502) at Phenol Recovery Section (DWG 14780-8120-20-25-0001). Nitrogen blanketed.

**Acid detector (AI-ACID):** On-line analyzer monitors acid concentration in crude product after neutralization.

### Key Equipment — Neutralization
| Tag | Description |
|-----|-------------|
| X-2310A/B | Direct Neutralization Static Mixers | |
| D-2306 | Acid Aromatics Knockout Drum | [[equipment/D-2306]] |
| D-2307 | Acid Aromatics Sump | |
| P-2304A | Acid Aromatics Sump Pump (P-13045 is warehouse spare) | |
| P-2306A/B | Neutralizing Agent Injection Pumps | |

### Neutralization Operating Parameters
| Parameter | Value | Unit | Stream | Source |
|-----------|-------|------|--------|--------|
| Crude Product to Fractionation | 63,255 | kg/h | S422 | PFD-0006 |
| Crude Product Temperature | 43 | °C | S422 | PFD-0006 |
| Acid Aromatics to TK-2502 | 1,994 | kg/h | S426 | PFD-0006 |
| Acid Aromatics Temperature | 41 | °C | S426 | PFD-0006 |
| Neutralizing Agent (Stream 433) | — | 31°C, 2.8 kg/cm²G | S433 | PFD-0006 |
| Neutralizing Agents Used | Amine + Diamine | — | — | PFD-0006 |

---

## Overall CDN Mass Balance (Key Streams)

From As-Built PFD-0006 Material Balance:

| Stream | Description | Temp (°C) | Mass Flow (kg/h) | MW |
|--------|-------------|-----------|------------------|----|
| S229 | Oxidate feed from Oxidation | 83 | 1,076,643 | 126.10 |
| S350 | Recycle Cumene to Oxidation | 39 | 140,798 | 120.21 |
| S372 | Conc. CHP (Flash Col. Btms) | 60 | 60,873 | — |
| S379 | CHP feed to Decomposer | 60 | 61,248 | — |
| S380 | Decomposer circulation | 60 | 1,887,481 | — |
| S384 | Decomposer (after Rx zone) | 72 | 1,826,477 | — |
| S387 | After Decomposer Cooler | 58 | 1,826,206 | — |
| S416 | To Dehydrators | 135 | 61,258 | — |
| S418 | After Dehydrators | 43 | 61,258 | — |
| S422 | Crude Product to Fractionation | 43 | 63,255 | 116.31 |
| S426 | Acid Aromatics to TK-2502 | 41 | 1,994 | — |

**CHP in Oxidate Feed (S229):** 1,600.81 kmol/h = ~22.6 wt%  
**Cumene in Oxidate Feed (S229):** 6,831.99 kmol/h = ~76.2 wt%

### Selected Material Balance by Component (kmol/h) — PFD-0006 As-Built

| Component | S229 (Feed) | S350 (Recycle Cumene) | S422 (Crude Product) |
|-----------|-------------|----------------------|---------------------|
| Water | 16.20 | TRACE | 94.40 |
| Nitrogen | 7.57 | — | — |
| Acetone | 0.16 | TRACE | (major product) |
| Phenol | — | — | (major product) |
| ACP (Acetophenone) | 7.20 | TRACE | 11.05 |
| AMS | 7.69 | TRACE | 1.20 |
| AMSO | 3.44 | 0.32 | 0.36 |
| Cumene | 6,831.99 | 1,171.28 | TRACE |
| CHP | 1,600.81 | 0.01 | — (fully converted) |
| DCP | 2.01 | TRACE | — |
| TOTAL mole flow | 8,538.25 | 1,417 | — |
| Mass flow (kg/h) | 1,076,643 | 140,798 | 63,255 |

---

## Inter-Section References

| Connection | To/From | Drawing Reference |
|------------|---------|------------------|
| Oxidate feed | FROM Oxidation (Oxidizer No.2) | 14780-8120-20-22-0002 |
| Recycle Cumene | TO Feed Wash Column V-2201, Oxidation | 14780-8120-20-22-0001 |
| Chilled water from Oxidation | FROM Oxidizer Chilled Vent Gas Sep. D-2211 | 14780-8120-20-22-0003 |
| Long circulation | TO Oxidizer No.2, Oxidation | 14780-8120-20-22-0002 |
| Decanter | TO D-2205, Oxidation Section | 14780-8120-20-22-0004 |
| Crude Product | TO Fractionation Feed Tanks TK-2401A/B | 14780-8120-20-24-0001 |
| Sprung Phenol Coalescer | AT Phenol Recovery Section X-2508 | 14780-8120-20-25-0003 |
| Diamine for neutralization | FROM D-2408, Fractionation Section | 14780-8120-20-24-0003 |
| Acid Aromatics | TO TK-2502, Phenol Recovery Section | 14780-8120-20-25-0001 |
| Process water | FROM P-2508A/B, Phenol Recovery Section | 14780-8120-20-25-0005 |
| Cumene overflow | TO TK-4104, Storage | 14780-8120-20-41-0012 |
| Sealant for X-2301 vacuum | FROM P-2204A/B, Oxidation | 14780-8120-20-22-0001 |

---

## Control Philosophy (from P&ID Standard Details — Drawing 0001)

### SIS Architecture
Three independent SIS logic controllers protect CDN. See [[instruments/sis-cdn]] for complete details.

| Controller | Annunciator | Scope |
|-----------|------------|-------|
| UC-2301 | UA-23-2301 | Concentration Section (Preflash, Flash, Steam Heater, Vacuum) |
| UC-2302 | UA-23-2302 | Decomposition Section (Decomposer, Dehydrators, Acid Injection) |
| UC-2303 | UA-23-2303 | Vacuum Producing Equipment (P-2316/2317) |

### Critical CHP Nitrogen Header Segregation
All nitrogen utility connections **upstream of UXV-1205** must connect to the **CHP Nitrogen Header** (sourced from Oxidation Section — see STD DWG 963766-120-01-A1). Connections downstream of UXV-1205 use the regular nitrogen header.

> ⚠️ **CORRECTION (confirmed Drawing 0012):** UXV-1205 is a **UC-2302 SIS valve** (not a manual valve as previously described). When the Decomposer ESD triggers, UXV-1205 closes — simultaneously cutting CHP feed AND sealing the CHP Nitrogen Header circuit from the downstream (regular N₂) zone. This is the physical enforcement of the N₂ segregation boundary during emergencies. Never connect regular nitrogen to any equipment upstream of UXV-1205.

### Pump Auto-Start Philosophy
- Decomposer Circulation P-2302A/B: **Auto-start** (FY-23-1702). Critical — must restore circulation within seconds of pump trip.
- Overhead Pumps P-2307A/B: **Type B — DCS-initiated LOW FLOW START only** (FAL-0802 alarm → operator or DCS starts standby). Drawing 0008B Note 2 explicitly states Type B. [CONFLICT: Motor control table Drawing 0001G may list as Type D — verify with field hardware]
- Flash Column Bottoms Pumps P-2301A/B: **Type B — no auto-start. On Reliable Power Supply (emergency bus).** Most hazardous pump in Concentration sub-section.
- Condensate Pumps P-2308A/B, P-2309A/B: Auto-start with SIS monitoring (Type L)
- Acid Injection Pumps P-2305A–F: **No auto-start** — manual restart required. Low acid pressure PXALL-23-1601 triggers decomposer ESD.

### Key Startup Sequence (Decomposer)
1. Establish Decomposer Circulation (P-2302A or B running)
2. Enable Feed to Decomposer via HXS-0105
3. Open CHP feed UXV-1301 (only opens with P-2302 running)
4. Calorimeters (X-2308A/B) begin measuring CHP reactivity
5. Acid injection rate set by Ratio Controller per calorimeter signal
6. Monitor TXAHH-1801/1802/1805 and TDXAHH-1803/1804 continuously

---

---

## Licensor Design Basis (GOM — UOP)

**Source:** UOP General Operating Manual (GOM), Rev 8 — [[sources/om-phenol-uop-2015]]
**Highest authority:** Licensor values supersede P&ID/PFD values where differences exist.

### Key Licensor Operating Limits (Summary)

For the full operating window table, see [[parameters/cdn-operating-windows]].

| Parameter | Normal | Limit / ESD | Unit | Source |
|-----------|--------|------------|------|--------|
| Flash zone pressure | 22–27 | — | mmHg | GOM §III |
| Flash column max temperature | — | 120 (ESD) | °C | GOM §XI |
| CHP in flash column bottoms | 80–84 | min 70 for decomposer feed | wt% | GOM §III, §X |
| Decomposer temperature | 60 | TSLL: 57 low ESD / 70 startup | °C | GOM §III, §XI |
| Decomposer pressure | 0.70 | — | kg/cm²(g) | GOM §VII |
| H₂SO₄ in circulating liquid | 40–60 | min 20 (danger) / 300 restart | wt ppm | GOM §III, §XI |
| CHP in circulating liquid | 1–1.5 | >2 wt% = instability | wt% | GOM §III |
| Water in circulating liquid | 1–2 | >2 wt% = instability | wt% | GOM §III |
| Calorimeter 1st stage ΔT (normal) | 7–10 | — | °C | GOM §VII |
| Dehydrator temperature | 125–145 | min 120°C | °C | GOM §III |
| DCP in crude product | 300–700 | max 900 (limited by o-cresol) | wt ppm | GOM §VII |
| Crude product pH (neutralization) | 2.3–2.7 | — | pH units | GOM §III |
| CHP in recycle cumene overhead | <1 | max 4 | wt% | GOM §VII |

### AMS Yield Target

UOP states ≥80 mole% AMS yield is achievable under the above conditions (GOM §VII.3).

### "Ready for Feed In" Conditions (After Any Shutdown)

Before restarting decomposer feed, ALL must be confirmed:

| Condition | Target |
|-----------|--------|
| Decomposer temperature | 70°C |
| H₂SO₄ concentration (bulk) | 300 wt ppm minimum (laboratory confirmed) |
| Water in circulating liquid | <2 wt% |
| Water injection rate | 0 kg/h (stopped) |
| Decomposer feed line | Flushed with cumene |

### Procedures (GOM-Sourced)

| Procedure | Link |
|-----------|------|
| Pre-commissioning / Commissioning | [[procedures/precommissioning-cdn]] |
| Start-up (Initial and Normal) | [[procedures/startup-cdn]] |
| Normal Operations | [[procedures/normal-operations-cdn]] |
| Normal Shutdown | [[procedures/normal-shutdown-cdn]] |
| Emergency Procedures | [[procedures/emergency-cdn]] |

### Troubleshooting (GOM-Sourced)

| Problem | Link |
|---------|------|
| Poor AMS yield | [[troubleshooting/cdn-poor-ams-yield]] |
| High acidity in flash column | [[troubleshooting/cdn-high-acidity-flash-column]] |
| Dehydrator plugging | [[troubleshooting/cdn-dehydrator-plugging]] |

---

## References
- [[sources/pfd-cdn]]
- [[sources/pid-cdn]]
- [[sources/om-phenol-uop-2015]] — UOP GOM (licensor authority)
- [[parameters/cdn-operating-windows]] — Full operating window table
- [[instruments/sis-cdn]] — SIS architecture
- [[instruments/pump-seal-plans]] — Pump seal plans
- [[instruments/motor-control]] — Motor control types and tags
- [[instruments/sampling-cdn]] — Sampling points
- [[equipment/P-2302]] — Decomposer Circulation Pumps
- [[project]]
- [[hazards/cumene-hydroperoxide]]
- [[hazards/phenol]]
