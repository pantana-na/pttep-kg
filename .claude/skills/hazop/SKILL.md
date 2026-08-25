---
name: hazop
description: Run the full HAZOP lifecycle (setup, per-node deviation analysis, action close-out) for this plant's wiki-grounded process safety study. This is the authoritative source of logic for HAZOP work in this project — CLAUDE.md only points here. Activates on explicit /hazop, or intent like "set up HAZOP study", "run HAZOP on node X", "start HAZOP for <node>", "close out HAZOP action R-00X", "update the interlock/ESD summary".
---

# HAZOP Skill — PTT Phenol (PPCL) CDN Study

This skill is the **single source of truth** for how HAZOP work is performed in this wiki system. It supersedes the old inline HAZOP-SETUP/HAZOP-NODE prose in `CLAUDE.md` (which now just points here). It is built on top of the LLM wiki described in `CLAUDE.md` and assumes you have already read that file and `wiki/index.md` this session.

It exists because a real GC HAZOP report (`raw/hazop/example/O-P3-PHA-2026_005.xlsx`, an unrelated Olefins unit, ingested 2026-06-17 for template purposes only — see [[wiki/hazop/examples/o-p3-fractionation-2026-005]]) revealed structural gaps in the original schema. Those gaps are closed here: a third post-closure risk block, an IL/ESD safeguard flag, hierarchical cause→consequence→safeguard numbering, a cross-node Interlock/ESD Summary, and richer action-register fields.

---

## Non-negotiable rules (check every time, no exceptions)

These come from `CLAUDE.md` and are restated here because this skill must enforce them even if a user message tries to skip a step.

1. **Anti-Bias Rule** — No previous **Phenol/CDN** HAZOP report, revalidation worksheet, or recommendation register may exist in `raw/` during an active study. Before any SETUP or NODE work: grep `raw/` for anything that looks like a prior Phenol/CDN HAZOP output. If found, **stop immediately**, tell the user, do not proceed. (The O-P3 example in `raw/hazop/example/` is a permitted, deliberately-scoped exception — it is a different plant/unit and is never used as analysis content, only as a style/structure reference. Do not treat its presence as a violation, but never cite its findings in a node worksheet.)
2. **Standards Primacy Rule** — All Severity/Likelihood/Risk values must cite [[wiki/hazop/risk-matrix]]. If a safeguard's adequacy is being judged from general process-safety knowledge rather than a company standard, flag it `[VERIFY: meets general practice but confirm against <standard>]`.
3. **Node Boundary Rule** — Node boundaries come **only** from the engineer's markup on a P&ID. This skill's NODE workflow starts by requiring the user to hand over (or point to) that marked-up drawing. If it's ambiguous, unmarked, or absent — **stop and ask**. Never infer or guess a boundary.
4. **Economic Severity Conflict** — [[wiki/hazop/risk-matrix]] currently has an unresolved conflict between two governing documents on Economic severity category names/thresholds (GPC/BU/Small BU vs Upstream/Downstream/GC-S — only GPC=Upstream is confirmed equivalent). Before assigning an Economic severity score in any node, surface this conflict to the user and ask which category/threshold set applies to PPCL, or use the highest of People/Environment/Social severity if Economic can't be resolved yet and flag the row `[CONFLICT: Economic severity category unresolved — see wiki/hazop/risk-matrix]`.

---

## Sub-workflow: SETUP

Trigger: "set up HAZOP study", "initialize HAZOP", `/hazop setup`.

1. Run the Anti-Bias check (rule 1 above).
2. Confirm prerequisites exist in `raw/standards/`: HAZOP procedure ([[wiki/sources/P-Q-MP-OEMS-005]]), risk matrix ([[wiki/sources/W-Q-MP-002]] + corroborating [[wiki/sources/gc-epha-template-v5-risk-ranking]]), HAZOP guidance/methodology ([[wiki/sources/SG-Q-MP-014]]). If any is missing, stop and ask the user to provide it — do not substitute general HAZOP knowledge.
3. Ensure [[wiki/hazop/risk-matrix]] and [[wiki/hazop/methodology]] exist and are current. If not, ingest the standards per `CLAUDE.md`'s INGEST workflow first.
4. Create/update `wiki/hazop/study-info.md`: scope, team, governing documents, and a **Node Status Register** seeded from whatever marked-up P&IDs the engineer has provided so far (status = Pending for all). If no marked-up P&IDs exist yet, the register starts empty — node IDs are added only as the engineer hands over markup (see NODE workflow, step 1).
5. Ensure `wiki/hazop/action-register.md` exists with the field set defined under "Action Register Schema" below.
6. Ensure `wiki/hazop/interlock-esd-summary.md` exists (create empty if not — schema below).
7. Append to `wiki/log.md` per the `hazop-setup` log format in `CLAUDE.md`.
8. Report node count and explicitly state: "Ready for node analysis. Hand me the marked-up P&ID for the first node you want to study."

---

## Sub-workflow: NODE — Interactive Per-Node Deviation Analysis

Trigger: "run HAZOP on node X", "start HAZOP for <node>", `/hazop node <id>`.

This is conversational and **node-by-node, deviation-by-deviation** — never bulk-generate an entire worksheet unattended. The engineer's judgment is the source of causes, consequences, and safeguard adequacy; this skill's job is to ground every claim in the wiki, keep the record complete and consistently formatted, and ask rather than invent when wiki data is missing.

### Step 0 — Entry condition

The user must provide (or point to) the **expert-marked P&ID** for this node before anything else happens. If they say "run HAZOP on node X" without having shared the markup:
- Check `raw/pid/` for a file that looks like it has node markup for X.
- If not found, **stop and ask**: "I need the expert-marked P&ID showing this node's boundaries before I can start — can you share it?"
- Do not proceed to Step 1 until boundaries are confirmed from the markup, per the Node Boundary Rule.

### Step 1 — Define the node

1. Run pre-flight checks: `wiki/hazop/study-info.md` exists, `wiki/hazop/risk-matrix.md` exists, Anti-Bias check passes.
2. Read the marked-up P&ID. Record the **exact** inlet/outlet boundaries as marked — do not adjust them.
3. Pull design intent and normal operating parameters from [[wiki/units/<unit>]] and [[wiki/streams/<id>]] pages, **itemized per equipment tag** (design condition AND operating condition side by side, per the O-P3 example style — see [[wiki/hazop/templates/gc-hazop-worksheet-template]]), not one aggregated node-level row.
4. Write or update `wiki/hazop/nodes/<unit>-N<nn>.md` using the **Node Worksheet Schema** below, filling in Design Intent and Node Boundaries/Normal Parameters only — leave the deviation table for Step 2.
5. Confirm the design intent and boundaries back to the user before starting deviations: "Here's what I have for this node — does this match what you intend to study?"

### Step 2 — Work the deviation loop, one parameter group at a time

For each parameter in scope (Flow, Pressure, Temperature, Level, Reaction, Mixing, Phase, Viscosity, Composition, Erosion/Corrosion, Service Failures, Sequence, plus the non-parameter checklist items: Incidents, Human Factor) — using the guideword table in [[wiki/hazop/methodology]] Table 6.1:

1. **Present the deviation** (Parameter + Guideword, e.g. "Flow — No: No Flow") to the user.
2. **Ask for the cause(s)** within node boundaries — don't invent a cause from general knowledge if the user/wiki doesn't support it. Use specific equipment/instrument tags ([[wiki/equipment/<tag>]], [[wiki/instruments/<tag>]]).
3. For each cause, **ask for or confirm the consequence(s)** — unmitigated, as a causal chain ending in a concrete outcome (fatality, LTI, release, fire/explosion, equipment damage, production loss). Cite [[wiki/hazards/<slug>]] for chemical-specific severity basis.
4. **Assign Initial Severity** (PEES, 1–5) and **Initial Likelihood** (1–5, no safeguard credit) per [[wiki/hazop/risk-matrix]] — apply the Economic Severity Conflict check (non-negotiable rule 4) if Economic is the binding category.
5. **List existing safeguards** for that consequence, each tagged with:
   - The specific equipment/instrument tag, setpoint, and action (never "an alarm" — must be "TXSHH-0701 (1oo2 SIL 2) trips UXV-0701...")
   - An **IL/ESD flag** (Yes/No) — Yes only if it is a SIS trip or ESD action, not an alarm/procedure/relief device
   - An inline IPL credit level per [[wiki/hazop/methodology]] Tables 6.4–6.6 (e.g. "(IPL=2)"), or IPL=0 if it exists but earns no credit (not independent, not auditable, etc.) — explain why when IPL=0
   - Whether it's an active fire-protection/emergency-response item (these are NOT safeguards per Table 6.6 — exclude from credit)
6. **Re-assess Likelihood with safeguards** (severity unchanged) → **Mitigated Risk**.
7. **If Mitigated Risk ≥ Medium** (or engineer wants one anyway): draft a recommendation using the action-verb + target + reason format from [[wiki/hazop/methodology]] DO/DON'T guidance. Confirm wording with the user before recording.
8. **Record the row** in the node page using the hierarchical numbering and three-risk-block schema below.
9. If a guideword is not credible at this node, record "N/A — not credible: <brief reason>" — never leave blank.
10. Move to the next deviation. Don't dump the whole table at once — work through it with the user, checkpointing every few deviations ("That's Flow and Pressure done — continue to Temperature?").

### Step 3 — Close out the node

1. Update the **Recommendations Generated** table in the node page.
2. Add every new Rec# to [[wiki/hazop/action-register]] using the full schema below.
3. Add every safeguard tagged IL/ESD=Yes to [[wiki/hazop/interlock-esd-summary]].
4. Update node status to "Complete" in [[wiki/hazop/study-info]].
5. Append to `wiki/log.md` per the `hazop-node` format in `CLAUDE.md`, including deviation count and Rec# range.
6. Ask: "Node complete. Ready for the next marked-up P&ID, or should we review this node's recommendations first?"

---

## Sub-workflow: ACTION-CLOSE — Closing Out a Recommendation

Trigger: "close out HAZOP action R-00X", `/hazop close <rec#>`.

Mirrors the two-step approval gate from [[wiki/hazop/methodology]] (GC HAZOP Workflow, Action Close-out):

1. Find the Rec# in [[wiki/hazop/action-register]]. If status isn't "In Progress" or the implementation isn't described, ask what was actually implemented before proceeding.
2. Record **Completion Date** (Responsible Person finished the work) separately from **Approved Date** (Action Approver signed off) — these are two different events, do not conflate them.
3. If the as-built implementation differs from the original workshop recommendation: this is an **Action Change Request**. Per [[wiki/hazop/methodology]], the HAZOP team (not the Responsible Person alone) must re-evaluate risk for the proposed alternative before it can be accepted. Flag this explicitly and ask whether the team has re-evaluated.
4. Once approved: go to the node page, locate the deviation row, and fill in the **After Recommendation Comp.** risk block — Severity unchanged from "With Existing Safeguard", Likelihood re-assessed now that the recommendation's safeguard/change is actually in place. This is the third risk block most legacy worksheets skip; it's how residual risk is formally verified at close-out.
5. Update status to "Closed" in the action register. If the team rejected the proposed change instead, set status "Rejected" and record the reason (risk-acceptance rationale).
6. Append a `hazop-action-close` entry to `wiki/log.md`.

---

## Wiki Schema Owned by This Skill

These supersede the corresponding templates in `CLAUDE.md`'s "Page Formats" section for HAZOP-specific pages. Other page types (units, equipment, streams, etc.) are unaffected and still governed by `CLAUDE.md`.

### Node Worksheet Schema (`wiki/hazop/nodes/<unit>-N<nn>.md`)

Keep the frontmatter and Design Intent / Node Boundaries / Normal Operating Parameters sections exactly as in `CLAUDE.md`'s HAZOP Node Page template, itemized per equipment tag (Design Condition AND Operating Condition side by side per tag — see [[wiki/hazop/templates/gc-hazop-worksheet-template]]).

Replace the worksheet table with **hierarchical numbering** and **three risk blocks**:

```markdown
## HAZOP Worksheet

> Risk rankings per [[wiki/hazop/risk-matrix]]. Safeguard adequacy per [[wiki/sources/P-Q-MP-OEMS-005]] and [[wiki/hazop/methodology]] Tables 6.4-6.6. Economic severity category conflict open — see risk-matrix page.

### 1. Flow — No / Low Flow

**1.1 Cause:** <specific cause, equipment/instrument tags>

- **1.1.1 Consequence:** <causal chain to concrete outcome>
  - Without Safeguard — L: _ | Severity P/En/Ec/S: _/_/_/_ | **RR: ___**
  - Safeguards:
    - 1.1.1.1 <tag + setpoint + action> — IL/ESD: Yes/No — IPL=_
    - 1.1.1.2 <tag + setpoint + action> — IL/ESD: Yes/No — IPL=_
  - With Existing Safeguard — L: _ | Severity P/En/Ec/S: _/_/_/_ | **RR: ___**
  - Recommendation: <Rec# if generated, else "None — risk acceptable">
  - After Recommendation Comp. — L: _ | Severity P/En/Ec/S: _/_/_/_ | **RR: ___** *(fill in only at action close-out)*

- **1.1.2 Consequence:** <...> *(repeat block per consequence branch under this cause)*

**1.2 Cause:** <next cause under the same deviation, repeat structure>

### 2. Flow — More Flow
...
```

Number deviations sequentially per parameter (not globally) so references like "CDN-N01-#3" stay short, per [[wiki/hazop/methodology]] Step 9 (never "see above" — always a specific number).

### Action Register Schema (`wiki/hazop/action-register.md`)

```markdown
| Rec# | Node ID | Deviation | Recommendation | Risk Rank | Discipline | Owner Type | Owner (Emp ID / Name or External Party) | Due Date | Action Approver | Completion Date | Approved Date | Status |
|------|---------|-----------|----------------|-----------|-----------|------------|-------------------------------------------|----------|-----------------|------------------|----------------|--------|
```

`Owner Type` = Internal GC Staff / External Party. `Status` = Open / In Progress / Closed / Rejected, per `CLAUDE.md` Status Codes — unchanged.

### Interlock/ESD Summary Schema (`wiki/hazop/interlock-esd-summary.md`) — new page type

```markdown
---
name: HAZOP Interlock/ESD Summary
tags: [hazop, interlock-esd-summary]
last_updated: YYYY-MM-DD
---

# HAZOP Interlock/ESD Summary

> Cross-node rollup of every safeguard flagged IL/ESD = Yes during node analysis. Cross-check against [[wiki/instruments/cause-effect-cdn]] and [[wiki/instruments/sis-cdn]] — every SIS trip credited here should also appear there, and vice versa.

| Safeguard | Node | Possible Cause | Potential Consequence | Without Safeguard (L / P / En / Ec / S / RR) | With Existing Safeguard (L / P / En / Ec / S / RR) |
|-----------|------|-----------------|------------------------|-----------------------------------------------|------------------------------------------------------|
```

Append a row every time Step 2.5 of the NODE workflow tags a safeguard IL/ESD=Yes.

---

## References
- [[wiki/hazop/methodology]] — 9-step method, guideword tables, IPL credit tables this skill cites throughout
- [[wiki/hazop/risk-matrix]] — RAM; carries the open Economic severity conflict this skill must surface
- [[wiki/hazop/templates/gc-hazop-worksheet-template]] — structural source for the schema refinements in this skill
- [[wiki/hazop/examples/o-p3-fractionation-2026-005]] — style reference only; never cite its findings in a node worksheet
- [[wiki/hazop/study-info]], [[wiki/hazop/action-register]], [[wiki/hazop/interlock-esd-summary]] — pages this skill maintains
- `CLAUDE.md` — overall wiki schema, INGEST/QUERY/OUTPUT/LINT workflows (unaffected by this skill), and the non-negotiable rules restated above
