---
name: "openHarness"
slug: "openharness"
layout: "agent.njk"
category: "agent"
maker: "zhijiewong"
license: "MIT"
url: "https://github.com/zhijiewong/openharness"
source_code_url: "https://github.com/zhijiewong/openharness"
source_available: True
platforms:
  - "CLI"
first_released: "2026-03-31"
current_release: "2026-05-12"
stars: "96"
language: "TypeScript"
homepage: "https://www.npmjs.com/package/@zhijiewang/openharness"
mcp_support: True
plugin_support: True
claude_code_plugin: False
subagents: True
hooks: True
plan_mode: True
model_providers: "Ollama, OpenAI, Anthropic, OpenRouter, llama.cpp, LM Studio"
pricing: "Free (MIT-licensed, BYOK for cloud models, free with Ollama locally)"
install_method: "npm install -g @zhijiewang/openharness"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "brad"
  - "ishandutta"
what_makes_it_special: "Works with ANY LLM via Ollama local models or cloud APIs (not locked to one provider); ~95% feature parity with Claude Code for CLI use; 44 tools and 80+ slash commands; auto git-commits every edit, reversible via /undo and /rewind; 27 hook event types configurable via .oh/config.yaml; full MCP server support (stdio + HTTP/SSE, OAuth 2.1); 11 specialized sub-agent roles; plan mode with read-only blocking; Cybergotchi companion pet; built-in evals system; ACP protocol support for editor integration; 7 permission modes with AST-based bash safety analysis."
---

Works with ANY LLM via Ollama local models or cloud APIs (not locked to one provider); ~95% feature parity with Claude Code for CLI use; 44 tools and 80+ slash commands; auto git-commits every edit, reversible via /undo and /rewind; 27 hook event types configurable via .oh/config.yaml; full MCP server support (stdio + HTTP/SSE, OAuth 2.1); 11 specialized sub-agent roles; plan mode with read-only blocking; Cybergotchi companion pet; built-in evals system; ACP protocol support for editor integration; 7 permission modes with AST-based bash safety analysis.
