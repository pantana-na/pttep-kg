# Specification Document: Journey 1 Process Explorer & Enterprise Technical Cockpit Redesign

**Document ID:** `SPEC-20260918-JOURNEY-1-EXPLORER-REDESIGN`  
**Status:** In Review / Proposed  
**Author(s):** Process Safety AI Architecture Team  
**Target Audience for Demo:** Customer's IT Technical Team / Cloud Architects / Cyber Security Leads  
**Governing Standard:** Spec-Driven Development (SDD) Protocol (`_agents/rules/spec_driven_development.md`)  
**Parent Baseline:** [`specs/baseline/system-overview.md`](../baseline/system-overview.md) & [`specs/features/SPEC-20260824-MULTI-AGENT-CLOUD-ARCHITECTURE.md`](./SPEC-20260824-MULTI-AGENT-CLOUD-ARCHITECTURE.md)  
**Date:** September 18, 2026  

---

## 1. Problem Statement & Goals

### 1.1 Context & Background
The current web application combines multiple complex workflows across three separate tabs: **Process Explorer (Q&A)**, **HAZOP Studio & 3-Gate HITL**, and **Document Manager**. While comprehensive, spreading focus across all three dilutes the demonstration impact when presenting to a **Customer's IT Technical Team**. 

Enterprise IT technical audiences (Enterprise Architects, Cloud Platform Engineers, Security Directors, and AI/Data Tech Leads) care intensely about:
1. **Cloud Architecture & Tri-Tier Storage:** How Cloud Spanner Graph (ISO GQL), Dataplex Knowledge Catalog (OEMS-005 aspect metadata & lineage), Vertex AI, and Google Cloud Storage operate together.
2. **AI Security & Guardrails:** How prompt injection, jailbreaking, and adversarial overrides are intercepted with microsecond-level latency before touching models or databases (Google Cloud Model Armor).
3. **Cognitive Transparency & Observability (Explainable AI / XAI):** Deep visibility into live agent thought streams, ISO GQL queries with TrueTime tokens, tool execution breakdowns, and Human-in-the-Loop (HITL) clarification state machines.
4. **Interactive Graph Topology:** The ability to visually interact with the petrochemical plant's topological digital twin (piping connections, SIS trip interlocks, equipment feed directions).

### 1.2 Objectives
- **Journey 1 Focus:** Redesign the primary application interface to focus 100% on **Journey 1: Interactive Process Safety Q&A, Security Guardrails & Topological Exploration**.
- **Interactive & Demo-Ready Cockpit:** Provide a mission-control experience tailored for IT teams with clickable architecture presets, live security meters, interactive knowledge graph visualization, and deep GQL/TrueTime telemetry.
- **Backend Design Stability:** Preserve the existing backend architecture and endpoints (`/api/v1/agent/stream`, `/api/v1/agent/query`, `/api/v1/agent/clarify`, `/healthz`) as-is.

### 1.3 Non-Goals
- Modifying core multi-agent orchestration logic or replacing Gemini 3.7 Flash.
- Removing the underlying HAZOP data structures or Spanner schema (they remain available in the background).
- Introducing mandatory authentication/RBAC (preserving frictionless direct ingress per user rules).

---

## 2. Proposed UI Architecture Choices for Customer IT Demo

Three UI design paradigms are proposed to maximize engagement and clarity for an enterprise IT audience:

### Option 1 (Recommended): "Enterprise AI Mission Control & Interactive Graph Cockpit"
* **Layout:** Balanced 2-Pane Split Workspace (`45% Chat & Security` / `55% Technical Deep-Dive Inspector`).
* **Left Pane (Conversational AI & Security Shield):**
  - **IT Demo Preset Bar:** Quick-action cards for 4 key IT demo stories:
    1. *⚡ Adversarial Attack Simulation* (Triggers Model Armor instant intercept).
    2. *🕸️ Multi-Hop Spanner GQL Traversal* (Triggers ISO GQL `FEEDS*1..3` upstream tracing).
    3. *📋 Dataplex Lineage & As-Built Audit* (Triggers OEMS-005 provenance check).
    4. *❓ HITL Disambiguation Stress Test* (Triggers Two-Tier Clarification pills).
  - **Live Chat Stream:** SSE token streaming with Gemini 3.7 Flash markdown rendering.
  - **Inline Security Badge:** Google Cloud Model Armor verdict, inspection latency, and policy template.
  - **Expandable Agent Thought Drawer:** Live stream of model reasoning chunks.
  - **Interactive HITL Clarification Cards:** Pill-based disambiguation with breadcrumb tracking.
* **Right Pane (Technical Deep-Dive Inspector — 3 Dynamic Tabs):**
  - **Tab 1: Interactive Spanner Knowledge Graph Explorer:** A visual interactive network graph (Canvas/SVG) rendering plant nodes (Vessels, Heat Exchangers, Pumps, SIS Interlocks) and directed edges (`FEEDS`, `TRIPS`, `PROTECTS`). Clicking any node inspects properties and triggers agent focus.
  - **Tab 2: Cloud Spanner ISO GQL & TrueTime Inspector:** Raw ISO GQL query viewer with syntax highlighting, row count, execution latency, and Google TrueTime commit timestamp token (`0x4e29b109_truetime`).
  - **Tab 3: Dataplex Lineage & Architecture Waterfall:** Dataplex aspect schema, revision lineage (`Rev Z1`), and execution latency waterfall chart (Model Armor -> Orchestrator -> Retriever MCP -> Gemini 3.7).

### Selected Design Paradigm: "Refinery Process Safety AI Mission Control & Interactive Graph Cockpit"
*Confirmed & Approved by User for Customer IT Technical Demo.*

* **Branding & Clean Architecture:** Strictly branded as **"Refinery Phenol Process Safety Expert"** (all references to legacy operator names replaced with "Refinery").
* **Layout:** Balanced 2-Pane Split Workspace (`45% Conversational AI & Security Shield` / `55% Deep Technical Inspector`).
* **Left Pane (Conversational AI & Security Shield):**
  - **Clean Query Input with Subtle Quick Chips:** Sleek, low-profile quick-action chips directly below search input (`🛡️ E-2303 Thermal Trips`, `🕸️ V-2301 Feed Streams`, `❓ Clarify Pump`, `🚨 Attack Test`).
  - **Live Chat Stream:** SSE token streaming with Gemini 3.7 Flash markdown rendering.
  - **Inline Security Badge:** Google Cloud Model Armor verdict, inspection latency (<1.0ms), and policy template.
  - **Expandable Agent Thought Drawer:** Live stream of model reasoning chunks.
  - **Interactive HITL Clarification Cards:** Pill-based disambiguation with breadcrumb tracking.
* **Right Pane (Deep Technical Inspector — 3 Dynamic Tabs):**
  - **Tab 1: Spanner Knowledge Graph & Cloud Spanner ISO GQL Console:**
    - **Query Subgraph Filtering:** Intelligently focuses on nodes and edges directly relevant to the user query (e.g. `E-2303`, upstream `E-2302A/B`, downstream `V-2301`, and SIS trip interlocks `TXSHH-0502A/B` / `UXV-0501/0502`).
    - **Full Plant Toggle:** Quick-switch button (`🌐 Show Full Plant` / `🎯 Focus Query Subgraph`) to view the entire plant topology or zoom into the active query's boundary.
    - **Node Inspector Sidecard:** Displays detailed design conditions, operating limits, and SIS interlock specs.
    - **Integrated ISO GQL Console:** Live GQL traversal query viewer with syntax highlighting, row count, execution latency, and Google TrueTime commit timestamp token (`0x4e29b109_truetime`).
  - **Tab 2: Dataplex Lineage & GCS LLM-Wiki Docs (Combined Documentation & Lineage):**
    - **Dataplex Knowledge Catalog Metadata:** As-Built certified P&ID drawing lineage (`14780-8120-25-23-0005_Z1.pdf`), entry group, process safety category, and OEMS-005 schema audit status.
    - **GCS LLM-Wiki Grounding Store:** Unstructured technical documentation viewer (`gs://refinery-process-safety-lake/wiki/...`) grounding Gemini 3.7 Flash with reaction kinetics and operating philosophies.
  - **Tab 3: Observability & End-to-End Latency Waterfall:**
    - **Latency Waterfall Breakdown:** Visual bar breakdown of end-to-end request processing (Model Armor guardrail <1ms, Orchestrator intent parsing, Retriever MCP Spanner/Dataplex, and Gemini 3.7 Flash synthesis).
    - **Cloud Run Observability & Health:** Liveness probe status (`/healthz`), unauthenticated direct ingress (`invoker-iam-disabled: 'true'`), and platform metrics.

---

## 3. Backend Alignment & Endpoint Specification

### 3.1 Preservation of Existing Core Endpoints
The existing backend design in `server/main.py` and `agents/orchestrator/agent.py` remains completely intact:
- `GET /api/v1/agent/stream?prompt=...`: Emits real-time SSE events (`armor_inspection`, `thought`, `tool_call`, `tool_result`, `clarification_requested`, `message_delta`, `message_done`).
- `POST /api/v1/agent/query`: Synchronous JSON execution returning full event arrays and synthesis.
- `POST /api/v1/agent/clarify`: Resolves disambiguated entity selections, queries interlocks, upstream graph, and provenance, and executes live Gemini synthesis.
- `GET /healthz`: Cloud Run liveness probe.

### 3.2 Approved Backend Addition: `GET /api/v1/graph/topology`
*Consulted and explicitly approved by the user.*

* **Endpoint:** `GET /api/v1/graph/topology`
* **Response Schema:**
```json
{
  "status": "SUCCESS",
  "nodes": [
    {
      "id": "E-2302A/B",
      "label": "E-2302A/B",
      "type": "equipment",
      "sub_type": "HeatExchanger",
      "name": "Preflash Feed Exchanger",
      "unit": "CDN",
      "design_temp": 120.0,
      "operating_temp": 83.0
    },
    {
      "id": "TXSHH-0502A",
      "label": "TXSHH-0502A",
      "type": "instrument",
      "sub_type": "TT",
      "sil": "SIL 2",
      "voting": "1oo2",
      "setpoint": "83.0 °C"
    }
  ],
  "edges": [
    {
      "source": "E-2302A/B",
      "target": "E-2303",
      "type": "FEEDS",
      "label": "S-2302"
    },
    {
      "source": "TXSHH-0502A",
      "target": "E-2303",
      "type": "TRIPS",
      "label": "Closes UXV-0501/0502"
    }
  ],
  "stats": {
    "equipment_count": 8,
    "instrument_count": 6,
    "feed_edges_count": 10,
    "trip_edges_count": 4
  }
}
```

---

## 4. Technical Invariants & Verification Matrix

### 4.1 Invariants
1. **Model Armor Gatekeeper Invariant:** Any query containing prompt injection or adversarial overrides MUST be blocked by Model Armor in <5ms, emitting 0 downstream database or tool calls.
2. **Clarification Depth Invariant:** Clarification depth is strictly capped at `MAX_CLARIFICATION_DEPTH = 3`.
3. **Chemical Safety Invariant:** Temperature limits for Cumene Hydroperoxide (CHP onset at 80.0°C) must never be relaxed or hallucinated.
4. **TrueTime Consistency Invariant:** All graph transactions and inspections must report valid TrueTime coordination tokens.
5. **Graph Topology Fidelity Invariant:** All edges returned by `GET /api/v1/graph/topology` must reference valid source and target nodes existing in the node registry.

### 4.2 Test Matrix
- `UT-TOPOLOGY-01`: `GET /api/v1/graph/topology` returns valid JSON with equipment, instruments, and flows.
- `UT-UI-STREAM`: SSE multiplexer successfully delivers all 7 event types.
- `UT-ARMOR-BLOCK`: Adversarial prompt yields `verdict: BLOCKED` and terminates SSE stream.
- `UT-HITL-RESOLVE`: Clarification button click resumes query and synthesizes multi-tier answer.
- `PBT-GRAPH-TOPOLOGY-VALIDITY`: Hypothesis test ensuring no orphan edges exist in graph topology output.

---

## 5. Granular Step-by-Step Implementation Plan

| Step # | Subsystem / Task | Target Files | Completion Criteria |
|---|---|---|---|
| **1.0** | **Backend Topology Endpoint** | `server/main.py` | Implement `GET /api/v1/graph/topology` exposing nodes, edges, and stats. |
| **2.0** | **Unit & Property-Based Tests** | `tests/test_server_endpoints.py` | Add `UT-TOPOLOGY-01` and `PBT-GRAPH-TOPOLOGY-VALIDITY` with Hypothesis. |
| **3.0** | **Dual-Pane UI Redesign (Journey 1 Cockpit)** | `server/static/index.html` | Build Dual-Pane Mission Control layout with IT demo presets, Model Armor badge, interactive SVG/Canvas graph visualizer, GQL inspector, and Dataplex lineage tab. |
| **4.0** | **Verification & Progress Tracking** | `specs/plan/PROGRESS_REPORT_20260918.md` | Run full test suite, verify local UI, and record progress report. |

