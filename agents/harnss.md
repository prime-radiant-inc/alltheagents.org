---
name: "harnss"
slug: "harnss"
layout: "agent.njk"
category: "multiplexer"
maker: "OpenSource03"
license: "MIT"
url: "https://github.com/OpenSource03/harnss"
source_code_url: "https://github.com/OpenSource03/harnss"
source_available: "True"
platforms:
  - "CLI"
  - "IDE"
  - "Web"
  - "Desktop"
first_released: "2026-02-19"
current_release: "2026-08-10"
stars: "352"
language: "TypeScript"
homepage: "https://harnss.app"
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: "no"
subagents: "True"
hooks: "no"
plan_mode: "True"
model_providers: "Anthropic (Claude Code), OpenAI (Codex), ACP-compatible agents (Gemini CLI, Goose, Docker cagent)"
pricing: "Free/open-source (MIT)"
install_method: "Download latest release from GitHub Releases (.dmg macOS / .exe Windows / .AppImage+.deb Linux); or dev: git clone, pnpm install, pnpm dev"
docs_url: "https://harnss.app"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/OpenSource03/harnss/releases/latest"
maintained: "active"
sources:
  - "github_topic3"
what_makes_it_special: "Unified desktop interface for multiple AI coding agents built on the Agent Client Protocol (ACP), enabling simultaneous side-by-side agent sessions without context loss. Rich tool visualization transforms raw JSON into interactive cards with word-level diffs; all-in-one workspace with terminal, browser, git, MCP, and file panels scoped per project."
---

harnss is a desktop application for running several AI coding agents side by side without losing context between them. It embeds Claude Code through the Anthropic Agent SDK, Codex through its JSON-RPC app-server, and any Agent Client Protocol-compatible agent such as Gemini CLI, Goose, or Docker cagent, keeping each session's state independent while allowing instant switching. The interface renders tool calls in detail — word-level diffs, syntax-highlighted code, inline command output, nested subagent trees — and layers on MCP server management per project, git operations with AI-generated commit messages, built-in terminal tabs, and a browser panel. Permission handling offers three levels from ask-first to full autonomy, with plan mode and background task agents for longer work. The project is early-stage and open about a pending rewrite, distributing unsigned binaries for macOS, Windows, and Linux.
