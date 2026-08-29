---
name: "Even"
slug: "even"
layout: "agent.njk"
category: "multiplexer"
maker: null
license: null
url: "https://even.dev"
source_code_url: null
source_available: "No (proprietary)"
platforms:
  - "CLI"
  - "IDE"
  - "Web"
  - "Desktop"
first_released: null
current_release: null
stars: null
language: null
homepage: "https://even.dev"
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: null
subagents: null
hooks: null
plan_mode: null
model_providers: "Local open models (Even LLMs), Anthropic (Claude Code), OpenAI (Codex)"
pricing: "Free while in beta"
install_method: "Download Universal .dmg (macOS), Windows installer, or .deb/AppImage (Linux)"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://even.dev"
maintained: "active"
sources:
  - "brad"
what_makes_it_special: "Agent-native workspace combining a native terminal, real in-app browser, one-click self-hosted services (Stacks), and local LLMs in one window; agents run under deny-by-default policy with audit trails; ships its own MCP server exposing terminal, browser, and stacks as callable tools"
---

Even was built on the premise that agents fail when given screenshots and sandboxes instead of real tools, so the desktop app gives agents the same surfaces the human uses: native terminal panes with full scrollback, a real in-app browser where agents navigate and type, and Stacks that launch self-hosted services (Postgres, code-server, n8n) without compose files. Local models run on the user's own hardware through a GPU-accelerated engine, and Even ships its own MCP server exposing terminal, browser, and stacks, with Even Connect brokering 56+ services through one meta-tool MCP to keep context lean. Security is the enterprise pitch: deny-by-default policy, risk-tiered approval gates, MCP allow-lists, an on-device credential vault, SSO/SCIM, and SIEM export, with code never leaving the machine. Teams use it to standardize agent/skill catalogs across Claude Code, Codex, and other harnesses.
