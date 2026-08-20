---
name: "zerostack"
slug: "zerostack"
layout: "agent.njk"
category: "agent"
maker: "gi-dellav"
license: "GPL-3.0-only"
url: "https://github.com/gi-dellav/zerostack"
source_code_url: "https://github.com/gi-dellav/zerostack"
source_available: True
platforms: []
first_released: "2026-05-12"
current_release: "2026-08-19"
stars: "1583"
language: "Rust"
homepage: "https://gi-dellav.github.io/zerostack/"
mcp_support: "yes - optional compile-time feature"
plugin_support: "no - custom prompts via Markdown files"
claude_code_plugin: "n/a - Claude Code hook-compatible settings.json schema; loads CLAUDE.md"
subagents: "yes - parallel/fast subagents for codebase exploration"
hooks: "yes - gated hooks feature; lifecycle hooks for tool calls, prompts, sessions; CC-compatible"
plan_mode: "yes - built-in /prompt modes including plan (planning-only)"
model_providers: "OpenRouter (default), OpenAI-compatible, Anthropic, Gemini, Ollama, custom providers"
pricing: "open-source"
install_method: "binary - install.sh, Cargo, Homebrew, or Nix"
docs_url: "https://github.com/gi-dellav/zerostack/blob/main/docs/GET_STARTED.md"
plugin_docs_url: null
config_docs_url: "https://github.com/gi-dellav/zerostack/blob/main/docs/CONFIG.md"
download_url: null
maintained: "active"
sources:
  - "github_topic"
what_makes_it_special: "Minimal high-performance Rust coding agent (~30k LoC, 26MB binary, ~16MB RAM, near-zero idle CPU) - dramatically smaller than JS-based agents like opencode (~300MB/700MB RAM). crossterm-based TUI with markdown rendering, mouse selection, reasoning visibility. Runtime-switchable system prompt modes (code, plan, review, debug, brainstorm). Prompt chaining (brainstorm -> plan -> code -> review). Claude Code hook compatibility. Gated features: persistent Markdown memory, advisor (second model for strategic guidance), ACP server (Zed), multimodal, sandbox (bubblewrap/zerobox), status signals over Unix sockets. Git worktrees with parallel agent workflows, loop system, five permission modes with per-tool globs and doom-loop detection."
---

Minimal high-performance Rust coding agent (~30k LoC, 26MB binary, ~16MB RAM, near-zero idle CPU) - dramatically smaller than JS-based agents like opencode (~300MB/700MB RAM). crossterm-based TUI with markdown rendering, mouse selection, reasoning visibility. Runtime-switchable system prompt modes (code, plan, review, debug, brainstorm). Prompt chaining (brainstorm -> plan -> code -> review). Claude Code hook compatibility. Gated features: persistent Markdown memory, advisor (second model for strategic guidance), ACP server (Zed), multimodal, sandbox (bubblewrap/zerobox), status signals over Unix sockets. Git worktrees with parallel agent workflows, loop system, five permission modes with per-tool globs and doom-loop detection.
