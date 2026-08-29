---
name: "Relay"
slug: "relay"
layout: "agent.njk"
category: "multiplexer"
maker: "jcast90"
license: "MIT"
url: "https://github.com/jcast90/relay"
source_code_url: "https://github.com/jcast90/relay"
source_available: "True"
platforms:
  - "CLI"
  - "IDE"
first_released: "2026-03-30"
current_release: "2026-07-11"
stars: "5"
language: "TypeScript"
homepage: "https://github.com/jcast90/relay#readme"
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: "False"
subagents: "True"
hooks: "True"
plan_mode: "True"
model_providers: "Claude, Codex, any OpenAI- or Anthropic-compatible HTTP API (MiniMax, OpenRouter, DeepSeek, Groq, Together, LiteLLM, vLLM)"
pricing: "Free / open-source (MIT)"
install_method: "npm install -g @jcast90/relay && rly welcome; or from source: git clone https://github.com/jcast90/relay && cd relay && ./install.sh; GUI app downloadable from GitHub releases (.dmg/.AppImage/.deb/.msi)"
docs_url: "https://github.com/jcast90/relay/blob/main/docs/getting-started.md"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/jcast90/relay/releases/latest"
maintained: "active"
sources:
  - "brad"
what_makes_it_special: "Cross-repo agent-to-agent delegation via a single orchestrator that reaches into multiple repos and coordinates a delegation tree — unlike single-repo agent harnesses. Local-first, all state in ~/.relay/, no cloud/telemetry. Three dashboards (CLI, TUI, GUI) sharing one source of truth. MCP server exposes 19 tools. Classifier → planner → decomposer pipeline with user approval for complex tiers."
---

Relay addresses the problem that coding agents operate inside one checkout at a time, while real work spans several repositories — a schema change in one repo breaks consumers in three others. A user hands the orchestrator a sentence, GitHub issue, or Linear ticket; it classifies complexity, produces a plan, decomposes it into a dependency DAG of tickets, and dispatches agents that verify their work and open PRs. State lives entirely in ~/.relay as atomic file writes, so there is no server and no telemetry, and sessions approaching context limits emit handoff briefs for their successors. It suits maintainers who already live in Claude Code or Codex CLI and want delegation across repos without adopting a hosted coordination service.
