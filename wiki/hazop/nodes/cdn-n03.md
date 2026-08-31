---
name: Flash Column Vaporizer & Concentrated Bottoms Circuit
node_id: CDN-N03
markup_label: "Node 23-03 (engineer P&ID markup)"
unit: CDN
pid_sheet: "14780-8120-25-23-0007, 14780-8120-25-23-0007A, 14780-8120-25-23-0008"
pid_marked_up: ""
inlet_boundary: "V-2302 bottoms to E-2304 shell side + SC3 steam supply to E-2304 tube side via UXV-0701..0706 + V-2302 concentrated bottoms to P-2301A/B suction"
outlet_boundary: "Two-phase vapor/liquid return to V-2302 + concentrated CHP product to Cleavage Reactor D-2304 via P-2301A/B discharge + E-2304 steam condensate"
tags: [hazop, node, CDN, confirmed]
last_updated: 2026-08-31
status: CONFIRMED by engineer; ready for interactive deviation review
---

# HAZOP Node CDN-N03 — Flash Column Vaporizer & Concentrated Bottoms Circuit

## Design Intent
Reboil V-2302 with SC3 steam in E-2304 to concentrate CHP to ~80-85 wt% and safely pump bottoms to Cleavage Section D-2304 via P-2301A/B.

## Node Boundaries
- **Inlet Boundary:** V-2302 bottoms to E-2304 shell side + SC3 steam supply to E-2304 tube side via UXV-0701..0706 + V-2302 concentrated bottoms to P-2301A/B suction
- **Outlet Boundary:** Two-phase vapor/liquid return to V-2302 + concentrated CHP product to Cleavage Reactor D-2304 via P-2301A/B discharge + E-2304 steam condensate

## Normal Operating Parameters
| Tag | Stream / Side | Design Condition | Operating Condition | Source |
|-----|---------------|------------------|---------------------|--------|
| **E-2304 shell** | Concentrated CHP (~80-85 wt%) | 3.5 kg/cm²g / FV @ 195 °C | 60–75 °C reboil liquid | E-2304 |
| **P-2301A/B** | Concentrated CHP Bottoms | 12 kg/cm²g @ 100 °C | 65 °C, 15 m³/h | P-2301AB |

## HAZOP Worksheet
