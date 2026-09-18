# System Specifications (SDD Repository)

Welcome to the **Specification-Driven Development (SDD)** repository for the **Phenol Process Expert & HAZOP Safety Agent**.

This directory serves as the **single source of truth** for all architectural definitions, baseline models, safety invariants, and proposed feature enhancements.

---

## 1. Specification Directory Structure

```
specs/
├── README.md                      ← Master specification index (this file)
├── templates/
│   └── sdd-template.md            ← Standardized SDD template with Implementation Plan & Testing Matrix
├── baseline/                      ← Brownfield baseline specifications (as-is system state)
│   └── system-overview.md         ← Full system baseline: architecture, data models, workflows, invariants
├── features/                      ← Future feature proposals and modifications (delta specs)
│   └── SPEC-20260824-MULTI-AGENT-CLOUD-ARCHITECTURE.md
└── plan/                          ← Implementation progress reports and execution tracking
    └── PROGRESS_REPORT_20260827.md
```

---

## 2. Specification Index

### 2.1 Baseline Specifications (Brownfield System State)

| Document ID | Title | Scope | Status | Last Updated |
|---|---|---|---|---|
| [`SPEC-BASELINE-20260824-SYSTEM-OVERVIEW`](./baseline/system-overview.md) | **System Baseline Overview** | Comprehensive architecture, Markdown wiki contracts, classifier heuristics, HAZOP lifecycle, 5×5 RAM, and system invariants. | Approved | 2026-08-24 |

### 2.2 Reusable Templates

| Template | Purpose | Target Use |
|---|---|---|
| [`specs/templates/sdd-template.md`](./templates/sdd-template.md) | Standard SDD Template | Required format for all new feature specifications, major refactors, or API changes. |

### 2.3 Feature Specifications & Architecture (`specs/features/`)

| Document ID | Title | Scope | Status | Last Updated |
|---|---|---|---|---|
| [`SPEC-20260824-MULTI-AGENT-CLOUD-ARCHITECTURE`](./features/SPEC-20260824-MULTI-AGENT-CLOUD-ARCHITECTURE.md) | **Multi-Agent Cloud Architecture & Enterprise HAZOP Platform** | Decomposes system into 5 Gemini 3.7 Flash subagents, Cloud Spanner Graph + Dataplex Knowledge Catalog, Model Armor guardrails, and Web UI with full observability. | Implemented & Verified | 2026-08-27 |
| [`SPEC-20260831-HAZOP-MARKUP-INGESTION-AND-STUDY-LIFECYCLE`](./features/SPEC-20260831-HAZOP-MARKUP-INGESTION-AND-STUDY-LIFECYCLE.md) | **HAZOP P&ID Markup Ingestion, Study Lifecycle & 7-Tab Excel Export** | Ingestion of engineer-annotated P&ID PDFs (e.g. Node 23-02/23-03), human-in-the-loop node confirmation gate, 14-parameter 3-risk-block deviation analysis, and 7-tab GC Excel export matching reference examples. | Implemented & Verified | 2026-08-31 |
| [`SPEC-20260918-JOURNEY-1-EXPLORER-REDESIGN`](./features/SPEC-20260918-JOURNEY-1-EXPLORER-REDESIGN.md) | **Journey 1 Process Explorer & Enterprise Technical Cockpit Redesign** | Redesign dedicated to Journey 1 for customer IT technical demos: interactive Spanner knowledge graph topology visualizer, Model Armor security live metrics, Cloud Spanner ISO GQL & TrueTime inspector, and dynamic query subgraph filtering. | Implemented & Verified | 2026-09-18 |
| [`SPEC-20260918-ZERO-MOCK-CLOUD-NATIVE-MIGRATION`](./features/SPEC-20260918-ZERO-MOCK-CLOUD-NATIVE-MIGRATION.md) | **100% Cloud-Native Zero-Mock Architecture Migration** | Replaces all remaining mocked subsystems with 100% real Google Cloud services: live regional Model Armor API (`asia-southeast1`), Dataplex Knowledge Catalog entry syncing, Vertex AI `text-embedding-004` 768-dim embeddings in Cloud Spanner. | Implemented & Verified | 2026-09-18 |

### 2.4 Implementation Progress & Execution Reports (`specs/plan/`)

| Document ID | Title | Scope | Status | Last Updated |
|---|---|---|---|---|
| [`PLAN-20260827-PROGRESS-REPORT`](./plan/PROGRESS_REPORT_20260827.md) | **Initial Multi-Agent Platform Progress Report** | Tracks completion of Steps 1.0–8.0, 40/40 Unit & PBT tests, Model Armor integration, live Gemini synthesis, and test prompts. | Implemented & Verified (40/40 Tests Green) | 2026-08-27 |
| [`PLAN-20260831-PROGRESS-REPORT`](./plan/PROGRESS_REPORT_20260831.md) | **HAZOP Markup Ingestion, All-in-One Grid & AI Scenario Creator Report** | Tracks completion of P&ID markup parser, `<NodeConfirmationCard />`, All-in-One Excel grid with Freeze Panes, "What-If" AI Scenario Creator, 7-tab Excel exporter, and 59/59 tests. | Implemented & Verified (59/59 Tests Green) | 2026-08-31 |
| [`PLAN-20260918-PROGRESS-REPORT`](./plan/PROGRESS_REPORT_20260918.md) | **Journey 1 Process Explorer & Enterprise Technical Cockpit Report** | Tracks completion of Option 1 Dual-Pane Mission Control Cockpit, interactive Spanner Knowledge Graph Canvas, Model Armor security live card, ISO GQL & TrueTime inspector, and 61/61 tests. | Implemented & Verified (61/61 Tests Green) | 2026-09-18 |
| [`PLAN-20260918-ZERO-MOCK-MIGRATION`](./plan/PROGRESS_REPORT_20260918_ZERO_MOCK.md) | **100% Cloud-Native Zero-Mock Architecture Migration Report** | Complete elimination of all mocks across Model Armor, Dataplex Catalog, and Vertex AI embeddings in Spanner, with 65/65 tests green. | Implemented & Verified (65/65 Tests Green) | 2026-09-18 |

---

## 3. Governance & SDD Directives

All development in this repository strictly adheres to:
1. **Spec First, Code Second:** No code modifications may begin without an approved SDD and granular implementation plan.
2. **Brownfield Protocol:** All modifications must be framed as explicit deltas against [`specs/baseline/system-overview.md`](./baseline/system-overview.md).
3. **Mandatory Testing at Every Step:** Every implementation step requires deterministic Unit Tests and generative Property-Based Tests (PBT).
4. **Zero Spec Drift:** Any behavioral or contract modification must be synchronized in the corresponding specification document in the same commit.

For detailed rules and guidelines, see:
- [`GEMINI.md`](../GEMINI.md) — Project Guidelines & Governance
- [`_agents/rules/spec_driven_development.md`](../_agents/rules/spec_driven_development.md) — Spec-Driven Development Standard
- [`_agents/rules/devops_security_and_quality_standards.md`](../_agents/rules/devops_security_and_quality_standards.md) — DevOps & Security Rules
