---
name: "vibeproxy"
slug: "vibeproxy"
layout: "agent.njk"
category: "other"
maker: "automazeio"
license: "MIT"
url: "https://github.com/automazeio/vibeproxy"
source_code_url: "https://github.com/automazeio/vibeproxy"
source_available: "Yes"
platforms:
  - "Desktop"
first_released: "2025-10-04"
current_release: "2026-08-20"
stars: "3295"
language: "Swift"
homepage: "https://github.com/automazeio/vibeproxy"
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "n/a"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "Anthropic, OpenAI, Google, Moonshot, Alibaba, Z.AI, GitHub Copilot"
pricing: "free"
install_method: "binary"
docs_url: "https://github.com/automazeio/vibeproxy/blob/main/INSTALLATION.md"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/automazeio/vibeproxy/releases"
maintained: "active"
sources:
  - "github_topic3"
what_makes_it_special: "Native macOS menu bar app that lets you reuse existing AI subscriptions (Claude Code, Codex, Gemini, Kimi, Qwen, Z.AI GLM) with AI coding tools like Factory Droids by handling OAuth, token management, and API routing automatically."
---

Subscription plans for Claude, ChatGPT, Gemini, Kimi, Qwen, and GLM cost far less than API usage, but third-party coding tools cannot authenticate with a subscription — they expect API keys, so developers end up paying twice. VibeProxy closes that gap: a signed macOS menu-bar app runs a local proxy (built on CLIProxyAPIPlus) that performs each provider's OAuth flow, manages token refresh, and exposes the subscriptions as API-compatible endpoints that coding tools like Factory Droids or Amp CLI call as if they were ordinary APIs. Multiple accounts per provider rotate round-robin with rate-limit failover, provider priorities hot-reload, and a Vercel AI Gateway mode routes Claude traffic through a sanctioned gateway specifically to avoid account flags. macOS developers stretching their existing subscriptions across tools are the users; it is MIT-licensed, free, code-signed, and auto-updates via Sparkle.
