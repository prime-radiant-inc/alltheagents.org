---
name: "lumnicode"
slug: "lumnicode"
layout: "agent.njk"
category: "agent"
maker: "martian56"
license: "MIT"
url: "https://github.com/martian56/lumnicode"
source_code_url: "https://github.com/martian56/lumnicode"
source_available: "True"
platforms:
  - "IDE"
  - "Web"
first_released: "2025-09-25"
current_release: "2026-04-16"
stars: "55"
language: "Python, TypeScript"
homepage: "https://lumnicode.ufazien.com"
mcp_support: "False"
plugin_support: "False"
claude_code_plugin: "False"
subagents: "False"
hooks: "False"
plan_mode: "no"
model_providers: "OpenAI, Anthropic, Google Gemini, Groq, Together, Fireworks, Cohere"
pricing: "Free / open-source; BYOK (you pay your own API usage)"
install_method: "git clone + docker-compose for PostgreSQL/MinIO + backend uv sync/uvicorn + frontend npm install/dev"
docs_url: "https://github.com/martian56/lumnicode/wiki"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "dormant"
sources:
  - "github_topic4"
what_makes_it_special: "Free web-based BYOK AI code editor/generator using Monaco editor with LangGraph orchestration pipeline (plan->config->generate->finalize) for AI project generation and S3-compatible file storage."
---

Lumnicode packages a self-hosted alternative to subscription AI editors: operators deploy it against PostgreSQL and any S3-compatible store (MinIO in development), and users bring their own provider keys, which the backend calls directly so costs track usage and no code or keys are pooled. Project generation runs through a LangGraph state machine - plan the file structure, generate configuration, write source files to S3, finalize - with per-node progress streamed over WebSocket into the editor. For existing code, a Cmd+K palette handles explain, refactor, completion, bug-finding, and test generation. Individual developers and small teams who want editor AI without per-seat pricing or vendor lock-in are the audience.
