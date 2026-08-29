---
name: "antigravity-jules-orchestration"
slug: "antigravity-jules-orchestration"
layout: "agent.njk"
category: "other"
maker: "Scarmonit"
license: "MIT"
url: "https://github.com/Scarmonit/antigravity-jules-orchestration"
source_code_url: "https://github.com/Scarmonit/antigravity-jules-orchestration"
source_available: "True"
platforms:
  - "Autonomous"
first_released: "2025-11-30"
current_release: "2026-04-01"
stars: "41"
language: "JavaScript"
homepage: null
mcp_support: "True"
plugin_support: null
claude_code_plugin: null
subagents: "True"
hooks: null
plan_mode: "True"
model_providers: "Jules API, Google Antigravity, Ollama"
pricing: null
install_method: "git clone, npm install, configure .env, npm run dev"
docs_url: "https://github.com/Scarmonit/antigravity-jules-orchestration"
plugin_docs_url: null
config_docs_url: "https://github.com/Scarmonit/antigravity-jules-orchestration"
download_url: "https://github.com/Scarmonit/antigravity-jules-orchestration"
maintained: "active"
sources:
  - "agent_infra"
what_makes_it_special: "Autonomous AI orchestration architecture combining Google Antigravity browser automation with the Jules API for hands-free development. 65 MCP tools across Jules Core API, Session Management, Templates, Batch Processing, Analytics, RAG, Semantic Memory, Render Integration, and Suggested Tasks. Browser Subagent for DOM capture, screenshots, and video recording. Semantic memory and batch processing."
---

The project exists because Antigravity's browser automation and Jules' autonomous coding sessions don't compose natively: this Node.js MCP server (Streamable HTTP, port 3323) exposes Jules core API, session management, templates, cloning, PR integration, queueing, batch processing, analytics, and Render deployment as tool families that Antigravity can orchestrate. Supporting machinery includes AES-256-GCM encrypted credential storage, LRU caching, circuit breakers with retry/backoff, and GitHub-issue-to-Jules-session automation. It requires Node 18+, a Jules API key, and both Google products installed; deployment targets Docker or Render (live at scarmonit.com). Version 2.6.x added auto-fix and semantic-memory tools; 42 stars and an active changelog mark it as a working personal automation layer rather than a community project.
