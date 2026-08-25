---
name: GC HAZOP Procedure P-(Q-MP)-OEMS-005
type: standard
tags: [source, standard, hazop]
document_id: P-(Q-MP)-OEMS-005
revision: "4"
date: 2026-05-26
owner: PTT Global Chemical Public Company Limited — GC Management System and Process Safety (Q-MP)
custodian: Technical Safety Service (Q-MP-TS)
created_by: Mr. Pongpasin Tanaruangarmorn (Senior Safety Engineer)
approved_by: Mr. Warakorn Decha (Vice President)
file: raw/standards/P-(Q-MP)-OEMS-005_R4.pdf
last_updated: 2026-06-13
---

# Source: P-(Q-MP)-OEMS-005 — Hazard and Operability Study (HAZOP) Procedure

GC corporate HAZOP procedure. Governs all HAZOP studies performed within PTT Global Chemical (GC) under the Management of Change (MoC) framework. 24 pages, Rev 4.

---

## Document Structure

| Section | Title | Pages |
|---------|-------|-------|
| 1 | Purpose / Objective | 1 |
| 2 | Scope | 2 |
| 3 | Roles and Responsibility | 3–8 |
| 4 | Workflow (flowchart) | 9 |
| 5 | Detailed Narrative of Workflow | 10–14 |
| 6 | Appendix (Terms, KPIs, Implementation) | 15–24 |

---

## Scope (§2)

Applied to HAZOP studies triggered by the **Change Review Team (CRT)** as part of `P-(TP-PM)-OEMS-002 Management of Change Procedure`. HAZOP is initiated when CRT determines that a HAZOP study is required following Preliminary, SHE Assessment, and SHE Evaluation.

> **Note for this wiki:** This wiki's CDN HAZOP study is being initiated independently as a process safety review (not under MoC). The roles and methodology described here still apply; the MoC-specific e-PHA registration steps are not applicable to this standalone study.

---

## Roles and Responsibilities (§3)

| Role | Qualification | Qualified By |
|------|--------------|--------------|
| HAZOP Coordinator | Qualified MoC Champion per P-(TP-PM)-OEMS-002 | TP-PM |
| HAZOP Leader (Internal) | Min 8 years' experience; HAZOP Leadership course trained; Awareness of Process Safety in Design trained; **must be independent** (independent from project org, EPC contractor/subsidiary, and VP Operation line of management) | HAZOP Procedure Custodian |
| HAZOP Leader (External) | Qualified and registered by Procedure Custodian | HAZOP Procedure Custodian |
| HAZOP Scribe | Min 2 years' experience; familiar with HAZOP methodology; trained in e-PHA system | HAZOP Procedure Custodian |
| HAZOP Team (Core) | MoC Champion + Operation rep (3+ yrs) + Process Engineer (3+ yrs) + Site Maintenance Engineer + Plant SHE representative | HAZOP Procedure Custodian |
| Responsible Person | Discipline Engineer or person with knowledge of action content | — |
| Action Approver | HAZOP team consensus; default = MoC Champion | HAZOP Procedure Custodian |
| PHA Element Leader | Division Manager of Plant Technic | — |

---

## HAZOP Methodology (§5.4) — **Key procedural rules**

The following steps govern the study execution:

1. **HAZOP Leader introduces** team, signs attendance sheet, briefs on Risk Assessment Matrix, presents ground rules.
2. **Node selection** — Leader selects node and explains boundaries.
3. **Design intent** — Process engineers present design intent and operating conditions.
4. **Deviation brainstorming** — Leader chooses deviation; team identifies all credible causes.
5. **Initial risk** — Team develops consequences and ranks Severity × Likelihood **without any safeguards**. Severity is set at this stage and **does not change**.
6. **Existing safeguards** — Team identifies safeguards and re-evaluates **Likelihood only** (Severity unchanged) → Mitigated risk.
7. **Recommendations** — If mitigated risk is unacceptable, recommend actions. Recommendations may also be raised for acceptable-risk items to improve operability.
8. Repeat steps 4–7 for all deviations; repeat 2–8 for all nodes.

> **Risk ranking rule:** Severity is fixed at initial risk evaluation. Only likelihood is re-evaluated when accounting for safeguards. This governs all HAZOP worksheets in this wiki.

---

## Required PSI for HAZOP Study (§5.2)

Per the procedure, the following documents must be available before HAZOP commences:

| # | Document | Status in wiki |
|---|----------|---------------|
| a | Design requirement and description | ✅ PFD, P&ID CDN complete |
| b | SDS (Safety Datasheet) | ⚠️ General SDS in [[wiki/hazards/]] — plant-specific SDS not ingested |
| c | Plot Plan & Layout | ❌ Not yet ingested |
| d | PFD (Process Flow Diagram) | ✅ CDN PFDs complete |
| e | P&ID | ✅ CDN P&IDs complete (Dwg 0002–0023) |
| f | Control & Safeguarding Diagram | ✅ Cause & Effect Table (Dwg 0002) ingested |
| g | Alarm and Trip Settings | ⚠️ Partially captured; setpoints TBC per wiki gaps |
| h | Piping class specification | ❌ Not yet ingested |
| i | Equipment datasheets | ❌ Not yet ingested |
| j | Relief and blowdown summary table | ⚠️ Relief header (Dwg 0022) ingested; summary table TBC |
| k | Operating / maintenance procedures | ✅ UOP GOM (CDN sections) ingested |

---

## HAZOP Workflow Summary (§5.1–5.8)

```
1. Initiation → 2. Preparation → 3. Arrangement → 4. Study Execution
→ 5. Documentation → 6. Action Close-out → 7. Action Change (if needed)
```

Monitoring program: Monthly (overdue recs), Continuous (PSE Tier 1/2 against HAZOP KPIs), Planned (corporate audit every ~2 years).

---

## HAZOP KPIs (§6.4)

| KPI | Description | Target |
|-----|-------------|--------|
| HAZOP-1 | PSE Tier 1/2 events where ineffective HAZOP study is a root cause | 0 cases |
| HAZOP-2/1 | % HAZOP (MoC) led by qualified and independent HAZOP Leader | 100% |
| HAZOP-2/2 | % HAZOP (MoC) performed with correct team disciplines and experience | 100% |
| HAZOP-3/1 | HAZOP reports where recommendations not registered in e-PHA | 0 items |
| HAZOP-3/2 | Active HAZOP recommendations overdue (not Closed/Approved by due date) | 0 items |
| HAZOP-3/3 | Recommendations closed out deviating from original intent without re-evaluation | 0 items |
| HAZOP-3/4 | Recommendations cancelled without re-evaluation by HAZOP team | 0 items |

---

## Key Terms (§6.1)

| Term | Definition |
|------|-----------|
| Initial risk | Risk ranking **without** consideration of existing safeguards |
| Mitigated risk | Risk ranking **with** consideration of existing safeguards |
| Existing Safeguard | Facility, process, or procedure that reduces likelihood or mitigates consequences |
| Deviation | Combination of parameter + guideword — how plant deviates from design intent |
| Node | Specific process location where deviations of design intent are evaluated |
| HAZOP Action Change | Changing the detail or cancelling an action that deviates from approved report |

---

## Related Documents Referenced (but NOT in raw/)

| Document ID | Title | Status |
|------------|-------|--------|
| **W-(Q-MP)-002** | **Operational Risk Assessment Matrix and Its Applications** | ❌ **MISSING — required for HAZOP-SETUP** |
| P-(TP-PM)-OEMS-002 | Management of Change (MoC) Procedure | Not needed (standalone study) |
| SG-(Q-MP)-004 | Guideline for Plant PSM Governance | Not needed |
| SG-(Q-MP-PS)-001 | Process Safety Management Leading Indicators | Not needed |
| **SG-(Q-MP)-014** | **Guidance for Hazard and Operability Studies (HAZOP)** — contains guideword set, deviation list, PSI readiness checklist | ❌ **MISSING — contains standard guidewords** |

---

## Critical Gaps for HAZOP-SETUP

> ⛔ **HAZOP-SETUP CANNOT PROCEED** until the following are provided:
>
> 1. **`W-(Q-MP)-002` — Operational Risk Assessment Matrix** — This is the severity × likelihood matrix required by this procedure (§5.2, §5.4e). Without it, no risk rankings can be assigned per the Standards Primacy Rule.
> 2. **`SG-(Q-MP)-014` — HAZOP Guidance** — Contains the guideword set and deviation list. While standard guidewords (No/More/Less/Reverse/As Well As/Other Than) are known, this document may specify additional GC-specific deviations.

## References
- [[wiki/hazop/study-info]] — HAZOP study initialization page
- [[wiki/hazop/risk-matrix]] — to be created from W-(Q-MP)-002
