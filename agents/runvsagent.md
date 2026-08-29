---
name: "RunVSAgent"
slug: "runvsagent"
layout: "agent.njk"
category: "multiplexer"
maker: "wecode-ai"
license: "Apache-2.0"
url: "https://github.com/wecode-ai/RunVSAgent"
source_code_url: "https://github.com/wecode-ai/RunVSAgent"
source_available: "yes"
platforms:
  - "IDE"
first_released: "2025-07-31"
current_release: "2026-05-12"
stars: "719"
language: "Kotlin, TypeScript"
homepage: null
mcp_support: "no"
plugin_support: "yes"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: null
pricing: "open-source"
install_method: "jetbrains"
docs_url: "https://github.com/wecode-ai/RunVSAgent"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/wecode-ai/RunVSAgent/releases"
maintained: "active"
sources:
  - "github_topic"
what_makes_it_special: "Bridges the VSCode ecosystem and JetBrains IDEs, allowing developers to use VSCode-based AI coding agents (Roo Code, Cline, Kilo Code) natively within JetBrains IDEs (IntelliJ IDEA, WebStorm, PyCharm) via an extension host with RPC communication. Maintained by WeCode-AI Team, Weibo Inc."
---

JetBrains users faced a choice between switching IDEs or losing access to the VS Code agent ecosystem, since Roo Code, Cline, and Kilo Code ship only as VS Code extensions; Weibo's WeCode-AI team built the bridge rather than a competing agent. The Kotlin plugin provides the IDE surface, while the Node Extension Host emulates the VS Code API the extensions call, with the two processes communicating over local sockets. Any supported agent runs with its own UI, MCP servers, and settings intact, which also means the bridge inherits those agents' model providers rather than defining its own. Installation is via the JetBrains Marketplace or a downloaded zip, requiring IDE 2023.1 or newer. It serves JetBrains developers who want a specific VS Code agent without changing editors, and the project is actively maintained with published known issues.
