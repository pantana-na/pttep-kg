---
name: Dehydrator Plugging
unit: CDN
tags: [troubleshooting, CDN, decomposition, dehydrator, maintenance]
sources: [OM-Phenol Unit UOP-2015.pdf]
last_updated: 2026-06-13
---

# Troubleshooting: Frequent Plugging of Dehydrators

**Authority:** UOP General Operating Manual, Rev 8, Section IX — Troubleshooting.

---

## Symptoms

- Frequent dehydrator tube plugging requiring cleaning (typical cycle: 1–3 months)
- Increased maintenance frequency
- May be accompanied by low AMS yields
- Increased dehydrator ΔP
- Dehydrator outlet temperature cannot be maintained

---

## Probable Causes

| Cause | Likelihood | Check |
|-------|-----------|-------|
| Excessive temperature or residence time in dehydrator | High | Check DCP in crude product — if below 300 wt ppm, temperature/residence time is too high |
| Frequent startups causing elevated acid concentration and residue formation | High | Startup conditions use 300 wt ppm H₂SO₄ (vs. normal 40 wt ppm) — causes higher residue formation |
| Improper dehydrator cleaning procedure | Medium | Check cleaning method against recommended procedure |

---

## Diagnostic Steps

1. **Check dehydrator temperature and residence time:**
   - Normal temperature range: 125–145°C.
   - If DCP in crude product is below 300 wt ppm: dehydrator is converting too much DCP.
   - This also correlates with low AMS yield (see [[troubleshooting/cdn-poor-ams-yield]]).

2. **Count startup frequency:**
   - Each startup requires 300 wt ppm H₂SO₄ in decomposer → high acid causes residue formation in dehydrator.
   - If dehydrator plugging is frequent and correlated with frequent shutdowns/startups, the source of shutdowns must be eliminated.

3. **Check cleaning method and effectiveness:**
   - Has the correct cleaning procedure been used?

---

## Corrective Actions

### For Excessive Temperature/Residence Time

- Reduce dehydrator temperature or reduce residence time (bypass expansion loop).
- **Do not decrease dehydrator temperature below 120°C.**
- Target DCP: 300–700 wt ppm (ideally 300–900 wt ppm depending on o-cresol spec).
- See also [[troubleshooting/cdn-poor-ams-yield]].

### For Frequent Startups

- Minimize the frequency of CDN shutdowns by addressing root causes of shutdowns.
- Nothing can be done within the decomposition/dehydration section itself to counter residue formation from 300 wt ppm startup acid; the source of frequent shutdowns must be resolved.

### Dehydrator Cleaning Procedure

Approved cleaning methods (from GOM):
1. **Hydroblasting** — high-pressure water cleaning of tubes.
2. **Mechanical cleaning** — brush cleaning aided by water flushing.

Do not use methods that may damage the tube surfaces or leave contamination that accelerates future plugging.

---

## Preventive Measures

- Operate dehydrator within 125–145°C and aim for DCP in crude product at 300–700 wt ppm.
- Minimize unnecessary CDN shutdowns and startups.
- Establish a proactive cleaning schedule (before plugging becomes complete) rather than reactive cleaning.
- Monitor dehydrator ΔP as early indicator of tube fouling.

---

## References

- [[sources/om-phenol-uop-2015]] — GOM §IX (primary source)
- [[parameters/cdn-operating-windows]] — Dehydrator temperature limits
- [[troubleshooting/cdn-poor-ams-yield]] — Related troubleshooting (overlapping causes)
- [[units/cdn]]
