---
name: "NanoClaw"
slug: "nanoclaw"
layout: "agent.njk"
category: "multiplexer"
maker: "nanocoai"
license: "MIT"
url: "https://github.com/nanocoai/nanoclaw"
source_code_url: "https://github.com/nanocoai/nanoclaw"
source_available: "True"
platforms:
  - "CLI"
  - "Web"
  - "Desktop"
first_released: null
current_release: null
stars: "30700"
language: "TypeScript"
homepage: null
mcp_support: "no"
plugin_support: "yes (skills system, customization by forking)"
claude_code_plugin: "no"
subagents: "yes (multi-agent support, per-agent containers)"
hooks: "no"
plan_mode: "no"
model_providers: "Anthropic (Claude Agent SDK), Codex, OpenCode, Ollama"
pricing: "free"
install_method: "git clone, pnpm install"
docs_url: null
maintained: "active"
sources:
  - "user_reported"
what_makes_it_special: "Lightweight, containerized alternative to OpenClaw that runs AI agents (via Claude Agent SDK) in isolated Docker containers and connects them to WhatsApp, Telegram, Slack, Discord, iMessage, Matrix, email, and other messaging apps. Host process routes messages through SQLite queues into per-agent containers with memory, scheduled tasks, and web access. Philosophy of deliberate smallness — small enough to understand, customize by forking with Claude Code."
---

NanoClaw is a self-hosted personal AI assistant harness that trades the weight of OpenClaw for something small enough to read and fork. A host process accepts messages from WhatsApp, Telegram, Slack, Discord, iMessage, Matrix, email, and other channels, routes them through SQLite queues, and hands each to an agent runner — Bun-based, built on the Claude Agent SDK — living inside its own isolated Docker container with its own memory, scheduled tasks, and web access. The container boundary is the point: agents are sandboxed per instance rather than sharing a process, and the harness itself stays out of the agent loop, which belongs to the underlying SDK. Customization is meant to happen by forking the small codebase with Claude Code rather than configuring plugins. The audience is people who want a personal assistant reachable from their existing chat apps without ceding control to a hosted product.
