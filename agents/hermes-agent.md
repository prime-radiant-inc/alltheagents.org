---
name: "Hermes Agent"
slug: "hermes-agent"
layout: "agent.njk"
category: "agent"
maker: "NousResearch"
license: "MIT"
url: "https://hermes-agent.nousresearch.com/"
source_code_url: "https://github.com/NousResearch/hermes-agent"
source_available: "True"
homepage: null
docs_url: "https://hermes-agent.nousresearch.com/docs"
download_url: "https://hermes-agent.nousresearch.com/#downloads"
install_method: "curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash"
platforms:
  - "CLI"
  - "Web"
  - "Desktop"
  - "Autonomous"
autonomy_level:
  - "agentic"
  - "autonomous-background"
specialization: "general"
language: "Python"
first_released: "2025-07-22"
current_release: "2026-11-16"
maintained: "active"
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: null
subagents: "True"
hooks: "True"
plan_mode: "True"
plugin_docs_url: "https://hermes-agent.nousresearch.com/docs/user-guide/features/plugins"
config_docs_url: "https://hermes-agent.nousresearch.com/docs/user-guide/configuration"
model_providers: "Nous Portal, OpenRouter, OpenAI, Anthropic, Google, DeepSeek, xAI, Ollama, LM Studio, or any OpenAI-compatible endpoint (40+ providers listed)"
pricing: "freemium"
stars: "264480"
sources:
  - "github-issue"
last_verified: "2026-11-18"
date_added: "2026-11-18"
what_makes_it_special: "A self-improving personal agent whose built-in learning loop turns experience into skills it writes and refines itself, with persistent memory and user modeling across sessions. One instance stays reachable from a terminal, a desktop app, and 21+ messaging platforms while it runs on anything from a $5 VPS to a serverless sandbox."
---

Nous Research, the lab behind the open Hermes model family, calls this the most widely used open source agent harness in the world, and positions it as a persistent companion rather than a per-task tool: deployed on a server, it keeps working after you close the terminal. It is a Python harness that owns its own prompt-model-tool loop, with built-in read_file, patch, and terminal tools it can point at a local shell or an isolated backend such as Docker, SSH, Modal, Daytona, or a Vercel sandbox, and a gateway process that exposes the same agent to Telegram, Discord, Slack, WhatsApp, and Signal. A cron scheduler and session heartbeats run reports and automations unattended, isolated subagents parallelize workstreams, and MCP servers plus a Python plugin system extend the toolset. It is aimed at developers who want one always-on agent for coding, research, and automation on their own infrastructure, using whatever model provider they choose; Nous sells Portal subscriptions and cloud hosting for those who would rather not collect API keys themselves.
