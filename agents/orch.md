---
name: "ORCH"
slug: "orch"
layout: "agent.njk"
category: "multiplexer"
maker: "oxgeneral"
license: "MIT"
url: "https://github.com/oxgeneral/ORCH"
source_code_url: "https://github.com/oxgeneral/ORCH"
source_available: "True"
platforms:
  - "CLI"
first_released: "2026-03-10"
current_release: "2026-08-01"
stars: "144"
language: "TypeScript"
homepage: "https://www.orch.one/"
mcp_support: "no"
plugin_support: "True"
claude_code_plugin: "True"
subagents: "True"
hooks: "no"
plan_mode: "True"
model_providers: "none (drives existing CLI agents: Claude Code, OpenCode, Codex, Pi, Cursor, Grok, Antigravity, plus a generic Shell adapter)"
pricing: "Open-source (MIT). You pay only for the AI APIs you already use (Claude, Codex, etc.)"
install_method: "npm install -g @oxgeneral/orch"
docs_url: "https://www.orch.one/"
plugin_docs_url: null
config_docs_url: "https://github.com/oxgeneral/ORCH/tree/main/docs"
download_url: "https://www.npmjs.com/package/@oxgeneral/orch"
maintained: "active"
sources:
  - "brad"
what_makes_it_special: "Coordinates multiple AI agents (and any CLI tool) in parallel on one project with isolated git worktrees, a state machine (todo -> in_progress -> review -> done) with mandatory code review, zero infrastructure (no database, no cloud, no Docker), file-based state, and pre-built team templates for engineering and non-engineering workflows. Includes /orch skill for Claude Code."
---

Orchestrating several AI agents on one repository usually introduces infrastructure: queues, databases, dashboards. ORCH keeps everything in the repo: an orchestrating CTO agent decomposes a goal into tasks, worker agents (Claude Code, Codex, Pi, Cursor, OpenCode, Grok, Antigravity, or a generic Shell adapter) execute in parallel inside isolated git worktrees, and a review gate blocks merging until a reviewer agent approves. State lives in .orchestry/ as plain YAML/JSON/JSONL — no database, no Docker, no accounts — with auto-retry, zombie detection, and inter-agent messaging handled by the CLI. Beyond code, the same Shell adapter runs editorial, sales, analytics, security, and DevOps workflows, and a headless orch serve daemon supports 24/7 operation under pm2 or systemd. Install is one npm global with Node 20+ on macOS, Linux, or WSL2, MIT-licensed with roughly 1,950 tests. Solo operators and small teams running agent fleets without infrastructure are the audience.
