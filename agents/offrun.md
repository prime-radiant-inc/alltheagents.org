---
name: "Offrun"
slug: "offrun"
layout: "agent.njk"
category: "multiplexer"
maker: "founderly-inc"
license: "Proprietary"
url: "https://offrun.dev"
source_code_url: null
source_available: "False"
homepage: null
docs_url: "https://offrun.dev/docs/"
download_url: "https://offrun.dev/download/"
install_method: "Download the .dmg from offrun.dev/download (macOS 14+, Apple Silicon or Intel; signed and notarized). Windows 10/11 .exe setup and Linux .deb/.AppImage are beta"
platforms:
  - "Desktop"
autonomy_level:
  - "agentic"
specialization: "general"
language: null
first_released: "2026-09-08"
current_release: "2026-11-13"
maintained: "active"
mcp_support: null
plugin_support: null
claude_code_plugin: null
subagents: "True"
hooks: null
plan_mode: null
plugin_docs_url: null
config_docs_url: null
model_providers: "Launches the coding agent CLIs you already have installed — Claude Code (claude), Codex (codex), AGY/Antigravity (agy), Grok Build (grok), and Muse Code (muse) — each signed in with your own account; the agents bring their own providers"
pricing: "free"
stars: null
sources:
  - "hackernews"
last_verified: "2026-11-19"
date_added: "2026-11-19"
what_makes_it_special: "A free desktop workspace built around human attention rather than orchestration: it runs Claude Code, Codex, AGY, Grok Build, and Muse Code side by side in git worktrees, moves a chat to your next account when one hits its usage limit, and adds cross-agent peer review — a second agent reads each turn's diff, lists fixes, and only forwards them when you press Ask agent to fix."
---

Offrun is a desktop app from Founderly, Inc. for developers juggling more than one coding agent, and its stated focus is the human's attention, not agent-to-agent orchestration. A chat is one agent on one task; several run at once, each in its own git worktree so two agents can change one repository without touching each other's files, and the home screen shows who is running, who is waiting on you, and who has an unread answer. Account limits are treated as fleet capacity: add a second Claude or ChatGPT login and a chat moves to it automatically when the first runs out, with the next agent able to pick up a chat when logins are exhausted. Its differentiating feature is peer review — pick a reviewer agent and a second CLI reads what each turn changed, lists what to fix, never edits code itself, and holds its findings until you forward them. The app is free on macOS (signed and notarized), with Windows and Linux builds in beta; it bundles no models and no agents, requiring at least one of the supported CLIs installed and signed in with your own account. Frequent releases (6.6.x as of November 2026) and a public changelog track rapid iteration.
