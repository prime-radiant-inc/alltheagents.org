---
name: "fable5-opus5-orchestrator"
slug: "fable5-opus5-orchestrator"
layout: "agent.njk"
category: "agent"
maker: "Rylaa"
license: "MIT"
url: "https://github.com/Rylaa/fable5-opus5-orchestrator"
source_code_url: "https://github.com/Rylaa/fable5-opus5-orchestrator"
source_available: True
platforms: []
first_released: "2026-06-12"
current_release: "2026-07-25"
stars: "49"
language: "Python"
homepage: null
mcp_support: False
plugin_support: True
claude_code_plugin: True
subagents: True
hooks: True
plan_mode: null
model_providers: "Anthropic (Claude Fable 5, Sonnet 5, Opus 5)"
pricing: "Free / open-source (depends on your Anthropic API/subscription plan)"
install_method: "/plugin marketplace add Rylaa/fable5-opus5-orchestrator && /plugin install orchestrator@fable-orchestrator (requires python3 on PATH; macOS and Linux only)"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: null
sources:
  - "agent_infra"
what_makes_it_special: "Claude Code plugin for token-frugal multi-agent orchestration keeping Claude Fable 5 as the chair while delegating volume work to Sonnet 5 and hard tasks to Opus 5; enforces a Requirements Ledger and guard hooks (spawn/task/close) with fresh-eyes verification on every close."
---

Claude Code plugin for token-frugal multi-agent orchestration keeping Claude Fable 5 as the chair while delegating volume work to Sonnet 5 and hard tasks to Opus 5; enforces a Requirements Ledger and guard hooks (spawn/task/close) with fresh-eyes verification on every close.
