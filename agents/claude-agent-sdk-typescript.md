---
name: "Claude Agent SDK (TypeScript)"
slug: "claude-agent-sdk-typescript"
layout: "agent.njk"
category: "agent-sdk"
maker: "anthropics"
license: "Anthropic Commercial Terms of Service"
url: "https://github.com/anthropics/claude-agent-sdk-typescript"
source_code_url: "https://github.com/anthropics/claude-agent-sdk-typescript"
source_available: "True"
platforms: []
first_released: "2025-09-27"
current_release: "2026-08-20"
stars: "1706"
language: "TypeScript / Node.js"
homepage: "https://docs.claude.com/en/api/agent-sdk/overview"
mcp_support: "yes (SDK MCP servers for custom tools)"
plugin_support: "yes"
claude_code_plugin: "n/a - this IS the Claude Code agent SDK"
subagents: "yes"
hooks: "yes"
plan_mode: "yes (permission modes: default, acceptEdits, plan, bypassPermissions)"
model_providers: "Anthropic (Claude)"
pricing: "BYOK"
install_method: "npm"
docs_url: "https://docs.claude.com/en/api/agent-sdk/overview"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/anthropics/claude-agent-sdk-typescript"
maintained: "active"
sources:
  - "namphuong"
what_makes_it_special: "Official Anthropic SDK that programmatically embeds Claude Code's agentic capabilities (codebase understanding, file editing, shell command execution, complex workflow orchestration) into custom TypeScript/Node.js applications. The evolution of the former 'Claude Code SDK', bridging interactive Claude Code use and production-grade automated agent systems."
---

The TypeScript Agent SDK is Anthropic's mechanism for embedding Claude Code's capabilities into custom applications and infrastructure: rather than driving the interactive CLI, programs invoke the same agent loop — codebase comprehension, file edits, shell command execution, multi-step workflow orchestration — as a library call. Renamed from the Claude Code SDK in late 2025, it exposes hooks for intercepting and controlling agent behavior at lifecycle points, custom tools registered as in-process MCP servers, permission modes that gate tool use, and sessions that persist or fork for resumable workflows. Teams use it to build production agent systems on top of Claude's coding competence without shelling out to a terminal process, from CI automation to custom internal copilots. Distribution follows Anthropic's commercial terms rather than an open-source license, and the SDK is actively developed as the sanctioned TypeScript entry point to the agent runtime.
