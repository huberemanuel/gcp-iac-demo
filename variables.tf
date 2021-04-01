variable "bucket_name" {
  type = string
  description = "Name of the bucket"
}

variable "project_id" {
  type = string
  default = "data-lake-test-gcp-iac" 
}

variable "storage_class" {
  type = string
}