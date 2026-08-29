---
name: "llama-vscode"
slug: "llama-vscode"
layout: "agent.njk"
category: "agent"
maker: "ggml.ai"
license: null
url: "https://marketplace.visualstudio.com/items?itemName=ggml-org.llama-vscode"
source_code_url: null
source_available: null
platforms:
  - "IDE"
first_released: "2025-01-21"
current_release: "2026-08-20"
stars: null
language: null
homepage: null
mcp_support: "True"
plugin_support: null
claude_code_plugin: null
subagents: null
hooks: null
plan_mode: null
model_providers: null
pricing: "free"
install_method: "Install from the VS Code Marketplace"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://marketplace.visualstudio.com/items?itemName=ggml-org.llama-vscode"
maintained: null
sources:
  - "gap-2026-08-20"
what_makes_it_special: "Local LLM-assisted code completion using llama.cpp"
---

The extension started as a local FIM completion client: it auto-installs llama.cpp, streams fill-in-the-middle suggestions from models such as Qwen2.5-Coder, and reuses a ring context of open and edited files so completion stays viable on CPU-only hardware. A later Llama Agent mode added a chat UI with nine built-in tools, MCP server tool support, custom JavaScript tools, and configurable loop counts, letting local models actually read and modify project files. Models load from ggml's Hugging Face presets or any local GGUF, and a Telegram bot interface plus deep links extend access beyond the editor. It targets developers who want editor AI without sending code to a cloud service; a sibling llama.vim plugin covers Vim and Neovim.
