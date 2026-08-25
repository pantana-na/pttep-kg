---
name: Process Data Sheets — Rotating Equipment & Filters Batch (2026-06-16)
tags: [source, data-sheet, CDN, pump, filter, vacuum-system]
last_updated: 2026-06-16
---

# Source Summary — PS Rotating Equipment & Filters Batch (13 sheets, 2026-06-16)

**Files:** 13 process/project specification sheets sorted from `input/` → `raw/data_sheets/` (14780-8120-PS-* series, Rev Z1, As-Built, May 10, 2016).

**Source:** POSCO Engineering & Construction for PTT Phenol Train II (PPCL). UOP licence, Project Spec 963766. All sheets are UOP-branded "Project Specification" forms (centrifugal pumps form 501, proportioning pumps form 503, sealless pumps form 506, vacuum pumps form 511, filters form 912) co-issued with POSCO's "Process Specification" cover pages.

**Purpose:** Closes PSI Readiness Table A6.2-2 Item 4 (Equipment Data Sheets) for CDN rotating equipment (pumps) and static filters/vacuum package not previously covered by the 2026-06-14 static equipment batch.

## Files Ingested

| File | Item | Service |
|------|------|---------|
| PS-P2301 | P-2301A/B | Flash Column Bottoms Pumps |
| PS-P2302 | P-2302A/B | Decomposer Circulation Pumps |
| PS-P2303 | P-2303A/B | Decomposer Product Pumps |
| PS-P2304 | P-2304A | Acid Aromatics Sump Pump |
| PS-P2305 | P-2305A/B/C/D/E/F | Decomposer Acid Injection Pumps |
| PS-P2306 | P-2306A/B | Neutralization Agent Injection Pumps |
| PS-P2307 | P-2307A/B | Preflash and Flash Columns Overhead Pumps |
| PS-P2308 | P-2308A/B | Preflash Column Steam Heater Condensate Pumps |
| PS-P2309 | P-2309A/B | Flash Column Vaporizer Condensate Pumps |
| PS-P2320 | P-2320 | Acid Aromatics Sump Pit Pump |
| PS-X2301 | X-2301 | Concentration Vacuum Producing Equipment |
| PS-X2302 | X-2302A/B | Preflash Column Feed Filters |
| PS-X2309 | X-2309A/B | Calorimeter No.1/No.2 |

## Pages Updated (13)

All 13 corresponding equipment pages already existed (created 2026-06-06/07 from P&ID-only data) and were updated with a new "Process Data Sheet Confirmation" section each:

- [[wiki/equipment/P-2301AB]], [[wiki/equipment/P-2302]], [[wiki/equipment/P-2303AB]], [[wiki/equipment/P-2304A]], [[wiki/equipment/P-2305ABCDEF]], [[wiki/equipment/P-2306AB]], [[wiki/equipment/P-2307AB]], [[wiki/equipment/P-2308AB]], [[wiki/equipment/P-2309AB]], [[wiki/equipment/P-2320]], [[wiki/equipment/X-2301]], [[wiki/equipment/X-2302AB]], [[wiki/equipment/X-2308]] (tagged X-2309A/B — see tag history note on that page)

## Key Findings

- **Sealless magnetic-drive pumps confirmed:** P-2308A/B and P-2309A/B are API 685 sealless mag-drive pumps (SiC bearings, 316 SS containment shell, no mechanical seal) — corrects the earlier wiki assumption of a conventional seal plan on these condensate pumps.
- **Standby power supply (Motor Note M13)** confirmed on P-2301A/B, P-2302A/B, and P-2303A/B — all CHP/decomposer-product duty pumps. **Not present** on P-2307A/B (recycle cumene service), corroborating the existing "Reliable Power Supply: No" note on that page.
- **Acid metering pump metallurgy:** P-2305A–F (98% H₂SO₄) constructed in **Alloy 20**; P-2306A/B (diamine) in **316 SS** with an explicit prohibition on copper/copper-alloy wetted parts.
- **Calorimeter internal liner:** X-2309A/B (file `X-2308.md`) wetted internals are **Hastelloy C276** — not previously documented; addresses combined H₂SO₄/CHP corrosion severity.
- **P-2320 sump pump is Zone 1** (more hazardous than the surrounding CDN Zone 2 classification) — flagged for HAZOP node scoping.
- **Data conflicts identified** (PS value adopted as authoritative, flagged per Confidence Level convention):
  - P-2302A/B: capacity 2,020 m³/h (PS) vs 3,020 m³/hr (P&ID-era wiki entry); SG 0.906 vs 0.996; seal barrier Plan 53B vs previously noted 53A
  - P-2303A/B: motor power 37 kW (wiki) vs 23.8 kW rated hydraulic power (PS) — needs field verification
  - P-2304A: differential pressure 7.53 (PS) vs 3.53 kg/cm²g (wiki); SG 0.926 vs 0.826
  - P-2309A/B: rated capacity 13.3 m³/hr (PS) vs 15.3 m³/hr (wiki)
  - P-2320: differential pressure 0.99 (PS) vs 0.69 kg/cm²g (wiki)

## References

- [[wiki/index]]
- [[wiki/hazop/study-info]] — PSI Readiness Table A6.2-2 Item 4 status
