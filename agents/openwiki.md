---
name: "OpenWiki"
slug: "openwiki"
layout: "agent.njk"
category: "other"
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
homepage: "https://github.com/langchain-ai/openwiki"
mcp_support: "yes (custom MCP connector — point at any MCP server and pull tools into a run; transport not specified)"
plugin_support: "yes (connectors: Notion, Slack, Gmail, X, Web Search, Hacker News, git-repo, LangSmith, Custom MCP)"
claude_code_plugin: "partial (generates/maintains CLAUDE.md at repo root for coding agent integration)"
subagents: "partial (uses Deep Agents framework; explicit subagent architecture not detailed)"
hooks: "no"
plan_mode: "no"
model_providers: "OpenAI, OpenAI (ChatGPT login), Anthropic, Gemini (AI Studio), Gemini Enterprise (Vertex AI), AWS Bedrock, GitHub Copilot, OpenRouter, Nebius, Fireworks, Baseten, NVIDIA NIM, OpenAI-compatible (LiteLLM, Ollama, LM Studio)"
pricing: "open-source (MIT), BYOK"
install_method: "npm"
docs_url: "https://github.com/langchain-ai/openwiki#readme"
plugin_docs_url: null
config_docs_url: "https://github.com/langchain-ai/openwiki#readme"
download_url: "https://www.npmjs.com/package/openwiki"
maintained: "active"
sources:
  - "brad"
what_makes_it_special: "CLI that uses AI agents to automatically write and maintain a Markdown wiki for your codebase or personal knowledge, keeping it current via CI on every change, with an interactive node-graph visualizer. Outputs portable Open Knowledge Format (OKF) bundles and supports 12+ model providers."
---

Codebase documentation decays faster than any other artifact, and agent-driven development accelerates the rot. OpenWiki, from the LangChain team, generates and maintains a linked Markdown wiki about a repository using a Deep Agents-powered pipeline: an init run plans and writes pages, and update runs diff the codebase against 'Grounded Claims' — statements tied to versioned source evidence — so the system knows precisely which facts went stale and rewrites only those pages. Scheduled CI workflows (GitHub Actions, GitLab, Bitbucket) keep the wiki current on every merge, and an interactive node-graph visualizer browses the result. Roughly nine connectors (Notion, Slack, Gmail, X, web search) extend sources, and integrations let Codex, Claude Code, OpenCode, or Cursor query the wiki as context. Install is npm -g with Node 22+, MIT-licensed, and 13 model providers are supported. Teams whose docs must survive heavy agent-driven churn are the audience.
