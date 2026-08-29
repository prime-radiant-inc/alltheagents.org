---
name: "Orca"
slug: "orca"
layout: "agent.njk"
category: "multiplexer"
maker: "stablyai"
license: "MIT"
url: "https://github.com/stablyai/orca"
source_code_url: "https://github.com/stablyai/orca"
source_available: "Yes"
platforms:
  - "CLI"
first_released: "2026-03-17"
current_release: "2026-08-20"
stars: "49120"
language: "TypeScript"
homepage: "https://onOrca.dev"
mcp_support: "no"
plugin_support: "yes (examples/plugins directory)"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "BYOK (uses your own subscriptions to Claude Code, Codex, Cursor, and 25+ agents)"
pricing: "open-source"
install_method: "binary (DMG/EXE/AppImage), brew, AUR, iOS App Store, Android APK"
docs_url: "https://www.onorca.dev/docs/"
plugin_docs_url: null
config_docs_url: "https://www.onorca.dev/docs"
download_url: "https://onorca.dev/download"
maintained: "active"
sources:
  - "author_search"
what_makes_it_special: "An AI Orchestrator / Agent IDE that runs multiple AI coding agents in parallel each in its own isolated git worktree, with a mobile companion app, Design Mode for clicking UI elements into prompts, and SSH worktrees for remote execution."
---

Running several coding agents against one repository means juggling terminal tabs, merge conflicts, and no shared view of who is doing what. Orca, an Electron desktop app from YC-backed Stably AI, runs Claude Code, Codex, OpenCode, Pi, and 30-plus other CLI agents side by side, each in an isolated git worktree, and can fan a single prompt across all of them to compare and merge the best result. A Design Mode feeds clicked UI elements into agent prompts, mobile companion apps (iOS App Store and Android APK) extend control beyond the desk, and the terminal layer uses Ghostty-class WebGL rendering with SSH worktree support. GitHub and Linear integrations plus usage/account tracking round out the workflow, and signed builds ship via SignPath with headless orca serve for Linux servers. MIT-licensed with 56k stars and daily releases, it targets developers running agent fleets rather than a single session.
