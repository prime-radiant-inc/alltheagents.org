---
name: "VSCode Agent"
slug: "vscode-agent"
layout: "agent.njk"
category: "agent"
maker: "Microsoft"
license: "Proprietary (VS Code is MIT-licensed but Copilot/agent features require subscription)"
url: "https://code.visualstudio.com/agent"
source_code_url: null
source_available: "True"
platforms:
  - "IDE"
first_released: "2025"
current_release: "2026"
stars: null
language: "TypeScript"
homepage: "https://code.visualstudio.com/docs"
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: "False"
subagents: "True"
hooks: "True"
plan_mode: "True"
model_providers: "GitHub Copilot models (Claude, GPT-4, Gemini, and others)"
pricing: "Included with GitHub Copilot subscription"
install_method: "Built into VS Code / VS Code Insiders; requires GitHub Copilot subscription"
docs_url: "https://code.visualstudio.com/docs/copilot/chat/chat-agent-mode"
plugin_docs_url: "https://code.visualstudio.com/docs/agent-customization/agent-plugins"
config_docs_url: "https://code.visualstudio.com/docs/copilot/chat/chat-agent-mode"
download_url: "https://code.visualstudio.com"
maintained: "active"
sources:
  - "web_search_multilingual"
what_makes_it_special: "Built-in agent-first experience in VS Code with dedicated Agents window, multiple chat surfaces (Agents window, Chat view, inline chat, Quick Chat). Full MCP support, plugin system, subagents, hooks, and plan mode. Agents can autonomously analyze code, make changes, run terminal commands, and use tools. Backed by GitHub Copilot's multi-model provider system."
---

VS Code evolved from an editor with AI completions into an agent-first harness: a dedicated Agents window hosts autonomous sessions where agents analyze code, edit files, run terminal commands, and use tools, while chat also remains available inline and through Quick Chat. The harness supports MCP servers for external tools, a plugin system for packaging agents, subagents, lifecycle hooks, and plan mode for reviewing multi-step work before execution. Because agents run inside the editor with workspace context, they can analyze code, apply edits, and run terminal commands without leaving the surface. It targets VS Code's large installed base, from individual developers to enterprise teams already using GitHub Copilot or BYO MCP endpoints.
