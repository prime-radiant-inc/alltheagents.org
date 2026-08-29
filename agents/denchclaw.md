---
name: "DenchClaw"
slug: "denchclaw"
layout: "agent.njk"
category: "agent"
maker: "DenchHQ"
license: "MIT"
url: "https://github.com/DenchHQ/DenchClaw"
source_code_url: "https://github.com/DenchHQ/DenchClaw"
source_available: "Yes"
platforms:
  - "Desktop"
first_released: "2026-02-01"
current_release: "2026-06-11"
stars: "1643"
language: "TypeScript"
homepage: "https://denchclaw.com"
mcp_support: null
plugin_support: null
claude_code_plugin: null
subagents: null
hooks: null
plan_mode: null
model_providers: null
pricing: "open-source"
install_method: "npx denchclaw@latest bootstrap (Node 22+)"
docs_url: "https://denchclaw.com"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "hackernews"
what_makes_it_special: "MIT-licensed framework that boots a dedicated OpenClaw gateway profile ('openclaw --profile dench') with its own gateway (~/.openclaw-dench, port 19001) and web UI (localhost:3100) for CRM automation and outreach agents; installed via npx denchclaw bootstrap with a Dench API key; 1.6k+ stars; maker now points users to dench.com, whose hosted product is $99/seat/month."
---

DenchClaw repackages the OpenClaw local-agent runtime into a personal CRM: contacts live in object tables, agents browse the web through your Chrome profile, answer questions by generating SQL against a local DuckDB, and update kanban pipelines automatically. Bootstrap provisions a separate OpenClaw gateway profile so DenchClaw coexists with a vanilla OpenClaw install, and skills from the Skills Store extend what agents can do. Scheduled 'Routines' run cron-style automations such as weekly reports or lead enrichment. It targets solo operators and small teams doing sales and outreach work who want agent automation on their own machine rather than a hosted SaaS.
