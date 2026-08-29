---
name: "Claude Squad"
slug: "claude-squad"
layout: "agent.njk"
category: "multiplexer"
maker: "smtg-ai"
license: "AGPL-3.0"
url: "https://github.com/smtg-ai/claude-squad"
source_code_url: "https://github.com/smtg-ai/claude-squad"
source_available: "True"
platforms:
  - "CLI"
  - "IDE"
first_released: "2025-03-09"
current_release: "2026-07-30"
stars: "8341"
language: "Go"
homepage: "https://smtg-ai.github.io/claude-squad/"
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "Claude Code, OpenAI Codex, Google Gemini, Aider, OpenCode, Amp"
pricing: "open-source"
install_method: "brew"
docs_url: "https://smtg-ai.github.io/claude-squad/"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/smtg-ai/claude-squad/releases"
maintained: "active"
sources:
  - "brad"
what_makes_it_special: "Terminal app (TUI) that manages multiple AI coding agents in separate isolated git worktrees, letting you run multiple tasks simultaneously in the background via tmux. Auto-accept/yolo mode. Review, commit, checkout, and push changes from a single terminal interface. Agent-agnostic -- works with virtually any CLI-based AI coding assistant (Claude Code, Codex, Gemini, Aider, OpenCode, Amp) through configurable profiles."
---

Claude Squad addresses the constraint that one terminal and one branch limit agents to one task at a time. It creates a tmux session plus git worktree per task so agents work on isolated branches without conflicting, while a single TUI lists sessions, shows previews and diffs, and handles review, commit, and push across all of them. A profiles system in ~/.claude-squad/config.json makes it agent-agnostic, so any terminal coding assistant can be dropped in. Background completion with auto-accept (-y) supports unattended runs. It is AGPL-3.0, written in Go, brew-installable, actively maintained by smtg-ai, and among the most widely adopted multiplexers in this census.
