---
name: "nasiko"
slug: "nasiko"
layout: "agent.njk"
category: "other"
maker: "Nasiko-Labs"
license: "Apache-2.0"
url: "https://github.com/Nasiko-Labs/nasiko"
source_code_url: "https://github.com/Nasiko-Labs/nasiko"
source_available: "True"
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

Nasiko targets teams operating fleets of A2A-protocol agents who need a single enforcement point for identity, cost, and security. Agents register through a CLI and are never publicly reachable; every hop passes through the control plane, which applies allowlists, rate limits, and OpenTelemetry tracing while collecting per-call token costs. An LLM router resolves provider, model, and key server-side so agents hold only short-lived identity tokens, and the MCP gateway merges Composio toolkits and custom servers into one credential-free URL. It hardcodes A2A spec v1.0, so language choice is unconstrained — Python, Rust, Go, and TypeScript agents all work. Deployment is Docker Compose with standard Postgres, Redis, and S3 backends.
