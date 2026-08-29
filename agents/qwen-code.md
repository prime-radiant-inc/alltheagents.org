---
name: "Qwen Code"
slug: "qwen-code"
layout: "agent.njk"
category: "agent"
maker: "QwenLM"
license: "Apache-2.0"
url: "https://github.com/QwenLM/qwen-code"
source_code_url: "https://github.com/QwenLM/qwen-code"
source_available: "True"
platforms:
  - "CLI"
first_released: "2025-06-26"
current_release: "2026-08-20"
stars: null
language: "TypeScript"
homepage: "https://qwenlm.github.io/qwen-code-docs/en/users/overview"
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: "no"
subagents: "True"
hooks: "True"
plan_mode: "True"
model_providers: "OpenAI, Anthropic, Gemini, Qwen APIs, any third-party provider or local model (Ollama/vLLM)"
pricing: "Free / open source"
install_method: "Standalone install scripts (Linux/macOS/Windows), npm install -g @qwen-code/qwen-code@latest (requires Node.js 22+), brew install qwen-code"
docs_url: "https://qwenlm.github.io/qwen-code-docs/en/users/overview"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "jqueryscript"
  - "brad"
  - "ishandutta"
  - "tiennm"
what_makes_it_special: "Feature-rich agentic coding assistant with auto-memory, auto-skills, subagents, agent teams, MCP support, plan mode, hooks, LSP integration, Git worktrees, and computer use for desktop automation. Multiple interaction modes: interactive terminal UI, headless mode, IDE plugins (VS Code, JetBrains, Zed), desktop app, daemon mode, and IM bot channels."
---

Qwen Code is Alibaba's open-source terminal coding agent, forked from Gemini CLI v0.8.2 and developed independently since, with the explicit goal of matching Claude Code's capabilities while running on any model provider. It supports subagents, hooks, plan mode, MCP, skills, and agent teams, with providers — OpenAI, Anthropic, Gemini, Qwen, or local Ollama/vLLM models — switchable at runtime rather than fixed at install. The project extends beyond the terminal into IDE plugins, a desktop app, SDKs, a daemon mode exposing a shared agent session over HTTP+SSE, and IM bots for Telegram, DingTalk, WeChat, and Feishu. Its development is partly self-referential: the team runs its own agent to file issues, submit pull requests, review code, and run tests on the codebase itself. An Agent Arena runs multiple models head-to-head on the same task, and headless mode supports CI pipelines. Developers who want a Claude Code-shaped tool without vendor lock-in use it across Qwen and non-Qwen models alike.
