---
name: "Amplifier Agent"
slug: "amplifier-agent"
layout: "agent.njk"
category: "agent"
maker: "microsoft"
license: "MIT"
url: "https://github.com/microsoft/amplifier-agent"
source_code_url: "https://github.com/microsoft/amplifier-agent"
source_available: True
platforms:
  - "CLI"
first_released: "2026-05-18"
current_release: "2026-08-19"
stars: "7"
language: "TypeScript, Python"
homepage: null
mcp_support: True
plugin_support: True
claude_code_plugin: null
subagents: True
hooks: null
plan_mode: null
model_providers: "Anthropic, OpenAI, Azure OpenAI, Ollama, GitHub Copilot, ChatGPT (OAuth), Chat Completions (OpenAI-compatible), Gemini, vLLM"
pricing: null
install_method: "curl -fsSL https://raw.githubusercontent.com/microsoft/amplifier-agent/main/install.sh | bash (requires uv, curl, git)"
docs_url: "https://github.com/microsoft/amplifier-agent/tree/main/docs"
plugin_docs_url: null
config_docs_url: "https://github.com/microsoft/amplifier-agent/blob/main/docs/CONFIGURATION.md"
download_url: "https://www.npmjs.com/package/amplifier-agent-ts"
maintained: "active"
sources:
  - "user_reported"
what_makes_it_special: "Agent engine that other software runs on — give it a prompt and it runs the full loop with tools, sub-agents, skills, and MCP, returning a result. Anything that can spawn a subprocess can use it (shell scripts, Node apps, Python services, chat bots, IDE plugins). Python apps can also embed the engine in-process. Skills system with role-based model routing for sub-agents."
---

Agent engine that other software runs on — give it a prompt and it runs the full loop with tools, sub-agents, skills, and MCP, returning a result. Anything that can spawn a subprocess can use it (shell scripts, Node apps, Python services, chat bots, IDE plugins). Python apps can also embed the engine in-process. Skills system with role-based model routing for sub-agents.
