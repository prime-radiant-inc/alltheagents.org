---
name: "Smelt"
slug: "smelt"
layout: "agent.njk"
category: "agent"
maker: "leonardcser"
license: "MIT"
url: "https://github.com/leonardcser/smelt"
source_code_url: "https://github.com/leonardcser/smelt"
source_available: "True"
platforms:
  - "CLI"
  - "IDE"
  - "Autonomous"
first_released: "2026-02-25"
current_release: "2026-08-18"
stars: "39"
language: "Rust"
homepage: "https://leonardcser.github.io/smelt/"
mcp_support: null
plugin_support: "True"
claude_code_plugin: null
subagents: null
hooks: null
plan_mode: "True"
model_providers: "OpenAI, Anthropic, OpenRouter, Ollama, GitHub Copilot, Kimi Code"
pricing: "open-source"
install_method: "Prebuilt binaries from GitHub Releases or cargo install --git https://github.com/leonardcser/smelt.git smelt-agent"
docs_url: "https://leonardcser.github.io/smelt/"
plugin_docs_url: "https://leonardcser.github.io/smelt/"
config_docs_url: "https://leonardcser.github.io/smelt/"
download_url: "https://github.com/leonardcser/smelt/releases"
maintained: "active"
sources:
  - "brad"
  - "ishandutta"
what_makes_it_special: "Small, fast, Lua-scriptable AI coding agent for the terminal (scriptable like Neovim). Custom terminal renderer (not ratatui). Built-in Vim editor (motions, text objects, registers, undo). Deterministic fuzzing with fixed clock and stubbed I/O for replayable crashes. No config needed. Mode cycle: Normal -> Plan -> Apply -> Yolo."
---

Smelt exists because its author found mainstream coding agents bloated and wanted the extensibility model of Neovim applied to an agent: keymaps, commands, autocmds, custom tools, and modes are all defined in Lua, with bundled plugins for which-key, an LSP-backed semantic code toolset, and a local request inspector. The Rust core uses a custom grid renderer, ships a built-in Vim editor with motions, text objects, registers, and undo, and cycles through Normal, Plan, Apply, and Yolo modes. Development is tested with deterministic fuzzing — stubbed I/O, fixed clocks, replayable failures — rather than ad hoc integration tests. Authentication covers subscription providers (ChatGPT, GitHub Copilot, Kimi Code) alongside any OpenAI-compatible endpoint, and the README warns that interfaces shift between alpha releases.
