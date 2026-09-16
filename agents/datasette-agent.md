---
name: "Datasette Agent"
slug: "datasette-agent"
layout: "agent.njk"
category: "agent"
maker: "datasette"
license: "Apache-2.0"
url: "https://agent.datasette.io/"
source_code_url: "https://github.com/datasette/datasette-agent"
source_available: "True"
homepage: null
docs_url: "https://github.com/datasette/datasette-agent#readme"
download_url: null
install_method: "datasette install datasette-agent"
platforms:
  - "CLI"
  - "Web"
autonomy_level:
  - "agentic"
  - "autonomous-background"
specialization: "sql-data"
language: "Python"
first_released: "2025-11-09"
current_release: "2026-07-31"
maintained: "active"
mcp_support: null
plugin_support: "True"
claude_code_plugin: null
subagents: "True"
hooks: null
plan_mode: null
plugin_docs_url: null
config_docs_url: null
model_providers: "OpenAI, Anthropic, Google Gemini, and any tool-calling model with an LLM plugin, including local models"
pricing: "free"
stars: "117"
sources:
  - "github-issue"
last_verified: "2026-09-11"
what_makes_it_special: "It works with hundreds of tool-calling models, any model with an LLM plugin, and other Datasette plugins can register extra tools for it. With the Datasette Apps plugin installed alongside it, it can also build HTML applications that run in sandboxed frames against your databases."
---

Datasette Agent is an open-source plugin that puts a conversational assistant inside Datasette, the tool for exploring and publishing SQLite databases. Installed next to Datasette, it serves a chat at /-/agent and a `datasette agent chat` mode in the terminal, where the model calls tools to inspect schemas, write and run SQL, and save what it wrote as a Datasette stored query. Write statements and saved queries are shown in full and run only after the person approves them, through Datasette's own permissions, and explorer reports and background agents run toward a goal without further input. Announced in May 2026 and still in alpha releases, it is aimed at people who already keep data in Datasette and want to ask questions of it without leaving the browser.
