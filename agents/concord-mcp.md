---
name: "Concord"
slug: "concord-mcp"
layout: "agent.njk"
category: "other"
maker: "Get-Concord-AI"
license: "MIT"
url: "https://github.com/Get-Concord-AI/concord-mcp"
source_code_url: "https://github.com/Get-Concord-AI/concord-mcp"
source_available: "True"
platforms:
  - "CLI"
first_released: "2026-07-14"
current_release: "2026-08-25"
stars: 283
language: "TypeScript"
homepage: "https://getconcord.ai"
mcp_support: "yes"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: null
pricing: "free"
install_method: "npm (@concord-ai/concord-mcp); state in a .concord/ folder at the repo root, shared by all agents in that repo"
docs_url: "https://github.com/Get-Concord-AI/concord-mcp/blob/main/README.md"
plugin_docs_url: null
config_docs_url: null
download_url: "https://www.npmjs.com/package/@concord-ai/concord-mcp"
maintained: "active"
sources:
  - "hackernews"
what_makes_it_special: "A single local-first MCP server that gives multiple coding agents a shared work state — presence, live messaging, file claims, decisions, and handoffs with review evidence — backed by SQLite in the repo, with tools start_work, inspect_work, update_work, transfer_work, and finish_work. Explicitly not an orchestrator or agent."
---

Concord is the shared nervous system for a set of coding agents working in the same repository: a single MCP server, local-first with SQLite state in a .concord/ folder at the repo root, that lets agents like Claude Code, Codex, Cursor, Gemini CLI, and Grok Build discover each other, exchange live messages and prompts, claim files before editing to detect overlaps, share decisions, and hand off tasks with review evidence. Its MCP tools are start_work, inspect_work, update_work, transfer_work, and finish_work, plus a CLI (concord status, dashboard, doctor) and a TUI dashboard for humans watching the fleet. The project is explicit about what it is not — not an orchestrator, not an autonomous agent, not a code reviewer, not a hosted sync service — and it sends opt-out telemetry that never includes code or file paths. It is the coordination layer around agents rather than a harness, aimed at teams running several agents against one codebase without a human relaying context between them.
