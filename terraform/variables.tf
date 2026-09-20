variable "project_id" {
  description = "The GCP project ID"
  type        = string
  default     = "cs-poc-y03r7kmfyov4kilzg50fd7s"
}

variable "region" {
  description = "The GCP region for deployment"
  type        = string
  default     = "asia-southeast1"
}

variable "environment" {
  description = "Environment name (nonprod or prod)"
  type        = string
  default     = "nonprod"
}

variable "container_image" {
  description = "Container image URI in Artifact Registry"
  type        = string
  default     = "asia-southeast1-docker.pkg.dev/cs-poc-y03r7kmfyov4kilzg50fd7s/phenol-repo/phenol-agent:latest"
}

variable "default_model" {
  description = "Default Gemini model for agents"
  type        = string
  default     = "gemini-3.8-flash"
}

variable "service_account" {
  description = "Dedicated Service Account email for Cloud Run execution"
  type        = string
  default     = ""
}

