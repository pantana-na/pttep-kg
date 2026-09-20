# Specification: Official Google ADK & Gemini Enterprise Agent Platform Refactor

- **Specification ID:** `SPEC-20260918-GOOGLE-ADK-AND-AGENT-RUNTIME-REFACTOR`
- **Status:** APPROVED & IN IMPLEMENTATION
- **Author:** Antigravity AI Platform Architecture
- **Date:** 2026-09-18
- **Governing Rules:** [`GEMINI.md`](../../GEMINI.md) | [`_agents/rules/spec_driven_development.md`](../../_agents/rules/spec_driven_development.md) | [`_agents/rules/devops_security_and_quality_standards.md`](../../_agents/rules/devops_security_and_quality_standards.md) | [`_agents/rules/google_adk_and_agent_runtime.md`](../../_agents/rules/google_adk_and_agent_runtime.md)
- **Target Environments:** Gemini Enterprise Agent Platform (`agent_runtime`), Cloud Run (`phenol-process-safety-prod`), Local (`adk run` / `adk api_server`)

---

## 1. Executive Summary & Goals

### 1.1 Problem Statement
The refinery process safety platform's multi-agent system was previously implemented using direct, custom Python orchestrator classes and raw `google-genai` SDK calls. While functional, it lacked standard conformance with Google's enterprise agent ecosystem:
1. **No Standard ADK Agent Primitives:** Agents did not inherit from `google.adk.agents.Agent` or `LlmAgent`, preventing standardization across Google tools.
2. **Missing Gemini Enterprise Agent Platform Lifecycle:** The platform could not be managed, evaluated, or deployed via `agents-cli` (`agents-cli deploy`, `agents-cli eval`).
3. **Missing ADK Manifest:** Lacked `agents-cli-manifest.yaml` linking the project to the Gemini Enterprise Agent Runtime.

### 1.2 Goals & Success Criteria
1. **Official `google-adk` Implementation:** Refactor subagents (`Orchestrator`, `Retriever`, `HazopStudy`, `Database`, `Extractor`) into official `google.adk.agents.Agent` / `LlmAgent` and `google.adk.apps.App` instances with typed `FunctionTool` declarations.
2. **Gemini Enterprise Agent Platform Runtime Integration:**
   - Author `agents-cli-manifest.yaml` targeting `agent_runtime` in `asia-southeast1`.
   - Provide standard ADK app entry point (`app/agent.py` or `agents/adk_app.py`) for `adk run`, `adk api_server`, and `agents-cli playground`.
3. **Unified Evaluation via `agents-cli eval`:** Standardize evaluation cases into ADK-compliant eval datasets and integrate `agents-cli eval run` into verification.
4. **Deploy Automation via `agents-cli deploy`:** Update `./scripts/deploy.sh` to support deploying directly to the Gemini Enterprise Agent Platform runtime (`agent_runtime`) and Cloud Run.
5. **Inline Model Armor Pre-Flight Hook:** Implement `before_agent_callback` in ADK to intercept adversarial prompt injections before tool execution.
6. **Zero Breaking Changes to Mission Control UI:** Maintain full backward compatibility for the dual-pane UI (`server/main.py`).
7. **Living Documentation & Agent Rules Update:** Update `_agents/rules/`, `GEMINI.md`, `AGENTS.md`, and `docs/architecture.md`.

---

## 2. Target Architecture: Google ADK & Gemini Enterprise Agent Runtime

```mermaid
flowchart TD
    User["Engineer / Web UI"] --> Ingress{"Ingress Layer"}
    
    subgraph Ingress["Dual Ingress Support"]
        Ingress -->|"Dual-Pane UI / SSE"| FastAPI["FastAPI Server (server/main.py)"]
        Ingress -->|"ADK Protocol / A2A"| ADKServer["ADK API Server (adk api_server)"]
        Ingress -->|"CLI Operators / CI/CD"| ACLI["Agents CLI (agents-cli)"]
    end

    subgraph ADKApp["Google ADK App Runtime (google.adk.apps.App)"]
        FastAPI --> ADKRoot["🛡️ Root Orchestrator Agent (google.adk.agents.Agent)<br/>Model: Vertex AI Gemini 3.7 Flash"]
        ADKServer --> ADKRoot
        ACLI --> ADKRoot

        ADKRoot --> ArmorHook["🔒 before_agent_callback<br/>Google Cloud Model Armor (asia-southeast1)"]

        subgraph ADKSubagents["Managed ADK Subagents & Tools"]
            ADKRoot --> RetrieverAgent["🔍 Retriever ADK Subagent<br/>• spanner_graph_query<br/>• spanner_vector_search<br/>• query_knowledge_catalog<br/>• read_gcs_wiki_document"]
            ADKRoot --> HazopAgent["📋 HazopStudy ADK Subagent<br/>• evaluate_hazop_deviation<br/>• calculate_ram_lopa_risk"]
            ADKRoot --> ExtractorAgent["📄 Extractor ADK Subagent<br/>• parse_pid_drawing_ocr"]
            ADKRoot --> DatabaseAgent["🏛️ Database ADK Subagent<br/>• sync_spanner_entities"]
        end
    end

    subgraph CloudServices["100% Live Managed Google Cloud Services"]
        RetrieverAgent --> Spanner[("Google Cloud Spanner<br/>ISO GQL Graph & Vector")]
        RetrieverAgent --> Dataplex[("Dataplex Knowledge Catalog<br/>phenol-psi")]
        RetrieverAgent --> GCS[("Google Cloud Storage<br/>gs://phenol-llm-wiki-...")]
        ArmorHook --> ModelArmor["Google Cloud Model Armor"]
    end
```

---

## 3. Component Specifications

### 3.1 `agents-cli-manifest.yaml`
```yaml
name: "phenol-process-safety"
acli_version: "1.1.0"
agent_directory: "app"
region: "asia-southeast1"
base_template: "adk"
language: "python"
create_params:
  deployment_target: "agent_runtime"
  session_type: "none"
  cicd_runner: "google_cloud_build"
  is_a2a: true
  agent_guidance_filename: "GEMINI.md"
```

### 3.2 ADK App & Root Agent Structure (`app/agent.py`)
```python
from google.adk.agents import Agent
from google.adk.apps import App
from google.adk.models import Gemini

# 1. Tools defined as typed Python callables with docstrings
# 2. Subagents defined with specialized instructions & tool sets
# 3. Root agent configured with before_agent_callback for Model Armor
# 4. App exported as root entrypoint for ADK CLI & runtime
```

---

## 4. Step-by-Step Implementation Plan

| Step | Component | Target Files | Completion Criteria |
| :--- | :--- | :--- | :--- |
| **Step 1.0** | **Agent Rules & Governance Update** | `_agents/rules/google_adk_and_agent_runtime.md`<br>`GEMINI.md`<br>`AGENTS.md` | Formal ADK and Gemini Enterprise Agent Platform governance codified. |
| **Step 2.0** | **Architecture Documentation Update** | `docs/architecture.md`<br>`docs/spanner-graph-and-knowledge-catalog-architecture.md` | Architecture docs and diagrams reflect official ADK runtime & tools. |
| **Step 3.0** | **ADK Dependency & Manifest Setup** | `requirements.txt`<br>`agents-cli-manifest.yaml` | `google-adk>=2.9.0` pinned; `agents-cli info` recognizes the project. |
| **Step 4.0** | **Official Google ADK Agent Implementation** | `app/agent.py`<br>`app/__init__.py`<br>`agents/adk_tools.py` | Root `Agent` + Subagents + Model Armor `before_agent_callback` pass ADK validation. |
| **Step 5.0** | **Dual Ingress & UI Compatibility** | `server/main.py`<br>`agents/orchestrator/agent.py` | FastAPI SSE stream invokes ADK agent while preserving dual-pane UI events. |
| **Step 6.0** | **Unit & Property-Based Tests for ADK** | `tests/test_adk_agents.py`<br>`tests/` | Deterministic unit tests and generative PBTs for ADK agents and tools pass 100%. |
| **Step 7.0** | **Evaluation & Deployment Lifecycle** | `evals/`<br>`scripts/deploy.sh` | `agents-cli eval` and `agents-cli deploy` verified. Living plan progress report generated. |

---

## 5. Test Strategy & Invariants

- **Unit Tests (`tests/test_adk_agents.py`):**
  - Verify ADK `Agent` and `App` initialization and tool registration.
  - Verify Model Armor `before_agent_callback` blocks adversarial prompts before tool dispatch.
  - Verify tool invocation returns structured results matching Pydantic schemas.
- **Property-Based Tests (PBT with Hypothesis):**
  - Invariant: Any query containing blocked injection patterns MUST trigger Model Armor interception without tool execution.
  - Invariant: Tool outputs must always return finite numbers and non-null status strings across generative equipment inputs.
