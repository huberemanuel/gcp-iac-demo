run_terraform:
	cd terraform && \
	terraform init && \
	terraform fmt -check && \
	terraform plan && \
	terraform apply

install:
	pip install -e .