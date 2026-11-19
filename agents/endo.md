---
name: "Endo"
slug: "endo"
layout: "agent.njk"
category: "multiplexer"
maker: "longsurf-ai"
license: "MIT"
url: "https://github.com/longsurf-ai/endo"
source_code_url: "https://github.com/longsurf-ai/endo"
source_available: "True"
homepage: "https://longsurf.ai"
docs_url: "https://github.com/longsurf-ai/endo/blob/main/README.md"
download_url: "https://downloads.longsurf.ai/endo/darwin/arm64/Endo.dmg"
install_method: "Download Endo.dmg for macOS (Apple Silicon) from downloads.longsurf.ai, or build from source with Node.js 24, Bun 1.4.2 and Just (just install, just desktop)"
platforms:
  - "Desktop"
autonomy_level:
  - "agentic"
  - "autonomous-background"
specialization: "general"
language: "TypeScript"
first_released: "2026-10-14"
current_release: "2026-10-16"
maintained: "active"
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: null
subagents: "True"
hooks: "True"
plan_mode: "False"
plugin_docs_url: "https://github.com/longsurf-ai/endo/blob/main/docs/architecture/agent-plugins.md"
config_docs_url: null
model_providers: "agents bring their own subscriptions and logins (Codex, Claude Code, Antigravity, Grok, OpenCode); OpenCode's native provider config also connects compatible endpoints"
pricing: "free"
stars: "102"
sources:
  - "hackernews"
last_verified: "2026-11-19"
date_added: "2026-11-19"
what_makes_it_special: "A Higher Order Harness that takes agents themselves as building blocks — switch between Codex, Claude Code, Antigravity, Grok and OpenCode mid-thread with full history carried over, and compose them into workflows like best-of-n that fan out across vendors on the subscriptions you already have."
---

Endo comes from longsurf.ai — the team behind the OpenChart market tool, whose core this project grew out of — and its name from endomorphism: it takes agents and gives you back an agent. A harness runs one agent, sending prompts, running tools and keeping history; Endo is a Higher Order Harness that composes any of them. In one session you can switch between Codex, Claude Code, Antigravity, Grok and OpenCode mid-thread — each agent picks up the full history — or select any part of an answer and Dig In, opening a focused side conversation while the main thread stays clean. Across sessions, workflows fan work out: a workflow is a TypeScript file in your workspace where agent() calls any model from any provider, parallel() fans calls out and a session ID continues an earlier agent's conversation, with /best-of-n, /multi-turn-debate, /thesis-killer and /hypothesis-race shipping as built-ins, and schedules run any prompt later on a cron or once. Endo drives those harnesses natively through their own CLIs on the accounts you already have, streaming every provider through one protocol so answers, tool calls, permission prompts and history behave the same whichever model you pick, and it adds its own application tools (schedules, resources, transcript search) to the mix. The Mac app is the primary distribution, sessions persist across restarts so any agent can continue where another left off, and the project is at 0.1.x with breaking changes expected. It suits developers holding multiple vendor subscriptions who want one interface and composability instead of five separate chats.
