---
name: "Open Interpreter"
slug: "open-interpreter"
layout: "agent.njk"
category: "agent"
maker: "openinterpreter"
license: "Apache-2.0"
url: "https://github.com/openinterpreter/openinterpreter"
source_code_url: "https://github.com/openinterpreter/openinterpreter"
source_available: "True"
platforms:
  - "CLI"
first_released: "2023-07-14"
current_release: "2026-08-20"
stars: null
language: "Rust"
homepage: "http://openinterpreter.com/"
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: "no"
subagents: "no"
hooks: "True"
plan_mode: "no"
model_providers: "Kimi K3, DeepSeek, Z.AI/GLM/ZCode, Qwen, Claude (via claude-code harness)"
pricing: "Free / open source (Apache-2.0)"
install_method: "curl -fsSL https://www.openinterpreter.com/install | sh (macOS/Linux), irm https://www.openinterpreter.com/install.ps1 | iex (Windows)"
docs_url: "https://www.openinterpreter.com/docs/terminal"
plugin_docs_url: "https://www.openinterpreter.com/docs/terminal"
config_docs_url: "https://www.openinterpreter.com/docs/terminal"
download_url: "https://www.openinterpreter.com/install"
maintained: "active"
sources:
  - "jqueryscript"
  - "ishandutta"
what_makes_it_special: "Fork of OpenAI's Codex optimized for low-cost models. Features harness emulation (switch between native, claude-code, kimi-code, qwen-code, deepseek-tui, swe-agent harnesses via /harness), native sandboxing on all platforms, ACP agent mode, shared AGENTS.md and .agents/skills standards, and a QA skill for web/native app testing."
---

Cheap and open-weight models underperform in agent harnesses tuned for frontier models, and the gap is often the harness rather than the model. Open Interpreter, a Rust rewrite of OpenAI's Codex with about 68,000 GitHub stars, addresses this by emulating provider-recommended harnesses: /harness switches between native, claude-code, kimi-code, qwen-code, deepseek-tui, swe-agent, and minimal modes, so a cheap model runs under the prompting and tool-calling conventions it was trained against. It supports MCP, skills, hooks, permissions, and AGENTS.md, remains compatible with the Codex SDK through a one-line binary override, and speaks ACP, while a built-in QA skill drives browsers and native applications for computer-use tasks. Installation is a curl script on macOS/Linux or PowerShell on Windows, and the tool is free with BYOK model access. Developers running low-cost models who want frontier-harness behavior without paying frontier prices are its audience.
