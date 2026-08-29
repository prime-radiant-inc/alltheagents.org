---
name: "forge-orchestrator"
slug: "forge-orchestrator"
layout: "agent.njk"
category: "multiplexer"
maker: "tarunms7"
license: "MIT"
url: "https://github.com/tarunms7/forge-orchestrator"
source_code_url: "https://github.com/tarunms7/forge-orchestrator"
source_available: "True"
platforms: []
first_released: "2026-02-27"
current_release: "2026-04-15"
stars: "42"
language: "Python"
homepage: null
mcp_support: "True"
plugin_support: null
claude_code_plugin: null
subagents: "True"
hooks: null
plan_mode: "True"
model_providers: "Anthropic, OpenAI"
pricing: "open-source"
install_method: "curl -fsSL https://raw.githubusercontent.com/tarunms7/forge-orchestrator/main/install.sh | sh"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/tarunms7/forge-orchestrator"
maintained: "active"
sources:
  - "agent_infra"
what_makes_it_special: "Self-evolving multi-agent orchestrator built on Claude Code. Plans tasks, runs parallel agents in isolated git worktrees, 5-gate review pipeline (build/lint/test/LLM review/contracts), Contract Builder generates binding API specs before coding. Self-evolving learning captures lessons from failures and applies them cross-pipeline. Real-time cost tracking with budget limits, multi-repo workspaces, health monitor for stuck tasks."
---

FORGE addresses the failure mode of running several coding agents at once: duplicated work, conflicting interfaces, and diffs nobody reviewed. A planner reads the codebase, asks clarifying questions, and produces a task DAG the user edits and approves; binding API/type contracts are generated before coding begins; one agent per git worktree executes in parallel with a health monitor watching for stuck tasks. Every change passes five gates (build, lint, test, LLM review, contract check) before auto-rebase, merge, and a single pull request via the GitHub CLI. Lessons captured from failed-then-retried tasks persist across pipelines, per-stage model routing balances cost and quality, and a Textual TUI plus Next.js dashboard expose state. Solo maintainers and small teams using Claude Code as their main harness are the audience.
