---
name: Ethylene Glycol Hazard
tags: [hazard, ethylene-glycol, utilities, cooling]
sources: ["SDS_107-21-1_ethylene-glycol.pdf"]
last_updated: 2026-06-14
---

# Hazard: Ethylene Glycol (C₂H₆O₂)

> ⚠️ Ethylene glycol (EG) is used in CDN as a **heat-transfer coolant medium** (typically 80:20 EG/water mixture). It is harmful if ingested — toxicity arises from metabolic conversion to oxalic acid which causes acute kidney failure. The specific antidote is **fomepizole** (4-methylpyrazole).

**Chemical formula**: HOCH₂CH₂OH (C₂H₆O₂)  
**Molecular weight**: 62.07 g/mol  
**CAS No.**: 107-21-1  
**Process section**: UT (Utilities) / CDN cooling systems — heat-transfer fluid in CDN coolers  
**Source**: SDS_107-21-1_ethylene-glycol.pdf

---

## GHS Classification (per SDS)

| Hazard Class | Category | Signal Word | H-Code |
|-------------|----------|-------------|--------|
| Acute Toxicity (oral) | 4 | Warning | H302 |

> Ethylene glycol has a **relatively low GHS classification** — this should not lead to complacency. Ingestion of a modest dose (100–150 mL pure EG for an adult) can be fatal due to metabolic toxicity. Treat all EG exposure incidents seriously.

---

## Properties

| Property | Value | Source |
|----------|-------|--------|
| Physical state | Colourless, viscous, slightly sweet liquid | SDS_107-21-1 |
| Boiling point | 197°C | SDS_107-21-1 |
| Melting point | −13°C (pure) | SDS_107-21-1 |
| Freeze point (80:20 EG/water) | ~−42°C (approximate; confirm with vendor) | General |
| Flash point | 111°C (closed cup) — combustible liquid | SDS_107-21-1 |
| Auto-ignition | 400°C | SDS_107-21-1 |
| LEL / UEL | 3.2% / 53% (at elevated temperature) | SDS_107-21-1 |
| Vapour pressure (20°C) | 0.008 kPa (negligible at ambient) | SDS_107-21-1 |
| TLV-TWA (ACGIH) | 50 ppm (vapour); 10 mg/m³ (aerosol/mist) | SDS_107-21-1 |
| TLV-STEL | 150 ppm (vapour) | SDS_107-21-1 |
| IDLH | Not established | SDS_107-21-1 |
| Odour | Almost odourless at ambient temperature | SDS_107-21-1 |
| Water solubility | Fully miscible | SDS_107-21-1 |

---

## Health Hazards

### Ingestion — PRIMARY SYSTEMIC CONCERN
- H302 (Acute Tox 4): harmful if swallowed
- **Metabolic pathway**: EG → glycoaldehyde → glycolic acid → oxalic acid (via alcohol dehydrogenase)
- Oxalic acid precipitates calcium oxalate crystals in renal tubules → **acute kidney failure** (nephrotoxicity)
- Clinical progression: Phase 1 (0–12 h): apparent inebriation (CNS effects); Phase 2 (12–24 h): metabolic acidosis; Phase 3 (24–72 h): oliguric kidney failure
- **Antidote**: fomepizole (4-methylpyrazole, Antizol®) — competitive inhibitor of alcohol dehydrogenase; alternatively ethanol (emergency use); haemodialysis for severe cases
- Minimum lethal dose in adults: ~1–1.4 mL/kg body weight (~100 mL for an adult)

### Inhalation
- Low vapour pressure at ambient — vapour exposure is limited at normal temperatures
- Mist inhalation at elevated temperatures may cause respiratory irritation
- OEL applies mainly to heated process or aerosol situations

### Skin / Eye Contact
- Mild skin irritant on prolonged contact; not significantly absorbed through skin
- Eye irritant — flush with water if contact occurs

---

## Fire and Explosion Hazards

- Flash point 111°C — combustible liquid (Class IIIB); low fire risk at ambient temperatures
- Fire risk increases if EG is heated or atomised/sprayed
- Firefighting: CO₂, dry chemical, foam, water spray; water is compatible

---

## Reactivity Hazards

| Incompatible With | Consequence |
|-----------------|------------|
| Strong oxidisers | Fire / explosion |
| Strong acids (e.g., H₂SO₄) | Exothermic esterification |
| Strong bases | Reacts at elevated temperatures |

No significant incompatibility hazards in normal heat-exchanger service.

---

## Emergency Response

### Spill
1. Contain with absorbent material (sand, earth)
2. Collect in labelled containers for disposal
3. Do NOT discharge to drains or watercourses untreated — high BOD/COD

### Person Contaminated
1. **Ingestion**: This is the critical scenario — call Poison Control immediately; administer fomepizole or ethanol per medical protocol; arrange emergency hospital transfer
2. Inhalation: move to fresh air; symptoms resolve in fresh air for mist exposure
3. Skin: wash with soap and water; remove contaminated clothing
4. Eyes: flush with water minimum 15 minutes

---

## PPE Requirements

| Task | Minimum PPE |
|------|------------|
| Routine rounds near cooling system | Safety glasses, standard PPE |
| Maintenance / draining EG cooling circuits | Safety glasses, standard gloves |
| Emergency response | Standard PPE; chemical-resistant gloves |

---

## Environmental Hazards

- Not GHS-classified for aquatic toxicity — however, high BOD/COD load
- Biodegradable (aerobic); monitor receiving waterway if large spill occurs
- Route to [[units/etp]] for large-volume releases

---

## Transport Classification

| Parameter | Value |
|-----------|-------|
| UN Number | Not regulated (non-dangerous goods for most transport quantities) |
| Note | Concentrated EG may require transport declaration in some jurisdictions — verify |

---

## References

- [[sources/SDS_107-21-1_ethylene-glycol]] — plant GHS Safety Data Sheet
- [[units/cleavage]] — CDN section (EG cooling circuits for decomposer and pre-flash coolers)
- [[units/utilities]] — UT section (EG supply and make-up system)
