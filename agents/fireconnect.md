---
name: "FireConnect"
slug: "fireconnect"
layout: "agent.njk"
category: "other"
maker: "fw-ai"
license: "Apache-2.0"
url: "https://github.com/fw-ai/fireconnect"
source_code_url: "https://github.com/fw-ai/fireconnect"
source_available: "True"
platforms:
  - "CLI"
  - "IDE"
first_released: "2026-06-12"
current_release: "2026-08-18"
stars: "45"
language: "JavaScript / Node.js (requires Node.js 18+) and Bash"
homepage: "https://docs.fireworks.ai/ecosystem/fireconnect/overview"
mcp_support: "True"
plugin_support: null
claude_code_plugin: null
subagents: "True"
hooks: null
plan_mode: null
model_providers: "Fireworks AI, Azure/Microsoft Foundry, Anthropic"
pricing: "Billed at Fireworks serverless rates"
install_method: "curl -fsSL https://raw.githubusercontent.com/fw-ai/fireconnect/main/install.sh | bash"
docs_url: "https://docs.fireworks.ai/ecosystem/fireconnect/overview"
plugin_docs_url: null
config_docs_url: null
download_url: "https://raw.githubusercontent.com/fw-ai/fireconnect/main/install.sh"
maintained: "active"
sources:
  - "brad"
what_makes_it_special: "CLI that configures existing AI coding tools (Claude Code, OpenCode, Codex, Pi, Cursor, VS Code, DeepSeek Harness) to route requests through Fireworks AI by natively rewriting their config files, restoring originals byte-for-byte on disconnect. Installs fireworks-websearch MCP server for Claude Code. Supports subagent model slot mapping. FireRouter feature dynamically routes requests based on complexity/cost."
---

Fireworks AI built FireConnect to remove the integration tax of pointing coding harnesses at alternative model providers: one command per harness (fireconnect claude, fireconnect codex, and so on) edits the tool's native configuration to route through Fireworks, and fireconnect off restores the original file byte-for-byte. There is deliberately no proxy or wrapper process, which keeps request paths and failure modes identical to the harness's normal operation. Beyond the core harness set (Claude Code, Codex, OpenCode, Pi, Cursor, VS Code Chat, DeepSeek Harness), it supports Azure/Foundry endpoints and FireRouter, a judge-model router for evaluation workflows. Users are Fireworks customers who want frontier-agent UX — Claude Code, Codex, Cursor — running against Fireworks' serverless model endpoints.
