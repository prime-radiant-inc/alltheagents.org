---
name: "AutoGen"
slug: "autogen"
layout: "agent.njk"
category: "agent-sdk"
maker: "microsoft"
license: "MIT"
url: "https://github.com/microsoft/autogen"
source_code_url: "https://github.com/microsoft/autogen"
source_available: "Yes"
platforms: []
first_released: "2023-08-18"
current_release: "2026-04-15"
stars: "60525"
language: "Python"
homepage: "https://microsoft.github.io/autogen/"
mcp_support: "yes (StdioServerParams, McpWorkbench)"
plugin_support: "yes (Extensions API)"
claude_code_plugin: "no"
subagents: "yes"
hooks: "no"
plan_mode: "no"
model_providers: "OpenAI, Azure OpenAI"
pricing: "open-source"
install_method: "pip"
docs_url: "https://microsoft.github.io/autogen/"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/microsoft/autogen"
maintained: "dormant"
sources:
  - "e2b"
  - "jim"
  - "caramaschi"
  - "brandonhimpfen"
  - "namphuong"
what_makes_it_special: "Pioneered multi-agent orchestration patterns at Microsoft Research with a layered extensible architecture (Core -> AgentChat -> Extensions), cross-language support (Python + .NET), and a no-code GUI (AutoGen Studio)."
---

AutoGen, from Microsoft Research, pioneered event-driven multi-agent orchestration with a layered architecture: a Core API for event-driven agents and distributed runtimes, an opinionated AgentChat API for group chats and two-agent conversations, and an Extensions API for OpenAI/Azure clients, code execution, and MCP interop (McpWorkbench). AutoGen Studio provides a no-code GUI for prototyping agent workflows, and Magentic-One demonstrates a generalist multi-agent team on top of the stack. Both Python and .NET implementations are supported. The project is now in maintenance mode - community-managed for bug fixes and security only - with Microsoft directing new development to the Microsoft Agent Framework, which reached production-ready 1.0. Existing Python and .NET users can migrate via the published guide.
