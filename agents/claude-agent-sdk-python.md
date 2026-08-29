---
name: "Claude Agent SDK (Python)"
slug: "claude-agent-sdk-python"
layout: "agent.njk"
category: "agent"
maker: "anthropics"
license: "MIT"
url: "https://github.com/anthropics/claude-agent-sdk-python"
source_code_url: "https://github.com/anthropics/claude-agent-sdk-python"
source_available: "True"
platforms: []
first_released: "2025-06-11"
current_release: "2026-08-20"
stars: "7935"
language: "Python"
homepage: "https://platform.claude.com/docs/en/agent-sdk/python"
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
download_url: "https://github.com/anthropics/claude-agent-sdk-python"
maintained: "active"
sources:
  - "namphuong"
what_makes_it_special: "Official Anthropic Python SDK for building agentic applications powered by Claude Code. In-process SDK MCP servers let custom tools run in the same Python process (no subprocess overhead, better performance, easier debugging, type safety). Auto-bundled Claude Code CLI -- no separate installation needed. Programmable hooks (PreToolUse etc.) for intercepting and controlling agent behavior at lifecycle points. Bidirectional conversations via ClaudeSDKClient for interactive, stateful sessions. Programmatic subagents and session forking. Custom tools defined as Python functions via @tool decorator, implemented as in-process MCP servers."
---

The Claude Agent SDK for Python is Anthropic's supported way to embed Claude Code's agent loop inside Python applications: it drives the same codebase-aware, tool-using agent programmatically rather than interactively. Custom tools are defined as plain Python functions through a @tool decorator backed by in-process MCP servers, avoiding subprocess overhead while remaining interoperable with external stdio MCP servers; hooks intercept lifecycle events such as PreToolUse for permission and safety control, and the SDK supports subagents and session forking for multi-step workflows. The package bundles the Claude Code CLI automatically, so installation is a single pip install without separate setup. Teams use it to build production automation on top of Claude's agentic capabilities — CI pipelines, internal tooling, and custom agent products — with usage governed by Anthropic's commercial terms. It is actively maintained alongside the TypeScript SDK.
