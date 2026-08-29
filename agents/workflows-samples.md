---
name: "Workflows-Samples"
slug: "workflows-samples"
layout: "agent.njk"
category: "other"
maker: "GoogleCloudPlatform"
license: "Apache-2.0"
url: "https://github.com/GoogleCloudPlatform/workflows-samples"
source_code_url: "https://github.com/GoogleCloudPlatform/workflows-samples"
source_available: "True"
platforms:
  - "Web"
first_released: "2020-11-11"
current_release: "2026-05-05"
stars: "88"
language: "YAML/JSON"
homepage: "https://cloud.google.com/workflows"
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "None — workflow sample definitions, no AI models"
pricing: null
install_method: "gcloud workflows deploy $WORKFLOW --source src/$WORKFLOW.workflows.yaml, gcloud workflows run $WORKFLOW"
docs_url: "https://cloud.google.com/workflows/docs"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "jim"
what_makes_it_special: "Official Google Cloud Platform samples repository for Google Cloud Workflows; contains workflow definitions as *.workflows.yaml/json files with JSON generated from YAML equivalents; JSON schema syntax autocompletion support; quick deploy-and-run workflow via gcloud CLI. Not a coding agent harness."
---

This repository collects official sample workflow definitions (*.workflows.yaml and generated JSON) for Google Cloud Workflows, Google Cloud's serverless orchestration service. The samples demonstrate YAML/JSON workflow syntax, JSON-schema-based autocompletion support, and quick deploy-and-run through the gcloud CLI. It contains no AI or agent components; it is documentation material for a cloud orchestration service and is included in the census only as a boundary case. GCP developers use it to learn Workflows syntax by example.
