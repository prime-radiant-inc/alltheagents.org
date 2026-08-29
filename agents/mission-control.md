---
name: "mission-control"
slug: "mission-control"
layout: "agent.njk"
category: "multiplexer"
maker: "builderz-labs"
license: "MIT"
url: "https://github.com/builderz-labs/mission-control"
source_code_url: "https://github.com/builderz-labs/mission-control"
source_available: "True"
platforms: []
first_released: "2026-02-13"
current_release: "2026-08-18"
stars: "6034"
language: "TypeScript"
homepage: "https://mc.builderz.dev"
mcp_support: "yes"
plugin_support: "yes"
claude_code_plugin: "no"
subagents: "yes"
hooks: "no"
plan_mode: "no"
model_providers: null
pricing: "open-source"
install_method: "docker, source"
docs_url: "https://github.com/builderz-labs/mission-control/blob/main/docs/quickstart.md"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "agent_infra"
what_makes_it_special: "Self-hosted control plane for operating AI agents that sits ABOVE agent runtimes (OpenClaw, Claude Code, Codex, CrewAI, LangGraph, AutoGen, Claude SDK) rather than replacing them. SQLite-backed, runs locally. Single dashboard for task dispatch, agent management, spend tracking, quality review (Aegis gate), memory/skills, scheduling, and governance. Multiple interfaces: Web UI, CLI, built-in MCP server, REST API (OpenAPI), WebSocket, SSE. Alpha software."
---

Mission Control addresses the operations layer that appears once someone runs several agents across several runtimes: which task belongs to which agent, what it cost, whether the output passed review, and what failed overnight. Agents register with heartbeats against runtime adapters for Claude Code, Codex, CrewAI, LangGraph, AutoGen, and others, and tasks flow through an inbox-assignment-execution-review pipeline whose Aegis gate checks quality before a completion receipt issues. The plane tracks token spend and cost per run, schedules cron jobs, raises alerts and webhooks, and exposes memory and skills registries alongside role-based governance, API keys, and audit logs — all over SQLite on a single host with no external services. Interfaces span a Next.js dashboard, a CLI, an OpenAPI REST surface, WebSocket/SSE streams, and an MCP server that lets Claude query the control plane directly. Operators running multiple heterogeneous agents use it for dispatch, audit, and cost control; it explicitly does not replace any runtime's reasoning or tool loop, and remains alpha software.
