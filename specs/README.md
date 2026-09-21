# System Specifications (SDD Repository)

Welcome to the **Specification-Driven Development (SDD)** repository for the **Refinery Phenol Process Safety Expert & Multi-Agent Platform**.

This directory serves as the **single source of truth** for all architectural definitions, baseline models, safety invariants, feature specifications, and execution progress tracking.

---

## 1. Specification Directory Structure

```
specs/
├── README.md                      ← Master specification index (this file)
├── templates/
│   └── sdd-template.md            ← Standardized SDD template with Implementation Plan & Testing Matrix
├── baseline/                      ← Brownfield baseline specifications (as-is system state)
│   └── system-overview.md         ← Full system baseline: architecture, data models, workflows, invariants
├── features/                      ← Authoritative feature & architectural specifications
│   ├── README.md                  ← Feature specifications index
│   └── CONSOLIDATED_FEATURE_SPECIFICATION.md ← Consolidated master system architecture & feature specification
└── plan/                          ← Living implementation progress reports and milestone tracking
    ├── README.md                  ← Implementation plan index
    └── CONSOLIDATED_IMPLEMENTATION_PLAN.md   ← Consolidated master execution plan, milestones, and test metrics
```

---

## 2. Specification Index

### 2.1 Baseline Specifications (Brownfield System State)

| Document ID | Title | Scope | Status | Last Updated |
|---|---|---|---|---|
| [`SPEC-BASELINE-20260824-SYSTEM-OVERVIEW`](./baseline/system-overview.md) | **System Baseline Overview** | Comprehensive architecture, Markdown wiki contracts, classifier heuristics, HAZOP lifecycle, 5×5 RAM, and system invariants. | Approved Baseline | 2026-08-24 |

### 2.2 Reusable Templates

| Template | Purpose | Target Use |
|---|---|---|
| [`specs/templates/sdd-template.md`](./templates/sdd-template.md) | Standard SDD Template | Required format for all new feature specifications, major refactors, or API changes. |

### 2.3 Authoritative Feature Specifications (`specs/features/`)

| Document ID | Title | Scope | Status | Last Updated |
|---|---|---|---|---|
| [`SPEC-CONSOLIDATED-20260921-SYSTEM-ARCHITECTURE`](./features/CONSOLIDATED_FEATURE_SPECIFICATION.md) | **Consolidated Feature Specification & System Architecture** | Unified master specification consolidating all 15 feature milestones: decoupled cloud architecture, single root orchestrator, zero regex intent dispatch, Tri-Tier knowledge layer (Spanner, Dataplex, GCS), live Model Armor guardrails, Tri-Pane Mission Control Cockpit, 14-parameter HAZOP facilitation with 7-tab Excel export, and Neutral Refinery data sanitization. | Approved & Implemented | 2026-09-21 |

### 2.4 Master Implementation Plan & Progress Reports (`specs/plan/`)

| Document ID | Title | Scope | Status | Last Updated |
|---|---|---|---|---|
| [`PLAN-CONSOLIDATED-20260921-MASTER-EXECUTION-REPORT`](./plan/CONSOLIDATED_IMPLEMENTATION_PLAN.md) | **Consolidated Master Implementation Plan & Progress Report** | Master execution record consolidating Milestones M-01 through M-15: test verification metrics (155/155 PBT, 20/20 live ADK, 105 Golden Benchmark evals), live Cloud Spanner graph verification, Dataplex catalog synchronization, GCS wiki sync, and zero Gemini API key production security compliance. | Completed & Production Verified | 2026-09-21 |

---

## 3. Governance & SDD Directives

All development in this repository strictly adheres to:
1. **Spec First, Code Second:** No code modifications may begin without an approved SDD and granular implementation plan.
2. **Brownfield Protocol:** All modifications must be framed as explicit deltas against [`specs/baseline/system-overview.md`](./baseline/system-overview.md).
3. **Mandatory Testing at Every Step:** Every implementation step requires deterministic Unit Tests and generative Property-Based Tests (PBT).
4. **Living Specs:** When any code or behavior changes, the corresponding SDD in `specs/features/` and execution progress report in `specs/plan/` must be synchronized in the same commit to prevent spec drift.

For detailed rules and guidelines, see:
- [`GEMINI.md`](../GEMINI.md) — Project Guidelines & Governance
- [`_agents/rules/spec_driven_development.md`](../_agents/rules/spec_driven_development.md) — Spec-Driven Development Standard
- [`_agents/rules/devops_security_and_quality_standards.md`](../_agents/rules/devops_security_and_quality_standards.md) — DevOps & Security Rules
