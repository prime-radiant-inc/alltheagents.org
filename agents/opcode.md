---
name: "opcode"
slug: "opcode"
layout: "agent.njk"
category: "multiplexer"
maker: "winfunc"
license: "AGPL-3.0"
url: "https://github.com/winfunc/opcode"
source_code_url: "https://github.com/winfunc/opcode"
source_available: "Yes"
platforms:
  - "Autonomous"
first_released: "2025-06-19"
current_release: "2025-10-16"
stars: "22382"
language: "Rust"
homepage: "https://opcode.sh"
mcp_support: "yes (dedicated MCP Server Management with registry, config UI, Claude Desktop import)"
plugin_support: "no"
claude_code_plugin: "n/a (standalone GUI built around Claude Code CLI, not a plugin)"
subagents: "yes (CC Agents feature: custom AI agents with system prompts, background process execution)"
hooks: "no"
plan_mode: "no"
model_providers: "Anthropic (Claude models)"
pricing: "open-source"
install_method: "binary (build from source via Tauri 2; releases pending)"
docs_url: "https://opcode.sh"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "github_topic"
what_makes_it_special: "A desktop GUI command center for Claude Code built with Tauri 2 (Rust + React), featuring session/project management, custom AI agents running in isolated background processes, timeline & checkpoints with session branching, and a usage analytics dashboard with real-time cost tracking."
---

opcode is a desktop command center built around the Claude Code CLI, which remains a prerequisite for any use. It browses and resumes sessions from ~/.claude/projects, and its CC Agents feature defines custom agents with system prompts, model selection, and per-agent file and network permissions running in isolated background processes. Usage analytics track cost and token breakdowns by model, project, and time period, and MCP server management centralizes registry configuration with Claude Desktop import. A timeline and checkpoint system versions sessions for branching and one-click restore. The app is built with Tauri 2 and React, stores everything locally with no telemetry, and is developed by the Asterisk team unaffiliated with Anthropic.
