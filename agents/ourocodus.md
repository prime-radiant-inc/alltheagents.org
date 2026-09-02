---
name: "Ourocodus"
slug: "ourocodus"
layout: "agent.njk"
category: "multiplexer"
maker: "2389-research"
license: "MIT"
url: "https://github.com/2389-research/ourocodus"
source_code_url: "https://github.com/2389-research/ourocodus"
source_available: "True"
platforms:
  - "Web"
first_released: null
current_release: null
stars: "0"
language: "Go"
homepage: null
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "yes (spins up multiple Claude Code ACP processes)"
hooks: "no"
plan_mode: "no"
model_providers: "Claude Code (via ACP), OpenAI Codex, other ACP-compatible agents"
pricing: "free"
install_method: "git clone, go build"
docs_url: null
maintained: "active"
sources:
  - "user_reported"
what_makes_it_special: "Multi-agent orchestrator that spins up and coordinates multiple AI coding agents (Claude Code via claude-code-acp, OpenAI Codex, or other ACP-compatible agents) working concurrently on the same codebase. Manages git worktrees, session lifecycle, and a WebSocket relay with optional Docker container isolation and NATS event logging. The agent loop belongs to the underlying agents; Ourocodus multiplexes them."
---

Ourocodus is an orchestrator and relay that runs several coding agents concurrently on one codebase and coordinates them, rather than being an agent itself. It speaks the Agent Client Protocol (ACP), so it can spin up Claude Code through claude-code-acp alongside OpenAI Codex or any other ACP-compatible agent, and route work between them over a WebSocket relay. Each agent gets its own git worktree and managed session lifecycle, with optional Docker container isolation and NATS event logging for observability. The agent loop stays with the underlying agents — Ourocodus multiplexes them, manages their worktrees, and relays their outputs. The project is early stage and aimed at users who want to experiment with multi-agent concurrency on shared code.
