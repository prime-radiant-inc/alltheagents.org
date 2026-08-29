---
name: "Open-Webui-Tools"
slug: "open-webui-tools"
layout: "agent.njk"
category: "other"
maker: "Haervwe"
license: "MIT"
url: "https://github.com/Haervwe/open-webui-tools"
source_code_url: "https://github.com/Haervwe/open-webui-tools"
source_available: "True"
platforms:
  - "Web"
first_released: "2024-11-09"
current_release: "2026-08-19"
stars: "794"
language: "Python"
homepage: "https://openwebui.com/u/Haervwe"
mcp_support: "yes (Planner Agent v3 with MCP support, connection deduplication, parallelism patches)"
plugin_support: "n/a (is itself a collection of Open WebUI tools)"
claude_code_plugin: "no"
subagents: "yes (Planner Agent v3 specialized subagents: Web Search, Image Gen, Knowledge, Code Interpreter, Terminal)"
hooks: "no"
plan_mode: "yes (ENABLE_PLAN_APPROVAL pauses for user review before executing)"
model_providers: "Ollama, OpenAI, OpenRouter, MiniMax, Google Gemini/Veo, Hugging Face, Cloudflare Workers AI, Atlas Cloud"
pricing: "open-source"
install_method: "web (Open WebUI Hub or copy py files into Workspace)"
docs_url: "https://github.com/Haervwe/open-webui-tools#readme"
plugin_docs_url: null
config_docs_url: "https://github.com/Haervwe/open-webui-tools#readme"
download_url: "https://openwebui.com/u/Haervwe"
maintained: "active"
sources:
  - "jim"
what_makes_it_special: "Modular collection of 20+ tools, function pipes, and filters extending Open WebUI into an AI workstation. Standout is Planner Agent v3 — advanced autonomous agent with agentic planning, parallel subagent execution, MCP integration, visual execution tracking, interactive UI modals, and native Open WebUI integration. Covers research, creative generation (music/image/video), and smart routing (Semantic Router with dynamic vision re-routing)."
---

Open WebUI ships as a chat front end, and operators who self-host it often want search, media generation, and autonomous behavior without assembling each integration from scratch. This repository packages 20-plus components as Open WebUI's native tools, function pipes, and filters: search utilities (arXiv, Perplexica, SearxNG, SerpBase), image/video/music generation via ComfyUI, Hugging Face, and Google Veo, and utility filters such as a semantic router that picks the model automatically. The centerpiece, Planner Agent v3, is an autonomous pipe with agentic planning, dependency-aware task trees, parallel subagents for web search, image generation, RAG, code interpretation, and terminal work, an optional plan-approval gate, and MCP server support with connection deduplication. Installation is a click from the Open WebUI Community page or manual paste into the Workspace. Self-hosters of Open WebUI who want an AI workstation rather than a chat window are the audience, and most tools need third-party API keys.
