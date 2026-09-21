---
name: Process Data Sheet — CDN Control Valves (2026-06-16)
description: Source summary for the 136-page CDN control valve process data sheet covering 43 control/on-off valve tags including the Decomposer Cooler split-range CW valves
metadata:
  type: source
tags: [source, instrument, data-sheet, control-valve, CDN]
sources: ["14780-8120-PS-0010_CONTROL VALVE PROCESS DATA SHEET CDN UNIT_Z1.pdf"]
last_updated: 2026-06-16
---

# Source: Process Data Sheet — CDN Control Valves (2026-06-16)

## Purpose

136-page AS-BUILT (Rev Z1) Control Valve process data sheet for the CDN unit, prepared by POSCO Engineering for Refinery Phenol Train II under UOP licence. Covers 43 distinct control/on-off valve tags (34 full process/actuator data sheets + 9 condensed pump-seal/N₂ purge valves in tabular format).

Full extraction is at [[instruments/control-valves-cdn]] — this page summarizes findings only.

## Equipment Touched

| Tag | Page | Status |
|-----|------|--------|
| E-2307 | [[equipment/E-2307]] | Updated — split-range CW valve tags/Cv added (TV-23-1302A/B), filling a gap where only the TY-1302A/B function blocks were previously documented |

No other equipment pages required changes — all other valve data confirms existing process descriptions without new equipment-level facts beyond Cv/material/fail-action detail now captured in the consolidated register.

## Key Findings

1. **TV-23-1302A** (Cv 13,139, 20" body) is the largest valve in the document — Reliable Cooling Water supply to the Decomposer Cooler E-2307, fail-open, paired in split range with **TV-23-1302B** (Cv 1,050, 12", fail-close, CW bypass around the cooler). This confirms and completes the split-range temperature control architecture already documented on [[equipment/E-2307]] (TIC-1302 → TY-1302A/B), which previously had no valve tags or sizing attached.
2. **Steam isolation pattern**: every steam supply header (S1.5, S3, S4) pairs a fail-close supply shutoff valve with a fail-open vent-to-atmosphere valve (e.g., UV-23-0502/UV-23-0501; UV-23-0703/UV-23-0702) — a consistent isolate-and-depressurize design across all three steam systems.
3. **Fail-action distribution**: 19 fail-open, 22 fail-close, 0 fail-last across 41 actuated valves; all 9 pump-seal N₂ valves are fail-open (maintains seal gas barrier on loss of air/power).
4. Manufacturer basis throughout: Masoneilan or Metso Automation (or equal). Body materials predominantly 316/316L SS for hydrocarbon/CHP service, carbon steel for steam/cooling-water service.

## References

- [[instruments/control-valves-cdn]] — full register (primary reference)
- [[equipment/E-2307]] — Decomposer Cooler split-range CW control
- [[instruments/sis-cdn]], [[instruments/cause-effect-cdn]] — SIS-actuated UXV/SOV cross-reference
