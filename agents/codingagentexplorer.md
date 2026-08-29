---
name: "CodingAgentExplorer"
slug: "codingagentexplorer"
layout: "agent.njk"
category: "other"
maker: "tndata"
license: "MIT"
url: "https://github.com/tndata/CodingAgentExplorer"
source_code_url: "https://github.com/tndata/CodingAgentExplorer"
source_available: "True"
platforms: []
first_released: "2026-02-08"
current_release: "2026-08-02"
stars: "48"
language: "C# / .NET 10 (vanilla HTML/JS/CSS frontend)"
homepage: "https://nestenius.se/ai/introducing-the-coding-agent-explorer-net/"
mcp_support: "True"
plugin_support: null
claude_code_plugin: null
subagents: "True"
hooks: "True"
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

Claude Code hides its API traffic in the terminal, which makes it hard to debug hook behavior, MCP server interactions, or unexpected token usage, and it gives instructors nothing to show students. Coding Agent Explorer inserts itself as a localhost reverse proxy: Claude Code is pointed at it via ANTHROPIC_BASE_URL, the proxy forwards to the Anthropic API, and a SignalR dashboard renders every request, response, streaming event, and MCP JSON-RPC call as a live chat-style timeline with token usage and latency per request. A companion HookAgent CLI captures all fifteen Claude Code hook event types and posts them to the same dashboard. Storage is in-memory (capped at 1,000 requests), API keys are redacted, and everything stays on localhost. It is used by developers debugging MCP servers and hooks, and by .NET instructor Tore Nestenius in his AI agent workshops.
