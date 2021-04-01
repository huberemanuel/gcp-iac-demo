provider "google" {
  project = var.project_id
  region  = var.region
}
resource "google_storage_bucket" "default" {
  name    = format("%s_%s", var.bucket_name_pattern, var.ENVIRONMENT)
  project = var.project_id
}