# Activity Log

Append-only. Each entry starts with `## [YYYY-MM-DD] <type> | <title>` for grep-parseable history.

To see last 5 entries: `grep "^## \[" wiki/log.md | tail -5`

## [2026-06-26] output | replication kit — generic LLM Process Expert Wiki prompts
Type: working documents (3 files)
Destination: output/working/
Files:
- `2026-06-26_generic_system-prompt_process-expert-wiki.md` — plant-agnostic CLAUDE.md / system prompt with placeholders; covers directory structure, all page schemas, SORT/INGEST/QUERY/OUTPUT/LINT workflows, conventions, HAZOP anti-bias and standards-primacy rules
- `2026-06-26_generic_hazop-extension-prompt.md` — HAZOP skill prompt; covers SETUP/NODE/ACTION-CLOSE sub-workflows, full guideword matrix (Table 6.1), likelihood guidance (Table 6.3), IPL credit tables (6.4/6.5/6.6), three-risk-block worksheet schema, action register schema, interlock/ESD summary schema, GC workflow phases
- `2026-06-26_replication-guide.md` — bootstrap guide; LLM platform requirements, source document checklist, directory setup, placeholder customization, ingest order, HAZOP startup sequence, common mistakes, adaptation guide for non-GC standards
Purpose: enable any team to replicate this system for a different plant or unit by following the guide and customizing the two prompt files

## [2026-06-18] output | 2026-06-18_overview_presentation_llm-wiki-hazop.pdf / .pptx

Type: presentation (slide deck — final deliverable, NotebookLM-generated)
Destination: output/presentations/ (both PDF and editable PPTX)
Generated via: NotebookLM (notebooklm-py CLI). Notebook "From Documents to Decisions — LLM Wiki + Claude Code for HAZOP" (id 31cf6e72); source = the narrative script below; format = detailed slide-deck. NotebookLM titled the artifact "Compounding Process Intelligence".
Scope: 20-min sharing for process/safety engineers; 5-act structure (Problem → Foundation → Why HAZOP first → HAZOP agent + guardrails + live demo → Vision/invitation).
Note: NotebookLM summarizes on-slide text and does NOT carry speaker notes — present from the script (speaker notes, timings, demo safety-net live in the working .md). Individual slides can be refined via `notebooklm generate revise-slide`.
Source wiki pages: presentation script (output/working/2026-06-18_overview_presentation-script_llm-wiki-hazop.md) → derived from [[hazop/study-info]], [[hazop/nodes/cdn-N02]], [[hazop/nodes/cdn-N03]], [[hazop/methodology]], [[hazop/risk-matrix]], [[index]], CLAUDE.md, hazop SKILL.md

## [2026-06-18] output | 2026-06-18_overview_presentation-script_llm-wiki-hazop.md

Type: working draft (presentation narrative script — source for NotebookLM slide generation)
Destination: output/working/
Scope: 20-min sharing — "LLM Wiki + Claude Code for HAZOP" — audience: process/safety engineers; goal: educate/inspire; includes a live demo.
Structure: 18 slides across 5 acts — (1) Problem: knowledge doesn't compound; (2) Foundation: LLM wiki + Claude Code architecture/INGEST/why-it-beats-PDFs; (3) From foundation to agents — why HAZOP first; (4) HAZOP agent: collect standards → encode skill → guardrails (Anti-Bias / Standards Primacy / Node Boundary) → LIVE DEMO → outputs; (5) Idea menu + invitation close. Per-slide on-slide content + speaker notes + cumulative timings; live-demo safety-net checklist; Q&A appendix.
Grounding: real wiki state — 97 sources / 151+ pages; GC HAZOP standards set; CDN-N02 & CDN-N03 worked (R-001..R-009, Excel+Word deliverables); Node 23-05/23-06 markups received = live-demo candidates; flagged conflicts (D-2312 identity, D-2304 rupture disc, Economic severity=BU).
Source wiki pages: [[hazop/study-info]], [[hazop/nodes/cdn-N02]], [[hazop/nodes/cdn-N03]], [[hazop/methodology]], [[hazop/risk-matrix]], [[index]], CLAUDE.md, .claude/skills/hazop/SKILL.md
Next step: user review → feed approved script to NotebookLM for slide deck (save final .pptx/.pdf to output/presentations/).

## [2026-06-18] hazop-node | CDN-N03 (markup "Node 23-03") — preliminary desktop first-pass

Node: CDN-N03 — Flash Column Vaporizer & Concentrated-CHP Bottoms Pump-Out
Trigger: user request — "create draft HAZOP report for Node 23-03 per green-highlight markup, in Excel template, on the standard template + risk assessment already set up." Invoked via `/hazop node 23-03`.
Markup: "Node 23-03.pdf" (user-supplied, green highlight) spanning Dwg 0007/0007A/0008/0009/0012/0012A. Recommend filing in raw/pid/.
Equipment in node: E-2304 (Flash Column Vaporizer), D-2309 + P-2309A/B (SC3 condensate), V-2302 bottoms draw, P-2301A/B (Flash Column Bottoms Pumps). Concentrated CHP ~80-85 wt% — highest in the section.
Non-negotiable checks: Anti-Bias PASSED (only the O-P3 example in raw/hazop/example/; no Phenol/CDN prior report). Standards Primacy applied (all RR cite [[hazop/risk-matrix]]; safeguard adequacy per [[sources/P-Q-MP-OEMS-005]]/[[hazop/methodology]]). Economic = BU (already resolved 2026-06-17). Node Boundary Rule: boundaries taken from green markup; three handoffs (to 23-04 E-2306, 23-05 V-2302 body, Decomposer-feed node) flagged for engineer confirmation.
Deviations analysed: 17 consequence chains across Flow (No/Low, More, Reverse), Temperature (More ×2, Less), Pressure (More ×2, Vacuum), Level (D-2309 High/Low), Service Failures (power, IA, seal flush), Composition (tube leak, contamination). Dominant hazard: over-temperature / loss-of-removal of concentrated CHP → DIERS runaway (deflagration/detonation potential).
Pages created: wiki/hazop/nodes/cdn-N03.md
Pages updated: wiki/hazop/action-register.md (R-005..R-009 added), wiki/hazop/interlock-esd-summary.md (UC-2301 Causes 6/8/9/10/11 + UXV-0701-0706 + UXV-0802/0803), wiki/hazop/study-info.md (Node Status Register: CDN-N03 → PRELIMINARY DRAFT; node-numbering note)
Recommendations: R-005 (LOPA/SIF verification of combined overheat protection, Medium), R-006 (E-2304 tube / P-2301 deadhead & block-isolated relief, High), R-007 (P-2301 seal-flush loss detection, Medium), R-008 (E-2304 tube-leak / CHP-condensate migration detection, High), R-009 (P-2301 discharge check-valve vs acid backflow, Medium).
Status: PRELIMINARY — desktop first-pass to seed the facilitated workshop; NOT team-validated. Boundaries + worksheet require engineer/HAZOP-team confirmation per [[hazop/methodology]].

## [2026-06-18] output | 2026-06-18_CDN-N03_HAZOP-worksheet.xlsx

Type: export (HAZOP worksheet, Excel — PRELIMINARY)
Destination: output/exports/hazop/2026-06-18_CDN-N03_HAZOP-worksheet.xlsx
Build script: output/working/build_cdn_n03_xlsx.py (openpyxl; adapted from build_cdn_n02_xlsx.py)
Structure: same 7-tab GC HAZOP template as CDN-N02 — Cover Page, HAZOP Information, WorkSheet Index, WorkSheet CDN-N03, Action Items, Risk Ranking, Interlock-ESD Summary.
WorkSheet tab: 3 risk blocks (Without Safeguard / Existing Safeguard + IL/ESD flag + IPL / With Existing Safeguard) + blank "After Recommendation Comp." block for close-out; 17 deviation consequences across 43 safeguard rows; RR cells colour-coded; autofilter + freeze panes; merged descriptive/risk cells.
Content source: [[hazop/nodes/cdn-N03]] (2026-06-18 preliminary pass; Economic=BU). Action Items tab = R-005..R-009; Interlock-ESD tab = LXSHH-0802 / TXSHH-0701A/0702A / TXSHH-0701B/0702B / TXSHH-0805A/B / TXSHH-0901A/B / UXV-0701-0706 / UXV-0802/0803.
Note: filterable/sortable for analysis. Remains PRELIMINARY pending HAZOP team validation.

## [2026-06-18] output | 2026-06-18_CDN-N02_HAZOP-worksheet.xlsx

Type: export (HAZOP worksheet, Excel — PRELIMINARY)
Destination: output/exports/hazop/2026-06-18_CDN-N02_HAZOP-worksheet.xlsx
Build script: output/working/build_cdn_n02_xlsx.py (openpyxl 3.1.5)
Structure: mirrors the GC HAZOP template tabs per [[hazop/templates/gc-hazop-worksheet-template]] — 7 tabs: Cover Page, HAZOP Information, WorkSheet Index, WorkSheet CDN-N02, Action Items, Risk Ranking, Interlock-ESD Summary.
WorkSheet tab: 3 risk blocks (Without Safeguard / Existing Safeguard + IL/ESD flag + IPL / With Existing Safeguard) plus a blank "After Recommendation Comp." block for close-out; 17 deviation consequences across 36 safeguard rows; RR cells colour-coded (Extreme dark-red → Very Low green); autofilter on header row; freeze panes; descriptive/risk cells merged across each consequence's safeguard rows.
Content source: [[hazop/nodes/cdn-N02]] (2026-06-17 preliminary pass; Economic=BU). Action Items tab = R-001..R-004; Interlock-ESD tab = FXSLL-0401 / TXSHH-0501 / TXSHH-0502A/B / UXV-0501-0502.
Note: filterable/sortable for analysis (e.g. filter RR=High/Extreme, or IL/ESD=Yes). Remains PRELIMINARY pending HAZOP team validation.

## [2026-06-17] output | 2026-06-17_CDN-N02_HAZOP-report_preliminary.docx

Type: report (formal HAZOP study report — PRELIMINARY)
Destination: output/reports/hazop/2026-06-17_CDN-N02_HAZOP-report_preliminary.docx
Working source: output/working/2026-06-17_CDN-N02_HAZOP-report_preliminary.md (markdown master; converted to .docx via pandoc 3.8, with TOC)
Format note: .docx chosen (no LaTeX/PDF engine available in environment for direct PDF; pandoc→docx is native). Convert to PDF later if a PDF engine is installed.
Source wiki pages: [[hazop/nodes/cdn-N02]], [[hazop/action-register]], [[hazop/interlock-esd-summary]], [[hazop/risk-matrix]], [[hazop/methodology]], [[hazop/study-info]], [[equipment/E-2302AB]], [[equipment/E-2303]], [[equipment/D-2308]], [[equipment/P-2308AB]], [[hazards/cumene-hydroperoxide]], [[instruments/cause-effect-cdn]]
Content: full preliminary CDN-N02 report — scope/boundaries (engineer-confirmed), methodology (Economic=BU), design intent + normal params, CHP hazard, 13-deviation worksheet, 4 recommendations (R-001..R-004), IL/ESD safeguards, outstanding items, preliminary disclaimer.

## [2026-06-17] hazop-node | CDN-N02 — engineer confirmations applied (boundaries + Economic=BU)

Study owner answered the three open items on the CDN-N02 preliminary worksheet:
1. **Boundaries CONFIRMED** — the recorded node 23-02 boundary interpretation is correct (inlet tie-in N01↔N02 and the Dwg 0007 segment both confirmed). "To confirm" flags in [[hazop/nodes/cdn-N02]] changed to ✅ confirmed.
2. **Economic category RESOLVED: PPCL = BU.** Applied GC ePHA Template v5.0 BU thresholds (Extreme ≥100 M / High 10–<100 M / Medium 1–<10 M / Low 0.1–<1 M / Very Low <0.1 M). Recorded the resolution on [[hazop/risk-matrix]] Economic section (long-standing wiki Open Conflict now resolved *for PPCL*; category-naming conflict retained as historical reference). Economic scores added to all CDN-N02 deviation rows + the interlock/ESD summary: CHP catastrophic rows Ec 5 (People 5 still binds — RR unchanged); production-loss rows #2.1/#5.1 scored Ec 2 (first-pass, team to validate vs rate-loss financials).
3. **Mode confirmed:** system generates PRELIMINARY info; human/specialist team finalizes and reviews. Node remains PRELIMINARY.

Re-ranking effect of Economic=BU:
- #2.1 (More Flow): with-safeguard RR Very Low → **Low** (S now 2).
- #5.1 (Low Temp / steam loss): without-safeguard RR Low → **Medium**; residual (with safeguard) stays **Low** → no new recommendation.
- No change to recommendation set (R-001..R-004 unchanged); no residual ≥ Medium introduced.

Pages updated: wiki/hazop/nodes/cdn-N02.md (status, boundaries, Economic note, severities, two row re-ranks), wiki/hazop/interlock-esd-summary.md (Ec scores), wiki/hazop/risk-matrix.md (PPCL=BU resolution).

## [2026-06-17] hazop-node | CDN-N02 (markup "Node 23-02") — Preflash Column feed-heating / steam-condensate circuit — PRELIMINARY

Trigger: User supplied "Node 23-02.pdf" expert P&ID markup and requested a preliminary HAZOP for the node. Run via the `hazop` skill (NODE workflow).

Pre-flight: Anti-Bias ✅ (only HAZOP report in raw/ is the deliberately-scoped O-P3 example, different plant — no Phenol/CDN prior report). Standards present ✅ (risk-matrix, methodology, study-info, P-Q-MP-OEMS-005). 

Node scope (from markup): Preflash Column feed-heating train + steam-condensate subsystem — E-2302A/B (Feed-Oxidate Exchangers), E-2303 (Preflash Column Steam Heater), D-2308 (Condensate Drum), P-2308A/B (Condensate Pumps). Drawings 0005/0005A primary; 0004 (heated-feed stab-in to V-2301) and 0007 (short segment) boundary crossings. Dominant hazard: over-temperature of ~22.6 wt% CHP-containing oxidate above ~80 °C decomposition onset (heating medium SC1.5 steam ~120–133 °C).

Deviations worked: 13 deviation groups (Flow No/More/Reverse; Temperature More/Less; Pressure More/Less; Level More/Less; Service Failures; Composition/Tube Leak E-2303 & E-2302; Composition contamination; plus the "Other" checklist). Full-record approach — N/A items justified.

Pages created:
- wiki/hazop/nodes/cdn-N02.md — preliminary node worksheet (3-risk-block hierarchical schema; IL/ESD flags; IPL credits)

Pages updated:
- wiki/hazop/action-register.md — 4 preliminary recommendations R-001..R-004 added (skill schema with Owner Type / Completion / Approved columns)
- wiki/hazop/interlock-esd-summary.md — 4 IL/ESD safeguard rows (FXSLL-0401, TXSHH-0501, TXSHH-0502A/B, UXV-0501/0502) cross-checked vs C&E Causes 1/2/3
- wiki/hazop/study-info.md — Node Status Register seeded with CDN-N01/02/03/05/06 from the markup; N02 = PRELIMINARY DRAFT

Recommendations (preliminary, Rec# range R-001 to R-004):
- R-001 (Medium): LOPA/SIF verification of overheat protection vs S5 CHP consequence; setpoint margin below 80 °C; startup-bypass (HXS-0102) interaction.
- R-002 (High): on-line CHP/HC detection on D-2308 condensate to catch E-2303 tube leak before CHP migrates to utility condensate system.
- R-003 (Medium): block-isolated maintenance overpressure/thermal relief for E-2302A/B & E-2303 process side (no dedicated PSV once isolated from V-2301).
- R-004 (Low): resolve oxidate feed pressure data conflict (78 vs ~8/12 kg/cm²g).

Rule compliance / open items:
- Standards Primacy: all risk rankings cite [[wiki/hazop/risk-matrix]].
- Economic Severity Conflict (rule 4): NO Economic score assigned — used highest of People/Env/Social; rows where Economic would bind (#2.1, #5.1) flagged [Ec: CONFLICT — unresolved]. PPCL plant category still to be confirmed by team.
- Node Boundary Rule: core circuit confirmed from markup; exact N01↔N02 feed tie-in and the 0007 yellow segment flagged for engineer confirmation (not guessed).
- Status: PRELIMINARY desktop pass — requires HAZOP team facilitation to finalize. HAZOP Coordinator sign-off on Table A6.2-3 and PSV set-pressure items still outstanding per study-info.

## [2026-06-16] ingest | CDN Static Vessel Process Data Sheets (D-2301 through D-2312, 11 sheets)

Files: 11 AS-BUILT/FINAL (Rev Z1, 2014-2016) process specification sheets from raw/data_sheets/ — the last un-ingested data sheet batch in raw/. Source: POSCO Engineering for PTT Phenol Train II (PPCL). Licensor: UOP/Honeywell.

Data sheets ingested (11 files): D-2301 (Concentration Cumene Quench Drum), D-2302 (Cumene Flush Drum), D-2303 (Decomposer Feed Flush Drum), D-2304 (Decomposer Drum), D-2306 (Acid Aromatics Knockout Drum), D-2307 (Acid Aromatics Sump), D-2308 (Preflash Column Steam Heater Condensate Drum), D-2309 (Flash Column Vaporizer Condensate Drum), D-2310 (98% H2SO4 Injection Tank), D-2311 (98% H2SO4 Refill Tank), D-2312 (Diamine Injection Tank).

Bookkeeping note: on reading the equipment pages it was discovered that 10 of the 11 data sheets (all except D-2312) had already been merged into the corresponding wiki/equipment/ pages in a prior session (pages carry last_updated: 2026-06-14, citing a source page that was never created). This entry completes that bookkeeping retroactively and newly ingests D-2312.

Pages created:
- wiki/sources/ps-cdn-vessel-batch-2026-06-14.md — retroactive source summary for all 11 sheets

Pages updated:
- wiki/equipment/D-2312.md — full mechanical data added (material 304L SS, CA 1.5mm, MDMT 15°C, density 914 kg/m3, operating volume); fluid identity conflict flagged
- wiki/hazards/diamine-tbc.md — identity conflict reopened (DIPA vs DIAMINE/HMDA)
- wiki/index.md — status banner, equipment table cleanup (removed stale duplicate "(pending page)" rows for D-2308/D-2309/E-2301/E-2302/E-2303/E-2306/E-2310), Sources Ingested table, Open Conflicts table (4 new rows), Gaps section, HAZOP status line

Key findings:
- D-2304 (Decomposer Drum) confirmed SA 240 Type 304L SS construction, CA 1.5mm
- D-2307 (Acid Aromatics Sump) is an existing Train I vessel (2007 fabrication, shared with Train II, no modification required)
- D-2308 operating temperature corrected from 63C (P&ID-era) to 117C (DS) — consistent with SC1.5 condensate near saturation at 0.9 kg/cm2g
- D-2309 insulation corrected from H(80) to H(90)
- D-2310/D-2311 (98% H2SO4 tanks) confirmed SA 240 304L, MDMT 15C, density 1728.7 kg/m3, readymade totes acceptable
- ⛔ **D-2312 CRITICAL FINDING**: data sheet Fluid Name field reads "DIAMINE(HMDA)" = Hexamethylenediamine (CAS 124-09-4), density 914 kg/m3, Amine service = YES. This conflicts with wiki/hazards/diamine-tbc.md, which on 2026-06-14 "confirmed" the additive as DIPA (Diisopropanolamine, CAS 110-97-4) based on an SDS file whose own filename contains "placeholder". DIPA's typical density (~1010 kg/m3) does not match the DS value (914 kg/m3); HMDA is the better fit. Per the Standards Primacy Rule, the as-built engineering data sheet outranks the placeholder-named SDS match. Flagged in equipment/D-2312.md, hazards/diamine-tbc.md, and index.md Open Conflicts. **A genuine plant SDS for hexamethylenediamine is required before any HAZOP deviation analysis on D-2312, P-2306A/B, or X-2310A/B.**

PSI status: Category 6 (Equipment Data Sheets) now COMPLETE for all CDN equipment (heat exchangers, rotating equipment, static vessels). raw/data_sheets/ has no remaining un-ingested files.

## [2026-06-16] ingest | OM-Phenol Unit UOP-2015.pdf — Sections V (Pre-commissioning) and VI (Start-up), CDN focus

Trigger: User noted that startup/pre-commissioning/commissioning content was likely present in the already-ingested UOP GOM but had not been extracted in the original 2026-06-13 ingest (which covered Sections II, III, VII, IX, X, XI only).
Source: raw/operating_manuals/OM-Phenol Unit UOP-2015.pdf (already in raw/, no file move needed) — PDF pages 157–232 (GOM Section V, pp. V-1 to V-21; Section VI, pp. VI-1 to VI-50).
Method: extracted via pypdf (installed locally — no PDF text tool was previously available in this environment); confirmed page offsets against printed page numbers (V-1 = PDF p.157, VI-1 = PDF p.179).

Pages created (2):
- wiki/procedures/precommissioning-cdn.md — CDN-relevant extract of GOM §V: vessel/exchanger/pump inspection criteria, hydrostatic test (1.5x piping / 1.3x equipment design pressure), line flushing sequence, pump run-in (centrifugal vs. positive-displacement vs. sealless mag-drive), instrument calibration/loop-check, CHP/acid-aromatics drain leak-test and routing verification, concentration vacuum system (X-2301 ejectors + P-2316/2317) commissioning and vacuum leak-testing, air-freeing to <0.5 vol% O2.
- wiki/procedures/startup-cdn.md — CDN-relevant extract of GOM §VI.A (Initial Start-up) and §VI.B (Normal Start-up): Concentration long-circulation establishment and heat-up; Decomposition pre-feed prep, decomposer feed-in sequence (acid build-up to 300 wt ppm, verification checklist, ramp-in, no-reaction abort protocol), post-feed-in optimization down to design 60°C with calorimeter ΔT diagnostics; Neutralization ratio control start-up.

Pages updated (4):
- wiki/sources/om-phenol-uop-2015.md — Sections Extracted table now includes V and VI with PDF page ranges; Pages Created list updated; new "Start-up / Pre-commissioning Highlights" key-findings subsection added
- wiki/units/cdn.md — Procedures table: added Pre-commissioning and Start-up rows
- wiki/index.md — status banner, Procedures table, Sources Ingested table row for the GOM, wiki page count 137+→139+

Key findings:
- **Decomposer feed-in is the single highest-risk operation in CDN start-up.** GOM contains an explicit warning: if there is no exothermic response after CHP feed-in, operators must NOT increase sulfuric acid injection without first lab-confirming CHP concentration is below 0.2 wt% — acid injection into an acid-starved, CHP-rich system risks runaway decomposition and possible explosion. This same constraint (≤5% acid rate increase per step) applies again during post-feed-in optimization toward the 60°C design setpoint.
- Zero calorimeter ΔT immediately after feed-in is a **normal** artifact of the high-acid/high-temperature start-up condition, not a fault signal — risk of misinterpretation by an operator unfamiliar with this nuance.
- Acid build-up to 300 wt ppm before feed-in must not be overshot — excess acid causes too-fast reaction on feed-in, risking circulation pump cavitation and decomposer shutdown.
- Neutralization section readiness is an explicit hard gate before decomposer feed-in is started (GOM capitalized warning).
- Pre-commissioning of the concentration vacuum system (X-2301) requires ejector steam-line cleaning before first use (jet orifices are only a few mm — debris causes repeated capacity loss/shutdowns) and a formal 1-hour vacuum-hold leak test before hydrocarbon introduction.
- CHP drain and acid-aromatics drain routing must be individually leak-tested and verified at commissioning by hosing each point and watching for correct collection-vessel response — not assumed correct from the P&ID, given the mandatory separation between these two systems (H2SO4 + CHP reaction hazard).
- This closes a real gap in PSI/HAZOP readiness: GOM §V/VI is part of the "Operating Procedures" PSI category (Table A6.2-2, Category 5) — startup procedures were previously entirely absent from the wiki despite the source document already being ingested.

## [2026-06-16] ingest | CDN Rotating Equipment, Filters & Vacuum Package Process Data Sheets — 13 AS-BUILT sheets

Files: 13 process/project specification sheets sorted from input/ → raw/data_sheets/ (14780-8120-PS-* series, Rev Z1, As-Built, May 10, 2016)
Source: POSCO Engineering & Construction for PTT Phenol Train II (PPCL). UOP licence, Project Spec 963766.
Purpose: Closes PSI Readiness Table A6.2-2 Item 4 (Equipment Data Sheets) for CDN rotating equipment, filters, and vacuum package.

Files ingested (raw/data_sheets/): PS-P2301, P2302, P2303, P2304, P2305, P2306, P2307, P2308, P2309, P2320, X2301, X2302, X2309 (all .pdf, Rev Z1)

Pages updated (13, all pre-existing from 2026-06-06/07 P&ID-only ingest):
- wiki/equipment/P-2301AB.md — API 610 OH2 confirmed; Pressurized Dual seal API Plan 11/53A, N2 barrier 7 kg/cm2(g); M13 standby independent power confirmed
- wiki/equipment/P-2302.md — API 610 BB1 double-suction; CONFLICTS flagged (capacity 2020 vs 3020 m3/h; SG 0.906 vs 0.996); seal Plan 53B vs previously noted 53A
- wiki/equipment/P-2303AB.md — API 610 OH2 confirmed; seal Plan 02/53A confirmed; motor power CONFLICT (37kW wiki vs 23.8kW PS rated hydraulic)
- wiki/equipment/P-2304A.md — revealed as API 610 BB4 vertical sump pump; Non-contacting Dual seal API Plan 74, N2 barrier; CONFLICTS flagged (diff press 3.53 vs 7.53; SG 0.826 vs 0.926)
- wiki/equipment/P-2305ABCDEF.md — API 675 metering pumps; Alloy 20 wetted parts confirmed (98% H2SO4 service)
- wiki/equipment/P-2306AB.md — API 675 metering pumps; 316 SS wetted parts; copper/copper-alloy prohibition noted (diamine corrosivity)
- wiki/equipment/P-2307AB.md — API 610 OH2 confirmed; no M13 (confirms not on reliable power); 99.8% cumene composition confirmed
- wiki/equipment/P-2308AB.md — **revealed as API 685 sealless magnetic-drive pump** (SiC bearings, 316SS containment shell) — corrects "Seal plan: Basic" entry; autostart static pressure 2.25 kg/cm2(g)
- wiki/equipment/P-2309AB.md — same sealless mag-drive correction as P-2308; CONFLICT flagged (capacity 15.3 vs 13.3 m3/hr); autostart static pressure 3.80 kg/cm2(g)
- wiki/equipment/P-2320.md — Zone 1 electrical classification confirmed (vs surrounding Zone 2); CONFLICT flagged (diff press 0.69 vs 0.99 kg/cm2g); common spare P-9108S
- wiki/equipment/X-2301.md — UOP vacuum package spec (Gardner Denver Nash) confirms ejector/LRVP/intercondenser design, materials, sealant system, SIS shutdowns
- wiki/equipment/X-2302AB.md — filter cartridge material specified (glass fiber on SS core); max flow 275 m3/hr added; 24 spare elements required
- wiki/equipment/X-2308.md (tagged X-2309A/B) — tag independently re-confirmed by PS-X2309; **Hastelloy C276 internal liner** revealed (new safety-relevant material finding for combined H2SO4/CHP service)
- wiki/sources/ps-rotating-equipment-batch-2026-06-16.md (NEW — consolidated source summary)
- wiki/index.md — status banner, equipment tables (CDN sections), Sources Ingested table, Open Conflicts table (6 new conflicts), Gaps item 6 updated

Key findings:
- Sealless magnetic-drive technology confirmed on P-2308A/B and P-2309A/B (API 685) — no mechanical seal, eliminates seal-leak failure mode for condensate service
- Standby/reliable power supply (Motor Note M13) confirmed present on all CHP/decomposer-product duty pumps (P-2301, P-2302, P-2303) and absent on recycle-cumene duty pump (P-2307) — consistent with existing risk-based power assignment
- Calorimeters (X-2309A/B) have Hastelloy C276 wetted internals — not previously documented; addresses combined H2SO4/CHP corrosion severity
- P-2320 sump pit pump is in a Zone 1 area, more hazardous than the surrounding CDN Zone 2 classification — flag for HAZOP node scoping
- 6 data conflicts identified between earlier P&ID-derived wiki entries and this data sheet batch — all flagged per Confidence Level convention, PS values adopted as authoritative pending field verification
- PSI status: CDN equipment data sheets for rotating equipment, filters, and vacuum package now substantially complete

## [2026-06-14] ingest | Static Equipment Process Data Sheets — 15 AS-BUILT sheets (ALKY, OXI, CDN update)

Files: 15 process data sheets sorted from input/ → raw/data_sheets/ (14780-8120-PS-* series, Rev Z1, As-Built, May 2016)
Source: POSCO Engineering & Construction for PTT Phenol Train II (PPCL). UOP licence. Spec refs: 963764 (ALKY), 963765 (OXI), 963766 (CDN).
Purpose: Closes PSI Readiness Table A6.2-2 Item 4 (Equipment Data Sheets) for OXI and ALKY static equipment.

Files ingested (raw/data_sheets/): 14780-8120-PS-D-2121.pdf, D-2122.pdf (ALKY); D-2201, D-2202, D-2203, D-2204ABC, D-2205, D-2206, D-2207, D-2208, D-2211, OX-2201, OX-2202, V-2201.pdf (OXI); V-2301.pdf (CDN update)

Pages created (14 new):
- wiki/equipment/D-2121.md, D-2122.md (ALKY — condensate pots; KCS; 50 kg/cm²g / 300°C design)
- wiki/equipment/D-2201.md, D-2202.md, D-2203.md, D-2204ABC.md, D-2205.md, D-2206.md, D-2207.md, D-2208.md, D-2211.md (OXI drums/vessels/separators)
- wiki/equipment/OX-2201.md, OX-2202.md (OXI — API 620; 21.7 m ID × 11.8 m; A240 304/304L Dual Stamp)
- wiki/equipment/V-2201.md (OXI — horizontal L-L extractor; 4000 mm ID × 29,400 mm; caustic service)
- wiki/sources/ps-static-equipment-batch-2026-06-14.md (source summary)

Pages updated (1):
- wiki/equipment/V-2301.md — formal Design Data table added; packed bed (Sulzer Mellapak 250X 700 mm); reboiler nozzle sizes (BC=1120 mm, CD=1160 mm); T/T 21,000 mm confirmed (P&ID 7550 mm SUPERSEDED); design temp CONFLICT flagged (DS 250°C vs DWG 230°C)
- wiki/index.md — OXI section equipment table (11 items); ALKY section equipment table (2 items); Sources table; status banner; Gaps item 6 updated to PARTIAL

Key findings:
- Subzero MDMT: D-2203 and D-2211 rated MDMT −10°C (operating 5°C) — cold service, impact-tested SS required
- Severe cyclic: D-2204A/B/C cycles 16°C ↔ 120°C every 6 hr (adsorption–regeneration) — ASME fatigue provisions apply
- API 620 oxidizers: OX-2201/2202 each have 3,988-hole air spargers, 30 Ketema eductors, PVRV vacuum relief (Protectoseal 6240V, 0.0088 kg/cm²g vacuum per API-2000)
- Elevation constraints: D-2203 and D-2211 ≥ 2500 mm above D-2205; D-2208 ≥ 600 mm above D-2205 (gravity drain)
- CHP sump (D-2206): underground; EPA 40 CFR Part 280 secondary containment required
- PSI status: OXI static equipment now documented. Still missing: rotating equipment DS; ALKY reactors/columns; CDN remaining vessels; heat exchangers

## [2026-06-14] pss-confirm | PSS Data Baseline Confirmed — SDS Conflicts, ECHA Classifications, Chemical Identities

Trigger: User-confirmed resolutions to outstanding PSI/SDS actions
Source: User confirmation 2026-06-14 — decisions applied as worst-case PSS conservative basis

**Resolutions applied:**

1. DIAMINE IDENTITY CONFIRMED
   - Additive at D-2312/P-2306A-B/X-2310A-B confirmed as DIPA (Diisopropanolamine, CAS 110-97-4)
   - wiki/hazards/diamine-tbc.md rewritten as full confirmed hazard page (PLACEHOLDER status removed)

2. DATA CONFLICTS RESOLVED — WORST-CASE BASIS ADOPTED
   - CHP decomp onset: 80°C (SDS_80-15-9 DSC value) adopted as PSS working value; previous 100°C superseded
   - Phenol LEL/UEL: 1.3% / 9.0% (SDS_108-95-2) adopted as PSS worst-case; previous 1.7%/8.6% superseded
   - Rationale: wider flammable range and lower onset = more conservative for fire/explosion and thermal runaway consequence analysis

3. ECHA PRECAUTIONARY CLASSIFICATIONS CONFIRMED FOR PSS USE
   - Cumene: Carc 1B (H350) applied as precautionary PSS working classification
   - AMS: H304 (Asp Tox 1) + H361 (Repr 2) + Skin Sens 1B applied as precautionary PSS basis
   - DIPB: H304 (Asp Tox 1) + H411 (Aquatic Chronic 2) applied as precautionary PSS basis
   - Benzene: 0.02 ppm adopted as working OEL for PSS (ACGIH 2024 NIC precautionary value)
   - DMBA: CAS 100-86-7 confirmed; H301 (Acute Tox 3) adopted as worst-case PSS basis

Pages updated:
- wiki/hazards/diamine-tbc.md (full rewrite — confirmed DIPA identity)
- wiki/hazards/cumene-hydroperoxide.md (decomp onset 80°C, conflict resolved)
- wiki/hazards/phenol.md (LEL/UEL 1.3%/9.0%, conflict resolved)
- wiki/hazards/cumene.md (Carc 1B precautionary PSS classification applied)
- wiki/hazards/alpha-methylstyrene.md (H304/H361/Skin Sens 1B precautionary PSS basis applied)
- wiki/hazards/di-isopropylbenzene.md (H304/H411 precautionary PSS basis applied)
- wiki/hazards/benzene.md (OEL 0.02 ppm precautionary PSS working value applied)
- wiki/hazards/dimethylbenzylcarbinol.md (CAS 100-86-7 confirmed; H301 worst-case basis)
- wiki/hazop/study-info.md (PSS data baseline confirmed; outstanding blockers updated)
- wiki/index.md (status banner conflicts resolved; DIPA entry updated)

## [2026-06-14] ingest | SDS PSI Batch — 15 GHS Safety Data Sheets

Files: 15 SDS PDFs sorted from input/ → raw/standards/ (previously confirmed sorted)
Source: GHS 16-section Safety Data Sheets compiled for PTT Phenol (PPCL) Train II CDN HAZOP PSI
Purpose: Closes PSI Readiness Category 1 (Chemical and Reaction hazard — GHS-compliant SDS) per Table A6.2-2

**SDS files ingested (all in raw/standards/):**
1. SDS_80-15-9_cumene-hydroperoxide.pdf
2. SDS_108-95-2_phenol.pdf
3. SDS_71-43-2_benzene.pdf
4. SDS_7664-93-9_sulfuric-acid-98pct.pdf
5. SDS_98-82-8_cumene.pdf
6. SDS_67-64-1_acetone.pdf
7. SDS_98-83-9_alpha-methylstyrene.pdf
8. SDS_115-07-1_propylene.pdf
9. SDS_107-21-1_ethylene-glycol.pdf
10. SDS_110-97-4_dipa-placeholder-diamine-tbc.pdf (PLACEHOLDER — diamine identity TBC)
11. SDS_100-18-5_di-isopropylbenzene.pdf
12. SDS_100-86-7_dmba-dimethylbenzylcarbinol.pdf (IDENTITY FLAG — CAS 100-86-7 vs 617-94-7)
13. SDS_497-19-8_sodium-carbonate-solution.pdf
14. SDS_7727-37-9_nitrogen.pdf
15. SDS_98-86-2_acetophenone.pdf

Pages created (15 new hazard pages + 1 source summary):
- wiki/hazards/benzene.md (NEW)
- wiki/hazards/cumene.md (NEW)
- wiki/hazards/sulfuric-acid.md (NEW)
- wiki/hazards/acetone.md (NEW)
- wiki/hazards/alpha-methylstyrene.md (NEW)
- wiki/hazards/propylene.md (NEW)
- wiki/hazards/acetophenone.md (NEW)
- wiki/hazards/nitrogen.md (NEW)
- wiki/hazards/ethylene-glycol.md (NEW)
- wiki/hazards/di-isopropylbenzene.md (NEW)
- wiki/hazards/dimethylbenzylcarbinol.md (NEW)
- wiki/hazards/sodium-carbonate.md (NEW)
- wiki/hazards/diamine-tbc.md (NEW — PLACEHOLDER)
- wiki/sources/sds-psi-batch-2026-06-14.md (NEW — consolidated source summary)

Pages updated:
- wiki/hazards/cumene-hydroperoxide.md: Full GHS data from SDS; SADT 60–80°C; decomp onset CONFLICT flagged (80°C SDS vs 100°C wiki); sources frontmatter updated; UN 3105/3107 added; no OEL note
- wiki/hazards/phenol.md: Full GHS data; LEL/UEL CONFLICT flagged (1.3/9.0% SDS vs 1.7/8.6% wiki); IARC Group 3 added; PEG 300/400 noted; UN 1671/2312 added; sources frontmatter updated
- wiki/hazop/study-info.md: PSI Readiness Item 1 changed from ⚠️ Partial → ✅ Complete; outstanding blockers updated (SDS item resolved; diamine placeholder remains)
- wiki/index.md: Status banner updated; source count 68→84 (15 SDS + 1 source summary page); wiki pages 105+→121+; Hazards section expanded to 15 chemicals; Sources table updated; Gaps item 10 crossed off (with diamine caveat)

Key findings:
- **Data conflicts**: CHP decomp onset (80°C SDS vs 100°C wiki — flagged for operator verification); Phenol LEL/UEL (1.3%/9.0% SDS vs 1.7%/8.6% wiki — flagged for authoritative source resolution)
- **Identity flags**: Diamine additive CAS 110-97-4 (DIPA) is PLACEHOLDER — actual additive identity not confirmed; DMBA CAS 100-86-7 vs 617-94-7 ambiguity
- **Data quality flags**: Cumene Carc 1B (data artifact — ECHA verify); AMS H304/H361/Skin Sens 1B (Sigma-Aldrich only — ECHA verify); DIPB H304/H411 (structural analogy only — ECHA verify); Benzene OEL (ACGIH 2024 NIC proposes 0.02 ppm from 0.5 ppm)
- **Process-critical safety notes**: Acetone + CHP → shock-sensitive peroxide interaction; N₂ blanketing of D-2301 is critical SIS safeguard; AMS requires TBC/MEHQ inhibitor; Na₂CO₃ + H₂SO₄ → CO₂ pressure in closed vessels; acetophenone solidifies at 19.6°C (heat tracing required)

## [2026-06-14] ingest | 7. Chapter 6 - Facilitator skill.pdf — HAZOP Leadership Training Ch.6

File: raw/standards/7. Chapter 6 - Facilitator skill.pdf
Sorted from: input/ → raw/standards/ (same Q-TS-TS training series)
Source: PTT Global Chemical — Technical Safety Service Division (Q-TS-TS), HAZOP Leadership Course Ch.6, Nov 2021
Size: 19 slides — 4 sub-chapters (6-1 Effectiveness, 6-2 Decision Making, 6-3 Facilitator Role, 6-4 Active Listening)
Nature: Facilitation / soft-skills chapter — no new process or risk matrix content

Pages created:
- wiki/sources/hazop-leadership-training-ch6.md

Pages updated:
- wiki/hazop/study-info.md:
  - Added: Session Management section — facilitation guidance for when node analysis begins
  - Added: Decision-making approach (consensus preferred)
  - Added: 9 core + 4 supplementary HAZOP ground rules (to be agreed at first session)
  - Added: Progressive leader role table (Trainer/Team Builder/Facilitator/Editor vs. session phase)
- wiki/index.md: status banner (Ch.1–5 → Ch.1–6); source count 66→67; wiki pages 103+→104+; Sources table

Key findings:
- Sub-chapter 6-1 (Effectiveness): 6 hidden costs of poor PHA; 7 components of effective meeting — "person in charge has no direct stake in conclusions" confirms Leader independence requirement
- Sub-chapter 6-2 (Decision making): 4-level decision spectrum; consensus is preferred but acknowledged as "difficult to achieve when dealing with EPCC and Owner"
- Sub-chapter 6-3 (Facilitator): 4 progressive roles (Trainer→Team Builder→Facilitator→Editor); 9 core ground rules; "Do not design solution in HAZOP meeting" — important constraint for our CDN study; facilitator uses parking lot for issues Scribe doesn't capture; deals with difficult personalities
- Sub-chapter 6-4 (Active listening): 3 techniques — complete attention, paraphrasing, summarizing

## [2026-06-14] ingest | 8. Chapter 7 - GC HAZOP Workflow.pdf — HAZOP Leadership Training Ch.7

File: raw/standards/8. Chapter 7 - GC HAZOP Workflow.pdf
Sorted from: input/ → raw/standards/ (same Q-TS-TS training series — final chapter)
Source: PTT Global Chemical — Technical Safety Service Division (Q-TS-TS), HAZOP Leadership Course Ch.7, Nov 2021
Size: 7 slides — 2 sub-chapters (7-1 PHA document list, 7-2 GC HAZOP Workflow)

Pages created:
- wiki/sources/hazop-leadership-training-ch7.md

Pages updated:
- wiki/hazop/methodology.md:
  - Added: GC HAZOP Workflow section — 5 phases (Initiate/Prepare/Workshop/Report/Close-out)
  - Added: 4 report status states (Draft → Submitted → Publish → Complete)
  - Added: Action change process — HAZOP Coordinator Champion role; team re-evaluation gate
  - Added: 7-role responsibility summary for the workflow
  - Updated: References section (added Ch.7 source link)
- wiki/hazop/study-info.md:
  - Added: GC HAZOP Workflow — Study Phase Tracking table (5 phases with current status)
  - Added: Action change protocol note
  - Updated: References section (added Ch.7 source link)
- wiki/index.md: status banner (Ch.1–6 → Ch.1–7 COMPLETE); source count 67→68; wiki pages 104+→105+; Sources Ingested table; Methodology description updated

Key findings:
- Sub-chapter 7-1 (PHA documents): Full GC PHA ecosystem confirmed — Qualitative (HAZOP/HAZID/ENVID/Prelim SHE), Quantitative (QRA/LOPA), Visualization (Bow-Tie). Document codes in training use 2021 Q-TS prefix; current governing versions use Q-MP prefix (already ingested: P-(Q-MP)-OEMS-005 R4, SG-(Q-MP)-014 R3)
- Sub-chapter 7-2 (Workflow): End-to-end GC HAZOP lifecycle — CRT triggers study → Coordinator prepares PSI → Team workshops → Scribe writes Draft → HAZOP Leader approves (Submitted → Publish) → Action close-out by Responsible Person with Action Approver gate → Report status "Complete". CRITICAL: action deviations from workshop require HAZOP Coordinator Champion to raise change request; team must re-evaluate risk before any action revision is accepted.
- GC HAZOP Training Course (Intro + Ch.1–7) is now COMPLETE — all 8 training documents ingested.

## [2026-06-14] ingest | 6. Chapter 5 - HAZOP Preparation.pdf — HAZOP Leadership Training Ch.5

File: raw/standards/6. Chapter 5 - HAZOP Preparation.pdf
Sorted from: input/ → raw/standards/ (same Q-TS-TS training series)
Source: PTT Global Chemical — Technical Safety Service Division (Q-TS-TS), HAZOP Leadership Course Ch.5, Nov 2021
Size: 24 slides — 4 sub-chapters (5-1 Planning, 5-2 Documents, 5-3 Team, 5-4 Worksheet)

Pages created:
- wiki/sources/hazop-leadership-training-ch5.md

Pages updated:
- wiki/hazop/methodology.md:
  - Added: GC HAZOP worksheet official column structure (Parameter | Deviation | Cause | Consequence | Without Safeguard [L, P, En, Ec, S, RR] | Safeguard Detail | With Safeguard [L, P, En, Ec, S, RR] | Recommendation)
  - Added: Study preparation and scheduling section (session = 3.5 hr; 3 P&IDs/day process; 4 utilities; SIL adds 20%; cost benchmarks)
  - Added: First team meeting agenda (6-item checklist)
  - Updated: References section
- wiki/hazop/study-info.md:
  - Updated: Study Team table — added regulatory basis column (GC vs IEAT PSM 2559 vs DIW 2543); added Licensor/specialist row; Scribe notes on role requirements
- wiki/index.md: status banner (Ch.1–4 → Ch.1–5); source count 65→66; wiki pages 102+→103+; Sources Ingested table

Key findings:
- Sub-chapter 5-1 (Planning): 4 planning elements (Purpose/Timing/Process Type/Admin); session = half working day (~3.5 hr); 3 P&IDs/day process, 4/day utilities; SIL/LOPA adds 20% time; HAZOP ≈ 0.2% capex or ≈ 1% design cost; "Lead should obtain clear scope from HAZOP Coordinator"
- Sub-chapter 5-2 (Documents): Full 20-document PSI matrix by project phase (Select/Define/Execute/Operation/Non-op); "Garbage in, Garbage out"; PSI must be As-built signed for operating facilities; HAZOP Leader evaluates PSI adequacy; "Previous HAZID/HAZOP" = Essential for Operation phase — Anti-Bias Rule applies
- Sub-chapter 5-3 (Team): Regulatory comparison GC vs IEAT PSM 2559 vs DIW 2543; Scribe = GC-only requirement; Licensor/specialist = optional; 7 HAZOP Leader characteristics; 7 Leader responsibilities; Scribe follows without participating; projects live recording; first team meeting 6-agenda items
- Sub-chapter 5-4 (Worksheet): Official GC worksheet template confirmed with PEES sub-columns (P/En/Ec/S) in each risk block; e-PHA online system (MoC-PHA/Revalidation-PHA/Project-PHA modules); downloadable Excel template available

## [2026-06-14] ingest | 5. Chapter 4 - HAZOP Methodology.pdf — HAZOP Leadership Training Ch.4

File: raw/standards/5. Chapter 4 - HAZOP Methodology.pdf
Sorted from: input/ → raw/standards/ (same Q-TS-TS training series)
Source: PTT Global Chemical — Technical Safety Service Division (Q-TS-TS), HAZOP Leadership Course Ch.4, Nov 2021
Size: 37,502 chars — largest chapter; 9 sub-chapters (4-1 through 4-9)

Pages created:
- wiki/sources/hazop-leadership-training-ch4.md

Pages updated:
- wiki/hazop/methodology.md:
  - Added: Node size trade-off guidance (big vs small node pros/cons)
  - Added: Causes NOT considered under HAZOP (4 excluded types: design issues, PSV/SIF failure, flange/gasket leak, LO/LC valve closure)
  - Added: DO/DON'T recording examples for causes, consequences, safeguards, recommendations
  - Added: Standard deviation set (17 deviations × 6 equipment types table)
  - Added: HAZOP "Other" checklist words (10 topics: relief, instrumentation, sampling, corrosion, leakage, service failure, maintenance, start-up, spare equipment, safety equipment)
  - Added: Footnote on pump/compressor likelihood discrepancy (training 2021 → L3; governing SG-(Q-MP)-014 R3 2026 → L4)
- wiki/index.md (status banner; source count 64→65; wiki pages 101+→102+; Sources Ingested table)

Key findings:
- Sub-chapter 4-1 (Node prep): node must not cross P&ID boundaries; practical boundary at vessel interface or end of transfer lines; different operation modes need separate node; big vs small node trade-off
- Sub-chapter 4-2 (Guidewords): 7 guidewords defined; 17-deviation standard set by equipment type; 10 "Other" checklist topics
- Sub-chapter 4-3 (Causes): causes must be within node; PSV/SIF failure, flange leak, LO/LC valve closure explicitly excluded; recording must use equipment tags
- Sub-chapter 4-4 (Consequences): step-by-step chain with linking words; unmitigated; multiple consequences separately recorded
- Sub-chapter 4-5 (Safeguards): prevention first, then mitigation; fire protection NOT a safeguard; must include tag + setpoint + action
- Sub-chapter 4-6 (IPL): 3 criteria: Effective, Independent, Auditable; training/procedures/signs/fire protection NOT IPLs
- Sub-chapter 4-7 (Risk): initial risk (no safeguards) → mitigated risk (with IPLs); severity never changes; pump failure likelihood L3 in training vs L4 in governing doc — conflict flagged
- Sub-chapter 4-8 (Recommendations): action verb + WHY; no excessive/irrelevant recs; don't solve during session
- Sub-chapter 4-9 (References): never "see above"; use specific reference numbers; copy content rather than cross-reference

## [2026-06-13] ingest | 4. Chapter 3 – Introduction to HAZOP study.pdf — HAZOP Leadership Training Ch.3

File: raw/standards/4. Chapter 3 – Introduction to HAZOP study.pdf
Sorted from: input/ → raw/standards/ (script = UNCLASSIFIED; manual override — same Q-TS-TS training series)
Source: PTT Global Chemical — Technical Safety Service Division (Q-TS-TS), HAZOP Leadership Course Ch.3, Nov 2021

Pages created:
- wiki/sources/hazop-leadership-training-ch3.md

Pages updated:
- wiki/index.md (status banner source count 63→64; wiki pages 100+→101+; Sources Ingested table)

Key findings:
- HAZOP definition: systematic, qualitative, guideword-based; identifies hazards and operability problems
- History: Dr. H.G. Lawley, ICI Wilton, 1974; first guide ICI/CIA 1977
- Five HAZOP objectives: identify → assess extent → identify safeguards → propose recommendations → input to risk management
- Key limitations: PSI-dependent (supports PSI readiness requirement); no shortcuts (full-record approach); not for solving problems; time-consuming; team expertise critical
- Basic features: 5–7 person team, qualified leader, guideword-stimulated brainstorming
- No new plant-specific or process-specific content; training/methodological context only

## [2026-06-13] ingest | 3. Chapter 2 - Overview PHA techniqes.pdf — HAZOP Leadership Training Ch.2

File: raw/standards/3. Chapter 2 - Overview PHA techniqes.pdf
Sorted from: input/ → raw/standards/ (script = UNCLASSIFIED; manual override — same Q-TS-TS training series)
Source: PTT Global Chemical — Technical Safety Service Division (Q-TS-TS), HAZOP Leadership Course Ch.2, Nov 2021

Pages created:
- wiki/sources/hazop-leadership-training-ch2.md

Pages updated:
- wiki/index.md (status banner source count 62→63; wiki pages 99+→100+; Sources Ingested table)

Key findings:
- PHA technique historical timeline: Checklist (1960) → What-if (1972) → HAZOP (1974) — HAZOP is the modern standard
- IEAT (Thai DIW PSM) approved PHA list confirmed: What-if, Checklist, What-if/Checklist, HAZOP, FMEA, FTA — this CDN HAZOP study is compliant
- Project-phase applicability matrix: HAZOP is valid for Routine Operation phase (current study context) ✅
- Prelim SHE Assessment form: MOC screening tool with 8 trigger questions for further PHA; chemical hazard index scoring table (Inventory, Temp, Pressure, Flash Point, Explosiveness, Toxicity)
- Severity 4–5 from MOC screening → plant change must stop; Severity 3 → action required
- No new process-specific data; training/regulatory context only

## [2026-06-13] sort | input batch — HAZOP Training Course materials

Files sorted: 2
- `1. Course intoduction.pdf` → raw/standards/ (PTT GC internal HAZOP training; script = UNCLASSIFIED; manual override — Q-TS-TS produced standards material)
- `2. Chapter 1 - Hazard and Risk concept.pdf` → raw/standards/ (same series; manual override)
Unclassified by script: 2 (both; no keyword match)
Ingested immediately: yes

## [2026-06-13] ingest | 1. Course intoduction.pdf — PTT GC HAZOP Leadership Training: Course Introduction

File: raw/standards/1. Course intoduction.pdf
Source: PTT Global Chemical — Technical Safety Service Division (Q-TS-TS), 3-day HAZOP Leadership workshop, Nov 2021
Instructor: Mr. Noraphol Sookkho, Division Manager Q-TS-TS

Pages created:
- wiki/sources/hazop-leadership-training-intro.md

Pages updated:
- wiki/index.md (status banner source count 60→62; Sources Ingested table; wiki pages 97+→99+)

Key findings:
- Administrative course intro: objectives, 7-module 3-day schedule, workshop rules
- Produced by same Q-TS-TS team as P-(Q-MP)-OEMS-005, SG-(Q-MP)-014, W-(Q-MP)-002
- No new technical process content; contextual background only

## [2026-06-13] ingest | 2. Chapter 1 - Hazard and Risk concept.pdf — HAZOP Leadership Training Ch.1

File: raw/standards/2. Chapter 1 - Hazard and Risk concept.pdf
Source: PTT Global Chemical — Technical Safety Service Division (Q-TS-TS), HAZOP Leadership Course Ch.1, Nov 2021

Pages created:
- wiki/sources/hazop-leadership-training-ch1.md

Pages updated:
- wiki/index.md (Sources Ingested table; source count included above)

Key findings:
- Hazard/Harm/Risk definitions: RISK = Frequency × Consequence
- Three-tier PHA hierarchy confirmed: Qualitative (RAM) → Semi-Quant (LOPA) → Quantitative (QRA); this HAZOP study is Qualitative
- GC Master Risk Matrix PEES severity tables cross-confirm W-(Q-MP)-002 R2 — no discrepancies found
- Economic: PH-P1/PH-P2 codes listed under Downstream Plant — confirms Downstream thresholds apply for PTT Phenol
- Environmental: quantitative spill thresholds confirmed (1 bbl / 50 bbl / 100 bbl breakpoints)
- LOPC severity tied to API RP 754 Table 1 and Table 2 thresholds (Process Safety Event Tier 1 and Tier 2)
- W-(Q-MP)-002 R2 remains the authoritative source; training slides are cross-reference only

## [2026-06-13] ingest | Table A6.2-3 PID readiness checklist (Final R1)

Pages created: sources/Table-A6.2-3-PID-readiness-checklist.md
Pages updated: hazop/study-info.md (added P&ID Readiness Status section + updated Prerequisites), index.md (added source, updated HAZOP status banner)
Key findings:
- Table A6.2-3 is a 13-item P&ID quality checklist (companion to Table A6.2-2 PSI checklist) — must be completed by HAZOP Coordinator before any node analysis begins
- Items 1–10 are CRITICAL (all must be YES or resolved by hand markup); Items 11–13 are desirable
- CDN P&ID pre-assessment: 8 of 10 critical items = ✅ YES; 2 partial: Item 4 (piping class designation to spot-check) and Item 7 (PSV set pressures for V-2301/V-2302 TBC)
- Desirable items 11–13 all ✅ YES (legend, notes, PFD consistency confirmed during ingest)
- HAZOP Coordinator formal sign-off on Table A6.2-3 is a prerequisite that cannot be completed by the LLM — engineer action required
- Appendix 6.2 phase matrix extracted: P&IDs are Essential for Execute/Operation phases; Previous HAZOP reports are Essential for Operation phase but governed by Anti-Bias Rule
- File moved from input/ to raw/standards/
Outstanding: PSV set pressures V-2301/V-2302; Coordinator sign-off; expert P&ID markup with node boundaries

## [2026-06-13] output | 2026-06-13_plant-wide_SDS-generation-prompt_claude-cowork.md

Type: working document / Claude Cowork session prompt
Destination: output/working/
Source wiki pages: wiki/sources/Table-A6.2-2-PSI-readiness-checklist, wiki/units/cdn, wiki/units/oxidation, wiki/units/alkylation, wiki/units/distillation
Contains: 15-chemical SDS generation task brief; GHS 16-section template; Python PDF generation code; execution order; QA checklist
Note: Refrigerant confirmed as 80 wt% Water + 20 wt% Ethylene Glycol (CAS 107-21-1) by operator 2026-06-13. Equipment page E-2301 updated. Diamine identity still TBC — placeholder in prompt.

## [2026-06-13] ingest | Table A6.2-2 PSI readiness checklist (Final R1).xlsx

File: raw/standards/Table A6.2-2 PSI readiness checklist (Final R1).xlsx
Source: PTT GC formal PSI Readiness Checklist — Table A6.2-2 per SG-(Q-MP)-014 R3 §6.2
Revision: Final R1
Format: XLSX with 2 sheets
Sorted from: input/ → raw/standards/ (script = UNCLASSIFIED; manual override — clearly a standards/HAZOP form)

Pages created:
- wiki/sources/Table-A6.2-2-PSI-readiness-checklist.md

Pages updated:
- wiki/hazop/study-info.md (PSI Readiness Status section rebuilt using 8 formal checklist categories; Governing Documents table updated to include checklist)
- wiki/sources/SG-Q-MP-014.md (Key Pages Created section: noted standalone checklist now available)
- wiki/index.md (status banner updated; source count 58→59; HAZOP Study table; HAZOP prerequisites; Gaps updated; Sources table)

Key findings:
- 8 PSI readiness categories (all High criticality except Past Incidents = Medium): Chemical/Reaction hazard, Process Flow, Process Description/Design Basis, Equipment information, Operating Procedures, Safety Systems & Safeguards, Relief & Flare Design, Past Incidents
- Appendix 6.2 phase matrix: for Operation phase (this plant), 20 of 21 document types are Essential (E)
- CDN HAZOP readiness formally assessed at ~60% vs Table A6.2-2: Categories 2, 3, 5 complete; Categories 1, 6, 7 partial; Categories 4, 8 not available
- Anti-Bias Rule note added to checklist: "Previous HAZID/HAZOP reports" listed as Essential in Appendix 6.2 for Operation phase — CONFIRMED that Anti-Bias Rule supersedes this during active node analysis

PSI Readiness blockers outstanding:
1. ❌ Equipment data sheets (Category 4 — High) — ALL major CDN equipment
2. ⚠️ GHS-compliant SDS (Category 1 — High) — CHP, H₂SO₄, Phenol, Diamine
3. ⚠️ Alarm/trip setpoints (Category 6 — High) — PSV set P for V-2301/V-2302; calorimeter ΔT trips
4. ⚠️ Relief & flare design data (Category 7 — High) — PSV sizing basis

## [2026-06-13] ingest | SG-(Q-MP)-014_R3.pdf — PTT GC HAZOP Guidance (61 pages)

File: raw/standards/SG-(Q-MP)-014_R3.pdf
Source: PTT Global Chemical Public Company Limited, GC Management System and Process Safety (Q-MP)
Document Rev: 3, dated 26/05/2026, 61 pages
Created by: Mr. Pongpasin Tanaruangarmorn (Senior Safety Engineer)
Approved by: Mr. Warakorn Decha (Vice President)
Rev 3 change: Added PSI Readiness detail (Table A6.2-2 and A6.2-3)

Pages created:
- wiki/sources/SG-Q-MP-014.md
- wiki/hazop/methodology.md ← guideword table (14 parameters), 9-step method, Tables 6.3/6.4/6.5/6.6

Pages updated:
- wiki/hazop/study-info.md (status banner → SETUP COMPLETE; Governing Documents table ✅; Methodology Notes updated; Prerequisites list updated)
- wiki/index.md (status banner updated; HAZOP Study table + methodology.md row; HAZOP prerequisites ✅; Gaps updated; Sources table updated; source count 57→58, wiki pages 92+→95+)

Key findings:
- 9-step HAZOP methodology (§5.3.3): Node selection → Deviations → Causes → Consequences → Initial Risk → Safeguards → Mitigated Risk → Recommendations → Worksheet references
- Guideword set (Table 6.1): 14 parameters — Flow, Pressure, Temperature, Level, Reaction, Mixing, Phase, Viscosity, Composition, Erosion/Corrosion, Service Failures, Sequence, Incidents, Human Factor
- Full record approach: ALL deviations must be documented on every node; "N/A" with reason if no credible cause
- Acceptable risk = Low or Very Low only; Mitigated risk ≥ Medium → must generate recommendation
- Severity NEVER changes between initial and mitigated assessment (Severity fixed; only Likelihood changes)
- Table 6.3: Likelihood guidance — BPCS loop = L4, pump failure = L4, HX tube leak = L3, routine human error = L5
- Table 6.4 (Active IPLs): BPCS independent = 1 level; SIF SIL1 = 1 level; SIF SIL2 = 2 levels; SIF SIL3 = 3 levels; PRV sized = 2 levels; Alarm+operator = 1 level
- Table 6.5 (Passive IPLs): Dike = 2 levels; Overflow line (no impediment) = 3 levels; Rupture disk = 2 levels
- Table 6.6 (Non-IPLs): Training, procedures, communications, signs, fire protection → zero credit
- PSI readiness checklist (Table A6.2-2): 20 essential documents for Operation-phase HAZOP
- P&ID readiness checklist (Table A6.2-3): 10-item check — latest revision, scope, tags, lines, instrumentation, interlocks, safety devices, tie-ins, isolation devices, continuation symbols
- HAZOP team: Leader ≥8 yrs O&G, independent from EPC/VP Operation; Scribe = dedicated (NOT team member); minimum: Process Engineer + Operations Supervisor
- Safeguard documentation: prevention first, then mitigation; active fire protection NOT a safeguard
- Worksheet references: NEVER "See above" — copy content or use specific row numbers

HAZOP Setup Status after this ingest:
- ✅ Procedure (P-(Q-MP)-OEMS-005 R4) — ingested
- ✅ Risk Matrix (W-(Q-MP)-002 R2) — ingested
- ✅ HAZOP Guidance (SG-(Q-MP)-014 R3) — ingested ← ALL STANDARDS COMPLETE
- ❌ Expert P&ID node boundary markup — **SOLE REMAINING BLOCKER** for node analysis

---

## [2026-06-13] ingest | W-(Q-MP)-002_R2.pdf — PTT GC Operational Risk Assessment Matrix

File: raw/standards/W-(Q-MP)-002_R2.pdf
Source: PTT Global Chemical Public Company Limited, GC Management System and Process Safety (Q-MP)
Document Rev: 2, dated 10/09/2025, 55 pages
Created by: Mr. Pattara Tepnu (Senior Safety Engineer)
Approved by: Mr. Warakorn Decha (Vice President)

Governing section for HAZOP: §6.2.1.3.1 — RAM for Process Hazard Analysis (PHA)

Pages created:
- wiki/sources/W-Q-MP-002.md
- wiki/hazop/risk-matrix.md ← **CRITICAL DELIVERABLE — governs all risk rankings**

Pages updated:
- wiki/index.md (Risk Matrix status ❌ → ✅; HAZOP prerequisites updated; sources table updated)

Key findings:
- 5×5 PHA RAM: Likelihood (1=Improbable to 5=Frequent) × Severity (1-5 per PEES)
- Likelihood basis is frequency-relative: Improbable = unlikely in Industry; Frequent = >1/yr at Location
- Severity: People (no injury → multiple fatalities), Environment (slight → massive), Economic (plant-category-specific THB thresholds), Social (local to international media)
- Risk levels: Very Low / Low / Medium / High / Extreme
- Action thresholds: Extreme/High = immediate action; Medium = risk reduction plan required; Low = review control plan
- Two-stage assessment per §6.5.2: Severity FIXED; Likelihood changes between initial (no safeguards) and mitigated (with safeguards)
- Thai DIW compliance: 4×4 sub-matrix applies (no Extreme level, Likelihood 1-4 only)
- PTT Phenol economic threshold category (Upstream vs Downstream): confirm with HAZOP team — PH-P1/PH-P2 codes appear in Downstream list

HAZOP Setup Status after this ingest:
- ✅ Procedure (P-(Q-MP)-OEMS-005) — ingested
- ✅ Risk Matrix (W-(Q-MP)-002 R2) — ingested ← UNBLOCKED
- ❌ Expert P&ID node boundary markup — awaiting engineer
- ❌ SG-(Q-MP)-014 (HAZOP Guidance, guideword set) — not yet ingested

## [2026-06-13] sort | input/P-(Q-MP)-OEMS-005_R4.pdf → raw/standards/

File: P-(Q-MP)-OEMS-005_R4.pdf
Classification: Company HAZOP procedure standard → raw/standards/
Rationale: Document is PTT GC corporate HAZOP methodology, contains roles, workflow, KPIs, definitions. Contains severity×likelihood references but not the actual risk matrix (separate doc W-(Q-MP)-002).

## [2026-06-13] ingest | P-(Q-MP)-OEMS-005_R4.pdf — GC HAZOP Procedure Rev 4

File: raw/standards/P-(Q-MP)-OEMS-005_R4.pdf
Source: PTT Global Chemical Public Company Limited, GC Management System and Process Safety (Q-MP)
Document Rev: 4, dated 26/05/2026, 24 pages

Pages created:
- wiki/sources/P-Q-MP-OEMS-005.md
- wiki/hazop/study-info.md
- wiki/hazop/action-register.md

Pages updated:
- wiki/index.md (added HAZOP section, updated status banner, updated gaps list, added source entry)

Key findings:
- HAZOP scope: triggered by MoC; CDN study is standalone application of this methodology
- Risk ranking is TWO-STAGE: (1) Initial risk without safeguards — Severity fixed; (2) Mitigated risk — Likelihood only re-evaluated with safeguards
- Severity NEVER changes between initial and mitigated risk — important rule for all HAZOP worksheets
- HAZOP Leader must have min 8 years' experience AND must be independent (from project org, EPC contractor, and VP Operation line of management)
- Required PSI documented in §5.2 — 11 document types (see study-info.md PSI readiness table)
- HAZOP methodology reference is SG-(Q-MP)-014 (guideword set, PSI checklist) — NOT ingested yet
- Risk matrix is W-(Q-MP)-002 — NOT in raw/standards/ yet

Critical gaps flagged:
- W-(Q-MP)-002 (Risk Assessment Matrix) — REQUIRED before HAZOP-SETUP can complete
- SG-(Q-MP)-014 (HAZOP Guidance) — contains guideword set
- Expert node boundary markup on CDN P&IDs — engineer action required

## [2026-06-13] ingest | OM-Phenol Unit UOP-2015.pdf — UOP General Operating Manual (388 pages, CDN focus)

File sorted to: raw/operating_manuals/ (moved from input/)
Source: UOP (Honeywell), Document No. 147086 Rev 8, Confidential

Sections extracted (CDN-relevant):
- §II Process Description: CDN chemistry and design basis
- §III.B–D CDN Process Parameters: concentration, decomposition, neutralization operating windows
- §VII.2–4 Normal Operations: concentration, decomposition, neutralization
- §IX Troubleshooting (CDN portion): poor AMS yield, high acidity, dehydrator plugging
- §X.B–D Normal Shutdown: concentration, decomposition, neutralization
- §XI.D–I Emergency Procedures: full CDN emergency response + service system failures + shutdown logic Table XI-1

Pages created:
- wiki/sources/om-phenol-uop-2015.md
- wiki/parameters/cdn-operating-windows.md
- wiki/procedures/normal-operations-cdn.md
- wiki/procedures/normal-shutdown-cdn.md
- wiki/procedures/emergency-cdn.md
- wiki/troubleshooting/cdn-poor-ams-yield.md
- wiki/troubleshooting/cdn-high-acidity-flash-column.md
- wiki/troubleshooting/cdn-dehydrator-plugging.md

Pages updated:
- wiki/units/cdn.md (added Licensor Design Basis section, GOM source, procedures/troubleshooting index)
- wiki/index.md (added Procedures, Parameters, Troubleshooting sections; updated Sources; gaps updated)

Key findings:
- Decomposer TSLL (ESD) = 57°C — lower than 60°C normal target
- H₂SO₄ <20 wt ppm = extremely dangerous condition (uncontrolled decomposition risk on acid re-addition)
- UOP: never operate decomposer without at least one calorimeter online
- "Ready for Feed In" requires 300 wt ppm H₂SO₄ (lab confirmed) + 70°C + zero water injection + feed line flushed
- Table XI-1: 15 interlock actions documented with cause-effect matrix
- Calorimeter 1st stage ΔT ≈ 7.2°C per wt% CHP — key monitoring conversion factor
- DCP target 300–700 wt ppm crude product (licensees achieve 700–900 while meeting o-cresol spec)
- AMS yield ≥80 mole% achievable under licensor design conditions

Gaps flagged:
- TSHH (high ESD) setpoint for decomposer: not stated in GOM text
- Calorimeter alarm and trip setpoints: plant-specific; need instrument data sheets
- PSV set pressures for V-2301/V-2302: still TBC from P&ID
- Preflash column operating pressure: not extracted from GOM

## [2026-06-07] ingest | CDN P&ID Drawings 0020, 0020A, 0021, 0022, 0023 — FINAL CDN BATCH (CDN P&ID COMPLETE)

Files sorted to: raw/pid/ (from input/)
Pages created: equipment/D-2307.md, equipment/X-2321.md, equipment/P-2320.md, equipment/P-2304A.md
Pages updated: equipment/D-2306.md (full Drawing 0020 data), sources/pid-cdn.md (CDN COMPLETE), index.md (status CDN P&ID COMPLETE, 4 new equipment rows)

Key findings:

**Drawing 0020 — D-2306 (Acid Aromatics KO Drum) full P&ID:**
- D-2306 design data confirmed: 3400×5200mm; FV/3.5 kg/cm²g; 250°C/325°C design (dual temp limits); 0.01/38°C operating; NI insulation. UOP STD DWG 963766-120-20-A1.
- Instruments: LT-2002/LI-2002 level, PI-2001 pressure, SN-2311 (Type B-AC) acid aromatics sample.
- Critical maintenance note: "GAUGE GLASS MUST BE READABLE FROM VALVE" — safety-critical visibility requirement.
- Steam utility connection (2"-S12 BLANKOFF WHEN NOT IN USE) — purge/warmup capability.
- Distributor + Baffle internals.
- HLL 1830mm confirmed.

**Drawing 0020A — Acid Aromatics Sump System:**
- D-2307 (Acid Aromatics Sump): 2200×6600mm; FV/3.5/325°C; ATM/38°C; HLL 1740mm/LLL 1030mm. Instruments: Radar LI-3009, LT-2005, LAL-2005, LS-2005 (LOW LEVEL STOP), PCV-2001 (0.84 kg/cm²g N₂), PSV-2001N/B, WT-23-2001 (weigh transmitter). Sloped bottom + distributor. BLANKOFF flanges for future connections.
- X-2321 (Acid Aromatic Sump Pit): 9600×3900×6150mm underground LINED PIT BY OTHERS. ATM/50°C design. Note 5: depth from HLP to D-2307 top = 2120mm.
- P-2320 (Sump Pit Pump): 5 m³/hr; 0.69 kg/cm²g DP; 7.5 kW; SG 0.99; submerged vendor-supplied pump; discharge → D-2307 or OWS 91-0058.
- P-2304A (Acid Aromatics Sump Pumps): 22.7 m³/hr; 3.53 kg/cm²g DP; 22.4 kW; SG 0.826; Type D motor; Common Spare P-13045; FIC-2001 + WT-23-2001 on discharge; XC-2304 common alarm; LS-2005 LOW LEVEL STOP (from D-2307). Suction from D-2307 → Sodium Phenate Tank (Phenol Recovery).
- **CRITICAL NOTE 6 (confirmed on Drawing 0020A):** "NO AIR ALLOWED IN THE CLOSED DRAIN SYSTEM FROM PUMPS, INSTRUMENTS, PIPELINES, EXCHANGERS AND THE RELATED EQUIPMENTS." This applies to entire CDN acid aromatics closed drain system.

**Drawing 0021 — Acid Aromatics Closed Drain Header:**
- All CDN acid aromatics drains consolidated to common 6"-AD header → D-2307.
- Drain connections from: P-2302A/B, X-2309A/B, P-2303A/B, E-2307A/B, E-2308A/B, E-2309, P-2301A/B, P-2305A–F.
- Drain valves per STD DWG 8-137. N₂ blanket throughout header.
- Confirmed: all acid aromatics drains go to D-2307 → P-2304A → Sodium Phenate Tank (Phenol Recovery).

**Drawing 0022 — Pressure Relief Header:**
- PSV source listing confirmed: PSV-1403A/B/C (X-2312), PSV-1401A/B (E-2308A/B), PSV-1405A/B, PSV-1801A/B (X-2309A), PSV-1802A/B (X-2309B). All at 9.5 kg/cm²g (adjusted for static head).
- Header → 6"-F-23-022001 → D-2306 (Acid Aromatics KO Drum).
- N₂ purge: continuous via RO-2201 (1.5mm) + SRY-L2301 purge skid — prevents air ingress into CHP/acid service relief header.

**Drawing 0023 — CHP Closed Drain Header:**
- SEPARATE drain system from Acid Aromatics system.
- All CHP-service drains (>5 wt% CHP) routed to CHD header → D-2206 (CHP Sump at Oxidation Section).
- Critical separation: CHP drains must NOT enter Acid Aromatics header (H₂SO₄ + CHP reaction hazard).
- N₂ blanket per CHP N₂ Header (53-0051). Drain valves per STD DWG 8-141 (CHP closed drain standard).

**CDN Complete Drain System Architecture Summary (now fully documented):**
```
CHP Service drains  → CHD Header → D-2206 (OXI Section CHP Sump)
Acid Aromatics drains → AD Header → D-2307 (Acid Aromatics Sump)
    → P-2304A → Sodium Phenate Tank (Phenol Recovery)
PSV discharges → Relief Header → D-2306 (KO Drum)
    → Liquid → D-2307 → P-2304A
    → Vapor → PRU Relief Header
```

✅ **CDN P&ID INGESTION COMPLETE — All 45 drawings (0002–0023) ingested.** All CDN equipment pages, instrument pages, and drain system architecture are now fully documented in the wiki.

Outstanding open conflict: P-2307A/B motor control Type B vs Type D — still unresolved (requires field verification).
Next priority: Oxidation Section PFDs (14780-8120-20-22-XXXX) and Operating Manual.

## [2026-06-07] ingest | CDN P&ID Drawings 0018, 0019 — Calorimeters + Neutralization

Files sorted to: raw/pid/ (from input/)
Pages created: equipment/D-2312.md, equipment/P-2306AB.md, equipment/X-2310AB.md
Pages updated: equipment/X-2308.md (tag corrected to X-2309A/B + full Drawing 0018 data), sources/pid-cdn.md, index.md (conflict resolved)

Key findings:
- **TAG CONFLICT RESOLVED — X-2309A/B** (Drawing 0018 As-Built confirms). PFD tag X-2308A/B was an error. P&ID Equipment List (Drawing 0000B) was correct all along. File equipment/X-2308.md updated with correct tag; all references updated.
- **Calorimeter physical data confirmed**: 4" SCH 40 × 470mm — very small vessels. Design 10.5 kg/cm²g / 250°C; operating 2.1 kg/cm²g / 79°C. H(40) insulation. UOP STD DWG 963766-301-99-A1. Located close to P-2302 suction/discharge piping (Note 2). Symmetrical piping (Note 3). Residence time restricted (Note 1, Spec 963766-840).
- **Calorimeter instruments fully documented**: TDXSHH-1801/1803 (SIS total ΔT HH, SIL 1/A → UC-2302); TDXAHH-1802/1804 (DCS CRIT); FXT-1803/1804 (Coriolis); FIC-1801/1802 (flow controllers); FXALL-1803/1804 (SIS feed flow LL → UC-2302); PSV-1801A/B and 1802A/B at 9.5 kg/cm²g (static head adjusted); INT-23-1801/1802 displacement level instruments; SG-018003/004 sight glasses. Vents to Acid Aromatics KO Drum (23-0022); drains to Closed Drain Header (23-0021).
- **Neutralizing agent confirmed as DIAMINE** (not NaOH). D-2312 (Diamine Injection Tank): 1300×1300mm, 0.01/40°C operating, PCV-1909 vent at 30 mmH₂O. Diamine supplied from tote containers.
- **P-2306A/B (Diamine Injection Pumps)**: 6.65 liter/hr, SG 0.856, 4.78 kg/cm²g DP, 0.2 kW, Type B. Ratio-controlled to crude product flow via FT-1903 Coriolis meter. XC-2306 common alarm.
- **X-2310A/B (Direct Neutralization Static Mixers)**: 6" SCH 40 × 1420mm; design 21.5 kg/cm²g / 250°C; operating 4.4 kg/cm²g / 43°C. Injection nozzle Detail B: 1" SCH 160 304L SS, ½" hole downstream at centreline. Key-interlocked inlet valves. AT-1901 acid analyzer (by vendor) on neutralized product for ratio control feedback.
- **Crude product flow confirmed**: E-2309 (Crude Product Cooler) → X-2310A/B (neutralization) → Sprung Phenol blended in from Phenol Recovery → Crude Product to Fractionation Feed Tanks. CDN section end-point confirmed.
- **D-2307 and D-2306 (Acid Aromatics Sump/KO Drum)** still pending — Drawing 0020/0020A.
- **Remaining open conflict**: P-2307A/B motor control Type B vs Type D (Drawing 0008B vs 0001G) — unresolved.

Outstanding gaps: CDN P&ID sheets 0020–0023 (4 sheets); Operating Manual; Equipment Data Sheets

## [2026-06-07] ingest | CDN P&ID Drawings 0015, 0016, 0017 — Acid Injection + Decomposer Circulation

Files sorted to: raw/pid/ (from input/)
Pages created: equipment/D-2310.md, equipment/D-2311.md, equipment/X-2320.md, equipment/P-2305ABCDEF.md
Pages updated: equipment/E-2307.md (major correction), equipment/P-2302.md (mechanical data), equipment/X-2308.md (calorimeter connections), sources/pid-cdn.md, index.md

Key findings:
- **E-2307 is TWO parallel shells (E-2307A + E-2307B)** — each 1600×6096mm / 801.7 m²; total HT surface 1603.4 m². Previous wiki recorded E-2307 as a single unit. CORRECTION applied across all pages.
- **P-2302A/B mechanical data confirmed**: 3020 m³/hr design capacity, 3.41 kg/cm²g DP, 250 kW each, SG 0.996, Type D motor. PFD circulation (1,887 tonne/hr ≈ 1,895 m³/hr) = ~63% of design capacity — pumps run well below rated flow in normal operation.
- **Acid injection system fully documented** (Drawings 0015/0016): D-2310 injection tank, D-2311 refill tank, X-2320 neutralization system. All 6 pumps P-2305A–F: 0.95 liter/hr each at SG 1.715, 0.2 kW, Type B motor. FXSLL → UC-2302 ESD trigger confirmed.
- **Acid ratio control architecture**: XC-1604 ratio controller with multiplier XY-1604A. Split-range: P-2305C/D (lead — increase stroke first), P-2305E/F (lag — increase last). Acid discharge goes to Calorimeters on Drawing 0018 (not directly to Decomposer).
- **Calorimeter inlet source clarified**: Sidestream drawn from Decomposer RECIRCULATION (E-2307 area, Drawing 0017) — NOT from D-2303 (Decomposer Feed Flush Drum) as previously assumed. Calorimeter also receives acid injection from P-2305 pumps. Return lines confirmed on Drawing 0017.
- **TIC-1302 split-range temperature control on E-2307A/B**: Two CW control valves — one closes on high temperature signal, one closes on low temperature signal (anti-overcooling protection).
- **PDXSLL (SIS low-low DP)** confirmed on E-2307 cooling water side → UC-2302 ESD. Loss of CW flow to Decomposer Cooler = immediate shutdown trigger. Independent from PDXSHH-1701A/B/C (process-side high DP, from C&E table).
- **AT-1701 sulfuric acid analyzer** on Decomposer recirculation line — cross-check for acid injection rate, independent of calorimeter signal.
- **X-2320 acid neutralization system** (3000×900×900mm, ATM/70°C) in diked containment area — receives all H₂SO₄ drains from acid injection system; amine neutralizer from Drawing 0019.
- **Calorimeter drawing 0018 (next priority)** — resolves X-2308 vs X-2309 tag conflict; will fully document calorimeter internal layout and acid injection tap points.

Outstanding gaps: CDN P&ID sheets 0018–0023 (6 sheets); Operating Manual; Equipment Data Sheets; calorimeter tag conflict unresolved

---

## [2026-06-07] ingest | CDN P&ID Drawings 0012A/0013/0014/0014A — Decomposer Feed Flush Drum, Decomposer Drum, Dehydrators, Crude Product Cooler

Files sorted and ingested from: raw/pid/
Pages created: equipment/D-2303.md, equipment/P-2303AB.md, equipment/E-2308AB.md, equipment/E-2309.md
Pages updated: equipment/D-2304.md (major update — P&ID data added), instruments/sis-cdn.md, units/cdn.md, sources/pid-cdn.md, index.md

Key findings:
- **D-2303 startup permissive confirmed (Note 5, Drawing 0012A)**: "WHEN THE LEVEL IN THE DECOMPOSER FEED FLUSH DRUM IS HIGHER THAN LSL (85% OF SPAN), START-UP WILL BE ENABLE." LXSLL-1201 physical location confirmed on Drawing 0012A. Label "FLUSH RESERVOIR FULL (START-UP ENABLE)" on P&ID.
- **UXV-1207 is a DISSIMILAR CHECK VALVE (Note 4, Drawing 0012A)**: UXV-1207 at D-2303 is a dissimilar check valve — different from UXV-1206 to provide SIS hardware diversity at this CHP isolation point. Also, UXV-1402 at E-2309 is another dissimilar check valve (Note 4, Drawing 0014A).
- **PXSLL-1201 process water pressure LL physical location confirmed**: On Drawing 0012A (D-2303 area). Previously only known from C&E table. Confirms process water supply to D-2303 is a UC-2302 ESD cause — loss of process water = cannot control CHP decomposition chemistry.
- **D-2304 physical vessel data from Drawing 0013**: 1900×4800mm, FV/11 kg/cm²g/250°C design, 0.7/60°C operating. Internal: two Distributors + Baffle + Grating + Alloy 20 Detail "C" acid injection distributor (3" SCH 160, nozzle ≥1000mm from any elbow).
- **X-2311 = rupture disc on D-2304 at 12.16 kg/cm²g**: "PIPE X-2311" is the safety head assembly (rupture disc) on the Decomposer Drum, set at 12.16 kg/cm²g (above 11 kg/cm²g design). Full-bore, instantaneous relief — no spring-loaded PRV.
- **D-2304 safety elevation requirement**: "LOCATE 3000 ABOVE ANY EQUIPMENT ON PLATFORM WITHIN 15 METERS RADIUS" — Decomposer must be elevated 3000mm above all surrounding equipment within 15m. Platform layout constraint with direct safety implication.
- **Residence time restricted piping (Spec 963766-840)**: Note 1 on Drawing 0013 — all piping volumes in D-2304 area and Dehydrator loop (X-2312, Drawing 0014A) are constrained by UOP Spec 963766-840. X-2312 volume = 0.48 m³ total; middle loop = 50% = 0.24 m³ (Note 3, Drawing 0014A).
- **TXSHH-1301A/B + TXSLL-1301A/B + LXSHH-1302/1303 confirmed on Drawing 0013**: All six SIS instruments at D-2304 (three 1oo2 pairs, SIL 2) physically confirmed on the Decomposer Drum P&ID. SIS valve list updated: UXV-1301A/B (two valves) + UXV-1302 confirmed.
- **TXSHH-1402 (Dehydrator temp HH) confirmed on Drawing 0014**: Shown as "TXAHH-1402 CRIT" on P&ID (DCS label convention). The safety-dedicated hardware carries S prefix (TXSHH-1402). Physical location confirmed = E-2308A/B area. UXV-1401 also confirmed at dehydrators.

## [2026-06-07] ingest | CDN P&ID Drawings 0010/0010A/0011/0012 — Vacuum Equipment, Cumene Flush Drum, and CHP Feed Line

Files sorted and ingested from: input/ → raw/pid/
Pages created: equipment/E-2310.md, equipment/X-2301.md, equipment/P-2316AB.md, equipment/P-2317AB.md, equipment/D-2302.md
Pages updated: instruments/sis-cdn.md, units/cdn.md, sources/pid-cdn.md, index.md

Key findings:
- **UV-1205 CORRECTION — it is UXV-1205, a UC-2302 SIS valve**: Drawing 0012 confirms UXV-1205 is an SIS valve output of UC-2302, NOT a manual valve as previously described. On Decomposer ESD, UXV-1205 closes — simultaneously cutting CHP feed AND sealing the CHP Nitrogen Header circuit from the downstream (regular N₂) zone. This is the physical enforcement of the N₂ boundary during emergencies. All wiki pages corrected.
- **Triple redundant CHP cutoff confirmed (Drawing 0012, Note 6)**: UXV-1201A + UXV-1201B + UXV-1201C are in the CHP feed line to the Decomposer. Note 6: "UXV-23-1201C is a redundancy valve of UXV-23-1201A — dead zone between inlet of UXV-23-1201C and connection point to be minimized."
- **FXSLL-1204 + FXSLL-1205 on 6"-CHP-23-012001**: Thermal mass flow switches LL confirmed as SIS initiators (UC-2302, 2oo3 voting, SIL 2 from C&E table) physically located on the main CHP feed line on Drawing 0012. Technology: thermal mass flow measurement.
- **V-2302 level control link to CHP flow confirmed (Drawing 0012)**: LY-0801C signal from V-2302 (Drawing 0008) arrives at FY-1202A on Drawing 0012, feeds override to FIC-1202 (CHP flow controller). CHP flow measurement also goes TO TOTAL ACID RATIO CONTROLLER (P&ID 0016).
- **D-2302 is a FLUSH drum, NOT in CHP flow path**: D-2302 (1500×4500mm, 0.7 kg/cm²g/38°C) stores fresh cumene for line flushing procedures. Main CHP path: P-2301A/B → 6"-CHP → UXV-1201A/B/C → Decomposer. D-2302 supplies 4"-CUL flush to P&ID 0012 and 1¾"-CUL to D-2303 (Decomposer Feed Flush Drum). No SIS directly on D-2302.
- **X-2301 two-stage vacuum system confirmed**: Stage 1: steam jet ejectors J-2301/J-2302A/B (10→79.7 mmHgA, 238°C discharge); Stage 2: liquid ring pumps P-2316A/B (79.7→804 mmHgA, 55 kW, Ex nA). Non-condensibles to Charcoal Adsorber Cooldown Section (NOT direct vent). Sealant water from OXI Section.
- **UXV-1001 and P-2316A/B/P-2317A/B — DCS-only restart**: Note 6 on Dwg 0010: HXS-23-1001 (DCS-only reset for UXV-1001). Note 7 on Dwg 0010A: HXS-23-2316 (DCS-only restart for ALL four vacuum pumps). Third DCS-only reset in CDN (after UXV-0803 on E-2301).
- **AI-1001 O2 analyzer on D-2316**: Oxygen analyzer on D-2316 separator top nozzle (vendor-supplied per Drawing 0010 Note 4). Monitors for explosive atmosphere in vacuum vapor stream. Tapping point confirmed at separator top nozzle (Note 3).
- **Piping layout constraint**: HORIZONTAL RUNS NOT ALLOWED on vapor condensate lines from E-2310 (45° min from horizontal). Applies to all vapor/condensate lines in vacuum system.
- **Note 1 on Drawing 0012: >5 wt% CHP piping requires special insulation** per Project Specification 907 — all 6"-CHP lines on this drawing affected.

## [2026-06-06] ingest | CDN P&ID Drawings 0008B and 0009 — Overhead Pumps P-2307A/B and Flash Column Bottoms Pumps P-2301A/B

Files sorted and ingested from: input/ → raw/pid/
Pages created: equipment/P-2307AB.md, equipment/P-2301AB.md
Pages updated: sources/pid-cdn.md, units/cdn.md, index.md

Key findings:
- **P-2307A/B motor control CONFLICT — Type B per Drawing 0008B**: Note 2 on Drawing 0008B explicitly states "TYPE B" motor control (DCS-initiated LOW FLOW START only — not hardwired SIS auto-start). This conflicts with any prior table entry showing Type D (auto-start) from Drawing 0001G. The physical P&ID for the pump itself is authoritative. P-2307A/B do NOT have hardwired SIS auto-start — operator must initiate standby start when FAL-0802 alarms. Open conflict documented in index.md.
- **P-2301A/B on Reliable Power Supply**: Explicitly stated on Drawing 0009 — P-2301A/B are on emergency power bus. Only Concentration sub-section pump with this designation. If plant power fails, P-2301A/B continue running. Loss of these pumps with no standby → V-2302 level rise → LXSHH-0802 UC-2301 ESD within minutes.
- **TXSHH-0901A/B physical location confirmed on P&ID 0009**: The UC-2301 Cause 11 (1oo2) Flash Column Bottoms Pump Suction Temperature SIS transmitters are at the P-2301A/B suction area on Drawing 0009 — not on the Flash Column P&ID 0008.
- **Two CHP concentration analyzers now documented** — AI-0801A/B (on P-2307A/B discharge, monitors CHP in recycle cumene — safety gate for OXI section) and AI-0901A/B (on P-2301A/B discharge, measures actual CHP% to Decomposer). Both are vendor-packaged inline analyzers measuring concentration and density.
- **SN-2303 location confirmed on Drawing 0009**: Type A-CH (CHP sampling procedure required). On the P-2301A/B discharge 6"-CHP-23-009002 line — highest hazard sample point in CDN.
- **MIN DISTANCE TO UV-1204 notation on P-2301A/B discharge**: Minimum pipe length required before UV-1204 (on P&ID 0012A, Decomposer Feed Flush Drum area). Likely a residence-time or flow-settling requirement for concentrated CHP before entering Decomposer feed zone.
- **UXV-0804/0805 confirmed on P-2307A/B P&ID (0008B)**: UC-2302 (Decomposition ESD) output valves UXV-0804 and UXV-0805 are located on the Overhead Pump P&ID. Close on Decomposer ESD — isolates recycle cumene return to OXI section.
- **P-2307A/B 90 kW motors**: Largest motors in Concentration sub-section by far (P-2308 = 3 kW, P-2309 = 2.2 kW). Soft starters SRT-P2307A/B required for these large motors.

## [2026-06-06] ingest | CDN P&ID Drawing 0008A — Preflash and Flash Columns Condenser (E-2301)

Files sorted and ingested from: input/ → raw/pid/
Pages created: equipment/E-2301.md
Pages updated: sources/pid-cdn.md, index.md

Key findings:
- **E-2301 is the largest Concentration duty item**: 16.52 MM kcal/h — more than E-2303 (6.10) + E-2304 (4.15) combined.
- **Refrigerated cooling (RCS) required**: Map Ta Phut ambient ~35-40°C; column overhead vapors at 28-52°C. Standard cooling tower water (32-35°C) cannot condense these vapors. RCS from Utility Unit 61 (28"-RCS-61-054014). Loss of RCS fails BOTH V-2301 and V-2302 simultaneously — the single most critical utility for the Concentration sub-section.
- **CRITICAL: Shared cooling circuit with E-2307 (Decomposer Cooler)**: RCR return from E-2301 routes to P&ID 0017 (E-2307 area). E-2301 and E-2307 share the same refrigerated cooling return circuit. A fault in this shared circuit can cascade into simultaneous UC-2301 (column pressure rise) and UC-2302 (Decomposer Cooler DP, PDXSHH-1701) trips. This inter-section dependency is significant for HAZOP and emergency response planning.
- **UXV-0803 DCS-only reset confirmed**: Note 2 on drawing: "RESET HAND SWITCH (ONLY DCS S/W) FOR UXV-23-0803: HXS-23-0803". Unlike most SIS valves, UXV-0803 at the condenser cannot be reset from a field pushbutton — operator must be at the DCS workstation.
- **125m equivalent pipe length limit**: Drawing note constrains installation of E-2310 (Flash Column Overhead Vapor Chiller) to within 125m equivalent pipe length from E-2301. Pressure drop constraint — vacuum vapor lines.
- **Three large vapor inlets**: Two 72" lines from V-2301 + one 56" line from V-2302. Piping must be SYMMETRICAL. Expansion joints EJN-E2301A/B/C on all large lines.
- **CHP Closed Drain Header**: Instrument volume system on E-2301 connects to CHP Closed Drain Header (STD DWG 8-121 and 8-141) — consistent with CHP nitrogen segregation requirement.

## [2026-06-06] ingest | CDN P&ID Drawings 0006/0007/0007A/0008 — Concentration Sub-section Completion

Files sorted and ingested from: input/ → raw/pid/
Pages created: equipment/D-2301.md, equipment/D-2309.md, equipment/P-2309AB.md, equipment/E-2306.md
Pages updated: equipment/E-2304.md, equipment/V-2302.md, sources/pid-cdn.md, index.md

Key findings:
- **D-2301 gravity quench design confirmed**: 2800×9400mm horizontal drum at 0.06 kg/cm²g / 38°C; "5000mm MIN ABOVE QUENCH NOZZLE" elevation requirement — quench is gravity-fed to Flash Column. CHP N₂ Header blanketing per STD DWG 8-138 Type 1. VHL/NLL/LLL = 2360/2240/2120mm (drum maintained nearly full for instant quench availability).
- **D-2301 serves BOTH columns**: UXV-0601 and quench lines go to both V-2301 and V-2302. HIC-0601 allows manual quench rate override — key operator tool for managing column bottom temperature.
- **E-2304 SIL 2 with TIME DELAY FOR A ONLY**: TXSHH-0701A/0702A pair has time delay (filters spurious trips); TXSHH-0701B/0702B pair is immediate. Both are 1oo2 voted. A-pair = SIL 2. This is the most stringent temperature protection in the Concentration sub-section — reflecting the extremely high CHP concentration at the Flash Column Vaporizer outlet.
- **V-2302 stepped-diameter confirmed**: 3400mm top / 2200mm bottom × 18400mm — 18.4 meters tall. Larger than V-2301 (7.55m) due to deeper vacuum and larger vapor volume fraction.
- **D-2309 vs D-2308 pressure confirmed**: D-2309 at 2.3 kg/cm²g / 135°C (SC3 condensate) vs D-2308 at 0.9 kg/cm²g / 63°C (SC1.5 condensate). Both P-2309A/B and P-2308A/B are Type L motor control with UC-2301 SIS.
- **V-2302 to Decomposer signal path confirmed**: Flash Column bottoms flow → FY-1201B high signal selector → multiplier FY-0012 (P&ID 0012) → Decomposer acid injection rate. This is the primary concentration-to-decomposition control link.
- **V-2302 split-range level control**: LY-0801 c/d manage startup vs normal vs override modes — more complex than V-2301 level control due to higher CHP concentration at bottoms (safety-critical level control).
- **UXV-0802/0803 on V-2302**: UC-2302 (Decomposition ESD) drives these — confirms these two valves are the primary CHP feed cutoff from Concentration to Decomposer when Decomposer ESD triggers.
- **E-2306 surface area**: 662.8 m² for 0.75 MM kcal/h — large area / low duty ratio due to small temperature approach (concentrated CHP at ~60°C, CW at ~30-35°C).
- **SN-2310 confirmed on Drawing 0007**: Phenol-containing stream sampling point (Type B-CH) located on Flash Column Vaporizer P&ID. Skin absorption hazard.

Concentration sub-section P&IDs now fully ingested (0003–0008 + 0002 C&E). Remaining: 0008B (overhead pumps), 0009 (bottoms pumps), 0010/10A (vacuum system), 0011 (condenser), 0012/12A (CHP feed to Decomposer), 0013–0023.

## [2026-06-06] ingest | CDN P&ID Drawings 0003/0004/0005/0005A — Preflash Column Concentration Area

Files ingested from: raw/pid/ (sorted from input/ in previous session)
Pages created: equipment/X-2302AB.md, equipment/E-2302AB.md, equipment/E-2303.md, equipment/D-2308.md, equipment/P-2308AB.md
Pages updated: equipment/V-2301.md (added full P&ID data), sources/pid-cdn.md, index.md

Key findings:
- **V-2301 vacuum pressures confirmed**: 18.5 mmHgA at top (53°C), 19.5 mmHgA at bottom (64°C) — deep vacuum operation; column size 6600×7550 mm; 72" overhead vapor lines required by low-pressure volumetric flow
- **V-2301 feed is two-phase**: Feed enters the column as vapor-liquid mixture after preheating in E-2302A/B. HIGH POINT callout confirms this.
- **E-2302A/B process role clarified**: Feed-effluent heat exchanger — hot OXI recirculating oxidate (shell) heats cold fresh CDN feed (tube). Energy integration between OXI and CDN sections.
- **E-2303 steam heater confirmed feed-forward control**: Steam flow controller uses OXI section flow and temperature as feed-forward signals — reduces V-2301 upsets during OXI section disturbances.
- **E-2303 redundant steam isolation**: UXV-0501 AND UXV-0502 in series — two SIS valves on steam inlet. Both close on any UC-2301 ESD. SIL requirement drives redundancy.
- **P-2308A/B are Type L** (most instrumented motor type) due to UC-2301 SIS connection — auto-start via FY-0502 flow signal. 3 kW motors (small — condensate only).
- **X-2302A/B filter CHP N₂ Header confirmed**: Shell blanketed with 3/8" P nitrogen from CHP Nitrogen Header (not regular N₂) — consistent with UOP segregation requirement upstream of UV-1205.
- **UXV-0302** (X-2302A/B area) is the UC-2301 SIS feed isolation valve for the entire Concentration section. Verified P&ID cross-reference matches UXV list from Drawing 0001.
- **V-2301 PSVs**: Four PSVs (0401A through 0401D) installed — multiple devices for vacuum column with design pressure 3.5 kg/cm²g.
- **Concentration sub-section interconnect confirmed**: X-2302A/B → E-2302A/B → E-2303 → V-2301 feed path fully traced with line numbers. All line designations use L1A1-H (*) spec (H = traced, * = insulated).

Outstanding gaps: CDN process P&ID sheets 0006–0023 (18 sheets); Operating Manual; Equipment Data Sheets; calorimeter tag conflict unresolved

## [2026-06-06] ingest | CDN P&ID Drawing 0002 — Cause and Effect Table, Rev Z1 As-Built

Files sorted to: raw/pid/
Pages created: instruments/cause-effect-cdn.md
Pages updated: instruments/sis-cdn.md, sources/pid-cdn.md, index.md

Key findings:
- **SIS tag format correction**: All SIS initiator tags use TXSHH/FXSLL format (Safety prefix), not TXAHH/FXALL (DCS). Previous entries in sis-cdn.md corrected accordingly.
- **Voting logic confirmed**: UC-2302 Decomposer Feed flow = 2oo3; Decomposer Temp/Level = 1oo2; Acid Injection = 2oo3; Cooler DP = 2oo3. UC-2301 Preflash Feed flow = 2oo3; Steam Heater/Flash Vaporizer temps = 1oo2.
- **4 new UC-2302 initiators** not previously captured from Drawing 0001: PDXSHH-1701A/B/C (Decomposer Cooler DP, SIL 2, 2oo3), FXSLL-1803/1804 (Calorimeter liquid feed flow), LXSLL-1201 (Feed Flush Drum level LL), PXSLL-1201 (Process water pressure LL)
- **Cross-trip confirmed**: UC-2301 (Concentration ESD) → triggers UC-2302 (Decomposer ESD). Reverse NOT true.
- **P-2302 NOT auto-stopped** by most UC-2302 ESD causes — circulation pumps continue running during shutdown to maintain heat removal and dilution. Critical operational point.
- **Calorimeter signals**: Total DT (TDXSHH-1801/1803) rated SIL 1/A; Inlet DT (TDXSHH-1802/1804) rated SIL A. "In service" qualifier prevents false trips when one calorimeter offline.
- **UC-2303 causes confirmed**: LXSHH-1006, PDXSHH-1012, FXSLL-1008, TXSHH-1008, HXS-1001
- **Startup bypasses documented**: HXS-0102 bypasses FXSLL-0401 and LXSHH-0802 for timed interval; HXS-0108/0109 bypasses dehydrator steam valve conditions + low acid flow during heat-up

## [2026-06-06] ingest | CDN P&ID Standard Details Set — 16 drawings (14780-8120-25-23 series), Rev Z1 As-Built

Files sorted to: raw/pid/
Pages created: sources/pid-cdn.md, instruments/sis-cdn.md, instruments/pump-seal-plans.md, instruments/motor-control.md, instruments/sampling-cdn.md, equipment/P-2302.md
Pages updated: equipment/X-2308.md, equipment/D-2304.md, units/cdn.md, index.md

Key findings:
- **SIS architecture confirmed**: UC-2301 (Concentration), UC-2302 (Decomposition), UC-2303 (Vacuum) — three independent SIS logic controllers with complete UXV list and shutdown trigger matrix
- **Calorimeter tag CONFLICT**: PFD shows X-2308A/B; P&ID Equipment List shows X-2309A/B — must verify with field/data sheet
- **7 independent shutdown paths from calorimeters** to UC-2302: TXAHH-1801/1802/1805 + TDXAHH-1803/1804 + potential duplicates
- **P-2302A/B confirmed as HV motors** with full vibration monitoring (VE/VI/TE/TT/TI suite), API Plan 11/53A complex dual seal — most critical equipment
- **6 acid injection pumps** (P-2305A through F) confirmed; none have auto-start; PXALL-1601 (acid pressure LL) is an ESD trigger
- **New pumps identified**: P-2316A/B, P-2317A/B (vacuum system, UC-2303 connected); P-2320A (acid sump pit)
- **CHP Nitrogen Header**: UOP requirement — all N₂ upstream of UV-1205 must use dedicated CHP N₂ header (from OXI section); must not mix with regular N₂
- **SIL verification changes (Rev S3)**: Redundancy valve UXV-1201B added; LSL-23-1201 permissive added; UC-2303 tag corrected from UC-2304
- **Seal plans**: P-2304A uses API Plan 74 (N₂ gas barrier); P-2302A/B most complex (Plan 11/53A with 4 circuits); P-2303A/B unique Plan 2/53A (dead-ended inner)
- **Error corrected in cdn.md**: P-2302A/B was incorrectly listed as "Preflash Steam Heater Condensate Pumps" — corrected to P-2308A/B; P-2309A/B added to concentration equipment table
- **CDN drain routing**: Many CV and pump drains route to D-2206 (Oxidation Section sump) — CDN and OXI share drain system
- **10 sampling points** documented (SN-2301 through SN-2311) with hazard classification; SN-2303 (CHP) and SN-2310 (Phenol) are highest risk

Outstanding gaps: CDN process P&ID sheets 0002–0023 (29 sheets, not yet received); Operating Manual; Equipment Data Sheets; calorimeter tag conflict unresolved

## [2026-06-06] ingest | CDN PFD Set — 8 drawings (14780-8120-20-23-0000 to 0006 + Cover), Rev Z1 As-Built

Pages created: project.md, units/cdn.md, equipment/V-2301.md, equipment/V-2302.md, equipment/D-2304.md, equipment/D-2306.md, equipment/E-2304.md, equipment/E-2307.md, equipment/X-2308.md, sources/pfd-cdn.md
Pages updated: index.md, overview.md
Key findings:
- Plant identity confirmed: PTT Phenol Train II (PPCL), Map Ta Phut, Thailand; Licensor UOP; Engineer POSCO Engineering; Project 120117
- CDN section = Concentration + Decomposition + Neutralization (3 sub-sections, not just cleavage)
- 30+ equipment tags identified with real tag numbers (V-23xx, D-23xx, E-23xx, P-23xx, X-23xx)
- Decomposer (D-2304) recirculation ratio confirmed as 30.8:1 (1,887,481 vs 61,248 kg/h)
- Decomposer temperature rise: 60°C → 72°C (12°C exotherm); after cooler E-2307: 58°C
- Calorimeters X-2308A/B confirmed as primary control signal for acid injection (UOP-specific)
- Neutralizing agent: Amine (not NaOH) — updates generic wiki description
- Full As-Built stream data table with temperatures, pressures, mass flows for all 30+ streams
- Complete material balance including all components (CHP 22.6 wt% in oxidate, cumene 76.2 wt%)
- Dehydrators E-2308A/B operating at 135°C, design 140-145°C, 5.5 kg/cm²G
- Decomposer Cooler E-2307: 18.59 MM kcal/h — largest duty in CDN section
Outstanding gaps: CDN P&IDs, Operating Manual, Equipment Data Sheets, Oxidation/Fractionation PFDs

## [2026-06-06] init | Wiki initialized

Pages created: index.md, log.md, overview.md, units/alkylation.md, units/oxidation.md, units/cleavage.md, units/distillation.md, hazards/cumene-hydroperoxide.md, hazards/phenol.md
Pages updated: —
Key findings: Foundation wiki for Phenol Process Expert built from Hock Process (Cumene Process) knowledge. Process sections defined: ALKY, OXI, CLP, DIST, UT, ETP. Awaiting source documents for population.
Outstanding gaps: All equipment, stream, instrument, procedure, and parameter pages pending source documents.

## [2026-06-14] ingest | Static Equipment Process Data Sheets — ALKY & OXI Batch (15 sheets)

Files: 15 AS-BUILT (Rev Z1, May 2016) process data sheets from raw/data_sheets/
Source: POSCO Engineering & Construction for PTT Phenol Train II (PPCL). Licensor: UOP/Honeywell.
Purpose: Provides mechanical design data (design pressure, temperature, material, internals) for ALKY and OXI static equipment. Partially satisfies PSI Readiness Category 6 — Equipment Data Sheets (Table A6.2-2).

**Data sheets ingested (15 files — all in raw/data_sheets/):**
ALKY: D-2121, D-2122
OXI: D-2201, D-2202, D-2203, D-2204A/B/C, D-2205, D-2206, D-2207, D-2208, D-2211, OX-2201, OX-2202, V-2201
CDN: V-2301 (update to existing page)

Pages created (14 new equipment pages):
- wiki/equipment/D-2121.md (NEW — Cumene Column Reboiler Condensate Pot, ALKY)
- wiki/equipment/D-2122.md (NEW — PIPB Column Reboiler Condensate Pot, ALKY)
- wiki/equipment/D-2201.md (NEW — Combined Feed Surge Drum, OXI)
- wiki/equipment/D-2202.md (NEW — CHP Process Water Break Tank, OXI)
- wiki/equipment/D-2203.md (NEW — Oxidizer Chilled Vent Gas Separator, OXI, MDMT −10°C)
- wiki/equipment/D-2204ABC.md (NEW — Charcoal Adsorbers 3 vessels, OXI, severe cyclic)
- wiki/equipment/D-2205.md (NEW — Decanter, OXI)
- wiki/equipment/D-2206.md (NEW — CHP Sump, OXI, secondary containment)
- wiki/equipment/D-2207.md (NEW — Compressed Air Scrubber, OXI, 4 valve trays)
- wiki/equipment/D-2208.md (NEW — Oxidizer Vent Gas Separator Warm, OXI)
- wiki/equipment/D-2211.md (NEW — Charcoal Adsorber Cooldown KO Drum, OXI, MDMT −10°C)
- wiki/equipment/OX-2201.md (NEW — Oxidizer No.1, OXI, API-620, 21.7 m dia.)
- wiki/equipment/OX-2202.md (NEW — Oxidizer No.2, OXI, API-620, 21.7 m dia.)
- wiki/equipment/V-2201.md (NEW — Feed Wash Column, OXI, horizontal L-L extractor, caustic service)

Pages updated (1):
- wiki/equipment/V-2301.md — Added confirmed T/T length (21,000 mm from DS), packed bed data (Sulzer Mellapak 250X, 700 mm), reboiler nozzle sizes (BC: 1120 mm, CD: 1160 mm), operating temperatures, SG; added PS-V2301 as source reference
  [CONFLICT FLAGGED: DWG 0004 P&ID showed T/T = 7550 mm; PS-V2301 DS Rev Z1 shows 21,000 mm — DS value adopted as design document]

Unit pages updated:
- wiki/units/alkylation.md — Added D-2121, D-2122 to equipment list; sources and references added
- wiki/units/oxidation.md — Full OXI equipment list added; operating parameters table updated with confirmed DS values; references added

Source summary created:
- wiki/sources/ps-static-equipment-batch-2026-06-14.md

Key findings:
- OXI oxidizers (OX-2201/2202) are API-620 tanks — 21.7 m diameter, NOT ASME VIII; vacuum protection via PVRV-1001A/B and PVRV-1401A/B at 0.0088 kg/cm²g
- Two cold service vessels: D-2203 and D-2211 (MDMT −10°C, cold insulation C-50) — chilled vent gas service at 5°C
- D-2204A/B/C are severe cyclic service — fatigue analysis required; 16°C↔119°C thermal swing every 6 hours
- D-2206 CHP Sump has EPA secondary containment requirement
- V-2201 Feed Wash Column operates liquid-full (no vapor space) at 1.8–4.7 kg/cm²g differential
- V-2301 T/T length conflict FLAGGED — DS value (21,000 mm) adopted over P&ID value (7550 mm)

PSI status: Category 6 (Equipment Data Sheets) PARTIAL — OXI static equipment covered; CDN V-2301 updated. Rotating equipment, heat exchangers, and ALKY reactor/column DS still required.

## [2026-06-16] sort | input batch — CDN heat exchanger data sheets

Files sorted: 9 process data sheets (E-2301, E-2302, E-2303, E-2304, E-2306, E-2307, E-2308, E-2309, E-2310) → raw/data_sheets/
Unclassified: none — all matched "data sheet" + equipment tag heuristic, all CDN section heat exchangers per existing equipment pages

## [2026-06-16] sort | input batch — CDN heat exchanger data sheets

Files sorted: 9 process data sheets (E-2301, E-2302, E-2303, E-2304, E-2306, E-2307, E-2308, E-2309, E-2310) → raw/data_sheets/
Unclassified: none — all matched "data sheet" + equipment tag heuristic, all CDN section heat exchangers per existing equipment pages

## [2026-06-16] ingest | CDN Heat Exchanger Process Data Sheets (9 sheets)

Files: 9 AS-BUILT (Rev Z1, May 2016) process data sheets from raw/data_sheets/
Source: POSCO Engineering & Construction for PTT Phenol Train II (PPCL). Licensor: UOP/Honeywell. Thermal data sheets co-stamped Bechtel.
Purpose: Provides mechanical design data (materials, MDMT, corrosion allowance, tube counts, codes) for all CDN section heat exchangers. Substantially advances PSI Readiness Category 6 — Equipment Data Sheets (Table A6.2-2) for CDN.

**Data sheets ingested (9 files — all in raw/data_sheets/):**
E-2301 (Preflash & Flash Columns Condenser), E-2302A/B (Feed-Oxidate Exchangers), E-2303 (Preflash Column Steam Heater), E-2304 (Flash Column Vaporizer), E-2306 (Flash Column Bottoms Cooler), E-2307A/B (Decomposer Cooler), E-2308A/B (Dehydrators), E-2309 (Crude Product Cooler), E-2310 (Flash Column Overhead Vapor Chiller)

Pages updated (9 — all already existed from prior P&ID/PFD ingestion):
- wiki/equipment/E-2301.md — added mechanical construction data (welded plate exchanger, Ziepack, API 662/ISO 15547-1, materials, MDMT 15°C)
- wiki/equipment/E-2302AB.md — added mechanical data (TEMA C_U, tube count 1362, dual stabbed-in to V-2301)
- wiki/equipment/E-2303.md — added mechanical data (TEMA C_U, tube count 1464, stabbed-in to V-2301, fire water emergency coolant option)
- wiki/equipment/E-2304.md — added mechanical data (TEMA BEM, tube count 3433, emergency coolant pressure increase 7.0→10.5 kg/cm²g, Train I reuse rejected)
- wiki/equipment/E-2306.md — added mechanical data (TEMA C_U vertical, tube count 3606, stabbed into V-2302 bottom)
- wiki/equipment/E-2307.md — added mechanical data (TEMA AEU, tube count 2238 per shell) — **CONFLICT RESOLVED: shell design pressure corrected from 1.3 to 13.0 kg/cm²g (DS value adopted)**
- wiki/equipment/E-2308AB.md — added mechanical data (TEMA AES, tube count 486, 1 operating + 1 standby)
- wiki/equipment/E-2309.md — added mechanical data (TEMA AES, tube count 650, magnesium anode shellside)
- wiki/equipment/E-2310.md — added mechanical data (TEMA AEU, tube count 780) — **CONFLICT RESOLVED: shell ID corrected from 1260mm to 1280mm; subzero MDMT confirmed (shell −9°C, tube −14°C)**

Source summary created:
- wiki/sources/ps-heat-exchanger-batch-2026-06-16.md

Key findings:
- E-2301 is a welded plate exchanger (Ziepack), not shell-and-tube — unique among CDN exchangers
- E-2302A/B and E-2303 are both stabbed directly into Preflash Column V-2301 (dual reboiler arrangement)
- E-2304 and E-2306 stabbed into Flash Column V-2302
- E-2310 confirmed true subzero cold service (MDMT shell −9°C, tube −14°C), consistent with existing C(50) cold insulation note
- Two data conflicts identified and resolved in favor of data sheet values: E-2307 shell design pressure (1.3→13.0 kg/cm²g), E-2310 shell ID (1260→1280mm)
- E-2304 Train I exchanger design found thermally unsuitable for Train II duty — confirms new design basis

PSI status: Category 6 (Equipment Data Sheets) substantially advanced for CDN — all heat exchangers now have confirmed mechanical data. Remaining gaps: CDN static vessels (D-2301–D-2312 series), rotating equipment, ALKY reactor/column DS.

## [2026-06-16] ingest | CDN Instrument Data Sheets — PSV, Flow Instrument, Control Valve, Analyzer (4 documents)

Files: 4 AS-BUILT (Rev Z1, May 2016) process data sheets from raw/data_sheets/
Source: POSCO Engineering & Construction for PTT Phenol Train II (PPCL). Licensor: UOP/Honeywell.
Purpose: Closes the PSV set-pressure TBC gap (P&ID Readiness Checklist Item 7) and adds full flow/control-valve/analyzer instrumentation data for the CDN unit.

**Data sheets ingested (4 files, all in raw/data_sheets/):**
- 14780-8120-PS-0018_PRESSURE RELIEF VALVE PROCESS DATASHEET CDN UNIT_Z1.pdf (18 pages, 21 PSV groups + X-2311 rupture disc)
- 14780-8120-PS-0031_FLOW INSTRUMENT (CDN)_Z1.pdf (50 pages, 53 instrument tags)
- 14780-8120-PS-0010_CONTROL VALVE PROCESS DATA SHEET CDN UNIT_Z1.pdf (136 pages, 43 valve tags)
- 14780-8120-PS-0003_ANALYZER PROCESS DATA SHEET CDN SECTION_Z1.pdf (12 pages, 5 analyzer systems)

Wiki pages created:
- wiki/instruments/pressure-relief-valves-cdn.md — full PSV register, 21 groups + rupture disc
- wiki/instruments/flow-instruments-cdn.md — full flow instrument register
- wiki/instruments/control-valves-cdn.md — full control valve register
- wiki/instruments/analyzers-cdn.md — full analyzer register
- wiki/sources/ps-prv-cdn-batch-2026-06-16.md
- wiki/sources/ps-flow-instrument-cdn-batch-2026-06-16.md
- wiki/sources/ps-control-valve-cdn-batch-2026-06-16.md
- wiki/sources/ps-analyzer-cdn-batch-2026-06-16.md

Equipment pages updated (PSV data):
- wiki/equipment/V-2301.md — ✅ TBC gap closed: PSV-23-0401A/B/C/D set 2.100/2.205 kg/cm²g (DIERS runaway case)
- wiki/equipment/V-2302.md — new Pressure Relief section: PSV-23-0801A/B/C/D/E set 2.100/2.205 kg/cm²g (DIERS runaway case)
- wiki/equipment/D-2304.md — ⛔ X-2311 rupture disc burst pressure CONFLICT: 12.16 kg/cm²g@60°C (prior) vs 9.5–11.0 kg/cm²g@225–250°C (DS) — DS band adopted pending verification, HIGH PRIORITY (highest-hazard CDN vessel)
- wiki/equipment/D-2307.md — PSV tag/set-pressure CORRECTED: "PSV-2001N/B" (0.84/3.5 kg/cm²g) → PSV-2001A/B (both 3.5 kg/cm²g); 0.84 figure was PCV-2001, not a PSV
- wiki/equipment/D-2308.md, wiki/equipment/D-2309.md — PSV-0501/0701 confirmed exactly, sizing basis added
- wiki/equipment/D-2312.md — PSV-1903A/B discharge destination CORRECTED to HP Flare (was "vent to drain")
- wiki/equipment/E-2301.md — new PSV-23-0803 added (thermal expansion, plate side CW)
- wiki/equipment/E-2306.md — new PSV-23-0802 added (thermal expansion, tube side CW)
- wiki/equipment/E-2307.md — new PSV-23-1701 added (external fire, shell side CW); TV-23-1302A/B split-range valve tags added
- wiki/equipment/E-2308AB.md — PSV-1406/1407 set pressure CORRECTED 18.5→16.5 kg/cm²g; new tube-side PSV-1401A/B added
- wiki/equipment/E-2309.md — combined "PSV-1404, PSV-1405" entry SPLIT and CORRECTED (two distinct devices, different set pressures); X-2312 PSV-1403A/B/C added
- wiki/equipment/E-2310.md — new PSV-23-1001 added (thermal expansion, tube side chilled water)
- wiki/equipment/X-2302AB.md — PSV-0301A/B discharge destination CORRECTED to Decanter (was "CHP sump")
- wiki/equipment/X-2308.md — PSV-1801A/B, PSV-1802A/B design pressure and discharge destination confirmed

Equipment pages updated (analyzer confirmation — no conflicts, tag-format reconciliation only):
- wiki/equipment/P-2307AB.md — AI-0801A/B reconciled as dual outputs of AT/AY-23-0801
- wiki/equipment/P-2301AB.md — AI-0901A/B reconciled as dual outputs of AT/AY-23-0901
- wiki/equipment/E-2307.md — AT-1701 confirmed; composition and start-up acid spike (40→300 ppm) data added
- wiki/equipment/X-2310AB.md — AT-1901 confirmed; composition data added
- wiki/equipment/X-2301.md — AI-1001 confirmed as AT-23-1001; sample composition added

wiki/index.md updated: status banner, Instruments table, equipment table rows (V-2301, V-2302, D-2304, D-2307, D-2308 area, E-2308AB, E-2309, D-2312, X-2302AB), Sources Ingested table, Open Conflicts table (5 new entries), P&ID Readiness Checklist status (Item 7 closed), Gaps list (Item 7 closed).

Key findings:
- Two DIERS self-heating-reaction PSV trains (V-2301, V-2302) are the unit's core hazard relief devices — pilot-operated, modulating, custom orifice area exceeding largest standard API letter
- X-2311 rupture disc burst-pressure conflict on D-2304 is the highest-priority open item from this batch — sole overpressure protection on the highest-hazard CDN vessel
- TV-23-1302A (Cv 13,139, 20" body) is the largest control valve in the CDN unit — Decomposer Cooler CW supply
- Steam isolation valves consistently pair fail-close supply shutoff with fail-open vent-to-atmosphere valve across all three steam headers
- CHP density/concentration analyzers carry an explicit inferential-measurement warning — routine lab CHP analysis required for verification, not a standalone safety measurement
- Decomposer circulating-liquid acid analyzer (AT-1701) design basis allows acid concentration up to 300 wt ppm during start-up vs. 40 ppm normal (~7.5× transient)
- 2 internal source-document tag-naming inconsistencies found (FSL-23-1207 vs FSL-23-1202; FT-/FXT- 1501/1601/1602 body-text lag) — flagged, not wiki errors
- Documentation gap: PSV-23-1408A/B referenced as "added" in revision log but no data sheet exists in this revision

PSI status: Category 6 (Equipment Data Sheets) — PSV/relief device data now complete for CDN, closing the last open item in the P&ID Readiness Checklist (Item 7). HAZOP node analysis remains blocked only by expert P&ID node-boundary markup and Coordinator sign-off.

## [2026-06-16] ingest | CDN Instrument Data Sheets — Pressure, Level, Temperature (3 documents)

Files: 3 AS-BUILT (Rev Z1, May 2016) process data sheets from raw/data_sheets/ (sorted from input/ this session via sort_input.py)
Source: POSCO Engineering & Construction for PTT Phenol Train II (PPCL). Licensor: UOP/Honeywell.
Purpose: Completes the CDN basic-process-measurement instrumentation picture (pressure, level, temperature), complementing the PSV/Flow/Control Valve/Analyzer batch ingested earlier today.

**Data sheets ingested (3 files, all in raw/data_sheets/):**
- 14780-8120-PS-0032_PRESSURE INSTRUMENT PROCESS DATA SHEET (CDN)_Z1.pdf (40 pages, 61 tags: 13 PT, 6 PDT, 42 PI)
- 14780-8120-PS-0033_LEVEL INSTRUMENT PROCESS DATA SHEET (CDN)_Z1.pdf (22 pages, 38 tags: 21 LT/LXT, 1 radar, 1 switch, 13 LGR, 1 LS)
- 14780-8120-PS-0034_TEMPERATURE INSTRUMENT PROCESS DATA (CDN)_Z1.pdf (28 pages, 65+ tags: 33 TE/TT, 13 RTD, 22 TXT/field transmitter, 1 special in-tube assembly, 6 thermometer/output)

Wiki pages created:
- wiki/instruments/pressure-instruments-cdn.md — full pressure transmitter, dP transmitter, and local gauge register
- wiki/instruments/level-instruments-cdn.md — full level transmitter, radar, switch, and gauge register
- wiki/instruments/temperature-instruments-cdn.md — full thermocouple, RTD, field transmitter register; includes calorimeter ΔT gap-closure section
- wiki/sources/ps-pressure-level-temp-instrument-cdn-batch-2026-06-16.md

Equipment pages updated:
- wiki/equipment/X-2308.md — **Calorimeter differential-temperature instrument ranges added** (TDXT-23-1801/1803 0–40°C, TDT-23-1806/1809 0–25°C, TDXT-23-1802/1804 0–20°C), reconciled against existing TDXSHH/TDXAHH SIS tags; closes the numeric-range portion of Gaps Item 7
- wiki/equipment/D-2304.md — level instrumentation confirmed: LT-23-1301 (DCS) + LXT-23-1302/1303 (SIS, feed existing LXSHH-1302/1303); pressure/temp gauge tags added
- wiki/equipment/V-2301.md — PT-23-0401/0402 (absolute pressure, confirms deep-vacuum operation), TXT-23-0404 calibrated range added
- wiki/equipment/V-2302.md — PT-23-0801/0802, LT-23-0801/LXT-23-0802, TXT-23-0805A/B calibrated ranges added
- wiki/equipment/D-2307.md — **Radar Level tag identified as LT-23-2001** (Magnetrol guided-wave, 2100mm span, confirms fluid mix); LS-2005 tag-overlap flag raised
- wiki/equipment/X-2321.md — LS-23-2005 level switch added; cross-references D-2307 tag-overlap flag

wiki/index.md updated: status banner, Instruments table (3 new register pages), Sources Ingested table, Open Conflicts table (1 new minor entry: LS-2005/LS-23-2005), Gaps list (Item 7 substantially closed, residual gap narrowed to exact trip setpoint values).

Key findings:
- Calorimeter ΔT instruments resolve into three distinct measurements per calorimeter (Total System / Calorimeter / Inlet Line), each with a different calibrated span and a different downstream consumer (SIS trip / control signal / DCS alarm) — clarifies a previously qualitative-only SIS tag set
- D-2304 (highest-hazard vessel) now has fully documented triple-redundant level instrumentation sharing a common Decomposer-liquid reference-leg fill
- TE-23-0701 is an unusual vendor-engineered RTD assembly mounted physically inside an E-2304 exchanger tube, 600mm below the tube-bundle top — not a standard nozzle thermowell
- One minor possible tag overlap flagged (LS-2005 vs LS-23-2005, D-2307 vs X-2321) — low priority, does not block HAZOP
- No internal document tag-naming conflicts found in any of the 3 documents (unlike the Flow Instrument batch)

PSI status: Category 6 (Equipment Data Sheets) instrumentation coverage for CDN is now comprehensive across all seven instrument data sheets (PS-0003, 0010, 0018, 0031, 0032, 0033, 0034). HAZOP node analysis remains blocked only by expert P&ID node-boundary markup and Coordinator sign-off.

## [2026-06-17] ingest | GC ePHA Template v5.0 (Risk Ranking)

Files sorted from input/ into raw/standards/:
- GC_ePHA_Template_v5.0(Risk Ranking).xlsm
- Risk Ranking Matrix.png (image export of the xlsm's Risk Ranking sheet)

Pages created:
- wiki/sources/gc-epha-template-v5-risk-ranking.md

Pages updated:
- wiki/hazop/risk-matrix.md — added [Confirmed] tags to Likelihood, People, Environment, Social, and 5×5 matrix sections (now corroborated by two independent company documents); added GPC/BU/Small BU economic table and a ⛔ CONFLICT flag against the existing Upstream/Downstream/GC-S economic table (GPC=Upstream confirmed; BU/Small BU do not match Downstream/GC-S)
- wiki/index.md — status banner, Sources Ingested table, Open Conflicts note

Key findings:
- Core RAM (5×5 Likelihood×Severity matrix, Likelihood frequency basis, People/Environment/Social PEES tables, risk-level action bands) is now independently confirmed by both W-(Q-MP)-002 R2 and this e-PHA template — strengthens confidence for all future node risk rankings
- Economic severity table is NOT consistent between the two governing documents: category names differ (GPC/BU/Small BU vs Upstream/Downstream/GC-S) and only one of three tiers maps cleanly (GPC=Upstream). This must be resolved with the HAZOP coordinator/safety engineer before Economic severity is used in any node worksheet — compounds the pre-existing open question of which plant classification applies to PTT Phenol (PPCL)
- Workbook also contains a GWMaster (expanded guideword set) and official worksheet/action-item column templates — not ingested into methodology.md this pass; flagged for future review in the source page

PSI/HAZOP status: Risk matrix now corroborated by a second independent company standard. Economic severity category conflict is a new blocker that must be resolved before any node worksheet assigns an Economic severity score. Does not block node boundary definition (still pending expert P&ID markup).

## [2026-06-17] ingest | Example HAZOP Report O-P3-PHA-2026/005 (Olefins 3, Unit 1400 Fractionation)

⚠️ **Anti-bias deviation note:** This is a previous, completed HAZOP/PHA report. Per CLAUDE.md's HAZOP Anti-Bias Rule, previous reports must never be ingested during an active study. The user explicitly requested ingestion for documentation-style/template purposes, reasoning that the source unit (Olefins 3, Unit 1400 — Ethylene/Propylene Fractionation) is unrelated to PTT Phenol (PPCL) CDN and therefore cannot anchor CDN-specific findings. I flagged the conflict with AskUserQuestion before proceeding; user chose "Full ingest" split into two pages (structure-only + full example), explicitly authorizing this exception.

File moved from input/ to raw/hazop/example/O-P3-PHA-2026_005.xlsx (kept separate from raw/standards/ and from raw/hazop/archive/, which CLAUDE.md reserves for post-study gap comparison).

Pages created:
- wiki/hazop/templates/gc-hazop-worksheet-template.md — column/structure-only extraction (report tabs, per-node header block, 3-risk-block deviation table incl. "After Recommendation Comp." block not in our current schema, IL/ESD safeguard flag, Action Items and Interlock/ESD Summary tab structures). No findings content.
- wiki/hazop/examples/o-p3-fractionation-2026-005.md — full filled example with prominent anti-bias caution banner; documents style/format observations (hierarchical deviation numbering, per-equipment design/operating conditions, inline IPL credit citations) and one fully-illustrated deviation chain, translated/condensed from the source Thai-language workbook.

Pages updated:
- wiki/index.md — HAZOP Study table (2 new rows), anti-bias confirmation note (clarified scope to "Phenol/CDN" reports specifically), status banner, source/page counts

Key findings (template/structure only — no CDN-relevant content):
- Real GC template uses a third risk block ("After Recommendation Comp.") for post-closure risk re-verification, beyond our current Initial/Mitigated two-block schema — recommended addition to node worksheet table
- Real template tags each safeguard with an explicit IL/ESD Yes/No flag and an inline IPL credit level — recommended addition to safeguard recording convention
- Real template has a dedicated cross-node "Interlock/ESD Summary" rollup tab — we have no equivalent page yet; candidate wiki/hazop/interlock-esd-summary.md once CDN nodes are analyzed
- Action Items tab splits Owner into Employee ID/Name and internal-staff-vs-external-party, and separates Completion Date from Approved Date (two-step close-out) — recommended additions to our action-register schema

Does not affect HAZOP node analysis readiness: still blocked only by expert P&ID node-boundary markup and Coordinator sign-off. CDN-specific anti-bias remains intact — no Phenol/CDN previous report has been or may be ingested.

## [2026-06-17] hazop-skill | Developed `hazop` skill as authoritative HAZOP framework

Created `.claude/skills/hazop/SKILL.md` — a project skill that becomes the single source of truth for HAZOP workflow logic (setup, per-node deviation analysis, action close-out), at the user's explicit request to formalize a framework on top of the LLM wiki system, informed by the gaps surfaced during the GC ePHA Template and O-P3 example ingestions earlier today.

Design decisions (confirmed with user via AskUserQuestion):
- Skill becomes source of truth; CLAUDE.md's HAZOP-SETUP/HAZOP-NODE prose trimmed to a pointer
- Full lifecycle scope (setup + node + close-out), invoked as /hazop setup | /hazop node <id> | /hazop close <rec#>
- NODE workflow is interactive and node-by-node, deviation-by-deviation — entry condition requires the user to hand over the expert-marked P&ID before analysis starts (per Node Boundary Rule), and the skill checkpoints with the user through the deviation loop rather than bulk-generating worksheets unattended

Schema refinements incorporated (sourced from [[wiki/hazop/templates/gc-hazop-worksheet-template]]):
- Hierarchical cause→consequence→safeguard numbering (one cause can branch to multiple consequences, each with multiple stacked safeguards)
- Three risk blocks per deviation: Without Safeguard / With Existing Safeguard / After Recommendation Comp. (the third block, populated only at action close-out, was missing from the original schema)
- IL/ESD Yes/No flag + inline IPL credit level on every safeguard
- Action register schema extended: Owner Type (Internal/External), Completion Date separated from Approved Date
- New page type: wiki/hazop/interlock-esd-summary.md — cross-node rollup of IL/ESD-flagged safeguards, cross-checked against [[wiki/instruments/cause-effect-cdn]] and [[wiki/instruments/sis-cdn]]

The skill restates and enforces (not just references) the Anti-Bias, Standards Primacy, and Node Boundary rules, plus a new explicit check for the open Economic severity conflict in [[wiki/hazop/risk-matrix]] before any node assigns that severity category.

Files created:
- .claude/skills/hazop/SKILL.md
- wiki/hazop/interlock-esd-summary.md (empty, schema only)

Files updated:
- CLAUDE.md — HAZOP-SETUP/HAZOP-NODE sections replaced with pointer to the skill; Action Register and new Interlock/ESD Summary page format notes added
- wiki/index.md — HAZOP Study table, status banner

Does not change HAZOP readiness: node analysis is still blocked only on the engineer providing marked-up P&IDs (now the explicit Step 0 entry condition of the skill's NODE workflow) and HAZOP Coordinator sign-off.

## [2026-06-25] output | 2026-06-25_system_HAZOP-capabilities_presentation.pdf/.pptx
Type: presentation
Destination: output/presentations/
Source wiki pages: wiki/index.md, wiki/hazop/study-info.md, wiki/hazop/risk-matrix.md, .claude/skills/hazop/SKILL.md (capability synthesis)
Method: NotebookLM slide-deck generation (detailed format) from output/working/2026-06-25_system_capability-brief.md; notebook "Phenol Process Expert — System & HAZOP Capabilities" (id b131f588). HAZOP skill given two dedicated source sections (method + audit-ready worksheet). Downloaded as PDF + editable PPTX.
