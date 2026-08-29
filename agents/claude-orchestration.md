---
name: "claude-orchestration"
slug: "claude-orchestration"
layout: "agent.njk"
category: "agent"
maker: "mbruhler"
license: "MIT"
url: "https://github.com/mbruhler/claude-orchestration"
source_code_url: "https://github.com/mbruhler/claude-orchestration"
source_available: "True"
platforms: []
first_released: "2025-11-08"
current_release: "2026-06-01"
stars: "218"
language: null
homepage: null
mcp_support: "no"
plugin_support: "True"
claude_code_plugin: "True"
subagents: "True"
hooks: "no"
plan_mode: "no"
model_providers: "Anthropic (via Claude Code)"
pricing: "Free"
install_method: "/plugin marketplace add mbruhler/claude-orchestration; /plugin install orchestration@mbruhler"
docs_url: "https://github.com/mbruhler/claude-orchestration/blob/main/docs"
plugin_docs_url: "https://github.com/mbruhler/claude-orchestration/blob/main/docs"
config_docs_url: null
download_url: "https://github.com/mbruhler/claude-orchestration"
maintained: "active"
sources:
  - "agent_infra"
what_makes_it_special: "Multi-agent workflow orchestration plugin for Claude Code; chain AI agents to automate complex tasks using natural language or declarative .flow syntax. Markdown-based plugin with built-in agents (Explore, Plan, general-purpose), custom agents importable from ~/.claude/agents/, temp agents."
---

The plugin brings data-pipeline ergonomics to agent work: instead of re-prompting Claude Code through each step of a multi-stage task, users describe a workflow in natural language or .flow syntax, and the plugin decomposes it into chained sub-agent invocations with captured outputs feeding later steps. Temp agents handle concrete steps like scraping or database queries; @review checkpoints pause for human input; state snapshots let crashed workflows resume; and .flow.test files allow dry-run unit testing of workflows. Everything runs through the Claude Code plugin system with no separate runtime. Developers automating scraping, reporting, and multi-repo chores install it from the plugin marketplace.
