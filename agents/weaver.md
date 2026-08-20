---
name: "Weaver"
slug: "weaver"
layout: "agent.njk"
category: "agent"
maker: "sean35mm"
license: "MIT"
url: "https://github.com/sean35mm/weaver"
source_code_url: "https://github.com/sean35mm/weaver"
source_available: True
platforms: []
first_released: "2026-06-01"
current_release: "2026-07-24"
stars: "2"
language: "TypeScript"
homepage: "https://sean35mm.github.io/weaver/"
mcp_support: False
plugin_support: False
claude_code_plugin: False
subagents: False
hooks: True
plan_mode: False
model_providers: "Claude Code, Codex, OpenCode, Pi (any agent that can run shell commands)"
pricing: "Free / open-source (MIT)"
install_method: "curl -fsSL https://raw.githubusercontent.com/sean35mm/weaver/main/install.sh | sh (installs binary to ~/.local/bin/weaver); then run weaver init (project or global). macOS/Linux arm64/x64; Windows via WSL2."
docs_url: "https://sean35mm.github.io/weaver/"
plugin_docs_url: null
config_docs_url: null
download_url: "https://raw.githubusercontent.com/sean35mm/weaver/main/install.sh"
maintained: "active"
sources:
  - "brad"
what_makes_it_special: "Local-only, serverless coordination layer for multiple AI coding agents in the same repo. Provides cross-agent presence, advisory file claims, durable notes that survive context compaction, recent activity tracking, and live views — all via a small CLI over local SQLite files (~/.weaver/). No telemetry, no account, no network calls. Git remains source of truth; claims are advisory, never blocking. Explicitly not an MCP server."
---

Local-only, serverless coordination layer for multiple AI coding agents in the same repo. Provides cross-agent presence, advisory file claims, durable notes that survive context compaction, recent activity tracking, and live views — all via a small CLI over local SQLite files (~/.weaver/). No telemetry, no account, no network calls. Git remains source of truth; claims are advisory, never blocking. Explicitly not an MCP server.
