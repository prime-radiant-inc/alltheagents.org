---
name: "interface"
slug: "interface"
layout: "agent.njk"
category: "multiplexer"
maker: "arctic-cli"
license: "MIT"
url: "https://github.com/arctic-cli/interface"
source_code_url: "https://github.com/arctic-cli/interface"
source_available: "True"
platforms:
  - "CLI"
  - "IDE"
first_released: "2025-12-25"
current_release: "2026-06-23"
stars: "145"
language: "TypeScript"
homepage: "https://usearctic.sh"
mcp_support: "True"
plugin_support: null
claude_code_plugin: "False"
subagents: null
hooks: null
plan_mode: null
model_providers: "OpenAI, Anthropic, Google, Perplexity, OpenRouter, Ollama"
pricing: "BYOK"
install_method: "curl -fsSL https://usearctic.sh/install | bash"
docs_url: "https://usearctic.sh/docs"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "github_topic3"
what_makes_it_special: "Multi-provider AI coding interface with real-time usage tracking, multiple accounts per provider (personal + work), switch models mid-conversation, imports existing Claude Code and OpenCode config (custom commands, agents, MCP servers)."
---

Arctic's premise is that heavy agent users juggle subscriptions: Claude here, Codex there, a work Copilot account, and no single view of what is left. The interface aggregates coding plans from ten providers (Claude Code, Codex, Gemini CLI, Antigravity, Copilot, Z.AI, Kimi, Amp, Qwen, MiniMax) alongside BYOK APIs (OpenAI, Anthropic, Google, Perplexity, OpenRouter, Ollama), tracking usage in real time and letting you switch models mid-conversation. Existing Claude Code and OpenCode setups import directly, so agents, slash commands, and MCP servers carry over without reconfiguration. Local-first storage keeps conversations on-device; an anonymous telemetry phase is opt-out. It targets developers juggling personal and work AI accounts across several agent subscriptions.
