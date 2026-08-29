---
name: "Cursor Memories / Automations (CMA)"
slug: "cursor-memories-automations-cma"
layout: "agent.njk"
category: "agent"
maker: null
license: null
url: "https://cursor.com/changelog/03-05-26"
source_code_url: null
source_available: "False"
platforms: []
first_released: null
current_release: null
stars: null
language: null
homepage: null
mcp_support: "True"
plugin_support: null
claude_code_plugin: null
subagents: null
hooks: "True"
plan_mode: null
model_providers: null
pricing: null
install_method: "Create at cursor.com/automations or start from a template on the Cursor Marketplace"
docs_url: "https://cursor.com/changelog/03-05-26"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "zhouhao"
what_makes_it_special: "Always-on agents triggered by schedules or events from Slack, Linear, GitHub, PagerDuty, and webhooks; spins up cloud sandbox on invocation using configured MCPs and models; memory tool enables agents to learn from past runs and improve with repetition."
---

Introduced in Cursor's March 2026 changelog, Automations extend the Cursor agent beyond interactive sessions: each automation runs on a schedule or in response to events from Slack, Linear, GitHub, PagerDuty, or webhooks, at which point Cursor spins up a cloud sandbox carrying the MCP servers and models the user has configured. A memory tool lets the agent retain lessons from previous runs so repeated automations improve rather than repeat mistakes. Users create automations from a marketplace of templates or from scratch at cursor.com/automations. The feature targets teams who want repo-aware background work, such as incident triage or dependency follow-ups, without a human opening the IDE.
