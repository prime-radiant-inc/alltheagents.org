---
name: "Speech-To-Code"
slug: "speech-to-code"
layout: "agent.njk"
category: "other"
maker: "dharllc"
license: "MIT"
url: "https://github.com/dharllc/speech-to-code"
source_code_url: "https://github.com/dharllc/speech-to-code"
source_available: "True"
platforms: []
first_released: "2024-08-09"
current_release: "2026-06-26"
stars: "1"
language: "JavaScript (frontend), Python (backend, FastAPI/uvicorn)"
homepage: null
mcp_support: "False"
plugin_support: "False"
claude_code_plugin: "False"
subagents: "False"
hooks: null
plan_mode: null
model_providers: "OpenAI, Anthropic, Google (Generative AI)"
pricing: "Free / open-source"
install_method: "git clone; chmod +x build.sh; ./build.sh (sets up Python venv, installs deps, creates .env files); start frontend (npm start) and backend (uvicorn main:app --reload) separately"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/dharllc/speech-to-code"
maintained: "dead"
sources:
  - "jim"
what_makes_it_special: "Web app that converts spoken language into executable code using LLMs; combines speech input, repository files, and manual text into a unified prompt composer. Uses LLM APIs directly to bypass rate limits/outages; includes cost tracking, system prompt management with versioning, and persistent chat sessions. Archived (read-only as of Jun 26, 2026)."
---

Speech-To-Code was built for developers who think faster than they type at a keyboard: a browser composer combines real-time speech-to-text, selectable repository files, and manual text into one prompt, then sends it straight to OpenAI, Anthropic, or Google APIs. Generated code is displayed for review and clipboard transfer rather than written back to disk, so the tool sits at the prompt-composition stage of development rather than acting on the repository. The FastAPI backend tracks spend per session, and system prompts are managed with versioning for reuse. The repository was archived read-only in June 2026 after 321 commits, so it remains available as a reference implementation of voice-driven LLM interaction rather than a maintained tool.
