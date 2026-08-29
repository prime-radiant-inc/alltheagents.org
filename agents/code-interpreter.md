---
name: "Code-Interpreter"
slug: "code-interpreter"
layout: "agent.njk"
category: "agent"
maker: "haseeb-heaven"
license: "Apache-2.0"
url: "https://github.com/haseeb-heaven/code-interpreter"
source_code_url: "https://github.com/haseeb-heaven/code-interpreter"
source_available: "True"
platforms:
  - "CLI"
first_released: "2023-10-06"
current_release: "2026-08-03"
stars: "279"
language: "TypeScript"
homepage: "https://www.npmjs.com/package/@haseeb_heaven/open-agent"
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: "True"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "OpenAI, Anthropic, Gemini, Groq, DeepSeek, NVIDIA, Together, HuggingFace, OpenRouter, Cerebras, Z.ai, Ollama, LM Studio"
pricing: "free"
install_method: "npm install -g @haseeb_heaven/open-agent"
docs_url: "https://github.com/haseeb-heaven/open-agent/blob/develop/docs/README.md"
plugin_docs_url: null
config_docs_url: "https://github.com/haseeb-heaven/open-agent/blob/develop/Models.MD"
download_url: "https://www.npmjs.com/package/@haseeb_heaven/open-agent"
maintained: "active"
sources:
  - "jim"
what_makes_it_special: "Open-source AI agent for the terminal. Describe a task in plain English and it plans, uses tools, and delivers. Free (OpenRouter free models), local (Ollama/LM Studio), and BYOK cloud models — no account required, no vendor lock-in. Cross-platform. Fork of Google's Gemini CLI."
---

The project packages an established agent loop as a zero-account terminal agent: --free mode runs on OpenRouter's free models, local Ollama or LM Studio setups need no key at all, and cloud providers connect through environment variables. On top of the Gemini CLI core it adds an extension marketplace, MCP server support, and a pluggable web-search layer spanning Exa, DuckDuckGo, Brave, Tavily, Serper, and Gemini grounding. A --yolo flag enables unattended execution in trusted workspaces. It suits cost-conscious users and people experimenting with local models who want a terminal agent without committing to a single vendor's account.
