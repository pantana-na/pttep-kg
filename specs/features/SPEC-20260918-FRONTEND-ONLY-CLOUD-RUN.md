# SPEC-20260918-FRONTEND-ONLY-CLOUD-RUN: Frontend-Only Cloud Run & Agent Platform Backend Decoupling

## Status: APPROVED
**Owner:** Core Engineering / Agent Architecture Team  
**Governed by:** `GEMINI.md` (Rules 1, 8, 9, 10, 11, 12), `_agents/rules/spec_driven_development.md`  
**Target Environment:** Non-Prod (`development`) & Prod (`production`)  
**GenAI Model:** `gemini-3.8-flash` (strictly enforced repository-wide)  

---

## 1. Problem Statement & Background

Previously, the Cloud Run service bundled both the web frontend cockpit (`server/static/index.html`) and the multi-agent reasoning execution loop (`OrchestratorAgent`, `HazopStudyAgent`, Spanner Graph MCP tools) within a single container. 

To achieve enterprise scalability, compliance with the Google Agent Development Kit (ADK) mandate, and clear separation of concerns:
1. **Cloud Run** must serve **strictly as the Frontend**:
   - Lightweight web server serving the interactive single-page application (SPA).
   - Fast client proxy for SSE event streams and study lifecycle requests.
   - Zero local model reasoning or heavy LLM execution inside the Cloud Run container.
2. **Gemini Enterprise Agent Platform (`agent_runtime`)** serves as the **AI Reasoning Backend**:
   - Deployed via official `agents-cli deploy` toolchain targeting Vertex AI Agent Engines (`agent_runtime`).
   - Hosts the ADK Multi-Agent hierarchy (`root_agent`, `retriever_agent`, `hazop_agent`).
   - Direct integration with Cloud Spanner Graph, Vertex AI Gemini 3.8 Flash, GCS LLM-Wiki, Dataplex Knowledge Catalog, and Model Armor security guardrails.
   - Exposes standard Reasoning Engine HTTP endpoints (`/api/reasoning_engine`, `/api/stream_reasoning_engine`, and `:streamQuery`).

---

## 2. Architecture & Topology

```
┌─────────────────────────────────────────────────────────────────────────────────────────┐
│                                 USER / CLIENT BROWSER                                   │
│                        (Cockpit UI, Spanner Graph, RAM 5x5)                             │
└─────────────────────────────────────────┬───────────────────────────────────────────────┘
                                          │ HTTPS / SSE
                                          ▼
┌─────────────────────────────────────────────────────────────────────────────────────────┐
│                    GOOGLE CLOUD RUN (Strictly Frontend Web Server & Proxy)              │
│                                                                                         │
│  - Static Asset Serving: / (server/static/index.html)                                  │
│  - Liveness & Readiness Probes: /healthz                                                │
│  - Graph Cockpit Topology Proxy: /api/v1/graph/topology                                 │
│  - Lightweight SSE Proxy: /api/v1/agent/stream?prompt=...                               │
│  - Target Env Config: AGENT_ENGINE_RESOURCE_NAME                                        │
└─────────────────────────────────────────┬───────────────────────────────────────────────┘
                                          │ Vertex AI ADC / Internal IAM
                                          ▼
┌─────────────────────────────────────────────────────────────────────────────────────────┐
│             GEMINI ENTERPRISE AGENT PLATFORM (Vertex AI Reasoning Engine Backend)       │
│                                                                                         │
│  - Deployed via: agents-cli deploy --deployment-target=agent_runtime                     │
│  - Endpoints: :streamQuery / /api/stream_reasoning_engine / :query                      │
│  - Multi-Agent Hierarchy (Google ADK):                                                  │
│      ├── OrchestratorAgent (Root Lead Orchestrator)                                     │
│      ├── RetrieverAgent (Tri-Hybrid Spanner Graph + Vector + Keyword + GCS + Dataplex)   │
│      └── HazopAgent (5x5 RAM Matrix + LOPA IPL Safeguards)                              │
│  - LLM Model: gemini-3.8-flash                                                          │
│  - Inline Security: Google Cloud Model Armor Guardrail (LOW_AND_ABOVE)                   │
└─────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Data Models & API Contracts

### 3.1 Cloud Run Frontend Proxy Contracts
- `GET /`: Serves `server/static/index.html`.
- `GET /healthz`: Returns `{"status": "HEALTHY", "role": "frontend-web-cockpit", "service": "phenol-process-safety"}`.
- `GET /api/v1/adk/info`: Returns backend status, pointing to `AGENT_ENGINE_RESOURCE_NAME`.
- `GET /api/v1/agent/stream?prompt=...&session_id=...`:
  - If `AGENT_ENGINE_RESOURCE_NAME` is configured:
    - Calls backend Reasoning Engine via `:streamQuery` (`async_stream_query`).
    - Streams SSE chunks to client (`event: message_delta\ndata: {"text": "..."}\n\n`).
  - If `AGENT_ENGINE_RESOURCE_NAME` is unset (local development / offline testing):
    - Invokes local orchestrator fallback to preserve deterministic testing and offline development.

### 3.2 Backend Agent Runtime Adapter Contracts
- `POST /api/stream_reasoning_engine`:
  - Payload: `{"class_method": "async_stream_query", "input": {"user_id": "...", "session_id": "...", "message": "..."}}`
  - Response: Newline-delimited JSON stream of ADK event dictionaries.
- `POST /api/reasoning_engine`:
  - Payload: `{"class_method": "async_create_session", "input": {"user_id": "..."}}`
  - Response: `{"output": {"id": "session-xyz"}}`

---

## 4. Step-by-Step Implementation Plan

### Step 1: Specification Authoring & Architecture Alignment
- Author formal SDD document `specs/features/SPEC-20260918-FRONTEND-ONLY-CLOUD-RUN.md`.
- Update `specs/README.md`.

### Step 2: Reasoning Engine Adapter in Backend
- Ensure backend container exposes `/api/stream_reasoning_engine` and `/api/reasoning_engine` using `attach_reasoning_engine_routes(app)` from ADK.
- Ensure `google-cloud-aiplatform>=2.0.0` is registered in `requirements.txt`.

### Step 3: Refactor Cloud Run (`server/main.py`) to Frontend-Only Web & Proxy
- Add `AGENT_ENGINE_RESOURCE_NAME` configuration resolution from environment variables.
- Add `AgentRuntimeClient` to handle authenticated calls to the remote Vertex AI Reasoning Engine using Application Default Credentials (ADC) or Identity Tokens.
- Wire `/api/v1/agent/stream` to proxy incoming prompts to the remote backend, converting output chunks into SSE events.
- Retain local orchestrator fallback when `AGENT_ENGINE_RESOURCE_NAME` is empty or during offline unit testing.

### Step 4: Update Deployment Pipeline (`scripts/deploy.sh`)
- In `scripts/deploy.sh`:
  - Automatically read `remote_agent_runtime_id` from `deployment_metadata.json`.
  - Pass `AGENT_ENGINE_RESOURCE_NAME=${AGENT_ENGINE_ID}` into `--set-env-vars` when deploying Cloud Run (`--app` or `--all`).
  - Document the frontend-only deployment model in CLI help and summary banners.

### Step 5: Unit & Property-Based Testing
- Unit tests verifying:
  - Frontend proxy forwards stream requests to remote backend when configured.
  - Fallback cleanly handles unconfigured or offline scenarios.
  - Healthcheck reflects frontend role.
- Property-based tests verifying SSE chunk framing invariants across arbitrary string prompts.

### Step 6: Live Deployment & Verification
- Execute `agents-cli deploy` for backend Agent Runtime.
- Execute `./scripts/deploy.sh prod --app` for frontend Cloud Run.
- Live probe `/healthz` and verify end-to-end question answering via the deployed service URL.

### Step 7: Documentation & Progress Tracking
- Author `specs/plan/PROGRESS_REPORT_20260918_FRONTEND_ONLY_CLOUD_RUN.md`.
- Update `docs/architecture.md`, `docs/architecture.html`, and `README.md`.

---

## 5. Invariants & Acceptance Criteria

1. **Decoupled Architecture:** Cloud Run does not run local agent loops when `AGENT_ENGINE_RESOURCE_NAME` is set.
2. **Model Standard:** All models strictly `gemini-3.8-flash`.
3. **Zero API Keys in Prod:** 100% IAM & ADC.
4. **Zero Regex Logic:** All intent classification and agent routing are model-driven.
5. **Continuous Quality:** 100% test pass rate across unit and property-based test suites.
