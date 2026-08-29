---
name: "kimchi"
slug: "kimchi"
layout: "agent.njk"
category: "agent"
maker: "getkimchi"
license: "Apache-2.0"
url: "https://github.com/getkimchi/kimchi"
source_code_url: "https://github.com/getkimchi/kimchi"
source_available: "Yes"
platforms:
  - "CLI"
first_released: "2026-04-07"
current_release: "2026-08-19"
stars: "2185"
language: "TypeScript"
homepage: "https://kimchi.dev"
mcp_support: "yes (mcp-adapter extension; can migrate MCP servers from Claude Code, OpenCode, and Cursor)"
plugin_support: "yes"
claude_code_plugin: "yes"
subagents: "yes"
hooks: "yes"
plan_mode: "yes"
model_providers: "Anthropic, OpenAI, BYOK, local (built-in kimchi-dev: kimi-k2.6, minimax-m2.7, nemotron-3-ultra-fp4)"
pricing: "open-source"
install_method: "brew"
docs_url: "https://docs.kimchi.dev"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/getkimchi/kimchi/releases/latest"
maintained: "active"
sources:
  - "github_deep"
what_makes_it_special: "Terminal coding agent with multi-model orchestration that automatically delegates tasks to different models by role (orchestrator, planner, builder, reviewer, explorer, researcher) with automatic tier-based routing for cost optimization, Ferment mode for cross-session progressive project management, built-in LSP integration, and /teleport remote session handoff to cloud sandboxes."
---

Kimchi is a terminal coding agent built on the pi-mono SDK that treats model selection as a routing problem: an orchestrator classifies each request and delegates to planner, builder, reviewer, explorer, and researcher roles, each of which can run on a different model or pool. Tier-based routing escalates complex work to heavier models and tags every request with a phase for cost attribution, and RTK-based hooks compress tool output to cut token spend. A cross-session project mode called Ferment persists goal-phase-step state through a deterministic state machine with crash recovery. It is used by developers who want per-role model economics in the terminal without abandoning Claude Code or Cursor configurations.
