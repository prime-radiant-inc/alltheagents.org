---
name: "OH-MY-PI"
slug: "oh-my-pi"
layout: "agent.njk"
category: "agent"
maker: "can1357"
license: "MIT"
url: "https://github.com/can1357/oh-my-pi"
source_code_url: "https://github.com/can1357/oh-my-pi"
source_available: "True"
platforms:
  - "CLI"
first_released: "2025-12-31"
current_release: "2026-08-19"
stars: null
language: "TypeScript, Rust"
homepage: "https://omp.sh"
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: "no"
subagents: "True"
hooks: "True"
plan_mode: "True"
model_providers: "60+ providers including Anthropic, OpenAI/Codex, Google Gemini/Vertex, xAI, DeepSeek, Mistral, Groq, Cerebras, Bedrock, Azure, OpenRouter, Ollama, LM Studio, vLLM, LiteLLM, Cursor, GitHub Copilot, GitLab Duo, Devin"
pricing: "Free / open source (MIT); users pay for their own API keys"
install_method: "curl -fsSL https://omp.sh/install | sh (macOS/Linux), brew install can1357/tap/omp, bun install -g @oh-my-pi/pi-coding-agent, nix run github:can1357/oh-my-pi, irm https://omp.sh/install.ps1 | iex (Windows), mise use -g github:can1357/oh-my-pi"
docs_url: "https://omp.sh"
plugin_docs_url: "https://omp.sh/docs/sdk"
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "jqueryscript"
  - "brad"
  - "ishandutta"
what_makes_it_special: "Coding agent with the IDE wired in. Features 31 built-in tools including LSP-integrated edits, real debugger driving (lldb/dlv/debugpy), persistent Python/JS execution cells, in-process shell, browser and desktop control, 23 web search backends, GitHub as filesystem, memory/learning, code review with verdicts, hash-anchored edits, AST-based edits, collaboration sessions, and time-traveling stream rules for hooks."
---

oh-my-pi is a fork of Mario Zechner's Pi rewritten as a coding-first agent with IDE-grade plumbing wired into a terminal interface. About 80,000 lines of Rust implement grep, shell, AST editing, and PTY handling in-process, eliminating fork/exec from the hot path. Every file write passes through LSP validation, and a debugger drives lldb, delve, and debugpy over DAP. A task tool fans out workspace-isolated subagents returning schema-validated results, and regex-triggered stream rules abort and retry mid-token for course correction. It inherits MCP servers, rules, and skills already on disk from eight other agent formats, so switching tools requires no migration. Ten model routing roles plus fallback chains cover sixty-plus providers.
