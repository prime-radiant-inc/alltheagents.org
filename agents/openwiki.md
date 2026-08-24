---
name: "OpenWiki"
slug: "openwiki"
layout: "agent.njk"
category: tool
maker: "langchain-ai"
license: "MIT"
url: "https://github.com/langchain-ai/openwiki"
source_code_url: "https://github.com/langchain-ai/openwiki"
source_available: "Yes"
platforms:
  - "CLI"
  - "IDE"
first_released: "2026-06-22"
current_release: "2026-08-20"
stars: "15364"
language: "TypeScript"
homepage: null
mcp_support: "yes (custom MCP connector — point at any MCP server and pull tools into a run; transport not specified)"
plugin_support: "yes (connectors: Notion, Slack, Gmail, X, Web Search, Hacker News, git-repo, LangSmith, Custom MCP)"
claude_code_plugin: "partial (generates/maintains CLAUDE.md at repo root for coding agent integration)"
subagents: "partial (uses Deep Agents framework; explicit subagent architecture not detailed)"
hooks: null
plan_mode: null
model_providers: "OpenAI, OpenAI (ChatGPT login), Anthropic, Gemini (AI Studio), Gemini Enterprise (Vertex AI), AWS Bedrock, GitHub Copilot, OpenRouter, Nebius, Fireworks, Baseten, NVIDIA NIM, OpenAI-compatible (LiteLLM, Ollama, LM Studio)"
pricing: "open-source (MIT), BYOK"
install_method: "npm"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://www.npmjs.com/package/openwiki"
maintained: "active"
sources:
  - "brad"
what_makes_it_special: "CLI that uses AI agents to automatically write and maintain a Markdown wiki for your codebase or personal knowledge, keeping it current via CI on every change, with an interactive node-graph visualizer. Outputs portable Open Knowledge Format (OKF) bundles and supports 12+ model providers."
---

CLI that uses AI agents to automatically write and maintain a Markdown wiki for your codebase or personal knowledge, keeping it current via CI on every change, with an interactive node-graph visualizer. Outputs portable Open Knowledge Format (OKF) bundles and supports 12+ model providers.
