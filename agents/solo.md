---
name: "solo"
slug: "solo"
layout: "agent.njk"
category: "multiplexer"
maker: "solo-agent"
license: "MIT"
url: "https://github.com/solo-agent/solo"
source_code_url: "https://github.com/solo-agent/solo"
source_available: "True"
platforms: []
first_released: "2026-06-12"
current_release: "2026-08-16"
stars: "531"
language: "Go, TypeScript"
homepage: "https://soloagent.team"
mcp_support: null
plugin_support: null
claude_code_plugin: null
subagents: null
hooks: null
plan_mode: null
model_providers: null
pricing: "open-source"
install_method: "git clone + make dev (requires Go 1.22+, Node.js 20+, npm, Docker, and a supported agent CLI)"
docs_url: "https://soloagent.team"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "agent_infra"
what_makes_it_special: "Local-first workspace where multiple AI coding agents (Claude Code, Codex, OpenCode, Hermes, OpenClaw) collaborate with humans via channels, threaded tasks, Kanban boards, team graphs, persistent memory, and artifacts — treating agents as teammates rather than CLI tools. Has a 'Thinking mode' that branches conversations into focused reasoning lines."
---

Solo solves the fragmentation of running several agent CLIs in terminal tabs by giving each one a persistent identity inside a shared workspace: a Go server, a local daemon that auto-detects agent CLIs on PATH, and a Next.js front end. Agents join channels, receive mentions and tasks, and keep per-agent memory files loaded into later sessions; work items carry their discussion threads, kanban state, and reviewable artifacts. Five backends are supported out of the box — Claude Code, Codex, OpenCode, Hermes, and OpenClaw — each with per-agent system prompt, model, and environment overrides, and the daemon auto-detects whatever is installed. Everything runs locally with PostgreSQL persistence, and observability views expose run traces and usage. It targets developers who coordinate multiple agents daily and want chat-style collaboration rather than another agent runtime.
