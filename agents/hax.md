---
name: "hax"
slug: "hax"
layout: "agent.njk"
category: "agent"
maker: "OleksandrChekhovskyi"
license: "MIT"
url: "https://github.com/OleksandrChekhovskyi/hax"
source_code_url: "https://github.com/OleksandrChekhovskyi/hax"
source_available: "True"
platforms:
  - "CLI"
first_released: "2026-04-24"
current_release: "2026-08-19"
stars: "262"
language: "C"
homepage: "https://usehax.dev"
mcp_support: "False"
plugin_support: "False"
claude_code_plugin: "False"
subagents: "False"
hooks: "False"
plan_mode: "False"
model_providers: "OpenAI (+compatible), Anthropic (+compatible), Codex (via ChatGPT subscription), OpenRouter, OpenCode Zen/Go, llama.cpp, Ollama, custom endpoints"
pricing: "Free / open-source"
install_method: "Homebrew: brew install oleksandrchekhovskyi/hax/hax; AUR (Arch Linux); prebuilt static binary from releases; or build from source (make)"
docs_url: null
plugin_docs_url: null
config_docs_url: "https://github.com/OleksandrChekhovskyi/hax/blob/master/docs/configuration.md"
download_url: "https://github.com/OleksandrChekhovskyi/hax/releases/latest"
maintained: "active"
sources:
  - "github_topic"
what_makes_it_special: "A minimalist, terminal-native coding agent written in C — single lightweight binary with small memory footprint, local models as first-class citizens, respects the terminal (preserves scrollback, no TUI takeover), fully inspectable transcripts, and uses Unix-style subprocess composition instead of plugins/MCP/IDE panels."
---

hax is a coding agent built as a single small C binary with minimal dependencies, aimed at developers who want agent capability without a heavyweight runtime. It supports interactive REPL, one-shot, and stdin-piped modes with session continuation and resume, and connects to OpenAI-compatible and Anthropic-compatible endpoints, OpenRouter, Codex subscriptions, and local llama.cpp or Ollama servers — with llama.cpp auto-discovery requiring no configuration. The interface respects the terminal it runs in: streaming Markdown reflows in place, tool output stays inline, and native scrollback is preserved rather than replaced. Config is plain text under XDG paths, transcripts are inspectable (Ctrl+T shows exactly what was sent and received), and capabilities extend through subprocess composition rather than a plugin system. It suits terminal-focused developers, local-model users, and environments where memory footprint and auditability matter.
