import os

from gcp_iac.environment import Environment

active_env = Environment[os.getenv("ENVIRONMENT").upper()]