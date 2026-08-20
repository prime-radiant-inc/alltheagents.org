---
name: "gastown"
slug: "gastown"
layout: "agent.njk"
category: "multiplexer"
maker: "gastownhall"
license: "MIT"
url: "https://github.com/steveyegge/gastown"
source_code_url: "https://github.com/steveyegge/gastown"
source_available: "Yes"
platforms: []
first_released: "2025-12-16"
current_release: "2026-08-19"
stars: "17670"
language: "Go"
homepage: null
mcp_support: "no"
plugin_support: "yes (plugins/ directory and plugin-system design doc)"
claude_code_plugin: "yes (Claude Code is a primary runtime; uses .claude/settings.json hooks)"
subagents: "yes (Polecats — worker agents with persistent identity, spawned for tasks)"
hooks: "yes (git worktree-based persistent storage; lifecycle hooks for session events)"
plan_mode: null
model_providers: "claude, gemini, codex, kiro, cursor, auggie, amp, opencode, copilot, pi, omp; custom agents configurable"
pricing: "open-source (MIT)"
install_method: "brew"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "brad"
what_makes_it_special: "Multi-agent orchestration system that coordinates 20-30+ AI coding agents working on different tasks simultaneously, using git-backed hooks for persistent work state that survives agent crashes and restarts, with built-in merge queue, scheduling, escalation, and federation features."
---

Multi-agent orchestration system that coordinates 20-30+ AI coding agents working on different tasks simultaneously, using git-backed hooks for persistent work state that survives agent crashes and restarts, with built-in merge queue, scheduling, escalation, and federation features.
