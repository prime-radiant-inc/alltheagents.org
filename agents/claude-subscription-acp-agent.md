---
name: "Claude Subscription ACP Agent"
slug: "claude-subscription-acp-agent"
layout: "agent.njk"
category: "multiplexer"
maker: "Vanssa"
license: "MIT"
url: "https://plugins.jetbrains.com/plugin/33150-claude-subscription-acp-agent"
source_code_url: null
source_available: "yes"
platforms:
  - "IDE"
first_released: "2026-07-26"
current_release: "2026-07-30"
stars: null
language: "Kotlin"
homepage: null
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "Anthropic (Claude subscription via ACP)"
pricing: "free"
install_method: "Install from the JetBrains Marketplace"
docs_url: "https://plugins.jetbrains.com/plugin/33150-claude-subscription-acp-agent"
plugin_docs_url: null
config_docs_url: null
download_url: "https://plugins.jetbrains.com/plugin/33150-claude-subscription-acp-agent"
maintained: "active"
sources:
  - "gap-2026-08-20"
what_makes_it_special: "Adds a Claude Subscription agent to JetBrains AI chat"
---

JetBrains ships a bundled Claude agent, but it launches with --hide-claude-auth, which removes subscription login and rejects claude.ai credentials, pushing users toward API keys or JetBrains AI credits. This plugin packages the same official ACP adapter without that flag, so the standard claude.ai subscription login works directly in the IDE's AI chat with no configuration files or wrapper scripts. It targets developers who already pay for Claude Pro/Max and organizations that restrict API token creation. It is MIT-licensed, free, unmodified official-tooling under the hood, and published on the JetBrains Marketplace by Vanssa in July 2026.
