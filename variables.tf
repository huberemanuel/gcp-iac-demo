variable "bucket_name" {
  type        = string
  description = "Name of the bucket"
}

variable "region" {
  type    = string
  default = "us"
}

variable "project_id" {
  type    = string
  default = "data-lake-test-gcp-iac"
}
