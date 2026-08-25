---
name: CDN Sampling Connection Details
unit: CDN
tags: [instruments, sampling, CDN, laboratory]
sources: [14780-8120-25-23-0001D_Z1.pdf, 14780-8120-25-23-0001E_Z1.pdf]
last_updated: 2026-06-06
---

# CDN Sampling Connection Details

**Source:** Drawings 0001D (1/2) and 0001E (2/2) — Rev Z1 As-Built

---

## Sampling Point Register

| Point | P&ID | Service / Stream | Fluid Code | Sample Type | Safety Note |
|-------|------|-----------------|-----------|------------|-------------|
| SN-2301 | 0008B | Preflash & Flash Column Overhead Pumps | CUL (Cumene) | A-AC without cooler | — |
| SN-2303 | 0009 | Flash Column Bottoms Pumps | CHP (Conc. CHP) | A-CH without cooler + flush | ⚠️ CHP — concentrated peroxide |
| SN-2304 | 0004 | Preflash Column feed/reflux area | Process | A-AC without cooler | — |
| SN-2305 | 0017 | Decomposer Circulation line | Process (CHP present) | A-AC with cooler | ⚠️ Hot stream |
| SN-2306 | 0019 | Neutralization area | CP (Crude Product) | A-AC without cooler | — |
| SN-2307 | 0020A | Acid Aromatics Sump | PL | A-AC without cooler | Corrosive — acid aromatic |
| SN-2308 | 0017 | Decomposer area | RCR (Recirculation) | B-SW without cooler | Process |
| SN-2309 | 0014A | Crude Product Cooler | CWR (Cooling Water Return) | B-SW without cooler | — |
| SN-2310 | 0007 | Flash Column Vaporizer area | PL (Phenol-containing) | B-AC with cooler | ⚠️ Phenol — skin absorption |
| SN-2311 | 0020 | Acid Aromatics Knockout Drum | Process | A-AC without cooler | Corrosive |

---

## Sampling Connection Types

### Type A-AC — Without Cooler (Liquid Hydrocarbon, Ambient or Low Temp)

**Used for:** SN-2301, SN-2304, SN-2306, SN-2307, SN-2311

Flow path:
- Process pipe nozzle → ¼" needle valve → flexible hose → **500 cc evacuated or N₂-purged sample container**
- Delta-P device to ensure sufficient flow through the sample loop
- Piping: ¾" size, on vertical or horizontal pipe as noted

Notes:
- For operating pressure **< 125 kg/cm²g**: Swagelok quick-connects (SS-QM4)
- For operating pressure **≥ 125 kg/cm²g**: Swagelok SS-QTS-4 or SS-OGT4
- All sample tubing shall be placed on **vertical piping** (liquid samples) or on **side or top of horizontal pipe** (gas samples)
- Sample bomb: 500 cc, 316/316L, 1/4" female NPT 1800 psi
- Quick connector: A182 F316/316L, 3000 psi — male NPT both ends
- Sample cylinder saddle: A351 CF8

### Type A-CH — Without Cooler (Cumene/Hydrocarbon With Flush)

**Used for:** SN-2303 (Flash Column Bottoms — CHP stream)

Same as A-AC but with an additional **flushing connection** using CUL (Cumene) line. Purpose: flush the sample lines with cumene before and after taking the sample to prevent CHP from remaining in the sample tubing (fire/explosion risk from CHP in deadleg).

> ⚠️ **SN-2303 is the most hazardous sampling point in CDN.** It handles concentrated CHP (≈60–80 wt%). All sampling of this point requires following the CHP sampling procedure with full PPE, double-block valve verification, and cumene pre-flush and post-flush. See [[hazards/cumene-hydroperoxide]].

Flushing line: 3/4"-CUL-22-027032 series → appropriate drain sump

### Type A-AC — With Cooler (Hot Liquid Hydrocarbon)

**Used for:** SN-2305 (Decomposer Circulation)

Same as A-AC but includes a **CWS/CWR sample cooler** in the sample loop. Reduces sample temperature before the flexible hose and container.

Coolant supply: 3/4"-CWS-61-052183(4)-MS1-NI  
Coolant drain: returns to CWR header

> **SN-2305** is on the Decomposer Circulation line — very hot stream, requires sample cooler. The stream contains crude product (phenol, acetone, cumene) with potentially residual CHP.

### Type B-SW — Without Cooler (Sour Water / Cooling Water Return)

**Used for:** SN-2308 (Decomposer area, RCR line), SN-2309 (Crude Product Cooler, CWR line)

For sour water streams or cooling water return where fluid temperature is manageable without cooling. Drain routes to SWS (Sour Water Sewer) rather than to CHP closed drain.

Sample details:
- SN-2308: P&ID 0017, sampling line 3/4"-RCR-23-017023-MS1-NI → drain to SWS → D-2206
- SN-2309: P&ID 0014A, line 3/4"-CWR-23-014032-MS1-NI → drain to SWS

### Type B-SW — With Cooler (Hot Process Stream, Sour Water Drain)

**Used for:** SN-2310 (Flash Column Vaporizer area — Phenol-containing stream)

> ⚠️ **SN-2310 samples a Phenol Line (PL).** The stream from P&ID 0007 contains phenol. Use appropriate PPE — phenol absorbs through skin rapidly. See [[hazards/phenol]].

Includes:
- CWS/CWR cooler with CWS line 3/4"-CWS-61-052234-MS1-NI
- Coolant drain: SWS → D-2206
- Depressure line provision

---

## General Sampling Requirements (All Types)

1. Sampling system length must be minimum to limit product lost when flushing
2. Route drain to appropriate flare header
3. Where sample cooler is required — suction in to be personnel protected
4. Sample container shall be provided (500 cc evacuated or N₂-purged)
5. Type of valve: Gate (default), Ball if noted in table
6. All sampling bombs shall be equipped with block valves on each side
7. Cooling box shall be internally covered with "epoxy"
8. A support for the cylinder "bomb" shall be foreseen
9. All low-point drain in CHP service must connect to the CHP closed drain header

---

## Drain and Sump Routing Summary

| Sample Point(s) | Drain Sump | Notes |
|----------------|-----------|-------|
| SN-2301 | D-2306 / D-2206 | Via CHD drain line |
| SN-2303 | D-2206 | Via CHD drain + cumene flush drain |
| SN-2304 | D-2307 | |
| SN-2305 | D-2307 | CWR also to CWR header |
| SN-2306, 2307 | D-2307 | |
| SN-2308, 2309 | D-2206 (SWS) | Sour water routing |
| SN-2310 | D-2206 (SWS) | Via CWR drain |
| SN-2311 | D-2307 | |

---

## References

- [[sources/pid-cdn]]
- [[units/cdn]]
- [[hazards/cumene-hydroperoxide]] — For SN-2303 (CHP sampling)
- [[hazards/phenol]] — For SN-2310 (phenol sampling)
