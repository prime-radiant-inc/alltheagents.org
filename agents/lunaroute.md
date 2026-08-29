---
name: "lunaroute"
slug: "lunaroute"
layout: "agent.njk"
category: "other"
maker: "erans"
license: "Apache-2.0"
url: "https://github.com/erans/lunaroute"
source_code_url: "https://github.com/erans/lunaroute"
source_available: "True"
platforms:
  - "CLI"
first_released: "2025-10-07"
current_release: "2026-07-27"
stars: "186"
language: "Rust"
homepage: null
mcp_support: "False"
plugin_support: "False"
claude_code_plugin: "False"
subagents: "no"
hooks: "False"
plan_mode: "False"
model_providers: "OpenAI, Anthropic"
pricing: "Free / open source (Apache 2.0); uses your own API keys"
install_method: "Download prebuilt binary from GitHub Releases, or build from source with cargo build --release"
docs_url: "https://github.com/erans/lunaroute#readme"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/erans/lunaroute/releases"
maintained: "active"
sources:
  - "github_topic2"
what_makes_it_special: "High-performance local proxy for AI coding assistants (Claude Code, OpenAI Codex CLI, OpenCode) with zero-overhead passthrough, sub-millisecond latency, dual-dialect passthrough (OpenAI + Anthropic formats simultaneously), comprehensive session recording (SQLite + JSONL), automatic PII redaction, built-in Web UI, and Prometheus metrics. One-command setup via eval $(lunaroute-server env)."
---

Teams adopting coding CLIs need visibility into what those agents send to model APIs without adding a cloud hop. LunaRoute sits locally in front of the assistants: one shell command starts the proxy and points ANTHROPIC_BASE_URL and OPENAI_BASE_URL at it, after which traffic passes through with sub-millisecond latency and full API fidelity, including WebSocket transport for Codex CLI. Every request and response is recorded with token counts, tool calls, and cost estimates, searchable through a built-in web UI, and PII is redacted pre-persistence under a local-first, zero-trust storage model. Prometheus metrics expose 24 metric types for operations dashboards. Individual developers and small teams with compliance constraints are the natural users.
