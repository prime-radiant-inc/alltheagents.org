---
name: "stoneforge"
slug: "stoneforge"
layout: "agent.njk"
category: "multiplexer"
maker: "stoneforge-ai"
license: "Apache-2.0"
url: "https://github.com/stoneforge-ai/stoneforge"
source_code_url: "https://github.com/stoneforge-ai/stoneforge"
source_available: True
platforms:
  - "Web"
first_released: "2026-02-14"
current_release: "2026-05-05"
stars: "175"
language: "TypeScript"
homepage: "https://stoneforge.ai"
mcp_support: False
plugin_support: False
claude_code_plugin: False
subagents: True
hooks: True
plan_mode: True
model_providers: "Claude Code, OpenCode, OpenAI Codex"
pricing: "Free / open source (Apache-2.0); costs are underlying AI provider subscriptions"
install_method: "npm install -g @stoneforge/smithy"
docs_url: "https://github.com/stoneforge-ai/stoneforge#readme"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "agent_infra"
what_makes_it_special: "Web dashboard and runtime for orchestrating AI coding agents (multi-agent orchestration platform). Two layers: Smithy (orchestrator) and Quarry (event-sourced data SDK). Features automatic git worktree isolation per worker, event-sourced state (SQLite + JSONL) with full audit trail, dispatch daemon for auto task assignment by priority, merge steward (runs tests, squash-merges on pass), multi-provider support (Claude Code, OpenCode, OpenAI Codex), multi-plan scaling, resumable workflows, persistent knowledge base with FTS5 + semantic search, and web dashboard with real-time agent output, kanban boards, and in-browser code editor."
---

Web dashboard and runtime for orchestrating AI coding agents (multi-agent orchestration platform). Two layers: Smithy (orchestrator) and Quarry (event-sourced data SDK). Features automatic git worktree isolation per worker, event-sourced state (SQLite + JSONL) with full audit trail, dispatch daemon for auto task assignment by priority, merge steward (runs tests, squash-merges on pass), multi-provider support (Claude Code, OpenCode, OpenAI Codex), multi-plan scaling, resumable workflows, persistent knowledge base with FTS5 + semantic search, and web dashboard with real-time agent output, kanban boards, and in-browser code editor.
