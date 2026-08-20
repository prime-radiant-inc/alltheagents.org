---
name: "Open Interpreter"
slug: "open-interpreter"
layout: "agent.njk"
category: "agent"
maker: "openinterpreter"
license: "Apache-2.0"
url: "https://github.com/openinterpreter/openinterpreter"
source_code_url: "https://github.com/openinterpreter/openinterpreter"
source_available: True
platforms:
  - "CLI"
first_released: "2023-07-14"
current_release: "2026-08-20"
stars: null
language: "Rust"
homepage: "http://openinterpreter.com/"
mcp_support: True
plugin_support: True
claude_code_plugin: null
subagents: null
hooks: True
plan_mode: null
model_providers: "Kimi K3, DeepSeek, Z.AI/GLM/ZCode, Qwen, Claude (via claude-code harness)"
pricing: "Free / open source (Apache-2.0)"
install_method: "curl -fsSL https://www.openinterpreter.com/install | sh (macOS/Linux), irm https://www.openinterpreter.com/install.ps1 | iex (Windows)"
docs_url: "https://www.openinterpreter.com/docs/terminal"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "jqueryscript"
  - "ishandutta"
what_makes_it_special: "Fork of OpenAI's Codex optimized for low-cost models. Features harness emulation (switch between native, claude-code, kimi-code, qwen-code, deepseek-tui, swe-agent harnesses via /harness), native sandboxing on all platforms, ACP agent mode, shared AGENTS.md and .agents/skills standards, and a QA skill for web/native app testing."
---

Fork of OpenAI's Codex optimized for low-cost models. Features harness emulation (switch between native, claude-code, kimi-code, qwen-code, deepseek-tui, swe-agent harnesses via /harness), native sandboxing on all platforms, ACP agent mode, shared AGENTS.md and .agents/skills standards, and a QA skill for web/native app testing.
