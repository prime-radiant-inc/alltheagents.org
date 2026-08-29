---
name: "fable5-opus5-orchestrator"
slug: "fable5-opus5-orchestrator"
layout: "agent.njk"
category: "multiplexer"
maker: "Rylaa"
license: "MIT"
url: "https://github.com/Rylaa/fable5-opus5-orchestrator"
source_code_url: "https://github.com/Rylaa/fable5-opus5-orchestrator"
source_available: "True"
platforms: []
first_released: "2026-06-12"
current_release: "2026-07-25"
stars: "49"
language: "Python"
homepage: null
mcp_support: "False"
plugin_support: "True"
claude_code_plugin: "True"
subagents: "True"
hooks: "True"
plan_mode: null
model_providers: "Anthropic (Claude Fable 5, Sonnet 5, Opus 5)"
pricing: "Free / open-source (depends on your Anthropic API/subscription plan)"
install_method: "/plugin marketplace add Rylaa/fable5-opus5-orchestrator && /plugin install orchestrator@fable-orchestrator (requires python3 on PATH; macOS and Linux only)"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "agent_infra"
what_makes_it_special: "Claude Code plugin for token-frugal multi-agent orchestration keeping Claude Fable 5 as the chair while delegating volume work to Sonnet 5 and hard tasks to Opus 5; enforces a Requirements Ledger and guard hooks (spawn/task/close) with fresh-eyes verification on every close."
---

The plugin addresses a cost problem specific to frontier subscriptions: every token an expensive chair model spends on routine work is a token unavailable for thinking, so Fable 5 is confined to planning and arbitration while Sonnet 5 writes code and tests and Opus 5 handles architecture, security review, and final verification. A /fire workflow clarifies the request one question at a time, writes a requirements ledger to .workflow/LEDGER.md, delegates to sized workers, and has a fresh agent verify the result. Five hook-based gates (Clarify, Approve, Spawn, Task list, Close) block non-compliant tool calls rather than trusting instructions, and a watchdog monitors spawned agents for stalled states. Claude Code subscribers on usage-limited plans running multi-step engineering work are the intended users.
