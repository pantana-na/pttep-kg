---
name: GC HAZOP Leadership Training — Chapter 5: HAZOP Preparation
tags: [source, hazop, standards, training]
metadata:
  type: standards
  series: Q-TS-TS HAZOP Leadership Training, Nov 2021
  chapter: 5
last_updated: 2026-06-14
---

# Source: GC HAZOP Leadership Training — Chapter 5: HAZOP Preparation

**File:** `raw/standards/6. Chapter 5 - HAZOP Preparation.pdf`
**Producer:** PTT Global Chemical — Technical Safety Service Division (Q-TS-TS)
**Course:** HAZOP Leadership Training, 1–3 November 2021
**Slides:** 24 pages (4 sub-chapters: 5-1 Planning, 5-2 Assemble Documents, 5-3 Team Selection, 5-4 Worksheet)

---

## Series Context

Chapter 5 of the Q-TS-TS HAZOP Leadership Training series, following:
- Course Introduction → [[sources/hazop-leadership-training-intro]]
- Chapter 1 (Hazard & Risk) → [[sources/hazop-leadership-training-ch1]]
- Chapter 2 (PHA Techniques) → [[sources/hazop-leadership-training-ch2]]
- Chapter 3 (HAZOP Introduction) → [[sources/hazop-leadership-training-ch3]]
- Chapter 4 (HAZOP Methodology) → [[sources/hazop-leadership-training-ch4]]

---

## Chapter 5-1: Planning

### Four Planning Elements
| Element | Key Points |
|---------|-----------|
| A — Purpose | Clear scope boundary; new facility vs. modification of existing plant; project phase (FEED, DD, Commissioning, Operation) |
| B — Timing | Determine duration required; set schedule |
| C — Type of Process | Continuous / Batch / Semi-batch; Automatic vs. manual handling |
| D — Administration | Meeting location / room; virtual meeting (MS Teams option) |

> **Rule:** "Lead should obtain clear scope and information of change/project from HAZOP coordinator for planning"

### Scheduling Rules of Thumb
- Each HAZOP review session = **half working day (~3.5 hours with breaks)**
- One extra session at beginning for: initial team review meeting + methodology/ground rules refreshment
- Then **one session per**: P&ID of average complexity **or** unit operation/major equipment piece
- **SIL / LOPA adds ~20%** to analysis time

### Cost Benchmarks
- HAZOP ≈ **0.2% of capital project cost** (0.25–0.3% if regulatory requirements)
- HAZOP ≈ **1% of design cost** (1.3–1.5% if regulatory); more accurate basis than capital cost
- Neither figure includes implementation of recommendations

### Time Requirements (P&ID throughput)
- **3 P&IDs per day** — process units (full and detailed)
- **4 P&IDs per day** — utilities
- **4–5 per day** — similar/repetitive equipment or early-stage drawings
- Nominal time only for duplicate trains and distribution drawings
- **Minimum acceptable: 3–4 P&IDs per day** on most projects

---

## Chapter 5-2: Assemble all Documents

> **Principle: "Caution — Garbage in, Garbage out"**
> HAZOP Leader must evaluate adequacy and accuracy of all PSI before conducting the study.

### PSI Document Requirements by Project Phase

| Document Type | Select | Define | Execute | Operation | Non-op |
|--------------|--------|--------|---------|-----------|--------|
| Operations and Maintenance philosophy | E | E | E | E | E |
| Process and Chemistry Descriptions | E | E | E | E | E |
| Process Control Narrative | D | E | E | E | E |
| Reactive Hazard (if applicable) | E | E | E | E | E |
| Material Safety Data Sheet | E | E | E | E | E |
| Plot Plan | E | E | E | E | E |
| General Equipment Arrangements & Elevations | — | E | E | E | E |
| Electrical / Hazardous Area Classification Drawings | — | E | E | E | E |
| Heat and Mass balances | D | E | E | E | E |
| Process Flow Scheme (PFD) and Utility Flow Scheme (UFS) | E | E | E | E | E |
| Process Engineering Flow Scheme / P&IDs and UEFS | D | D | E | E | E |
| Line lists for piping & process equipment | — | E | E | E | E |
| Equipment data sheet | — | D | E | E | E |
| Process Safeguarding Flow Scheme | D | E | E | E | E |
| Cause and Effect Diagrams | — | E | E | E | E |
| SIL Study report | — | — | E | E | E |
| Control valve turndown, RV, trip and alarm settings | — | E | E | E | E |
| Latest construction / as-built drawings | — | — | E | E | E |
| Previous HAZID/HAZOP reports and Close-out reports | — | D | E | E | E |
| Details of change since last PHA | — | D | E | E | E |
| Other safety studies (Bow-tie analysis) | — | — | D | E | E |

E = Essential, D = Desirable

**Key rules:**
- For **operating facility not undergoing modification**: PSI shall be signed off to "As-built" revision
- For **operating facility undergoing modification or new facility**: PSI level appropriate to project phase
- HAZOP Leader shall evaluate adequacy and accuracy to ensure information is sufficiently developed for an effective review

**Notable:** "Previous HAZID/HAZOP reports" listed as Essential for Execute/Operation phases — governed by [[CLAUDE.md]] Anti-Bias Rule during active node analysis; only permitted for gap comparison after study completion.

---

## Chapter 5-3: Select the Right Team

### Required Team Members by Regulatory Standard

| Team Member | GC | IEAT PSM 2559 | DIW 2543 |
|-------------|-----|----------------|----------|
| HAZOP Leader | ✅ | ✅ | ✅ |
| Scribe | ✅ (GC only) | — | — |
| Process Engineer | ✅ | ✅ | ✅ |
| Operation representative | ✅ | ✅ | ✅ |
| Plant Safety Engineer | ✅ | ✅ | ✅ |
| Site Maintenance Engineer | ✅ | — | ✅ |
| Licensor / specialist / vendor | Y/N (optional) | — | — |

**GC requires Scribe as a dedicated separate role** — not required under IEAT PSM 2559 or DIW 2543 but mandatory under GC standard. This is consistent with SG-(Q-MP)-014 §5.2.5.

**Common team failures:** numbers too large/small; key persons absent; insufficient team experience; only some members actively contribute.

> "Leader can request required member"

### HAZOP Leader Characteristics
- Deep understanding and considerable experience of HAZOP studies
- Wide experience across all stages of HAZOP
- Extensive experience as HAZOP study member (participant)
- Trained in leadership of HAZOP studies
- **Independent from the project** — no direct responsibility to project leader/manager beyond completing HAZOP scope
- Technical competence; quick understanding of process
- Meticulous attention to relevant details
- Good analytical thinking
- Motivation skills — encourages creativity and open speaking; moves team toward conclusions

### HAZOP Leader Responsibilities
1. Gather information for node preparation
2. Review design to determine sufficient technical information and required skills
3. Verify adequacy of team membership for multi-disciplinary effectiveness
4. Facilitate meeting/workshop; ensure all issues covered in adequate depth
5. Alert to time pressures — must NOT compromise quality, thoroughness, or integrity
6. Advise project/site leadership to delay/postpone if integrity issues cannot be resolved
7. Review and approve HAZOP study report

### HAZOP Scribe Characteristics and Responsibilities
- Must be familiar with HAZOP methodology
- Technical background — understands team discussion without constant explanations
- **Follows discussion without participating** — filters what is worth recording; records in clear diction
- Team must always know exactly what has been recorded
- Use computer recording file projected so all team members can see
- Use GC HAZOP Template (Excel or e-PHA system)

### HAZOP Team Member Responsibilities
- Fully participate (active core team member)
- Identify credible causes; develop consequences for hazards and operability problems including existing safeguards
- Evaluate risk level; suggest recommendations for prevention and mitigation to reduce risk to acceptable level

### HAZOP Team Member Characteristics
- Multi-disciplinary — experience in their represented field
- Knowledge of design basis, design intention, operating conditions, and process hazards
- Knowledge of equipment principle, working, and limitations; **current hands-on maintenance experience**
- Experience with day-to-day operations — knowing how facilities *actually* operate vs. how they are intended to operate
- Familiar with design intent, operating, start-up, shutdown, emergency, and commissioning procedures
- Good knowledge of occupational safety, health, and environment

### First HAZOP Team Meeting Agenda
Before beginning formal HAZOP methodology, the Leader should cover:
1. Team qualifications (introductions and verification)
2. Documentation (confirm all PSI available and current)
3. Plant layout / brief process description / hazards of the process
4. Previous incidents (relevant to the plant/section)
5. HAZOP method (methodology refresher, guidewords)
6. Ground rules (attendance, decision-making, participation expectations)

---

## Chapter 5-4: HAZOP Worksheet

### GC HAZOP Worksheet Column Structure (Official Template)

| Column | Sub-columns | Notes |
|--------|-------------|-------|
| Parameter | — | Flow, Temperature, Pressure, Level, etc. |
| Deviation | — | e.g., "No Flow", "High Temperature" |
| Possible Cause | — | Root cause within node |
| Potential Consequence | — | Unmitigated consequence chain |
| **Without Safeguard** | L, Severity (P / En / Ec / S), RR | Initial risk assessment — 4 severity sub-columns per PEES |
| **Existing Safeguard** | Detail | List of safeguards |
| **With Existing Safeguard** | L, Severity (P / En / Ec / S), RR | Mitigated risk — same 4 severity sub-columns |
| Recommendation | Detail | Action required if residual risk unacceptable |

**PEES severity columns:** P = People, En = Environment, Ec = Economic, S = Social — consistent with W-(Q-MP)-002 R2 RAM categories.

### Recording Options
1. **GC Excel Template** — downloadable from e-PHA system (Download button)
2. **e-PHA online system** — GC internal platform with modules:
   - MoC-PHA (Management of Change studies)
   - Revalidation-PHA / Other
   - Project-PHA
   - Analysis Dashboard (MoC)
   - PHA Leader (HAZOP) management module
   - Locked by responsible analyst; export to Excel available

---

## Pages Updated

- [[wiki/hazop/methodology]] — Added: scheduling rules of thumb, P&ID throughput rates, GC worksheet column structure (PEES sub-columns), first team meeting agenda, PSI document table
- [[wiki/hazop/study-info]] — Added: team role detail (regulatory basis GC/IEAT/DIW), Leader responsibilities, Scribe requirements

## Cross-References

- [[sources/SG-Q-MP-014]] — governs team requirements (§5.2.5); this chapter is a training complement
- [[sources/W-Q-MP-002]] — RAM with PEES categories matching worksheet severity columns (P, En, Ec, S)
- [[sources/Table-A6.2-2-PSI-readiness-checklist]] — GC-specific implementation of the PSI document table above
- [[hazop/methodology]] — execution methodology (Chapters 4–5 combined)
- [[hazop/study-info]] — study team, scheduling, and preparation status
