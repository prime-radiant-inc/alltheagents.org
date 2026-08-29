---
name: "ACP Client"
slug: "acp-client"
layout: "agent.njk"
category: "multiplexer"
maker: "Jun Han"
license: "MIT"
url: "https://marketplace.visualstudio.com/items?itemName=formulahendry.acp-client"
source_code_url: null
source_available: True
platforms:
  - "IDE"
first_released: "2026-02-08"
current_release: "2026-05-16"
stars: null
language: "TypeScript"
homepage: null
mcp_support: null
plugin_support: null
claude_code_plugin: null
subagents: null
hooks: null
plan_mode: null
model_providers: "agent CLIs: Copilot, Claude Code, Gemini CLI, Qwen Code, Auggie, Qoder, Codex CLI, OpenCode, OpenClaw, Kiro CLI, custom ACP agents"
pricing: "free"
install_method: "Install from the VS Code Marketplace"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://marketplace.visualstudio.com/items?itemName=formulahendry.acp-client"
maintained: "active"
sources:
  - "gap-2026-08-20"
what_makes_it_special: "Agent Client Protocol client connecting Copilot, Claude Code, Gemini CLI, Qwen Code, Codex CLI, OpenCode"
---

The Agent Client Protocol standardizes how editors talk to coding agents, but each editor needs a client implementation, and VS Code's built-in options leave gaps. ACP Client plugs the protocol into VS Code with 11 agents pre-configured — GitHub Copilot, Claude Code, Gemini CLI, Qwen Code, Codex CLI, OpenCode, Auggie, and more — plus support for custom agents over the same protocol. The chat panel renders markdown and reasoning, exposes mode and model pickers, handles file and terminal access with per-action permission management, and logs raw protocol traffic for debugging. With 27,000+ installs, it is one of the most-used ACP frontends, serving developers who switch among multiple agent CLIs.
