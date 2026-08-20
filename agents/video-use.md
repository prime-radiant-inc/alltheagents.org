---
name: "video-use"
slug: "video-use"
layout: "agent.njk"
category: "agent"
maker: "browser-use"
license: "MIT"
url: "https://github.com/browser-use/video-use"
source_code_url: "https://github.com/browser-use/video-use"
source_available: "Yes"
platforms:
  - "IDE"
first_released: "2026-04-12"
current_release: "2026-07-01"
stars: "21136"
language: "Python"
homepage: null
mcp_support: "no"
plugin_support: "yes (skills-based; symlinks into agent skill directories)"
claude_code_plugin: "yes (via ~/.claude/skills/video-use)"
subagents: "yes (spawns parallel sub-agents for animations)"
hooks: "no"
plan_mode: "yes (asks for strategy approval before executing)"
model_providers: "Claude Code, Codex, Hermes, Openclaw, any shell-access agent"
pricing: "open-source (MIT); requires ElevenLabs API key (BYOK)"
install_method: "pip"
docs_url: "https://github.com/browser-use/video-use/blob/main/README.md"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "github_topic"
what_makes_it_special: "Enables coding agents to edit raw video footage by reading word-level audio transcripts and on-demand visual composites instead of processing every frame, achieving precise word-boundary cuts with minimal token usage and a self-evaluation loop at every cut boundary."
---

Enables coding agents to edit raw video footage by reading word-level audio transcripts and on-demand visual composites instead of processing every frame, achieving precise word-boundary cuts with minimal token usage and a self-evaluation loop at every cut boundary.
