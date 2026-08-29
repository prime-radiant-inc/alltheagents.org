---
name: "Devx"
slug: "termux-devx"
layout: "agent.njk"
category: "agent"
maker: "apvcode"
license: "MIT"
url: "https://github.com/apvcode/Termux-Dev"
source_code_url: "https://github.com/apvcode/Termux-Dev"
source_available: "True"
platforms:
  - "CLI"
first_released: "2026-08-24"
current_release: "2026-08-28"
stars: 14
language: "TypeScript"
homepage: null
mcp_support: "yes"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "yes"
model_providers: "OpenRouter, Google Gemini, DeepSeek, Groq, Mistral, OpenAI, Anthropic, Alibaba, Ollama, LM Studio"
pricing: "free"
install_method: "npm install -g termux-dev (Node.js >= 20)"
docs_url: "https://github.com/apvcode/Termux-Dev/blob/main/README.md"
plugin_docs_url: null
config_docs_url: null
download_url: "https://www.npmjs.com/package/termux-dev"
maintained: "active"
sources:
  - "hackernews"
what_makes_it_special: "A coding agent built Android-first for Termux: PLAN mode asks requirements questions before any edits, AGENT mode runs autonomously, and a built-in live web server previews web apps on the phone via termux-open-url. Self-healing diagnostics auto-detect and fix TypeScript, JavaScript, Python, and Rust errors before finishing a turn."
---

Devx (npm package termux-dev) is a terminal AI coding agent whose primary target is Android via Termux, though it also runs on Windows, macOS, and Linux. Its dual-mode architecture separates an interactive PLAN-mode architect that asks requirements questions without touching code from an AGENT mode that performs autonomous file edits, terminal commands, and package installs, with Tab toggling between them and one-click plan approval. It supports multimodal vision via pasted screenshots, snapshot rollback, git commits with AI-generated semantic messages, a per-project memory bank, MCP server support, and a headless one-shot mode for CI/CD and Termux:Widget. The live web server on port 3000 auto-opens in the Android browser, making it practical to build and preview web apps entirely on a phone.
