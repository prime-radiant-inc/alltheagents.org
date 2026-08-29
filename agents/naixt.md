---
name: "Naixt"
slug: "naixt"
layout: "agent.njk"
category: "agent"
maker: "stephen-chancetop"
license: "Apache-2.0"
url: "https://plugins.jetbrains.com/plugin/26662-naixt"
source_code_url: null
source_available: "yes"
platforms:
  - "IDE"
first_released: "2025-03-25"
current_release: "2025-03-25"
stars: null
language: "Kotlin (plugin) + agent server package"
homepage: "https://plugins.jetbrains.com/plugin/26662-naixt"
mcp_support: "no"
plugin_support: "yes"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "OpenAI, Azure OpenAI"
pricing: "free"
install_method: "Install from the JetBrains Marketplace"
docs_url: "https://plugins.jetbrains.com/plugin/26662-naixt"
plugin_docs_url: null
config_docs_url: null
download_url: "https://plugins.jetbrains.com/plugin/26662-naixt"
maintained: "dormant"
sources:
  - "gap-2026-08-20"
what_makes_it_special: "Coding agent with configurable LLM endpoint"
---

Naixt integrates a coding agent into JetBrains IDEs as a tool window. The plugin expects SYS_LLM_ENDPOINT and SYS_LLM_APIKEY environment variables, with an optional provider selector covering litellm, Azure, and azure-inference deployments. The agent server is configured and run locally, and the plugin auto-downloads the agent package from a companion GitHub repository if needed. Conversation happens in the tool window after pressing Start, with the agent operating on the open project. The vendor is an unverified JetBrains Marketplace organization, and the plugin shows only 449 downloads since March 2025, so it is best treated as a low-adoption niche tool.
