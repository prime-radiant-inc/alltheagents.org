---
name: "Episko"
slug: "episko"
layout: "agent.njk"
category: "multiplexer"
maker: "respeak-io"
license: "MIT"
url: "https://episko.dev/"
source_code_url: "https://github.com/respeak-io/episko"
source_available: "True"
platforms:
  - "Desktop"
first_released: "2026-07-16"
current_release: "2026-08-28"
stars: 20
language: "TypeScript"
homepage: "https://episko.dev/"
mcp_support: null
plugin_support: null
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "delegates to Claude Code"
pricing: "free"
install_method: "Download the macOS .dmg (Apple silicon) or Windows .msi from episko.dev; requires Claude Code on PATH"
docs_url: "https://episko.dev/"
plugin_docs_url: null
config_docs_url: null
download_url: "https://episko.dev/"
maintained: "active"
sources:
  - "hackernews"
what_makes_it_special: "A cockpit that gives every Claude Code session its own live terminal gathered into one dashboard, with per-session model, context usage, cost, tokens, and the exact tool currently running, permission prompts surfaced with risk indication, and Claude usage-limit tracking with pace warnings — built on Tauri, MIT, no accounts or telemetry."
---

Episko — from the Greek episkopos, the one who watches over — is a desktop cockpit for herding Claude Code agents. Each Claude Code session gets its own live terminal (or connects to Ghostty, Terminal, or iTerm), and all of them gather into a single dashboard where you can see model, context usage, cost, token counts, and the exact tool currently running per session, with urgency-colored states and cmd+K search to jump to whatever needs attention. Permission prompts surface as allow/deny cards with risk indication, agents launch on repos, branches, or git worktrees with GitHub issue integration that creates a worktree and writes a claim so teammates' agents don't duplicate work, and local analytics track spend, tokens by model, and cost per session. It reuses Claude's --session-id so restarts rebuild panes with scrollback intact, and it tracks the 5-hour and weekly usage windows with pace warnings. Built by Respeak in Karlsruhe on Tauri, it is free and open source with no accounts and no telemetry.
