---
name: "Grok CLI"
slug: "grok-cli"
layout: "agent.njk"
category: "agent"
maker: "superagent-ai"
license: "MIT"
url: "https://github.com/superagent-ai/grok-cli"
source_code_url: "https://github.com/superagent-ai/grok-cli"
source_available: "True"
platforms:
  - "CLI"
first_released: "2025-07-14"
current_release: "2026-07-06"
stars: null
language: "TypeScript"
homepage: null
mcp_support: "True"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "True"
hooks: "True"
plan_mode: "no"
model_providers: "xAI Grok API exclusively"
pricing: "open-source"
install_method: "curl -fsSL https://raw.githubusercontent.com/superagent-ai/grok-cli/main/install.sh | bash"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/superagent-ai/grok-cli/releases"
maintained: "active"
sources:
  - "jqueryscript"
  - "brad"
  - "ishandutta"
what_makes_it_special: "Deeply integrated with Grok API including X (Twitter) live search and web search, built-in computer sub-agent for host desktop automation (macOS), Telegram remote control with voice transcription, media generation (image/video), microVM sandboxing via Shuru, scheduling support, and OpenTUI React-based terminal UI."
---

grok-cli is a community terminal coding agent built by Superagent on xAI's Grok API, using TypeScript, Bun, and OpenTUI for its interface. Beyond standard file and shell tools, it integrates Grok-specific capabilities: live search over X posts and the web, media generation, and a computer sub-agent that drives macOS applications through accessibility snapshots and scripted actions. Sessions persist and can be driven remotely through a paired Telegram bot, including voice notes transcribed via Grok's speech-to-text API, and a daemon supports scheduled tasks. MCP servers, hooks, AGENTS.md instructions, and an optional microVM sandbox round out the toolset, and a /verify command runs apps in isolation for verification. It targets developers already using Grok models who want those unique data sources and remote-control paths inside their agent loop.
