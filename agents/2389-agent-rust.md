---
name: "2389 Agent Protocol (Rust)"
slug: "2389-agent-rust"
layout: "agent.njk"
category: "agent-sdk"
maker: "2389-research"
license: "MIT"
url: "https://github.com/2389-research/2389-agent-rust"
source_code_url: "https://github.com/2389-research/2389-agent-rust"
source_available: "True"
platforms: []
first_released: null
current_release: null
stars: "2"
language: "Rust"
homepage: null
mcp_support: "no"
plugin_support: "yes (extensible JSON-schema-validated tool system)"
claude_code_plugin: "no"
subagents: "yes (agent discovery/capability matching)"
hooks: "no"
plan_mode: "no"
model_providers: "OpenAI, Anthropic"
pricing: "free"
install_method: "cargo install"
docs_url: null
maintained: "active"
sources:
  - "user_reported"
what_makes_it_special: "Production-ready Rust implementation of the 2389 Agent Protocol — a standard for interoperable AI agents communicating via MQTT in distributed systems. Provides an agent runtime (deployable agent binaries), a Rust library (agent2389 on crates.io), multi-LLM support, extensible JSON-schema-validated tool system, MQTT transport with QoS 1, agent discovery/capability matching, and observability (health endpoints, metrics)."
---

This is the production-ready Rust implementation of the 2389 Agent Protocol, a standard for interoperable AI agents that communicate over MQTT in distributed systems. It ships an agent runtime as deployable binaries and a Rust library (agent2389 on crates.io) for embedding the protocol elsewhere. Agents advertise capabilities through discovery and capability matching, transport runs over MQTT with QoS 1, and tools are extensible and JSON-schema-validated so an agent's tool surface is describable and checkable. Multi-LLM support spans OpenAI and Anthropic, and observability comes via health endpoints and metrics. It is a framework for building interoperable agents, not a coding agent itself. The audience is developers wiring agents together across processes and machines who need a real protocol rather than ad-hoc HTTP.
