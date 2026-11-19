---
name: "Lunar"
slug: "lunar"
layout: "agent.njk"
category: "agent"
maker: "gszr"
license: "MIT"
url: "https://github.com/gszr/lunar"
source_code_url: "https://github.com/gszr/lunar"
source_available: "True"
homepage: null
docs_url: "https://github.com/gszr/lunar/blob/main/docs/README.md"
download_url: null
install_method: "brew install --HEAD gszr/taps/lunar (homebrew tap, builds from source), or cargo install --git https://github.com/gszr/lunar"
platforms:
  - "CLI"
autonomy_level:
  - "agentic"
specialization: "general"
language: "Rust"
first_released: "2026-08-19"
current_release: "2026-11-05"
maintained: "active"
mcp_support: "False"
plugin_support: null
claude_code_plugin: null
subagents: "False"
hooks: null
plan_mode: "False"
plugin_docs_url: null
config_docs_url: "https://github.com/gszr/lunar/blob/main/docs/configuration.md"
model_providers: "xAI, OpenAI, Anthropic subscriptions via /login; any provider with an API key via Lua config (Chat Completions, OpenAI Responses, and Anthropic Messages formats)"
pricing: "free"
stars: "21"
sources:
  - "hackernews"
last_verified: "2026-11-19"
date_added: "2026-11-19"
what_makes_it_special: "A deliberately small Rust terminal coding harness — four tools (read, write, edit, run), no approval prompts, no plan modes, no sub-agents — where a Lua guest supplies all model and provider configuration, switchable mid-session without restarts."
---

Lunar is an open experimental coding harness by Guilherme Salazar, openly inspired by Pi and built around a two-part design: a Rust host owns the terminal, the model transport, and exactly four tools (read, write, edit, run), while a Lua guest supplies the model and provider configuration — aliases, API formats, context windows, thinking levels, and key commands — with project-level init.lua files overriding the user's, hot-reloadable through /config without a restart. The design philosophy is to keep nothing between you and the model: it deliberately does not impose plan modes, sub-agents, or approval prompts, and tools run without gating (the README says use it only in environments you trust). Missions are its unit of work: readable JSONL transcripts, resumable by name, date, or content, with /btw side questions kept out of the main context. Practical touches include /model for switching between xAI, OpenAI, and Anthropic subscriptions or any API-key provider mid-session, /request to export the next request as a curl command, /context for token-by-token inspection, stacks for naming related repositories so the model knows where to look, and an AGENTS.md/skills convention that loads instructions from disk rather than hiding them in a system prompt. It is early software for macOS and Linux, installed from a Homebrew tap or cargo, and suits developers who want a transparent harness they can configure in a few lines of Lua rather than adopt a workflow.
