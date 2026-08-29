---
name: "Superlog"
slug: "superlog"
layout: "agent.njk"
category: "agent"
maker: "superloglabs"
license: "Apache-2.0"
url: "https://superlog.sh"
source_code_url: "https://github.com/superloglabs/superlog"
source_available: "True"
platforms: []
first_released: "2026-06-02"
current_release: "2026-08-20"
stars: "1358"
language: "TypeScript"
homepage: "https://superlog.sh"
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: null
subagents: null
hooks: null
plan_mode: null
model_providers: null
pricing: "Free open-source community edition; Superlog Cloud with free tier, pay-to-go plan, and monthly credit packs"
install_method: "pnpm install, docker compose up -d, pnpm --filter @superlog/db db:migrate, pnpm dev (requires Node.js 20+, pnpm 9+, Docker); or npx skills add superloglabs/skills --all"
docs_url: "https://docs.superlog.sh"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/superloglabs/superlog"
maintained: "active"
sources:
  - "toolify"
what_makes_it_special: "Open-source agentic telemetry system that ingests traces, logs, and metrics, groups noisy signals into incidents, and uses AI agents to self-heal software. Local-first observability workspace for OpenTelemetry data with OTLP ingest proxy, ClickHouse-backed queries, and pluggable investigation runtimes. Y Combinator P26 company. MCP server listed (sh.superlog/superlog)."
---

Superlog collapses the path from production signal to code change. Telemetry flows in via OpenTelemetry or imports from Datadog, Sentry, AWS, GCP, Cloudflare, Vercel, Render, and Railway, where errors are fingerprinted into incidents with severity scoring and impact assessment instead of raw alert noise. For each incident, the Responder agent investigates using codebase context (including AGENTS.md/CLAUDE.md and connected Notion or Linear docs), prepares a resolution PR when its confidence gate passes, and otherwise posts findings to the responsible engineers; a memory system feeds PR comments and review outcomes back into future fixes. All telemetry — logs, traces, metrics, dashboards — is exposed over MCP so external agents can query it. The core is Apache-2.0 and local-first with a hosted cloud tier, and the company (Pulsent Labs) is Y Combinator-backed.
