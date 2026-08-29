---
name: "Open SWE"
slug: "open-swe"
layout: "agent.njk"
category: "agent"
maker: "langchain-ai"
license: "MIT"
url: "https://github.com/langchain-ai/open-swe"
source_code_url: "https://github.com/langchain-ai/open-swe"
source_available: "True"
platforms:
  - "Web"
  - "Autonomous"
first_released: "2025-05-21"
current_release: "2026-08-19"
stars: null
language: "Python"
homepage: "https://www.langchain.com/blog/open-swe-an-open-source-framework-for-internal-coding-agents"
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: "no"
subagents: "True"
hooks: "True"
plan_mode: "no"
model_providers: "OpenAI, Anthropic"
pricing: "Free / open-source"
install_method: "Local dev setup (backend + dashboard), Docker, or macOS desktop beta"
docs_url: "https://github.com/langchain-ai/open-swe/blob/main/docs/INSTALLATION.md"
plugin_docs_url: "https://github.com/langchain-ai/open-swe/blob/main/docs/CUSTOMIZATION.md"
config_docs_url: "https://github.com/langchain-ai/open-swe/blob/main/docs/INSTALLATION.md"
download_url: "https://github.com/langchain-ai/open-swe"
maintained: "active"
sources:
  - "jqueryscript"
what_makes_it_special: "Open-source replica of the internal coding-agent architecture used by Stripe (Minions), Ramp (Inspect), and Coinbase (Cloudbot); built on LangGraph + Deep Agents; isolated cloud sandboxes, multi-channel invocation (Slack/Linear/GitHub), auto PR creation, server-side MCP for observability with security boundaries."
---

Several frontier companies built internal coding agents — Stripe's Minions, Ramp's Inspect, Coinbase's Cloudbot — but published none of the architecture. Open SWE reconstructs that pattern as an open-source framework on LangGraph and Deep Agents: tasks arrive from Slack, Linear, or GitHub, run in isolated cloud sandboxes (Modal, Daytona, Runloop, E2B, or custom), spawn child agents through the Deep Agents task tool for parallel subtasks, and end in a pull request. Middleware hooks around the agent loop inject mid-run messages, alert Slack when step limits hit, and wrap tool errors, while optional server-side MCP integrations (Datadog, Corridor guardrails) keep observability credentials out of the sandbox. Sandboxes, models, triggers, and system prompts are all customizable per deployment, and per-user model settings live in the web dashboard. Engineering teams self-hosting an internal coding agent in the style of those proprietary systems are the intended users.
