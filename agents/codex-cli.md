---
name: "Codex CLI"
slug: "codex-cli"
layout: "agent.njk"
category: "agent"
maker: "openai"
license: "Apache-2.0"
url: "https://github.com/openai/codex"
source_code_url: "https://github.com/openai/codex"
source_available: "True"
platforms:
  - "CLI"
first_released: "2025-04-13"
current_release: "2026-08-19"
stars: null
language: "Rust, TypeScript"
homepage: "https://developers.openai.com/codex"
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: null
subagents: "True"
hooks: "True"
plan_mode: "True"
model_providers: "OpenAI, Amazon Bedrock"
pricing: "Included in ChatGPT Plus/Pro/Business/Edu/Enterprise plans, or pay-as-you-go via OpenAI API key"
install_method: "curl -fsSL https://chatgpt.com/codex/install.sh | sh (macOS/Linux), npm install -g @openai/codex, brew install --cask codex, or download binaries from GitHub Releases"
docs_url: "https://developers.openai.com/codex"
plugin_docs_url: "https://developers.openai.com/codex/plugins"
config_docs_url: "https://developers.openai.com/codex/config-file"
download_url: null
maintained: "active"
sources:
  - "jqueryscript"
  - "brad"
  - "caramaschi"
  - "ishandutta"
  - "tiennm"
what_makes_it_special: "OpenAI's official coding agent that runs in the terminal with native sandboxing; can also integrate into VS Code, Cursor, and Windsurf. Supports MCP, plugins, hooks, subagents, and multiple execution modes."
---

Codex CLI is OpenAI's terminal coding agent, distributed as open source under Apache-2.0 with the core written in Rust. It runs locally with sandboxing around command execution and file edits, and offers approval modes from read-only through full autonomy. Authentication uses either a ChatGPT account (Plus, Pro, Business, Edu, or Enterprise) or an OpenAI API key, and the CLI connects to the same Codex ecosystem as the IDE extension and the cloud-based Codex Web at chatgpt.com/codex. The agent supports MCP servers, plugins, hooks, and subagents, with configuration documented at developers.openai.com/codex. It is installed via a curl script, npm (@openai/codex), Homebrew, or GitHub release binaries.
