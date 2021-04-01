variable "bucket_name_pattern" {
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

variable "ENVIRONMENT" {
  type = string
}