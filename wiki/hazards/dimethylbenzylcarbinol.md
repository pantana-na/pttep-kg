---
name: Dimethylbenzylcarbinol (DMBA) Hazard
tags: [hazard, dmba, dimethylbenzylcarbinol, cleavage, distillation]
sources: ["SDS_100-86-7_dmba-dimethylbenzylcarbinol.pdf"]
last_updated: 2026-06-14
---

# Hazard: Dimethylbenzylcarbinol / DMBA

> **Identity confirmed 2026-06-14**: DMBA in CDN product streams is confirmed as **CAS 100-86-7** (2-Methyl-1-phenyl-2-propanol / benzyl dimethyl carbinol), consistent with the plant PSI brief and SDS compiled. CAS 617-94-7 ambiguity is resolved.

**Chemical formula (CAS 100-86-7)**: C₆H₅CH₂C(CH₃)₂OH (C₁₀H₁₄O)  
**Molecular weight**: 150.22 g/mol  
**CAS No. (as specified in PSI)**: 100-86-7  
**Process section**: CDN (heavy by-product in cleavage bottoms), DIST (acid aromatics)  
**Source**: SDS_100-86-7_dmba-dimethylbenzylcarbinol.pdf

---

## GHS Classification (per SDS — CAS 100-86-7)

| Hazard Class | Category | Signal Word | H-Code | Note |
|-------------|----------|-------------|--------|------|
| Acute Toxicity (oral) | **3** | Danger | **H301** | Worst-case basis adopted for PSS per conservative convention (confirmed 2026-06-14) |
| Flammable Liquid | 4 | Warning | H227 | Combustible liquid |

> **Worst-case basis confirmed 2026-06-14**: H301 (Acute Tox 3 — toxic if swallowed, LD50 <300 mg/kg) adopted as the conservative working classification for this process safety study. H302 (the less conservative alternative) is superseded for PSS purposes. CAS 100-86-7 confirmed as the correct DMBA identity.

---

## Properties (CAS 100-86-7 surrogate)

| Property | Value | Source |
|----------|-------|--------|
| Physical state | Colourless liquid | SDS_100-86-7 |
| Boiling point | ~207°C (estimated) | SDS_100-86-7 |
| Flash point | ~98°C (closed cup, estimated) — combustible liquid | SDS_100-86-7 |
| LEL / UEL | Not well established | SDS_100-86-7 |
| Vapour pressure (20°C) | Very low (<0.01 kPa) | SDS_100-86-7 |
| TLV-TWA | Not established | SDS_100-86-7 |
| IDLH | Not established | SDS_100-86-7 |
| Odour | Faint aromatic / alcohol | SDS_100-86-7 |

---

## Health Hazards

### Acute Toxicity — H301 (Acute Tox 3, PSS worst-case basis)
- **H301: toxic if swallowed** (LD50 <300 mg/kg) — adopted as worst-case basis for this process safety study (confirmed 2026-06-14)
- Skin and eye: irritant; no significant dermal absorption reported
- Inhalation: low vapour pressure at ambient; risk limited to heated or atomised situations

---

## Fire and Explosion Hazards

- Flash point ~98°C — combustible liquid (Class IIIB); low fire risk at ambient temperatures
- High boiling point limits vapour generation; negligible flammable vapour hazard at ambient
- Firefighting: CO₂, dry chemical, foam, water spray

---

## Reactivity Hazards

| Incompatible With | Consequence |
|-----------------|------------|
| Strong acids (H₂SO₄) | **Acid-catalysed dehydration → α-Methylstyrene (AMS) + water** — critical process reaction |
| Strong bases | May catalyse ether formation |
| Strong oxidisers | Fire / explosion |

> ⚠️ **DMBA → AMS dehydration**: In the presence of the cleavage circuit acid (H₂SO₄), DMBA undergoes acid-catalysed dehydration to produce Alpha-Methylstyrene (AMS):
> ```
> C₆H₅CH₂C(CH₃)₂OH  →  C₆H₅C(CH₃)=CH₂ + H₂O     (acid-catalysed at cleavage T)
> ```
> This reaction contributes to AMS production in CDN. AMS carries polymerisation hazard — see [[hazards/alpha-methylstyrene]].

---

## Emergency Response

### Spill
1. Contain with inert absorbent
2. Collect in labelled closed containers for disposal
3. Prevent entry into drains

### Person Contaminated
1. Skin: wash with soap and water; remove contaminated clothing
2. Eyes: flush with water minimum 15 minutes; seek medical attention
3. **Ingestion: DO NOT induce vomiting** (aspiration and acute tox concern — apply H301 conservative precaution); seek medical attention immediately
4. Inhalation: move to fresh air; low vapour pressure limits risk at ambient

---

## PPE Requirements

| Task | Minimum PPE |
|------|------------|
| Routine rounds | Safety glasses, standard PPE |
| Sampling | Chemical-resistant gloves, safety glasses |
| Maintenance | Face shield, chemical-resistant gloves and apron |
| Emergency response | Chemical-resistant gloves, face shield; SCBA if heated material involved |

---

## PSS Confirmation Record (2026-06-14)

| Item | Resolution |
|------|-----------|
| CAS identity (100-86-7 vs 617-94-7) | ✅ Confirmed: CAS 100-86-7 (2-Methyl-1-phenyl-2-propanol) |
| Acute toxicity (H301 vs H302) | ✅ H301 adopted as worst-case PSS basis per conservative convention |

---

## Transport Classification

| Parameter | Value |
|-----------|-------|
| UN Number | Non-regulated at typical concentrations (combustible liquid — verify if H301 confirmed) |
| Note | If confirmed as H301 Acute Tox 3: may require Class 6.1 transport classification |

---

## References

- [[sources/SDS_100-86-7_dmba-dimethylbenzylcarbinol]] — plant GHS Safety Data Sheet (CAS 100-86-7 surrogate)
- [[units/cleavage]] — CDN section (DMBA accumulates in cleavage bottoms)
- [[units/distillation]] — DIST / acid aromatics (DMBA concentrated in heavy ends)
- [[hazards/alpha-methylstyrene]] — AMS (product of DMBA acid-catalysed dehydration)
- [[hazards/acetophenone]] — acetophenone (related heavy aromatic by-product)
