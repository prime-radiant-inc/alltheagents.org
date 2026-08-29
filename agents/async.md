---
name: "Async"
slug: "async"
layout: "agent.njk"
category: "agent"
maker: "ZYKJShadow"
license: "Apache-2.0"
url: "https://github.com/ZYKJShadow/Async"
source_code_url: "https://github.com/ZYKJShadow/Async"
source_available: "True"
platforms:
  - "IDE"
  - "Desktop"
first_released: "2026-03-30"
current_release: "2026-05-19"
stars: "476"
language: "TypeScript, React, Electron"
homepage: null
mcp_support: "True"
plugin_support: "no (extensibility via MCP servers, local skills, and IM adapters instead)"
claude_code_plugin: null
subagents: "True"
hooks: "no"
plan_mode: "True"
model_providers: "Anthropic, OpenAI, Google Gemini, OpenAI-compatible (Ollama, vLLM, self-hosted)"
pricing: "BYOK"
install_method: "git clone https://github.com/ZYKJShadow/Async.git; cd Async; npm install; npm run desktop"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/ZYKJShadow/Async"
maintained: "active"
sources:
  - "github_deep"
what_makes_it_special: "Agent-first AI-native desktop shell built entirely from scratch (not a VS Code fork) on Electron + React + Monaco, where the agent is the center of gravity with a transparent Think -> Plan -> Execute -> Observe loop. Uniquely includes an IM bot bridge to control the agent workspace externally via Telegram, Slack, Discord, and Feishu. Four Composer modes: Agent, Plan, Ask, Debug."
---

Async (ZYKJShadow/Async) is an agent-first desktop shell built on Electron, React, and Monaco, deliberately not a VS Code fork, so the agent rather than the editor is the primary surface. Its agent loop runs a visible Think-Plan-Execute-Observe cycle with streaming tool parameter cards, approval gates for sensitive operations, and nested sub-agents, backed by Read/Write/Edit/Glob/Grep/Shell tools and MCP server support. Four Composer modes (Agent, Plan, Ask, Debug) control autonomy, and a Team mode coordinates Lead, specialist, and reviewer agents. Multi-model support spans Anthropic, OpenAI, Gemini, and OpenAI-compatible endpoints (Ollama, vLLM) under a BYOK model, with Telegram, Slack, Discord, and Feishu adapters reusing the same agent runtime from chat apps. It is Apache-2.0, actively developed, and aimed at developers who want a local-first, hackable IDE where the agent is the primary interface.
