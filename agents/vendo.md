---
name: "Vendo"
slug: "vendo"
layout: "agent.njk"
category: "agent-sdk"
maker: "runvendo"
license: "Apache-2.0"
url: "https://github.com/runvendo/vendo"
source_code_url: "https://github.com/runvendo/vendo"
source_available: "True"
platforms:
  - "Web"
first_released: "2026-06-30"
current_release: null
stars: 590
language: "TypeScript"
homepage: "https://vendo.run"
mcp_support: "yes"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "any AI SDK LanguageModel"
pricing: "free"
install_method: "npm packages (@vendoai/vendo) in a pnpm monorepo; PGlite by default, Postgres in production; deployable on Railway"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://www.npmjs.com/package/@vendoai/vendo"
maintained: "active"
sources:
  - "hackernews"
what_makes_it_special: "An embedded agent SDK for B2B SaaS that lets your end customers build their own features and micro-apps on top of your product: agents execute through the host product's own API as the signed-in user, build live views from the host's components, remix the UI in place, and create standing automations — all without touching the host's source code."
---

Vendo is a YC-backed open-source layer for B2B SaaS teams that want to give their customers in-product customization without shipping a plugin platform of their own. The embedded agent executes through the host product's own API as the signed-in user, so permissions and data boundaries come from the product itself: users ask questions and get live views composed from the host's components, hover a UI element and describe a change to remix it in place, and turn plain-language instructions into standing automations with per-tool approvals. Safety controls include policy enforcement, grants, circuit breakers, and audit logging, with generated UI running in a sandboxed iframe. For developers it is a TypeScript SDK compatible with any AI SDK LanguageModel, integrating with Claude Code, Cursor, Copilot, and MCP clients during development, self-hostable with PGlite or Postgres and optional Vendo Cloud features via API key.
