---
name: "ai-dev-kit"
slug: "ai-dev-kit"
layout: "agent.njk"
category: "other"
maker: "databricks-solutions"
license: "Databricks License (proprietary, © 2026 Databricks, Inc.)"
url: "https://github.com/databricks-solutions/ai-dev-kit"
source_code_url: "https://github.com/databricks-solutions/ai-dev-kit"
source_available: "Source-visible (no OSS license)"
platforms:
  - "IDE"
first_released: "2025-12-17"
current_release: "2026-08-13"
stars: "1856"
language: "Python"
homepage: null
mcp_support: "yes (standalone databricks-mcp-server exposing 40+ Databricks tools; builder app also serves as MCP server at /mcp)"
plugin_support: "yes"
claude_code_plugin: "yes"
subagents: "no"
hooks: "yes"
plan_mode: "no"
model_providers: "BYOK (works with any AI coding agent: Claude Code, Cursor, Gemini CLI, Antigravity, Codex, GitHub Copilot, Windsurf, OpenCode, Kiro)"
pricing: "free"
install_method: "binary"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://raw.githubusercontent.com/databricks-solutions/ai-dev-kit/main/install.sh"
maintained: "active"
sources:
  - "github_deep"
what_makes_it_special: "Curated by Databricks Field Engineering, brings Databricks-specific patterns/skills to any AI coding agent with a Visual Builder App with Claude Code integration. Includes a standalone MCP server exposing 40+ Databricks tools. Certified Gold Project; works across 9+ AI coding tools with a single install."
---

Building on Databricks means knowing house patterns for Unity Catalog, Spark Declarative Pipelines, AI/BI dashboards, and Genie spaces — knowledge generic coding agents lack. The AI Dev Kit ships those patterns as agent skills installable into Claude Code, Cursor, Codex, Gemini CLI, Copilot, and Windsurf, with distribution now delegated to the official databricks/databricks-agent-skills repo through the Databricks CLI and tracked in a skills.lock file. A standalone MCP server exposes over 40 Databricks operations to any MCP client, and a full-stack Visual Builder app provides chat-driven Databricks development that can itself run as an MCP server. Installation is a one-liner per platform that delegates to the Databricks CLI. It is aimed at developers building Databricks assets with any coding agent, under the Databricks source license rather than an OSI license.
