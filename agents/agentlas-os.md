---
name: "Agentlas OS"
slug: "agentlas-os"
layout: "agent.njk"
category: "other"
maker: "agentlas-ai"
license: "Apache-2.0"
url: "https://github.com/agentlas-ai/Agentlas-OS"
source_code_url: "https://github.com/agentlas-ai/Agentlas-OS"
source_available: "True"
platforms:
  - "Web"
first_released: "2026-06-04"
current_release: "2026-08-19"
stars: "1158"
language: "Shell, Python"
homepage: "https://agentlas.cloud"
mcp_support: "yes"
plugin_support: "yes"
claude_code_plugin: "no"
subagents: "yes"
hooks: "yes"
plan_mode: "no"
model_providers: "Anthropic (Claude Code), OpenAI (Codex), Google (Gemini CLI), Antigravity, Cursor, OpenCode, OpenClaw, Hermes, Grok, local/API models (BYOM)"
pricing: "open-source"
install_method: "binary"
docs_url: "https://agentlas.cloud/docs/trust/agent-trust"
plugin_docs_url: "https://github.com/agentlas-ai/Agentlas-OS/blob/main/PLUGIN_CONTRIBUTIONS.md"
config_docs_url: null
download_url: "https://github.com/agentlas-ai/Agentlas-OS/releases/latest"
maintained: "active"
sources:
  - "brad"
what_makes_it_special: "Engine-neutral agent standard: agents are portable, owner-scoped packages (not trapped in one vendor workspace). Separates Build/Borrow/Own. Package contract is a 'method document' with routing cards, memory boundaries, verification gates. Local-first execution; works across multiple LLM hosts with the same agent package. Per-runtime plugin drivers for Claude Code, Codex, etc. Multi-agent teams with PM Orchestrator, Memory Curator, Policy Gate, QA."
---

Agent definitions are usually trapped inside a single vendor's workspace, so Agentlas OS specifies a package format that separates the LLM (the worker), the runtime (files, shell, browser facilities), and the agent package (procedures, judgement rules, I/O contracts, stop conditions). A package-contract.json plus a verification script enforce that every build emits required artifacts such as intake and output schemas, and provenance markers (extracted, read, graded, absent) keep package claims auditable. Runtime drivers adapt the same package to Claude Code, Codex, Gemini CLI/Antigravity, Cursor, OpenCode, OpenClaw, Hermes, Grok, Kimi, Goose, Ollama, and API hosts through slash commands like /agentlas build or Codex $hephaestus-* skills. Supporting subsystems include a meta-agent factory, a briefing interview engine that freezes work briefs after ambiguity gates, Stormbreaker verification-gated execution, and a local SQLite/FTS5 ontology runtime. Developers who want agent assets to outlive any one vendor workspace are the target audience.
