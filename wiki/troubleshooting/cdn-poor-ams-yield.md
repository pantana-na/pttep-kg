---
name: Poor AMS Yield in Decomposer
unit: CDN
tags: [troubleshooting, CDN, decomposition, AMS]
sources: [OM-Phenol Unit UOP-2015.pdf]
last_updated: 2026-06-13
---

# Troubleshooting: Poor AMS Yield in Decomposer

**Authority:** UOP General Operating Manual, Rev 8, Section IX — Troubleshooting.

---

## Symptoms

- AMS yield below target (target: ≥80 mole%)
- Low AMS concentration in crude product
- Calorimeter ΔTs out of expected range

---

## Probable Causes

| Cause | Likelihood | Check |
|-------|-----------|-------|
| Low CHP concentration in decomposer circulation loop | High | Laboratory analysis vs. calorimeter delta T. See [[procedures/emergency-cdn]] §B.3 for ΔT matrix |
| Excessive temperature or residence time in dehydrator effluent | Medium | DCP in crude product (target 300–700 wt ppm). If below 300 → too much conversion in dehydrator |
| Dehydrator temperature too high | Medium | Check dehydrator inlet/outlet temperature (target 125–145°C) |

---

## Diagnostic Steps

1. **Check laboratory analysis vs. calorimeter delta T values:**
   - Compare lab-measured CHP in circulating liquid with calorimeter 1st stage ΔT (~7–10°C at normal 1–1.5 wt% CHP).
   - If CHP is low: review calorimeter scenarios in [[procedures/emergency-cdn]].

2. **Check DCP in crude product:**
   - Target: 300–700 wt ppm (licensees achieve up to 900 wt ppm while meeting o-cresol spec).
   - If DCP < 300 wt ppm: too much DCP conversion in dehydrator — excessive temperature or residence time.
   - If DCP at target but AMS yield still low: investigate calorimeter-side chemistry.

3. **Review dehydrator operating conditions:**
   - Temperature range: 125–145°C.
   - Minimum: 120°C (below this, dehydration reaction rate insufficient to control DCP target).
   - If temperature is too high (>145°C): residue formation increases, DCP over-converted.

---

## Corrective Actions

### If Cause is Low CHP in Decomposer Loop

- Verify calorimeter ΔTs are in normal range (1st stage 7–10°C).
- Review H₂SO₄ injection rates — acid must be at 40–60 wt ppm in bulk.
- Review CHP concentration of flash column bottoms feed (must be ≥70 wt% for stable decomposition).
- See [[procedures/emergency-cdn]] §B.3 for the complete calorimeter diagnostic matrix.

### If Cause is Excessive Temperature/Residence Time in Dehydrator

- Reduce the dehydrator temperature, or reduce residence time (bypass expansion loop).
- **Do not decrease dehydrator temperature below 120°C** — conversion stops.
- Target DCP: 300–700 wt ppm in crude product.
- Monitor o-cresol in phenol product: sets upper DCP limit. UOP states 700–900 wt ppm DCP is achievable while still meeting o-cresol spec.

---

## Preventive Measures

- Maintain decomposer CHP within 1–1.5 wt% range (excessive CHP or very low CHP both indicate problems).
- Keep H₂SO₄ at 40–60 wt ppm — low acid = poor selectivity; too much acid = first stage ΔT loss.
- Monitor calorimeter ΔTs continuously; do not allow deviations to persist without investigation.
- Check laboratory analysis frequency per UOP recommendation (minimum daily for key CDN parameters).

---

## References

- [[sources/om-phenol-uop-2015]] — GOM §IX (primary source)
- [[parameters/cdn-operating-windows]] — Operating window table
- [[procedures/emergency-cdn]] — Calorimeter ΔT troubleshooting matrix
- [[equipment/D-2304]] — Decomposer Drum
- [[equipment/X-2308]] — Calorimeters
- [[units/cdn]]
