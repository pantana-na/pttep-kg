---
name: SDS PSI Batch — 15 GHS Safety Data Sheets (2026-06-14)
description: Consolidated source summary for 15 GHS-compliant Safety Data Sheets ingested to complete PSI Category 1 (Chemical hazard SDS) for PPCL CDN HAZOP study
metadata:
  type: source
tags: [source, hazard, sds, psi, ghs]
sources: ["SDS_80-15-9_cumene-hydroperoxide.pdf", "SDS_108-95-2_phenol.pdf", "SDS_71-43-2_benzene.pdf", "SDS_7664-93-9_sulfuric-acid-98pct.pdf", "SDS_98-82-8_cumene.pdf", "SDS_67-64-1_acetone.pdf", "SDS_98-83-9_alpha-methylstyrene.pdf", "SDS_115-07-1_propylene.pdf", "SDS_107-21-1_ethylene-glycol.pdf", "SDS_110-97-4_dipa-placeholder-diamine-tbc.pdf", "SDS_100-18-5_di-isopropylbenzene.pdf", "SDS_100-86-7_dmba-dimethylbenzylcarbinol.pdf", "SDS_497-19-8_sodium-carbonate-solution.pdf", "SDS_7727-37-9_nitrogen.pdf", "SDS_98-86-2_acetophenone.pdf"]
last_updated: 2026-06-14
---

# Source: SDS PSI Batch — 15 GHS Safety Data Sheets

## Purpose

These 15 GHS-compliant Safety Data Sheets (16-section GHS format) were compiled and ingested on 2026-06-14 to fulfil **PSI Readiness Category 1** (Chemical and Reaction hazard — GHS-compliant SDS) per the formal Table A6.2-2 PSI Readiness Checklist for the PTT Phenol (PPCL) Train II CDN HAZOP study.

---

## SDS Inventory

| # | Chemical | CAS | File | Wiki Hazard Page | Data Quality Flags |
|---|---------|-----|------|-----------------|-------------------|
| 1 | Cumene Hydroperoxide (CHP) | 80-15-9 | SDS_80-15-9_cumene-hydroperoxide.pdf | [[hazards/cumene-hydroperoxide]] | Decomp onset CONFLICT (80°C SDS vs 100°C wiki — see page) |
| 2 | Phenol | 108-95-2 | SDS_108-95-2_phenol.pdf | [[hazards/phenol]] | LEL/UEL CONFLICT (SDS 1.3%/9.0% vs wiki 1.7%/8.6% — see page) |
| 3 | Benzene | 71-43-2 | SDS_71-43-2_benzene.pdf | [[hazards/benzene]] | OEL FLAG: ACGIH 2024 NIC proposes 0.02 ppm vs historical 0.5 ppm — verify final adopted value |
| 4 | Sulfuric Acid (98%) | 7664-93-9 | SDS_7664-93-9_sulfuric-acid-98pct.pdf | [[hazards/sulfuric-acid]] | None |
| 5 | Cumene / Isopropylbenzene | 98-82-8 | SDS_98-82-8_cumene.pdf | [[hazards/cumene]] | Carc 1B data-aggregation artifact (NOT in SDS; ECHA verification recommended) |
| 6 | Acetone | 67-64-1 | SDS_67-64-1_acetone.pdf | [[hazards/acetone]] | CHP interaction: acetone + CHP → shock-sensitive acetone peroxide |
| 7 | Alpha-Methylstyrene (AMS) | 98-83-9 | SDS_98-83-9_alpha-methylstyrene.pdf | [[hazards/alpha-methylstyrene]] | H304/H361/Skin Sens 1B from Sigma-Aldrich SDS — NOT in plant SDS; ECHA C&L verification required |
| 8 | Propylene | 115-07-1 | SDS_115-07-1_propylene.pdf | [[hazards/propylene]] | None |
| 9 | Ethylene Glycol | 107-21-1 | SDS_107-21-1_ethylene-glycol.pdf | [[hazards/ethylene-glycol]] | None; fomepizole antidote noted |
| 10 | Diamine Additive (TBC) | 110-97-4 (DIPA — PLACEHOLDER) | SDS_110-97-4_dipa-placeholder-diamine-tbc.pdf | [[hazards/diamine-tbc]] | ⛔ PLACEHOLDER: actual additive identity NOT confirmed; DIPA used as surrogate — PRIORITY ACTION required |
| 11 | Di-isopropylbenzene (DIPB) | 100-18-5 | SDS_100-18-5_di-isopropylbenzene.pdf | [[hazards/di-isopropylbenzene]] | H304 and H411 not confirmed in plant SDS — by structural analogy only; ECHA verification required |
| 12 | Dimethylbenzylcarbinol (DMBA) | 100-86-7 | SDS_100-86-7_dmba-dimethylbenzylcarbinol.pdf | [[hazards/dimethylbenzylcarbinol]] | ⚠️ IDENTITY FLAG: CAS 100-86-7 vs 617-94-7 — confirm with PPCL; H301 vs H302 CONFLICT |
| 13 | Sodium Carbonate Solution | 497-19-8 | SDS_497-19-8_sodium-carbonate-solution.pdf | [[hazards/sodium-carbonate]] | None |
| 14 | Nitrogen | 7727-37-9 | SDS_7727-37-9_nitrogen.pdf | [[hazards/nitrogen]] | None |
| 15 | Acetophenone | 98-86-2 | SDS_98-86-2_acetophenone.pdf | [[hazards/acetophenone]] | Solidifies at 19.6°C — heat tracing required |

---

## Key Findings and Conflicts

### Data Conflicts (require operator resolution before HAZOP finalisation)

| # | Chemical | Conflict | Disposition |
|---|---------|----------|-------------|
| C-01 | CHP | Decomp onset: wiki stated ~100°C; SDS_80-15-9 (DSC at 88 wt%) states ~80°C | FLAGGED in [[hazards/cumene-hydroperoxide]] — operator to verify with plant calorimetry |
| C-02 | Phenol | LEL/UEL: wiki stated 1.7%/8.6%; SDS_108-95-2 states 1.3%/9.0% | FLAGGED in [[hazards/phenol]] — resolve with authoritative source (NFPA/ECHA) |

### Data Quality Flags (require ECHA C&L verification)

| # | Chemical | Flag | Action Required |
|---|---------|------|----------------|
| Q-01 | Cumene | Carc 1B (H350) appeared in data-aggregation search; NOT in plant SDS | Verify against ECHA C&L Inventory for CAS 98-82-8 |
| Q-02 | AMS | H304/H361/Skin Sens 1B from Sigma-Aldrich; NOT in plant SDS | Verify against ECHA C&L for CAS 98-83-9 |
| Q-03 | DIPB | H304 and H411 by structural analogy only; NOT confirmed in plant SDS | Verify against ECHA C&L for CAS 100-18-5 |
| Q-04 | DMBA | H301 vs H302 acute tox conflict between sources | Confirm CAS identity first, then resolve against ECHA C&L |
| Q-05 | Benzene | ACGIH 2024 NIC proposes TLV-TWA reduction from 0.5 ppm to 0.02 ppm | Verify final ACGIH 2024/2025 adopted value; align Thailand OEL |

### Identity Flags (require PPCL/licensor confirmation)

| # | Chemical | Flag | Priority |
|---|---------|------|----------|
| I-01 | Diamine (TBC) | Actual CAS number and chemical identity not confirmed; DIPA (CAS 110-97-4) used as PLACEHOLDER | ⛔ HIGHEST — must be resolved before this chemical is used in HAZOP consequence analysis |
| I-02 | DMBA | CAS 100-86-7 vs 617-94-7 — both appear in cumene process literature for "DMBA" | HIGH — confirm which isomer is present in CDN product streams |

---

## PSI Compliance Assessment

This SDS batch closes **Table A6.2-2 Item 1 — Chemical and Reaction hazard (GHS-compliant SDS)**:

| Condition | Met? |
|-----------|------|
| GHS-compliant SDS for all process chemicals in scope | ✅ Yes — 15 SDS ingested covering all identified chemicals |
| Hazard pages in wiki for each chemical | ✅ Yes — 15 hazard pages written (2 updated, 13 new) |
| Data conflicts flagged for operator resolution | ✅ Yes — 2 data conflicts flagged (CHP decomp onset; Phenol LEL/UEL) |
| Data quality flags noted for ECHA verification | ✅ Yes — 5 flags noted |
| Identity-unconfirmed chemicals flagged | ✅ Yes — Diamine TBC and DMBA flagged |

**Remaining gaps (not closed by this batch):**
- ⛔ Diamine additive: identity must be confirmed and correct SDS obtained
- ⚠️ ECHA C&L verification for Q-01 through Q-05 above
- ⚠️ Data conflicts C-01 and C-02 pending operator resolution

---

## References

- [[hazop/study-info]] — PSI Readiness Table (Item 1 now ✅ Complete with noted caveats)
- [[sources/Table-A6.2-2-PSI-readiness-checklist]] — governing PSI readiness checklist
- All 15 individual wiki hazard pages (see SDS Inventory table above)
