# SPEC-20260920-TRI-PANE-MISSION-CONTROL-COCKPIT: Tri-Pane Mission Control Cockpit Redesign

**Document ID:** `SPEC-20260920-TRI-PANE-MISSION-CONTROL-COCKPIT`  
**Status:** APPROVED  
**Author(s):** Antigravity Agent & Core Architecture Team  
**Governed by:** `GEMINI.md` (Rules 1, 3, 4, 6, 7, 8, 11, 12), `_agents/rules/spec_driven_development.md`  
**Target Environment:** Non-Prod (`main`) & Prod (`prod`)  
**GenAI Model:** `gemini-3.8-flash` (strictly enforced repository-wide)  
**Date:** September 20, 2026  

---

## 1. Problem Statement & Goals

### 1.1 Context & Problem Statement
The current frontend (`server/static/index.html`) is structured as a single-turn query form with a dual-pane layout:
1. **Lack of Hierarchical Asset Exploration:** Business users cannot easily browse equipment, instruments, and HAZOP study nodes in an interactive tree or catalog; they must know or guess equipment tags beforehand.
2. **Single-Turn Chat Limitation:** Every new query wipes previous results and runs without a persistent session ID (`session_id`), preventing multi-turn conversational exploration and follow-up investigations.
3. **Disconnected Observability:** Tool executions and thought streams are displayed in a transient stream container that is separated from the conversation thread, lacking clear per-step latency metrics right alongside the active turn.

### 1.2 Goals & Non-Goals
- **Goals:**
  1. **Tri-Pane Mission Control Cockpit Layout:**
     - **Left Pane (25%):** Interactive Plant Asset Hierarchy Tree (Process Sections $\rightarrow$ HAZOP Nodes $\rightarrow$ Equipment $\rightarrow$ Instruments) with live search and filter, plus one-click action chips (`🛡️ Query Interlocks`, `⚡ Run HAZOP`, `📋 Certified P&ID`).
     - **Center Pane (45%):** Persistent Multi-Turn Conversational Cockpit with user/agent message bubbles, markdown risk tables, inline `<ClarificationCard />`, persistent `session_id`, and a `🔄 Reset Session` control.
     - **Right Pane (30%):** Live XAI & Observability Inspector featuring real-time step-by-step latency waterfall (`Model Armor`, `Cognitive Reasoning`, `Tool Execution`, `Gemini Synthesis`), collapsible thought stream, and interactive HTML5 Spanner graph canvas.
  2. **Catalog Hierarchy API:** Add `GET /api/v1/catalog/hierarchy` returning structured nodes, equipment, and instruments grouped by section.
  3. **Continuous Multi-Turn Session:** Maintain `session_id` in frontend state/localStorage and forward to `agent_proxy.stream_query` so the backend retains conversational memory across turns.
  4. **Per-Step Latency Breakdown:** Real-time metrics for every phase of execution displayed in milliseconds.
- **Non-Goals:**
  - Modifying the underlying Spanner schema or DDL.
  - Adding heavy client-side frameworks; maintain zero-build, ultra-fast single-page deployment via Tailwind CSS + vanilla modern ES6 inside `server/static/index.html`.

---

## 2. System Architecture & UI Layout

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│  🛡️ MISSION CONTROL  •  Cumene Oxidation & Cleavage (CDN)  •  Gemini 3.8 Flash  •  [ 🔄 Reset Session ] [ 🤖 6 Tools ]  │
├──────────────────────────────┬───────────────────────────────────────────┬───────────────────────────────────────┤
│ 📂 Plant Asset Hierarchy     │ 💬 Multi-Turn Safety Assistant            │ ⏱️ Agent Reasoning & Tool Latency     │
│                              │                                           │                                       │
│ 🔍 Filter (e.g. "pump", "E-")│ User: What trips protect E-2303?          │ ⚡ Execution Waterfall (Total: 842ms) │
│ ▾ Section: Cleavage (CDN)    │                                           │ ├─ 🛡️ Model Armor: 0.8ms (Passed)     │
│   ▾ Node CDN-N02 (Preflash)  │ Agent: Protections for E-2303 include:   │ ├─ 💭 Thought Stream: 45ms            │
│     ▾ 📦 Equipment: E-2303   │ • TXSHH-0502A/B (1oo2 SIL 1)              │ │    "Searching property graph for    │
│       ├─ 🎛️ TXSHH-0502A      │ • Trips Steam Isolation UV-2301           │ │     active interlocks on E-2303..." │
│       └─ 🎛️ TXSHH-0502B      │ [ 📋 P&ID Rev Z1 ] [ ⚡ Evaluate HAZOP ]   │ ├─ 🔧 Tool: spanner_graph_query       │
│     ▸ 📦 Equipment: V-2301   │                                           │ │    Latency: 38ms (2 trips returned) │
│     ▸ 📦 Equipment: P-2301A/B│ User: What about feed pump P-2301A?       │ └─ ⚡ Gemini Synthesis: 758ms (TTFT)  │
│   ▸ Node CDN-N01 (Quench)    │                                           │                                       │
│   ▸ Node CDN-N03 (Vacuum)    │ Agent: Feed pump P-2301A has FSL-0501...  │ [ Sub-Tabs: Telemetry | GQL | Graph ] │
│                              │                                           │                                       │
│ [ 💡 Click tag to ask agent ]│ [ Input: Ask follow-up...         ] [ 🚀 ]│ [ Interactive Live Spanner Canvas ]   │
└──────────────────────────────┴───────────────────────────────────────────┴───────────────────────────────────────┘
```

---

## 3. Data Models & API Contracts

### 3.1 `GET /api/v1/catalog/hierarchy`
Returns full structured plant hierarchy:
```json
{
  "status": "SUCCESS",
  "total_equipment": 54,
  "total_instruments": 256,
  "sections": [
    {
      "section_id": "SEC-23",
      "name": "Cumene Cleavage & Decomposition Section (CDN)",
      "nodes": [
        {
          "node_id": "CDN-N02",
          "name": "Preflash Column & Vaporizer Section",
          "equipment": [
            {
              "tag": "E-2303",
              "name": "Preflash Column Steam Heater",
              "type": "Heat Exchanger (Shell & Tube)",
              "operating_temp_c": 115.0,
              "operating_press_barg": 0.8,
              "drawing_ref": "14780-8120-20-23-0002",
              "instruments": [
                {
                  "tag": "TXSHH-0502A",
                  "type": "Temperature Transmitter High-High",
                  "sil_rating": "SIL 1",
                  "voting_logic": "1oo2",
                  "is_sis_initiator": true
                },
                {
                  "tag": "TXSHH-0502B",
                  "type": "Temperature Transmitter High-High",
                  "sil_rating": "SIL 1",
                  "voting_logic": "1oo2",
                  "is_sis_initiator": true
                }
              ]
            }
          ]
        }
      ]
    }
  ]
}
```

### 3.2 `GET /api/v1/agent/stream?prompt=...&session_id=...`
SSE streaming endpoint accepting persistent `session_id`.
Events emitted:
- `event: armor_inspection`: `{"status": "PASSED|BLOCKED|OUT_OF_DOMAIN", "inspection_time_ms": 0.8, "verdict": "ALLOWED"}`
- `event: thought`: `{"thought_chunk": "...", "timestamp_ms": 1234}`
- `event: tool_invoked`: `{"tool_name": "...", "tool_args": {...}, "invoking_subagent": "OrchestratorAgent"}`
- `event: tool_result`: `{"tool_name": "...", "latency_ms": 34.2, "result_preview": "..."}`
- `event: message_delta`: `{"content": "...", "text_delta": "..."}`
- `event: telemetry_waterfall`: `{"total_ms": 842.1, "phase1_ms": 0.8, "phase2_ms": 45.0, "phase3_ms": 38.0, "phase4_ms": 758.3}`
- `event: message_done`: `{"status": "COMPLETED", "session_id": "..."}`

---

## 4. Step-by-Step Implementation Plan

### Step 1: Specification Authoring & Protocol Compliance
- Author formal SDD `specs/features/SPEC-20260920-TRI-PANE-MISSION-CONTROL-COCKPIT.md`.
- Update `specs/README.md`.

### Step 2: Backend API Endpoints & Session Management (`server/main.py`)
- Implement `GET /api/v1/catalog/hierarchy` grouping Spanner DB equipment and instruments by Section and HAZOP Node (`CDN-N01`, `CDN-N02`, `CDN-N03`, `CDN-N04`, `OXI-N01`, `ALKY-N01`).
- Update `/api/v1/agent/stream` to honor `session_id` and stream per-step tool execution durations and waterfall breakdowns.
- Implement `POST /api/v1/session/reset` to support clean session recycling.

### Step 3: Tri-Pane Mission Control UI Redesign & Multi-Turn Synchronization (`server/static/index.html`)
- **Left Pane:** Plant hierarchy accordion tree with search filter, badge indicators, and quick action chips (`🛡️ Query Interlocks`, `⚡ Run HAZOP`, `📋 Certified P&ID`).
- **Center Pane:** Conversational chat thread with message bubbles, Markdown formatting, auto-scroll, persistent `session_id` in localStorage, non-destructive DOM insertion (`insertAdjacentHTML`), and `🔄 Reset Session` control.
  - Interactive Conversation Turn Header: Each turn bubble renders `Turn #N` with an interactive badge: `🟢 Showing in Right Pane` (active) / `📊 View Stats` (clickable).
  - Resilient streaming renderer: try/catch markdown parser with fallback, inline error status on disconnect.
- **Right Pane:** Multi-Turn Inspector defaulting to the latest conversation turn:
  - Step latency waterfall card reflecting the selected turn's latency breakdown.
  - Live Tool Invocation Drawer listing tools executed in the selected turn.
  - Model Thought Stream for the selected turn.
  - Interactive HTML5 Spanner graph canvas focused on the selected turn's target node.
  - Dataplex certified drawing lineage and GCS wiki docs for the selected turn's target node.
  - Top header indicator showing which turn is currently under inspection with a `[Jump to Latest]` button.

### Step 4: Unit Testing & Property-Based Testing
- Unit tests in `tests/test_frontend_proxy.py`:
  - Verify `GET /api/v1/catalog/hierarchy` status, structure, and integrity.
  - Verify session persistence and reset.
  - Verify SSE telemetry event streaming with `session_id`.
  - Verify proxy stream lifecycle sequencing (telemetry waterfall emitted before message_done).
  - Verify parameter-aware HAZOP deviation routing.
- Property-Based Tests (Hypothesis):
  - Every equipment item in the hierarchy has non-empty tag and valid section/node linkage.
  - Total equipment count in hierarchy matches database count.
  - Waterfall latency phases sum monotonically to total elapsed time.

### Step 5: End-to-End Testing & Golden Benchmark Verification
- Run test regressions asserting 100% test pass rate.
- Verify frontend responsiveness, middle pane output streaming, and turn switching.

### Step 6: Deployment & Post-Deploy Health Check
- Execute `./scripts/deploy.sh prod` (or Cloud Run deploy).
- Run post-deploy probe against `/healthz` and `/api/v1/catalog/hierarchy`.

### Step 7: Progress Report Synchronization
- Author `specs/plan/PROGRESS_REPORT_20260920_TRI_PANE_COCKPIT_REDESIGN.md`.
- Synchronize `specs/README.md`.

