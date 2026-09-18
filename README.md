# Refinery Phenol Process Safety Expert & Multi-Agent Platform

An enterprise multi-agent petrochemical process safety system built for chemical engineers, safety specialists, and HAZOP teams. Powered by **Google Cloud Vertex AI (Gemini 3.7 Flash)**, **Cloud Spanner ISO GQL Property Graph**, **Google Cloud Model Armor**, and **Dataplex Knowledge Catalog**.

---

## 🚀 Key Capabilities (Journey 1 Mission Control Cockpit)

1. **Dual-Pane Interactive Process Cockpit:**
   - **Left Pane (Conversational AI & Security Shield):**
     - Streaming Gemini 3.7 Flash reasoning with real-time thought chunk cards.
     - Sleek **Quick Query Chips** (`🛡️ E-2303 Thermal Trips`, `🕸️ V-2301 Feed Streams`, `❓ Clarify Pump`, `🚨 Attack Test`).
     - Sub-millisecond **Google Cloud Model Armor** live guardrail (`<1ms` inspection badge, prompt injection intercept alert).
     - **Two-Tier Human-in-the-Loop (HITL) Disambiguation:** Interactive UI selection pills for generic tags (e.g. pumps, exchangers).
   - **Right Pane (Deep Technical Inspector — 3 Consolidated Tabs):**
     - **Tab 1: Spanner Knowledge Graph & ISO GQL Console:** Subgraph extraction focusing on target equipment, 1-hop upstream/downstream feeds, and SIS interlocks, alongside a live ISO GQL console with TrueTime transaction tokens.
     - **Tab 2: Dataplex Lineage & GCS LLM-Wiki:** Consolidated OEMS-005 metadata aspects, certified As-Built drawing lineage (`14780-8120-25-23-0005_Z1.pdf`), and GCS Markdown technical documentation viewer.
     - **Tab 3: Observability & Latency Waterfall Breakdown:** Multi-phase millisecond breakdown across request phases (Model Armor <1ms, Orchestrator ~115ms, Retriever MCP ~42ms, Gemini 3.7 Flash ~740ms).

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
DEFAULT_MODEL=gemini-3.7-flash
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

## 🚢 Automated Cloud Deployment Script (`scripts/deploy.sh`)

Deploying the platform to Google Cloud is fully automated via [`scripts/deploy.sh`](./scripts/deploy.sh):

```bash
# 1. Validate configuration and commands (Dry-Run Mode)
./scripts/deploy.sh nonprod --dry-run
./scripts/deploy.sh prod --dry-run

# 2. Provision Infrastructure via Google Cloud Infrastructure Manager & Terraform (GEMINI.md Rule 9)
./scripts/deploy.sh nonprod --infra
./scripts/deploy.sh prod --infra

# 3. Deploy Application Container (Default: Cloud Build + Cloud Run)
./scripts/deploy.sh nonprod
./scripts/deploy.sh prod

# 4. Full Stack Provision & Deploy (Infra Manager Terraform + Container Build & Deploy)
./scripts/deploy.sh prod --all
```

The script automatically:
1. Loads and validates variables from `.env`.
2. Resolves environment profiles (`NONPROD_*` vs `PROD_*`).
3. For `--infra`: invokes `gcloud infra-manager deployments apply` targeting `phenol-container-nonprod` or `phenol-container-prod` using declarative Terraform files in `terraform/`.
4. For `--app`: submits container build to Google Cloud Build and deploys to Google Cloud Run with Vertex AI ADC, resource limits, and compliant labels (`run.googleapis.com/invoker-iam-disabled: 'true'`).
5. Performs an automated health check probe against `/healthz`.

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
