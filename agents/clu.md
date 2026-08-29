---
name: "clu"
slug: "clu"
layout: "agent.njk"
category: "other"
maker: "Arjia-Labs"
license: "MIT"
url: "https://github.com/arjia-labs/clu"
source_code_url: "https://github.com/arjia-labs/clu"
source_available: "True"
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
model_providers: "Agent-agnostic (any CLI agent can claim and work issues)"
pricing: "free"
install_method: "go install github.com/arjia-labs/clu/cmd/clu@latest (or make install from clone)"
docs_url: "https://arjia-labs.github.io/clu/"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/arjia-labs/clu/releases"
maintained: "active"
sources:
  - "brad"
what_makes_it_special: "SQLite-backed issue tracker for coordinating AI coding agents on a single machine. Atomic claims (racing agents get different issues), dependency graphs with cascading cancel, bulk graph instantiation via clu batch, context inheritance for agents, workflow templates with human-approval gates, and an in-process local Web UI. No daemon, no server, no network. Includes an integration pattern using Claude Code's Monitor tool (clu ready --watch)."
---

clu fills the gap between having several agent processes and having anywhere durable for them to pick up work: issues live in one SQLite file with no daemon or network, claims are atomic SQL updates so two agents never take the same task, and cancel cascades walk the dependency graph so downstream work never runs on cancelled premises. Workflow templates encode human-approval checkpoints for risky steps, a mailbox lets agents communicate, and a local web dashboard exposes kanban, graph, and approval views. It deliberately excludes an agent runtime, positioning itself as the coordination substrate beneath any harness, and its design favors single-machine, local-first setups over distributed orchestration.
