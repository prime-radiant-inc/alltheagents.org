---
name: "terminal"
slug: "terminal"
layout: "agent.njk"
category: "agent"
maker: "bbarit"
license: null
url: "https://github.com/bbarit/terminal"
source_code_url: "https://github.com/bbarit/terminal"
source_available: "False"
platforms:
  - "CLI"
  - "IDE"
  - "Desktop"
first_released: "2026-04-15"
current_release: "2026-08-02"
stars: "33"
language: "Rust (backend), TypeScript/React 19 (frontend); Tauri v2"
homepage: "https://bbarit.com"
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: "n/a"
subagents: "True"
hooks: "True"
plan_mode: "True"
model_providers: "OpenAI, Anthropic, Google, Mistral, AWS Bedrock, Azure, Ollama, and more (37 providers / 1,000+ models)"
pricing: "Free with GitHub sign-in"
install_method: "Download latest release build for macOS or Windows; launch and sign in with GitHub. Auto-updates via Tauri updater."
docs_url: "https://bbarit.com"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/bbarit/terminal/releases/latest"
maintained: "active"
sources:
  - "github_deep"
what_makes_it_special: "Unified AI vibe-coding IDE: native terminal, code editor, and coding agent in one desktop app built 100% in Rust (Tauri). Broker Agent is a one-click autonomous AI dev<->review pair with a mechanical (zero-LLM-cost) broker mediating the full design->build->test->review->merge loop on isolated git worktrees. Keeps all projects and terminals on a single screen, runs multiple AI coding CLIs side by side in real PTYs, with an enforced verify loop (must run tests/build and pass before finishing). Includes built-in Monaco editor, Office file editors, SQLite, Chromium browser with AI toolbar, Kanban, Gantt, and remote access via web terminal."
---

BBARIT Terminal (formerly Octo Terminal, built by Tenmiles Inc.) collapses the terminal, the code editor, and the coding agent into one desktop application written entirely in Rust on Tauri. Its built-in agent works with an enforced verification loop — tests or builds must pass before a task can complete — alongside line-anchored safe edits, automatic rollback snapshots, and blocking of catastrophic commands, and a Broker Agent stages autonomous developer/reviewer pairs (for example Claude writing while Codex reviews) mediated by a deterministic, non-LLM broker that costs no tokens. The same screen hosts multiple real PTY terminals running other AI CLIs side by side (Claude Code, Codex, Gemini, Kimi, Qwen, OpenCode), a Monaco editor, git worktree panels with Kanban/Gantt views, an embedded Chromium browser, and remote access through a web terminal. MCP integration adds external tools, and 37 model providers (plus local Ollama) cover inference; GitHub sign-in suffices for the free app. Solo developers who want an all-in-one agentic workspace, particularly on Apple Silicon, are the audience.
