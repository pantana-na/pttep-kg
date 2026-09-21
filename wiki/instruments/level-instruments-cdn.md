---
name: CDN Level Instrument Register
unit: CDN
tags: [instruments, level, LT, LXT, LGR, radar, CDN]
sources: ["14780-8120-PS-0033_LEVEL INSTRUMENT PROCESS DATA SHEET (CDN)_Z1.pdf"]
last_updated: 2026-06-16
---

# CDN Level Instrument Register

**Source:** 14780-8120-PS-0033, Rev Z1 (AS-BUILT, May 2016), Refinery Phenol Train II, POSCO Engineering / UOP licensor basis. 22-page process specification covering DP/capillary level transmitters, one guided-wave radar transmitter, one thermal-dispersion shutdown switch, level gauges (reflex glass), and one level switch.

---

## Differential-Pressure / Capillary Level Transmitters (21 tags)

316SS or cadmium-plated CS/316SS wetted, silicone-filled capillary, 4–20 mA output, Honeywell/Rosemount (or equal). X-prefixed tags (LXT) are SIS-qualified instruments feeding the UC-2301/2302 logic; non-X tags (LT) are DCS-only.

| Tag | Service | Calibrated Range | Process Temp | Process Press | Sealing Leg | Equipment |
|-----|---------|-------------------|--------------|----------------|-------------|-----------|
| LT-23-0803 | Preflash/Flash Columns Condenser Liquid Boot | 0–207 mBar | 38°C | -1.0 kg/cm²(g) | — | [[equipment/E-2301]] |
| LT-23-2002 | Acid Aromatics Knockout Drum | 0–164 mBar | 38°C | 0.01 kg/cm²(g) | — | [[equipment/D-2306]] |
| LT-23-0601 | Concentration Cumene Quench Drum | 12–74 mBar | 46°C | 0.07 kg/cm²(g) | Cumene ref. leg, 400mm level range, SG 0.841 | [[equipment/D-2301]] |
| LT-23-0501 | Preflash Column Steam Heater Condensate Drum | 60–370 mBar | 117°C | 0.9 kg/cm²(g) | Water ref. leg, 800mm range, SG 0.947 | [[equipment/D-2308]] |
| LT-23-0701 | Flash Column Vaporizer Condensate Drum | 60–370 mBar | 135°C | 2.3 kg/cm²(g) | Water ref. leg, 800mm range, SG 0.931 | [[equipment/D-2309]] |
| LT-23-1101 | Cumene Flush Drum | 60–370 mBar | 10°C | 0.7 kg/cm²(g) | Cumene ref. leg, 4200mm range, SG 0.841 | [[equipment/D-2302]] |
| LXT-23-1201 | Decomposer Feed Flush Drum | 60–370 mBar | 46°C | 0.7 kg/cm²(g) | Cumene ref. leg, 1400mm range, SG 0.841 | [[equipment/D-2303]] |
| LXT-23-1303 | Decomposer Drum | 0–36 mBar | 60°C | 0.7 kg/cm²(g) | Decomposer liquid ref. leg, 400mm range, SG 0.920 | [[equipment/D-2304]] |
| LT-23-1301 | Decomposer Drum | 0–72 mBar | 60°C | 0.7 kg/cm²(g) | Decomposer liquid ref. leg, 800mm range, SG 0.920 | D-2304 |
| LXT-23-1302 | Decomposer Drum | 0–36 mBar | 60°C | 0.7 kg/cm²(g) | Decomposer liquid ref. leg, 400mm range, SG 0.920 | D-2304 |
| LT-23-0402 | Preflash Column Bottom | 0–107 mBar | 70°C | -1.0 kg/cm²(g) | Capillary, max fill temp 250°C | [[equipment/V-2301]] |
| LT-23-0403 | Preflash Column Bottom | 0–107 mBar | 70°C | -1.0 kg/cm²(g) | Capillary, max fill temp 250°C | V-2301 |
| LT-23-0801 | Flash Column Bottom | 0–219 mBar | 95°C | -0.24 kg/cm²(g) | Capillary, max fill temp 125°C | [[equipment/V-2302]] |
| LXT-23-0802 | Flash Column Bottom | 0–219 mBar | 95°C | -0.24 kg/cm²(g) | Capillary, max fill temp 125°C | V-2302 |
| LT/LI-23-1501 | Decomposer Acid Injection Tote | 0–168 mBar | 30°C | 0.01 kg/cm²(g) | Capillary, max fill temp 120°C | [[equipment/D-2310]] / [[equipment/D-2311]] |
| LT/LI-23-1901 | Neutralizing Agent Injection Tote | 0–168 mBar | 30°C | 0.01 kg/cm²(g) | Capillary, max fill temp 120°C, SG 0.8488 | [[equipment/D-2312]] |

> **D-2304 has three independent level transmitters confirmed**: LT-23-1301 (DCS, 800mm span) plus LXT-23-1302 and LXT-23-1303 (SIS-qualified, 400mm span each). These correspond to the already-recorded SIS tags **LXSHH-1302 / LXSHH-1303** (Level High-High, 1oo2, SIL 2) on [[equipment/D-2304]] — this data sheet closes the instrument-data gap for those switches by confirming physical transmitter ranges and the shared Decomposer-liquid reference-leg fill (SG 0.920).
>
> **V-2301 and V-2302 bottoms each carry a redundant pair**: V-2301 = LT-23-0402 (DCS) + LT-23-0403 (also DCS — both non-X despite the equipment page's "LXI/LX-0401" SIS designations referring to a *separate* upper-section level loop, not these two bottom-of-column instruments); V-2302 = LT-23-0801 (DCS) + LXT-23-0802 (SIS, feeds LXSHH-0802).

## Radar Level Instrument (1 tag)

| Tag | Service | Type | Measurement Length | Fluid | Process Temp/Press | Design Temp/Press | Equipment |
|-----|---------|------|---------------------|-------|----------------------|---------------------|-----------|
| LT-23-2001 | Acid Aromatics Sump | Guided-wave (TDR) radar, coaxial/twin-rod, 3" 300RF, 316/316L SS wetted | 2100 mm; 100% level = top of horizontal section | Acetone, Phenol, CHP, Cumene, H₂SO₄ (trace), H₂O — non-coating, non-bridging | 38°C / 0.01 kg/cm²(g) | 325°C / 3.5 kg/cm²(g) | [[equipment/D-2307]] |

Supplier: Magnetrol (or equal). Response <1s, linearity <0.1% of probe length, repeatability ±0.1 inch. **This is the named tag for the "Radar Level — Primary level measurement on D-2307" entry already recorded on [[equipment/D-2307]]** — confirms it is the primary, not secondary, level signal on that vessel, and that the measured fluid mix includes the full range of CHP-decomposition-derived chemicals (consistent with D-2307 collecting all CDN acid-aromatics drains).

## Alarm and Shutdown Switch (1 tag)

| Tag | Service | Type | Operating Conditions | Equipment |
|-----|---------|------|------------------------|-----------|
| LXSHH-23-0401 | Preflash Column Bottom | Thermal Dispersion level switch, hermetically sealed SPDT relay, 316L SS sensor, 2" 300RF | -1.0 kg/cm²(g) / 70°C; design 3.5 kg/cm²(g), FV / 250, 195°C | [[equipment/V-2301]] |

Supplier: Endress + Hauser (or equal). Switch relay **de-energizes and contacts open when level rises above the switch** — fail-safe high-level alarm action. This is the data sheet for the already-recorded **LXSHH-0401** SIS tag on [[equipment/V-2301]] (UC-2301 Trigger, Cause 5).

## Level Gauges — Reflex Type (13 tags)

Per local gauge-glass data sheet 14780-8550-DS-0008.

| Tag | Service | Equipment |
|-----|---------|-----------|
| LGR-23-0502 | Preflash Column Steam Heater Condensate Drum | [[equipment/D-2308]] |
| LGR-23-0602 | Concentration Cumene Quench Drum | [[equipment/D-2301]] |
| LGR-23-0702 | Flash Column Vaporizer Condensate Drum | [[equipment/D-2309]] |
| LGR-23-0703 | Sample Receiver | — |
| LGR-23-0804A/B | Preflash & Flash Columns Condenser Liquid Boot | [[equipment/E-2301]] |
| LGR-23-1102A/B/C | Cumene Flush Drum | [[equipment/D-2302]] |
| LGR-23-1202 | Decomposer Feed Flush Drum | [[equipment/D-2303]] |
| LGR-23-1304A/B/C | Decomposer Drum | [[equipment/D-2304]] |
| LGR-23-2003A/B | Acid Aromatics Knockout Drum | [[equipment/D-2306]] |

## Level Switch (1 tag)

| Tag | Service | Fluid | Process Temp/Press | Design Temp/Press | Equipment |
|-----|---------|-------|-----------------------|----------------------|-----------|
| LS-23-2005 | Acid Aromatics Sump Pit | Water, SG 1 | AMB / 0.01 kg/cm²(g) | 120°C / 3.5 kg/cm²(g) | [[equipment/X-2321]] |

> **Clarification:** The data sheet's service description ties LS-23-2005 to **X-2321 (Acid Aromatics Sump Pit)**, while [[equipment/D-2307]]'s page (and the equipment table entry for [[equipment/P-2304A]]) describes "LS-2005" as the LOW LEVEL STOP protecting P-2304A's suction from **D-2307 (Acid Aromatics Sump)**. These may be the same tag serving both functions, or two related-but-distinct instruments sharing a similar number. Flagged for verification against the physical field tag before relying on this for HAZOP safeguard credit on either vessel.

## References

- [[sources/ps-pressure-level-temp-instrument-cdn-batch-2026-06-16]] — source summary
- [[instruments/cause-effect-cdn]] — SIS-side level tags (LXSHH series)
- [[equipment/D-2304]], [[equipment/V-2301]], [[equipment/V-2302]], [[equipment/D-2307]], [[equipment/X-2321]] — equipment-level cross-references
