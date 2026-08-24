---
name: "Claude Agent SDK (Python)"
slug: "claude-agent-sdk-python"
layout: "agent.njk"
category: tool
maker: "anthropics"
license: "MIT"
url: "https://github.com/anthropics/claude-agent-sdk-python"
source_code_url: "https://github.com/anthropics/claude-agent-sdk-python"
source_available: True
platforms: []
first_released: "2025-06-11"
current_release: "2026-08-20"
stars: "7935"
language: "Python"
homepage: null
mcp_support: "yes"
plugin_support: "yes"
claude_code_plugin: "no"
subagents: "yes"
hooks: "yes"
plan_mode: "no"
model_providers: "Anthropic"
pricing: "BYOK"
install_method: "pip"
docs_url: "https://platform.claude.com/docs/en/agent-sdk/python"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "namphuong"
what_makes_it_special: "Official Anthropic Python SDK for building agentic applications powered by Claude Code. In-process SDK MCP servers let custom tools run in the same Python process (no subprocess overhead, better performance, easier debugging, type safety). Auto-bundled Claude Code CLI -- no separate installation needed. Programmable hooks (PreToolUse etc.) for intercepting and controlling agent behavior at lifecycle points. Bidirectional conversations via ClaudeSDKClient for interactive, stateful sessions. Programmatic subagents and session forking. Custom tools defined as Python functions via @tool decorator, implemented as in-process MCP servers."
---

Official Anthropic Python SDK for building agentic applications powered by Claude Code. In-process SDK MCP servers let custom tools run in the same Python process (no subprocess overhead, better performance, easier debugging, type safety). Auto-bundled Claude Code CLI -- no separate installation needed. Programmable hooks (PreToolUse etc.) for intercepting and controlling agent behavior at lifecycle points. Bidirectional conversations via ClaudeSDKClient for interactive, stateful sessions. Programmatic subagents and session forking. Custom tools defined as Python functions via @tool decorator, implemented as in-process MCP servers.
