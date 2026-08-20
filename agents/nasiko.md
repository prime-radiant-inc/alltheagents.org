---
name: "nasiko"
slug: "nasiko"
layout: "agent.njk"
category: "agent"
maker: "Nasiko-Labs"
license: "Apache-2.0"
url: "https://github.com/Nasiko-Labs/nasiko"
source_code_url: "https://github.com/Nasiko-Labs/nasiko"
source_available: True
platforms: []
first_released: "2026-02-12"
current_release: "2026-08-19"
stars: "4959"
language: "Rust"
homepage: "https://www.nasiko.com"
mcp_support: "yes"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "yes"
hooks: "no"
plan_mode: "no"
model_providers: "OpenAI-compatible (LLM Router proxy)"
pricing: "open-source"
install_method: "docker"
docs_url: "https://docs.nasiko.com"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "agent_infra"
what_makes_it_special: "Single-process developer control plane for any A2A-protocol-speaking agent. Terminates TLS, authenticates, proxies all agent-to-agent traffic (agents never publicly exposed). Built-in MCP Gateway, LLM Router (OpenAI-compatible egress with short-lived tokens), embedded OCI registry, encrypted secrets, 3-stage intelligent routing (embedding → rerank → LLM pick), full OpenTelemetry observability with token cost collection."
---

Single-process developer control plane for any A2A-protocol-speaking agent. Terminates TLS, authenticates, proxies all agent-to-agent traffic (agents never publicly exposed). Built-in MCP Gateway, LLM Router (OpenAI-compatible egress with short-lived tokens), embedded OCI registry, encrypted secrets, 3-stage intelligent routing (embedding → rerank → LLM pick), full OpenTelemetry observability with token cost collection.
