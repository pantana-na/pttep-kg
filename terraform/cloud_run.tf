resource "google_cloud_run_v2_service" "phenol_agent_service" {
  name     = "phenol-process-safety-${var.environment}"
  location = var.region
  ingress  = "INGRESS_TRAFFIC_ALL"

  template {
    scaling {
      min_instance_count = var.environment == "prod" ? 1 : 0
      max_instance_count = var.environment == "prod" ? 10 : 3
    }

    containers {
      image = var.container_image

      resources {
        limits = {
          cpu    = "2000m"
          memory = "2Gi"
        }
      }

      env {
        name  = "GCP_PROJECT"
        value = var.project_id
      }
      env {
        name  = "GCP_REGION"
        value = var.region
      }
      env {
        name  = "SPANNER_INSTANCE"
        value = "phenol-process-graph"
      }
      env {
        name  = "SPANNER_DATABASE"
        value = "safety-db"
      }

      liveness_probe {
        http_get {
          path = "/healthz"
          port = 8080
        }
        initial_delay_seconds = 10
        period_seconds        = 30
        failure_threshold     = 3
      }
    }
  }

  labels = {
    "run.googleapis.com/invoker-iam-disabled" = "true"
    "environment"                            = var.environment
  }
}
