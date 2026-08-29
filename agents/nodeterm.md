---
name: "nodeterm"
slug: "nodeterm"
layout: "agent.njk"
category: "multiplexer"
maker: "eneskirca"
license: "BUSL-1.1"
url: "https://github.com/eneskirca/nodeterm"
source_code_url: "https://github.com/eneskirca/nodeterm"
source_available: "True"
platforms:
  - "CLI"
  - "Web"
  - "Desktop"
first_released: "2026-06-15"
current_release: "2026-08-20"
stars: "956"
language: "TypeScript"
homepage: "https://nodeterm.dev"
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "yes — subagent cards with live transcripts; agents can spawn teams and verify each other's work via canvas-control CLI"
hooks: "yes — hook-driven status system (pulsing badges, OS notifications, permission prompts, push notifications from SSH hosts)"
plan_mode: "no"
model_providers: null
pricing: "free"
install_method: "binary"
docs_url: "https://nodeterm.dev/docs"
plugin_docs_url: null
config_docs_url: null
download_url: "https://nodeterm.dev"
maintained: "active"
sources:
  - "github_topic2"
what_makes_it_special: "Spatial infinite canvas for terminals and AI coding agents as draggable nodes; dual canvas/kanban view where cards are live running sessions; three surfaces (desktop, browser Server Edition, iOS companion) sharing the same live tmux sessions."
---

nodeterm rethinks agent management as spatial layout rather than stacked terminal tabs, placing terminals, agent sessions, editors, and diff views as nodes on a shared canvas. Every project is tmux-backed, so sessions survive app restarts and machine reboots, and group nodes bind to git worktrees to give each agent its own branch. A hook-driven status system surfaces which sessions need attention through badges, notifications, and permission prompts answered in-node, and agents can drive the canvas itself through a built-in control CLI. The same renderer runs as a desktop app, a self-hosted browser server, and an iOS companion over an encrypted relay. Licensing is BUSL-1.1, converting to MIT four years after each release.
