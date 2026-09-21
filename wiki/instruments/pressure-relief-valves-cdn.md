---
name: CDN Pressure Relief Valves (PSV) Register
unit: CDN
tags: [instruments, PSV, relief, safety, CDN, PSI]
sources: [14780-8120-PS-0018_PRESSURE RELIEF VALVE PROCESS DATASHEET CDN UNIT_Z1.pdf]
last_updated: 2026-06-16
---

# CDN Pressure Relief Valve (PSV) Register

**Source:** 14780-8120-PS-0018, Rev Z1 (AS-BUILT), Refinery Phenol Train II, POSCO Engineering / UOP licensor basis.

> ✅ **This document closes the long-standing "PSV set pressures TBC" gap** flagged in [[sources/Table-A6.2-3-PID-readiness-checklist]] (P&ID Readiness Item 7) and the HAZOP Gaps list. All CDN PSV set pressures are now confirmed AS-BUILT. Risk ranking and IPL credit for these devices in HAZOP node analysis should cite this page per the Standards Primacy Rule.

This is the authoritative register for relief device protection in the CDN unit. Equipment pages link here; this page is the single source of truth for set pressures, sizing basis, and discharge routing.

---

## Column Overpressure Protection — DIERS Runaway Reaction Case

These two groups protect the two CDN vacuum columns against the worst-case CHP self-heating/runaway decomposition scenario (DIERS methodology) — the highest-consequence relief case in the unit.

| Tag | Protected Equipment | Sizing Case | Set Pressure | Design Pressure | Relief Vapor Rate | Orifice | Type | Valves (Online/Spare) | Discharge |
|-----|---------------------|-------------|--------------|------------------|--------------------|---------|------|------------------------|-----------|
| PSV-23-0401A/B/C/D | [[equipment/V-2301]] Preflash Column | Self-Heating Reaction (DIERS, ω=2.222) | 2.100 (lead+spare) / 2.205 (others) kg/cm²g | 3.5 kg/cm²g | 308,264 kg/h; effective orifice area 754.06 cm² (no standard API letter — custom oversized) | — | Pilot Operated, Modulating | 3 / 1 | Atmosphere, safe location; backflow preventer required (vacuum service) |
| PSV-23-0801A/B/C/D/E | [[equipment/V-2302]] Flash Column | Self-Heating Reaction (DIERS, ω=1.436) | 2.100 (lead+spare) / 2.205 (others) kg/cm²g | 3.5 kg/cm²g | 327,745 kg/h; effective orifice area 1005.42 cm² (no standard API letter) | — | Pilot Operated, Modulating | 4 / 1 | Atmosphere, safe location; backflow preventer required (vacuum service) |

> These are unusually large multi-valve pilot-operated relief trains sized for the unit's core hazard scenario: an uncontrolled exothermic decomposition reaction inside the vacuum columns. The custom (non-API-letter) orifice area reflects sizing beyond the largest standard API 526 letter (T = 729 cm²).

## Decomposer Drum Overpressure Protection — Rupture Disc

| Tag | Protected Equipment | Type | Burst Pressure | Basis | Discharge |
|-----|---------------------|------|-----------------|-------|-----------|
| X-2311 | [[equipment/D-2304]] Decomposer Drum | Rupture Disc (BS&B Type B, 24") + Safety Head Type FA-7R | **Not to exceed 11.0 kg/cm²(g) @ 250°C; not less than 9.5 kg/cm²(g) @ 225°C** | MAWP of D-2304 | Atmosphere, safe location via 24" vent pipe, angle-cut cap; 1 operating + 2 spares |

> ⛔ **CONFLICT WITH EXISTING WIKI VALUE.** [[equipment/D-2304]] previously recorded the X-2311 burst pressure as a single value: **12.16 kg/cm²g @ 60°C**. The AS-BUILT PSV/rupture-disc data sheet (this document) instead specifies a burst-pressure **band** referenced to the vessel's actual design temperature (225–250°C, matching D-2304's 250°C design temperature) rather than 60°C (D-2304's *operating* temperature). The new data sheet value is both more recent (formal relief-device AS-BUILT data sheet vs. an earlier P&ID-derived figure) and more physically consistent (burst pressure quoted at a temperature matching the vessel's design basis, not its normal operating temperature). **DS value adopted: 9.5–11.0 kg/cm²(g) band, referenced at 225–250°C.** Verify against the physical disc nameplate during the next turnaround — this is the single highest-consequence relief device in the CDN unit and the conflict should be closed before HAZOP touches the D-2304 node.

## Acid Aromatics / Neutralization Area

| Tag | Protected Equipment | Service | Sizing Case | Set Pressure | Design Pressure | Capacity | Orifice | Type | Valves | Discharge |
|-----|---------------------|---------|-------------|--------------|------------------|----------|---------|------|--------|-----------|
| PSV-23-2001A/B | [[equipment/D-2307]] Acid Aromatics Sump | HC vapor, MW 62.5 | External Fire | 3.500 kg/cm²g | 3.500 kg/cm²g | 6,687 kg/h; orifice 14.33 cm² | L | Spring Loaded, Balanced Bellows | 1/1 | Relief Header |
| PSV-23-0301A/B | [[equipment/X-2302AB]] Preflash Column Feed Filters | HC vapor | External Fire | 11.0 kg/cm²g (adj. for liquid static head) | — | 2,945 kg/h/valve | 1-1/2G3 | Conventional | 1/1 | **Decanter** |
| PSV-23-1903A/B | [[equipment/D-2312]] Diamine Injection Tank | Diamine, vapor | External Fire | 3.5 kg/cm²g | — | 1,012 kg/h | 1-1/2H3 | Bellows | 1/1 | **HP Flare**; interlock required |

> ⛔ **D-2307 CONFLICT/CORRECTION.** [[equipment/D-2307]] currently lists a "dual PSV arrangement": **PSV-2001N at 0.84 kg/cm²g** and **PSV-2001B at 3.5 kg/cm²g**. This AS-BUILT data sheet shows only **one PSV pair, PSV-23-2001A/B, both rated at the same 3.5 kg/cm²g set/design pressure** (fire case) — there is no second, low-set relief valve in the formal PSV register. The 0.84 kg/cm²g figure matches **PCV-2001** (the vent *pressure control valve* already separately documented on the D-2307 page, which maintains N₂ blanket pressure) — not a PSV. The "N" suffix and the implied low-set relief valve both appear to be a data-entry error from the earlier P&ID-based ingest, most likely conflating PCV-2001 with a PSV and misreading "A" as "N". **Correct AS-BUILT designation: PSV-2001A (operating) / PSV-2001B (spare), both set at 3.5 kg/cm²g, discharging to the Relief Header** — see [[equipment/D-2307]] for the corrected entry.
>
> **X-2302 discharge correction:** wiki previously stated PSV-0301A/B discharge to "CHP sump." This data sheet specifies discharge to the **Decanter** (D-2205, OXI section) instead. DS value adopted.
>
> **D-2312 discharge correction:** wiki previously stated "vent to drain." This data sheet specifies discharge to **HP Flare**, with an interlock requirement. DS value adopted.

## Calorimeter Loop

| Tag | Protected Equipment | Sizing Case | Set Pressure | Design Pressure | Capacity | Orifice | Type | Valves | Discharge |
|-----|---------------------|-------------|--------------|------------------|----------|---------|------|--------|-----------|
| PSV-23-1801A/B | [[equipment/X-2308]] Calorimeter No. 1 (X-2309A) | Blocked Inlet/Outlet + Thermal Expansion | 9.50 kg/cm²g | 10.50 kg/cm²g | 0.000253–0.152 m³/h (negligible) | D | Spring Loaded, Balanced Bellows | 2/2 (combined with 1802 group) | Acid Aromatics KO Drum (D-2306) |
| PSV-23-1802A/B | [[equipment/X-2308]] Calorimeter No. 2 (X-2309B) | Blocked Inlet/Outlet + Thermal Expansion | 9.50 kg/cm²g | 10.50 kg/cm²g | 0.000253–0.152 m³/h (negligible) | D | Spring Loaded, Balanced Bellows | 2/2 (combined with 1801 group) | Acid Aromatics KO Drum (D-2306) |

> Confirms existing wiki entries on [[equipment/X-2308]] (set 9.5 kg/cm²g) — this data sheet adds design pressure (10.5 kg/cm²g) and discharge destination (D-2306).

## Dehydrator / Crude Product Cooler Area

| Tag | Protected Equipment | Service Side | Sizing Case | Set Pressure | Capacity | Orifice | Type | Valves | Discharge |
|-----|---------------------|--------------|-------------|--------------|----------|---------|------|--------|-----------|
| PSV-23-1403A/B/C | [[equipment/E-2309]] X-2312 Dehydrator Reactor Loop | Process liquid, SG 0.832 | Blocked-in / Thermal Expansion | 20.50 kg/cm²g | negligible (0.00273 m³/h) | D | Spring Loaded, Balanced Bellows | 3/0 (each sized 100%) | Acid Aromatics KO Drum |
| PSV-23-1406 | [[equipment/E-2308AB]] Dehydrator A, shell (steam) | External Fire | **16.5 kg/cm²g** | 761 kg/h | 1D2 | Conventional | 1/0 | Atmosphere |
| PSV-23-1407 | [[equipment/E-2308AB]] Dehydrator B, shell (steam) | External Fire | **16.5 kg/cm²g** | 761 kg/h | 1D2 | Conventional | 1/0 | Atmosphere |
| PSV-23-1401A/B | [[equipment/E-2308AB]] Dehydrators, tube (HC liquid) | Thermal Expansion | 19.8 kg/cm²g (adj. static head) | 4,012 kg/h | 3/4"x1" | Conventional | 1/1 | HP Flare |
| PSV-23-1404 | [[equipment/E-2309]] Crude Product Cooler, shell (CW) | External Fire | **16.5 kg/cm²g** | 862 kg/h | 1E2 | Conventional | 1/0 | Atmosphere |
| PSV-23-1405A/B | [[equipment/E-2309]] Crude Product Cooler, tube (HC) | External Fire | **20.5 kg/cm²g** (adj. static head) | 835 kg/h | 1D2 | Conventional | 1/1 | HP Flare; **interlock required** |

> ⛔ **E-2308AB CONFLICT.** Wiki previously recorded both shell-side fire-case PSVs (PSV-1406, PSV-1407) at **18.5 kg/cm²g**. This data sheet confirms both at **16.5 kg/cm²g**. DS value adopted — see [[equipment/E-2308AB]]. This data sheet also identifies a **second, previously undocumented PSV pair** on the tube side (PSV-1401A/B, 19.8 kg/cm²g, thermal expansion, discharge to HP Flare) — added to the equipment page.
>
> ⛔ **E-2309 CONFLICT.** Wiki previously combined "PSV-1404, PSV-1405" into a single entry at **20.5 kg/cm²g**. This data sheet shows these are **two separate, differently-rated devices**: PSV-1404 (shell/CW, external fire, **16.5 kg/cm²g**, discharge atmosphere) and PSV-1405A/B (tube/HC, external fire, **20.5 kg/cm²g**, discharge HP Flare, interlock required). The combined entry has been split and corrected on [[equipment/E-2309]].

## Cooling/Chilled Water Thermal-Expansion Relief (Utility Side)

These protect the cold/CW-side of heat exchangers against thermal expansion when isolated full of liquid — low consequence, high frequency credit devices.

| Tag | Protected Equipment | Service | Set Pressure | Capacity | Orifice | Type | Discharge |
|-----|---------------------|---------|--------------|----------|---------|------|-----------|
| PSV-23-0802 | [[equipment/E-2306]] Flash Column Bottoms Cooler, tube (Reliable CW) | Thermal Expansion | 10.5 kg/cm²g | 136 kg/h | 3/4"x1" | Conventional | Atmosphere |
| PSV-23-0803 | [[equipment/E-2301]] Preflash/Flash Columns Condenser, plate (Reliable CW) | Thermal Expansion | 10.5 kg/cm²g | 2,981 kg/h | 3/4"x1" | Conventional | Atmosphere |
| PSV-23-1001 | [[equipment/E-2310]] Flash Column Overhead Vapor Chiller, tube (Chilled Water) | Thermal Expansion | 11.5 kg/cm²g | 58 kg/h | 3/4"x1" | Conventional | Atmosphere |
| PSV-23-1701 | [[equipment/E-2307]] Decomposer Cooler, shell (Reliable CW) | External Fire | 13.0 kg/cm²g | 2,479 kg/h | 1-1/2G3 | Conventional | Atmosphere |

> All four were previously undocumented on their respective equipment pages — added.

## Steam Condensate Drums (existing wiki entries — confirmed)

| Tag | Protected Equipment | Sizing Case | Set Pressure | Design Pressure | Capacity | Orifice | Type | Discharge |
|-----|---------------------|-------------|--------------|------------------|----------|---------|------|-----------|
| PSV-23-0501 | [[equipment/D-2308]] Steam Heater Condensate Drum | External Fire | 7.0 kg/cm²g | 7.0 kg/cm²g | 157 kg/h | D | Conventional | Atmosphere |
| PSV-23-0701 | [[equipment/D-2309]] Vaporizer Condensate Drum | External Fire | 7.0 kg/cm²g | 7.0 kg/cm²g | 157 kg/h | D | Conventional | Atmosphere |

> Both confirm pre-existing wiki entries exactly — no change needed beyond adding sizing basis (external fire) and orifice designation.

## Documentation Gaps

| Item | Issue |
|------|-------|
| PSV-23-1002 | Listed in revision log as **DELETED** — vendor-supplied, not part of this data sheet. No equipment page action needed. |
| PSV-23-1408A/B | Revision log (Rev F1) states this PSV was **"ADDED"** per UOP-Refinery Operations Ltd.-SPOTS RELEASE-T178, referencing page 18 — but page 18 in this Rev Z1 copy contains PSV-23-1701/1405A/B/1903A/B, not 1408A/B. **No data sheet for PSV-1408A/B exists in this revision.** Either superseded/renumbered in a later revision without updating the log, or a stale log entry. **Open documentation gap — flag for the process engineer; do not assume this device's protection scope until resolved.** |

## References

- [[sources/ps-prv-cdn-batch-2026-06-16]] — source summary
- [[equipment/V-2301]], [[equipment/V-2302]] — DIERS runaway relief (primary CHP hazard protection)
- [[equipment/D-2304]] — X-2311 rupture disc (burst pressure conflict)
- [[equipment/D-2307]] — PSV-2001A/B correction
- [[equipment/X-2302AB]] — PSV-0301A/B discharge correction
- [[equipment/D-2312]] — PSV-1903A/B discharge correction
- [[equipment/E-2308AB]], [[equipment/E-2309]] — set-pressure corrections and new tube-side PSVs
- [[hazop/risk-matrix]] — risk ranking basis for any HAZOP deviation citing these devices
- [[sources/Table-A6.2-3-PID-readiness-checklist]] — PSV set pressure TBC item, now closed
