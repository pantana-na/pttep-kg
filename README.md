# Refinery Phenol Process Safety Expert & Multi-Agent Platform

An enterprise multi-agent petrochemical process safety system built for chemical engineers, safety specialists, and HAZOP teams. Powered by **Google Cloud Vertex AI (Gemini 3.8 Flash)**, **Cloud Spanner ISO GQL Property Graph**, **Google Cloud Model Armor**, and **Dataplex Knowledge Catalog**.

---

## 🚀 Key Capabilities (Journey 1 Mission Control Cockpit)

1. **Dual-Pane Interactive Process Cockpit:**
   - **Left Pane (Conversational AI & Security Shield):**
     - Streaming Gemini 3.8 Flash reasoning with real-time thought chunk cards.
     - Sleek **Quick Query Chips** (`🛡️ E-2303 Thermal Trips`, `🕸️ V-2301 Feed Streams`, `❓ Clarify Pump`, `🚨 Attack Test`).
     - Sub-millisecond **Google Cloud Model Armor** live guardrail (`<1ms` inspection badge, prompt injection intercept alert).
     - **Two-Tier Human-in-the-Loop (HITL) Disambiguation:** Interactive UI selection pills for generic tags (e.g. pumps, exchangers).
   - **Right Pane (Deep Technical Inspector — 3 Consolidated Tabs):**
     - **Tab 1: Spanner Knowledge Graph & ISO GQL Console:** Subgraph extraction focusing on target equipment, 1-hop upstream/downstream feeds, and SIS interlocks, alongside a live ISO GQL console with TrueTime transaction tokens.
     - **Tab 2: Dataplex Lineage & GCS LLM-Wiki:** Consolidated OEMS-005 metadata aspects, certified As-Built drawing lineage (`14780-8120-25-23-0005_Z1.pdf`), and GCS Markdown technical documentation viewer.
     - **Tab 3: Observability & Latency Waterfall Breakdown:** Multi-phase millisecond breakdown across request phases (Model Armor <1ms, Orchestrator ~115ms, Retriever MCP ~42ms, Gemini 3.8 Flash ~740ms).

---

## �� Enterprise Cloud Security: Zero Gemini API Key in Production

In accordance with enterprise Google Cloud security governance:
- **Production (`PROD_*`):** Uses **Google Cloud Vertex AI** via Application Default Credentials (ADC) and Cloud Run Service Account IAM (`roles/aiplatform.user`). **ZERO Gemini API keys** are used, stored, or passed in production.
- **Model Armor Guardrail:** Pre-flight inspection catches prompt injections, jailbreaks, and safety overrides in `< 1ms` before any downstream agent reasoning or database queries occur.
- **Org Policy Ingress Compliance:** Cloud Run deployed with `run.googleapis.com/invoker-iam-disabled: 'true'`, guaranteeing 100% compliance with `constraints/iam.allowedPolicyMemberDomains` (zero `allUsers` IAM bindings).

---

## ⚙️ Centralized Multi-Environment Configuration (`.env`)

All parameters for **both Non-Prod and Prod environments** are maintained in a **single unified `.env` file** (templated in `.env.example`):

```bash
# Core Shared Configuration
GCP_PROJECT=cs-poc-y03r7kmfyov4kilzg50fd7s
GCP_REGION=asia-southeast1
GENAI_LOCATION=asia-southeast1
DEFAULT_MODEL=gemini-3.8-flash
SPANNER_INSTANCE=phenol-process-graph
SPANNER_DATABASE=safety-db
ARTIFACT_REGISTRY_REPO=phenol-repo

# Non-Prod Environment
NONPROD_ENVIRONMENT_NAME=development
NONPROD_SERVICE_NAME=phenol-process-safety-nonprod
NONPROD_MIN_INSTANCES=0
NONPROD_MAX_INSTANCES=3
NONPROD_USE_VERTEXAI=true
NONPROD_GEMINI_API_KEY=""

# Production Environment (ZERO API Key — Vertex AI ADC / Service Account IAM)
PROD_ENVIRONMENT_NAME=production
PROD_SERVICE_NAME=phenol-process-safety-prod
PROD_MIN_INSTANCES=1
PROD_MAX_INSTANCES=10
PROD_USE_VERTEXAI=true
PROD_GEMINI_API_KEY=""
PROD_SERVICE_ACCOUNT=phenol-runner-sa@cs-poc-y03r7kmfyov4kilzg50fd7s.iam.gserviceaccount.com
```

---

## 🚀 Enterprise Agent Platform & CLI Deployment (`agents-cli`)

The multi-agent system is deployed to the **Gemini Enterprise Agent Platform (`agent_runtime`)** using official **`agents-cli`**:

```bash
# 1. Direct Agent Platform Deployment via agents-cli
agents-cli deploy --project=cs-poc-y03r7kmfyov4kilzg50fd7s --region=asia-southeast1

# 2. Check deployment status or view deployed agents
agents-cli deploy --status
agents-cli deploy --list

# 3. Evaluate Agent Performance & Golden Benchmark Rubrics
agents-cli eval generate --config tests/eval/eval_config.yaml
agents-cli eval grade

# 4. Local Interactive ADK CLI Chat
adk run app
```

---

## 🚢 Decoupled Multi-Target Deployment Script (`scripts/deploy.sh`)

[`scripts/deploy.sh`](./scripts/deploy.sh) orchestrates decoupled deployments for both the **AI Reasoning Backend (`Gemini Enterprise Agent Platform`)** and the **Frontend Web Cockpit (`Google Cloud Run`)**:

```bash
# 1. Deploy AI Reasoning Backend to Gemini Enterprise Agent Platform via agents-cli (Default)
./scripts/deploy.sh nonprod             # Non-Prod Agent Runtime
./scripts/deploy.sh prod                # Production Agent Runtime (Vertex AI ADC)

# 2. Deploy Frontend Web Cockpit Container to Cloud Run (Proxies to Agent Platform Backend)
./scripts/deploy.sh nonprod --app
./scripts/deploy.sh prod --app

# 3. Full-Stack Deployment (agents-cli Backend first + Cloud Run Frontend wired to it)
./scripts/deploy.sh prod --all

# 4. Dry-Run Validation
./scripts/deploy.sh prod --dry-run
```

The script automatically:
1. Loads and validates multi-environment variables from unified `.env`.
2. Verifies zero-mock cloud synchronization: checks Dataplex Catalog and ensures Model Armor RAI filters are `LOW_AND_ABOVE`.
3. Dispatches `agents-cli deploy` targeting `agent_runtime` in `asia-southeast1` using [`agents-cli-manifest.yaml`](./agents-cli-manifest.yaml).
4. When `--app` or `--all` is set, builds and deploys the frontend web container to Cloud Run with `invoker-iam-disabled: 'true'` compliance and automatic `AGENT_ENGINE_RESOURCE_NAME` backend binding.

---

## 💻 Local Development & Testing

```bash
# 1. Install dependencies
uv venv && source .venv/bin/activate
uv pip install -r requirements.txt

# 2. Run local server
PYTHONPATH=. python -m uvicorn server.main:app --host 0.0.0.0 --port 8000

# 3. Access local Mission Control UI
open http://127.0.0.1:8000

# 4. Run automated test suite (Unit & Property-Based Tests)
PYTHONPATH=. pytest
```

---

## 📚 Technical Architecture Documentation

- **Architecture Walkthrough:** [`docs/architecture.md`](./docs/architecture.md)
- **Interactive Dark-Themed SVG Architecture Diagram:** Open [`docs/architecture.html`](./docs/architecture.html) in any browser.
- **Specifications & SDDs:** [`specs/README.md`](./specs/README.md)
