---
name: "honeydew-ai-coding-agents-plugins"
slug: "honeydew-ai-coding-agents-plugins"
layout: "agent.njk"
category: "other"
maker: "honeydew-ai"
license: "Apache-2.0"
url: "https://github.com/honeydew-ai/honeydew-ai-coding-agents-plugins"
source_code_url: "https://github.com/honeydew-ai/honeydew-ai-coding-agents-plugins"
source_available: "True"
platforms: []
first_released: "2026-02-23"
current_release: "2026-08-18"
stars: "39"
language: "Shell"
homepage: "https://honeydew.ai"
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: "True"
subagents: "no"
hooks: "True"
plan_mode: "no"
model_providers: "agent-agnostic (Claude Code, Codex, Cursor, GitHub Copilot CLI, Gemini CLI)"
pricing: "freemium"
install_method: "Claude Code: /plugin marketplace add honeydew-ai/honeydew-ai-coding-agents-plugins then /plugin install honeydew-ai@honeydew-ai-claude-plugins; varies by agent"
docs_url: "https://honeydew.ai/docs/integration/mcp"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/honeydew-ai/honeydew-ai-coding-agents-plugins/releases/latest/download/honeydew-ai-claude.zip"
maintained: "active"
sources:
  - "github_topic3"
what_makes_it_special: "Skills and tools powered by the Honeydew MCP that help coding agents build semantic models and analyze data through natural conversation. 13 skills spanning semantic model creation, querying, anomaly investigation, and validation. Agent-agnostic markdown skills. Supports Snowflake, Databricks, and BigQuery. Plugin packages for Claude Code, Codex, Cursor, GitHub Copilot CLI, and Gemini CLI."
---

honeydew-ai-coding-agents-plugins packages skills and tool access that let coding agents work with enterprise semantic layers. Thirteen skills cover the modeling lifecycle — creating entities, relations, attributes, metrics, and domains — plus exploration, natural-language and YAML querying, filtering, query debugging, mandatory post-creation validation, workspace branching, and bulk review of past analysis conversations. The skills are plain markdown files any agent can consume, wired through the Honeydew MCP server and packaged as native plugins for Claude Code, Codex, Cursor, GitHub Copilot CLI, and Gemini CLI. Under the hood the MCP server executes against Snowflake, Databricks, or BigQuery warehouses through a Honeydew workspace, so the agent builds governed semantic models rather than issuing raw SQL. It targets data teams that want agents to create and query semantic layers with the same guardrails their BI tools enforce.
