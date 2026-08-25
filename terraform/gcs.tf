resource "google_storage_bucket" "raw_docs_bucket" {
  name          = "phenol-raw-docs-${var.project_id}-${var.environment}"
  location      = var.region
  force_destroy = false
  uniform_bucket_level_access = true

  versioning {
    enabled = true
  }
}

resource "google_storage_bucket" "wiki_bucket" {
  name          = "phenol-llm-wiki-${var.project_id}-${var.environment}"
  location      = var.region
  force_destroy = false
  uniform_bucket_level_access = true

  versioning {
    enabled = true
  }
}
