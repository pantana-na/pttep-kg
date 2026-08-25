---
name: CDN Pump Mechanical Seal Plans
unit: CDN
tags: [instruments, pumps, seal-plan, mechanical-seal, CDN]
sources: [14780-8120-25-23-0001I_Z1.pdf, 14780-8120-25-23-0001J_Z1.pdf, 14780-8120-25-23-0001K_Z1.pdf, 14780-8120-25-23-0001L_Z1.pdf, 14780-8120-25-23-0001_Z1.pdf]
last_updated: 2026-06-06
---

# CDN Pump Mechanical Seal Plans

**Source:** Drawings 0001I, 0001J, 0001K, 0001L, 0001 — Rev Z1 As-Built

> All seal plans include DCS logic for seal failure common alarm. Alarm activates on seal failure of either operating pump or spare pump.

---

## Seal Plan Summary

| Pump(s) | API Plan | Description | Service Reason |
|---------|---------|-------------|----------------|
| P-2304A | **74** | N₂ gas barrier seal | Acid Aromatics Sump — corrosive fluid, no liquid flush |
| P-2301A/B, P-2307A/B | **11/53A** | Pressurized dual, RCS flush | Hydrocarbon overhead/bottoms — CHP present |
| P-2302A/B | **11/53A** | Pressurized dual, most complex | Decomposer circulation — largest/most critical pumps |
| P-2303A/B | **2/53A** | Dead-ended inner + pressurized outer | Decomposer product — prevent seal fluid contamination |

---

## API Plan 74 — Nitrogen Gas Barrier (P-2304A)

**Drawing:** 0001I  
**Applied to:** P-2304A (Acid Aromatic Sump Pump) — P&ID 0020A

The only gas-barrier seal in CDN. Nitrogen from header 53-0051/2 is regulated by a PCV into the seal face. The inboard (process-side) fluid never contacts the atmospheric side.

### Instruments

| Tag | Description |
|-----|-------------|
| PCV-23-2002 | Nitrogen pressure control valve |
| FIF-23-2002 | Nitrogen flow indicator (totalizer) |
| FS-23-2003 | Nitrogen flow switch |
| FAH-23-2004 | Nitrogen flow alarm — High (excess flow = seal failure) |
| PG-23-2004 | Pressure gauge |
| PS-23-2005 | Pressure switch |
| PAL-23-2005 | Pressure alarm — Low (low N₂ pressure = barrier lost) |
| XS-23-2001 | Seal status indicator |

**Operational significance:** PAL activates immediately if nitrogen supply fails — this is the primary seal failure warning. If PAL triggers, the pump must be stopped immediately to prevent acid aromatic fluid from reaching atmosphere.

---

## API Plan 11/53A — Pressurized Dual (P-2301A/B, P-2307A/B)

**Drawing:** 0001J  
**Applied to:** P-2301A/B (Flash Column Bottoms Pumps, P&ID 0009) and P-2307A/B (Preflash & Flash Columns Overhead Pumps, P&ID 0008B)

Dual mechanical seal with inner + outer seal faces. Buffer reservoir pressurized by nitrogen. Cooling water provided to seal housing.

### Utilities Per Pump
- **Cooling Water Supply:** 1-1/2" RCS-61-054040 series (P-2301) or CWS-61-052148 series (P-2307)
- **Cooling Water Return:** 1-1/2" ROR-61-054041 series (P-2301) or CWR-61-052149 series (P-2307)
- **Nitrogen Supply:** 3/4"-N-53-052085 through 052098 series
- **Drain:** 3/4"-CHD-23-009005 / 008044 series → Drain Header

### Instruments (per pump — A side example)
| Instrument | P-2301A Tag | P-2307A Tag | Description |
|-----------|-------------|-------------|-------------|
| RO (restriction orifice) | 23-0902 | 23-0802 | Flow restriction to inner seal |
| LG (level gauge) | 23-0901 | 23-0801 | Buffer reservoir level |
| LS-A | 23-0902 | 23-0802 | Level switch (outer seal circuit) |
| LAH | 23-0903 | 23-0803 | Level alarm — High |
| LS-B | 23-0904 | 23-0804 | Level switch (inner seal circuit) |
| LAL | 23-0907 | 23-0807 | Level alarm — Low |
| PAL | 23-0904 | 23-0804 | Pressure alarm — Low |
| XS | 23-0901 | 23-0801 | Seal status |

---

## API Plan 11/53A — Pressurized Dual, Complex (P-2302A/B)

**Drawing:** 0001K  
**Applied to:** P-2302A/B (Decomposer Circulation Pumps, P&ID 0017) — **Most critical pump seal in CDN**

Full dual pressurized seal with four independent monitoring circuits (A, B, C, D) — more comprehensive than any other pump in CDN. This reflects the criticality of these HV motors and the consequence of seal failure on the running decomposer.

### Utilities Per Pump
- **Cooling Water Supply (per seal):** 1-1/2"-CWS-61-052140 to 052145 series
- **Cooling Water Return (per seal):** 1-1/2"-CWR-61-052141 to 052145 series
- **Nitrogen Supply:** 3/4"-N-53-053003 to 053006 series
- **Drain to Header:** 23-0021

### Instruments (P-2302A example — A and B circuits for each seal)
| Instrument | P-2302A Tags | Description |
|-----------|-------------|-------------|
| RO-A / RO-B | 23-1701 / 23-1704 | Restriction orifices (inner/outer seal circuits) |
| LG-A/B/C/D | 23-1701/1702/1703/1704 | Four level gauges (inner and outer seal, each side) |
| LS-A/B | 23-1702 / 23-1703 | Level switches |
| LS-C/D | 23-1706 / 23-1707 | Level switches (second seal) |
| LAH-A/B | 23-1702 / 23-1703 | Level alarm — High |
| LAL-C/D | 23-1706 / 23-1707 | Level alarm — Low |
| PI-A / PI-B | 23-1705 / 23-1708 | Pressure indicators |
| PS-A / PS-B | 23-1705 / 23-1708 | Pressure switches |
| PAL-A / PAL-B | 23-1705 / 23-1708 | Pressure alarm — Low |
| PCV | 23-1702 | Buffer pressure control valve |
| XS | 23-1701 | Seal status |

**Note:** P-2302B uses similar tags in the 23-1703 through 23-1712 range.

**Operational significance:** Any PAL on P-2302 seal must be investigated immediately. These pumps cannot be stopped without initiating decomposer shutdown first. A seal failure on a running decomposer requires a controlled shutdown sequence — not an emergency stop.

---

## API Plan 2/53A — Dead-Ended Inner + Pressurized Outer (P-2303A/B)

**Drawing:** 0001L  
**Applied to:** P-2303A/B (Decomposer Product Pumps, P&ID 0013)

Unique plan: the **inner seal chamber is dead-ended** (no flush recirculation). The inner seal faces are wetted by the process fluid (decomposer product) but the fluid is not recirculated. Outer seal pressurized with nitrogen. A "dead-ended with no flush" inner design is used when:
- Process fluid is acceptable as a seal lubricant but
- Recirculating it would cause unacceptable degradation or coke formation

For Decomposer Product (crude phenol + acetone + cumene + residual CHP), the dead-ended design prevents build-up from recirculation while the pressurized outer seal maintains emission control.

### Utilities Per Pump
- **Cooling Water Supply:** 1"-CWS-61-052136 (P-2303A) / 052138 (P-2303B)
- **Cooling Water Return:** 1"-CWR-61-052137 (P-2303A) / 052139 (P-2303B)
- **Nitrogen Supply:** 3/4"-N-53-053007 (P-2303A) / 053008 (P-2303B)
- **Drain to Header:** 3/4"-AD-23-013011/013012 → Header 23-0021

### Instruments
| Tag Range | Description |
|-----------|-------------|
| 23-1305/1306/1307/1308/1309 | P-2303A: RO, LG, LS, LAH, LS-B, LAL, PI, PS, PAL, PCV, XS |
| 23-1307/1308/1309/1310/1311 | P-2303B: same suite with offset tags |

---

## Seal Flush Fluid Types (from Drawing 0001 — Seal Flush Details)

### Detail "DD" — Dry Non-Contacting Pressurized Dual Tandem
Used when seal flush fluid is supplied by vendor (buffer/barrier fluid by vendor).

### Detail "DD-CHP" — Dry Non-Contacting Dual Tandem for CHP Service
Same as DD but uses **CHP Nitrogen** as the buffer gas. Applied where seals contact CHP-bearing streams. CHP Nitrogen comes from the dedicated CHP Nitrogen Header (see [[instruments/sis-cdn]] for CHP N₂ header note).

### Detail "DM" — Pressurized Dual (Double Mechanical) Seal
Seal flush system furnished by pump supplier. Uses nitrogen from header 53-0051/2. Drain to collection header via 1" silicone tubing. This is a common arrangement for standard CDN centrifugal pumps.

### Detail "DM-CHP" — Pressurized Dual for CHP Service
Same as DM but uses **CHP Nitrogen** as barrier gas. Note: 2002 tag refers to P-2304A and P-13045 (warehouse spare).

---

## References

- [[sources/pid-cdn]]
- [[equipment/P-2302]] — Decomposer Circulation Pumps (API Plan 11/53A, most complex)
- [[units/cdn]]
- [[hazards/cumene-hydroperoxide]]
