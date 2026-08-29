---
name: "damocles"
slug: "damocles"
layout: "agent.njk"
category: "agent"
maker: "AizenvoltPrime"
license: "MIT"
url: "https://github.com/AizenvoltPrime/damocles"
source_code_url: "https://github.com/AizenvoltPrime/damocles"
source_available: "True"
platforms:
  - "IDE"
first_released: "2025-12-23"
current_release: "2026-08-17"
stars: "72"
language: "TypeScript"
homepage: "https://github.com/AizenvoltPrime/damocles"
mcp_support: "True"
plugin_support: null
claude_code_plugin: "False"
subagents: "True"
hooks: "True"
plan_mode: "True"
model_providers: "Anthropic, OpenAI, StepFun, DeepSeek, OpenRouter, Google Gemini"
pricing: "Free and open-source (BYO API keys or existing subscriptions)"
install_method: "Clone repo, npm install, npm run build, press F5 in VS Code; or package as .vsix and install via Extensions menu"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "github_topic4"
what_makes_it_special: "VS Code extension embedding an AI coding agent powered by the Pi agent runtime, with deep editor integration including inline diff previews, subagent visualization, persistent SQLite-backed memory, collaborative multi-agent teams, a workspace knowledge graph (Compass), integrated stealth browser automation, and hands-free voice input (Jarvis mode)."
---

Damocles embeds a full coding agent into VS Code by building on the Pi agent runtime, so the loop, tools, and subagent machinery come from Pi while the extension adds deep editor integration: inline diff previews, checkpointed rewinds and forking, and real-time subagent visualization. Its model providers include Claude, GPT/Codex, StepFun, and DeepSeek, and its MCP client merges servers from Claude Code, Codex, and its own config files with OAuth and auto-reconnect. Beyond single-agent use it supports nested subagents with mid-task steering and optional 2–5 agent collaborative teams with scratchpads and verification ledgers, plus extras such as a knowledge graph over the codebase, browser automation, and voice control. It is a solo-maintained MIT project aimed at developers who want Claude Code-class behavior inside the editor with local, inspectable state.
