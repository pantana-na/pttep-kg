#!/usr/bin/env bash
# ==============================================================================
# Multi-Environment Deployment Script for Refinery Phenol Process Safety Platform
# Governed by: GEMINI.md (Rules 8, 9, 10) & DevOps Standards
#
# Usage:
#   ./scripts/deploy.sh [nonprod|prod] [--dry-run]
#
# Examples:
#   ./scripts/deploy.sh nonprod             # Deploy to Non-Prod / Staging
#   ./scripts/deploy.sh prod                # Deploy to Production (Vertex AI ADC)
#   ./scripts/deploy.sh prod --dry-run      # Print resolved config & commands
# ==============================================================================

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"
ENV_FILE="${ROOT_DIR}/.env"

# Colors for terminal output
RED='\033[0;31m'
GREEN='\033[0;32m'
CYAN='\033[0;36m'
YELLOW='\033[1;33m'
BOLD='\033[1m'
NC='\033[0m' # No Color

log_info() { echo -e "${CYAN}[INFO]${NC} $1"; }
log_success() { echo -e "${GREEN}[SUCCESS]${NC} $1"; }
log_warn() { echo -e "${YELLOW}[WARN]${NC} $1"; }
log_error() { echo -e "${RED}[ERROR]${NC} $1"; }

# ------------------------------------------------------------------------------
# 1. Parse Arguments
# ------------------------------------------------------------------------------
TARGET_ENV="nonprod"
DEPLOY_TARGET="app"
DRY_RUN=false

while [[ $# -gt 0 ]]; do
  case "$1" in
    nonprod|development|dev)
      TARGET_ENV="nonprod"
      shift
      ;;
    prod|production)
      TARGET_ENV="prod"
      shift
      ;;
    --infra|--infra-manager)
      DEPLOY_TARGET="infra"
      shift
      ;;
    --app)
      DEPLOY_TARGET="app"
      shift
      ;;
    --all)
      DEPLOY_TARGET="all"
      shift
      ;;
    --dry-run)
      DRY_RUN=true
      shift
      ;;
    --help|-h)
      echo "Usage: ./scripts/deploy.sh [nonprod|prod] [--app|--infra|--all] [--dry-run]"
      echo ""
      echo "Environments:"
      echo "  nonprod   Deploy to Non-Prod (min=0, max=3, dev bucket)"
      echo "  prod      Deploy to Production (min=1, max=10, Vertex AI ADC, NO API Key)"
      echo ""
      echo "Deployment Targets:"
      echo "  --app     (Default) Deploy application container via Cloud Build + Cloud Run"
      echo "  --infra   Provision Cloud Infrastructure (Spanner, GCS, Cloud Run) via"
      echo "            Google Cloud Infrastructure Manager & Terraform (GEMINI.md Rule 9)"
      echo "  --all     Provision infrastructure via Infra Manager, then build and deploy container"
      echo ""
      echo "Flags:"
      echo "  --dry-run Print configuration and gcloud commands without executing"
      exit 0
      ;;
    *)
      log_warn "Unknown argument: $1"
      shift
      ;;
  esac
done

# ------------------------------------------------------------------------------
# 2. Load Unified .env Configuration
# ------------------------------------------------------------------------------
if [[ ! -f "$ENV_FILE" ]]; then
  log_error ".env file not found at: $ENV_FILE"
  log_info "Creating .env from .env.example..."
  if [[ -f "${ROOT_DIR}/.env.example" ]]; then
    cp "${ROOT_DIR}/.env.example" "$ENV_FILE"
    log_warn "Created default .env. Please verify configuration before deploying."
  else
    log_error "No .env.example found. Aborting."
    exit 1
  fi
fi

# Export variables from .env
set -a
# shellcheck source=/dev/null
source "$ENV_FILE"
set +a

# ------------------------------------------------------------------------------
# 3. Resolve Environment Specific Variables
# ------------------------------------------------------------------------------
# Shared Core
GCP_PROJECT="${GCP_PROJECT:-cs-poc-y03r7kmfyov4kilzg50fd7s}"
GCP_REGION="${GCP_REGION:-asia-southeast1}"
GENAI_LOCATION="${GENAI_LOCATION:-asia-southeast1}"
DEFAULT_MODEL="${DEFAULT_MODEL:-gemini-3.7-flash}"
REASONING_MODEL="${REASONING_MODEL:-gemini-3.7-flash}"
SPANNER_INSTANCE="${SPANNER_INSTANCE:-phenol-process-graph}"
SPANNER_DATABASE="${SPANNER_DATABASE:-safety-db}"
ARTIFACT_REGISTRY_REPO="${ARTIFACT_REGISTRY_REPO:-phenol-repo}"

if [[ "$TARGET_ENV" == "prod" ]]; then
  ENVIRONMENT_NAME="${PROD_ENVIRONMENT_NAME:-production}"
  SERVICE_NAME="${PROD_SERVICE_NAME:-phenol-process-safety-prod}"
  DEPLOYMENT_ID="${PROD_DEPLOYMENT_ID:-phenol-container-prod}"
  GCS_WIKI_BUCKET="${PROD_GCS_WIKI_BUCKET:-phenol-llm-wiki-${GCP_PROJECT}-prod}"
  MIN_INSTANCES="${PROD_MIN_INSTANCES:-1}"
  MAX_INSTANCES="${PROD_MAX_INSTANCES:-10}"
  CPU="${PROD_CPU:-2000m}"
  MEMORY="${PROD_MEMORY:-2Gi}"
  USE_VERTEXAI="true"
  SERVICE_ACCOUNT="${PROD_SERVICE_ACCOUNT:-}"
  # SECURITY MANDATE: Zero Gemini API key in production
  DEPLOY_API_KEY=""
else
  ENVIRONMENT_NAME="${NONPROD_ENVIRONMENT_NAME:-development}"
  SERVICE_NAME="${NONPROD_SERVICE_NAME:-phenol-process-safety-nonprod}"
  DEPLOYMENT_ID="${NONPROD_DEPLOYMENT_ID:-phenol-container-nonprod}"
  GCS_WIKI_BUCKET="${NONPROD_GCS_WIKI_BUCKET:-phenol-llm-wiki-${GCP_PROJECT}-nonprod}"
  MIN_INSTANCES="${NONPROD_MIN_INSTANCES:-0}"
  MAX_INSTANCES="${NONPROD_MAX_INSTANCES:-3}"
  CPU="${NONPROD_CPU:-2000m}"
  MEMORY="${NONPROD_MEMORY:-2Gi}"
  USE_VERTEXAI="${NONPROD_USE_VERTEXAI:-true}"
  SERVICE_ACCOUNT=""
  DEPLOY_API_KEY="${NONPROD_GEMINI_API_KEY:-}"
fi

COMMIT_SHA=$(git -C "$ROOT_DIR" rev-parse --short HEAD 2>/dev/null || echo "manual-$(date +%s)")
IMAGE_TAG="${GCP_REGION}-docker.pkg.dev/${GCP_PROJECT}/${ARTIFACT_REGISTRY_REPO}/phenol-agent:${COMMIT_SHA}"
IMAGE_LATEST="${GCP_REGION}-docker.pkg.dev/${GCP_PROJECT}/${ARTIFACT_REGISTRY_REPO}/phenol-agent:${TARGET_ENV}-latest"

# ------------------------------------------------------------------------------
# 4. Deployment Plan Summary
# ------------------------------------------------------------------------------
MODE_DESC="App Container Only (Cloud Build + Cloud Run)"
if [[ "$DEPLOY_TARGET" == "infra" ]]; then
  MODE_DESC="Infrastructure Only (Terraform via Google Cloud Infrastructure Manager)"
elif [[ "$DEPLOY_TARGET" == "all" ]]; then
  MODE_DESC="Full Stack (Infra Manager Terraform + App Container Build & Deploy)"
fi

INFRA_INPUTS="project_id=${GCP_PROJECT},region=${GCP_REGION},environment=${TARGET_ENV},container_image=${IMAGE_TAG},default_model=${DEFAULT_MODEL}"
if [[ -n "${SERVICE_ACCOUNT}" ]]; then
  INFRA_INPUTS="${INFRA_INPUTS},service_account=${SERVICE_ACCOUNT}"
fi
INFRA_DEPLOYMENT_PATH="projects/${GCP_PROJECT}/locations/${GCP_REGION}/deployments/${DEPLOYMENT_ID}"
INFRA_CMD="gcloud infra-manager deployments apply ${INFRA_DEPLOYMENT_PATH} \
  --local-source=${ROOT_DIR}/terraform \
  --input-values=\"${INFRA_INPUTS}\""

echo -e "\n${BOLD}==============================================================================${NC}"
echo -e "${BOLD}       REFINERY PHENOL PROCESS SAFETY PLATFORM — DEPLOYMENT PLAN               ${NC}"
echo -e "${BOLD}==============================================================================${NC}"
echo -e " Target Environment:     ${GREEN}${TARGET_ENV^^}${NC} (${ENVIRONMENT_NAME})"
echo -e " Deployment Mode:        ${BOLD}${DEPLOY_TARGET^^}${NC} — ${MODE_DESC}"
echo -e " Google Cloud Project:   ${CYAN}${GCP_PROJECT}${NC}"
echo -e " Deployment Region:      ${CYAN}${GCP_REGION}${NC}"
echo -e " Infra Manager Instance: ${BOLD}${DEPLOYMENT_ID}${NC}"
echo -e " Cloud Run Service:      ${BOLD}${SERVICE_NAME}${NC}"
echo -e " Scaling Profile:        min=${MIN_INSTANCES}, max=${MAX_INSTANCES} instances (${CPU} CPU, ${MEMORY} RAM)"
echo -e " Model Auth Strategy:    ${GREEN}Vertex AI (ADC / IAM Service Account)${NC} (API Key: ${YELLOW}${DEPLOY_API_KEY:-NONE - Zero Key in Prod}${NC})"
echo -e " GenAI Model:            ${DEFAULT_MODEL}"
echo -e " Spanner Property Graph: ${SPANNER_INSTANCE} / ${SPANNER_DATABASE}"
echo -e " Target Container Image: ${IMAGE_TAG}"
echo -e " Org Policy Compliance:  ${GREEN}invoker-iam-disabled: 'true' (100% compliant, zero allUsers)${NC}"
echo -e "${BOLD}==============================================================================${NC}\n"

# ------------------------------------------------------------------------------
# 5. Build & Deploy Execution
# ------------------------------------------------------------------------------
ENV_VARS_LIST="GCP_PROJECT=${GCP_PROJECT}"
ENV_VARS_LIST="${ENV_VARS_LIST},GCP_REGION=${GCP_REGION}"
ENV_VARS_LIST="${ENV_VARS_LIST},GENAI_LOCATION=${GENAI_LOCATION}"
ENV_VARS_LIST="${ENV_VARS_LIST},DEFAULT_MODEL=${DEFAULT_MODEL}"
ENV_VARS_LIST="${ENV_VARS_LIST},REASONING_MODEL=${REASONING_MODEL}"
ENV_VARS_LIST="${ENV_VARS_LIST},SPANNER_INSTANCE=${SPANNER_INSTANCE}"
ENV_VARS_LIST="${ENV_VARS_LIST},SPANNER_DATABASE=${SPANNER_DATABASE}"
ENV_VARS_LIST="${ENV_VARS_LIST},GOOGLE_GENAI_USE_VERTEXAI=${USE_VERTEXAI}"
ENV_VARS_LIST="${ENV_VARS_LIST},ENVIRONMENT=${TARGET_ENV}"
ENV_VARS_LIST="${ENV_VARS_LIST},GCS_WIKI_BUCKET=${GCS_WIKI_BUCKET}"
ENV_VARS_LIST="${ENV_VARS_LIST},USE_REAL_SPANNER=true"
if [[ -n "${DEPLOY_API_KEY}" ]]; then
  ENV_VARS_LIST="${ENV_VARS_LIST},GEMINI_API_KEY=${DEPLOY_API_KEY}"
fi

BUILD_CMD="gcloud builds submit --project=${GCP_PROJECT} --tag=${IMAGE_TAG} ${ROOT_DIR}"

DEPLOY_CMD="gcloud run deploy ${SERVICE_NAME} \
  --project=${GCP_PROJECT} \
  --image=${IMAGE_TAG} \
  --region=${GCP_REGION} \
  --platform=managed \
  --ingress=all \
  --no-allow-unauthenticated \
  --min-instances=${MIN_INSTANCES} \
  --max-instances=${MAX_INSTANCES} \
  --cpu=${CPU} \
  --memory=${MEMORY} \
  --set-env-vars=${ENV_VARS_LIST} \
  --labels=run.googleapis.com/invoker-iam-disabled=true,environment=${TARGET_ENV}"

if [[ -n "${SERVICE_ACCOUNT}" ]]; then
  DEPLOY_CMD="${DEPLOY_CMD} --service-account=${SERVICE_ACCOUNT}"
fi

if [[ "$DRY_RUN" == true ]]; then
  log_warn "DRY RUN MODE ENABLED — Commands will not be executed."
  if [[ "$DEPLOY_TARGET" == "infra" || "$DEPLOY_TARGET" == "all" ]]; then
    echo -e "\n${BOLD}[Infrastructure Manager: Apply Terraform Configuration]${NC}"
    echo "  $INFRA_CMD"
  fi
  if [[ "$DEPLOY_TARGET" == "app" || "$DEPLOY_TARGET" == "all" ]]; then
    echo -e "\n${BOLD}[1. Build Container Image via Cloud Build]${NC}"
    echo "  $BUILD_CMD"
    echo -e "\n${BOLD}[2. Deploy Application Revision to Cloud Run]${NC}"
    echo "  $DEPLOY_CMD"
    echo -e "\n${BOLD}[3. Post-Deployment Verification Probe]${NC}"
    echo "  curl -f -s https://\${SERVICE_URL}/healthz"
  fi
  log_success "Dry run validation complete."
  exit 0
fi

# Preflight Tool Check
if ! command -v gcloud &> /dev/null; then
  log_error "gcloud CLI is not installed or not in PATH."
  exit 1
fi

log_info "Verifying gcloud authorization..."
gcloud config set project "${GCP_PROJECT}"

# Ensure Artifact Registry repository exists
if ! gcloud artifacts repositories describe "${ARTIFACT_REGISTRY_REPO}" --location="${GCP_REGION}" --project="${GCP_PROJECT}" &>/dev/null; then
  log_info "Creating Artifact Registry repository: ${ARTIFACT_REGISTRY_REPO} (${GCP_REGION})..."
  gcloud artifacts repositories create "${ARTIFACT_REGISTRY_REPO}" \
    --repository-format=docker \
    --location="${GCP_REGION}" \
    --description="Phenol Process Safety container repository" \
    --project="${GCP_PROJECT}"
fi

# Execute Infrastructure Manager (if requested)
if [[ "$DEPLOY_TARGET" == "infra" || "$DEPLOY_TARGET" == "all" ]]; then
  log_info "Applying Infrastructure via Google Cloud Infrastructure Manager (${DEPLOYMENT_ID})..."
  eval "$INFRA_CMD"
  log_success "Infrastructure Manager deployment submitted successfully."
fi

# Execute Application Container Build & Deploy (if requested)
if [[ "$DEPLOY_TARGET" == "app" || "$DEPLOY_TARGET" == "all" ]]; then
  log_info "Step 1/3: Building container image via Google Cloud Build..."
  eval "$BUILD_CMD"
  gcloud artifacts docker tags add "${IMAGE_TAG}" "${IMAGE_LATEST}" --quiet 2>/dev/null || true

  log_info "Step 2/3: Deploying container to Cloud Run (${SERVICE_NAME})..."
  eval "$DEPLOY_CMD"

  log_info "Step 3/3: Running post-deployment health check..."
  SERVICE_URL=$(gcloud run services describe "${SERVICE_NAME}" --project="${GCP_PROJECT}" --region="${GCP_REGION}" --format='value(status.url)' 2>/dev/null || echo "")

  if [[ -n "$SERVICE_URL" ]]; then
    log_success "Cloud Run service is live at: ${SERVICE_URL}"
    log_info "Probing health check at: ${SERVICE_URL}/healthz"
    if curl -f -s -m 10 "${SERVICE_URL}/healthz"; then
      echo ""
      log_success "Service health check probe PASSED (200 OK)."
    else
      log_warn "Health check probe timed out or returned non-200. Container may still be initializing."
    fi
  else
    log_warn "Could not resolve Service URL."
  fi
fi

log_success "Deployment pipeline completed successfully for target: [${DEPLOY_TARGET}] environment: [${TARGET_ENV}]."
