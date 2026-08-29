---
name: "tmux-assistant-resurrect"
slug: "tmux-assistant-resurrect"
layout: "agent.njk"
category: "multiplexer"
maker: "timvw"
license: "MIT"
url: "https://github.com/timvw/tmux-assistant-resurrect"
source_code_url: "https://github.com/timvw/tmux-assistant-resurrect"
source_available: "True"
platforms:
  - "CLI"
first_released: "2026-02-14"
current_release: "2026-08-19"
stars: "78"
language: "Shell"
homepage: null
mcp_support: "no"
plugin_support: "yes"
claude_code_plugin: "False"
subagents: "no"
hooks: "True"
plan_mode: "no"
model_providers: null
pricing: "open-source"
install_method: "Tmux Plugin Manager (TPM): set -g @plugin 'timvw/tmux-assistant-resurrect' in ~/.tmux.conf, then prefix + I"
docs_url: "https://github.com/timvw/tmux-assistant-resurrect"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "github_topic2"
what_makes_it_special: "tmux plugin that persists and restores AI coding assistant sessions (Claude Code, GitHub Copilot CLI, OpenCode, Codex CLI, Pi, Oh My Pi, Grok) across tmux restarts and reboots. Hooks into tmux-resurrect to save assistant session IDs, CLI flags, and environment variables, then re-launches with the same config. Installs tool-native hooks (Claude Code SessionStart/SessionEnd hooks, OpenCode session-tracker plugin). Docker-based test suite with 400+ tests."
---

tmux-assistant-resurrect solves a narrow but costly problem: AI coding assistant sessions vanish when tmux restarts or the machine reboots, taking their conversation context with them. The plugin attaches to the tmux-resurrect and tmux-continuum save cycle, snapshotting every pane with ps and recording which recognized assistant CLI each pane runs along with its session ID, flags, and environment in a JSON manifest. On restore it rebuilds the original command line and feeds it to each pane with tmux send-keys, so the seven supported CLIs resume where they left off; tool-native hooks (Claude Code SessionStart/SessionEnd, an OpenCode session-tracker plugin) are wired in alongside. Distribution is a four-line TPM block, and the project ships a Docker-based test suite of 400+ checks on GitHub Actions, though the author describes it as vibecoded with limited production exposure. Terminal-centric developers who juggle several assistant sessions across reboots are the users.
