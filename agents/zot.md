---
name: "Zot"
slug: "zot"
layout: "agent.njk"
category: "agent"
maker: "patriceckhart"
license: "MIT"
url: "https://zot.sh"
source_code_url: "https://github.com/patriceckhart/zot"
source_available: "Yes"
platforms:
  - "CLI"
first_released: "2026-04-17"
current_release: "2026-08-17"
stars: "319"
language: "Go"
homepage: "https://zot.sh"
mcp_support: "no"
plugin_support: "yes"
claude_code_plugin: null
subagents: "yes"
hooks: null
plan_mode: "no"
model_providers: null
pricing: "BYOK"
install_method: "curl -fsSL https://www.zot.sh/install.sh | bash (single static Go binary; also manual download from GitHub releases)"
docs_url: "https://zot.sh/docs"
plugin_docs_url: null
config_docs_url: null
download_url: "https://www.zot.sh/install.sh"
maintained: "active"
sources:
  - "hackernews"
what_makes_it_special: "A deliberately minimal terminal coding agent shipped as one static Go binary with a four-tool toolbox (read, write, edit, bash), no mandatory MCP, extensions in any language over subprocess JSON-RPC, and a Telegram bridge for driving the agent by direct message."
---

Zot is built as a counter-position to harness bloat: a terminal coding agent shipped as a single static Go binary with no runtime, no Docker, and no package manager — put it on the PATH and it works. Its tool set is deliberately the minimum viable set for a coding loop (read, write, edit, bash), a design stance the project maintains rather than grows past. Model access is nonetheless broad, with a unified catalog spanning Anthropic, OpenAI, Gemini, Bedrock, Azure, Ollama, llama.cpp, and roughly twenty other providers, plus custom entries through models.json. When four tools are not enough, extensions connect over JSON-RPC from any language, registering slash commands, tools, permission gates, and interactive panels — installed opt-in rather than bundled. Sessions can be resumed, forked, branched, compacted, and exported, background subagent loops run within the same repository, and an unusual Telegram bridge lets the agent be steered by direct message from a phone. The project is MIT-licensed, hosted on GitHub, and self-described as in beta indefinitely; the harness itself is free with users paying provider API costs shown per model in the UI. Its audience is developers who want a small, inspectable harness they can carry as one binary rather than a platform.
