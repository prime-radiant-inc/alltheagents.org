---
name: "AetherStudio"
slug: "aetherstudio"
layout: "agent.njk"
category: "agent"
maker: "aetherstudio-cn"
license: "MIT"
url: "https://github.com/aetherstudio-cn/AetherStudio"
source_code_url: "https://github.com/aetherstudio-cn/AetherStudio"
source_available: "True"
platforms:
  - "IDE"
  - "Desktop"
first_released: "2026-06-22"
current_release: "2026-08-16"
stars: "87"
language: "Rust"
homepage: "https://aetherstudio.cn"
mcp_support: "False"
plugin_support: "True"
claude_code_plugin: "False"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "DeepSeek, Kimi"
pricing: "open-source"
install_method: "cargo build -p aether-win32 --bin aether-app --release"
docs_url: "https://aetherstudio.cn"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/aetherstudio-cn/AetherStudio"
maintained: "active"
sources:
  - "github_topic4"
what_makes_it_special: "Native Windows code editor built with Rust + Win32 API using Direct2D rendering and a Piece Table text buffer. Features multi-cursor editing, Tree-sitter, LSP/DAP, SSH remote development, ConPTY terminal, and CJK IME support. Includes an aether-plugin crate for plugin extensions and AI-assisted coding via DeepSeek/Kimi."
---

AetherStudio (牧羊人编辑器) starts from a performance complaint: Electron-based editors cost memory and input latency on Windows, so it renders with Direct2D/DirectWrite through the Win32 API in Rust, using a Piece Table buffer for multi-cursor editing at native speed. It is a complete editor rather than a demo — Tree-sitter highlighting, LSP and DAP clients, SSH remote development, ConPTY terminal, and CJK IME support for Chinese users. The AI layer integrates DeepSeek and Kimi presets for code explanation, rewriting, and inline suggestions, and can feed agent tool results back into the loop. Windows users who want native responsiveness with Chinese-market AI presets are the audience; the project is MIT-licensed and actively developed by Song Diyang.
