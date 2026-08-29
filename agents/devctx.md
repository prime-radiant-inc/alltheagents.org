---
name: "devctx"
slug: "devctx"
layout: "agent.njk"
category: "other"
maker: "IAmUnbounded"
license: "MIT"
url: "https://github.com/IAmUnbounded/devctx"
source_code_url: "https://github.com/IAmUnbounded/devctx"
source_available: "True"
platforms:
  - "IDE"
first_released: "2026-02-14"
current_release: "2026-02-15"
stars: "233"
language: "TypeScript/JavaScript (Node.js)"
homepage: null
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: null
subagents: "no"
hooks: "True"
plan_mode: "no"
model_providers: "OpenAI-compatible"
pricing: "open-source"
install_method: "npm install -g devctx"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/IAmUnbounded/devctx"
maintained: "active"
sources:
  - "github_topic"
what_makes_it_special: "CLI tool that captures and restores AI coding context (task, goal, approaches, decisions, state) scoped to repo and branch, enabling persistence across sessions, editors, and team members. Provides an MCP server for Claude Code & Windsurf with tools devctx_save, devctx_resume, devctx_log."
---

Every AI coding session starts from zero context, and the problem compounds when a teammate or a different editor takes over. devctx treats the prompt itself as the interface: a .devctx/ directory in the repo stores task, goal, approaches tried, decisions, and stopping state, and `devctx resume` emits a formatted prompt that any assistant can ingest. Core commands run locally with no API key; optional AI commands (summarize, suggest, compress) use an OpenAI-compatible endpoint. An MCP server exposes the same context natively to Claude Code and Windsurf, and a VS Code extension auto-resumes context on project open. Teams commit the folder to git so intent history syncs alongside code.
