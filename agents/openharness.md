---
name: "openHarness"
slug: "openharness"
layout: "agent.njk"
category: "agent"
maker: "zhijiewong"
license: "MIT"
url: "https://github.com/zhijiewong/openharness"
source_code_url: "https://github.com/zhijiewong/openharness"
source_available: "True"
platforms:
  - "CLI"
first_released: "2026-03-31"
current_release: "2026-05-12"
stars: "96"
language: "TypeScript"
homepage: "https://www.npmjs.com/package/@zhijiewang/openharness"
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: "False"
subagents: "True"
hooks: "True"
plan_mode: "True"
model_providers: "Ollama, OpenAI, Anthropic, OpenRouter, llama.cpp, LM Studio"
pricing: "Free (MIT-licensed, BYOK for cloud models, free with Ollama locally)"
install_method: "npm install -g @zhijiewang/openharness"
docs_url: "https://github.com/zhijiewong/openharness/blob/main/docs/hooks.md"
plugin_docs_url: null
config_docs_url: "https://github.com/zhijiewong/openharness/blob/main/docs/mcp-servers.md"
download_url: "https://www.npmjs.com/package/@zhijiewong/openharness"
maintained: "active"
sources:
  - "brad"
  - "ishandutta"
what_makes_it_special: "Works with ANY LLM via Ollama local models or cloud APIs (not locked to one provider); ~95% feature parity with Claude Code for CLI use; 44 tools and 80+ slash commands; auto git-commits every edit, reversible via /undo and /rewind; 27 hook event types configurable via .oh/config.yaml; full MCP server support (stdio + HTTP/SSE, OAuth 2.1); 11 specialized sub-agent roles; plan mode with read-only blocking; Cybergotchi companion pet; built-in evals system; ACP protocol support for editor integration; 7 permission modes with AST-based bash safety analysis."
---

Claude Code's terminal workflow is compelling but locks users to Anthropic models and accounts, and local-model users have no equivalent harness. OpenHarness reimplements that surface as a Node CLI called oh: 44 built-in tools, 80-plus slash commands, MCP server support, 27 hook events, permission modes, checkpoints with rewind, sub-agents, and a headless mode for CI/CD with a --max-budget-usd cost cap. Providers include Ollama (auto-detected, no key needed), OpenAI, Anthropic, OpenRouter, llama.cpp/GGUF, and LM Studio, so the same harness runs free on local models or BYOK in the cloud. Distribution covers npm plus official Python and TypeScript SDKs and a VS Code extension, and the repo publishes SWE-bench-Lite evaluations alongside its benchmarks. The project is small (96 stars) but actively developed with 1,502 passing tests. Developers who want the Claude Code interaction model on their own provider mix — especially local models — are the audience.
