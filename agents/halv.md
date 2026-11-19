---
name: "Halv"
slug: "halv"
layout: "agent.njk"
category: "multiplexer"
maker: "halv-ai"
license: "Apache-2.0"
url: "https://github.com/halv-ai/halv"
source_code_url: "https://github.com/halv-ai/halv"
source_available: "True"
homepage: "https://halv.ai"
docs_url: "https://github.com/halv-ai/halv/blob/main/README.md"
download_url: "https://halv.ai/download/"
install_method: "Download the installer from halv.ai/download/ or the GitHub releases (macOS dmg aarch64/x64, Windows msi, Linux deb/rpm/AppImage); the app updates itself. Build from source with pnpm and the Rust toolchain (pnpm install, pnpm fetch:rtk, pnpm fetch:crux, pnpm build:supervisor, pnpm tauri dev)"
platforms:
  - "Desktop"
autonomy_level:
  - "agentic"
specialization: "general"
language: "Rust"
first_released: "2026-10-20"
current_release: "2026-11-04"
maintained: "active"
mcp_support: "True"
plugin_support: null
claude_code_plugin: null
subagents: "True"
hooks: "False"
plan_mode: null
plugin_docs_url: null
config_docs_url: null
model_providers: "delegates to the connected agent CLIs (Claude Code, Codex, Kimi, GLM) on the user's own subscriptions; optional OpenAI API key in native chat mode"
pricing: "freemium"
stars: "5"
sources:
  - "hackernews"
last_verified: "2026-11-19"
date_added: "2026-11-19"
what_makes_it_special: "A desktop workspace for Claude Code, Codex, Kimi, and GLM that routes every request through a local Headroom context-compression proxy and shows the estimated dollars saved at API prices, alongside a Crux code index, command-output filtering, a local OS sandbox, per-project approvals, and turn diff/revert."
---

Halv is a Tauri desktop app (macOS, Windows, Linux) built by Pedro Villaca and a small team around a simple pitch: coding agents are expensive because they ship huge contexts, so it runs a local Headroom proxy between the agents and their providers that compresses prompts and responses, then shows the estimated savings on a live meter. On top of that proxy it gives the agent CLIs it runs — Claude Code, Codex, Kimi, and GLM, on the subscriptions you already pay for — up to 32 panes of native terminals with subagent fan-out, per-project approvals, a local OS sandbox, and turn-level diff and revert. Two more local layers cut context further: Crux, a code index that answers caller/reference/impact questions instead of file-by-file reads (also shipped standalone as an MIT MCP server), and RTK, which filters command output before it reaches the agent. The optional US$10/month Halv Cloud plan runs on the maker's servers: JEV routing that rates each task brief to pick a lane, model, and effort tier, a cross-machine savings dashboard, and automatic rotation across Claude accounts when one plan's usage window fills. Developers who spend on multiple agent subscriptions and want to watch and cut that spend are the audience.
