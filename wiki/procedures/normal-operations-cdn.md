---
name: CDN Normal Operations
type: Normal
unit: CDN
tags: [procedure, normal, CDN, concentration, decomposition, neutralization]
sources: [OM-Phenol Unit UOP-2015.pdf]
last_updated: 2026-06-13
---

# CDN Normal Operations

> ⚠️ CHP is a peroxide — thermal decomposition risk. See [[hazards/cumene-hydroperoxide]].

**Authority:** UOP General Operating Manual, Rev 8, Section VII — Normal Operations.

---

## Scope

Daily operation guidance for the CDN section:
- **2. Concentration** — Flash column operation and vacuum system
- **3. Decomposition** — Temperature, acid, calorimeter, and dehydrator management
- **4. Neutralization** — pH control and diamine injection

---

## A. Concentration Section Normal Operations

**Primary objective:** Produce concentrated CHP (80–84 wt%) at the safest possible conditions — minimum temperature while maintaining product specification.

### Flash Column Operating Philosophy

1. **Temperature is the primary safety variable.** The safer the operation, the lower the temperature at which CHP can be concentrated. Target the lowest flash zone temperature that achieves the 80–84 wt% CHP target at the flash column bottoms.

2. **CHP in recycle cumene overhead target:** <4 wt% (design target); <1 wt% consistently demonstrated in existing units at design rates. Operate at least at the design reflux flow rate (not excessive) to maintain this specification.
   - Excess CHP in recycle cumene impacts yields at high concentrations.

3. **Key parameters to monitor daily** (data collection list from GOM §VII.2.1):

| Parameter | Tag Type | Purpose |
|-----------|----------|---------|
| Preflash column feed filter ΔP | — | Filter fouling detection |
| Preflash column feed temperature | TI | Feed heat balance |
| Preflash column feed flow rate | FI | Feed rate control |
| Preflash column flash zone pressure | PI | Vacuum control |
| Flash column flash zone pressure | PI | Vacuum depth |
| Flash column bottoms CHP concentration | AI | Product quality |
| Flash column bottoms temperature | TI | Safety monitoring |
| Flash column bottoms level | LI | Inventory control |
| CHP nitrogen to vacuum system flow rate | FI | Inert blanket |
| Concentration cumene quench drum level | LI | Emergency quench readiness |

### Vacuum System Operating Notes

UOP ejectors operate only over a limited range. Key sensitivities:
- Steam pressure must be maintained close to design. Excess pressure → steam backs into suction header.
- Wet steam → random fluctuation + nozzle/diffuser erosion.
- Discharge pressure above design → reverse flow risk.
- Increased vapor load above design → vacuum falls off sharply.
- Higher inter-condenser temperature → reduces ejector capacity significantly.

For liquid ring vacuum pump operation: refer to vendor instructions.

### Performance Evaluation

Monitor flash column bottoms CHP concentration versus target (80–84 wt%). If CHP is below target, heat duty to the flash column vaporizer may be insufficient, or vacuum may not be deep enough.

[Source: OM-Phenol Unit UOP-2015.pdf, §VII.2, UOP licensor]

---

## B. Decomposition Section Normal Operations

**Primary objective:** Efficiently and safely decompose concentrated CHP into phenol and acetone at highest AMS yield, minimizing by-products.

> UOP statement (GOM §VII.3): "Deviations from design operational parameters are strongly discouraged. The operating conditions in the decomposer and dehydrator are such as to operate essentially on the limit of the reaction chemistry involved."

### Target Operating Conditions

| Parameter | Normal Target | Limit | Unit | Notes |
|-----------|--------------|-------|------|-------|
| Decomposer temperature | 60 | Do not exceed without reason | °C | |
| Decomposer pressure | 0.70 | — | kg/cm²(g) | |
| H₂SO₄ in circulating liquid | 40 | Min 20 before action needed | wt ppm | |
| CHP in circulating liquid | 1–1.5 | >2 → instability | wt% | |
| Calorimeter 1st stage ΔT | 7–10 | — | °C | Cross-check CHP level |
| Crude product DCP | 300–700 | Max 900 (limited by o-cresol) | wt ppm | |
| Dehydrator temperature | 125–145 | Min 120°C | °C | Below 120 = slow conversion |

**AMS yield expectation:** ≥80 mole% achievable under above conditions.

### Instability Warning Signs

Two conditions cause reaction instability — **do not allow either**:
1. CHP in circulating liquid >1.5 wt% → temperature control oscillates, may become unstable → risk of sudden CHP concentration increase
2. Water concentration in crude product >2 wt% → same instability risk

### Temperature Management (TIC)

- Normal target: 60°C. Controlled by TIC via split-range cooling water valves on [[equipment/E-2307]] (Decomposer Cooler).
- Do NOT try to optimize by running closer to instability limits. The design is already at the chemical limit.

### Acid Injection Management

- Normal range: 40–60 wt ppm in bulk circulating liquid.
- H₂SO₄ injection goes to: (1) bulk circulating liquid, (2) Calorimeter 1, (3) Calorimeter 2.
- Monitor flow rates to all three injection points independently — loss of one must be compensated by increasing bulk injection.
- Laboratory verification of acid concentration required regularly (do not rely on flow meters alone).

### Calorimeter Monitoring (Daily)

Monitor both calorimeters independently. Normal pattern for both calorimeters:
- 1st stage ΔT (inlet): 7–10°C (proportional to CHP concentration in circulating liquid)
- 2nd stage ΔT (outlet): varies based on DCP
- Total ΔT: sum of both stages

Any anomalous ΔT reading must be investigated immediately. See [[procedures/emergency-cdn]] for the 11-scenario ΔT troubleshooting matrix.

### Dehydrator Management

- Target outlet temperature: 125–145°C.
- Minimum: 120°C. Below this → DCP conversion slows → poor AMS yield.
- Monitor DCP in crude product by laboratory analysis. Target 300–700 wt ppm (licensees demonstrate up to 900 wt ppm while still meeting o-cresol specification).
- Higher DCP → higher AMS yield, but increases o-cresol in phenol product. Find optimum within specification.
- Dehydrator expansion loop can increase residence time if needed; but temperature control takes priority.

### Water Injection

- Normal target: 1–2 wt% water in circulating liquid.
- Water injection rate adjusted to maintain this.
- Do NOT allow water >2 wt% — reaction inhibition risk.

### Key Parameters to Monitor Daily (from GOM §VII.3.1)

| Parameter | Tag |
|-----------|-----|
| Decomposer feed flow rate | FI |
| Decomposer temperature | TI |
| Decomposer level | LI |
| Decomposer pressure | PI |
| Decomposer circulation flow rate | FI |
| Decomposer cooler ΔP | PDI |
| Calorimeter 1 flow rate | FI |
| Calorimeter 1 1st stage ΔT | TDI |
| Calorimeter 1 2nd stage ΔT | TDI |
| Calorimeter 1 total ΔT | TDI |
| Calorimeter 2 flow rate | FI |
| Calorimeter 2 1st stage ΔT | TDI |
| Calorimeter 2 total ΔT | TDI |
| H₂SO₄ injection to bulk | FI |
| H₂SO₄ injection to Cal 1 | FI |
| H₂SO₄ injection to Cal 2 | FI |
| Dehydrator inlet/outlet temperature | TI |
| Dehydrator ΔP | PDI |
| Water injection rate | FI |
| Crude product temperature | TI |

[Source: OM-Phenol Unit UOP-2015.pdf, §VII.3, UOP licensor]

---

## C. Neutralization Section Normal Operations

**Primary objective:** Remove H₂SO₄ from crude product to pH 2.3–2.7 (suitable for fractionation without corrosion or yield loss).

### Operating Philosophy

Optimization of neutralization is primarily economic — minimize diamine injection while achieving pH 2.3–2.7. The ratio controller (diamine:crude product flow) should maintain pH within range.

### pH Control

- Target: pH 2.3–2.7 in crude product
- Use ratio controller (diamine injection to crude product flow) as primary control
- Adjust ratio based on regular laboratory analysis of crude product pH
- Field pH transmitter calibration: check regularly

### Daily Data Collection (from GOM §VII.4)

| Parameter | Purpose |
|-----------|---------|
| Diamine injection flow rate | Injection rate verification |
| Combined crude product and sprung phenol temperature | Feed condition |
| Static mixer ΔP | Fouling detection |
| Neutralized crude product H₂SO₄ concentration | Quality check |

### Notes

- If pH cannot be maintained: stop CDN feed, put oxidation section on long recycle. Do not send un-neutralized crude product to fractionation.
- High static mixer ΔP: sodium sulfate carryover fouling — see [[troubleshooting/cdn-static-mixer-fouling]].

[Source: OM-Phenol Unit UOP-2015.pdf, §VII.4, UOP licensor]

---

## D. CHP Sampling Procedure Note

CHP-containing streams cannot be sampled in a closed container (CHP continues to react, skewing analysis).

**Procedure:** "Freeze" the sample by adding a neutralizing agent to the sample container before collection:
- Approved agents: NaOH solutions, soda ash, sodium bicarbonate, HMDA (Hexamethylenediamine), Dytek A (2-MPMD)
- Add sufficient agent to neutralize all acid in the sample

Use open-style flow-through sampling system for CHP streams (GOM §VIII — Analytical).

---

## References

- [[sources/om-phenol-uop-2015]] — UOP GOM §VII (primary source)
- [[parameters/cdn-operating-windows]] — Operating limits
- [[units/cdn]]
- [[equipment/D-2304]] — Decomposer Drum
- [[equipment/E-2307]] — Decomposer Cooler
- [[equipment/X-2308]] — Calorimeters
- [[equipment/V-2301]] — Flash Column (V-2301 = Preflash; V-2302 = Flash)
- [[procedures/emergency-cdn]] — Emergency reference
- [[hazards/cumene-hydroperoxide]]
