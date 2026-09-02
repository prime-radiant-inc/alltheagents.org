---
name: "Hex"
slug: "hex"
layout: "agent.njk"
category: "agent"
maker: "2389-research"
license: "MIT"
url: "https://github.com/2389-research/hex"
source_code_url: "https://github.com/2389-research/hex"
source_available: "True"
platforms:
  - "CLI"
first_released: null
current_release: null
stars: "1"
language: "Go"
homepage: null
mcp_support: "yes (extensible via MCP servers)"
plugin_support: "yes (MCP server integration)"
claude_code_plugin: "no"
subagents: "yes (Task tool for sub-agents)"
hooks: "no"
plan_mode: "no"
model_providers: "Anthropic (Claude)"
pricing: "BYOK"
install_method: "curl install script, homebrew, go install, or pre-built binaries"
docs_url: null
maintained: "active"
sources:
  - "user_reported"
what_makes_it_special: "Open-source Claude Code–style agentic CLI built in Go with 13 built-in tools (Read, Write, Bash, Edit, Grep, Glob, AskUserQuestion, TodoWrite, WebFetch, WebSearch, Task, BashOutput, KillShell), SQLite conversation persistence with resume, streaming responses, sub-agents, background processes, and multi-agent orchestration with event-sourcing and cost tracking. Uses Bubbletea TUI, Cobra CLI, and pure-Go SQLite."
---

Hex is a native-Go answer to Claude Code for developers who would rather run their coding agent as a single statically-linked binary than a Node stack. Inspired by Claude Code, Crush, Codex, and MaKeR, it ships 13 built-in tools — Read, Write, Bash, Edit, Grep, Glob, AskUserQuestion, TodoWrite, WebFetch, WebSearch, Task, BashOutput, and KillShell — covering file work, shell control, web fetches, and sub-agent fan-out. Conversations persist in pure-Go SQLite and can be resumed, so long tasks survive restarts, and streaming responses keep the Bubbletea TUI responsive while background processes and sub-agents run in parallel. A v1.0.0 production release reflects real polish, and MCP server integration extends the tool surface beyond the built-ins. The target user is a Go developer who wants a fast, self-contained, Claude-backed coding agent without leaving the language's toolchain.
