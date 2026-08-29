---
name: "Claurst"
slug: "claurst"
layout: "agent.njk"
category: "agent"
maker: "Kuberwastaken"
license: "GPL-3.0"
url: "https://github.com/Kuberwastaken/claurst"
source_code_url: "https://github.com/Kuberwastaken/claurst"
source_available: "True"
platforms: []
first_released: "2026-03-31"
current_release: "2026-07-31"
stars: "10250"
language: "Rust"
homepage: "https://claurst.kuber.studio/"
mcp_support: "no"
plugin_support: "yes"
claude_code_plugin: "no"
subagents: "yes"
hooks: "no"
plan_mode: "yes"
model_providers: "Anthropic, Google Gemini"
pricing: "open-source"
install_method: "npm"
docs_url: "https://claurst.kuber.studio/docs"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/Kuberwastaken/claurst/releases"
maintained: "active"
sources:
  - "brad"
  - "ishandutta"
what_makes_it_special: "Clean-room Rust reimplementation of Claude Code as a terminal coding agent (TUI pair programmer). Multi-provider routing with no telemetry/tracking. Agent Client Protocol (ACP) support for editor integration (Zed, Neovim, JetBrains). Ultracode mode runs a plan -> delegate -> integrate -> verify multi-agent workflow. Unique features: /share (GitHub Gist sharing), /goal for sustained multi-turn objectives, chat forking, memory consolidation."
---

Claurst demonstrates that a production-grade agent harness can be specified behaviorally and rebuilt without copying code: the repository contains no proprietary source, only spec files derived from analysis and an independent Rust implementation. The result is a GPL-3.0 terminal agent with tool-call streaming, approval flows, subagent and swarm spawning, background tasks, and editor integration through ACP so Zed, Neovim, or JetBrains can drive it. An experimental Free Mode lowers the entry cost, and /share publishes sessions as GitHub Gists. With over ten thousand stars and active releases, it is one of the most successful Claude Code reimplementations in this census.
