---
name: "Paseo"
slug: "paseo"
layout: "agent.njk"
category: "multiplexer"
maker: "getpaseo"
license: "AGPL-3.0"
url: "https://github.com/getpaseo/paseo"
source_code_url: "https://github.com/getpaseo/paseo"
source_available: "Yes"
platforms:
  - "CLI"
first_released: "2025-10-13"
current_release: "2026-08-19"
stars: "14355"
language: "TypeScript"
homepage: "https://paseo.sh"
mcp_support: "yes (packages/server includes an MCP server; transport not specified)"
plugin_support: "partial (plugin-examples/ directory; skills system for extensibility)"
claude_code_plugin: "yes (.claude/skills/ directory; Claude Code is a supported agent)"
subagents: "yes (/paseo-advisor and /paseo-committee skills spin up additional agents)"
hooks: "no"
plan_mode: "no"
model_providers: "Claude Code, Codex, GitHub Copilot, OpenCode, Pi"
pricing: "open-source (AGPL-3.0)"
install_method: "npm"
docs_url: "https://paseo.sh/docs"
plugin_docs_url: null
config_docs_url: "https://paseo.sh/docs/configuration"
download_url: "https://paseo.sh/download"
maintained: "active"
sources:
  - "author_search"
what_makes_it_special: "Self-hosted, privacy-first orchestration platform providing a single interface across multiple AI coding agents (Claude Code, Codex, Copilot, OpenCode, Pi), enabling parallel agent execution on your own machine with cross-device control via desktop, mobile, web, and CLI."
---

Paseo exists because coding agents strand work in a single terminal on a single machine: sessions die when the laptop closes and there is no way to supervise several agents at once. Its self-hosted daemon runs Claude Code, Codex, GitHub Copilot, OpenCode, and Pi locally with the user's own credentials, exposing them through desktop, web, mobile, and CLI clients, with agents running in parallel and handoff skills that pass work between them or convene advisor and committee agents for review. The design is deliberately privacy-first: no telemetry, no forced accounts, and an E2E-encrypted relay only for pairing remote devices. The server package includes an MCP server and a TypeScript SDK for integrations, and a skills system extends orchestration. With 15k+ GitHub stars and multilingual documentation, it draws individual developers and small teams who want local control over multi-agent workflows.
