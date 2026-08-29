---
name: "multiplayer"
slug: "multiplayer"
layout: "agent.njk"
category: "agent"
maker: "multiplayer-app"
license: "MIT"
url: "https://github.com/multiplayer-app/multiplayer"
source_code_url: "https://github.com/multiplayer-app/multiplayer"
source_available: "True"
platforms: []
first_released: "2026-06-17"
current_release: "2026-08-18"
stars: "38"
language: "JavaScript, TypeScript (Node.js, pnpm/Turborepo monorepo)"
homepage: "https://www.multiplayer.app/"
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: "False"
subagents: null
hooks: null
plan_mode: null
model_providers: "Claude Code (GA), Codex (private beta), Copilot (private beta)"
pricing: "open-source"
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

Multiplayer attacks the weakest input to AI debugging: coding agents fix production bugs poorly because they see stack traces, not the unsampled full-stack session data — request and response bodies, headers, cross-service correlation — that APM tools sample away. The platform runs locally alongside a coding agent, captures complete session data through recorder SDKs spanning JavaScript, React Native, Go, .NET, Python, Ruby, and Java, and auto-correlates the traces across components. Its triage layer filters for high-priority bugs and deduplicates identical errors, so a recurring exception produces one merge-ready pull request rather than a flood of duplicates; the loop runs from error capture through agent prompting to PR creation and notification. The self-hostable stack (MongoDB, Kafka, ClickHouse, Redis, MinIO) deploys via Docker Compose, and a companion CLI provides a terminal surface for reviewing sessions and turning fixes into branches. Teams running Claude Code against production incidents are the target users; the project is young, with a small commit history and adoption still forming.
