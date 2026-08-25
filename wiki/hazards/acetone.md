---
name: Acetone Hazard
tags: [hazard, acetone, cleavage, distillation]
sources: ["SDS_67-64-1_acetone.pdf"]
last_updated: 2026-06-14
---

# Hazard: Acetone (CH₃COCH₃)

> ⚠️ Acetone is a **highly flammable** liquid with a very low flash point (−20°C). Contact between acetone and concentrated CHP may form **shock-sensitive peroxide complexes** — keep acetone away from CHP-rich streams. Acetone is also a static accumulator — control static during transfer operations.

**Chemical formula**: CH₃COCH₃ (C₃H₆O)  
**Molecular weight**: 58.08 g/mol  
**CAS No.**: 67-64-1  
**Process section**: CDN (cleavage product), DIST (purification / distillation)  
**Source**: SDS_67-64-1_acetone.pdf

---

## GHS Classification (per SDS)

| Hazard Class | Category | Signal Word | H-Code |
|-------------|----------|-------------|--------|
| Flammable Liquid | 2 | Danger | H225 |
| Eye Irritation | 2A | Warning | H319 |
| Specific Target Organ Toxicity (SE) | 3 | Warning | H336 (CNS narcosis) |

---

## Properties

| Property | Value | Source |
|----------|-------|--------|
| Physical state | Colourless, volatile liquid | SDS_67-64-1 |
| Boiling point | 56.2°C | SDS_67-64-1 |
| Melting point | −95°C | SDS_67-64-1 |
| Flash point | −20°C (closed cup) — extremely flammable at all ambient temperatures | SDS_67-64-1 |
| Auto-ignition | 465°C | SDS_67-64-1 |
| LEL / UEL | 2.5% / 12.8% | SDS_67-64-1 |
| Vapour pressure (20°C) | 24.7 kPa — highly volatile | SDS_67-64-1 |
| Vapour density (air = 1) | 2.0 — heavier than air; collects in low-lying areas | SDS_67-64-1 |
| TLV-TWA (ACGIH) | 500 ppm (1188 mg/m³) | SDS_67-64-1 |
| TLV-STEL (ACGIH) | 750 ppm | SDS_67-64-1 |
| IDLH (NIOSH) | 2500 ppm | SDS_67-64-1 |
| Odour | Characteristic sweet/ketone; threshold ~20 ppm — provides good early warning | SDS_67-64-1 |
| Static accumulator | Yes — low conductivity; bonding and grounding required for transfers | SDS_67-64-1 |
| Water solubility | Miscible in all proportions | SDS_67-64-1 |

---

## Health Hazards

### Acute Effects
- H336 (STOT SE 3): narcotic effects — dizziness, headache, nausea, drowsiness at high concentrations
- Eye irritant (H319): causes irritation; flush with water if contact occurs
- High vapour concentrations: CNS depression, loss of consciousness (rare at typical process exposure levels)
- Low chronic toxicity — not classified as carcinogen or reproductive toxin at current evidence

### Skin
- Defatting agent — prolonged or repeated contact causes dermatitis
- Not absorbed significantly through skin at typical exposures

### Ingestion
- Moderate oral toxicity — causes GI irritation; unlikely to be fatal at small quantities
- Seek medical attention if large quantity ingested

---

## Fire and Explosion Hazards

- **Flash point −20°C** — fire hazard at ALL ambient temperatures; extremely flammable vapour
- Very volatile (BP 56.2°C) — high vapour generation rate in warm conditions
- Wide flammable range (2.5–12.8%) — significant fire/explosion envelope
- **Requires alcohol-resistant foam** for firefighting — standard foam dissolves in acetone (polar solvent)
- CO₂ or dry chemical for small fires; water spray for container cooling only
- Static accumulator: ground and bond all containers during transfer; use anti-static hoses

> ⚠️ **CHP interaction**: Contact between liquid acetone and concentrated Cumene Hydroperoxide (CHP) can generate shock-sensitive acetone peroxide (di- and tri-acetone peroxide). This is a **secondary hazard** — do not allow acetone to contaminate CHP streams or vice versa. Maintain strict flow segregation in CDN section. See [[hazards/cumene-hydroperoxide]].

---

## Reactivity Hazards

| Incompatible With | Consequence |
|-----------------|------------|
| Cumene Hydroperoxide (CHP) — concentrated | May form shock-sensitive acetone peroxide compounds |
| Strong oxidisers (HNO₃, H₂O₂, permanganate) | Fire / explosion |
| Strong acids or bases | May initiate aldol condensation (heat evolution) |
| Chloroform + bases | Forms chloroacetone (toxic lachrymator) |

---

## Emergency Response

### Spill
1. Evacuate area; eliminate all ignition sources (including static)
2. Prevent vapour accumulation in low-lying areas (vapour density 2.0)
3. Contain with inert absorbent; do NOT use paper or sawdust (fire risk)
4. Bond and ground recovery containers; use explosion-proof equipment

### Fire
1. **Use alcohol-resistant foam** — standard foam dissolves in acetone
2. CO₂ or dry chemical for small fires
3. Water spray to cool containers; withdraw if containers are engulfed

### Person Contaminated
1. Inhalation: move to fresh air; supplemental O₂ if breathing is difficult
2. Skin: wash with soap and water; remove contaminated clothing
3. Eyes: flush with water minimum 15 minutes; seek medical attention if irritation persists

---

## PPE Requirements

| Task | Minimum PPE |
|------|------------|
| Routine rounds | Safety glasses, standard PPE; gas monitor |
| Sampling | Chemical-resistant gloves, face shield; anti-static precautions |
| Maintenance / draining | Full face shield, chemical-resistant gloves, organic vapour respirator (if enclosed) |
| Emergency response | SCBA, chemical-resistant suit |

---

## Environmental Hazards

- Not classified for aquatic toxicity — highly biodegradable
- High COD/BOD load if released in large quantities to wastewater
- Route process drains to [[units/etp]]

---

## Transport Classification

| Parameter | Value |
|-----------|-------|
| UN Number | UN 1090 |
| Hazard Class | 3 (Flammable Liquid) |
| Packing Group | II |
| Proper Shipping Name | Acetone |

---

## References

- [[sources/SDS_67-64-1_acetone]] — plant GHS Safety Data Sheet
- [[units/cleavage]] — CDN section (acetone is primary cleavage product alongside phenol)
- [[units/distillation]] — DIST section (acetone is distilled and purified)
- [[hazards/cumene-hydroperoxide]] — interaction hazard: acetone + CHP peroxide formation risk
