---
name: "Nanocoder"
slug: "nanocoder"
layout: "agent.njk"
category: "agent"
maker: "Nano-Collective"
license: "Source Available"
url: "https://github.com/Nano-Collective/nanocoder"
source_code_url: "https://github.com/Nano-Collective/nanocoder"
source_available: "True"
platforms:
  - "CLI"
first_released: "2025-07-30"
current_release: "2026-08-20"
stars: null
language: "TypeScript"
homepage: "https://docs.nanocollective.org/nanocoder"
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: "False"
subagents: "True"
hooks: "True"
plan_mode: "True"
model_providers: "Ollama,OpenAI,OpenRouter,Anthropic,Google"
pricing: "Free, no paid tiers"
install_method: "npm install -g @nanocollective/nanocoder"
docs_url: "https://docs.nanocollective.org/nanocoder/docs"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/Nano-Collective/nanocoder/releases"
maintained: "active"
sources:
  - "jqueryscript"
  - "brad"
  - "ishandutta"
what_makes_it_special: "Open-source terminal agentic coding assistant; bring-your-own-model, no telemetry, skills system (commands/subagents/tools/event triggers), checkpointing, and plan/auto-accept/yolo dev modes."
---

Nanocoder targets developers who want Claude Code-style terminal assistance without vendor lock-in or telemetry. It boots into one of four development modes (normal, auto-accept, yolo, plan) and combines slash commands, a per-project daemon, checkpointing, and MCP servers configured per project. The skills system unifies commands, subagents, tools, and event triggers, and a non-interactive run mode supports scripting. Distribution is npm, Homebrew, or Nix Flakes, and the project is governed as a community collective under the Nano Collective umbrella with shared conventions across its projects.
