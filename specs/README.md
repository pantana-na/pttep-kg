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
| [`SPEC-20260824-MULTI-AGENT-CLOUD-ARCHITECTURE`](./features/SPEC-20260824-MULTI-AGENT-CLOUD-ARCHITECTURE.md) | **Multi-Agent Cloud Architecture & Enterprise HAZOP Platform** | Decomposes system into Gemini 3.8 Flash subagents, Cloud Spanner Graph + Dataplex Knowledge Catalog, Model Armor guardrails, and Web UI with full observability. | Implemented & Verified | 2026-08-27 |
| [`SPEC-20260831-HAZOP-MARKUP-INGESTION-AND-STUDY-LIFECYCLE`](./features/SPEC-20260831-HAZOP-MARKUP-INGESTION-AND-STUDY-LIFECYCLE.md) | **HAZOP P&ID Markup Ingestion, Study Lifecycle & 7-Tab Excel Export** | Ingestion of engineer-annotated P&ID PDFs (e.g. Node 23-02/23-03), human-in-the-loop node confirmation gate, 14-parameter 3-risk-block deviation analysis, and 7-tab GC Excel export matching reference examples. | Implemented & Verified | 2026-08-31 |
| [`SPEC-20260918-JOURNEY-1-EXPLORER-REDESIGN`](./features/SPEC-20260918-JOURNEY-1-EXPLORER-REDESIGN.md) | **Journey 1 Process Explorer & Enterprise Technical Cockpit Redesign** | Redesign dedicated to Journey 1 for customer IT technical demos: interactive Spanner knowledge graph topology visualizer, Model Armor security live metrics, Cloud Spanner ISO GQL & TrueTime inspector, and dynamic query subgraph filtering. | Implemented & Verified | 2026-09-18 |
| [`SPEC-20260918-ZERO-MOCK-CLOUD-NATIVE-MIGRATION`](./features/SPEC-20260918-ZERO-MOCK-CLOUD-NATIVE-MIGRATION.md) | **100% Cloud-Native Zero-Mock Architecture Migration** | Replaces all remaining mocked subsystems with 100% real Google Cloud services: live regional Model Armor API (`asia-southeast1`), Dataplex Knowledge Catalog entry syncing, Vertex AI `text-embedding-004` 768-dim embeddings in Cloud Spanner. | Implemented & Verified | 2026-09-18 |
| [`SPEC-20260918-GOOGLE-ADK-AND-AGENT-RUNTIME-REFACTOR`](./features/SPEC-20260918-GOOGLE-ADK-AND-AGENT-RUNTIME-REFACTOR.md) | **Official Google ADK & Gemini Enterprise Agent Platform Refactor** | Refactors multi-agent system to official `google-adk` (`Agent`, `App`, `FunctionTool`), configures `agents-cli-manifest.yaml` targeting `agent_runtime` in `asia-southeast1`, and wires inline Model Armor security callback. | Implemented & Verified | 2026-09-18 |
| [`SPEC-20260918-MODEL-INTENT-DISPATCH-AND-CLEANUP`](./features/SPEC-20260918-MODEL-INTENT-DISPATCH-AND-CLEANUP.md) | **Model-Driven Intent Classification, UI Cleanup & Gemini 3.8 Flash Migration** | Eliminates regular expressions, implements strictly 3 canonical intents with question suggestions, dynamically returns all 12 pumps for ambiguous queries, dynamic UI latency waterfall, disabled unused agents, and Gemini 3.8 Flash everywhere. | Implemented & Verified | 2026-09-18 |
| [`SPEC-20260918-FRONTEND-ONLY-CLOUD-RUN`](./features/SPEC-20260918-FRONTEND-ONLY-CLOUD-RUN.md) | **Frontend-Only Cloud Run & Agent Platform Backend Decoupling** | Decouples Cloud Run into strictly a frontend SPA web server & thin SSE proxy; offloads all multi-agent AI reasoning to Gemini Enterprise Agent Platform runtime via `agents-cli deploy`. | Implemented & Verified | 2026-09-18 |
| [`SPEC-20260918-CONSOLIDATED-SINGLE-ORCHESTRATOR`](./features/SPEC-20260918-CONSOLIDATED-SINGLE-ORCHESTRATOR.md) | **Consolidated Single Orchestrator Agent Architecture** | Consolidates OrchestratorAgent, RetrieverAgent, and HazopAgent into one unified root OrchestratorAgent with direct tool access, zero subagent hops, and sub_agents=[]. | Implemented & Verified | 2026-09-18 |
| [`SPEC-20260919-AGENT-EVAL-100-DATASETS`](./features/SPEC-20260919-AGENT-EVAL-100-DATASETS.md) | **100+ Golden Agent Evaluation Benchmark Suite** | Expands Agent Evaluation suite to 105 grounded cases across SIS trips, flow tracing, provenance, HAZOP/LOPA, and Model Armor security against live Spanner and Vertex AI. | Implemented & Verified | 2026-09-19 |
| [`SPEC-20260920-TRI-PANE-MISSION-CONTROL-COCKPIT`](./features/SPEC-20260920-TRI-PANE-MISSION-CONTROL-COCKPIT.md) | **Tri-Pane Mission Control Cockpit Redesign** | Redesigns frontend into a Tri-Pane Mission Control Cockpit: Plant Asset Hierarchy tree, persistent multi-turn chat, step-by-step latency observability, and interactive Spanner graph canvas. | Implemented & Verified | 2026-09-20 |
| [`SPEC-20260920-DATABASE-FIRST-EQUIPMENT-CATALOG`](./features/SPEC-20260920-DATABASE-FIRST-EQUIPMENT-CATALOG.md) | **Database-First Equipment Catalog & Live Spanner Synchronization** | Migrates all 54 equipment operating/design conditions, HAZOP nodes, and mappings to Cloud Spanner; deletes hardcoded catalog dictionary in code. | Implemented & Verified | 2026-09-20 |
| [`SPEC-20260920-ZERO-HARDCODED-DATA-AND-DB-DRIVEN-ARCHITECTURE`](./features/SPEC-20260920-ZERO-HARDCODED-DATA-AND-DB-DRIVEN-ARCHITECTURE.md) | **100% Database-Driven Architecture & Zero Hardcoded Data** | Eliminates all hardcoded dictionaries, static risk scores, and node if/else mappings; backed by Cloud Spanner HAZOP entities, Dataplex, and dynamic RAM. | Implemented & Verified | 2026-09-20 |
| [`SPEC-20260920-DYNAMIC-TELEMETRY-WATERFALL-LATENCY`](./features/SPEC-20260920-DYNAMIC-TELEMETRY-WATERFALL-LATENCY.md) | **Dynamic Wall-Clock Telemetry Waterfall & Model Armor Measurement** | Eliminates static 0.5ms / 120ms / 200ms latency clamps; establishes real wall-clock measurement across Model Armor, intent deliberation, tool execution, and token streaming. | Implemented & Verified | 2026-09-20 |
| [`SPEC-20260920-SPANNER-GRAPH-PAN-SCROLL-AND-AUTO-CENTER`](./features/SPEC-20260920-SPANNER-GRAPH-PAN-SCROLL-AND-AUTO-CENTER.md) | **Spanner Graph 2D Pan/Scroll Navigation & Automatic Node Centering** | Full 2D canvas mouse drag, trackpad/wheel scroll, toolbar directional pan controls, automatic node centering, and beacon focus on selected equipment. | Implemented & Verified | 2026-09-20 |
| [`SPEC-20260921-DATA-SANITIZATION-NEUTRAL-REFINERY`](./features/SPEC-20260921-DATA-SANITIZATION-NEUTRAL-REFINERY.md) | **Full Repository Data Sanitization (Neutral Refinery Profile)** | Systematic sanitization of all proprietary corporate identifiers across 52 wiki files, code docstrings, DB seeds, and specs to Neutral Refinery. | Implemented & Verified | 2026-09-21 |


### 2.4 Implementation Progress & Execution Reports (`specs/plan/`)

| Document ID | Title | Scope | Status | Last Updated |
|---|---|---|---|---|
| [`PLAN-20260827-PROGRESS-REPORT`](./plan/PROGRESS_REPORT_20260827.md) | **Initial Multi-Agent Platform Progress Report** | Tracks completion of Steps 1.0–8.0, 40/40 Unit & PBT tests, Model Armor integration, live Gemini synthesis, and test prompts. | Implemented & Verified (40/40 Tests Green) | 2026-08-27 |
| [`PLAN-20260831-PROGRESS-REPORT`](./plan/PROGRESS_REPORT_20260831.md) | **HAZOP Markup Ingestion, All-in-One Grid & AI Scenario Creator Report** | Tracks completion of P&ID markup parser, `<NodeConfirmationCard />`, All-in-One Excel grid with Freeze Panes, "What-If" AI Scenario Creator, 7-tab Excel exporter, and 59/59 tests. | Implemented & Verified (59/59 Tests Green) | 2026-08-31 |
| [`PLAN-20260918-PROGRESS-REPORT`](./plan/PROGRESS_REPORT_20260918.md) | **Journey 1 Process Explorer & Enterprise Technical Cockpit Report** | Tracks completion of Option 1 Dual-Pane Mission Control Cockpit, interactive Spanner Knowledge Graph Canvas, Model Armor security live card, ISO GQL & TrueTime inspector, and 61/61 tests. | Implemented & Verified (61/61 Tests Green) | 2026-09-18 |
| [`PLAN-20260918-ZERO-MOCK-MIGRATION`](./plan/PROGRESS_REPORT_20260918_ZERO_MOCK.md) | **100% Cloud-Native Zero-Mock Architecture Migration Report** | Complete elimination of all mocks across Model Armor, Dataplex Catalog, and Vertex AI embeddings in Spanner, with 65/65 tests green. | Implemented & Verified (65/65 Tests Green) | 2026-09-18 |
| [`PLAN-20260918-ADK-REFACTOR`](./plan/PROGRESS_REPORT_20260918_ADK_REFACTOR.md) | **Official Google ADK & Agent Platform Runtime Refactoring Report** | Refactors multi-agent hierarchy to official `google-adk`, `agents-cli-manifest.yaml`, Model Armor callback, dual ingress, and 81/81 tests green. | Implemented & Verified (81/81 Tests Green) | 2026-09-18 |
| [`PLAN-20260918-MODEL-DRIVEN-INTENT-AND-UI-CLEANUP`](./plan/PROGRESS_REPORT_20260918_MODEL_DRIVEN_INTENT_AND_UI_CLEANUP.md) | **Model-Driven Intent, Dynamic Telemetry & Gemini 3.8 Flash Migration Report** | Tracks completion of model-driven intent classification, zero regex rule, all-pump candidate ambiguity resolution, dynamic UI waterfall, RAI filters, and 84/84 tests green. | Implemented & Verified (84/84 Tests Green) | 2026-09-18 |
| [`PLAN-20260918-FRONTEND-ONLY-CLOUD-RUN`](./plan/PROGRESS_REPORT_20260918_FRONTEND_ONLY_CLOUD_RUN.md) | **Frontend-Only Cloud Run & Agent Platform Backend Decoupling Report** | Decouples Cloud Run into strictly a frontend SPA web server & thin SSE proxy; offloads AI reasoning to Gemini Enterprise Agent Platform runtime via `agents-cli deploy`, 87/87 tests green. | Implemented & Verified (87/87 Tests Green) | 2026-09-18 |
| [`PLAN-20260918-CONSOLIDATED-SINGLE-ORCHESTRATOR`](./plan/PROGRESS_REPORT_20260918_CONSOLIDATED_SINGLE_ORCHESTRATOR.md) | **Consolidated Single Orchestrator Agent & Dead Code Removal Report** | Pruned legacy `OrchestratorAgent` class, removed dead `agents/` folder and unused files, aligned all tests to production ADK tools, 80/80 tests green. | Implemented & Verified (80/80 Tests Green) | 2026-09-18 |
| [`PLAN-20260919-AGENT-EVAL-100-DATASETS`](./plan/PROGRESS_REPORT_20260919_AGENT_EVAL_100_DATASETS.md) | **100+ Golden Agent Evaluation Benchmark Suite & Mode B Execution** | 105 grounded datasets across 5 suites, Mode A (105/105 passed, 1.0000 groundedness), Reasoning Engine deployment, and Mode B background execution with 1h timeout. | Implemented & Verified / In Progress | 2026-09-19 |
| [`PLAN-20260920-TRI-PANE-MISSION-CONTROL-COCKPIT`](./plan/PROGRESS_REPORT_20260920_TRI_PANE_COCKPIT_REDESIGN.md) | **Tri-Pane Mission Control Cockpit Redesign & Deployment Report** | Option 1 Tri-Pane Cockpit: Plant Asset Hierarchy tree, persistent multi-turn chat, step-by-step latency observability, Spanner graph canvas, 43/43 tests green, deployed to Cloud Run. | Implemented & Verified (43/43 Tests Green) | 2026-09-20 |
| [`PLAN-20260920-DATABASE-FIRST-EQUIPMENT-CATALOG`](./plan/PROGRESS_REPORT_20260920_DATABASE_FIRST_EQUIPMENT_CATALOG.md) | **Database-First Equipment Catalog & Live Spanner Migration Report** | Migrated all 54 assets, 6 nodes, 54 mappings into live Cloud Spanner; removed hardcoded `equipment_catalog.py` (-731 lines), 45/45 tests green. | Implemented & Verified (45/45 Tests Green) | 2026-09-20 |
| [`PLAN-20260920-ZERO-HARDCODED-DATA`](./plan/PROGRESS_REPORT_20260920_ZERO_HARDCODED_DATA.md) | **100% Database-Driven Architecture & Zero Hardcoded Data Report** | Eliminated all hardcoded node name mappings, static risk scores, and catalog fallback dictionaries; 70/70 tests green, deployed to Cloud Run prod (`00017-fj4`). | Implemented & Verified (70/70 Tests Green) | 2026-09-20 |
| [`PLAN-20260920-DYNAMIC-TELEMETRY-WATERFALL`](./plan/PROGRESS_REPORT_20260920_DYNAMIC_TELEMETRY_WATERFALL.md) | **Dynamic Telemetry Waterfall & Real Model Armor Latency Report** | Eliminates static 0.5ms / 120ms / 200ms latency clamps; establishes real wall-clock measurement across Model Armor, intent deliberation, tool execution, and token streaming; 39/39 tests green. | Implemented & Verified (39/39 Tests Green) | 2026-09-20 |
| [`PLAN-20260920-SPANNER-GRAPH-PAN-AND-CENTER`](./plan/PROGRESS_REPORT_20260920_SPANNER_GRAPH_PAN_AND_CENTER.md) | **Spanner Graph 2D Pan/Scroll Navigation & Automatic Node Centering Report** | Full 2D canvas mouse drag, trackpad/wheel 2D scroll, directional controls, mathematical auto-centering, and glowing beacon; 40/40 tests green. | Implemented & Verified (40/40 Tests Green) | 2026-09-20 |
| [`PLAN-20260921-DATA-SANITIZATION`](./plan/PROGRESS_REPORT_20260921_DATA_SANITIZATION.md) | **Full Repository Data Sanitization (Neutral Refinery Profile)** | Decontamination of proprietary names across 52 wiki files, DB seeds, and codebase; 155/155 PBT invariant tests passing. | Implemented & Verified (155/155 Tests Green) | 2026-09-21 |



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
