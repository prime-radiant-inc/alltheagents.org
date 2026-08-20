---
name: "forgeo"
slug: "forgeo"
layout: "agent.njk"
category: "multiplexer"
maker: "lucaGazzola"
license: "MIT"
url: "https://github.com/lucaGazzola/forgeo"
source_code_url: "https://github.com/lucaGazzola/forgeo"
source_available: True
platforms: []
first_released: "2026-07-31"
current_release: "2026-08-19"
stars: "36"
language: "Python 3.11+"
homepage: "https://forgeo.org"
mcp_support: null
plugin_support: False
claude_code_plugin: False
subagents: False
hooks: null
plan_mode: null
model_providers: "Agent-agnostic - works with any coding agent CLI (Claude Code, Codex, opencode named)"
pricing: "Free / open-source (MIT)"
install_method: "brew install lucaGazzola/forgeo/forgeo (macOS/Linux); or curl -fsSL https://forgeo.org/install.sh | bash (Linux/macOS/Windows); or pipx install forgeo-cli"
docs_url: "https://forgeo.org"
plugin_docs_url: null
config_docs_url: "docs/configuration.md (in-repo)"
download_url: "https://github.com/lucaGazzola/forgeo"
maintained: "active"
sources:
  - "github_topic"
what_makes_it_special: "Scheduled, agent-driven software factory layer on top of any coding-agent CLI; maintain a plain-JSON backlog and the daemon autonomously picks tasks, runs the agent, commits directly to main (no branches, no PRs), retries transient failures, and runs a refactoring pass when idle; only escalates to a human for genuine decisions; everything stored in inspectable plain files with automatic backup/restore; supports multiple independent repository instances with a central web dashboard; backlog can optionally live behind an HTTP endpoint with OAuth2 auth."
---

Scheduled, agent-driven software factory layer on top of any coding-agent CLI; maintain a plain-JSON backlog and the daemon autonomously picks tasks, runs the agent, commits directly to main (no branches, no PRs), retries transient failures, and runs a refactoring pass when idle; only escalates to a human for genuine decisions; everything stored in inspectable plain files with automatic backup/restore; supports multiple independent repository instances with a central web dashboard; backlog can optionally live behind an HTTP endpoint with OAuth2 auth.
