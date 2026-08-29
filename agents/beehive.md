---
name: "beehive"
slug: "beehive"
layout: "agent.njk"
category: "multiplexer"
maker: "storozhenko98"
license: "MIT"
url: "https://github.com/storozhenko98/beehive"
source_code_url: "https://github.com/storozhenko98/beehive"
source_available: "True"
platforms: []
first_released: "2026-02-23"
current_release: "2026-08-12"
stars: "60"
language: "Rust, TypeScript"
homepage: "https://www.beehiveapp.dev"
mcp_support: null
plugin_support: null
claude_code_plugin: "False"
subagents: null
hooks: null
plan_mode: null
model_providers: null
pricing: "Free / open source (MIT)"
install_method: "Desktop: .dmg from Releases; TUI: curl -fsSL beehiveapp.dev/install.sh | bash; From source: npm install + npm run tauri build or cargo build --release"
docs_url: "https://www.beehiveapp.dev"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/storozhenko98/beehive/releases/latest"
maintained: "active"
sources:
  - "github_topic"
what_makes_it_special: "Orchestrates coding agents across isolated git workspaces; manage multiple repos, create isolated workspace clones (combs) on different branches, run terminals and AI agents side-by-side from one window; supports launching Claude Code or any CLI agent; custom buttons for per-repo agent commands"
---

Beehive organizes AI coding agent workspaces the way tmux organizes terminals: repos are 'hives', grouped into 'nests', each with isolated full git clones ('combs') on any branch, and persistent 'panes' that hold terminal or agent sessions across context switches. Agents such as Claude Code run as ordinary CLI processes inside panes, so the app manages workspaces and sessions rather than coding itself - fitting the multiplexer category. Isolated workspace clones (combs) can be duplicated, including uncommitted changes, for safe experimentation on different branches, with per-repo quick-launch buttons and persisted pane layouts. It ships as a macOS desktop GUI (Tauri) and a Rust TUI for macOS and Linux, MIT-licensed, with beehiveapp.dev as its site. It targets developers running several agent sessions across many repos who want tmux-style isolation.
