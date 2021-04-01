from setuptools import setup, find_packages

setup(
    name = "gcp_iac",
    version = "0.0.1",
    author = "Emanuel Huber",
    author_email = "emanuel.tesv@gmail.com",
    description = "IaC on Google Cloud test",
    packages = find_packages(),
    install_requires = [
        "gcloud==0.18.3",
        "google-cloud-storage==1.37.0",
        "tqdm==4.59.0",
        "tensorflow==2.4.1",
        "Pillow==8.2.0"
    ]
)