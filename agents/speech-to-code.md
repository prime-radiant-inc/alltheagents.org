---
name: "Speech-To-Code"
slug: "speech-to-code"
layout: "agent.njk"
category: "agent"
maker: "dharllc"
license: "MIT"
url: "https://github.com/dharllc/speech-to-code"
source_code_url: "https://github.com/dharllc/speech-to-code"
source_available: True
platforms: []
first_released: "2024-08-09"
current_release: "2026-06-26"
stars: "1"
language: "JavaScript (frontend), Python (backend, FastAPI/uvicorn)"
homepage: null
mcp_support: False
plugin_support: False
claude_code_plugin: False
subagents: False
hooks: null
plan_mode: null
model_providers: "OpenAI, Anthropic, Google (Generative AI)"
pricing: "Free / open-source"
install_method: "git clone; chmod +x build.sh; ./build.sh (sets up Python venv, installs deps, creates .env files); start frontend (npm start) and backend (uvicorn main:app --reload) separately"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/dharllc/speech-to-code"
maintained: "archived"
sources:
  - "jim"
what_makes_it_special: "Web app that converts spoken language into executable code using LLMs; combines speech input, repository files, and manual text into a unified prompt composer. Uses LLM APIs directly to bypass rate limits/outages; includes cost tracking, system prompt management with versioning, and persistent chat sessions. Archived (read-only as of Jun 26, 2026)."
---

Web app that converts spoken language into executable code using LLMs; combines speech input, repository files, and manual text into a unified prompt composer. Uses LLM APIs directly to bypass rate limits/outages; includes cost tracking, system prompt management with versioning, and persistent chat sessions. Archived (read-only as of Jun 26, 2026).
