---
name: "Coven"
slug: "coven"
layout: "agent.njk"
category: "multiplexer"
maker: "2389-research"
license: "MIT"
url: "https://github.com/2389-research/coven"
source_code_url: "https://github.com/2389-research/coven"
source_available: "True"
platforms:
  - "CLI"
  - "Web"
first_released: null
current_release: null
stars: "4"
language: "Rust"
homepage: null
mcp_support: "yes (mcp-bridge-pack)"
plugin_support: "yes (tool packs via Pack SDK)"
claude_code_plugin: "no"
subagents: "yes (coven-swarm supervises agents across workspaces)"
hooks: "no"
plan_mode: "no"
model_providers: "Anthropic (Claude)"
pricing: "free"
install_method: "cargo build"
docs_url: null
maintained: "active"
sources:
  - "user_reported"
what_makes_it_special: "Rust platform for orchestrating AI agents with tool capabilities and gRPC streaming. coven-agent runs a single-workspace agent, coven-swarm supervises agents across multiple workspaces, and the Go gateway handles routing, SQLite thread/message storage, and tool pack registry. Supports TUI, HTTP API, Matrix bridge, and CLI frontends with modular tool packs."
---

Coven is a Rust platform for orchestrating AI agents that need tool capabilities and gRPC streaming. The architecture splits cleanly: coven-agent runs a single-workspace agent, coven-swarm supervises agents across multiple workspaces, and a separate Go gateway (coven-gateway) handles routing, persists threads and messages in SQLite, and serves as the tool pack registry. Tool packs built via the Pack SDK extend agent capabilities, and an mcp-bridge-pack bridges MCP tools into the same surface. Frontends are pluggable — a TUI, an HTTP API, a Matrix bridge, and a CLI all talk to the gateway — so the same agents can be driven from a terminal or a chat room. The audience is developers coordinating multiple Claude-backed agents across workspaces who want the orchestration layer in Rust.
