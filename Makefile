run_terraform:
	cd terraform && \
	terraform init && \
	terraform fmt -check && \
	terraform plan && \
	terraform apply

install:
	pip install -e .

ingest_data:
	python -m gcp_iac.apps.ingestion