# Refinery Phenol Process Safety Expert & Multi-Agent Platform

An enterprise multi-agent petrochemical process safety system built for chemical engineers, safety specialists, and HAZOP teams. Powered by **Google Cloud Vertex AI (Gemini 3.8 Flash)**, **Cloud Spanner ISO GQL Property Graph**, **Google Cloud Model Armor**, and **Dataplex Knowledge Catalog**.

---

## 🚀 Key Capabilities (Journey 1 Mission Control Cockpit)

1. **Dual-Pane Interactive Process Cockpit:**
   - **Left Pane (Conversational AI & Security Shield):**
     - Streaming Gemini 3.8 Flash reasoning with real-time thought chunk cards.
     - Sleek **Quick Query Chips** (`🛡️ E-2303 Thermal Trips`, `��️ V-2301 Feed Streams`, `❓ Clarify Pump`, `🚨 Attack Test`).
     - Sub-millisecond **Google Cloud Model Armor** live guardrail (`<1ms` inspection badge, prompt injection intercept alert).
     - **Two-Tier Human-in-the-Loop (HITL) Disambiguation:** Interactive UI selection pills for generic tags (e.g. pumps, exchangers).
   - **Right Pane (Deep Technical Inspector — 3 Consolidated Tabs):**
     - **Tab 1: Spanner Knowledge Graph & ISO GQL Console:** Subgraph extraction focusing on target equipment, 1-hop upstream/downstream feeds, and SIS interlocks, alongside a live ISO GQL console with TrueTime transaction tokens.
     - **Tab 2: Dataplex Lineage & GCS LLM-Wiki:** Consolidated OEMS-005 metadata aspects, certified As-Built drawing lineage (`14780-8120-25-23-0005_Z1.pdf`), and GCS Markdown technical documentation viewer.
     - **Tab 3: Observability & Latency Waterfall Breakdown:** Multi-phase millisecond breakdown across request phases (Model Armor <1ms, Orchestrator ~115ms, Retriever MCP ~42ms, Gemini 3.8 Flash ~740ms).

---

## 🔒 Enterprise Cloud Security: Zero Gemini API Key in Production

In accordance with enterprise Google Cloud security governance:
- **Production (`PROD_*`):** Uses **Google Cloud Vertex AI** via Application Default Credentials (ADC) and Cloud Run Service Account IAM (`roles/aiplatform.user`). **ZERO Gemini API keys** are used, stored, or passed in production.
- **Model Armor Guardrail:** Pre-flight inspection catches prompt injections, jailbreaks, and safety overrides in `< 1ms` before any downstream agent reasoning or database queries occur.
- **Org Policy Ingress Compliance:** Cloud Run deployed with `run.googleapis.com/invoker-iam-disabled: 'true'`, guaranteeing 100% compliance with `constraints/iam.allowedPolicyMemberDomains` (zero `allUsers` IAM bindings).

---

## ⚙️ Centralized Multi-Environment Configuration (`.env`)

All configurable parameters for **both Non-Prod and Prod environments** are maintained in a **single unified `.env` file** (templated in `.env.example`):

```bash
# Core Shared Configuration
GCP_PROJECT=your-gcp-project-id
GCP_REGION=asia-southeast1
GENAI_LOCATION=asia-southeast1
DEFAULT_MODEL=gemini-3.8-flash
SPANNER_INSTANCE=phenol-process-graph
SPANNER_DATABASE=safety-db
ARTIFACT_REGISTRY_REPO=phenol-repo
GITHUB_REPO_URL=https://github.com/your-org/pttep-kg.git

# Gemini Enterprise Agent Platform Backend (Reasoning Engine Resource ID)
AGENT_ENGINE_RESOURCE_NAME=projects/YOUR_PROJECT_NUMBER/locations/asia-southeast1/reasoningEngines/YOUR_REASONING_ENGINE_ID

# Non-Prod Environment
NONPROD_ENVIRONMENT_NAME=development
NONPROD_SERVICE_NAME=phenol-process-safety-nonprod
NONPROD_DEPLOYMENT_ID=phenol-container-nonprod
NONPROD_MIN_INSTANCES=0
NONPROD_MAX_INSTANCES=3
NONPROD_USE_VERTEXAI=true
NONPROD_GEMINI_API_KEY=""

# Production Environment (ZERO API Key — Vertex AI ADC / Service Account IAM)
PROD_ENVIRONMENT_NAME=production
PROD_SERVICE_NAME=phenol-process-safety-prod
PROD_DEPLOYMENT_ID=phenol-container-prod
PROD_GCS_RAW_BUCKET=phenol-raw-docs-your-gcp-project-id-prod
PROD_GCS_WIKI_BUCKET=phenol-llm-wiki-your-gcp-project-id-prod
PROD_MIN_INSTANCES=1
PROD_MAX_INSTANCES=10
PROD_USE_VERTEXAI=true
PROD_GEMINI_API_KEY=""
PROD_SERVICE_ACCOUNT=phenol-runner-sa@your-gcp-project-id.iam.gserviceaccount.com
PROD_MODEL_ARMOR_TEMPLATE=phenol-safety-armor-template
```

---

## 🚢 Deployment & Redeployment Guide (Frontend & Backend)

The system is decoupled into two independent deployable services:
1. **AI Reasoning Backend:** Gemini Enterprise Agent Platform (`agent_runtime` / Vertex AI Reasoning Engine) deployed via `agents-cli`.
2. **Frontend Web Cockpit:** Thin SSE streaming proxy and web UI container deployed to **Google Cloud Run**.

### 1. Prerequisites
Ensure active Google Cloud credentials and environment variables:
```bash
# 1. On Cloudtop: Ensure LOAS certificate is fresh
gcert

# 2. Authenticate Application Default Credentials (ADC)
gcloud auth application-default print-access-token >/dev/null

# 3. Set default GCP project and region
gcloud config set project cs-poc-y03r7kmfyov4kilzg50fd7s
gcloud config set compute/region asia-southeast1
```

---

### 2. Full-Stack One-Command Deployment (`--all`)
To deploy or redeploy **both the AI Reasoning Backend and Frontend Web Cockpit** in a single synchronized workflow:

```bash
# Production Full-Stack Redeployment (Backend first, then Frontend wired to it)
./scripts/deploy.sh prod --all

# Non-Prod Full-Stack Redeployment
./scripts/deploy.sh nonprod --all

# Dry-run validation (inspect resolved configuration without deploying)
./scripts/deploy.sh prod --dry-run
```

---

### 3. Deploying / Redeploying Backend Only (`agents-cli`)
Deploy or redeploy the **AI Reasoning Backend** whenever you modify:
- Agent prompts and orchestration logic (`app/agent.py`, `app/hazop/agent.py`)
- Tool definitions and database connectors (`app/tools.py`)
- Model Armor pre-flight security callbacks (`app/security/model_armor.py`)

#### Option A: Using the Deployment Script (Recommended)
```bash
# Deploy backend to Production Agent Platform runtime
./scripts/deploy.sh prod

# Deploy backend to Non-Prod Agent Platform runtime
./scripts/deploy.sh nonprod
```

#### Option B: Direct `agents-cli` Command
```bash
# Deploy to Gemini Enterprise Agent Platform runtime
agents-cli deploy \
  --project=cs-poc-y03r7kmfyov4kilzg50fd7s \
  --region=asia-southeast1

# Inspect deployment status and live resource ID
agents-cli deploy --status
agents-cli deploy --list
```

> **Note on Resource IDs:** If `agents-cli deploy` provisions a new Reasoning Engine ID, update `AGENT_ENGINE_RESOURCE_NAME` in `.env` so the frontend directs requests to the new instance:
> ```bash
> # Example:
> AGENT_ENGINE_RESOURCE_NAME=projects/114618371568/locations/asia-southeast1/reasoningEngines/<NEW_ENGINE_ID>
> ```

---

### 4. Deploying / Redeploying Frontend Only (`Cloud Run`)
Deploy or redeploy the **Frontend Web Cockpit** whenever you modify:
- User interface layout or styling (`server/static/index.html`, JavaScript/CSS)
- FastAPI routing or endpoints (`server/main.py`)
- SSE streaming proxy layer (`server/proxy.py`)
- Dockerfile packaging or dependencies

#### Option A: Using the Deployment Script (Recommended)
```bash
# Deploy frontend container to Production Cloud Run
./scripts/deploy.sh prod --app

# Deploy frontend container to Non-Prod Cloud Run
./scripts/deploy.sh nonprod --app
```

#### Option B: Direct Cloud Build & Cloud Run Commands
```bash
# 1. Build and push container image via Cloud Build
gcloud builds submit \
  --tag asia-southeast1-docker.pkg.dev/cs-poc-y03r7kmfyov4kilzg50fd7s/phenol-repo/phenol-process-safety-prod:latest \
  .

# 2. Deploy container to Google Cloud Run
gcloud run deploy phenol-process-safety-prod \
  --image asia-southeast1-docker.pkg.dev/cs-poc-y03r7kmfyov4kilzg50fd7s/phenol-repo/phenol-process-safety-prod:latest \
  --region asia-southeast1 \
  --service-account phenol-runner-sa@cs-poc-y03r7kmfyov4kilzg50fd7s.iam.gserviceaccount.com \
  --min-instances 1 \
  --max-instances 10 \
  --cpu 2000m \
  --memory 2Gi \
  --set-env-vars="USE_REAL_SPANNER=true,GCP_PROJECT=cs-poc-y03r7kmfyov4kilzg50fd7s,GCP_REGION=asia-southeast1,SPANNER_INSTANCE=phenol-process-graph,SPANNER_DATABASE=safety-db,DATAPLEX_ENTRY_GROUP=phenol-psi,PROD_GCS_WIKI_BUCKET=phenol-llm-wiki-cs-poc-y03r7kmfyov4kilzg50fd7s-prod,AGENT_ENGINE_RESOURCE_NAME=projects/114618371568/locations/asia-southeast1/reasoningEngines/5733267043596107776,FORCE_OFFLINE_MOCK=false,PROD_USE_VERTEXAI=true,PROD_MODEL_ARMOR_TEMPLATE=phenol-safety-armor-template"
```

#### Verifying Frontend Deployment
```bash
# Check service health endpoint
curl -f https://phenol-process-safety-prod-114618371568.asia-southeast1.run.app/healthz
# Expected output: {"status":"healthy"}
```

---

### 5. Synchronizing Cloud Data Tiers (Spanner, Dataplex & GCS)

If you modify wiki markdown files, database seeds, or equipment descriptions:

```bash
# 1. Synchronize GCS LLM-Wiki bucket
gcloud storage rsync -r wiki/ gs://phenol-llm-wiki-cs-poc-y03r7kmfyov4kilzg50fd7s-prod/wiki/ --delete-unmatched-destination-objects

# 2. Synchronize Dataplex Knowledge Catalog entries
./.venv/bin/python scripts/sync_dataplex_catalog.py

# 3. Seed / verify Cloud Spanner database
./.venv/bin/python database/init_db.py
```

---

## 💻 Local Development & Testing

```bash
# 1. Install dependencies
uv venv && source .venv/bin/activate
uv pip install -r requirements.txt

# 2. Run local Web Cockpit server
PYTHONPATH=. python -m uvicorn server.main:app --host 0.0.0.0 --port 8000

# 3. Access local UI in browser
open http://127.0.0.1:8000

# 4. Interactive ADK CLI Chat
adk run app

# 5. Run full test suite (Unit & Property-Based Tests)
PYTHONPATH=. pytest

# 6. Run Golden Agent Evaluation Benchmark
agents-cli eval run --config tests/eval/eval_config.yaml
```

---

## 📚 Technical Architecture & Specifications

- **Consolidated System Specification:** [`specs/features/CONSOLIDATED_FEATURE_SPECIFICATION.md`](./specs/features/CONSOLIDATED_FEATURE_SPECIFICATION.md)
- **Consolidated Master Implementation Plan:** [`specs/plan/CONSOLIDATED_IMPLEMENTATION_PLAN.md`](./specs/plan/CONSOLIDATED_IMPLEMENTATION_PLAN.md)
- **Architecture Documentation:** [`docs/architecture.md`](./docs/architecture.md)
- **Interactive Dark-Themed SVG Architecture Diagram:** Open [`docs/architecture.html`](./docs/architecture.html) in any browser.
- **Master SDD Index:** [`specs/README.md`](./specs/README.md)
