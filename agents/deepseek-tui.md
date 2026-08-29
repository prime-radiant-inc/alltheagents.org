---
name: "DeepSeek-TUI"
slug: "deepseek-tui"
layout: "agent.njk"
category: "agent"
maker: "Independent"
license: "MIT"
url: "https://github.com/deepseek-tui/deepseek-tui"
source_code_url: "https://github.com/deepseek-tui/deepseek-tui"
source_available: "True"
platforms:
  - "CLI"
first_released: "2025"
current_release: "2026"
stars: null
language: "Rust"
homepage: null
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: "False"
subagents: "True"
hooks: null
plan_mode: "True"
model_providers: "DeepSeek (default), NVIDIA NIM, Fireworks, SGLang, vLLM"
pricing: "deepseek-v4-pro: $0.003625/1M cache hit, $0.435/1M cache miss, $0.87/1M output; deepseek-v4-flash: $0.0028/1M input, $0.14/1M cache miss, $0.28/1M output (75% discount until May 31 2026)"
install_method: "Download prebuilt binaries from GitHub Releases (.7z for Windows x64, .dmg for macOS ARM64)"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/DeepSeek-TUI-app/DeepSeek-TUI/releases"
maintained: "active"
sources:
  - "web_search_multilingual"
what_makes_it_special: "Terminal coding agent for DeepSeek V4 models. Streams reasoning blocks, edits local workspaces with approval gates, reads/edits files, runs shell commands, searches the web, manages git, and coordinates sub-agents. Includes auto mode that selects model and thinking level per turn. Has Plan (read-only investigation), Agent, and YOLO modes. MCP support and a Skills system for composable, installable instruction packs from GitHub. Note: the original source_code_url (github.com/deepseek-tui/deepseek-tui) 404s; actual repo is github.com/DeepSeek-TUI-app/DeepSeek-TUI."
---

deepseek-tui was a terminal coding agent built around DeepSeek V4 models: it streamed the models' reasoning blocks into the terminal, edited local workspaces behind approval gates, ran shell commands, searched the web, managed git, and coordinated subagents from a TUI. The project attracted an ecosystem — a Homebrew tap, Windows install tutorials, desktop re-implementations, and DeepSeek Harness TUI distributions such as seektty and cocode — indicating real adoption at its peak. The canonical repository at github.com/deepseek-tui/deepseek-tui now returns 404, confirmed via GitHub's API, so the original source is no longer available. Users who want comparable tooling must rely on the surviving fork/companion projects, which complicates provenance and security review.
