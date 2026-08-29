---
name: "harness-terminal"
slug: "harness-terminal"
layout: "agent.njk"
category: "multiplexer"
maker: "robzilla1738"
license: "MIT"
url: "https://github.com/robzilla1738/harness-terminal"
source_code_url: "https://github.com/robzilla1738/harness-terminal"
source_available: "True"
platforms:
  - "CLI"
  - "Desktop"
first_released: "2026-05-27"
current_release: "2026-06-13"
stars: "300"
language: "Swift"
homepage: "https://harnesscli.dev"
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "True"
plan_mode: "no"
model_providers: "none (hosts Claude Code, Codex, Cursor, Grok, Gemini, Aider, Goose, OpenCode sessions)"
pricing: "open-source"
install_method: "Download DMG, drag Harness.app to Applications; or build from source via make release"
docs_url: "https://github.com/robzilla1738/harness-terminal/blob/main/docs/"
plugin_docs_url: null
config_docs_url: "https://github.com/robzilla1738/harness-terminal/blob/main/docs/MIGRATION.md"
download_url: "https://github.com/robzilla1738/harness-terminal/releases/latest/download/Harness.dmg"
maintained: "active"
sources:
  - "github_deep"
what_makes_it_special: "Native macOS terminal with GPU rendering, persistent daemon-owned sessions (survive app quit), CLI automation (harness-cli), remote/headless daemon support, and agent detection — monitors coding agents (Claude Code, Codex, Cursor, etc.) and notifies you when an agent stops or needs approval."
---

harness-terminal is a macOS terminal emulator designed around the reality that its users spend their day inside coding agents. A process-tree detector identifies which agent (Claude Code, Codex, Cursor, Grok, Gemini, Aider, Goose, OpenCode, and others) is running in each session and surfaces that in the UI, with desktop notifications and a sidebell when an agent finishes or awaits permission; agents can also self-notify through harness-cli notify. Beneath the agent features sits a full terminal: Metal-based GPU rendering, 490 themes, ligatures, inline images, shell integration, and a command palette. Sessions are owned by a daemon, so tabs, splits, and scrollback survive app quits and even daemon restarts, and the same daemon runs headless on Linux for remote workflows. A harness-cli exposes send-keys, capture-pane, and attachment commands for scripting, with tmux-parity behavior across four experience modes.
