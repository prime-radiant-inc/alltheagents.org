---
name: "plugins-coding-agents"
slug: "plugins-coding-agents"
layout: "agent.njk"
category: "other"
maker: "UI5"
license: "Apache-2.0"
url: "https://github.com/UI5/plugins-coding-agents"
source_code_url: "https://github.com/UI5/plugins-coding-agents"
source_available: "True"
platforms: []
first_released: "2026-03-17"
current_release: "2026-08-18"
stars: "33"
language: "JavaScript/Node.js"
homepage: null
mcp_support: "False"
plugin_support: "True"
claude_code_plugin: "True"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: null
pricing: "Free/open source"
install_method: "Per-plugin installation guides (linked in Plugin Overview)"
docs_url: "https://code.claude.com/docs/"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/UI5/plugins-coding-agents"
maintained: "active"
sources:
  - "github_topic3"
what_makes_it_special: "Provides UI5/SAPUI5/OpenUI5-specific plugins tailored for coding agents, covering project creation, API reference look-up, linter integration, modernization of deprecated APIs, and JavaScript-to-TypeScript conversion — filling a niche for SAP frontend development with AI assistance. Three plugins: UI5, UI5 Modernization, UI5 TypeScript Conversion."
---

plugins-coding-agents is SAP's answer to a recurring problem in enterprise frontend work: general-purpose coding agents know JavaScript but not the conventions, deprecated APIs, and linter rules of SAPUI5/OpenUI5, so AI-assisted changes to UI5 projects break in framework-specific ways. The repository ships three plugins — a general UI5 plugin covering project creation, API reference lookup, and linting; a UI5 Modernization plugin that autonomously replaces deprecated APIs across multi-phase workflows; and a TypeScript Conversion plugin that walks JavaScript UI5 projects through incremental TS migration. Each plugin packages installation guides and skills for Claude Code and compatible agents, maintained under Apache-2.0 by the UI5 (SAP) organization with release-please automation. Its users are SAP frontend developers introducing coding agents into UI5 codebases, supported through the OpenUI5 community Slack and a dedicated Stack Overflow tag.
