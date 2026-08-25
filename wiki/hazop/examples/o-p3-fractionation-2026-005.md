---
name: Example HAZOP Report — Olefins 3 (O-P3) Fractionation Unit 1400 Revalidation
tags: [hazop, example, external-reference]
source: O-P3-PHA-2026_005.xlsx
plant: Olefins 3 (O-P3) — NOT PTT Phenol (PPCL)
last_updated: 2026-06-17
---

# Example HAZOP Report — O-P3 Fractionation Unit 1400 (PHA No. O-P3-PHA-2026/005)

> ⚠️ **ANTI-BIAS CAUTION — READ BEFORE USE**
> This page contains **actual findings** (causes, consequences, safeguards, recommendations, risk rankings) from a real, completed GC HAZOP revalidation. It is from **Olefins 3 (O-P3), Unit 1400 — Ethylene/Propylene Fractionation** — a different plant, different unit, different chemistry (C2/C3 olefins, not phenol/cumene) from PTT Phenol (PPCL) CDN.
>
> **Permitted use:** as a worked example of GC's documentation style, level of technical detail, and recording conventions (per the user's explicit instruction on 2026-06-17 to ingest this for template/concept purposes, given it is from an unrelated unit).
>
> **Not permitted:** citing this page's specific causes, consequences, safeguard designs, or risk rankings as a basis for any Phenol CDN node deviation, safeguard adequacy judgment, or risk score. CDN HAZOP node analysis must derive findings independently from CDN process data per the Standards Primacy Rule and the project's HAZOP Anti-Bias Rule. Do not reference this page from any `wiki/hazop/nodes/<id>.md` worksheet.
>
> Per CLAUDE.md, previous reports are normally excluded entirely during an active study; this page exists as a deliberate, user-authorized exception scoped to template/style learning only, because the source unit is unrelated to the plant under study.

---

## Report Identity

| Field | Value |
|-------|-------|
| PHA No. | O-P3-PHA-2026/005 |
| Project / MOC No. | GC11-REV-2026/001 |
| Title | HAZOP Revalidation Unit 1400 |
| Plant | Olefins 3 (O-P3) |
| Unit/Facility | Fractionation |
| Purpose | HAZOP Revalidation |
| Scope | Ethylene Fractionation unit reboiler and ethane recycle; Depropylenizer No.1 & 2; Debutanizer; MAPD convertor |
| Team size | 23 attendees (Leader, Scribe, Process/Ops/Maintenance/Safety members, 1 external corporate party) |
| Nodes | 8 |

---

## Documentation Style Observations (transferable to our CDN study)

1. **Node Description field includes a parenthetical scope note** in the source language (Thai) clarifying boundary mergers (e.g., "รวม 9-1 unit 1400 แล้ว" — "unit 9-1 already merged into 1400") — shows the team documents node-boundary history/rationale inline, not just the final boundary.
2. **Design Intention is written as flowing prose**, not bullet points — describes the process purpose and the equipment train in one paragraph (feed source → separation → overhead path → bottoms path), consistent with our schema's "Design Intent" prose requirement.
3. **Design Condition / Operating Condition are itemized per equipment tag**, each with Temp/Pressure/Flow rather than one aggregated node-level table — see [[wiki/hazop/templates/gc-hazop-worksheet-template]] recommendation to adopt this per-equipment layout.
4. **Deviation numbering is hierarchical**: Parameter-level deviation "1 Low/No flow" → Cause "1.1" → Consequence "1.1.1" / "1.1.2" / "1.1.3" (one cause can branch to multiple independent consequences) → Safeguard "1.1.1.1", "1.1.1.2" (multiple safeguards stack under one consequence). This is more structured than a flat row-per-deviation table and worth considering for CDN node pages with multi-branch consequences.
5. **Each safeguard line cites an IPL credit level inline** — e.g. "(IPL=1)", "(IPL=2)", "(IPL=0)" — directly in the safeguard description, alongside the Yes/No "is this an Interlock/ESD" flag. Gives an at-a-glance IPL stacking view per consequence branch.
6. **Recommendations in the Action Items tab are concrete and specific** — e.g. "Lock-open (LO) the Treated Water supply valve and Cooling Water return line, and update P&ID page 1000-PI-1402" — names the exact valve action and which drawing to revise. Matches our [[wiki/hazop/methodology]] DO/DON'T recording guidance (action verb + specific target + reason).
7. **One recommendation cites an external risk-ranking tool** ("ref. Top List MAE Bowtie") — shows recommendations may draw on parallel risk-assessment artifacts (bowtie analysis) beyond the HAZOP worksheet itself.

---

## Illustrative Deviation Entry (Node 1 — Ethylene Fractionation reflux/product, condensed/translated)

> Shown only to illustrate documentation depth and style. Numbers, tags, and safeguard designs are specific to Olefins 3 Unit 1400 and must not be reused for Phenol CDN.

- **Parameter / Deviation:** Flow / Low-No Flow
- **Cause 1.1:** Reflux pump trip, or loss of suction during pump changeover
- **Consequence 1.1.1:** Loss of reflux → column overpressure beyond design → equipment damage, fire, explosion, one fatality
  - Severity: P=4, En=3, Ec=4, S=3 → **Risk (without safeguard): High**
  - Safeguard 1.1.1.1: High-pressure alarm (PIC, setpoint ~16.7 kg/cm²g) prompting operator to open a vent valve to flare (IPL=1, not Interlock/ESD)
  - Safeguard 1.1.1.2: 2-out-of-3 voted pressure transmitters trip the refrigerant valves on the condensers (SIL 2 target) (IPL=2, **Interlock/ESD = Yes**)
  - Safeguard 1.1.1.3: Pressure relief valves set at 18.8 kg/cm²g, relieving to flare (IPL=1, not Interlock/ESD)
  - With safeguards: Likelihood reduced from 4 to 1 → **Risk (mitigated): Low**
- **Consequence 1.1.2:** Off-spec product to flare, minor community impact, no equipment/safety effect
  - Severity: P=1, En=1, Ec=1, S=2 → **Risk (without safeguard): Medium**
  - Safeguard: Ethane-in-ethylene analyzer alarm (High/High-High setpoints) prompting pump restart (IPL=1)
  - Mitigated: **Low**
- **Consequence 1.1.3:** Rising column level → same overpressure consequence chain as 1.1.1
  - Safeguards: High-level alarm prompting feed-rate reduction (IPL=1); high-pressure alarm/vent (IPL=0, no credit — duplicate of 1.1.1.1 with no independent action)

This shows the worksheet crediting **multiple independent IPLs stacked per consequence** (alarm + SIL-rated interlock + relief device) and explicitly assigning **IPL=0** to a safeguard that exists but earns no likelihood-reduction credit because it isn't independent — a good model for how to record non-credited safeguards in CDN worksheets per [[wiki/hazop/methodology]] Table 6.4–6.6.

---

## Action Items (style sample, content not transferable)

| # | Action (translated) | Responsible | Notes |
|---|---------------------|-------------|-------|
| 1 | Lock-open the Treated Water supply valve and Cooling Water return line; update P&ID 1000-PI-1402 | TBD | |
| 2 | Consider adding flow control for low-temperature ethane to protect the ethane storage tank (ref. Top List MAE Bowtie) | TBD | |
| 3 | Update P&ID 1000-PI-1406 to add a low-pressure alarm at 14PI012 | TBD | |
| 4 | Add a step to procedure W-(O-P3-OP)-145 (Regeneration) requiring verification of swing-blind opening and venting steam/N₂ from R-1420 to atmosphere | TBD | |

---

## References
- [[wiki/hazop/templates/gc-hazop-worksheet-template]] — structural/column extraction from the same source workbook, safe for direct reuse
- [[wiki/hazop/methodology]] — our governing methodology; this example corroborates several of its DO/DON'T and IPL-credit conventions
- `raw/hazop/example/O-P3-PHA-2026_005.xlsx` — full source workbook (8 nodes, kept in `raw/hazop/example/`, deliberately separate from `raw/standards/` and never to be cross-referenced from active CDN node worksheets)
