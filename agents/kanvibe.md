---
name: "kanvibe"
slug: "kanvibe"
layout: "agent.njk"
category: "multiplexer"
maker: "rookedsysc"
license: "AGPL-3.0"
url: "https://github.com/rookedsysc/kanvibe"
source_code_url: "https://github.com/rookedsysc/kanvibe"
source_available: "True"
platforms:
  - "CLI"
  - "Desktop"
first_released: "2026-02-10"
current_release: "2026-08-19"
stars: "138"
language: "TypeScript"
homepage: null
mcp_support: null
plugin_support: "True"
claude_code_plugin: "False"
subagents: null
hooks: "True"
plan_mode: null
model_providers: null
pricing: "Free / open-source (AGPL-3.0); commercial SaaS distribution not permitted"
install_method: "Homebrew cask: brew install --cask rookedsysc/kanvibe/kanvibe"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "github_topic3"
what_makes_it_special: "Keyboard-first Kanban workspace that ties AI coding agents to branch-based git worktrees and tmux/zellij terminal sessions; automatically tracks task status via agent hooks across four AI CLIs (Claude Code, Gemini CLI, Codex CLI, OpenCode); live AI session tracking on board cards; in-app AI account/usage management without extra API keys; built-in GitHub-style diff viewer."
---

Agentic CLI work tends to disappear into terminal windows, making it hard to track several parallel tasks. Kanvibe gives each task its own branch and worktree, runs the coding CLI in a tmux or zellij pane attached to the card, and uses the CLIs' hook mechanisms to detect status changes such as a completed edit or an agent waiting on a follow-up question. The board also tracks AI account usage in-app so no extra API keys are needed, and includes a diff viewer for reviewing what each agent changed. It targets solo developers and small teams that run multiple Claude Code, Codex, Gemini CLI, or OpenCode sessions in parallel.
