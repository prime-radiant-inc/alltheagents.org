---
name: "BLACKBOX AI"
slug: "blackbox-ai"
layout: "agent.njk"
category: "agent"
maker: "BLACKBOXAI"
license: "Proprietary"
url: "https://marketplace.visualstudio.com/items?itemName=Blackboxapp.blackbox"
source_code_url: null
source_available: null
platforms:
  - "IDE"
first_released: "2022-09-01"
current_release: "2026-08-25"
stars: null
language: null
homepage: "https://www.blackbox.ai"
mcp_support: "True"
plugin_support: "no"
claude_code_plugin: "no"
subagents: null
hooks: null
plan_mode: null
model_providers: "Blackbox-hosted models plus Claude, GPT, Gemini, Grok endpoints via its router"
pricing: "usage"
install_method: "Install from the VS Code Marketplace"
docs_url: "https://docs.blackbox.ai"
plugin_docs_url: null
config_docs_url: null
download_url: "https://marketplace.visualstudio.com/items?itemName=Blackboxapp.blackbox"
maintained: "active"
sources:
  - "gap-2026-08-20"
what_makes_it_special: "AI coding assistant with real-time code completion, documentation, and debugging suggestions"
---

Blackbox AI operates an enterprise inference platform and, increasingly, an agent-dispatch service on top of it. Its Agents API accepts a task over HTTP, runs it in an isolated cloud sandbox with full terminal, filesystem, and Git access, streams logs back to the caller, and opens pull requests with scoped branches and test evidence on GitHub, GitLab, or Bitbucket. A distinguishing capability is multi-agent orchestration: the same task can be dispatched in parallel to Blackbox, Claude Code, Codex, and Gemini agents, with a 'Chairman LLM' evaluating the implementations and a human able to override the selection. The company also ships an 'agentic terminal' CLI and a VS Code extension ('Blackbox Agent - Coding Copilot') that edits files and runs commands with per-step permission. Enterprise inference is the revenue engine — zero data retention at the gateway and single-tenant GPU deployments — with the coding agent layered on the same infrastructure for teams that want both from one vendor.
