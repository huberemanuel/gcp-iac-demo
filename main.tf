provider "google" {
  credentials = file("~/Downloads/data-lake-test-gcp-iac-02e7dd9405c4.json")
  project     = var.project_id
  region      = "us"
}
resource "google_storage_bucket" "default" {
  name = var.bucket_name
  project = var.project_id
  #storage_class = var.storage_class
