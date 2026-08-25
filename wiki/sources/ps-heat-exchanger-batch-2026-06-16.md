---
name: Process Data Sheets — CDN Heat Exchanger Batch (9 sheets, 2026-06-16)
description: Source summary for 9 shell-and-tube/plate heat exchanger process data sheets covering all CDN section heat exchangers (E-2301 through E-2310); AS-BUILT Rev Z1, May 2016, POSCO Engineering for PTT Phenol Train II
metadata:
  type: source
tags: [source, equipment, data-sheet, heat-exchanger, CDN]
sources: ["14780-8120-PS-E2301_E-2301 PROCESS DATA SHEET_Z1.pdf", "14780-8120-PS-E2302_E-2302 PROCESS DATA SHEET_Z1.pdf", "14780-8120-PS-E2303_E-2303 PROCESS DATA SHEET_Z1.pdf", "14780-8120-PS-E2304_E-2304 PROCESS DATA SHEET_Z1.pdf", "14780-8120-PS-E2306_E-2306 PROCESS DATA SHEET_Z1.pdf", "14780-8120-PS-E2307_E-2307 PROCESS DATA SHEET_Z1.pdf", "14780-8120-PS-E2308_E-2308 PROCESS DATA SHEET_Z1.pdf", "14780-8120-PS-E2309_E-2309 PROCESS DATA SHEET_Z1.pdf", "14780-8120-PS-E2310_E-2310 PROCESS DATA SHEET_Z1.pdf"]
last_updated: 2026-06-16
---

# Source: Process Data Sheets — CDN Heat Exchanger Batch (2026-06-16)

## Purpose

9 AS-BUILT (Rev Z1, May 2016) Process Data Sheets for all shell-and-tube and plate heat exchangers in the CDN section of PTT Phenol Train II. Prepared by POSCO Engineering & Construction (process sheets stamped Bechtel for thermal data) under UOP licence. These data sheets provide mechanical design basis (materials, MDMT, corrosion allowance, tube counts, codes) confirming and extending the existing CDN equipment pages built from P&ID and PFD drawings.

This batch substantially closes **PSI Readiness Category 6 — Equipment Data Sheets** for CDN heat exchangers.

---

## Equipment Inventory

| Tag | Name | Wiki Page | Page Status |
|-----|------|-----------|-------------|
| E-2301 | Preflash and Flash Columns Condenser | [[equipment/E-2301]] | Updated — mechanical data added |
| E-2302A/B | Feed-Oxidate Exchangers | [[equipment/E-2302AB]] | Updated — mechanical data added |
| E-2303 | Preflash Column Steam Heater | [[equipment/E-2303]] | Updated — mechanical data added |
| E-2304 | Flash Column Vaporizer | [[equipment/E-2304]] | Updated — mechanical data added |
| E-2306 | Flash Column Bottoms Cooler | [[equipment/E-2306]] | Updated — mechanical data added |
| E-2307A/B | Decomposer Cooler | [[equipment/E-2307]] | Updated — mechanical data added; **design pressure conflict resolved** |
| E-2308A/B | Dehydrators | [[equipment/E-2308AB]] | Updated — mechanical data added |
| E-2309 | Crude Product Cooler | [[equipment/E-2309]] | Updated — mechanical data added |
| E-2310 | Flash Column Overhead Vapor Chiller | [[equipment/E-2310]] | Updated — mechanical data added; **shell ID and subzero MDMT confirmed** |

All 9 items already had wiki pages from prior P&ID/PFD ingestion (2026-06-06/07). This batch adds confirmed mechanical/material-of-construction data rather than creating new process descriptions, except where conflicts are noted below.

---

## Key Engineering Findings

### Design Standards
- All exchangers: ASME Section VIII Division 1, TEMA Class R 9th edition, API 660 8th edition (2007)
- E-2301 is the exception: a welded plate exchanger (Ziepack, mandatory supplier) per API 662 Part 1 / ISO 15547-1 — not a shell-and-tube design
- All other 8 units: conventional shell-and-tube (TEMA types C_U, AEU, AES, BEM as applicable)

### Subzero / Cold Service Equipment
- **E-2310** (Flash Column Overhead Vapor Chiller): MDMT shell −9°C, tube −14°C — confirmed true cold service, consistent with existing C(50)/C(50) cold insulation note

### Materials of Construction (General Pattern)
- Tube-side / shell-side in contact with Cumene/CHP/Phenol process fluid: 304L Stainless Steel
- Steam or cooling-water-only sides: Killed Carbon Steel acceptable (UOP Std 3-11), 304L where UOP Std 3-15 specified
- All tubes strength-welded or expanded per TEMA Class R requirements; Helium leak testing required per ASME Code Section V Article 10

### Data Conflicts Identified and Resolved

| # | Equipment | Conflict | Resolution |
|---|-----------|----------|-----------|
| C-01 | E-2307A/B | Existing wiki (from Drawing 0017) recorded shell design pressure as 1.3 kg/cm²g; PS-E2307 data sheet shows **13.0 kg/cm²g** | Adopted DS value (13.0) — likely decimal transcription error in original P&ID reading. Updated in [[equipment/E-2307]] |
| C-02 | E-2310 | Existing wiki (from Drawing 0010) recorded shell ID as 1260 mm; PS-E2310 data sheet shows **1280 mm** | Adopted DS value (1280 mm). Updated in [[equipment/E-2310]] |

### Dual Stabbed-In Reboilers (V-2301 Preflash Column)
E-2302A/B and E-2303 are both stabbed directly into the Preflash Column V-2301 shell (1120 mm and 1160 mm ID nozzles respectively), confirming the reboiler arrangement referenced in [[equipment/V-2301]]. TEMA type C front heads specified for both; type A/B requires OWNER/CONSULTANT approval.

### Emergency Coolant Provisions
- **E-2304** (Flash Column Vaporizer): shell design pressure raised from 7.0 to 10.5 kg/cm²g specifically to accommodate Reliable Cooling Water / fire water as emergency coolant
- **E-2306** (Flash Column Bottoms Cooler): similar provision noted, design pressure 10.5 kg/cm²g
- **E-2309** (Crude Product Cooler): cooling water backflush connection provided for tube-side cleaning

### Severe / Special Service Notes
- **E-2304**: existing Train I exchanger design (PPCL DS 13850-8100-DS-0042, E-1304) found NOT thermally suitable for Train II's new duty (−30.7% undersurface) — confirms a new design was required, not a Train I copy
- **E-2307A/B**: two parallel shells (not a single unit) — already correctly noted in existing wiki page from Drawing 0017 correction (2026-06-07)
- **E-2308A/B**: 2 units, 1 operating + 1 standby (not parallel duty-sharing)

---

## PSI Significance

This batch substantially completes **Table A6.2-2 PSI Readiness Checklist, Item 4 — Equipment Data Sheets** for CDN heat exchangers. Combined with the [[sources/ps-static-equipment-batch-2026-06-14]] (ALKY/OXI vessels) ingested 2026-06-14, equipment data sheet coverage now spans:
- CDN: all heat exchangers (this batch) + V-2301 (static equipment batch)
- OXI: all major static equipment (static equipment batch)
- ALKY: 2 condensate pots (static equipment batch)

Remaining PSI data sheet gaps: CDN static vessels not yet covered by data sheet (D-2301 through D-2312 series — currently P&ID-sourced only), rotating equipment (pumps, compressors) across all sections, ALKY reactors/columns.

## References

- [[units/cdn]] — CDN unit overview
- [[sources/Table-A6.2-2-PSI-readiness-checklist]] — PSI readiness tracker (Category 6 substantially advanced)
- [[sources/ps-static-equipment-batch-2026-06-14]] — companion batch (ALKY/OXI static equipment + V-2301)
- [[hazards/cumene-hydroperoxide]] — CHP safety data
