---
name: "claude-code-viewer"
slug: "claude-code-viewer"
layout: "agent.njk"
category: "multiplexer"
maker: "d-kimuson"
license: "MIT"
url: "https://github.com/d-kimuson/claude-code-viewer"
source_code_url: "https://github.com/d-kimuson/claude-code-viewer"
source_available: "True"
platforms:
  - "CLI"
  - "IDE"
  - "Web"
first_released: "2025-08-31"
current_release: "2026-08-18"
stars: "1272"
language: "TypeScript"
homepage: "https://www.npmjs.com/package/@kimuson/claude-code-viewer"
mcp_support: "yes"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "yes"
hooks: "no"
plan_mode: "no"
model_providers: "Anthropic"
pricing: "open-source"
install_method: "npm"
docs_url: "https://github.com/d-kimuson/claude-code-viewer#readme"
plugin_docs_url: null
config_docs_url: null
download_url: "https://www.npmjs.com/package/@kimuson/claude-code-viewer"
maintained: "active"
sources:
  - "github_topic4"
what_makes_it_special: "Full-featured web-based Claude Code client for managing projects — start conversations, resume sessions, monitor tasks in real-time, browse history via modern web UI. Zero data loss via Zod schema validation; MCP Server Viewer; built-in Git operations; session flow analysis; PWA with mobile support; built-in terminal and browser preview; multi-language (EN/JA/ZH)."
---

Claude Code records every session as JSONL files that are painful to read after the fact, and resuming old work means returning to the terminal. ccv runs a local Node server that renders those logs as a searchable web UI and, in full mode, drives Claude Code through the Agent SDK for chat, approvals, uploads, and git operations from the browser. After Anthropic's April 2026 ToS change restricted Agent SDK use on subscription accounts, chat features became opt-in: API-key users get everything, subscription users degrade to log viewing plus a copy-CLI-command flow. Developers reviewing long agent histories, working from mobile, or wiring sessions into automation (an --api-only mode exists for n8n) are the core users.
