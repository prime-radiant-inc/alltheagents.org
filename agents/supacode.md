---
name: "supacode"
slug: "supacode"
layout: "agent.njk"
category: "multiplexer"
maker: "supabitapp"
license: "FSL-1.1-ALv2 (Functional Source License, converts to Apache 2.0 after 2 years)"
url: "https://github.com/supabitapp/supacode"
source_code_url: "https://github.com/supabitapp/supacode"
source_available: "Source-available (no OSS license)"
platforms:
  - "Desktop"
first_released: "2026-01-21"
current_release: "2026-08-19"
stars: "2290"
language: "Swift"
homepage: "https://supacode.sh"
mcp_support: null
plugin_support: null
claude_code_plugin: "no"
subagents: null
hooks: "yes"
plan_mode: null
model_providers: null
pricing: "open-source"
install_method: "binary"
docs_url: "https://supacode.sh"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "brad"
what_makes_it_special: "Native macOS command center for running coding agents in parallel with a worktree-first workflow (each task gets its own git worktree and real terminal via libghostty), background session persistence that survives app quits (via zmx), and live coding agent presence detection."
---

supacode is built for developers who run several agents concurrently and lose track of which session is working on what. Every task gets its own git worktree and a real terminal rendered through libghostty, with the sidebar tracking branch, file, and PR state per worktree alongside pinning, archiving, and auto-delete. Sessions persist in the background via zmx so work survives app restarts and SSH interruptions, and agent presence badges (busy, awaiting input, idle) with notifications make parallel agents legible at a glance. Remote SSH repositories are supported over a single multiplexed connection, and a CLI plus supacode:// deeplinks allow scripting. It is developed by Supabit under a Functional Source License that converts to Apache 2.0 after two years.
