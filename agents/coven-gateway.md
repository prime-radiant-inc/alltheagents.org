---
name: "Coven Gateway"
slug: "coven-gateway"
layout: "agent.njk"
category: "other"
maker: "2389-research"
license: "MIT"
url: "https://github.com/2389-research/coven-gateway"
source_code_url: "https://github.com/2389-research/coven-gateway"
source_available: "True"
platforms:
  - "CLI"
  - "Web"
first_released: null
current_release: null
stars: "2"
language: "Go"
homepage: null
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: null
pricing: "free"
install_method: "go install"
docs_url: null
maintained: "active"
sources:
  - "user_reported"
what_makes_it_special: "gRPC control plane for Coven agents that routes messages from frontends (TUI, web, Matrix bridge) to connected agents with sticky channel bindings, streams responses back via HTTP/SSE, persists threads and messages in SQLite, and includes an admin CLI (coven-admin), JWT auth, health checks, and Tailscale/tsnet integration."
---

Coven Gateway is the gRPC control plane and message router for the Coven agent platform — infrastructure rather than an agent. Frontends (a TUI, a web client, a Matrix bridge) send messages in, and the gateway routes them to connected agents with sticky channel bindings so a conversation stays pinned to the right agent, then streams responses back over HTTP/SSE. Threads and messages persist in SQLite, and an admin CLI (coven-admin) handles operations alongside JWT auth, health checks, and Tailscale/tsnet integration for private networking. The agent loop lives in the Coven agents; the gateway only routes, stores, and authenticates. The audience is operators running a Coven deployment who need the routing and persistence layer as its own service.
