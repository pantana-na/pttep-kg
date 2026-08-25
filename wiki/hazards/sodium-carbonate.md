---
name: Sodium Carbonate Solution Hazard
tags: [hazard, sodium-carbonate, cdn, neutralization]
sources: ["SDS_497-19-8_sodium-carbonate-solution.pdf"]
last_updated: 2026-06-14
---

# Hazard: Sodium Carbonate Solution (Na₂CO₃)

> ⚠️ Sodium carbonate reacts with acid (H₂SO₄) to produce **CO₂ gas** — do NOT perform neutralisation with Na₂CO₃ in closed vessels (CO₂ over-pressure). Segregate Na₂CO₃ storage from H₂SO₄ acid storage and from CHP-containing streams (carbonates may catalyse CHP decomposition at elevated pH).

**Chemical formula**: Na₂CO₃ (anhydrous); Na₂CO₃·aq (as solution)  
**Molecular weight**: 105.99 g/mol (anhydrous)  
**CAS No.**: 497-19-8  
**Common name**: Soda ash (anhydrous); Washing soda; Sodium carbonate solution  
**Process section**: CDN — Neutralisation (X-2310A/B); used to neutralise acid aromatics / residual H₂SO₄ in product streams  
**Source**: SDS_497-19-8_sodium-carbonate-solution.pdf

---

## GHS Classification (per SDS — aqueous solution)

| Hazard Class | Category | Signal Word | H-Code |
|-------------|----------|-------------|--------|
| Eye Irritation | 2A | Warning | H319 |

> Sodium carbonate solution has a **low GHS hazard classification**. This reflects intrinsic chemical toxicity only — the process interaction hazards (CO₂ generation with acid; CHP sensitivity to alkaline pH) are the primary process safety concerns. See Reactivity Hazards section.

---

## Properties

| Property | Value | Source |
|----------|-------|--------|
| Physical state | Colourless/white solution (pH ~11.6 at 10 wt%) | SDS_497-19-8 |
| Flash point | Not applicable — non-flammable | SDS_497-19-8 |
| LEL / UEL | Not applicable | SDS_497-19-8 |
| Density (10 wt% solution) | ~1.10 g/mL | SDS_497-19-8 |
| pH (10 wt% solution) | ~11.6 (alkaline — mild caustic hazard for skin/eyes) | SDS_497-19-8 |
| TLV-TWA (ACGIH, dust) | 10 mg/m³ (inhalable fraction) | SDS_497-19-8 |
| IDLH | Not established | SDS_497-19-8 |
| Odour | Odourless | SDS_497-19-8 |

---

## Health Hazards

### Eye Contact — PRIMARY CONCERN (for the solution)
- H319 (Eye Irrit 2A): causes serious eye irritation
- Alkaline solution (pH ~11.6) is mildly caustic — can cause irritation and delayed chemical conjunctivitis
- Flush with water immediately for minimum 15 minutes; seek medical attention

### Skin Contact
- Mild alkaline irritant on prolonged or repeated contact; dermatitis possible
- Flush with water; not a significant systemic toxin through skin

### Inhalation (dust/aerosol)
- Na₂CO₃ dust or fine aerosol is a respiratory irritant
- Process solution is low-volatility — inhalation risk mainly during dry handling or high-pressure spray

### Ingestion
- Mildly toxic — causes GI irritation; not expected to be fatal from typical exposures
- Seek medical attention if large quantity ingested

---

## Fire and Explosion Hazards

- **Non-flammable** — sodium carbonate does not burn
- No fire hazard from the compound itself
- However: reaction with H₂SO₄ generates CO₂ — builds pressure in closed systems

---

## Reactivity Hazards

| Incompatible With | Consequence |
|-----------------|------------|
| Sulfuric acid (H₂SO₄) | Neutralisation reaction: Na₂CO₃ + H₂SO₄ → Na₂SO₄ + H₂O + **CO₂↑** — CO₂ generation creates pressure in closed vessels; violent in concentrated systems |
| Concentrated CHP (alkaline pH) | Alkaline pH may catalyse CHP decomposition — maintain tight pH control in CDN neutralisation |
| Aluminium (reactive metal) | H₂ evolution (high pH) |

> ⚠️ **CO₂ pressure hazard**: The neutralisation of H₂SO₄ with Na₂CO₃ in the CDN Neutralization section (X-2310A/B) generates CO₂. Vessels or enclosed piping in this service must be designed for CO₂ pressure, or vented. Confirm equipment design with process data sheets when available.

> ⚠️ **CHP sensitivity**: Alkaline species (Na₂CO₃, NaOH, amines) can catalyse CHP decomposition at elevated temperature. Ensure no Na₂CO₃ solution backflows into CHP-containing streams. Maintain flow direction and check valve integrity in neutralisation circuit.

> ⚠️ **Storage segregation**: Segregate Na₂CO₃ solution storage from concentrated H₂SO₄ storage. If vessels or piping breach, accidental mixing generates CO₂ and heat — potential for rapid pressure rise in any enclosed space.

---

## Emergency Response

### Spill
1. For small spills: flush with large volumes of water
2. For large spills: contain; prevent entry into drains (high pH — may need neutralisation)
3. High-alkaline wastewater to [[units/etp]] for pH adjustment before discharge

### Person Contaminated
1. **Eyes**: Flush immediately with large volumes of water minimum 15 minutes; seek medical attention — alkaline injury can be delayed
2. Skin: Flush with water; remove contaminated clothing
3. Inhalation (dust): Move to fresh air; symptoms resolve; medical attention if respiratory symptoms persist
4. Ingestion: Seek medical attention; do not induce vomiting; give water to dilute

---

## PPE Requirements

| Task | Minimum PPE |
|------|------------|
| Routine rounds | Safety glasses, standard PPE |
| Sampling / connection to Na₂CO₃ lines | Safety glasses, chemical-resistant gloves |
| Maintenance (pump/valve work) | Full face shield, chemical-resistant gloves and apron |
| Emergency response | Face shield, chemical-resistant gloves |

---

## Environmental Hazards

- Not GHS-classified for aquatic toxicity
- Alkaline pH: high pH wastewater is toxic to aquatic life; neutralise before discharge
- Comply with Thai DIW effluent pH limits (typically 5.5–9.0)

---

## Transport Classification

| Parameter | Value |
|-----------|-------|
| UN Number | Not regulated as dangerous goods (dilute solution — confirm concentration) |
| Note | Concentrated Na₂CO₃ solution may require Class 8 (corrosive) labelling at very high concentrations |

---

## References

- [[sources/SDS_497-19-8_sodium-carbonate-solution]] — plant GHS Safety Data Sheet
- [[units/cleavage]] — CDN section (neutralisation of acid aromatics)
- [[hazards/sulfuric-acid]] — H₂SO₄ (incompatible — CO₂ generation on contact); segregate storage
- [[hazards/cumene-hydroperoxide]] — CHP (alkaline pH hazard — CHP sensitivity to base catalysis)
- [[instruments/cause-effect-cdn]] — pH control alarms in neutralisation circuit (X-2310A/B)
