---
name: "Zellij"
slug: "zellij"
layout: "agent.njk"
category: "other"
maker: "zellij-org"
license: "MIT"
url: "https://github.com/zellij-org/zellij"
source_code_url: "https://github.com/zellij-org/zellij"
source_available: "True"
platforms:
  - "CLI"
first_released: "2020-09-01"
current_release: "2026-08-20"
stars: "35002"
language: "Rust"
homepage: "https://zellij.dev"
mcp_support: "no"
plugin_support: "True"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: null
pricing: "Free (open source)"
install_method: "OS package, prebuilt binary from GitHub releases, or cargo install --locked zellij"
docs_url: "https://zellij.dev/documentation/"
plugin_docs_url: "https://zellij.dev/documentation/plugin-api"
config_docs_url: "https://zellij.dev/documentation/configuration"
download_url: null
maintained: "active"
sources:
  - "user_reported"
what_makes_it_special: "Terminal workspace/multiplexer aimed at developers with layouts, floating and stacked panes, multiplayer collaboration, a built-in web-client, and a WebAssembly plugin system (plugins can be written in any language compiling to WASM). Not a coding agent harness; a terminal multiplexer. ~35k stars."
---

Zellij rebuilds the terminal multiplexer concept that tmux and GNU screen have held for decades around modern development habits. It ships friendly default keybindings with on-screen hints so new users are productive without reading documentation, supports layout files that recreate a multi-pane workspace on demand, and allows panes to float above or stack within the tiling grid. Its plugin system compiles to WebAssembly, so extensions written in Rust or any other WASM-targeting language run in a sandbox with a stable API instead of shelling out to arbitrary scripts. Two features go beyond what classic multiplexers offer: multiplayer sessions, where several people attach to the same workspace and interact collaboratively, and a built-in web client that exposes the session in a browser. Rust and Cargo-based build tooling keep the core self-contained, and distribution covers cargo install, prebuilt binaries, and OS packages. Developers running long-lived terminal sessions — including those hosting terminal coding agents — use it to organize panes, persist work across disconnects, and share sessions with teammates.
