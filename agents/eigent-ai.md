---
name: "Eigent AI"
slug: "eigent-ai"
layout: "agent.njk"
category: "agent"
maker: "Eigent"
license: "Apache-2.0"
url: "https://eigent.ai"
source_code_url: "https://github.com/eigent-ai/eigent"
source_available: "True"
platforms:
  - "CLI"
  - "Web"
first_released: "2024"
current_release: "2026"
stars: null
language: "TypeScript, Python"
homepage: "https://eigent.ai"
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: null
subagents: "True"
hooks: null
plan_mode: null
model_providers: "Model Agnostic (cloud APIs, vLLM, Ollama, LM Studio)"
pricing: "Open source (free); cloud and enterprise plans available"
install_method: "git clone + npm install + npm run dev (requires Node.js 18-22); or download desktop app"
docs_url: "https://docs.eigent.ai"
plugin_docs_url: null
config_docs_url: null
download_url: "https://eigent.ai"
maintained: "active"
sources:
  - "web_search_multilingual"
what_makes_it_special: "100% open-source, local-first desktop multi-agent cowork app built on CAMEL-AI's framework. Combines single-agent harness with multi-agent workforce coordination (parallel specialized agents that divide work & collaborate), MCP integration, skill integration, built-in browser & terminal toolkits, model agnosticism, and full data privacy."
---

Eigent came out of the CAMEL-AI ecosystem to give people who cannot or will not route work through a cloud assistant a local alternative: a desktop app where a prompt is decomposed across an agent pool rather than answered by one model. Single-agent mode provides one CAMEL Agent with file, terminal, screenshot, and search toolkits; Workforce mode registers specialized agents that divide and execute tasks concurrently, with an execution context tracking which skills, MCP servers, and referenced files each task used. Model access is agnostic — cloud APIs, enterprise gateways, or local models via BYOK — and scheduled-task automation adds recurring workflows with trigger configuration, execution logs, and success-rate statistics. Non-technical operators use it for multi-step computer work, and enterprises can self-host the same stack on their own infrastructure.
