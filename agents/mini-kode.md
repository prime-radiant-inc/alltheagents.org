---
name: "Mini-Kode"
slug: "mini-kode"
layout: "agent.njk"
category: "agent"
maker: "minmaxflow"
license: "MIT"
url: "https://github.com/minmaxflow/mini-kode"
source_code_url: "https://github.com/minmaxflow/mini-kode"
source_available: "True"
platforms:
  - "CLI"
first_released: "2025-10-30"
current_release: "2025-11-04"
stars: "305"
language: "TypeScript"
homepage: null
mcp_support: "True"
plugin_support: null
claude_code_plugin: null
subagents: "False"
hooks: null
plan_mode: null
model_providers: "OpenAI-compatible APIs including DeepSeek, GLM (Zhipu), any OpenAI-compatible via custom base URL"
pricing: "Free/open-source (MIT)"
install_method: "npm install -g mini-kode; set MINIKODE_API_KEY/MINIKODE_BASE_URL/MINIKODE_MODEL env vars; run mini-kode"
docs_url: "https://github.com/minmaxflow/mini-kode/blob/master/docs/README.md"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/minmaxflow/mini-kode"
maintained: "active"
sources:
  - "brad"
  - "ishandutta"
what_makes_it_special: "Educational AI coding agent CLI (~14K lines of production code) purpose-built for learning how modern coding agents work internally - a manageable scale between toy demos and production behemoths. Clean architecture with comprehensive comments, streaming responses, human-in-the-loop permission approval, unified tool system, and a modern React/Ink terminal UI."
---

Mini-Kode addresses the learning gap between toy agents (a few hundred lines) and production harnesses too large to read: at roughly fourteen thousand lines of TypeScript it is a working agent whose internals can actually be studied. The loop streams from any OpenAI-compatible endpoint (DeepSeek and GLM verified in the README), dispatches a unified tool system for files, search, and command execution behind two-layer permission approval, and reads AGENTS.md at startup for persistent project conventions — mirroring the conventions-file pattern of production agents. Architecture is deliberately legible: separate modules for tools, permissions, LLM, sessions, and UI, written for readers rather than throughput, with a DeepWiki walkthrough accompanying the code. A roadmap of session persistence, subagents, and context caching marks the gaps between it and production harnesses. Developers use it to learn how coding agents are assembled and as a base for their own experiments rather than for daily production work.
