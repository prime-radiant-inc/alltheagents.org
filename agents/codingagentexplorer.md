---
name: "CodingAgentExplorer"
slug: "codingagentexplorer"
layout: "agent.njk"
category: "agent"
maker: "tndata"
license: "MIT"
url: "https://github.com/tndata/CodingAgentExplorer"
source_code_url: "https://github.com/tndata/CodingAgentExplorer"
source_available: True
platforms: []
first_released: "2026-02-08"
current_release: "2026-08-02"
stars: "48"
language: "C# / .NET 10 (vanilla HTML/JS/CSS frontend)"
homepage: "https://nestenius.se/ai/introducing-the-coding-agent-explorer-net/"
mcp_support: True
plugin_support: null
claude_code_plugin: null
subagents: True
hooks: True
plan_mode: null
model_providers: "Anthropic"
pricing: "Free (open-source, MIT)"
install_method: "git clone, dotnet build, dotnet run --project CodingAgentExplorer; configure with EnableProxy.sh/bat"
docs_url: "https://nestenius.se/ai/introducing-the-coding-agent-explorer-net/"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/tndata/CodingAgentExplorer"
maintained: "active"
sources:
  - "github_topic3"
what_makes_it_special: "Real-time .NET proxy and dashboard for inspecting Claude Code API calls. Transparent proxy architecture using YARP and SignalR. Captures MCP tool calls between Claude Code and HTTP-based MCP servers (port 9999). HookAgent CLI bridges Claude Code's hook system with 15 hook events. API keys automatically redacted for security. Note: this is an inspection/observability tool, not a coding agent harness itself."
---

Real-time .NET proxy and dashboard for inspecting Claude Code API calls. Transparent proxy architecture using YARP and SignalR. Captures MCP tool calls between Claude Code and HTTP-based MCP servers (port 9999). HookAgent CLI bridges Claude Code's hook system with 15 hook events. API keys automatically redacted for security. Note: this is an inspection/observability tool, not a coding agent harness itself.
