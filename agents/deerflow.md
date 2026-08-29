---
name: "DeerFlow"
slug: "deerflow"
layout: "agent.njk"
category: "agent"
maker: "bytedance"
license: "MIT"
url: "https://github.com/bytedance/deer-flow"
source_code_url: "https://github.com/bytedance/deer-flow"
source_available: "Yes"
platforms:
  - "CLI"
  - "IDE"
  - "Web"
  - "Autonomous"
first_released: "2025-05-07"
current_release: "2026-08-20"
stars: "80339"
language: "Python"
homepage: "https://deerflow.tech"
mcp_support: "yes (HTTP/SSE with OAuth, stdio with per-tool timeouts)"
plugin_support: "yes"
claude_code_plugin: "yes"
subagents: "yes"
hooks: "yes"
plan_mode: "yes"
model_providers: "OpenAI, OpenRouter, vLLM, Claude Code (OAuth), Codex CLI, MiniMax Code (ACP), OpenAI-compatible"
pricing: "open-source"
install_method: "git clone + make setup, docker"
docs_url: "https://deerflow.tech"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/bytedance/deer-flow"
maintained: "active"
sources:
  - "brad"
  - "caramaschi"
what_makes_it_special: "A batteries-included 'super agent harness' orchestrating sub-agents, long-term memory, sandbox-aware execution, and extensible skills; ships with built-in skills for research, slides, web pages, and image/video generation with progressive skill loading."
---

DeerFlow started as ByteDance's deep-research framework and was rebuilt for 2.0 as a general agent harness: the lead agent decomposes work, delegates to subagents only when parallelism or context isolation pays, and verifies their structured results. Skills provide progressive-loading capabilities (research, slides, web pages), memory persists across sessions, and sandbox modes range from local processes to Docker, Kubernetes, and E2B. An extension API exposes task-lifecycle hooks and middleware, and the gateway reaches IM channels from Telegram to DingTalk. Teams use it as a self-hosted agent platform where they control models — Doubao-Seed-2.0-Code, DeepSeek, Kimi — and data.
