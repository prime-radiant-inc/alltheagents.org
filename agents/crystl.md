---
name: "crystl"
slug: "crystl"
layout: "agent.njk"
category: "multiplexer"
maker: "crystl"
license: null
url: "https://crystl.dev"
source_code_url: null
source_available: "False"
platforms: []
first_released: null
current_release: null
stars: null
language: "Swift"
homepage: "https://crystl.dev"
mcp_support: "True"
plugin_support: null
claude_code_plugin: "False"
subagents: "True"
hooks: "True"
plan_mode: null
model_providers: "Claude Code, Codex, Antigravity CLI, Kimi Code, opencode, aider, goose, Ollama"
pricing: "Free plan; Guild plan $170/year"
install_method: "Native macOS app (direct download or site signup); iOS companion on App Store"
docs_url: "https://crystl.dev/docs/"
plugin_docs_url: null
config_docs_url: null
download_url: "https://crystl.dev/login/?signup=1"
maintained: "active"
sources:
  - "toolify"
what_makes_it_special: "Multitasking terminal for macOS that orchestrates multiple AI CLI agents in parallel with per-agent git worktree isolation. cavrn engine captures terminal output as structured agent-readable metadata (Metal GPU-accelerated). crystl quest assembles role-played 'adventure party' of specialized agents collaborating in shared chat. Action panels for approvals/notifications. iPhone app for remote monitoring. Hero shards summon specialized solo agents. Agent-callable CLI."
---

Crystl is a native macOS terminal built around the reality that developers now run several AI CLI agents at once. Each 'shard' runs in its own git worktree so parallel agents never conflict on one checkout, and the app adds scheduling, auto-resume, and persistent searchable history across sessions. An orchestrator agent can be appointed to manage subagents or run role-played 'parties' of specialists, and the built-in crystl CLI exposes spawning, output reading, and approval handling to agents themselves. The underlying agents are external CLIs the user already has (Claude Code, Codex, Antigravity CLI, Kimi Code, opencode, aider, goose), which places crystl in the multiplexer role; the free tier covers core features and a $170/year Guild plan adds scheduling, formations, and CLI orchestration.
