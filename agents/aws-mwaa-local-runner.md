---
name: "Aws-Mwaa-Local-Runner"
slug: "aws-mwaa-local-runner"
layout: "agent.njk"
category: "other"
maker: "aws"
license: "MIT-0"
url: "https://github.com/aws/aws-mwaa-local-runner"
source_code_url: "https://github.com/aws/aws-mwaa-local-runner"
source_available: "True"
platforms:
  - "CLI"
  - "IDE"
first_released: "2021-04-27"
current_release: "2025-10-03"
stars: "809"
language: "Shell, Python, Docker"
homepage: "https://github.com/aws/aws-mwaa-local-runner"
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
maintained: "dormant"
sources:
  - "jim"
what_makes_it_special: "Not an agent harness — a CLI utility that replicates an Amazon Managed Workflows for Apache Airflow (MWAA) environment locally via Docker, enabling local development/testing of DAGs, custom plugins, and dependencies before deploying to MWAA. Transitioning to legacy (production Docker image moved to amazon-mwaa-docker-images for Airflow 3.x)."
---

This AWS repository has nothing to do with coding agents: it is a CLI utility that builds a Docker container replicating an Amazon MWAA (Managed Workflows for Apache Airflow) environment locally, so developers can test DAGs, custom plugins, and requirements.txt packages before deploying to the managed service. Commands cover building the image, starting the local environment, and testing requirements/startup scripts against the MWAA production configuration. The repository was archived by AWS in August 2026, read-only, with users directed to the amazon-mwaa-docker-images repository, which open-sources MWAA's actual production images and supports Airflow 2.9+ and future 3.x releases. It appears in this census only because keyword-driven gap sweeps can misclassify infrastructure tooling; the correct category is 'other'.
