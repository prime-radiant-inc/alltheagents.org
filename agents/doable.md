---
name: "Doable"
slug: "doable"
layout: "agent.njk"
category: "agent"
maker: "doable-me"
license: "MIT"
url: "https://github.com/doable-me/Doable"
source_code_url: "https://github.com/doable-me/Doable"
source_available: "True"
platforms:
  - "IDE"
first_released: "2026-03-14"
current_release: "2026-07-21"
stars: "24"
language: "TypeScript"
homepage: "https://doable.me"
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: "False"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "Anthropic, OpenAI, Google Gemini, Groq, Mistral, DeepSeek, xAI, Ollama, LM Studio, vLLM, OpenRouter, Moonshot, Alibaba, Baidu, any OpenAI-compatible endpoint"
pricing: "Free (MIT, self-hosted); per-workspace plan tiers: Free / Pro / Business / Enterprise"
install_method: "git clone + ./deployment/docker/setup.sh (Docker); local dev via pnpm install; one-click deploy to DigitalOcean/Render/Railway/Heroku/Codespaces; doable Rust CLI for provisioning"
docs_url: "https://docs.doable.me"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/doable-me/Doable"
maintained: "active"
sources:
  - "github_final"
what_makes_it_special: "Fully self-hostable and air-gappable multi-tenant AI app builder with row-level security isolation, sandboxed code execution (per-project Linux UIDs, seccomp, egress firewall), audit logs, MFA, RBAC, real-time collaboration, BYOK for 53+ AI providers, and 630+ integrations — all MIT-licensed and owned by you."
---

Doable rebuilds the AI app-builder stack — the Lovable/Bolt category — for operators who cannot send code or data to a hosted service. A describe-and-preview loop generates frontend, in-process backend, and database per tenant, with each project sandboxed under its own Linux UID, seccomp profile, and egress firewall, and audit logs covering the run. Administration is product surface, not ops: a five-step setup wizard covers AI provider (BYOK from 53+ providers), Cloudflare DNS, and plan quotas, and row-level security isolates tenants on shared hardware. It is aimed at teams and regulated organizations that want a self-hostable builder on their own VPS or PaaS.
