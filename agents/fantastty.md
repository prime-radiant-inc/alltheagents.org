---
name: "Fantastty"
slug: "fantastty"
layout: "agent.njk"
category: "other"
maker: "blaine"
license: "MIT"
url: "https://github.com/blaine/fantastty"
source_code_url: "https://github.com/blaine/fantastty"
source_available: "True"
platforms:
  - "Desktop"
first_released: "2026-02-06"
current_release: "2026-07-03"
stars: "47"
language: "Swift (SwiftUI; uses Zig for Ghostty dependency)"
homepage: null
mcp_support: null
plugin_support: null
claude_code_plugin: null
subagents: null
hooks: null
plan_mode: null
model_providers: null
pricing: "Free (open source)"
install_method: "Download signed/notarized DMG from GitHub Releases (requires macOS 15.0+ Sequoia, Apple Silicon); alternatively build from source with Xcode 16+, Zig, and make xcframework"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/blaine/fantastty/releases"
maintained: "active"
sources:
  - "user_reported"
what_makes_it_special: "A macOS terminal app built on Ghostty (libghostty) with workspace-based session management and persistent tmux-backed sessions. Workspaces are independent sidebar items with tabs, timestamped notes (with revision history), auto-generated names, and tracked ticket/PR URLs (via UI or shell escape sequences). Supports SSH sessions with tmux persistence on both ends, workspace archiving, and attention indicators (background workspaces light up on bell/command completion). Shell integration with zsh. Not a coding agent harness; a terminal app. ~47 stars."
---

Fantastty wraps Ghostty's rendering core (libghostty as a static library) in a SwiftUI terminal aimed at developers whose work spans many long-lived sessions. Workspaces are sidebar items with their own tabs, notes, and metadata, auto-named for quick identification, while tmux backing keeps shell sessions alive across restarts and reconnects. Notes can be written from the shell itself via a zsh integration (fantastty-note), workspaces carry ticket or PR URLs, and SSH sessions get first-class treatment alongside local ones. It targets macOS developers — including those running AI CLI agents — who want terminal history and workspace state to survive context switches, with no AI features of its own.
