---
name: "Rikki Coding Agent"
slug: "rikki-coding-agent"
layout: "agent.njk"
category: "agent"
maker: "Creeper5261"
license: "MIT"
url: "https://plugins.jetbrains.com/plugin/30315-rikki-coding-agent"
source_code_url: null
source_available: null
platforms:
  - "IDE"
first_released: "2026-03-05"
current_release: null
stars: null
language: null
homepage: null
mcp_support: null
plugin_support: null
claude_code_plugin: null
subagents: null
hooks: null
plan_mode: null
model_providers: "OpenAI, Anthropic, Google Gemini, Ollama, DeepSeek, Moonshot Kimi"
pricing: "free"
install_method: "Install from the JetBrains Marketplace"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://plugins.jetbrains.com/plugin/30315-rikki-coding-agent"
maintained: "active"
sources:
  - "gap-2026-08-20"
what_makes_it_special: "Lightweight AI coding assistant connecting directly to LLM APIs"
---

Most JetBrains AI plugins route through a vendor cloud; Rikki connects the IDE straight to whichever LLM API the developer configures, which suits users of self-hosted or regional models such as DeepSeek or Ollama. The chat agent works over the project — reading files, editing code, and executing terminal and Git commands, with high-risk actions gated behind approval. Inline completion runs in fill-in-the-middle mode for providers that support it and falls back to chat-format completion for those that do not. The plugin is free, MIT-licensed, and young, published in early 2026 with a few hundred downloads, so its audience is so far individual developers comfortable with early-stage tooling.
