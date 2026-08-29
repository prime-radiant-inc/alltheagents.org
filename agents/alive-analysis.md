---
name: "alive-analysis"
slug: "alive-analysis"
layout: "agent.njk"
category: "other"
maker: "with-geun"
license: "MIT"
url: "https://github.com/with-geun/alive-analysis"
source_code_url: "https://github.com/with-geun/alive-analysis"
source_available: "True"
platforms: []
first_released: "2026-02-10"
current_release: "2026-05-27"
stars: "41"
language: "Shell"
homepage: null
mcp_support: "True"
plugin_support: null
claude_code_plugin: "True"
subagents: "True"
hooks: null
plan_mode: null
model_providers: null
pricing: "free"
install_method: "git clone and bash install.sh (Claude Code) or --cursor (Cursor) or --both; MCP server via npm install -g alive-analysis-mcp"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/with-geun/alive-analysis"
maintained: "active"
sources:
  - "github_topic"
what_makes_it_special: "Structured analysis workflow toolkit implementing the ALIVE loop (Ask, Look, Investigate, Voice, Evolve) with quality gates. 31 specialist agents with intelligent routing (top 3 per stage). Persistent team analytical memory (Decision Records + AI-maintained Analysis Wiki). Experiment/A-B testing support with pre-registration locks. Education mode with 7 guided scenarios and rubric scoring. Interactive node-graph team dashboard. MCP integration for cross-session memory."
---

Data analysts working inside AI coding agents lacked repeatability: each analysis lived in chat history with no way to reproduce or review it. alive-analysis installs as prompt/agent files for Claude Code or Cursor, structuring work through the Ask, Look, Investigate, Voice, Evolve stages with four mandatory quality gates (scope, data quality, and others) that run automatically. Analyses materialize as five markdown files committed to git, searchable through 25+ slash commands, with an A/B testing mode adding pre-registration locks and SRM detection. A v1.4 memory system adds Decision Records and an AI-compiled Analysis Wiki, plus an optional npm MCP server (alive-analysis-mcp) and Obsidian integration. Single maintainer, MIT-licensed, v1.4.0.
