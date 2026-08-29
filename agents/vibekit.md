---
name: "VibeKit"
slug: "vibekit"
layout: "agent.njk"
category: "multiplexer"
maker: "superagent-ai"
license: "MIT"
url: "https://www.vibekit.sh"
source_code_url: "https://github.com/superagent-ai/vibekit"
source_available: "True"
platforms: []
first_released: "2025-05-14"
current_release: "2026-01-13"
stars: "1847"
language: "TypeScript"
homepage: "https://vibekit.sh"
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "Claude Code, Gemini CLI, Grok CLI, Codex CLI, OpenCode"
pricing: "Free / open-source"
install_method: "npm install -g vibekit (CLI); also @vibe-kit/sdk and @vibe-kit/auth packages"
docs_url: "https://docs.vibekit.sh"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/superagent-ai/vibekit"
maintained: "active"
sources:
  - "toolify"
what_makes_it_special: "Safety layer for coding agents - runs any coding agent in an isolated Docker sandbox with automatic redaction of secrets/API keys and full observability (real-time logs, traces, metrics). Universal agent support while working entirely offline with no cloud dependencies."
---

Handing a coding agent execution rights on a developer machine or in CI exposes credentials, lets it touch unrelated files, and leaves no audit trail. VibeKit addressed that by launching any supported agent — Claude Code, Gemini CLI, Codex, OpenCode, Grok CLI — inside disposable Docker containers, redacting API keys and secrets from traffic automatically, and streaming structured logs, traces, and metrics back to the host in real time. Because the sandbox layer was agent-agnostic, teams could adopt it for autonomous background tasks, CI automation, or running agents against untrusted code without changing which agent they used. The vibekit.sh site now returns 404 and the project shows no recent activity, so it appears abandoned and the tool is no longer available.
