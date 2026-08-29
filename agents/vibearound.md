---
name: "VibeAround"
slug: "vibearound"
layout: "agent.njk"
category: "multiplexer"
maker: "jazzenchen"
license: "MIT"
url: "https://github.com/jazzenchen/VibeAround"
source_code_url: "https://github.com/jazzenchen/VibeAround"
source_available: "True"
platforms:
  - "CLI"
  - "IDE"
  - "Web"
first_released: "2026-02-23"
current_release: "2026-08-18"
stars: "520"
language: "Rust, TypeScript"
homepage: "https://vibearound.ai/"
mcp_support: "no"
plugin_support: "True"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "DeepSeek, Alibaba DashScope, Moonshot/Kimi, MiniMax, Xiaomi MiMo, xAI/Grok, NVIDIA NIM, Z.AI/GLM, Google Gemini, OpenRouter, Azure OpenAI"
pricing: "free"
install_method: "npm i @vibearound/cli  (or desktop app: macOS dmg, Windows exe/msi/zip, Linux AppImage/deb)"
docs_url: "https://github.com/jazzenchen/VibeAround/wiki"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/jazzenchen/VibeAround/releases"
maintained: "active"
sources:
  - "github_topic3"
what_makes_it_special: "All-in-one hub that launches multiple AI coding agents (Claude Code, Codex CLI, Gemini CLI, Pi, OpenCode, etc.) from a single UI with an API bridge that translates between incompatible provider protocols (OpenAI Responses, Chat Completions, Anthropic Messages, Gemini Generate Content). Enables session continuity across desktop/CLI/web/mobile/IM channels (Feishu, Discord, Slack, Telegram)."
---

VibeAround exists because the agent ecosystem fragmented: every CLI has its own config format and protocol, subscriptions overlap, and a session is trapped on the device where it started. The hub launches Claude Code, Codex, Gemini CLI, Pi, OpenCode, and desktop variants from one desktop/CLI/web surface with per-agent profiles, workspaces, and terminals, without modifying the agents' own configs. Its standalone API bridge translates between OpenAI Responses, Chat Completions, Anthropic Messages, and Gemini shapes — with model aliases, provider presets, and a live request recorder — and can expose local agents as OpenAI/Anthropic-compatible endpoints. Sessions continue across devices and IM channels (Feishu/Lark, Discord, Slack, Telegram, WeChat) via /pickup handover, with host-side web search injected when a provider lacks it. Individual developers running several agents — largely a single active maintainer's project — use it to keep subscriptions and sessions unified; it is MIT-licensed and local-first.
