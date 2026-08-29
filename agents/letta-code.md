---
name: "Letta Code"
slug: "letta-code"
layout: "agent.njk"
category: "agent"
maker: "letta-ai"
license: "Apache-2.0"
url: "https://github.com/letta-ai/letta-code"
source_code_url: "https://github.com/letta-ai/letta-code"
source_available: "True"
platforms:
  - "CLI"
first_released: "2025-10-25"
current_release: "2026-08-20"
stars: null
language: "TypeScript"
homepage: "https://www.letta.com/agent"
mcp_support: null
plugin_support: "False"
claude_code_plugin: "False"
subagents: "True"
hooks: "True"
plan_mode: null
model_providers: "OpenAI,Anthropic,Z.ai"
pricing: "freemium"
install_method: "npm install -g @letta-ai/letta-code"
docs_url: "https://docs.letta.com/letta-code"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "jqueryscript"
  - "brad"
  - "ishandutta"
what_makes_it_special: "Stateful agent harness where agents self-improve by rewriting their own memory, skills, prompts, and harness; supports subagents, hooks, crons, and messaging integrations (Slack/Telegram/Discord)."
---

Letta Code applies the MemGPT research lineage (memory blocks, sleep-time compute) to coding: agents hold identity and experience in editable memory blocks, learn skills at global, project, and agent scope, and can rewrite their own prompts and even their harness through a mods mechanism. Memory is git-tracked and syncable to GitHub, /sleeptime runs periodic offline 'dreaming' to consolidate context, and /doctor audits memory health. Subagents, hooks, message search, and messaging integrations (Slack, Telegram, Discord) extend it beyond a single terminal session, with optional Letta Cloud for remote state and GitHub Actions. The harness is Apache-2.0 and free; the cloud layer is the paid part.
