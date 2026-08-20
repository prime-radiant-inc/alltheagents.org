---
name: "clu"
slug: "clu"
layout: "agent.njk"
category: "agent"
maker: "Arjia-Labs"
license: "MIT"
url: "https://github.com/arjia-labs/clu"
source_code_url: "https://github.com/arjia-labs/clu"
source_available: True
platforms:
  - "CLI"
  - "Autonomous"
first_released: "2026-05-26"
current_release: "2026-07-17"
stars: "8"
language: "Go"
homepage: "https://arjia-labs.github.io/clu/"
mcp_support: null
plugin_support: null
claude_code_plugin: null
subagents: null
hooks: null
plan_mode: null
model_providers: null
pricing: null
install_method: "go install github.com/arjia-labs/clu/cmd/clu@latest (or make install from clone)"
docs_url: "https://arjia-labs.github.io/clu/"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "brad"
what_makes_it_special: "SQLite-backed issue tracker for coordinating AI coding agents on a single machine. Atomic claims (racing agents get different issues), dependency graphs with cascading cancel, bulk graph instantiation via clu batch, context inheritance for agents, workflow templates with human-approval gates, and an in-process local Web UI. No daemon, no server, no network. Includes an integration pattern using Claude Code's Monitor tool (clu ready --watch)."
---

SQLite-backed issue tracker for coordinating AI coding agents on a single machine. Atomic claims (racing agents get different issues), dependency graphs with cascading cancel, bulk graph instantiation via clu batch, context inheritance for agents, workflow templates with human-approval gates, and an in-process local Web UI. No daemon, no server, no network. Includes an integration pattern using Claude Code's Monitor tool (clu ready --watch).
