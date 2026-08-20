---
name: "sandbox-agent"
slug: "sandbox-agent"
layout: "agent.njk"
category: "multiplexer"
maker: "rivet-dev"
license: "Apache-2.0"
url: "https://github.com/rivet-dev/sandbox-agent"
source_code_url: "https://github.com/rivet-dev/sandbox-agent"
source_available: True
platforms: []
first_released: "2026-01-25"
current_release: "2026-06-19"
stars: "1538"
language: "Rust (server) + TypeScript (SDK)"
homepage: "https://sandboxagent.dev"
mcp_support: "partial - planned (roadmap: automatic MCP/skill/hook configuration)"
plugin_support: "yes - skill-based system (npx skills add)"
claude_code_plugin: "n/a - Claude Code is a supported agent; .claude config dir present"
subagents: "no"
hooks: "partial - planned (roadmap)"
plan_mode: "no"
model_providers: "OpenAI, Anthropic (via supported agents)"
pricing: "open-source"
install_method: "npm"
docs_url: "https://sandboxagent.dev/docs"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "github_topic3"
what_makes_it_special: "Server that runs inside sandboxes to remotely control coding agents (Claude Code, Codex, OpenCode, Cursor, Amp, Pi) over HTTP/SSE. Universal Agent API - one HTTP interface controls six different agents, swappable via config. Universal Session Schema normalizes all agent event formats for storage/replay (Postgres, ClickHouse, Rivet). Single Rust static binary, fast startup, runs anywhere (E2B, Daytona, Modal, Cloudflare Containers, Docker). Replaces fragile SSH/TTY piping that breaks streaming, permissions, and human-in-the-loop flows. Dual mode: HTTP server or embedded via TypeScript SDK. Built-in Inspector UI."
---

Server that runs inside sandboxes to remotely control coding agents (Claude Code, Codex, OpenCode, Cursor, Amp, Pi) over HTTP/SSE. Universal Agent API - one HTTP interface controls six different agents, swappable via config. Universal Session Schema normalizes all agent event formats for storage/replay (Postgres, ClickHouse, Rivet). Single Rust static binary, fast startup, runs anywhere (E2B, Daytona, Modal, Cloudflare Containers, Docker). Replaces fragile SSH/TTY piping that breaks streaming, permissions, and human-in-the-loop flows. Dual mode: HTTP server or embedded via TypeScript SDK. Built-in Inspector UI.
