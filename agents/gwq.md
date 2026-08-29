---
name: "gwq"
slug: "gwq"
layout: "agent.njk"
category: "other"
maker: "d-kuro"
license: "Apache-2.0"
url: "https://github.com/d-kuro/gwq"
source_code_url: "https://github.com/d-kuro/gwq"
source_available: "True"
platforms: []
first_released: "2025-05-26"
current_release: "2026-05-02"
stars: "463"
language: "Go"
homepage: null
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "none"
pricing: "Free / open-source"
install_method: "Homebrew (brew install d-kuro/tap/gwq), go install, or build from source"
docs_url: "https://github.com/d-kuro/gwq#readme"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/d-kuro/gwq"
maintained: "active"
sources:
  - "github_topic"
what_makes_it_special: "CLI for managing Git worktrees with a fuzzy finder; enables parallel AI coding agent workflows by allowing multiple AI agents to work in isolated worktrees simultaneously without merge conflicts"
---

gwq manages Git worktrees from the command line with a fuzzy-finder interface, letting a developer spin up isolated working copies per task in seconds. Its main use case is parallel AI coding: each agent runs in its own worktree, so several Claude Code or Codex sessions can proceed on separate branches without interfering, and gwq's status dashboard with watch mode tracks what each worktree contains. Beyond worktree CRUD it offers global cross-repository discovery, exec and cd helpers, tmux integration for long-running processes, JSON/CSV output for scripting, and shell completions. The tool itself contains no AI; it is the scaffolding that makes multi-agent workflows practical for a single developer.
