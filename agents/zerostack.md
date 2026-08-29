---
name: "zerostack"
slug: "zerostack"
layout: "agent.njk"
category: "agent"
maker: "gi-dellav"
license: "GPL-3.0-only"
url: "https://github.com/gi-dellav/zerostack"
source_code_url: "https://github.com/gi-dellav/zerostack"
source_available: "True"
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

zerostack began as an argument about budgets: if a coding agent mostly shells out and edits text, it should not need hundreds of megabytes of RAM. Written in Rust in roughly two weeks and inspired by pi and opencode, it delivers the standard agent toolbox — editing, execution, session management with auto-compaction, web fetch and search — in a 26MB binary that idles near zero CPU. The crossterm TUI renders markdown, supports mouse selection, and can display model reasoning inline. Capability is modular: MCP support, hooks, persistent memory, an advisor model for second opinions, multimodal input, ACP server mode for Zed, and sandboxing (bubblewrap on Linux, zerobox on macOS) are compile-time features a user includes or excludes, keeping the default binary lean. Behavior is shaped by switchable system-prompt modes (code, plan, review, debug, brainstorm, refactor) and a chaining mechanism that runs them in sequence, plus parallel git-worktree workflows for concurrent agent runs and a permission system with five modes, per-tool globs, and doom-loop detection. Hook compatibility with Claude Code's settings schema lets existing hook configurations carry over. Distributed under GPL-3.0 via install script, cargo, Homebrew, and Nix, it suits developers on constrained machines or those who want their agent's entire ~30k-line source readable.
