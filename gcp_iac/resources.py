from gcp_iac import active_env

active_env_str = active_env.value
gcp_iac_project_id = "data-lake-test-gcp-iac"
gcp_iac_bucket_name = f"gcp_iac_bucket_{active_env_str}"