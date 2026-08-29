---
name: "project-os-for-codex"
slug: "project-os-for-codex"
layout: "agent.njk"
category: "multiplexer"
maker: "herry2059"
license: "Apache-2.0"
url: "https://github.com/herry2059/project-os-for-codex"
source_code_url: "https://github.com/herry2059/project-os-for-codex"
source_available: "True"
platforms: []
first_released: "2026-07-09"
current_release: "2026-07-14"
stars: "101"
language: "TypeScript, React, Node.js"
homepage: null
mcp_support: "True"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "AI provider adapter (replaceable boundary); OpenAI Codex CLI / ChatGPT"
pricing: "Free / open source"
install_method: "docker compose up --build (recommended) or manual pnpm install + pnpm dev; requires Node.js 22+, pnpm 9+, Git"
docs_url: "https://github.com/herry2059/project-os-for-codex/tree/main/docs"
plugin_docs_url: null
config_docs_url: "https://github.com/herry2059/project-os-for-codex/tree/main/docs"
download_url: "https://github.com/herry2059/project-os-for-codex"
maintained: "active"
sources:
  - "agent_infra"
what_makes_it_special: "Git-as-durable-project-record design; fail-closed MCP preflight with strict two-tool surface; short-lived (24h/7d) project-bound credentials instead of password sharing; handoff packages readable by humans and AI; built from real delivery experience (14,570 Codex tasks, 8.8B tokens); not affiliated with OpenAI"
---

Project OS for Codex exists because handing a coding agent a long-running project usually means sharing passwords, losing context between sessions, and having no auditable record of what the agent actually did. It provides a web dashboard plus a strict two-tool MCP server: one tool returns the current kickoff card, acceptance criteria, and handoff package, and the other appends one validated, idempotent progress event with an agent-reported verification note and a matching commit in a separate record repository. A fail-closed preflight verifies the credential, project binding, and exact tool surface before Codex starts, and high-risk operations like key management or deployment are deliberately kept outside the MCP surface for humans. Handoffs use short-lived, scope-limited credentials — 24-hour or 7-day expiry — instead of shared passwords, with everything hashed and independently revocable. Solo developers running Codex on multi-session projects use it to keep work auditable and handoff-safe.
