---
name: "qwengate"
slug: "qwengate"
layout: "agent.njk"
category: "other"
maker: "youssefvdel"
license: "MIT"
url: "https://github.com/youssefvdel/qwengate"
source_code_url: "https://github.com/youssefvdel/qwengate"
source_available: "True"
platforms:
  - "CLI"
  - "IDE"
first_released: "2026-05-22"
current_release: "2026-08-14"
stars: "162"
language: "TypeScript"
homepage: "https://github.com/youssefvdel/qwen-gate"
mcp_support: "no"
plugin_support: null
claude_code_plugin: null
subagents: null
hooks: null
plan_mode: null
model_providers: "Qwen (qwen3-7-max, qwen3-6-plus, qwen3-max, qwen3-coder, qwen3-5-plus, qwen3-5-flash, and more, via chat.qwen.ai automation)"
pricing: "Free/self-hosted (uses free Qwen chat accounts)"
install_method: "curl -sSL https://raw.githubusercontent.com/youssefvdel/qwen-gate/main/install.sh | bash (Linux/macOS); PowerShell script (Windows); or manual git clone + bun install"
docs_url: "https://github.com/youssefvdel/qwengate/blob/dev/docs/"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/youssefvdel/qwen-gate"
maintained: "active"
sources:
  - "github_topic2"
what_makes_it_special: "Self-hosted OpenAI-compatible API gateway providing free access to Qwen models via browser automation of chat.qwen.ai; multi-account rotation, session pooling, streaming SSE, tool calling parsed from text, and a real-time web dashboard; drop-in for Cursor, Continue.dev, Claude Code, VS Code Copilot, or any OpenAI-compatible client."
---

QwenGate solves a specific gap: Alibaba offers capable Qwen models free in its web chat, but provides no API endpoint, so tools like Claude Code, Cursor, or any OpenAI SDK client cannot use them directly. The gateway logs into chat.qwen.ai accounts via Playwright browser automation once, pools those sessions, and exposes standard /v1/chat/completions endpoints backed by a browserless transport for per-request speed. Multiple accounts rotate round-robin with cooldown tracking and automatic failover to stay under rate limits, and because Qwen's chat models lack native tool calling, the gateway parses JSON tool-call text from responses and re-emits it as OpenAI-format tool calls with schema validation. SSE streaming, a content filter that strips thinking tags, and a five-page observability dashboard round out the server. Self-hosters use it as a free backend for coding agents, with the README noting it is unaffiliated with Alibaba and subject to chat.qwen.ai's terms of service.
