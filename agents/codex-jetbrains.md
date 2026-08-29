---
name: "Codex-JetBrains"
slug: "codex-jetbrains"
layout: "agent.njk"
category: "multiplexer"
maker: "Haleclipse"
license: "Apache-2.0"
url: "https://github.com/Haleclipse/Codex-JetBrains"
source_code_url: "https://github.com/Haleclipse/Codex-JetBrains"
source_available: "True"
platforms:
  - "IDE"
first_released: "2025-12-26"
current_release: "2025-12-28"
stars: "125"
language: "Kotlin, TypeScript"
homepage: null
mcp_support: null
plugin_support: "True"
claude_code_plugin: "False"
subagents: null
hooks: null
plan_mode: null
model_providers: null
pricing: "Free (Apache-2.0)"
install_method: "JetBrains Marketplace: search RunVSAgent in Settings -> Plugins -> Marketplace; or download .zip from GitHub Releases and Install Plugin from Disk; or build from source with Node.js 18+, JDK 17+"
docs_url: "https://github.com/wecode-ai/RunVSAgent#readme"
plugin_docs_url: null
config_docs_url: null
download_url: "https://plugins.jetbrains.com/plugin/28068-runvsagent"
maintained: "active"
sources:
  - "github_deep"
what_makes_it_special: "Cross-platform JetBrains plugin (RunVSAgent) that runs VSCode-based coding agents and extensions (Roo Code, Cline, Kilo Code) within JetBrains IDEs via a Kotlin plugin and Node.js extension host communicating over RPC; supports all major JetBrains IDEs (2023.1+)"
---

RunVSAgent, of which this repository is a mirror, brings VS Code-only coding agents to JetBrains IDEs. A Kotlin plugin provides the JetBrains-side UI and editor integration, while a Node.js extension host implements the VS Code API surface those extensions expect, with the two communicating over RPC on Unix domain sockets or named pipes. The result is that Roo Code, Cline, and Kilo Code run inside IntelliJ IDEA, WebStorm, PyCharm, GoLand, Rider, and other JetBrains IDEs from 2023.1 onward with their native UIs and agent behavior intact. The tool was developed by the WeCode-AI team at Weibo and is distributed through the JetBrains Marketplace as plugin 28068; the Haleclipse repository mirrors it rather than being the primary distribution.
