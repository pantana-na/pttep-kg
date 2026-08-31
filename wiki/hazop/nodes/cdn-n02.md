---
name: Preflash Column Feed-Heating / Steam-Condensate Circuit
node_id: CDN-N02
markup_label: "Node 23-02 (engineer P&ID markup)"
unit: CDN
pid_sheet: "14780-8120-25-23-0005, 14780-8120-25-23-0005A"
pid_marked_up: ""
inlet_boundary: "Oxidate feed to E-2302A/B tube side (from feed filters X-2302A/B / Node 23-01) + hot OXI recirculate to E-2302A/B shell + SC1.5 steam supply to E-2303 tube (via UXV-0501/0502)"
outlet_boundary: "Heated oxidate to V-2301 (Preflash Column) + OXI recirculate shell return to OXI + steam condensate from P-2308A/B to condensate return system (66-0056)"
tags: [hazop, node, CDN, confirmed]
last_updated: 2026-08-31
status: CONFIRMED by engineer; ready for interactive deviation review
---

# HAZOP Node CDN-N02 — Preflash Column Feed-Heating / Steam-Condensate Circuit

## Design Intent
Heat oxidate feed to Preflash Column target temp: recover heat in E-2302A/B, trim with SC1.5 steam in E-2303, deliver to V-2301; collect/return E-2303 condensate.

## Node Boundaries
- **Inlet Boundary:** Oxidate feed to E-2302A/B tube side (from feed filters X-2302A/B / Node 23-01) + hot OXI recirculate to E-2302A/B shell + SC1.5 steam supply to E-2303 tube (via UXV-0501/0502)
- **Outlet Boundary:** Heated oxidate to V-2301 (Preflash Column) + OXI recirculate shell return to OXI + steam condensate from P-2308A/B to condensate return system (66-0056)

## Normal Operating Parameters
| Tag | Stream / Side | Design Condition | Operating Condition | Source |
|-----|---------------|------------------|---------------------|--------|
| **E-2302A/B tube** | Fresh oxidate feed (CHP ~22.6 wt%) | 12 kg/cm²g / FV @ 83→120 °C | ~82–83 °C; feed flow 1,076,643 kg/h | E-2302AB; PFD-0001 |
| **E-2303 shell** | Oxidate (process, CHP) | 3.5 kg/cm²g / FV @ 195/250 °C | in ~82 °C → out ~83 °C target | E-2303 |

## HAZOP Worksheet
