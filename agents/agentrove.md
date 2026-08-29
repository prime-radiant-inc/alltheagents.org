---
name: "agentrove"
slug: "agentrove"
layout: "agent.njk"
category: "multiplexer"
maker: "Mng-dev-ai"
license: "Apache-2.0"
url: "https://github.com/Mng-dev-ai/agentrove"
source_code_url: "https://github.com/Mng-dev-ai/agentrove"
source_available: "True"
platforms: []
first_released: "2025-12-15"
current_release: "2026-08-15"
stars: "316"
language: "Python, TypeScript, Rust"
homepage: null
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: "no"
subagents: "True"
hooks: "True"
plan_mode: "no"
model_providers: "Claude Code, Codex, Copilot, Cursor, Grok, OpenCode (via ACP adapters)"
pricing: "Free/open-source (Apache 2.0)"
install_method: "git clone; cp .env.example .env; set SECRET_KEY via openssl rand -hex 32; docker compose up -d (open http://localhost:3000)"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/Mng-dev-ai/agentrove/releases/latest"
maintained: "active"
sources:
  - "github_topic3"
what_makes_it_special: "Self-hosted AI coding workspace that orchestrates multiple AI coding agents (not just one) from one interface via ACP adapters, each in its own Docker/host sandbox. Multi-agent 'agent fleet' orchestration: a lead agent on a strong model decomposes work and routes tasks to specialized worker agents/models/personas running in parallel git worktrees. Ships as Docker web app, macOS Tauri desktop, and native iOS."
---

Running several coding agents usually means juggling terminal windows, scattered config, and no shared history. Agentrove bundles chat, editor, terminal, diffs, secrets, and git tooling into one self-hosted web workspace, with each agent (Antigravity, Claude Code, Codex, Copilot, Cursor, Grok, OpenCode) connected through ACP adapters and each workspace isolated in its own Docker or host sandbox. A bundled MCP server exposes the instance as orchestrator tools, enabling sub-threads where a lead chat spawns worker chats in isolated worktrees, fans reviewer personas over diffs, and delegates accepted fixes back. Workers can run unattended in full-execution mode while the lead polls and evaluates results. It ships as a Docker Compose stack with a Tauri macOS desktop app and an iOS thin client, under Apache 2.0.
