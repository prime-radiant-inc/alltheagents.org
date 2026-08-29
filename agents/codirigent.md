---
name: "Codirigent"
slug: "codirigent"
layout: "agent.njk"
category: "multiplexer"
maker: "oso95"
license: "GPL-3.0"
url: "https://github.com/oso95/Codirigent"
source_code_url: "https://github.com/oso95/Codirigent"
source_available: "True"
platforms:
  - "CLI"
  - "Desktop"
first_released: "2026-02-02"
current_release: "2026-07-09"
stars: "104"
language: "Rust"
homepage: "https://codirigent.dev/"
mcp_support: null
plugin_support: null
claude_code_plugin: "yes"
subagents: null
hooks: "True"
plan_mode: null
model_providers: "Claude Code, Codex, Gemini CLI (wrapped CLIs)"
pricing: "Free / open source"
install_method: "Download .msi (Windows) or .dmg (macOS) from GitHub Releases; or cargo install --path ."
docs_url: "https://codirigent.dev"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/oso95/Codirigent/releases/latest"
maintained: "active"
sources:
  - "github_topic3"
what_makes_it_special: "Purpose-built for parallel AI coding workflows with real-time per-session status indicators, custom saveable grid layouts with drag-and-drop, synced file tree, Git worktree support for branch-isolated agents, automatic session resume for Claude Code/Codex, and smart clipboard that converts file paths for target CLIs"
---

Running several coding CLIs at once means juggling terminal windows with no shared view of what each agent is doing. Codirigent gives those sessions a single workspace: multiple agent CLIs run in parallel panes with live status indicators - idle, working, needs attention, ready - driven by status hooks that the tool registers into each CLI's own configuration (Claude Code, Codex, and Gemini settings files) on first launch. Sessions arrange into custom, saveable grid layouts with drag-and-drop, a synchronized file tree follows the focused session, and git worktree support isolates each agent on its own branch so parallel work does not collide. Session resume recovers Claude Code and Codex sessions automatically after restarts. Developers running several agent CLIs in parallel are the audience; the project is an early alpha with Windows and macOS builds.
