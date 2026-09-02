---
name: "Fleet Control"
slug: "fleet-control"
layout: "agent.njk"
category: "multiplexer"
maker: "2389-research"
license: null
url: "https://github.com/2389-research/fleet-control"
source_code_url: "https://github.com/2389-research/fleet-control"
source_available: "True"
platforms:
  - "CLI"
first_released: null
current_release: null
stars: "0"
language: "Go"
homepage: null
mcp_support: "yes (MCP server so agents can inspect/instruct each other)"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "yes (agents can send instructions to other agents via MCP)"
hooks: "no"
plan_mode: "no"
model_providers: null
pricing: "free"
install_method: "go install"
docs_url: null
maintained: "active"
sources:
  - "user_reported"
what_makes_it_special: "Control plane / fleet management tool for AI coding agents running in tmux panes. A background daemon polls tmux sessions, captures pane scrollback, classifies each pane's status (running/idle/done), records session history to SQLite, and exposes a CLI, TUI dashboard, REST API over Unix socket, and MCP server so one agent can inspect, read conversations of, or send instructions to other agents."
---

Fleet Control is a control plane for AI coding agents that live in tmux panes. A background daemon polls tmux sessions, captures each pane's scrollback, and classifies its status — running, idle, or done — so an operator can see the whole fleet at a glance from a TUI dashboard or a CLI. Session history is recorded to SQLite, and a REST API over a Unix socket exposes the same state programmatically. The notable piece is an MCP server: one agent can inspect another pane, read its conversation, or send it instructions, turning the fleet into something agents can drive themselves. Fleet Control owns no agent loop — the agents in the panes do — it just observes, classifies, and relays. The audience is anyone running many agent sessions side by side in tmux who wants visibility and inter-agent coordination without a heavier orchestrator.
