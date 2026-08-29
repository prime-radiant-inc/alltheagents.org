---
name: "peerd"
slug: "peerd"
layout: "agent.njk"
category: "agent"
maker: "NotASithLord"
license: "Apache-2.0"
url: "https://peerd.ai"
source_code_url: "https://github.com/NotASithLord/peerd"
source_available: "Yes"
platforms:
  - "Web"
first_released: "2026-06-22"
current_release: "2026-08-20"
stars: "392"
language: "JavaScript"
homepage: "https://peerd.ai"
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "yes"
hooks: "no"
plan_mode: "no"
model_providers: "Anthropic, OpenRouter, Ollama (BYOK)"
pricing: "BYOK"
install_method: "git clone + load unpacked extension (chrome://extensions); no build step"
docs_url: "https://peerd.ai"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/NotASithLord/peerd"
maintained: "active"
sources:
  - "hackernews"
what_makes_it_special: "Runs the agent inside the browser itself — the live DOM replaces MCP, a WASM Debian VM replaces the shell, and agents coordinate peer-to-peer over WebRTC with Ed25519 identities — deliberately refusing MCP as an exfiltration risk."
---

peerd is a bet that the browser, not the terminal, is the right runtime for a personal AI agent: the extension turns an existing Chrome or Firefox installation into the harness, inheriting the user's real logins and sessions instead of proxying them. Its act layer drives tabs through the live DOM, the think layer routes models (Anthropic, OpenRouter, local Ollama), spawns subagents, and plans, and a compute layer runs JavaScript notebooks, WASI/WASM tools, and a full Debian VM in WebAssembly. The design rejects MCP entirely — tabs stand in for app access, fetch for APIs, the WebVM for shell — on the argument that MCP dilutes the browser-native thesis and creates exfiltration paths. Agents coordinate peer-to-peer over WebRTC with Ed25519 identities and share signed app bundles through a DHT. It is Apache-2.0, free, accountless, and run-from-source as a v0.x developer preview, aimed at developers who want local, user-owned agent infrastructure.
