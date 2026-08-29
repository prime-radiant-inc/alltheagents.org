---
name: "CornMCP"
slug: "cornmcp"
layout: "agent.njk"
category: "other"
maker: "yuki-20"
license: "MIT"
url: "https://github.com/yuki-20/CornMCP"
source_code_url: "https://github.com/yuki-20/CornMCP"
source_available: "True"
platforms: []
first_released: "2026-03-26"
current_release: "2026-04-14"
stars: "64"
language: "TypeScript"
homepage: null
mcp_support: "True"
plugin_support: null
claude_code_plugin: null
subagents: null
hooks: null
plan_mode: "True"
model_providers: "Voyage AI, OpenAI-compatible embedding APIs"
pricing: "Free / open source (MIT)"
install_method: "npx corn-install (recommended) or manual git clone + pnpm + Docker"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/yuki-20/CornMCP"
maintained: "active"
sources:
  - "github_topic2"
what_makes_it_special: "MCP server + analytics dashboard giving AI coding agents surgical, token-saving access to codebases via 18 tools: semantic memory, AST-based code intelligence, quality gates, session tracking, analytics"
---

Coding agents waste tokens re-reading code, re-deriving call graphs, and repeating lessons from prior sessions, and nothing checks the quality of what they produce before it lands. CornMCP runs locally as a three-service stack - an MCP server exposing 18 tools, a Hono REST API with a native TypeScript AST engine, and a Next.js analytics dashboard - giving agents surgical codebase access instead of repeated full-file reads. Semantic memory stores persist lessons across sessions, impact analysis traces the blast radius of a proposed change, and quality gates reject agent plans scoring below a threshold before execution proceeds. Session tracking and tool-usage analytics surface in the dashboard for tuning. Developers running Claude Code, Cursor, Codex, or Windsurf against large codebases attach it to cut token spend and enforce standards.
