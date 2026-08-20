---
name: "Relay"
slug: "relay"
layout: "agent.njk"
category: "multiplexer"
maker: "jcast90"
license: "MIT"
url: "https://github.com/jcast90/relay"
source_code_url: "https://github.com/jcast90/relay"
source_available: True
platforms:
  - "CLI"
  - "IDE"
first_released: "2026-03-30"
current_release: "2026-07-11"
stars: "5"
language: "TypeScript"
homepage: "https://github.com/jcast90/relay#readme"
mcp_support: True
plugin_support: True
claude_code_plugin: False
subagents: True
hooks: True
plan_mode: True
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

Cross-repo agent-to-agent delegation via a single orchestrator that reaches into multiple repos and coordinates a delegation tree — unlike single-repo agent harnesses. Local-first, all state in ~/.relay/, no cloud/telemetry. Three dashboards (CLI, TUI, GUI) sharing one source of truth. MCP server exposes 19 tools. Classifier → planner → decomposer pipeline with user approval for complex tiers.
