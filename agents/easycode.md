---
name: "EasyCode"
slug: "easycode"
layout: "agent.njk"
category: "agent"
maker: "OrionStarAI"
license: "Apache-2.0"
url: "https://github.com/OrionStarAI/EasyCode"
source_code_url: "https://github.com/OrionStarAI/EasyCode"
source_available: "True"
platforms: []
first_released: "2025-09-24"
current_release: "2026-06-17"
stars: "423"
language: "TypeScript"
homepage: "https://easycode.bot"
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: "True"
subagents: "True"
hooks: "True"
plan_mode: "True"
model_providers: "Google Gemini, OpenAI, OpenAI-compatible (Azure OpenAI, LM Studio, Ollama, Groq, Together AI), Anthropic Claude, custom OpenAI/Anthropic-compatible"
pricing: "open-source"
install_method: "npm install -g easycode-ai (also via yarn/pnpm), or build from source; VS Code extensions via .vsix installation"
docs_url: "https://github.com/OrionStarAI/EasyCode/tree/opensource/docs"
plugin_docs_url: null
config_docs_url: null
download_url: "https://www.npmjs.com/package/easycode-ai"
maintained: "active"
sources:
  - "github_deep"
what_makes_it_special: "Formerly DeepV Code; highly customizable AI coding assistant that understands entire project context, acts as an autonomous agent with Shell/File/Web tools, persistent session management, and serves as an ACP orchestrator that can delegate tasks to local Claude Code or Codex installations"
---

EasyCode (OrionStar, formerly DeepV Code) is a Claude Code-style terminal agent built in the open: it plans before editing via /plan, executes through built-in shell, filesystem, and web tools, and keeps sessions that can be saved, restored, and compressed. MCP servers provide project context and third-party tool access, a hooks mechanism injects custom logic at workflow nodes, and a self-hostable server variant lets teams run the backend themselves. Any OpenAI-compatible or Anthropic-format model works, including local Ollama or LM Studio endpoints, with costs paid directly to providers. It targets developers — particularly in the Chinese ecosystem — who want a customizable, self-hostable alternative to Claude Code or Codex.
