---
name: "ChainlessChain IDE Bridge"
slug: "chainlesschain-ide-bridge"
layout: "agent.njk"
category: "multiplexer"
maker: "chainlesschain"
license: "MIT"
url: "https://plugins.jetbrains.com/plugin/32208-chainlesschain-ide-bridge"
source_code_url: null
source_available: null
platforms:
  - "IDE"
first_released: "2026-08-27"
current_release: null
stars: null
language: null
homepage: "https://plugins.jetbrains.com/plugin/32208-chainlesschain-ide-bridge"
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "yes (via cc CLI /plan)"
model_providers: "BYOK via the cc CLI (model configured in the agent, not the bridge)"
pricing: "free"
install_method: "Install from the JetBrains Marketplace"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://plugins.jetbrains.com/plugin/32208-chainlesschain-ide-bridge"
maintained: "active"
sources:
  - "gap-2026-08-20"
what_makes_it_special: "Brings the ChainlessChain cc agent CLI into JetBrains as a side-panel coding agent"
---

ChainlessChain IDE Bridge integrates the ChainlessChain cc agent CLI into JetBrains IDEs as a side-panel coding agent, for developers who want the agent's capabilities without leaving IntelliJ-based IDEs. The plugin hosts multiple cc agent processes as conversation tabs with session resume across restarts, feeds editor context automatically (current selection, open tabs, diagnostics), and renders proposed changes as native side-by-side diffs with accept, request-changes, or reject actions across multi-file batches. Slash commands mirror the CLI's own vocabulary — including /plan, /auto, /think, and /cost — and an embedded JCEF view runs the dev server inside the IDE for live preview of generated apps. The plugin requires the chainlesschain CLI installed separately and is free under an MIT license, first published to the JetBrains Marketplace in August 2026 with rapid release cadence (v0.4.103 within weeks) tracking the cc CLI's own frequent updates.
