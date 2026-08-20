---
name: "Claude Code"
slug: "claude-code"
layout: "agent.njk"
category: "agent"
maker: "anthropics"
license: "Closed Source"
url: "https://github.com/anthropics/claude-code"
source_code_url: "https://github.com/anthropics/claude-code"
source_available: True
platforms:
  - "CLI"
first_released: "2025-02-22"
current_release: "2026-08-20"
stars: null
language: "TypeScript, JavaScript (Node.js)"
homepage: "https://code.claude.com/docs/en/overview"
mcp_support: True
plugin_support: True
claude_code_plugin: True
subagents: True
hooks: True
plan_mode: True
model_providers: "Anthropic (Claude models)"
pricing: null
install_method: "curl -fsSL https://claude.ai/install.sh | bash (macOS/Linux); brew install --cask claude-code; irm https://claude.ai/install.ps1 | iex (Windows); winget install Anthropic.ClaudeCode; or npm install -g @anthropic-ai/claude-code (deprecated)"
docs_url: "https://code.claude.com/docs/en/overview"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/anthropics/claude-code"
maintained: "active"
sources:
  - "jqueryscript"
  - "brad"
  - "tiennm"
what_makes_it_special: "Anthropic's official terminal-native agentic coding assistant that understands your codebase and operates through natural language; works across terminal, IDE (VS Code with @-mentions and plan review), and GitHub (via @claude mentions). Extensible plugin system for custom commands and agents; MCP server support for external data sources (Google Drive, Jira, Slack); hooks to run shell commands before/after actions (auto-format, lint); subagents via spawnable parallel Claude Code agents coordinated by a lead agent; dedicated Agent SDK for building custom agents. Major project (142k stars, 731 commits)."
---

Anthropic's official terminal-native agentic coding assistant that understands your codebase and operates through natural language; works across terminal, IDE (VS Code with @-mentions and plan review), and GitHub (via @claude mentions). Extensible plugin system for custom commands and agents; MCP server support for external data sources (Google Drive, Jira, Slack); hooks to run shell commands before/after actions (auto-format, lint); subagents via spawnable parallel Claude Code agents coordinated by a lead agent; dedicated Agent SDK for building custom agents. Major project (142k stars, 731 commits).
