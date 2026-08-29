---
name: "perles"
slug: "perles"
layout: "agent.njk"
category: "other"
maker: "zjrosen"
license: "MIT"
url: "https://github.com/zjrosen/perles"
source_code_url: "https://github.com/zjrosen/perles"
source_available: "True"
platforms:
  - "CLI"
first_released: "2025-12-01"
current_release: "2026-08-18"
stars: "175"
language: "Go"
homepage: "https://zjrosen.github.io/perles"
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "False"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: null
pricing: "Free / open source (MIT)"
install_method: "curl -sSL https://raw.githubusercontent.com/zjrosen/perles/main/install.sh | bash; or brew tap zjrosen/perles && brew install perles"
docs_url: "https://github.com/zjrosen/perles#readme"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/zjrosen/perles"
maintained: "active"
sources:
  - "agent_infra"
what_makes_it_special: "Terminal UI for Beads issue tracking with custom BQL (Beads Query Language) supporting boolean logic, date filtering, dependency tree traversal, and customizable kanban board views. Also described as a multi-agent orchestration control plane workflow runner, though specific agent orchestration features are not detailed in the README."
---

perles exists for developers who manage their work in Beads, Steve Yegge's local-first issue tracker, and want a richer interface than its CLI offers. The Go-based terminal UI renders issues as customizable kanban boards and supports searching through BQL, a query language with boolean logic, date filtering, and traversal of dependency trees between issues. It runs inside any project containing a .beads directory and requires a beads database of version 0.62 or newer, upgrading via a migration command where needed. The repository's description also references a multi-agent orchestration control plane aspect, with an ORCHESTRATION.md exploring workflow-runner ideas, but the shipped product is the issue TUI. Its users are Beads adopters — often developers running AI coding agents that file and consume Beads issues as their task queue.
