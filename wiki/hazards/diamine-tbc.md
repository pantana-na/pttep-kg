---
name: Diisopropanolamine (DIPA) — CDN Neutralisation Additive
tags: [hazard, dipa, diamine, cdn, neutralization, conflict]
sources: ["SDS_110-97-4_dipa-placeholder-diamine-tbc.pdf", "14780-8120-PS-D2312_Z1.pdf"]
last_updated: 2026-06-16
---

# Hazard: Diisopropanolamine / DIPA (C₆H₁₅NO₂)

> ⛔ **IDENTITY CONFLICT REOPENED (2026-06-16) — DO NOT USE THIS PAGE AS HAZOP SAFETY BASIS UNTIL RESOLVED.** The "confirmed" identity below was matched 2026-06-14 from an SDS whose own filename contains "placeholder" (`SDS_110-97-4_dipa-placeholder-diamine-tbc.pdf`). The AS-BUILT Process Data Sheet for [[equipment/D-2312]] (PS-D2312 Rev Z1, an authoritative engineering document, ingested 2026-06-16) explicitly states the fluid name as **"DIAMINE(HMDA)"** = **Hexamethylenediamine, CAS 124-09-4** — a primary diamine, chemically distinct from DIPA (a secondary alkanolamine). Density check supports HMDA over DIPA: DS records 914 kg/m³, which is far from DIPA's ~1010 kg/m³ but consistent with HMDA. Per the Standards Primacy Rule, the engineering data sheet outranks a placeholder-named SDS. **Action required: obtain a genuine plant SDS for hexamethylenediamine and re-verify before this page or any D-2312/P-2306A/B/X-2310A/B HAZOP deviation is finalized.** All hazard data below is retained for reference only and must not be treated as validated until identity is settled.
>
> **Identity confirmed 2026-06-14 (now disputed)**: The CDN neutralisation additive (equipment tags D-2312, P-2306A/B, X-2310A/B) is confirmed as **Diisopropanolamine (DIPA), CAS 110-97-4**. Plant equipment documentation refers to this additive as "Diamine". This page replaces the previous PLACEHOLDER entry.

**Chemical formula**: [CH₃CH(OH)CH₂]₂NH (C₆H₁₅NO₂)  
**IUPAC name**: Bis(2-hydroxypropyl)amine  
**Molecular weight**: 133.19 g/mol  
**CAS No.**: 110-97-4  
**Synonyms**: DIPA; Diisopropanolamine; N-methyldiethanolamine variant (secondary alkanolamine)  
**Process section**: CDN — Neutralisation circuit (D-2312 storage → P-2306A/B pumps → X-2310A/B static mixers)  
**Source**: SDS_110-97-4_dipa-placeholder-diamine-tbc.pdf [Confirmed 2026-06-14]

---

## GHS Classification (per SDS — confirmed identity)

| Hazard Class | Category | Signal Word | H-Code |
|-------------|----------|-------------|--------|
| Acute Toxicity (oral) | 5 | Warning | H303 |
| Eye Irritation | 2A | Warning | H319 |
| Specific Target Organ Toxicity (RE) | 2 | Warning | H373 |

---

## Properties

| Property | Value | Source |
|----------|-------|--------|
| Physical state | Colourless to pale yellow viscous liquid or solid | SDS_110-97-4 |
| Boiling point | ~248°C | SDS_110-97-4 |
| Melting point | ~44°C (may solidify near ambient — check heat tracing requirements for transfer lines) | SDS_110-97-4 |
| Flash point | ~127°C (closed cup) — combustible liquid | SDS_110-97-4 |
| LEL / UEL | Not well established; low vapour pressure limits vapour hazard at ambient | SDS_110-97-4 |
| Vapour pressure (20°C) | Very low (<0.001 kPa) | SDS_110-97-4 |
| Density | ~1.01 g/mL | SDS_110-97-4 |
| pH (10 wt% solution) | ~11 (alkaline — amine base) | SDS_110-97-4 |
| TLV-TWA | Not established for DIPA (ACGIH) | SDS_110-97-4 |
| IDLH | Not established | SDS_110-97-4 |
| Odour | Faint amine odour | SDS_110-97-4 |

---

## Health Hazards

### Eye Contact — PRIMARY CONCERN
- H319 (Eye Irrit 2A): causes serious eye irritation — alkaline amine is a contact hazard for eyes
- Flush with water immediately for minimum 15 minutes; seek medical attention

### Skin Contact
- Mildly alkaline; prolonged or repeated contact may cause skin irritation or sensitisation
- Remove contaminated clothing; wash with soap and water
- Amine sensitisation potential: monitor for any skin reaction after first exposure; report to occupational health

### Inhalation
- Low vapour pressure at ambient — inhalation risk mainly from heated material, mist, or aerosol
- Amine odour provides some warning
- STOT RE 2 (H373): possible organ damage from repeated/prolonged exposure — apply ALARA principle

### Ingestion
- H303 (Acute Tox 5): may be harmful if swallowed in large quantities
- Seek medical attention; do not induce vomiting

---

## Fire and Explosion Hazards

- Flash point ~127°C — combustible liquid (Class IIIB); negligible fire hazard at ambient temperatures
- High boiling point; low vapour pressure — vapour ignition hazard is limited
- Firefighting: CO₂, dry chemical, water spray, foam

---

## Reactivity Hazards

| Incompatible With | Consequence |
|-----------------|------------|
| Strong acids (H₂SO₄) | Exothermic neutralisation — forms salt (diisopropanolamine sulfate) |
| CHP (concentrated) | **Alkaline amines can catalyse CHP decomposition** — maintain acid/base balance in cleavage circuit; prevent DIPA backflow into CHP streams |
| Strong oxidisers | Fire / explosion |
| Reactive halides | Exothermic reaction |

> ⚠️ **CHP interaction**: DIPA is an alkaline amine base (pH ~11 in solution). If DIPA contacts concentrated CHP (e.g., via backflow in X-2310A/B or D-2312 spill), it can catalyse CHP decomposition. Check valve integrity and flow direction interlocks in the neutralisation circuit. See [[hazards/cumene-hydroperoxide]] and [[instruments/cause-effect-cdn]].

> ⚠️ **H₂SO₄ neutralisation function**: DIPA reacts with residual H₂SO₄ in the crude product from D-2304 to form DIPA sulfate salts (water-soluble). This is the intended process function. Maintain correct DIPA injection ratio per [[parameters/cdn-operating-windows]] to avoid under-neutralisation (acid carry-over to fractionation) or over-neutralisation (excess base affecting downstream chemistry).

---

## Functional Role in CDN

| Equipment | Function |
|----------|----------|
| D-2312 | DIPA storage/injection day tank (1300×1300mm; 0.01/40°C operating; LC-1901; PCV-1909 vent) |
| P-2306A/B | DIPA metering pumps (6.65 L/hr each; ratio-controlled; FT-1903 Coriolis flow meter) |
| X-2310A/B | Direct neutralisation static mixers — DIPA injected into crude product stream (4.4°C / 43°C operating) |
| AT-1901 | Acid analyser at X-2310 inlet — monitors pH/acidity of crude product entering neutralisation |

DIPA injection is ratio-controlled (XC-2306) against crude product flow to maintain target neutralisation. FT-1903 Coriolis flow meter provides injection rate feedback. See [[instruments/cause-effect-cdn]] for alarms.

---

## Emergency Response

### Spill
1. Contain with inert absorbent; collect in labelled closed containers
2. Prevent entry into drains — high pH wastewater; neutralise or route to [[units/etp]]

### Person Contaminated
1. **Eyes**: Flush immediately with large volumes of water minimum 15 minutes; seek medical attention — alkaline amine burns can be delayed
2. Skin: Flush with water; remove contaminated clothing; watch for delayed sensitisation response
3. Inhalation: Move to fresh air; seek medical attention if symptoms persist
4. Ingestion: Seek medical attention; do not induce vomiting

---

## PPE Requirements

| Task | Minimum PPE |
|------|------------|
| Routine rounds | Safety glasses, standard PPE |
| Sampling / connection operations | Chemical-resistant gloves, face shield |
| Maintenance (D-2312/P-2306/X-2310) | Full face shield, chemical-resistant gloves and apron |
| Emergency response | Face shield, chemical-resistant gloves; SCBA if heated/aerosolised material |

---

## Environmental Hazards

- Not GHS-classified for aquatic toxicity at SDS concentration
- Alkaline pH — route to [[units/etp]] for pH normalisation before discharge
- DIPA is biodegradable under aerobic conditions

---

## Transport Classification

| Parameter | Value |
|-----------|-------|
| UN Number | Not regulated as dangerous goods (at process-use concentrations — verify) |

---

## References

- [[sources/SDS_110-97-4_dipa-placeholder-diamine-tbc]] — confirmed plant GHS Safety Data Sheet (DIPA, CAS 110-97-4)
- [[units/cleavage]] — CDN section (DIPA injection in neutralisation node)
- [[hazards/cumene-hydroperoxide]] — CHP (amine + CHP interaction hazard)
- [[hazards/sulfuric-acid]] — H₂SO₄ (neutralised by DIPA injection at X-2310A/B)
- [[instruments/cause-effect-cdn]] — pH control and neutralisation alarms (AT-1901, XC-2306)
- [[equipment/D-2312]] — DIPA injection tank
- [[equipment/P-2306AB]] — DIPA metering pumps
- [[equipment/X-2310AB]] — direct neutralisation static mixers
