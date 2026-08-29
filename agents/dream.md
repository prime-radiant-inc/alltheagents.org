---
name: "dream"
slug: "dream"
layout: "agent.njk"
category: "multiplexer"
maker: "dreamide"
license: "MIT"
url: "https://github.com/dreamide/dream"
source_code_url: "https://github.com/dreamide/dream"
source_available: "True"
platforms:
  - "IDE"
first_released: "2026-05-11"
current_release: "2026-08-19"
stars: "41"
language: "TypeScript"
homepage: "https://dreamide.app"
mcp_support: null
plugin_support: null
claude_code_plugin: null
subagents: null
hooks: null
plan_mode: null
model_providers: null
pricing: "open-source"
install_method: "Download pre-built installers (macOS .dmg, Windows .exe, Linux .deb/.rpm/.AppImage) or clone and pnpm install for development"
docs_url: "https://dreamide.app"
plugin_docs_url: null
config_docs_url: null
download_url: "https://files.dreamide.app/latest/"
maintained: "active"
sources:
  - "github_deep"
what_makes_it_special: "Desktop IDE built specifically for working with multiple AI coding agents. Multi-project workspace with the ability to view multiple agent chats simultaneously alongside standard IDE features. Supports Codex, Claude Code, OpenCode, and Cursor Agent CLIs."
---

Working with several coding agents usually means several terminal windows and no shared view of what changed. Dream is an Electron desktop IDE that arranges multiple agent chats side by side in a multi-project workspace, with git status, commit, push, and PR flows, a file explorer, diff rendering, an integrated terminal, and a browser preview panel in the same window. It ships no model of its own — users bring at least one supported agent CLI (Codex, Claude Code, OpenCode, Cursor Agent), and the IDE hosts and visualizes their sessions. Developers juggling parallel agent tasks across repos are the intended users. The repository now lives under umami-software/dream and remains active.
