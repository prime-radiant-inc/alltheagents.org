---
name: "pi-mem"
slug: "pi-mem"
layout: "agent.njk"
category: "other"
maker: "jo-inc"
license: "MIT"
url: "https://github.com/jo-inc/pi-mem"
source_code_url: "https://github.com/jo-inc/pi-mem"
source_available: "True"
platforms: []
first_released: "2026-02-11"
current_release: "2026-07-21"
stars: "73"
language: "TypeScript"
homepage: "https://www.npmjs.com/package/@jo-inc/pi-mem"
mcp_support: "no"
plugin_support: "yes"
claude_code_plugin: "yes"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "none (memory layer; the host agent's providers apply)"
pricing: "open-source"
install_method: "pi install git:github.com/jo-inc/pi-mem"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://www.npmjs.com/package/@jo-inc/pi-mem"
maintained: "active"
sources:
  - "brad"
what_makes_it_special: "Persistent memory system (plugin) for the pi coding agent and other LLM agents (Claude Code, etc.). Stores long-term facts (MEMORY.md), daily append-only logs, scratchpads, and notes as plain Markdown. Features context injection into system prompt, keyword search across memory files, dashboard widget with 'Last 24h' session summary, autocommit to git, and configurable via env vars or .pi-mem.json. Not a coding agent harness itself; it's a memory plugin."
---

pi-mem exists because coding agents lose every session's decisions, preferences, and lessons the moment the session ends, and pi ships with no persistent memory of its own. The plugin maintains a set of Markdown files — a curated MEMORY.md of durable facts, an append-only daily log, a scratchpad checklist, and free-form notes — and injects the relevant ones into the system prompt at each turn, with keyword search over the full store on demand. Tools for writing, reading, searching, and scratchpad management are exposed to the agent, while a dashboard widget summarizes the last 24 hours of sessions and optional git auto-commit versions every change. Because everything is plain Markdown, the same store works with Claude Code and other agents, not only pi. Developers running pi on long-lived projects use it to accumulate project conventions and context across sessions.
