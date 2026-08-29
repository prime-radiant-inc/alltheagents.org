---
name: "codeany"
slug: "codeany"
layout: "agent.njk"
category: "agent"
maker: "codeany-ai"
license: "MIT"
url: "https://github.com/codeany-ai/codeany"
source_code_url: "https://github.com/codeany-ai/codeany"
source_available: "True"
platforms:
  - "CLI"
first_released: "2026-04-01"
current_release: "2026-04-04"
stars: "185"
language: "Go"
homepage: null
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: "False"
subagents: "True"
hooks: "True"
plan_mode: "True"
model_providers: "Anthropic, OpenRouter, custom (via CODEANY_BASE_URL/CODEANY_MODEL env vars)"
pricing: "Free / open source (MIT)"
install_method: "curl -fsSL https://raw.githubusercontent.com/codeany-ai/codeany/main/install.sh | sh, or go install github.com/codeany-ai/codeany/cmd/codeany@latest"
docs_url: "https://github.com/codeany-ai/codeany#readme"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "github_topic5"
what_makes_it_special: "Open-source AI-powered terminal agent built with Go, Bubble Tea TUI, and Open Agent SDK. Features 78 built-in slash commands, custom Skills system (user-defined sub-agents via SKILL.md files), plugin architecture, pre/post tool use hooks, plan mode, Chinese/IME input support, self-update capability, and compatibility with both CODEANY.md and CLAUDE.md project instruction files."
---

Codeany is a terminal coding agent built in Go on the Open Agent SDK with a Bubble Tea interface, covering codebase explanation, test execution, commits, review, and bug investigation through an agentic loop with maxTurns bounds and permission modes. Its configuration surface mirrors Claude Code conventions: project instructions come from CODEANY.md or CLAUDE.md plus .codeany/rules/ markdown files, and per-user state lives under ~/.codeany/ with settings, permissions, memory, sessions, skills, and plugins directories. Extensibility covers stdio MCP servers managed through /mcp, pre/post tool-use hooks, SKILL.md-defined skills, and plugins loaded from ~/.codeany/plugins/. Models default to Anthropic with OpenRouter or custom endpoints configured through environment variables, sessions resume or export as JSON, and non-interactive pipe and print modes support scripting. The project is young — a small commit history and no releases — with Chinese/IME input support among its distinguishing features.
