---
name: "InsForge"
slug: "insforge"
layout: "agent.njk"
category: "other"
maker: "InsForge"
license: "Apache-2.0"
url: "https://github.com/InsForge/InsForge"
source_code_url: "https://github.com/InsForge/InsForge"
source_available: "Yes"
platforms: []
first_released: "2025-07-29"
current_release: "2026-08-20"
stars: "12751"
language: "TypeScript/JavaScript (Next.js, Deno for edge functions)"
homepage: "https://insforge.dev"
mcp_support: "yes (MCP server, both self-hosted and cloud; likely stdio)"
plugin_support: "yes (CLI + Skills system; .claude/skills and .codex/skills directories)"
claude_code_plugin: "yes (.claude-plugin directory and CLAUDE_PLUGIN.md present)"
subagents: null
hooks: null
plan_mode: null
model_providers: "multiple LLM providers via OpenAI-compatible Model Gateway"
pricing: "open-source (Apache-2.0); cloud-hosted option at insforge.dev (freemium)"
install_method: "docker"
docs_url: "https://docs.insforge.dev/introduction"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "github_topic"
what_makes_it_special: "All-in-one open-source backend platform designed specifically for agentic coding, providing AI coding agents with database, auth, storage, compute, hosting, and an AI gateway through MCP server and CLI+Skills interfaces, enabling agents to operate the backend like backend engineers."
---

InsForge inverts the usual relationship between coding agents and backends: instead of the agent writing Supabase glue code, the backend exposes itself as MCP tools and CLI skills the agent calls directly — run migrations, deploy edge functions, create buckets, configure auth, fetch logs. Postgres with pgvector, OAuth-ready auth, S3-compatible storage, Deno edge functions, and an OpenAI-compatible model gateway cover the full-stack surface, and self-hosting is one curl script plus Docker Compose, with Railway, Zeabur, and Sealos templates for one-click deploys. Teams building with Claude Code or Codex use it to let the agent operate infrastructure like a backend engineer rather than generating boilerplate against a foreign API.
