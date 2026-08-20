---
name: "multiplayer"
slug: "multiplayer"
layout: "agent.njk"
category: "agent"
maker: "multiplayer-app"
license: "MIT"
url: "https://github.com/multiplayer-app/multiplayer"
source_code_url: "https://github.com/multiplayer-app/multiplayer"
source_available: True
platforms: []
first_released: "2026-06-17"
current_release: "2026-08-18"
stars: "38"
language: "JavaScript, TypeScript (Node.js, pnpm/Turborepo monorepo)"
homepage: "https://www.multiplayer.app/"
mcp_support: True
plugin_support: True
claude_code_plugin: False
subagents: null
hooks: null
plan_mode: null
model_providers: "Claude Code (GA), Codex (private beta), Copilot (private beta)"
pricing: null
install_method: "Docker Compose (recommended): cp .env.example docker/.env, edit credentials, docker compose -f docker/docker-compose.prod.yml up -d. Requires Node v22+, pnpm v10+, Docker. Local dev: pnpm install; cp .env.example .env; docker compose -f docker/docker-compose.dev.yml up -d; pnpm start:pm2"
docs_url: "https://www.multiplayer.app/docs"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/multiplayer-app/multiplayer"
maintained: "active"
sources:
  - "github_topic5"
what_makes_it_special: "Open-source debugging agent that runs locally alongside coding agents and bridges them directly to production runtime data; captures deep, unsampled full-stack session data (including request/response bodies and headers that APMs miss); intelligently deduplicates identical errors to produce one merge-ready fix instead of duplicate PRs; provides session recorder SDKs for JavaScript, React Native, Go, .NET, Python, Ruby, and Java."
---

Open-source debugging agent that runs locally alongside coding agents and bridges them directly to production runtime data; captures deep, unsampled full-stack session data (including request/response bodies and headers that APMs miss); intelligently deduplicates identical errors to produce one merge-ready fix instead of duplicate PRs; provides session recorder SDKs for JavaScript, React Native, Go, .NET, Python, Ruby, and Java.
