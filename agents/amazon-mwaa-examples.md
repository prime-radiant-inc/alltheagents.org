---
name: "Amazon-Mwaa-Examples"
slug: "amazon-mwaa-examples"
layout: "agent.njk"
category: "other"
maker: "aws-samples"
license: "MIT-0"
url: "https://github.com/aws-samples/amazon-mwaa-examples"
source_code_url: "https://github.com/aws-samples/amazon-mwaa-examples"
source_available: "True"
platforms:
  - "Web"
first_released: "2021-03-01"
current_release: "2026-05-28"
stars: "119"
language: "Python"
homepage: null
mcp_support: "False"
plugin_support: "True"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: null
pricing: "Free (open-source example code)"
install_method: "Clone repository; requires a working Amazon MWAA environment; follow per-folder README.md"
docs_url: "https://docs.aws.amazon.com/mwaa/latest/userguide/"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/aws-samples/amazon-mwaa-examples"
maintained: "active"
sources:
  - "jim"
what_makes_it_special: "Provides complete, end-to-end sample use cases (DAGs, requirements.txt, plugins, CloudFormation templates) specifically tested for Amazon MWAA, bridging open-source Apache Airflow and managed AWS service integrations."
---

The repository bridges the gap between open-source Apache Airflow documentation and the managed Amazon MWAA service by providing complete, tested examples: DAGs for Secrets Manager migration, EMR jobs, and RBAC patterns; end-to-end usecases with CloudFormation (image processing pipelines, CodeArtifact-based dependency serving, environment start/stop); provider package requirements; and infrastructure templates. Most examples also run on self-managed Airflow since MWAA runs stock Airflow. AWS maintains it as an active samples repo (226 commits, community PRs accepted) under MIT-0, with the standard disclaimer that samples are educational and untested for production. Its census relevance is nominal — it is workflow automation infrastructure, not an AI agent.
