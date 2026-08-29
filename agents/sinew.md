---
name: "sinew"
slug: "sinew"
layout: "agent.njk"
category: "agent"
maker: "Paseru"
license: "MIT"
url: "https://github.com/Paseru/sinew"
source_code_url: "https://github.com/Paseru/sinew"
source_available: "True"
platforms:
  - "IDE"
first_released: "2026-05-13"
current_release: "2026-07-29"
stars: "65"
language: "Rust, TypeScript"
homepage: "https://sinew-ide.com/"
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: "no"
subagents: "True"
hooks: null
plan_mode: "True"
model_providers: "Anthropic, OpenAI, Google, Kimi, OpenRouter"
pricing: "Free / open source; uses existing subscriptions via OAuth or API keys/OpenRouter"
install_method: "Download pre-built binaries from GitHub Releases (.dmg/.msi/.AppImage/.deb) or build from source (npm install + npm run tauri build)"
docs_url: "https://sinew-ide.com"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/Paseru/sinew/releases/latest"
maintained: "active"
sources:
  - "github_topic"
what_makes_it_special: "Desktop AI coding harness (Tauri 2) where every tool is toggleable, every description editable, every provider pluggable; agent only sees the surface area you keep; Skills system compatible with Claude Agent Skills convention"
---

Sinew starts from the observation that most harnesses fix the toolset and the prompt, then fights the model's failures; it instead exposes the harness itself for editing — toggle tools, rewrite their descriptions, swap providers per mode, per sub-agent, or per teammate. Three modes cover normal work (Act), hours-long autonomous runs (Goal), and interactive plan production (Plan), with a peer-to-peer swarm of two to eight agents sharing a task board and messaging. Skills use SKILL.md files compatible with Claude Agent Skills, MCP servers plug in via settings, and compaction plus clickable rollback checkpoints manage long sessions. It is a Tauri 2 desktop app in Rust and React, MIT-licensed, distributed through GitHub releases with self-update. The audience is developers who want Claude Code-class capability with total control over what the model is allowed to see and touch.
