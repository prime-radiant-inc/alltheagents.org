---
name: "singulary"
slug: "singulary"
layout: "agent.njk"
category: "agent"
maker: "sammwyy"
license: "MIT"
url: "https://github.com/sammwyy/singulary"
source_code_url: "https://github.com/sammwyy/singulary"
source_available: "True"
platforms: []
first_released: "2026-05-24"
current_release: "2026-05-25"
stars: "49"
language: "TypeScript"
homepage: null
mcp_support: "False"
plugin_support: "False"
claude_code_plugin: "False"
subagents: "False"
hooks: "False"
plan_mode: "False"
model_providers: "OpenAI, Anthropic, OpenRouter, Groq, Google, xAI, DeepSeek, OpenAI-compatible (Ollama, LM Studio)"
pricing: "Free / open-source (MIT); BYOK, no token markup"
install_method: "git clone + cp .env.example .env + docker compose up --build; or pnpm install + pnpm dev for local dev (Node >=22, pnpm 9)"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "github_final"
what_makes_it_special: "Open-source self-hosted FOSS alternative to v0/Lovable/Bolt/Replit Agent; agent reads/writes/patches files, runs shell commands, and provisions services inside isolated Docker workspaces with built-in Monaco editor, interactive terminals, live preview, multi-user support, and encrypted secrets at rest."
---

Singulary replicates the v0/Lovable/Bolt workflow — prompt, get a running web app, iterate — but on the operator's own hardware with their own API keys and no SaaS backend or telemetry. Each project runs in an isolated Docker container and network where the agent edits files, installs dependencies, restarts dev servers, and asks approval before dangerous calls, with a Monaco editor, interactive terminals, and live preview with automatic port detection in the browser. The whole stack is a single Node process with SQLite, deployable with one docker compose up, and secrets are AES-GCM encrypted at rest. Being very early (a handful of commits), it lacks snapshots and quota enforcement at call time, both on the roadmap. It targets teams and self-hosters who want an app-builder platform they control, and the Docker socket mount warrants rootless-Docker hardening before exposure.
