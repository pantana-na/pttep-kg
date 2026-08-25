---
name: Cumene Hydroperoxide (CHP) Hazard
tags: [hazard, peroxide, oxidation, cleavage]
sources: ["SDS_80-15-9_cumene-hydroperoxide.pdf"]
last_updated: 2026-06-14
---

# Hazard: Cumene Hydroperoxide (CHP)

> ⚠️ CHP is an organic peroxide — thermal decomposition risk. See [[hazards/cumene-hydroperoxide]].

> ⚠️ CHP is thermally unstable and can decompose violently and autocatalytically. It is the **highest-hazard chemical** in the phenol plant. Concentrated CHP (>50 wt%) can deflagrate or detonate under runaway conditions.

**Chemical formula**: C₆H₅C(CH₃)₂OOH (C₉H₁₂O₂)  
**Molecular weight**: 152.19 g/mol  
**CAS No.**: 80-15-9  
**Source**: [SDS_80-15-9_cumene-hydroperoxide.pdf — Source: SDS_80-15-9_cumene-hydroperoxide.pdf]

---

## GHS Classification (per SDS)

| Hazard Class | Category | Signal Word | H-Code |
|-------------|----------|-------------|--------|
| Organic Peroxide | Type E | Danger | H242 |
| Flammable Liquid | 4 | Warning | H227 |
| Acute Toxicity (oral) | 4 | Warning | H302 |
| Acute Toxicity (dermal) | 4 | Warning | H312 |
| Acute Toxicity (inhalation, vapour) | 3 | Danger | H331 |
| Skin Corrosion / Irritation | 1B | Danger | H314 |
| Specific Target Organ Toxicity (RE) | 2 | Warning | H373 |
| Aquatic Hazard (Acute) | 2 | — | H401 |
| Aquatic Hazard (Chronic) | 2 | — | H411 |

---

## Properties

| Property | Value | Source |
|----------|-------|--------|
| Physical state | Colourless to pale yellow liquid | SDS_80-15-9 |
| Molecular weight | 152.19 g/mol | SDS_80-15-9 |
| Boiling point | >150°C (decomposes before boiling) | SDS_80-15-9 |
| Flash point | ~79°C (closed cup, ~80 wt% technical grade) | SDS_80-15-9 |
| LEL / UEL | ~1% / ~7% (as cumene — vapour) | SDS_80-15-9 |
| Vapour pressure (20°C) | ~0.13 kPa | SDS_80-15-9 |
| Density | ~1.06 g/mL (80 wt% grade) | SDS_80-15-9 |
| Decomposition onset | **~80°C** (DSC at 88 wt% grade, SDS_80-15-9) — adopted as **worst-case basis for process safety study** per PSS conservative convention. Previous reference value of ~100°C superseded. [Source: SDS_80-15-9_cumene-hydroperoxide.pdf, confirmed 2026-06-14] | SDS_80-15-9 |
| Rapid decomposition above | ~130°C (uncontrolled, autocatalytic) | SDS_80-15-9 |
| SADT (Self-Accelerating Decomp. Temp.) | 60–80°C for concentrated grade (≥80 wt%) | SDS_80-15-9 |
| Heat of decomposition | >1300 J/g (exothermic) | SDS_80-15-9 |
| Auto-ignition temp | ~220°C [unverified — not confirmed by SDS_80-15-9; use with caution] | General |
| TLV-TWA | Not established (no ACGIH/OSHA OEL for CHP); use cumene OEL (50 ppm) as surrogate — confirm with industrial hygienist | SDS_80-15-9 |
| IDLH | Not established | SDS_80-15-9 |
| Odour | Sharp, phenolic | SDS_80-15-9 |

---

## Decomposition Reaction

CHP decomposes exothermically — the decomposition is **autocatalytic** once initiated:

```
C₆H₅C(CH₃)₂OOH  →  C₆H₅OH + CH₃COCH₃         (controlled cleavage at ~50°C, acid catalyst)
C₆H₅C(CH₃)₂OOH  →  Phenol + Acetone + AMS + Acetophenone + O₂ + heat  (uncontrolled)
```

**Decomposition products** (uncontrolled — per SDS): acetone (CH₃COCH₃), phenol (C₆H₅OH), cumene (C₉H₁₂), alpha-methylstyrene (AMS, C₉H₁₀), acetophenone (C₈H₈O), oxygen (O₂).

Uncontrolled decomposition generates heat, pressure, and flammable vapours rapidly. Autocatalytic nature means onset is slow but escalation is rapid once temperature exceeds SADT.

---

## Health Hazards

- **Inhalation**: Toxic (H331 — Acute Tox 3). Vapours above OEL irritate respiratory tract; high concentrations cause pulmonary oedema
- **Skin contact**: Corrosive (H314 — Skin Corr 1B). Causes burns; also Acute Tox 4 (H312) — dermal absorption hazard
- **Eye contact**: Corrosive — severe burns, permanent damage possible; flush immediately minimum 20 minutes
- **Ingestion**: Acute Tox 4 (H302) — harmful if swallowed
- **Chronic**: STOT RE 2 (H373) — possible organ damage (liver, kidney) from repeated exposure

---

## Fire and Explosion Hazards

- **Class 5.2 Organic Peroxide Type E** for transport — burns without external oxidiser
- Flash point ~79°C (flammable liquid hazard above this temperature)
- Concentrated CHP (>50 wt%) at elevated temperature: **deflagration or detonation possible**
- SADT 60–80°C — refrigerated/temperature-controlled storage required
- Decomposition releases O₂ internally — feeds self-sustaining fire even in absence of air
- **Do NOT use CO₂ or dry chemical** on burning CHP — use large quantities of water from distance
- Contamination with metals (Fe, Cu, Mn, Co), acids, or bases accelerates decomposition

---

## Reactivity Hazards

| Incompatible With | Consequence |
|-----------------|------------|
| Strong acids (H₂SO₄, HCl) | Rapid catalytic decomposition — autocatalytic onset |
| Strong bases (NaOH, Na₂CO₃) | Decomposition with heat evolution |
| Transition metals: Fe, Cu, Mn, Co, Ni | Catalytic decomposition — even trace contamination |
| Reducing agents | Rapid exothermic reaction |
| Combustible / organic materials | Fire risk via decomposition-released O₂ |
| Amines (including diamine additive) | Potential base-catalysed decomposition — maintain pH control |
| Heat above SADT (60–80°C) / decomp onset 80°C | Autocatalytic runaway possible — **80°C adopted as worst-case onset for all HAZOP consequence analysis** |

> ⚠️ **Iron ion contamination** (Fe²⁺/Fe³⁺ from corrosion) is a potent CHP decomposition catalyst. Maintain stainless steel wetted components for CHP service; avoid carbon steel in CHP-rich streams.

> ⚠️ **Copper and copper alloys** must not be used in CHP service — even trace Cu catalyses decomposition.

---

## Emergency Response

### Spill / Release
1. Evacuate area — eliminate all ignition sources
2. Do not walk through spilled CHP or contact with skin
3. Contain with dry sand or inert absorbent — **do NOT use sawdust or organic material**
4. Apply water spray to cool and dilute — do NOT apply concentrated water jet (may spread fire)
5. Isolate contaminated runoff — do not allow to enter drains
6. Notify emergency team and HAZOP coordinator immediately

### Fire Involving CHP
1. **Evacuate area** — do NOT fight from close range
2. Apply large volumes of water from maximum safe distance to cool containers
3. If fire is escalating / containers exposed to fire → withdraw all personnel and let burn under water cooling
4. Inform fire brigade of peroxide inventory and quantity
5. Detonation potential if large volume of concentrated CHP is involved — maintain exclusion zone

### Person Contaminated
1. Remove contaminated clothing immediately
2. Flush with large volumes of water for minimum 15–20 minutes
3. Flush eyes for minimum 20 minutes (hold eyelids open)
4. Seek medical attention immediately — report CHP exposure to physician

---

## PPE Requirements

| Task | Minimum PPE |
|------|------------|
| Routine rounds in CHP area | Safety glasses, standard PPE, gas monitor |
| Sampling | Face shield, chemical-resistant gloves, apron |
| Maintenance (draining CHP lines) | Full face shield, chemical-resistant suit, gloves, boot covers, H₂S/O₂ monitor |
| Emergency response | Full SCBA, chemical-resistant encapsulating suit |

---

## Plant-Specific Safe Operating Limits

| Parameter | Safe Limit | Action if Exceeded |
|-----------|-----------|-------------------|
| CHP in Oxidiser outlet (OXI feed to CDN) | ≤35 wt% | Reduce temperature, increase air purge |
| CHP feed to Cleavage (D-2304 inlet) | ≤88 wt% | Hold concentration step, check online analysis |
| CHP in Cleavage recirculation (D-2304 outlet) | ≤5 wt% | Check recirculation, acid catalyst, temperature |
| CHP storage temperature (D-2301) | ≤45°C | Increase chiller cooling; check N₂ blanketing |
| CHP drum / vessel temperature alarm | ΔT abnormal | Evacuate and investigate — potential runaway onset |

> [Source: SDS_80-15-9_cumene-hydroperoxide.pdf; operating limits from UOP GOM — confirm against equipment data sheets when available]

---

## Transport Classification

| Parameter | Value |
|-----------|-------|
| UN Number (≥80 wt% CHP) | UN 3105 |
| UN Number (other concentrations) | UN 3107 |
| Hazard Class | 5.2 (Organic Peroxide) |
| Packing Group | Not assigned (Class 5.2 specific packing) |
| Proper Shipping Name | Organic peroxide type E, liquid / Organic peroxide type G, liquid |

---

## References

- [[sources/SDS_80-15-9_cumene-hydroperoxide]] — plant GHS Safety Data Sheet (primary source)
- [[units/oxidation]] — OXI section where CHP is produced
- [[units/cleavage]] — CDN section where CHP is decomposed
- [[hazards/phenol]] — primary cleavage product
- [[hazards/acetone]] — primary cleavage product
- [[hazards/alpha-methylstyrene]] — by-product; polymerisation hazard
- [[hazards/cumene]] — starting material; CHP decomp product
- [[hazards/nitrogen]] — used for CHP tank blanketing (D-2301)
- [[instruments/cause-effect-cdn]] — SIS trips and alarms for CHP runaway prevention
