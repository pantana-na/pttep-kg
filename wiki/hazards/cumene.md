---
name: Cumene Hazard
tags: [hazard, cumene, alkylation, oxidation]
sources: ["SDS_98-82-8_cumene.pdf"]
last_updated: 2026-06-14
---

# Hazard: Cumene / Isopropylbenzene (C₉H₁₂)

> ⚠️ Cumene is an aspiration hazard — do NOT induce vomiting after ingestion. Cumene also auto-oxidises to Cumene Hydroperoxide (CHP) on prolonged air exposure — see [[hazards/cumene-hydroperoxide]].

**Chemical formula**: C₆H₅CH(CH₃)₂ (C₉H₁₂)  
**IUPAC name**: Isopropylbenzene  
**Molecular weight**: 120.19 g/mol  
**CAS No.**: 98-82-8  
**Process section**: ALKY (product), OXI (feedstock), CDN (cleavage product / recycle)  
**Source**: SDS_98-82-8_cumene.pdf

---

## GHS Classification (per SDS)

| Hazard Class | Category | Signal Word | H-Code |
|-------------|----------|-------------|--------|
| Flammable Liquid | 3 | Danger | H226 |
| Aspiration Hazard | 1 | Danger | H304 |
| Acute Toxicity (inhalation) | 4 | Warning | H332 |
| Specific Target Organ Toxicity (SE) | 3 | Warning | H336 (CNS narcosis) |
| Specific Target Organ Toxicity (RE) | 2 | Warning | H373 |

> **PSS precautionary classification — Carcinogenicity:** Carc 1B (H350) is applied as a **precautionary working basis for this process safety study** per confirmation 2026-06-14. This classification is not present in the plant SDS (SDS_98-82-8_cumene.pdf) but has appeared in ECHA C&L submissions. ACGIH designates cumene as A3 (confirmed animal carcinogen). **For all HAZOP consequence analysis and occupational hygiene assessments in this study, treat cumene as a potential carcinogen (Carc 1B basis).** ECHA C&L Inventory verification is recommended before finalising the formal PSI document. [Confirmed 2026-06-14 — PSS conservative basis]

---

## Properties

| Property | Value | Source |
|----------|-------|--------|
| Physical state | Colourless liquid, aromatic odour | SDS_98-82-8 |
| Boiling point | 152.4°C | SDS_98-82-8 |
| Melting point | −96.0°C | SDS_98-82-8 |
| Flash point | 38°C (closed cup) | SDS_98-82-8 |
| Auto-ignition | 424°C | SDS_98-82-8 |
| LEL / UEL | 0.9% / 6.5% | SDS_98-82-8 |
| Vapour pressure (20°C) | 0.6 kPa | SDS_98-82-8 |
| Vapour density (air = 1) | 4.1 — significantly heavier than air | SDS_98-82-8 |
| TLV-TWA (ACGIH) | 50 ppm (244 mg/m³); Skin notation; A3 carcinogen designation | SDS_98-82-8 |
| TLV-STEL (ACGIH) | 75 ppm | SDS_98-82-8 |
| IDLH (NIOSH) | 900 ppm | SDS_98-82-8 |
| Odour threshold | ~0.1 ppm | SDS_98-82-8 |

---

## Health Hazards

### Aspiration — CRITICAL WARNING
- H304 (Aspiration Hazard 1): if swallowed and enters lungs — can cause severe chemical pneumonitis (aspiration pneumonia)
- **Do NOT induce vomiting** after ingestion; seek medical attention immediately

### Acute Inhalation
- H332 (Acute Tox 4) + H336 (STOT SE 3): narcotic effect — dizziness, headache, nausea, drowsiness at concentrations above TLV
- High concentrations: CNS depression, loss of consciousness

### Chronic / Repeat Exposure
- H373 (STOT RE 2): possible systemic organ damage from repeated/prolonged exposure
- **Carc 1B precautionary PSS basis** (H350): ACGIH A3 confirmed animal carcinogen; Carc 1B applied as working conservative classification for this process safety study per confirmation 2026-06-14 — apply ALARA; biological monitoring recommended for workers with routine cumene exposure

### Skin / Eye
- Mild skin irritant on prolonged contact; causes dermatitis
- Eye irritant — flush with water immediately

---

## Fire and Explosion Hazards

- Flash point 38°C — flammable liquid; elevated risk during warm-weather operations and hot-work
- Vapour density 4.1 — heavier than air; vapour accumulates in low points (drains, sumps, pits)
- Fires: CO₂, dry chemical, foam; water spray to cool containers
- Prevent static accumulation — bond and ground all transfer equipment

---

## Reactivity Hazards

| Incompatible With | Consequence |
|-----------------|------------|
| Strong oxidisers | Fire / explosion |
| Air (prolonged contact) | **Auto-oxidation to CHP** — monitor CHP content in cumene storage/recycle |
| Nitric acid + H₂SO₄ | Nitration hazard |
| Aluminium chloride / Lewis acids | Alkylation / Friedel-Crafts reaction |

> ⚠️ **Auto-oxidation to CHP**: Cumene slowly auto-oxidises in the presence of air and light to form Cumene Hydroperoxide. CHP content in cumene storage/recycle streams must be monitored regularly — accumulation creates a peroxide decomposition hazard. See [[hazards/cumene-hydroperoxide]].

---

## Emergency Response

### Spill
1. Evacuate area; eliminate ignition sources
2. Prevent vapour accumulation (heavier than air — drains, pits)
3. Contain with inert absorbent; collect in labelled closed containers for disposal
4. Inert gas purge if contained in closed space

### Fire
1. CO₂, dry chemical, or foam; water spray to cool containers
2. Withdraw from areas with containers exposed to fire

### Person Contaminated
1. Inhalation: move to fresh air; supplemental O₂ if breathing is difficult
2. Skin: wash with soap and water; remove contaminated clothing
3. Eye: flush with water minimum 15 minutes
4. Ingestion: **DO NOT induce vomiting** — seek medical attention immediately

---

## PPE Requirements

| Task | Minimum PPE |
|------|------------|
| Routine rounds | Safety glasses, standard PPE; gas monitor |
| Sampling | Chemical-resistant gloves, face shield |
| Maintenance / draining | Full face shield, chemical-resistant gloves and apron, organic vapour respirator |
| Emergency response | SCBA, chemical-resistant suit |

---

## Environmental Hazards

- No H411 classification in SDS but aromatic hydrocarbon — apply spill containment
- Biodegradable under aerobic conditions; COD/BOD load if released to wastewater
- All spill runoff to [[units/etp]]

---

## Transport Classification

| Parameter | Value |
|-----------|-------|
| UN Number | UN 1918 |
| Hazard Class | 3 (Flammable Liquid) |
| Packing Group | III |
| Proper Shipping Name | Isopropylbenzene (Cumene) |

---

## References

- [[sources/SDS_98-82-8_cumene]] — plant GHS Safety Data Sheet
- [[units/alkylation]] — ALKY section (cumene is primary product)
- [[units/oxidation]] — OXI section (cumene is oxidised to CHP)
- [[units/cleavage]] — CDN section (cumene recycled from cleavage products)
- [[hazards/cumene-hydroperoxide]] — CHP (cumene auto-oxidation product; cleavage feedstock)
- [[hazards/benzene]] — alkylation co-feedstock
- [[hazards/propylene]] — alkylation co-feedstock
