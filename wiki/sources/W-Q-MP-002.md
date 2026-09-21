---
name: W-(Q-MP)-002 Operational Risk Assessment Matrix and Its Applications
type: standard
tags: [source, standard, risk-matrix, hazop]
last_updated: 2026-06-13
---

# Source: W-(Q-MP)-002 — Operational Risk Assessment Matrix and Its Applications

**Issuer:** Refinery Petrochemical Corporation, GC Management System and Process Safety (Q-MP)
**Document No.:** W-(Q-MP)-002
**Revision:** 2
**Date:** 10/09/2025
**Pages:** 55
**File:** `raw/standards/W-(Q-MP)-002_R2.pdf`
**Created by:** Mr. Pattara Tepnu, Senior Safety Engineer
**Approved by:** Mr. Warakorn Decha, Vice President
**Reviewed by:** Mr. Sompong Wannasiriluck, Division Manager Q-MP-IO

---

## Document Purpose

Establishes the GC Risk Assessment Matrix (RAM) — a qualitative risk assessment tool used consistently across Refinery Group and subsidiaries. The RAM is applied to Process Hazard Analysis (PHA/HAZOP), Incident Investigation, RCM, RBI, SIF, Corrective Maintenance, OT Cyber Security, and other operational risk processes.

The wiki page extracted for HAZOP use: [[wiki/hazop/risk-matrix]]

---

## Key Findings for HAZOP

### RAM Structure
- **5×5 matrix**: 5 Likelihood levels × 5 Consequence severity levels
- **4 Consequence categories (PEES)**: People, Environment, Economic, Social
- **Risk rankings**: Very Low (green) → Low (yellow) → Medium (orange) → High (red) → Extreme (dark red)
- For HAZOP: Section 6.2.1.3.1 — "RAM for Process Hazard Analysis (PHA)" governs

### Risk Assessment Process (4 steps)
1. Identify potential Consequences
2. Estimate Severity of each Consequence (1–5 per PEES category)
3. Estimate Likelihood (1–5)
4. Determine Risk Rating from matrix

### Two-Stage HAZOP Risk Assessment
Consistent with P-(Q-MP)-OEMS-005 §6.5.2:
- **Initial Risk** = Severity × Likelihood WITHOUT safeguards
- **Mitigated Risk** = Severity FIXED (never changes) × Likelihood re-evaluated WITH safeguards

### Thai Regulation (DIW) Note
For PHA required to comply with Thai DIW regulation:
- 4×4 RAM applies: Consequence (1)–(4), Likelihood "Improbable (1)" to "Likely (4)"
- Risk ranks: Very Low to High (no "Extreme" level in DIW matrix)

### Action Thresholds
| Risk Level | Action Required |
|-----------|----------------|
| Extreme | Serious risk — action & risk reduction plan immediately |
| High | Unacceptable risk — action & risk reduction plan immediately |
| Medium | Medium risk — require risk reduction plan |
| Low | Acceptable risk — require review of control plan |
| Very Low | Very low risk |

---

## Wiki Pages Created from This Source
- [[wiki/hazop/risk-matrix]] — Full PHA RAM extracted and formatted for HAZOP use

## Related Documents
- [[sources/P-Q-MP-OEMS-005]] — HAZOP procedure that references this RAM
- P-(Q-MP)-OEMS-004 — Incident Investigation System
- P-(TP-RE)-001 — Safety Instrumented Function (SIF) System Management
