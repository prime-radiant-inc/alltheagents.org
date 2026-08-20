---
name: "camelAI"
slug: "camelai"
layout: "agent.njk"
category: "agent"
maker: "qaml-ai"
license: "MIT"
url: "https://github.com/qaml-ai/camelAI"
source_code_url: "https://github.com/qaml-ai/camelAI"
source_available: True
platforms:
  - "Web"
first_released: "2026-07-24"
current_release: "2026-08-19"
stars: "352"
language: "TypeScript"
homepage: null
mcp_support: True
plugin_support: True
claude_code_plugin: null
subagents: null
hooks: null
plan_mode: null
model_providers: "Anthropic, OpenAI, OpenRouter, AWS Bedrock, custom endpoints"
pricing: null
install_method: "git clone; bun install --frozen-lockfile; cp .dev.vars.example .dev.vars; bun run dev (requires Node.js 22+, Bun, Cloudflare account, Docker)"
docs_url: "https://camelai.com"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/qaml-ai/camelAI"
maintained: "active"
sources:
  - "github_deep"
what_makes_it_special: "Each chat thread runs its own coding agent in a Cloudflare Durable Object (not a VM) for persistent state without container overhead. Custom agent harness (not Claude Code or Codex) that writes JavaScript instead of bash, runs it in fresh V8 isolates, and keeps credentials outside the execution sandbox. Publishes user apps directly to live URLs via Workers for Platforms."
---

Each chat thread runs its own coding agent in a Cloudflare Durable Object (not a VM) for persistent state without container overhead. Custom agent harness (not Claude Code or Codex) that writes JavaScript instead of bash, runs it in fresh V8 isolates, and keeps credentials outside the execution sandbox. Publishes user apps directly to live URLs via Workers for Platforms.
