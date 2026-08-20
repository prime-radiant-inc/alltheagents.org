---
name: "cowork-to-code-bridge"
slug: "cowork-to-code-bridge"
layout: "agent.njk"
category: "agent"
maker: "abhinaykrupa"
license: "MIT"
url: "https://github.com/abhinaykrupa/cowork-to-code-bridge"
source_code_url: "https://github.com/abhinaykrupa/cowork-to-code-bridge"
source_available: True
platforms:
  - "IDE"
  - "Web"
  - "Desktop"
  - "Autonomous"
first_released: "2026-05-28"
current_release: "2026-08-07"
stars: "12"
language: "Python"
homepage: "https://github.com/abhinaykrupa/cowork-to-code-bridge#install--two-pastes-total"
mcp_support: True
plugin_support: True
claude_code_plugin: True
subagents: null
hooks: True
plan_mode: True
model_providers: "Claude (haiku, sonnet, opus, fable)"
pricing: null
install_method: "curl -fsSL https://raw.githubusercontent.com/abhinaykrupa/cowork-to-code-bridge/main/install.sh | bash; brew install abhinaykrupa/tap/cowork-to-code-bridge; pip install cowork-to-code-bridge"
docs_url: "https://github.com/abhinaykrupa/cowork-to-code-bridge/blob/main/docs/"
plugin_docs_url: null
config_docs_url: null
download_url: "https://pypi.org/project/cowork-to-code-bridge/"
maintained: "active"
sources:
  - "brad"
what_makes_it_special: "Bridges Claude Cowork (cloud sandbox) to Claude Code on your local machine via a shared file-based queue — no open ports, no network listener. Outbound-only, idempotent task execution (safe retries after dropped connections/crashes), token-gated, only runs user-whitelisted scripts, daemon auto-restarts and survives reboots. Designed as a universal MCP-based local code execution backend."
---

Bridges Claude Cowork (cloud sandbox) to Claude Code on your local machine via a shared file-based queue — no open ports, no network listener. Outbound-only, idempotent task execution (safe retries after dropped connections/crashes), token-gated, only runs user-whitelisted scripts, daemon auto-restarts and survives reboots. Designed as a universal MCP-based local code execution backend.
