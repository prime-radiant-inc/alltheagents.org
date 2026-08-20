---
name: "wallfacer"
slug: "wallfacer"
layout: "agent.njk"
category: "agent"
maker: "changkun"
license: "MIT"
url: "https://github.com/changkun/wallfacer"
source_code_url: "https://github.com/changkun/wallfacer"
source_available: True
platforms:
  - "Autonomous"
first_released: "2026-02-16"
current_release: "2026-08-09"
stars: "76"
language: "Go"
homepage: "https://wf.latere.ai/"
mcp_support: null
plugin_support: True
claude_code_plugin: null
subagents: True
hooks: null
plan_mode: True
model_providers: "Claude Code (Anthropic), Codex (OpenAI), Cursor, OpenCode, Pi"
pricing: null
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

Open-source, locally-run autonomous engineering platform that coordinates AI coding agents across multiple abstraction levels: chat (exploration), specs (structured design), tasks (parallel execution), and code (surgical edits). Provides a task board, plan mode, oversight audit trails, and cost/usage tracking. Works with coding agent harnesses (Claude Code, Codex, Cursor, OpenCode, Pi) through a pluggable harness layer; user-authored agents/flows as YAML in ~/.wallfacer/. Per-task git worktrees for parallel execution, spec lifecycle with dependency DAG, composable sub-agent roles, and circuit breakers.
