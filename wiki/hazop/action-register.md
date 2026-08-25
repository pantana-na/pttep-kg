---
name: HAZOP Action Register
tags: [hazop, action-register]
last_updated: 2026-06-17
---

# HAZOP Action Register

> All recommendations generated during HAZOP study. Update status as actions are closed.
>
> **Status: PRELIMINARY — 9 recommendations from desktop first-passes of Nodes CDN-N02 (R-001–R-004, "Node 23-02") and CDN-N03 (R-005–R-009, "Node 23-03"). Subject to HAZOP team confirmation; node boundaries not yet engineer-confirmed.**

| Rec# | Node ID | Deviation | Recommendation | Risk Rank | Discipline | Owner Type | Owner (Emp ID / Name or External Party) | Due Date | Action Approver | Completion Date | Approved Date | Status |
|------|---------|-----------|----------------|-----------|-----------|------------|-------------------------------------------|----------|-----------------|------------------|----------------|--------|
| R-001 | CDN-N02 | Temperature — More / Flow — No (overheat) | LOPA / SIF verification of combined overheat protection (TXSHH-0501 + TXSHH-0502A/B SIL 1 + UXV-0501/0502) for the S5 CHP-decomposition consequence; confirm setpoints below 80 °C onset with margin; confirm startup bypass HXS-0102 does not disable temp protection. | Medium | Instrument / Process | TBD | TBD | TBD | TBD | — | — | Open |
| R-002 | CDN-N02 | Composition — Tube Leak (E-2303) | Provide on-line CHP/hydrocarbon detection (conductivity/pH or HC analyzer + alarm/divert) on D-2308 / steam-condensate return to detect an E-2303 tube leak and prevent CHP migration to the unrated utility condensate system. | High | Process / Instrument | TBD | TBD | TBD | TBD | — | — | Open |
| R-003 | CDN-N02 | Pressure — More (block-isolated) | Review overpressure/thermal-relief protection for E-2302A/B and E-2303 process (CHP) side when block-isolated for maintenance (no dedicated PSV once isolated from V-2301 relief); confirm safe CHP drain/purge for single-train isolation. | Medium | Process / Mechanical | TBD | TBD | TBD | TBD | — | — | Open |
| R-004 | CDN-N02 | Pressure — More (data basis) | Resolve oxidate feed pressure data conflict (S229 78 kg/cm²G vs E-2302 tube 12 / X-2302 8 kg/cm²g) and confirm feed-line design pressure / piping class. | Low | Process | TBD | TBD | TBD | TBD | — | — | Open |
| R-005 | CDN-N03 | Temperature — More / Flow — No (overheat) | LOPA / SIF verification that combined over-temperature protection (TXSHH-0701A/0702A SIL 2 Cause 8 + TXSHH-0701B/0702B Cause 9 + TXSHH-0805A/B SIL 2 Cause 10 + TXSHH-0901A/B Cause 11 + LXSHH-0802 Cause 6 → UC-2301/UXV-0701-0706) achieves tolerable risk for the S5 concentrated-CHP (~80-85 wt%) decomposition consequence; confirm setpoints below 80 °C onset with margin; confirm time-delay "A" architecture and HXS-0102 startup bypass do not disable temp protection. | Medium | Instrument / Process | TBD | TBD | TBD | TBD | — | — | Open |
| R-006 | CDN-N03 | Pressure — More (block-isolated / deadhead) | Review overpressure/thermal-relief for E-2304 tube side and P-2301A/B discharge when block-isolated (no dedicated PSV once UXV-0802/0803 closed and isolated from V-2302 PSV-23-0801 relief), incl. P-2301 deadhead (Reliable Power, not ESD-stopped); confirm 4"-CHP-23-009004 recirc is continuous vs startup-only; confirm safe concentrated-CHP drain/purge for single-train isolation; confirm SC3 steam valve fail-closed action. | High | Process / Mechanical | TBD | TBD | TBD | TBD | — | — | Open |
| R-007 | CDN-N03 | Service Failure — Seal Flush | Confirm P-2301A/B Plan 53A dual-seal cumene-flush / N₂-barrier (22-0027) low-pressure/high-flow alarm coverage and operator response are adequate to detect loss of seal flush before concentrated CHP attacks the seal and causes LOPC; verify barrier-fluid integrity monitoring. | Medium | Mechanical / Process | TBD | TBD | TBD | TBD | — | — | Open |
| R-008 | CDN-N03 | Composition — Tube Leak (E-2304) | Provide on-line CHP/hydrocarbon detection (conductivity/pH or HC analyzer + alarm/divert) on D-2309 / SC3 condensate return to detect an E-2304 tube leak and prevent concentrated-CHP migration to the unrated utility condensate system; given the emergency CW/firewater coolant connection on the E-2304 shell, also address water-into-CHP ingress detection. | High | Process / Instrument | TBD | TBD | TBD | TBD | — | — | Open |
| R-009 | CDN-N03 | Flow — Reverse | Confirm independent check-valve protection (presence, type, testability) on P-2301A/B discharge (6"-CHP-23-009002/003) prevents reverse flow of acidified/partially-decomposed material from the Decomposer feed back into the concentrated CHP at V-2302 (acid backflow is a potent CHP decomposition catalyst). | Medium | Process / Mechanical | TBD | TBD | TBD | TBD | — | — | Open |

---

## Status Codes
- **Open** — not yet actioned
- **In Progress** — engineering/procurement underway
- **Closed** — implemented and verified
- **Rejected** — risk accepted by management (document reason)

## References
- [[wiki/hazop/study-info]] — node status register
- [[wiki/hazop/risk-matrix]] — risk ranking criteria (pending)
