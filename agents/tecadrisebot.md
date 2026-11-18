---
name: "TecAdRiseBot"
slug: "tecadrisebot"
layout: "agent.njk"
category: "agent"
maker: "tecadrise-ai"
license: "MIT"
url: "https://tecadrise.ai/products/tecadrisebot"
source_code_url: "https://github.com/tecadrise-ai/TecAdRiseBot"
source_available: "True"
homepage: null
docs_url: "https://github.com/tecadrise-ai/TecAdRiseBot#readme"
download_url: "https://tecadrise.ai/downloads/tecadrisebot/TecAdRiseBot-Setup-win64.exe"
install_method: "Download the Windows installer and run it; from source: git clone, npm install, npm run dev"
platforms:
  - "Desktop"
  - "Autonomous"
autonomy_level:
  - "agentic"
  - "autonomous-background"
specialization: "general"
language: "TypeScript"
first_released: "2026-09-19"
current_release: "2026-11-06"
maintained: "active"
mcp_support: "True"
plugin_support: "False"
claude_code_plugin: null
subagents: "True"
hooks: "False"
plan_mode: "False"
plugin_docs_url: null
config_docs_url: null
model_providers: "Cursor, or BYOK with any OpenAI-compatible key (Hugging Face, OpenRouter, OpenAI, Claude, NVIDIA NIM)"
pricing: "free"
stars: "0"
sources:
  - "github-issue"
last_verified: "2026-11-18"
date_added: "2026-11-18"
what_makes_it_special: "A free, MIT-licensed Windows desktop app that runs named local agents over the Cursor SDK or any OpenAI-compatible BYOK key. Each agent gets its own workspace, MCP servers, and scheduled routines, and a localhost-only control plane exposes the agents to external automation."
---

TecAdRiseBot is a Windows Electron desktop app for running named agents locally, positioned by its maker as a free open-source alternative to xAI's Grok Bot. Each agent has its own sticky instructions (a "Soul"), model, and workspace, and the app assembles every turn itself — inlining SYSTEM.md and MEMORY.md, binding global and per-agent MCP servers, and passing its own host tools such as list_peers and message_agent — before running the turn through the embedded Cursor TypeScript SDK or its own tool loop against an OpenAI-compatible BYOK provider, with API keys held in Electron safeStorage rather than the chat database. On top of the chat surface it adds attachments, a routine scheduler (loop, interval, daily, weekly, once, or cron), inter-agent messages in which a running agent asks an idle peer and waits for its reply, and step workflows where a Runner agent executes steps while an Owner agent reviews and fixes. An unauthenticated localhost control plane on 127.0.0.1:8787 lets external scripts or IDE agents drive and reconfigure the running agents. It is aimed at people who want a self-hosted multi-agent setup on Windows.
