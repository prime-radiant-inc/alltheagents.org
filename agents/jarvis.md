---
name: "jarvis"
slug: "jarvis"
layout: "agent.njk"
category: "agent"
maker: "danilofalcao"
license: "MIT"
url: "https://github.com/danilofalcao/jarvis"
source_code_url: "https://github.com/danilofalcao/jarvis"
source_available: "True"
platforms: []
first_released: "2025-01-03"
current_release: "2025-01-26"
stars: "641"
language: "Python"
homepage: null
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "DeepSeek, Codestral, Google, Grok, Anthropic, OpenAI, OpenRouter"
pricing: "open-source"
install_method: "source"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "github_deep"
what_makes_it_special: "Multi-model AI coding assistant with integrated cross-platform terminal (xterm.js), file attachments (PDF/Word/Excel/OCR), WebSocket real-time updates, workspace management, diff-based code modification previews, and context-aware chat"
---

jarvis is a DIY control panel for code work across models: a browser workspace shows files, diffs, and a real terminal side by side, so generating a change, reviewing its diff, and running it happen in one screen. Document attachments with OCR feed PDFs, spreadsheets, and screenshots into context, and WebSocket streaming keeps generation live. The backend is a single Flask app with Flask-SocketIO; the frontend is plain JS with CodeMirror and Tailwind. All provider keys are configured in .env, and the tool is BYOK end to end. Activity stopped around early 2025 — 140 commits, no releases — making it a snapshot of the 2025 local-coding-chat wave.
