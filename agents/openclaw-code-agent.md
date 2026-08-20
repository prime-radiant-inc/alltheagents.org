---
name: "openclaw-code-agent"
slug: "openclaw-code-agent"
layout: "agent.njk"
category: "agent"
maker: "goldmar"
license: "MIT"
url: "https://github.com/goldmar/openclaw-code-agent"
source_code_url: "https://github.com/goldmar/openclaw-code-agent"
source_available: True
platforms: []
first_released: "2026-02-21"
current_release: "2026-08-19"
stars: "44"
language: "TypeScript (with shell scripts)"
homepage: "https://www.npmjs.com/package/openclaw-code-agent"
mcp_support: null
plugin_support: True
claude_code_plugin: null
subagents: True
hooks: True
plan_mode: True
model_providers: "Claude Code, Codex, OpenCode"
pricing: null
install_method: "openclaw plugins install openclaw-code-agent, then openclaw plugins enable openclaw-code-agent"
docs_url: "https://github.com/goldmar/openclaw-code-agent/blob/main/docs/REFERENCE.md"
plugin_docs_url: null
config_docs_url: null
download_url: "https://www.npmjs.com/package/openclaw-code-agent"
maintained: "active"
sources:
  - "github_topic3"
what_makes_it_special: "Stateful coding agent plugin for OpenClaw that runs Claude Code, Codex, and experimental OpenCode as managed background coding sessions launched from Telegram, Discord, or other OpenClaw-supported chat channels. Adds plan approval, session lifecycle, wake routing, worktree isolation, merge/PR follow-through, and explicit goal loops. Default launch mode is 'plan' with delegate plan review. Modes: plan, ask, off, manual, auto-merge, auto-pr. Session persistence/recovery across restarts, routed outcome summaries back to originating chat threads."
---

Stateful coding agent plugin for OpenClaw that runs Claude Code, Codex, and experimental OpenCode as managed background coding sessions launched from Telegram, Discord, or other OpenClaw-supported chat channels. Adds plan approval, session lifecycle, wake routing, worktree isolation, merge/PR follow-through, and explicit goal loops. Default launch mode is 'plan' with delegate plan review. Modes: plan, ask, off, manual, auto-merge, auto-pr. Session persistence/recovery across restarts, routed outcome summaries back to originating chat threads.
