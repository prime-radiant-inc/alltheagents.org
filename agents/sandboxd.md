---
name: "sandboxd"
slug: "sandboxd"
layout: "agent.njk"
category: "multiplexer"
maker: "tastyeffectco"
license: "MIT"
url: "https://github.com/tastyeffectco/sandboxd"
source_code_url: "https://github.com/tastyeffectco/sandboxd"
source_available: "True"
platforms: []
first_released: "2026-06-03"
current_release: "2026-08-19"
stars: "910"
language: "Go"
homepage: "https://sandboxd.io/"
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "OpenCode, Claude Code"
pricing: "open-source"
install_method: "docker"
docs_url: "https://sandboxd.io"
plugin_docs_url: null
config_docs_url: "https://sandboxd.io/reference/configuration"
download_url: null
maintained: "active"
sources:
  - "github_final"
what_makes_it_special: "Self-hosted AI app builder with deliberately minimal architecture (one Go binary + Docker + Traefik + SQLite); sleep/wake sandboxes so idle apps cost nothing; credential isolation via proxy injection (API keys never enter sandboxes); 80+ curated one-click open-source apps."
---

sandboxd is the self-hosted answer to Lovable-style app builders: an operator runs one binary on a VPS, and users prompt a coding agent that works inside an isolated container per app, exposed at a preview URL. Each app sleeps when idle and wakes on request, keeping idle cost at zero, while tasks are checkpointed so any agent mistake can be reverted. Beyond generated apps it curates more than eighty one-click apps (n8n, Ghost, Grafana, Gitea, Jupyter, Keycloak) and runtime presets for React, Next.js, Express, FastAPI, and Workers. Everything is a versioned /v1 REST call, so the browser console is just one client. It is MIT-licensed and beta (0.x) with container-level isolation and API auth off by default, aimed at developers who want an app-builder platform under their own domain rather than a SaaS.
