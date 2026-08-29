---
name: "Proliferate"
slug: "proliferate"
layout: "agent.njk"
category: "multiplexer"
maker: "proliferate-ai"
license: "AGPL-3.0"
url: "https://github.com/proliferate-ai/proliferate"
source_code_url: "https://github.com/proliferate-ai/proliferate"
source_available: "True"
platforms:
  - "Desktop"
  - "Web"
first_released: "2026-04-30"
current_release: "2026-08-27"
stars: 440
language: "Rust"
homepage: "https://proliferate.com"
mcp_support: "yes"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "yes"
hooks: "no"
plan_mode: "no"
model_providers: "delegates to the connected agents (Claude Code, Codex, OpenCode, Cursor, Grok)"
pricing: "free"
install_method: "Desktop app for macOS, or self-host the control plane via Docker Compose, one-click AWS CloudFormation, GCP, Azure, Kubernetes, or air-gapped deployment"
docs_url: "https://proliferate.com/docs"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "hackernews"
what_makes_it_special: "An open-source AI IDE that runs Claude Code, Codex, OpenCode, Cursor, and Grok in parallel through their native harnesses, giving every task an isolated git worktree with its own branch, terminal, conversation, and review state, plus recurring and event-driven workflows — self-hostable all the way to air-gapped operation."
---

Proliferate is a workspace for running many coding agents at once rather than a coding agent itself: each task gets an isolated git worktree and the agent of your choice drives it through its native harness, so subscriptions, logins, and MCP servers stay as configured. The control plane is fully self-hostable — Docker Compose, one-click AWS, GCP, Azure, Kubernetes, or air-gapped — with a macOS desktop app for local use, and the runtime itself is Rust with a TypeScript/Node frontend. Beyond parallel sessions it supports subagent delegation, integrations including MCP, skills, computer and browser use, and custom tools, plus workflows that run agents on schedules or events like nightly reviews and alert triage. Its audience is teams and self-hosters who want a Vercel-style control plane over the agent CLIs they already pay for.
