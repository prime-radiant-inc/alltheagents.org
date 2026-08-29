---
name: "Traycer AI"
slug: "traycer-ai"
layout: "agent.njk"
category: "multiplexer"
maker: "Traycer"
license: "Proprietary"
url: "https://traycer.ai"
source_code_url: null
source_available: "False"
platforms:
  - "IDE"
first_released: "2025"
current_release: "2026"
stars: null
language: null
homepage: "https://traycer.ai"
mcp_support: null
plugin_support: "True"
claude_code_plugin: "False"
subagents: "True"
hooks: "False"
plan_mode: "True"
model_providers: "BYOA: Claude Code, Codex, Cursor, OpenCode, Gemini, Windsurf, custom agents, local runtimes; optional Traycer native inference on paid tiers"
pricing: "BYOA $0/user/month, Sync $10/user/month, Lite $20/user/month, Pro $40/user/month, Ultra $100/user/month"
install_method: "VS Code / Open VSX extension"
docs_url: "https://traycer.ai"
plugin_docs_url: null
config_docs_url: null
download_url: "https://traycer.ai/download"
maintained: "active"
sources:
  - "web_search_multilingual"
what_makes_it_special: "Orchestration and planning layer ('Nerve Center') for coding agents — connects agents like Claude Code, Codex, Cursor, and Opencode in a shared workspace with shared context, memory, and handoff. Built-in workflow skills for planning, debugging, and reviewing. Available as VS Code / Open VSX extension. BYOA (Bring Your Own Agent) tier is free."
---

Traycer addresses the fragmentation of running multiple coding agents: each lives in its own chat, plans live in scrollback, and handing work between agents means re-explaining everything. It sits above the agents as a shared workspace — each task carries its own filesystem, artifacts, and decision memory so models can be switched mid-task without losing context, while agents ask each other questions, request reviews, and hand off work through a defined protocol over worktrees. The built-in skills cover planning, debugging, reviewing, debating, documenting, and ticket-breaking, with Epic Mode decomposing high-level intent into specs before any code exists. Teams use it to supervise several agents from one workspace, with teammates inspecting tasks and steering work in multiplayer mode; pricing starts at $0 for BYOA, with paid tiers for cloud sync and Traycer-hosted inference.
