---
name: "Aws-Mwaa-Local-Runner"
slug: "aws-mwaa-local-runner"
layout: "agent.njk"
category: "agent"
maker: "aws"
license: "MIT-0"
url: "https://github.com/aws/aws-mwaa-local-runner"
source_code_url: "https://github.com/aws/aws-mwaa-local-runner"
source_available: True
platforms:
  - "CLI"
  - "IDE"
first_released: "2021-04-27"
current_release: "2025-10-03"
stars: "809"
language: "Shell, Python, Docker"
homepage: null
mcp_support: "no"
plugin_support: "yes (Airflow plugins directory)"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: null
pricing: "open-source"
install_method: "git clone, docker"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "abandoned"
sources:
  - "jim"
what_makes_it_special: "Not an agent harness — a CLI utility that replicates an Amazon Managed Workflows for Apache Airflow (MWAA) environment locally via Docker, enabling local development/testing of DAGs, custom plugins, and dependencies before deploying to MWAA. Transitioning to legacy (production Docker image moved to amazon-mwaa-docker-images for Airflow 3.x)."
---

Not an agent harness — a CLI utility that replicates an Amazon Managed Workflows for Apache Airflow (MWAA) environment locally via Docker, enabling local development/testing of DAGs, custom plugins, and dependencies before deploying to MWAA. Transitioning to legacy (production Docker image moved to amazon-mwaa-docker-images for Airflow 3.x).
