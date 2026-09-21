---
name: HAZOP Leadership Training for GC — Chapter 4: HAZOP Study Methodology
file: "5. Chapter 4 - HAZOP Methodology.pdf"
location: raw/standards/
type: training
tags: [hazop, training, methodology, guidewords, ipl, standards]
last_updated: 2026-06-13
---

# Source: HAZOP Leadership Training — Chapter 4: HAZOP Study Methodology

## Document Identity

| Field | Value |
|-------|-------|
| Title | HAZOP Leadership Training for GC — Chapter 4: HAZOP Study Methodology |
| Organisation | Refinery Petrochemical Corporation — Technical Safety Service Division (Q-TS-TS) |
| Instructor | Mr. Noraphol Sookkho, Division Manager, Q-TS-TS |
| Date | 1–3 November 2021 |
| File | `raw/standards/5. Chapter 4 - HAZOP Methodology.pdf` |
| Parent course | [[sources/hazop-leadership-training-intro]] |

## Purpose

The most technically detailed chapter of the training course. Covers all 9 sub-steps of HAZOP execution with worked examples, DO/DON'T guidance, guideword table, standard deviation set, IPL concept, risk determination, and recommendation recording. Content cross-validates and supplements [[hazop/methodology]].

> **Precedence note:** Where this training material conflicts with the governing document SG-(Q-MP)-014 R3, the governing document ([[sources/SG-Q-MP-014]] / [[hazop/methodology]]) takes precedence. Training slides pre-date the governing standard by ~5 years.

---

## Sub-Chapter Structure

| Sub-chapter | Topic |
|-------------|-------|
| 4-1 | Node preparation — node selection and design intent |
| 4-2 | Guidewords and deviations |
| 4-3 | Developing and recording possible causes |
| 4-4 | Developing and recording potential consequences |
| 4-5 | Existing safeguards |
| 4-6 | IPL concept |
| 4-7 | Risk determination |
| 4-8 | Developing recommendations |
| 4-9 | Worksheet reference |

---

## 4-1: Node Preparation

### HAZOP Leader Qualifications (reaffirmed from training)
- **Internal Leader:** min 8 years in Refinery/Petrochemical/Chemical; trained HAZOP Leadership course; trained Awareness of Process Safety in Design; must be **independent person**
- **External Leader:** must be qualified and registered by Q-TS-TS (qualified leader list maintained by Q-TS-TS)
- HAZOP Coordinator submits CV to HAZOP Procedure custodian for approval

### Node Definition
- Node = breaking the overall complex process design into simpler sections for individual review
- Usually defined by study leader prior to/during meetings in consultation with process engineer
- P&IDs divided into nodes based on logical process flow
- Nodes are points where process parameters have an identified design intent
- **Good practice: nodes should not cross from one P&ID to the next**

### Node Boundary Guidance

| Approach | Guidance |
|----------|---------|
| Strict | Whenever a parameter changes |
| Practical | End of transfer lines, at vessel interface |
| Single line or vessel | Normally constitutes one node |
| Short feed line | May be reviewed together with the upstream interface |
| Heat exchangers/condensers | Can be included in the same node as the connected vessel |
| Pressure control and relief lines | Can be included with the vessel |
| Complete vapor circuit (compressor) | Can be a single node even if spanning several flow sheets |
| Systems with multiple operation modes | Separate node OR repeat same node with different operation mode (regeneration, de-coke, etc.) |

### Node Size Trade-off

| Node Size | Pros | Cons |
|-----------|------|------|
| Big (broad boundary) | Saves study time | Hard to handle; team confusion; potential to miss hazards |
| Small (narrow boundary) | Easy to understand; better hazard identification | Extremely time-consuming; repetitive data; team fatigue and loss of interest |

### Design/Operation Intent Requirements

A good design intent statement must include:
- Description of normal design/operation occurring at the node
- Functions of the node, stream compositions, and numerical ranges of all important parameters
- Source and destination of streams
- Nature of reaction (exothermic/endothermic, mild/moderate/highly)
- Clear exclusions (e.g., vendor packages not included)

---

## 4-2: Guidewords and Deviations

### Guideword Definitions

| Guideword | Meaning | Key Examples |
|-----------|---------|-------------|
| **No / None** | Complete negation — nothing happens | No flow, no reaction |
| **More** | Quantitative increase | High flow, high pressure, high temp, high concentration |
| **Less** | Quantitative decrease | Low flow, low level, low temperature |
| **As Well As** | Qualitative increase — something added | Additional phase (vapor/solid in liquid), contaminants, air, water |
| **Part Of** | Qualitative decrease — something missing | Incomplete reaction, missing component in mixture |
| **Inversion / Reversal** | Logical inversion | Reverse flow, decomposition instead of synthesis |
| **Other Than** | Complete substitution or deviation | Different material, different operating condition (start-up, shutdown), phase change |

### Standard Deviation Set (17 Deviations by Equipment Type)

| # | Deviation | Column | Vessel | Line | Exchanger | Pump | Compressor |
|---|-----------|--------|--------|------|-----------|------|------------|
| 1 | High Flow | | | ✓ | | ✓ | ✓ |
| 2 | High Level | ✓ | ✓ | | | | |
| 3 | High Interface | ✓ | ✓ | | | | |
| 4 | High Pressure | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 5 | High Temperature | ✓ | ✓ | ✓ | ✓ | | ✓ |
| 6 | High Concentration | ✓ | ✓ | ✓ | | | |
| 7 | Low / No Flow | | | ✓ | | ✓ | ✓ |
| 8 | Low Level | ✓ | ✓ | | | | |
| 9 | Low Interface | ✓ | ✓ | | | | |
| 10 | Low Pressure | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 11 | Low Temperature | ✓ | ✓ | ✓ | ✓ | | |
| 12 | Low Concentration | ✓ | ✓ | ✓ | | | |
| 13 | Reverse / Misdirected Flow | | | ✓ | | ✓ | ✓ |
| 14 | Tube Leak | | | | ✓ | | |
| 15 | Tube Rupture | | | | ✓ | | |
| 16 | Leak | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 17 | Rupture | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |

### HAZOP "Other" Checklist Words

In addition to the parameter × guideword deviations, these special topics must be considered at each node:

| Checklist Topic | What to Consider |
|----------------|-----------------|
| Relief scenario | Are all credible overpressure scenarios covered by relief devices? |
| Instrumentation | Missing, incorrect, or mislocated instruments? |
| Sampling | Safe sampling provisions; sample representative of process? |
| Corrosion | Materials of construction adequate for service? |
| Leakage | Flange, valve, pump seal leak scenarios |
| Service failure | Loss of utility (steam, CW, IA, N₂, power) |
| Maintenance | Safe isolation, purging, blinding requirements |
| Start-up | Hazards specific to start-up mode |
| Spare equipment | Is standby equipment correctly lined up? Start-up issues? |
| Safety equipment | Availability and adequacy of fire/gas detection, ESD |

---

## 4-3: Possible Causes

### Rules for Cause Identification

- Causes must be **within the node** (exception: boundary nodes may consider upstream causes for completeness)
- HAZOP Leader manages brainstorming — team does NOT search for root causes or solutions during the session
- Each possible cause that leads to the same deviation must be recorded **separately**
- If no credible cause: record "No credible cause was/were identified" or "Not credible" or "Not applicable"

### Typical Causes Considered

- BPCS instrument loop failure
- Pressure regulator failure
- Exchanger tube leak
- Pump / compressor trip
- Utility failure (steam, cooling water, instrument air, power)
- Specific human errors (e.g., "Operator opens drain valve at V-1301 during routine round")
- General interface: loss of feed from upstream / obstruction downstream

### Causes NOT Considered Under HAZOP

> ⚠️ Do NOT record these as HAZOP causes — they are excluded by convention:

| Excluded Cause | Reason |
|----------------|--------|
| Design issues / concerns | Not a deviation-cause; design basis is taken as given |
| PSV or SIF failure | These are IPLs; their failure is addressed in SIL assessment, not HAZOP cause list |
| Pipe flange / gasket leak | Small leak — typically handled by inspection/maintenance; not a process deviation initiator |
| Closure of manual valves labelled LO/LC or CSO/CSC | Assumed to be locked in correct position per management system |

### DO / DON'T: Cause Recording

**DO:**
- "Malfunction of 11-TIC-012 leading to 11-TV-012 fully open"
- "No butene-1 supplied from T-6000"
- "Filter at the inlet of A-4451 totally blocked"
- "Pump P-1101A/B stopped"
- "Drain valve at V-1301 left open"

**DON'T:**
- "Control Fault"
- "No feed flow"
- "Filter blocked"
- "Pump faulty"
- "Low level in vessel"

---

## 4-4: Potential Consequences

### Rules for Consequence Development

- Describe consequence **without credit to any safeguard** (unmitigated)
- Consequence may occur inside OR outside the node
- Describe **"step by step"** chain with linking words: "leading to", "resulting in", "causing"
- Multiple consequences from the same cause → record **separately**
- HAZOP Leader decides whether to include out-of-node consequences in this node or defer to a later node — but they must be fully covered somewhere

### DO / DON'T: Consequence Recording

**DO:**
- "Reaction runaway causing high pressure & temperature inside reactor (R-110) resulting in reactor fail/rupture, potential LOPC fire and explosion"
- "Low reflux to C-1302 leading high temperature and pressure at overhead of C-1302, potential loss of ethylene to overhead and overpressure at C-1302, resulting in LOPC, fire & explosion, single fatality"

**DON'T:**
- "R-110 Runaway"
- "Loss reflux to C-1302 leading high temperature and pressure at overhead of C-1302"

---

## 4-5: Existing Safeguards

### Definition
Existing safeguard = engineered systems or administrative controls designed to prevent or mitigate consequences, **already present** in the facility or design documentation.

- Safeguards are **not restricted** to inside the node
- Record **prevention safeguards first**, then mitigation safeguards
- General active fire protection and emergency response are **NOT listed** as safeguards (post-event; uncertain effectiveness)
- Use equipment tag or location to identify; describe what it protects and how

### DO / DON'T: Safeguard Recording

**DO:**
- "Pressure control 13-PIC-100 (5 kg/cm²g) on separator V-1000"
- "High high pressure 14PAHH006A/B/C (10.7 kscg, 2oo3 voting) to trigger Interlock Z-141 (SIL-1) to cut steam to reboiler E-1406A/R"
- "11-PSV-056A/B/R (Set at 23 barg) on HP separator V-1000"

**DON'T:**
- "High pressure alarm PAH"
- "PSV-100"
- "High level alarm"

### Typical Preventive Safeguards
- BPCS instrument loops (PIC, FIC, TIC)
- Alarms with operator response (PAH, PAL, LAH, LAL)
- Safety Instrumented Function (SIF / SIS trip)
- Mechanical switches
- Pressure relief devices (PSV, rupture disc, emergency hatch)

### Typical Mitigative Safeguards
- Dike / impounding basin (contains release after event)

---

## 4-6: IPL Concept

### IPL Definition
Independent Protection Layer (IPL) = a device, system, or action capable of preventing a scenario from proceeding to its undesired consequence, **independent** of the initiating event or any other layer of protection.

> *All IPLs are safeguards, but not all safeguards are IPLs.*

### Three IPL Criteria

| Criterion | Requirement |
|-----------|-------------|
| **Effective** | Fit for purpose; capable of detecting hazard condition in time and taking corrective action |
| **Independent** | Not part of the initiating event; not part of another safeguard; does not create additional hazard |
| **Auditable** | Management systems in place to maintain barrier health; can be audited/tested |

### Key IPL Evaluation Questions (per criterion)

**Effective:**
- Can it detect the hazard condition?
- Can it detect it in time to take corrective action?
- Does it have adequate ability to take the required action in the time available?

**Independent:**
- Does the initiating event affect the IPL's function?
- Does another IPL in the chain affect this IPL?

**Auditable:**
- Is there evidence of SIL assessment and proof testing within proper period?
- Does management comply with maintenance standards?

### What Is NOT an IPL

| Non-IPL | Reason |
|---------|--------|
| Training, certification, procedures | May affect PFD of operator response, but not an IPL by itself |
| Signs and labels | Unclear, obscured, or ignored; not reliable alone |
| Normal testing, inspection and maintenance | Baseline assumption; not a protective function |
| Active fire protection / emergency response | Post-event; effectiveness may be affected by the very fire/explosion it is intended to contain |
| Communications | Basic assumption; not an IPL by itself |

---

## 4-7: Risk Determination

### Likelihood Guidance (from training — see governing table in [[hazop/methodology]])

| Initiating Event | Typical Frequency | Guidance Likelihood Level |
|-----------------|------------------|--------------------------|
| BPCS instrument loop | 1 to 1/10 per year | **L4** |
| Human error — routine (≥ once/week) | ~1/year | **L5** |
| Human error — periodic (1/year ≤ task < 1/week) | 1 to 1/10 per year | **L4** |
| Pressure regulator | 1 to 1/10 per year | **L4** |
| Pump / fan / compressor failure | 1/10 to 1/100 per year | **L3** |
| Loss of supply (upstream pump, accidental block) | 1 to 1/10 per year | **L4** |
| Cooling water failure | 1 to 1/10 per year | **L4** |
| Site-wide loss of power — no history | — | **L3** |
| Site-wide loss of power — has occurred | — | **L4** |
| Site-wide loss of power — > once/year | — | **L5** |

> ⚠️ **DISCREPANCY NOTE:** This training (2021) assigns pump/compressor failure → L3. The governing document SG-(Q-MP)-014 R3 [[hazop/methodology]] Table 6.3 assigns L4 (1 to 1/10 per year). Use the governing document value (**L4**) for this CDN HAZOP study.

### IPL Likelihood Reduction (from training — cross-reference [[hazop/methodology]] Tables 6.4/6.5)

| IPL Type | PFD | Reduction |
|----------|-----|-----------|
| BPCS independent loop | 0.1 | 1 level |
| SIF SIL 1 (PFD 0.1–0.01) | 0.1 | 1 level |
| SIF SIL 2 (PFD 0.01–0.001) | 0.01 | 2 levels |
| SIF SIL 3 (PFD 0.001–0.0001) | 0.001 | 3 levels |
| Alarm + operator response (sufficient time) | 0.1 | 1 level |
| Routine operator surveillance (documented, sufficient time) | 0.1 | 1 level |
| PRV — adequately sized for scenario | 0.1 | 1 level |
| 3 PRVs — 2 of 3 required, all connected | 0.001 | 3 levels |
| 3 PRVs — > 1 required but staged | — | 1 level |

---

## 4-8: Recommendations

### When to Recommend
- **Mandatory:** when mitigated risk is in unacceptable range (Medium, High, Extreme)
- **Optional:** may also recommend when risk is already acceptable (voluntary improvement)

### What to Avoid
- **Excessive recommendations:** do not issue a recommendation for every negative-consequence scenario if risk is acceptable
- **Irrelevant recommendations:** do not use HAZOP to obtain approval for operational improvements unrelated to personnel safety or hazardous release
- **Solving during HAZOP:** generate the action; do not re-engineer the plant during the session

### DO / DON'T: Recommendation Recording

**DO:**
- "Add level transmitter at V-1301 with low level alarm and operator action to prevent cavitation of P310A/B"
- "Add FI-3128, FI-3129, PI-3131 in field operator lock sheet with appropriate values"
- "Add high level alarm at E-1235 and drain valve to prevent hexane contamination to fuel gas; prepare work instruction for draining activity"

**DON'T:**
- "Add new Level indicator"
- "Update log sheet"
- "Add level alarm and drain valve"

**Recording format:** Start with action verb (Add, Change, Configure, Provide, Update, Prepare); explain **why** the recommendation is needed.

---

## 4-9: Worksheet Reference

- Use specific reference numbers for previously documented causes, consequences, or recommendations
- **Never use:** "See above", "See below", "Same as above", "Same as earlier node"
- **Never cascade references** (A references B, B references C → both A and C should reference B directly or copy content)
- **Never reference numbers from other nodes or projects** — copy the content instead

---

## Example HAZOP Worksheet (GC Format)

Typical worksheet columns (from training example slide):

| Deviation | Cause | Consequence | Existing Safeguard | Recommendation |
|-----------|-------|-------------|-------------------|----------------|
| 1. No/Low Flow | 1.1. Loss of fuel gas supply (closure of control valve 5PV-62016) | 1.1.1. Low pressure in flare header → potential vacuum → air ingress → explosive mixture → LOPC | 1.1.1.1. Low pressure alarm 5PI-50014 on KO Drum 5V-5001; 1.1.1.2. Back-up N₂ supply | 10. Provide parallel letdown control valve redundant to 5PV-62016 on fuel gas supply header |

---

## New Content Added to [[hazop/methodology]] (from this chapter)

The following content from Chapter 4 was not previously in the methodology page and has been added:
1. Standard deviation set (17 deviations by equipment type) — see §Standard Deviation Set in methodology.md
2. HAZOP "Other" checklist words (10 topics)
3. Causes NOT considered under HAZOP (4 excluded categories)
4. Node size trade-off guidance
5. DO/DON'T recording examples (causes, consequences, safeguards, recommendations)
6. Pump/compressor likelihood discrepancy note flagged

---

## References
- [[hazop/methodology]] — Governing HAZOP execution guide (SG-(Q-MP)-014 R3); supersedes training where conflicts exist
- [[sources/SG-Q-MP-014]] — SG-(Q-MP)-014 R3 — governing HAZOP guidance document
- [[hazop/risk-matrix]] — W-(Q-MP)-002 R2 — governs all risk rankings
- [[sources/hazop-leadership-training-intro]] — Course introduction
- [[sources/hazop-leadership-training-ch3]] — Chapter 3: Introduction to HAZOP
- [[hazop/study-info]] — CDN HAZOP study scope and status
