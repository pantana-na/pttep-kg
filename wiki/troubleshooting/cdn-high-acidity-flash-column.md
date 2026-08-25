---
name: High Acidity in Flash Column Bottoms
unit: CDN
tags: [troubleshooting, CDN, concentration, acidity]
sources: [OM-Phenol Unit UOP-2015.pdf]
last_updated: 2026-06-13
---

# Troubleshooting: High Acidity in Flash Column Bottoms

**Authority:** UOP General Operating Manual, Rev 8, Section IX — Troubleshooting.

---

## Symptoms

- High acid (H₂SO₄ or organic acid) concentration in flash column bottoms (concentrated CHP)
- Acid breakthrough to fractionation feed tank
- Abnormal pH in crude product (below 2.3 despite diamine injection)

---

## Probable Causes

| Cause | Likelihood | Check |
|-------|-----------|-------|
| High acidity in terminal oxidizer concentrating in flash column bottoms | High | Check terminal oxidizer for acidity issues |
| High DMPC concentration in oxidizer (low spent air O₂) causing organic acid formation | Medium | Check spent air O₂ concentration |
| Decomposer acid breakthrough during extended startup periods | Medium | Check if startup condition is prolonged |
| Insufficient diamine injection at neutralization | Low | Check diamine rate and pH |

---

## Diagnostic Steps

1. **Check terminal oxidizer acidity:**
   - High acidity in the oxidizer feed concentrates through the preflash and flash columns since acid does not evaporate.
   - Check the feed wash column (CWC) performance — aqueous bottoms should be pH ~14 with free caustic 1–1.5 wt%.

2. **Check spent air O₂ concentration:**
   - High DMPC formation in the oxidizer (spent air O₂ < 5 vol%) leads to higher organic acid formation.
   - Increase air flow rate or decrease oxidizer temperature to bring spent air O₂ back to 5–7 vol%.

3. **Check for startup-period acid breakthrough:**
   - During startup, H₂SO₄ concentration in decomposer is 300 wt ppm.
   - This higher acid level can break through to fractionation feed tank — this is normal if startup period is short.
   - If startup is prolonged: review why unit cannot be brought to normal acid level (40 wt ppm).

4. **Check diamine injection:**
   - Confirm diamine injection pump is functioning and dosing correctly.
   - Target pH 2.3–2.7 in crude product.
   - Do not dilute crude product in water when analyzing pH (will give false reading).

---

## Corrective Actions

### For Oxidizer Acidity
- Improve feed wash column (CWC) operation to reduce organic acids and phenol in cumene feed.
- Check CWC aqueous phase pH (should be ~14) and free caustic (1–1.5 wt%).
- Check for cooling water leak into oxidizers (dedicated cooling tower water should be checked for organics).

### For Low Spent Air O₂ / High DMPC
- Either increase air flow rate or decrease oxidizer temperature to reduce DMPC formation while maintaining CHP production balance.

### For Diamine Injection
- Increase diamine injection rate to achieve target pH.
- Calibrate field pH transmitter.

---

## Preventive Measures

- Maintain oxidizer feed wash column at proper pH and caustic concentration.
- Keep spent air O₂ within 5–7 vol% to minimize organic acid byproduct formation.
- Monitor flash column bottoms acidity as part of daily laboratory analysis routine.
- Minimize startup duration to avoid extended 300 wt ppm acid level in decomposer.

---

## References

- [[sources/om-phenol-uop-2015]] — GOM §IX (primary source)
- [[parameters/cdn-operating-windows]] — H₂SO₄ operating limits
- [[units/cdn]]
- [[equipment/V-2301]] — Flash Column (Preflash)
- [[equipment/V-2302]] — Flash Column
