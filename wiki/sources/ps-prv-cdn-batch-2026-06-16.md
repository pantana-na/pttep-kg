---
name: Process Data Sheet — CDN Pressure Relief Valves (2026-06-16)
description: Source summary for the CDN Pressure Relief Valve / rupture disc process data sheet — closes the PSV set pressure TBC gap and resolves several set-pressure/discharge-destination conflicts
metadata:
  type: source
tags: [source, instrument, data-sheet, PSV, relief, CDN, PSI, HAZOP]
sources: ["14780-8120-PS-0018_PRESSURE RELIEF VALVE PROCESS DATASHEET CDN UNIT_Z1.pdf"]
last_updated: 2026-06-16
---

# Source: Process Data Sheet — CDN Pressure Relief Valves (2026-06-16)

## Purpose

18-page AS-BUILT (Rev Z1) Pressure Relief Valve / rupture disc process data sheet for the CDN unit, prepared by POSCO Engineering for Refinery Phenol Train II under UOP licence. Provides set pressure, sizing case, relief capacity, orifice designation, valve type, and discharge routing for all CDN relief devices.

> ✅ **This closes [[sources/Table-A6.2-3-PID-readiness-checklist]] Item 7 (PSV set pressures TBC)** — the single remaining blocker noted in the P&ID Readiness assessment for CDN. All CDN PSV set pressures are now AS-BUILT confirmed.

Full extraction with all 21 PSV tag groups + the X-2311 rupture disc is at [[instruments/pressure-relief-valves-cdn]] — this page summarizes findings and PSI/HAZOP significance only.

---

## Equipment Touched

| Tag | Page | Status |
|-----|------|--------|
| V-2301 | [[equipment/V-2301]] | Updated — **PSV TBC gap closed** (PSV-23-0401A/B/C/D, DIERS case) |
| V-2302 | [[equipment/V-2302]] | Updated — new Pressure Relief section added (PSV-23-0801A/B/C/D/E, DIERS case) |
| D-2304 | [[equipment/D-2304]] | Updated — **X-2311 rupture disc burst pressure conflict flagged** |
| D-2307 | [[equipment/D-2307]] | Updated — **PSV tag/set-pressure correction** (PSV-2001A/B replaces erroneous "PSV-2001N/B") |
| D-2308, D-2309 | [[equipment/D-2308]], [[equipment/D-2309]] | Confirmed — existing PSV-0501/0701 entries match exactly |
| D-2312 | [[equipment/D-2312]] | Updated — discharge destination corrected (HP Flare, not "vent to drain") |
| E-2301, E-2306, E-2310, E-2307 | various | Updated — new thermal-expansion/fire-case PSVs added (previously undocumented) |
| E-2308AB | [[equipment/E-2308AB]] | Updated — **shell PSV set pressure corrected 18.5→16.5 kg/cm²g**; new tube-side PSV-1401A/B added |
| E-2309 | [[equipment/E-2309]] | Updated — **combined PSV-1404/1405 entry split and corrected** (two different devices, two different set pressures); X-2312 PSVs added |
| X-2302AB | [[equipment/X-2302AB]] | Updated — discharge destination corrected (Decanter, not CHP sump) |
| X-2308 (X-2309 Calorimeters) | [[equipment/X-2308]] | Confirmed — existing entries match; design pressure and discharge destination added |

## Key Findings

1. **Two DIERS self-heating-reaction relief trains** (PSV-23-0401A/B/C/D on V-2301, PSV-23-0801A/B/C/D/E on V-2302) protect the columns against runaway CHP decomposition — the unit's core process hazard. Both are large, custom-orificed, pilot-operated, modulating valve trains with no standard API letter (orifice area exceeds the largest standard API 526 size).
2. **X-2311 rupture disc burst-pressure conflict**: existing wiki value (12.16 kg/cm²g @ 60°C) vs. this data sheet (9.5–11.0 kg/cm²g band @ 225–250°C). The new value is referenced at the vessel's actual design temperature and is adopted; flagged as the highest-priority open conflict in this batch given D-2304 is the highest-hazard vessel in CDN.
3. **D-2307 PSV correction**: the previously recorded "dual PSV arrangement" (PSV-2001N @ 0.84 / PSV-2001B @ 3.5 kg/cm²g) appears to have conflated the vent pressure control valve (PCV-2001, 0.84 kg/cm²g) with a relief valve. AS-BUILT data confirms a single PSV pair (PSV-2001A/B) both set at 3.5 kg/cm²g.
4. **E-2308AB / E-2309 set-pressure and entry-structure corrections** — two cases where the prior P&ID-era ingest either recorded the wrong set pressure (18.5 vs. 16.5 kg/cm²g for the Dehydrator shell PSVs) or merged two physically distinct devices into one entry (E-2309's PSV-1404 shell/CW vs. PSV-1405A/B tube/HC, which have different set pressures, sizing cases, and discharge routes).
5. **Discharge-destination corrections**: X-2302AB filter PSVs route to the Decanter (D-2205, OXI), not the CHP sump as previously recorded; D-2312 diamine tank PSVs route to HP Flare, not a generic drain.
6. **Documentation gap**: PSV-23-1408A/B is referenced in the revision log as "added" but no corresponding data sheet exists in this revision — open item for the process engineer.

## PSI / HAZOP Significance

This batch is the single most HAZOP-relevant data sheet ingested to date for CDN: PSV set pressures and discharge routing are direct inputs to deviation consequence severity and safeguard-adequacy assessment under [[hazop/risk-matrix]]. The rupture-disc burst-pressure conflict on D-2304 should be resolved before any HAZOP deviation analysis on that node is finalized, per the Standards Primacy Rule.

## References

- [[instruments/pressure-relief-valves-cdn]] — full PSV register (primary reference)
- [[sources/Table-A6.2-3-PID-readiness-checklist]] — PSV set pressure gap, now closed
- [[hazop/risk-matrix]] — risk ranking basis
- [[hazards/cumene-hydroperoxide]] — CHP runaway decomposition hazard basis for the DIERS relief trains
