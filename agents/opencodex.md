---
name: "OpenCodex"
slug: "opencodex"
layout: "agent.njk"
category: "other"
maker: "lidge-jun"
license: "MIT"
url: "https://github.com/lidge-jun/opencodex"
source_code_url: "https://github.com/lidge-jun/opencodex"
source_available: "True"
platforms:
  - "CLI"
  - "IDE"
first_released: "2026-06-18"
current_release: "2026-08-20"
stars: "11304"
language: "TypeScript"
homepage: "https://opencodex.me/"
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "yes"
hooks: "no"
plan_mode: "no"
model_providers: "OpenAI, Anthropic, Google Gemini, xAI, Kimi, Azure OpenAI, Ollama, DeepSeek, Groq, OpenRouter, Together, Fireworks, Cerebras, Mistral, HuggingFace, NVIDIA NIM, MiniMax, Qwen Cloud, SiliconFlow, 40+ providers"
pricing: "open-source"
install_method: "npm"
docs_url: "https://opencodex.me/"
plugin_docs_url: null
config_docs_url: "https://opencodex.me/docs"
download_url: "https://www.npmjs.com/package/@bitkyc08/opencodex"
maintained: "active"
sources:
  - "brad"
what_makes_it_special: "Universal local proxy that translates OpenAI Codex's Responses API into any LLM provider's format (streaming, tool calls, reasoning tokens, images). Unifies four AI coding tools (Codex CLI/App/SDK, Claude Code, Claude Desktop, Grok Build) with any model while preserving native UIs. Combos feature for virtual model IDs with failover or weighted round-robin. ChatGPT account pooling with quota-aware routing and thread affinity. OAuth login to skip API keys. Web search & vision sidecars for non-OpenAI models."
---

Codex speaks OpenAI's Responses API, Claude Code speaks Anthropic's, and Grok Build has its own protocol, so mixing providers across those tools means juggling keys, endpoints, and incompatible streaming formats. OpenCodex runs a local proxy on localhost:10100 that speaks the Responses API on one side and translates to Claude, Gemini, Grok, GLM, DeepSeek, Kimi, Qwen, Ollama, and other OpenAI-compatible endpoints on the other, handling streaming, tool calls, reasoning tokens, and images in both directions. ChatGPT account pooling adds quota-aware routing across accounts, and model combos provide failover or round-robin across providers; a web dashboard exposes traffic and configuration. Install is npm -g with an ocx CLI that can register itself as a background service on launchd, systemd, or Task Scheduler. The maintainers explicitly warn it is unaffiliated with OpenAI and Anthropic and that some providers may suspend accounts routed through third-party proxies, so it targets users who accept that risk.
