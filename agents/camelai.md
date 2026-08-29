---
name: "camelAI"
slug: "camelai"
layout: "agent.njk"
category: "agent"
maker: "qaml-ai"
license: "MIT"
url: "https://github.com/qaml-ai/camelAI"
source_code_url: "https://github.com/qaml-ai/camelAI"
source_available: "True"
platforms:
  - "Web"
first_released: "2026-07-24"
current_release: "2026-08-19"
stars: "352"
language: "TypeScript"
homepage: "https://camelai.com"
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: null
subagents: null
hooks: null
plan_mode: null
model_providers: "Anthropic, OpenAI, OpenRouter, AWS Bedrock, custom endpoints"
pricing: "open-source"
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

camelAI is an open-source, full-stack AI app-building platform built entirely on Cloudflare's serverless primitives. Each conversation thread instantiates a Durable Object holding the agent loop and its state, while project files live across Durable Object SQLite and R2 storage with git history via Cloudflare Artifacts — no VMs or containers for the interactive loop. The custom agent harness, built on pi's agent libraries rather than Claude Code or Codex, generates JavaScript instead of shell commands; that code runs in fresh V8 isolates with credentials kept outside the execution sandbox, and applications publish to live URLs through Workers for Platforms. The platform also ships with organizational features (SSO, billing, usage metering), Slack and Discord bridges, and an eval harness, and it self-hosts via Docker Compose for teams that want the whole stack on their own infrastructure. It is MIT-licensed and under active development, targeting teams that want a self-hostable alternative to proprietary app builders.
