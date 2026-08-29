---
name: "clodex-ide"
slug: "clodex-ide"
layout: "agent.njk"
category: "agent"
maker: "mereyabdenbekuly-ctrl"
license: "AGPL-3.0"
url: "https://github.com/mereyabdenbekuly-ctrl/clodex-ide"
source_code_url: "https://github.com/mereyabdenbekuly-ctrl/clodex-ide"
source_available: "True"
platforms:
  - "IDE"
  - "Autonomous"
first_released: "2026-07-12"
current_release: "2026-08-13"
stars: "862"
language: "TypeScript"
homepage: "https://ide.clodex.xyz"
mcp_support: "yes — user-configured stdio and remote MCP servers, HTTP/SSE transports, OAuth flows, tools, resources, prompts, approval-aware execution"
plugin_support: "yes — integration surfaces for plugins and extension metadata, MCP servers, and reusable skills/context files"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "CLODEx account (hosted models), BYOK, custom OpenAI-compatible endpoints, Ollama (local inference)"
pricing: "free"
install_method: "binary"
docs_url: "https://ide.clodex.xyz"
plugin_docs_url: "https://github.com/mereyabdenbekuly-ctrl/clodex-ide/blob/main/docs/developer/extensions-and-integrations.md"
config_docs_url: null
download_url: "https://github.com/mereyabdenbekuly-ctrl/clodex-ide/releases"
maintained: "active"
sources:
  - "github_deep"
what_makes_it_special: "Local-first agentic IDE for long-running engineering work with durable tasks that persist across restarts; zero-trust philosophy (model output is input, not authority) with explicit permission/approval/review surfaces; proof-based releases with SBOMs and checksums."
---

CLODEx restructures agent interaction around persistence: a task carries workspace context, approval history, and pending edits across restarts, so long-running engineering work survives reboots and session switches instead of being reconstructed from messages. The agent runtime inspects files and executes local tools only through explicit permission checks, and every output - diffs, terminal logs, browser state - lands on review surfaces before it can be committed, enforcing the principle that model output is input rather than authority. It began as a Stagewise fork and diverged into an independent AGPL-3.0 project, accepting hosted accounts, BYOK, OpenAI-compatible endpoints, or local Ollama. The project is an actively developed single-maintainer technical preview.
