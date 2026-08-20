---
name: "tmux-assistant-resurrect"
slug: "tmux-assistant-resurrect"
layout: "agent.njk"
category: "multiplexer"
maker: "timvw"
license: "MIT"
url: "https://github.com/timvw/tmux-assistant-resurrect"
source_code_url: "https://github.com/timvw/tmux-assistant-resurrect"
source_available: True
platforms:
  - "CLI"
first_released: "2026-02-14"
current_release: "2026-08-19"
stars: "78"
language: "Shell"
homepage: null
mcp_support: null
plugin_support: null
claude_code_plugin: False
subagents: null
hooks: True
plan_mode: null
model_providers: null
pricing: null
install_method: "Tmux Plugin Manager (TPM): set -g @plugin 'timvw/tmux-assistant-resurrect' in ~/.tmux.conf, then prefix + I"
docs_url: "https://github.com/timvw/tmux-assistant-resurrect"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: null
sources:
  - "github_topic2"
what_makes_it_special: "tmux plugin that persists and restores AI coding assistant sessions (Claude Code, GitHub Copilot CLI, OpenCode, Codex CLI, Pi, Oh My Pi, Grok) across tmux restarts and reboots. Hooks into tmux-resurrect to save assistant session IDs, CLI flags, and environment variables, then re-launches with the same config. Installs tool-native hooks (Claude Code SessionStart/SessionEnd hooks, OpenCode session-tracker plugin). Docker-based test suite with 400+ tests."
---

tmux plugin that persists and restores AI coding assistant sessions (Claude Code, GitHub Copilot CLI, OpenCode, Codex CLI, Pi, Oh My Pi, Grok) across tmux restarts and reboots. Hooks into tmux-resurrect to save assistant session IDs, CLI flags, and environment variables, then re-launches with the same config. Installs tool-native hooks (Claude Code SessionStart/SessionEnd hooks, OpenCode session-tracker plugin). Docker-based test suite with 400+ tests.
