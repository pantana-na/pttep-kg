---
name: HAZOP Interlock/ESD Summary
tags: [hazop, interlock-esd-summary]
last_updated: 2026-06-17
---

# HAZOP Interlock/ESD Summary

> Cross-node rollup of every safeguard flagged IL/ESD = Yes during node analysis. Cross-check against [[wiki/instruments/cause-effect-cdn]] and [[wiki/instruments/sis-cdn]] — every SIS trip credited here should also appear there, and vice versa. Maintained by the HAZOP study engine ([`app/hazop/agent.py`](file:///usr/local/google/home/pantana/lab/Refinery-kg/app/hazop/agent.py)) as nodes are completed.
>
> **Status: PRELIMINARY — IL/ESD safeguards from the desktop first-passes of Nodes CDN-N02 ("Node 23-02", UC-2301 Causes 1/2/3) and CDN-N03 ("Node 23-03", UC-2301 Causes 6/8/9/10/11 + UC-2302 UXV-0802/0803). All cross-checked against [[wiki/instruments/cause-effect-cdn]]. Risk values are preliminary pending team confirmation.**

| Safeguard | Node | Possible Cause | Potential Consequence | Without Safeguard (L / P / En / Ec / S / RR) | With Existing Safeguard (L / P / En / Ec / S / RR) |
|-----------|------|-----------------|------------------------|-----------------------------------------------|------------------------------------------------------|
| **FXSLL-0401A/B/C** (2oo3, SIL 1) → UC-2301: close UXV-0401 feed + UXV-0501/0502 steam (C&E Cause 1) | CDN-N02 | Loss of oxidate feed (filter plug / OXI pump trip / UXV-0401) with steam on | Stagnant CHP overheats in E-2303 → decomposition → rupture, fire/explosion | 4 / 5 / 4 / 5 / 4 / Extreme | 2 / 5 / 4 / 5 / 4 / Medium |
| **TXSHH-0501** (1oo1, SIL 1) → UC-2301 Concentration ESD (C&E Cause 2) | CDN-N02 | E-2302A/B hot OXI recirculate over-temperature (preheat) | CHP over-temperature → decomposition → rupture, fire/explosion | 3 / 5 / 4 / 5 / 4 / High | 1 / 5 / 4 / 5 / 4 / Low |
| **TXSHH-0502A/B** (1oo2, SIL 1) → UC-2301: close UXV-0501/0502 SC1.5 steam (C&E Cause 3) | CDN-N02 | E-2303 steam control fails open (FIC-0501 / valve) | CHP over-temperature → decomposition → rupture, fire/explosion | 4 / 5 / 4 / 5 / 4 / Extreme | 2 / 5 / 4 / 5 / 4 / Medium |
| **UXV-0501 + UXV-0502** redundant series SC1.5 steam isolation (UC-2301 final elements) | CDN-N02 | Any UC-2301 demand (above causes) | Positive removal of heat source from CHP-containing oxidate | (final element — credited within FXSLL-0401 / TXSHH-0502 rows) | — |
| **LXSHH-0802** (1oo1) Flash Col bottom HH level → UC-2301: close UXV-0701-0706 + cross-trip UC-2302 (C&E Cause 6) | CDN-N03 | Loss of concentrated-CHP removal (P-2301 stop) with E-2304 heating | CHP accumulation + reboil → decomposition runaway → rupture, fire/explosion | 4 / 5 / 4 / 5 / 4 / Extreme | 2 / 5 / 4 / 5 / 4 / Medium |
| **TXSHH-0701A/0702A** (1oo2, SIL 2, time-delay A) vaporizer outlet HH temp → UC-2301 close UXV-0701-0706 (C&E Cause 8) | CDN-N03 | E-2304 SC3 steam control fails open | Concentrated CHP over-temperature → DIERS runaway → rupture, fire/explosion | 4 / 5 / 4 / 5 / 4 / Extreme | 2 / 5 / 4 / 5 / 4 / Medium |
| **TXSHH-0701B/0702B** (1oo2, immediate) vaporizer outlet HH temp → UC-2301 (C&E Cause 9) | CDN-N03 | E-2304 over-temperature (immediate-acting backup pair) | Concentrated CHP over-temperature → DIERS runaway → rupture, fire/explosion | 4 / 5 / 4 / 5 / 4 / Extreme | 2 / 5 / 4 / 5 / 4 / Medium |
| **TXSHH-0805A/B** (1oo2, SIL 2) Flash Col bottom HH temp → UC-2301 cuts SC3 steam (C&E Cause 10) | CDN-N03 | Flash Column bottom over-temperature | Concentrated CHP over-temperature → DIERS runaway → rupture, fire/explosion | 4 / 5 / 4 / 5 / 4 / Extreme | 2 / 5 / 4 / 5 / 4 / Medium |
| **TXSHH-0901A/B** (1oo2) bottoms-pump suction HH temp → UC-2301 ESD (C&E Cause 11) | CDN-N03 | Hot concentrated CHP at P-2301 suction (e.g. loss of E-2306 cooling) | Decomposition at pump/suction → LOPC, fire/explosion | 3 / 5 / 4 / 5 / 4 / High | 1 / 5 / 4 / 5 / 4 / Low |
| **UXV-0701-0706** (UC-2301 final elements) SC3 steam + vaporizer-area isolation | CDN-N03 | Any UC-2301 demand (Causes 6/8/9/10/11) | Positive removal of reboiler heat source from concentrated CHP | (final element — credited within Cause 6/8/9/10 rows) | — |
| **UXV-0802/0803** (UC-2302 final elements) Flash Col bottoms-to-Decomposer isolation | CDN-N03 | UC-2302 trip / reverse-flow demand (#3.1) | Isolate concentrated CHP feed to Decomposer; backs up reverse-flow protection | (final element — credited within reverse-flow #3.1.1 row) | — |

## References
- [[wiki/hazop/study-info]] — node status register
- [[wiki/instruments/cause-effect-cdn]], [[wiki/instruments/sis-cdn]] — SIS data to cross-check against
- [`app/hazop/agent.py`](file:///usr/local/google/home/pantana/lab/Refinery-kg/app/hazop/agent.py) — HAZOP facilitator engine
