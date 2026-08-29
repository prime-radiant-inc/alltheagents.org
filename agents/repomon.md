---
name: "repomon"
slug: "repomon"
layout: "agent.njk"
category: "multiplexer"
maker: "AliHamzaAzam"
license: "Apache-2.0"
url: "https://github.com/AliHamzaAzam/repomon"
source_code_url: "https://github.com/AliHamzaAzam/repomon"
source_available: "True"
platforms:
  - "CLI"
  - "IDE"
first_released: "2026-05-29"
current_release: "2026-08-19"
stars: "14"
language: "Rust"
homepage: "https://repomon.alihamzaazam.com"
mcp_support: "True"
plugin_support: null
claude_code_plugin: null
subagents: "True"
hooks: null
plan_mode: null
model_providers: "Claude Code, Codex, Antigravity, OpenCode, Cursor, Aider"
pricing: "open-source"
install_method: "Desktop app (DMG/EXE/AppImage/deb/rpm) from GitHub releases; CLI via curl install script, Homebrew, or cargo install --git"
docs_url: "https://github.com/AliHamzaAzam/repomon/blob/main/docs/architecture.md"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/AliHamzaAzam/repomon/releases/latest"
maintained: "active"
sources:
  - "brad"
what_makes_it_special: "Mission control for managing a fleet of AI coding agents across many repos x many worktrees x many agents simultaneously. Unlike tools that run parallel agents in one repo, repomon is built for developers juggling 5-15 active projects with a fleet of agents running at once. Durable tmux-backed runtime, desktop app and TUI clients, git explorer, in-app editor, fleet mail between agents, remote access via WebSocket bridge, usage limit tracking. An orchestrator (repomind) spawns and manages worker agents."
---

Running five agents in five repos means five terminals, five notification streams, and no overview of which one is blocked; repomon exists to collapse that into one screen. A single daemon backs a Tauri desktop app and a Rust TUI with four zoom levels, from a fleet overview down to a single agent's scrollback, with agents waiting on the human floated to the top. Fleet mail routes messages between agents per lane or broadcast, a git explorer and editor resolve merge conflicts in place, and a token-gated WebSocket bridge exposes the whole board over Tailscale for remote access. It is aimed at developers who treat multiple agent sessions as a permanent part of their workflow rather than an experiment.
