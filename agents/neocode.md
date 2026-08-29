---
name: "NeoCode"
slug: "neocode"
layout: "agent.njk"
category: "agent"
maker: "Hardik180704"
license: "MIT"
url: "https://github.com/Hardik180704/NeoCode"
source_code_url: "https://github.com/Hardik180704/NeoCode"
source_available: "True"
platforms:
  - "CLI"
  - "IDE"
first_released: "2026-06-04"
current_release: "2026-08-17"
stars: "45"
language: "TypeScript / JavaScript (Bun monorepo; Vite React landing page)"
homepage: "https://neocode.in"
mcp_support: "True"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "True"
hooks: "no"
plan_mode: "True"
model_providers: "Hosted NeoCode API (Railway-based, overridable via API_URL) with model selection via /models; specific providers not enumerated"
pricing: "freemium"
install_method: "Homebrew (brew install Hardik180704/tap/neocode), curl script for macOS/Linux, PowerShell script for Windows, or standalone binaries via GitHub Releases"
docs_url: "https://neocode.in"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/Hardik180704/NeoCode/releases"
maintained: "active"
sources:
  - "github_deep"
what_makes_it_special: "Open-source, terminal-native coding agent (IDE) keeping you in the terminal. NeoLens built-in local codebase explorer visualizes TypeScript dependency graphs, offers read-only file previews, and replays agent activity timelines (tokens, durations, costs) without sending source to cloud. PLAN mode (read-only investigation) and BUILD mode (implementation). MCP integrations via project-local .neocode/mcp.json (stdio and Streamable HTTP transports). Switchable plan/build agents via /agents command."
---

NeoCode targets developers who want an agentic coding loop without leaving the terminal. Sessions run through an OpenTUI interface with streaming responses, persistent re-openable sessions, and a strict separation between read-only PLAN mode and implementation BUILD mode. MCP servers are configured per project and denied by default: each tool gets an explicit read/write/disabled policy, and secrets are passed through environment references without leaving the server process. File contents never leave the machine — the hosted API receives only session activity, never code. The project is a Bun monorepo shipped as self-contained binaries bundling the Bun runtime, with Homebrew and installer-script distribution.
