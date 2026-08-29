---
name: "Swades Agent"
slug: "swades-agent"
layout: "agent.njk"
category: "agent"
maker: "xerv"
license: "MIT"
url: "https://plugins.jetbrains.com/plugin/33117-swades-agent"
source_code_url: null
source_available: "yes"
platforms:
  - "IDE"
first_released: "2026-07-24"
current_release: null
stars: null
language: "JavaScript"
homepage: "https://github.com/Xerv-Org/Swades-Agent"
mcp_support: null
plugin_support: null
claude_code_plugin: null
subagents: null
hooks: null
plan_mode: null
model_providers: null
pricing: "free"
install_method: "Install from the JetBrains Marketplace"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://plugins.jetbrains.com/plugin/33117-swades-agent"
maintained: "active"
sources:
  - "gap-2026-08-20"
what_makes_it_special: "Autonomous AI software engineering agent ReAct loop in IntelliJ terminal"
---

Swades Agent brings a ReAct-pattern coding agent — interleaved reasoning and tool calls — into the IntelliJ built-in terminal, where it reads the codebase, edits files, runs shell commands, and searches code iteratively until a plain-text task is complete. The plugin is a thin wrapper: the agent itself is an open-source JavaScript project under the Xerv organization, and the plugin simply hosts the loop inside the IDE terminal, which keeps the tool surface ordinary shell commands and file operations. It is distributed free on the JetBrains Marketplace under an MIT license. Adoption is minimal so far (single-digit installs, one-star repo activity as of mid-2026), so it is best read as an early autonomous-agent experiment for JetBrains users rather than an established tool.
