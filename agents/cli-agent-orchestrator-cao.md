---
name: "CLI Agent Orchestrator (CAO)"
slug: "cli-agent-orchestrator-cao"
layout: "agent.njk"
category: "multiplexer"
maker: "awslabs"
license: "Apache-2.0"
url: "https://github.com/awslabs/cli-agent-orchestrator"
source_code_url: "https://github.com/awslabs/cli-agent-orchestrator"
source_available: "True"
platforms:
  - "CLI"
first_released: "2025-07-29"
current_release: "2026-08-19"
stars: "1079"
language: "Python"
homepage: "https://awslabs.github.io/cli-agent-orchestrator/"
mcp_support: "yes"
plugin_support: "yes"
claude_code_plugin: "no"
subagents: "yes"
hooks: "no"
plan_mode: "no"
model_providers: "Kiro CLI, Claude Code, Codex CLI, Antigravity CLI, Hermes, Kimi CLI, GitHub Copilot CLI, OpenCode CLI, Oh My Pi (OMP) CLI, Cursor CLI, Grok Build CLI"
pricing: "open-source"
install_method: "pip"
docs_url: "https://awslabs.github.io/cli-agent-orchestrator/"
plugin_docs_url: null
config_docs_url: "https://awslabs.github.io/cli-agent-orchestrator/"
download_url: "https://pypi.org/project/cli-agent-orchestrator/"
maintained: "active"
sources:
  - "brad"
what_makes_it_special: "Orchestrates multiple AI coding CLI agents simultaneously in isolated tmux sessions, allowing a supervisor to delegate work to specialist agents in parallel or sequence. Supports 11+ provider CLIs, offers a Web UI, MCP server, plugins, flows/workflows, skills, persistent memory with self-learning, and agent profiles — all while keeping each agent as a full native CLI process with its own authentication."
---

CAO solves the coordination problem when a team uses several CLI coding agents at once: each provider CLI keeps its own authentication and full native capability, while CAO handles tmux session isolation, delegation from a supervisor profile to specialist workers, and lifecycle management through a server with a Web UI, HTTP API, PTY WebSocket, and MCP surface. Flows extend ad-hoc delegation into scheduled multi-step pipelines, and profiles can restrict which tools an agent may use. It is Apache-2.0, pip-installable from awslabs, documented with courses, and under active development, making it the most institutional entry among the CLI-agent orchestrators.
