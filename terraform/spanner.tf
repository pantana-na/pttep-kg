resource "google_spanner_instance" "phenol_graph_instance" {
  name         = "phenol-process-graph"
  config       = "regional-${var.region}"
  display_name = "Phenol Process Safety Property Graph"
  num_nodes    = 1

  labels = {
    "environment" = var.environment
  }
}

resource "google_spanner_database" "phenol_safety_db" {
  instance                 = google_spanner_instance.phenol_graph_instance.name
  name                     = "safety-db"
  version_retention_period = "3d"
}
