---
name: "wallfacer"
slug: "wallfacer"
layout: "agent.njk"
category: "multiplexer"
maker: "changkun"
license: "MIT"
url: "https://github.com/changkun/wallfacer"
source_code_url: "https://github.com/changkun/wallfacer"
source_available: "True"
platforms:
  - "Autonomous"
first_released: "2026-02-16"
current_release: "2026-08-09"
stars: "76"
language: "Go"
homepage: "https://wf.latere.ai/"
mcp_support: null
plugin_support: "True"
claude_code_plugin: null
subagents: "True"
hooks: null
plan_mode: "True"
model_providers: "Claude Code (Anthropic), Codex (OpenAI), Cursor, OpenCode, Pi"
pricing: "open-source"
install_method: "curl -fsSL https://raw.githubusercontent.com/changkun/wallfacer/main/install.sh | sh"
docs_url: "https://github.com/changkun/wallfacer/blob/main/docs/guide/usage.md"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: null
sources:
  - "github_topic"
what_makes_it_special: "Open-source, locally-run autonomous engineering platform that coordinates AI coding agents across multiple abstraction levels: chat (exploration), specs (structured design), tasks (parallel execution), and code (surgical edits). Provides a task board, plan mode, oversight audit trails, and cost/usage tracking. Works with coding agent harnesses (Claude Code, Codex, Cursor, OpenCode, Pi) through a pluggable harness layer; user-authored agents/flows as YAML in ~/.wallfacer/. Per-task git worktrees for parallel execution, spec lifecycle with dependency DAG, composable sub-agent roles, and circuit breakers."
---

wallfacer exists to keep AI-assisted engineering organized as projects grow, instead of scattering work across chat sessions. Ideas enter as chat, become versioned Markdown specs arranged in a dependency tree with a seven-state lifecycle, and dispatch as tasks onto a kanban board where each task runs as a host process in its own git worktree with auto-test, auto-retry, circuit breakers, and per-task token/cost budgets. A pluggable harness layer lets each task or agent role be pinned to Claude Code, Codex, Cursor, OpenCode, or Pi, and oversight surfaces provide event timelines, diffs, and AI-generated summaries for review. The system is locally run with no cloud dependency and notably has developed much of its own recent functionality. It targets developers who want spec-driven, parallel agent execution on their own machines.
