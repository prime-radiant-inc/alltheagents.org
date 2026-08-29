---
name: "Cortex Code CLI"
slug: "cortex-code-cli"
layout: "agent.njk"
category: "agent"
maker: null
license: "Apache-2.0 (CLI); Snowflake Skills License (skills)"
url: "https://www.snowflake.com/en/product/cortex-code/"
source_code_url: null
source_available: "Yes"
platforms:
  - "CLI"
first_released: null
current_release: null
stars: null
language: "Python"
homepage: null
mcp_support: null
plugin_support: "yes (works as plugins for Claude Code and OpenAI Codex; auto-detects Snowflake prompts and routes them; also works natively in Cursor via 'Third-party skills')"
claude_code_plugin: "yes"
subagents: null
hooks: null
plan_mode: "yes"
model_providers: "Claude and OpenAI GPT models via Snowflake Cortex (auto-select available)"
pricing: "usage"
install_method: "bash install.sh / ./install.ps1 / npx @snowflake-labs/ai-kit"
docs_url: "https://docs.snowflake.com/en/user-guide/cortex-code/cortex-code-cli"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/Snowflake-Labs/snowflake-ai-kit"
maintained: "active"
sources:
  - "brad"
what_makes_it_special: "Snowflake's data-native AI coding agent CLI with 55+ built-in skills spanning SQL, data governance, dynamic tables, ML, streaming, cost intelligence, lineage, dbt, notebooks, and security investigation; lightweight keyword filter runs on every prompt (~50ms, no network) to detect Snowflake intent and auto-route; ships as plugins for Claude Code and Codex."
---

Data engineering work - writing SQL, tracing lineage, tuning warehouses, building dbt projects - happens inside Snowflake's governance boundary, where generic coding agents lack both context and permissions. Cortex Code is Snowflake's terminal agent for that domain: it takes natural-language requests, orchestrates over 55 Snowflake-native skills plus MCP tools, shows its reasoning steps, and in plan mode confirms each action before executing. Skills cover catalog discovery, query optimization, dynamic tables, cost intelligence, lineage, dbt projects, and security investigation, and the same skill set installs as plugins for Claude Code, Codex, and Cursor via Snowflake's AI Kit. Access requires a paid Snowflake account with Cortex roles, with usage billed through Snowflake Cortex; Claude and OpenAI models are selectable via /model. Data engineers and analytics teams are the users.
