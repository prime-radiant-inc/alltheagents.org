---
name: "ai-devkit"
slug: "ai-devkit"
layout: "agent.njk"
category: "agent"
maker: "codeaholicguy"
license: "MIT"
url: "https://github.com/codeaholicguy/ai-devkit"
source_code_url: "https://github.com/codeaholicguy/ai-devkit"
source_available: True
platforms: []
first_released: "2025-10-14"
current_release: "2026-08-19"
stars: "1584"
language: "TypeScript / Node.js"
homepage: "https://ai-devkit.com"
mcp_support: "yes - memory exposed through MCP; init wires up MCP servers per agent"
plugin_support: "yes - composable skills from 30+ publishers; skill add <registry> <skill>"
claude_code_plugin: "yes - .claude-plugin directory; full setup + remote control support"
subagents: "yes - multi-agent coordination (agent send, groups, dev-lifecycle phases)"
hooks: "yes - hooks/ directory, .husky"
plan_mode: "yes - dev-lifecycle skill enforces requirements -> design -> planning -> implementation -> testing -> review"
model_providers: "Claude Code, Gemini CLI, Codex CLI, Grok Build, Cursor, Copilot, Devin, opencode, Pi, Amp, Junie, Cline, Antigravity, Kilo Code, Roo Code"
pricing: "open-source"
install_method: "npm"
docs_url: "https://ai-devkit.com/docs/"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "github_deep"
what_makes_it_special: "Local-first control plane for AI coding agents - unifies scattered agents (Claude Code, Codex, Gemini CLI, Cursor, Copilot, Devin, etc.) under one shared operating layer: single .ai-devkit.json config, live TUI console for supervising sessions, cross-agent messaging (agent send), local SQLite memory retrieval without context bloat, and a dev-lifecycle skill forcing disciplined engineering phases with verification gates. Not a replacement for agents but infrastructure to manage many of them together."
---

Local-first control plane for AI coding agents - unifies scattered agents (Claude Code, Codex, Gemini CLI, Cursor, Copilot, Devin, etc.) under one shared operating layer: single .ai-devkit.json config, live TUI console for supervising sessions, cross-agent messaging (agent send), local SQLite memory retrieval without context bloat, and a dev-lifecycle skill forcing disciplined engineering phases with verification gates. Not a replacement for agents but infrastructure to manage many of them together.
