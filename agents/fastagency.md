---
name: "FastAgency"
slug: "fastagency"
layout: "agent.njk"
category: "other"
maker: "ag2ai"
license: "Apache-2.0"
url: "https://github.com/airtai/fastagency"
source_code_url: "https://github.com/airtai/fastagency"
source_available: "True"
platforms: []
first_released: "2024-07-17"
current_release: "2026-02-23"
stars: "547"
language: "Python"
homepage: "https://fastagency.ai/latest"
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: null
hooks: "no"
plan_mode: "no"
model_providers: "OpenAI, AG2"
pricing: "open-source"
install_method: "pip"
docs_url: "https://fastagency.ai/latest"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "caramaschi"
what_makes_it_special: "Unified programming interface for deploying AG2 (AutoGen) multi-agent workflows to production; seamless OpenAPI integration with few lines of code; Tester class for CI; CLI for orchestration; multiple UI options (Console, Mesop web) and network adapters (FastAPI REST, NATS via FastStream)"
---

FastAgency was built because multi-agent workflows that work in a notebook rarely survive contact with production: it provides one programming interface over AG2 workflows with pluggable UIs (console, Mesop web chat) and serving options (REST API, NATS-based distributed deployment). OpenAPI integration lets agents call existing REST services with minimal glue code, a Tester class runs workflows inside CI, and Cookiecutter scaffolding generates a complete project with devcontainer and deployment scripts for Docker and Fly.io behind GitHub Actions. Maintained by the ag2ai organization alongside AG2 itself, it targets Python teams moving multi-agent systems from prototypes to operated services rather than individual developers picking a coding assistant.
