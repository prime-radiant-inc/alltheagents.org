---
name: "amux"
slug: "amux"
layout: "agent.njk"
category: "multiplexer"
maker: "andyrewlee"
license: "MIT"
url: "https://github.com/andyrewlee/amux"
source_code_url: "https://github.com/andyrewlee/amux"
source_available: "True"
platforms:
  - "CLI"
first_released: "2025-12-31"
current_release: "2026-08-17"
stars: "147"
language: "Go"
homepage: null
mcp_support: null
plugin_support: "False"
claude_code_plugin: "False"
subagents: null
hooks: null
plan_mode: null
model_providers: null
pricing: "Free / open-source"
install_method: "brew tap andyrewlee/amux && brew install amux, or install script (curl -fsSL https://raw.githubusercontent.com/andyrewlee/amux/main/install.sh | sh), or go install github.com/andyrewlee/amux/cmd/amux@latest"
docs_url: null
plugin_docs_url: null
config_docs_url: "https://github.com/andyrewlee/amux/blob/main/docs/CONFIG.md"
download_url: null
maintained: "active"
sources:
  - "brad"
what_makes_it_special: "TUI for running multiple coding agents in parallel using tmux sessions with git worktree-based isolated workspaces; no wrappers - works directly with existing agents (Claude Code, Codex, Gemini, Amp, OpenCode, Droid)."
---

Running three coding agents on one repo means three agents trampling the same working tree; amux solves this with tmux sessions per agent and git worktrees per workspace, so parallel work stays isolated and merges back cleanly. The Go TUI gives keyboard-and-mouse control over starting, diffing, committing, and merging workspaces, with per-workspace port allocation and extensive env-var hooks for scripting. Agents — Claude Code, Codex, OpenCode, Droid, Cursor, Grok, Amp, Cline — are configured per-user in ~/.amux/config.json while workspaces are per-project in .amux/workspaces.json. Actively maintained Go project (869 commits, GoReleaser, CI, Discord) licensed MIT for Linux and macOS.
