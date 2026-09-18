---
name: Preflash Column Feed-Heating / Steam-Condensate Circuit
node_id: CDN-N02
markup_label: "Node 23-02 (engineer P&ID markup)"
unit: CDN
pid_sheet: "14780-8120-25-23-0005, 14780-8120-25-23-0005A"
pid_marked_up: "Node 23-02.pdf"
inlet_boundary: "Oxidate feed to E-2302A/B tube side (from feed filters X-2302A/B / Node 23-01) + hot OXI recirculate to E-2302A/B shell (from OXI Oxidizer No.2 pumps) + SC1.5 steam supply to E-2303 tube (via UXV-0501/0502)"
outlet_boundary: "Heated oxidate to V-2301 (Preflash Column) + OXI recirculate shell return to OXI + steam condensate from P-2308A/B to condensate return system (66-0056)"
tags: [hazop, node, CDN, confirmed]
last_updated: 2026-08-31
status: COMPLETE — Closed-out & certified by engineer; ready for interactive deviation review
---

# HAZOP Node CDN-N02 — Preflash Column Feed-Heating / Steam-Condensate Circuit

## Design Intent
Heat oxidate feed to Preflash Column target temp: recover heat in E-2302A/B, trim with SC1.5 steam in E-2303, deliver to V-2301; collect/return E-2303 condensate.

## Node Boundaries
- **Inlet Boundary:** Oxidate feed to E-2302A/B tube side (from feed filters X-2302A/B / Node 23-01) + hot OXI recirculate to E-2302A/B shell (from OXI Oxidizer No.2 pumps) + SC1.5 steam supply to E-2303 tube (via UXV-0501/0502)
- **Outlet Boundary:** Heated oxidate to V-2301 (Preflash Column) + OXI recirculate shell return to OXI + steam condensate from P-2308A/B to condensate return system (66-0056)

## Normal Operating Parameters
| Tag | Stream / Side | Design Condition | Operating Condition | Source |
|-----|---------------|------------------|---------------------|--------|
| **E-2302A/B tube** | Fresh oxidate feed (CHP ~22.6 wt%) | 12 kg/cm²g / FV @ 83→120 °C | ~82–83 °C; feed flow part of S229 1,076,643 kg/h total | E-2302A/B; PFD-0001 |
| **E-2302A/B shell** | Hot OXI recirculate (CHP-containing) | 3.5 kg/cm²g / FV @ 195/250 °C | hot recirculate from OXI | E-2302A/B |
| **E-2303 shell** | Oxidate (process, CHP) | 3.5 kg/cm²g / FV @ 195/250 °C | in ~82 °C → out ~83 °C target to V-2301 | E-2303 |
| **E-2303 tube** | SC1.5 steam | 7 kg/cm²g / FV @ 120/195 °C | SC1.5 steam, ~120–133 °C sat. | E-2303 |
| **D-2308** | Steam condensate | INT 7 kg/cm²g / FV @ 195 °C | 0.9 kg/cm²g / 117 °C; NLL 550 mm | D-2308 |
| **P-2308A/B** | Steam condensate | INT 7 kg/cm²g / FV @ 195 °C | 0.9 kg/cm²g / 117 °C; NLL 550 mm | P-2308A/B |

## HAZOP Worksheet


## Finalized Worksheet Rows
| Ref | Parameter | Deviation | Cause | Consequence | Initial Risk | Mitigated Risk | Recommendation |
|---|---|---|---|---|---|---|---|
| 1.1.1 | Flow | No / Low Flow | Feed pump trip | Heater dryout | Extreme | High | R-001: Install redundant interlock |
