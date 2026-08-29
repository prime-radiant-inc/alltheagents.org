---
name: "AgentsView"
slug: "agentsview"
layout: "agent.njk"
category: "other"
maker: "kenn-io"
license: "MIT"
url: "https://github.com/kenn-io/agentsview"
source_code_url: "https://github.com/kenn-io/agentsview"
source_available: "True"
platforms:
  - "CLI"
first_released: "2026-02-19"
current_release: "2026-08-20"
stars: "5146"
language: "Go"
homepage: "https://agentsview.io"
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "LiteLLM, OpenRouter (for cost calculation); reads sessions from 20+ agents"
pricing: "open-source"
install_method: "binary"
docs_url: "https://agentsview.io"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/kenn-io/agentsview/releases"
maintained: "active"
sources:
  - "author_search"
what_makes_it_special: "Local-first analytics tool (single Go binary) that browses, searches, and tracks costs across 20+ AI coding agents' session data. SQLite-indexed for 100x faster queries vs re-parsing raw files. Multi-backend (SQLite, PostgreSQL, DuckDB), full-text + semantic search, SSE live updates, privacy-focused (loopback binding, disableable telemetry), Tauri desktop wrapper."
---

Session logs from coding agents pile up in vendor-specific formats, making cost tracking and history search a per-tool chore. AgentsView discovers sessions from a long list of agents (Claude Code, Codex, Copilot CLI, Gemini CLI, Cursor, Windsurf, OpenCode, Goose, Aider, Devin CLI, Zed, Warp, and dozens more), normalizes them into a local SQLite database with FTS5 search, and serves a local web UI with usage dashboards, activity heatmaps, and live SSE updates. Everything stays on the machine by default; optional PostgreSQL push supports team dashboards and DuckDB offers a read-only analytical mirror. Cost analytics are cache-aware with LiteLLM/OpenRouter pricing, positioned as a dramatically faster replacement for ccusage-style accounting. Distribution is a single binary via install script, Homebrew cask, GitHub releases, or Docker.
