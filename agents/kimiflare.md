---
name: "kimiflare"
slug: "kimiflare"
layout: "agent.njk"
category: "agent"
maker: "sinameraji"
license: "MIT"
url: "https://github.com/sinameraji/kimiflare"
source_code_url: "https://github.com/sinameraji/kimiflare"
source_available: "True"
platforms:
  - "CLI"
  - "Web"
first_released: "2026-04-21"
current_release: "2026-08-19"
stars: "168"
language: "TypeScript"
homepage: "https://kimiflare.com"
mcp_support: "True"
plugin_support: null
claude_code_plugin: null
subagents: null
hooks: "True"
plan_mode: "True"
model_providers: "Cloudflare Workers AI (Kimi K2.7/K2.6/K2.5, GLM-5.2, Kimi K3); any OpenAI-compatible endpoint via KIMIFLARE_BASE_URL"
pricing: "Free/self-hosted (pay Cloudflare Workers AI rates on your own account)"
install_method: "npm install -g kimiflare (or npx kimiflare)"
docs_url: "https://kimiflare.com"
plugin_docs_url: null
config_docs_url: null
download_url: "https://www.npmjs.com/package/kimiflare"
maintained: "active"
sources:
  - "github_deep"
what_makes_it_special: "Terminal coding agent running entirely on your own Cloudflare account via Workers AI; 262k context window, AI Gateway-confirmed cost tracking, local SQLite+embeddings memory, image understanding, OS-aware shell (Windows support), headless SDK + RPC mode; 5 hook events (PreToolUse, PostToolUse, UserPromptSubmit, Stop, PreCompact)."
---

Kimiflare addresses token-cost opacity by running inference on the user's own Cloudflare Workers AI account and routing traffic through Cloudflare AI Gateway, which returns authoritative per-turn costs, cache-hit ratios, and per-feature breakdowns instead of estimates. The agent ships 262k-context models, image understanding, MCP tool extension, LSP integration, local SQLite memory, and veto-capable hooks at five lifecycle points managed through a /hooks catalog. Modes cycle between plan (read-only research), edit (approval per mutation), and auto. Individual developers and small teams use it to keep coding-agent spend inside a Cloudflare bill they already control.
