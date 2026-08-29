---
name: "Microsoft Agent Framework"
slug: "microsoft-agent-framework"
layout: "agent.njk"
category: "agent-sdk"
maker: null
license: "MIT"
url: "https://learn.microsoft.com/en-us/agent-framework/overview/agent-framework-overview"
source_code_url: null
source_available: "Yes"
platforms: []
first_released: null
current_release: null
stars: null
language: "Python, C#"
homepage: null
mcp_support: "yes"
plugin_support: "yes (middleware, tools, Agent Skills, AF Labs)"
claude_code_plugin: null
subagents: "yes (multi-agent graph-based workflows)"
hooks: "yes (middleware for intercepting agent actions)"
plan_mode: "yes (Harness Agent with planning and todo tracking)"
model_providers: "Microsoft Foundry, Anthropic, Azure OpenAI, OpenAI, Ollama, GitHub Copilot SDK"
pricing: "open-source"
install_method: "Python: pip install agent-framework; .NET: dotnet add package Microsoft.Agents.AI; Go: go get github.com/microsoft/agent-framework-go"
docs_url: "https://learn.microsoft.com/en-us/agent-framework/"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/microsoft/agent-framework"
maintained: "active"
sources:
  - "jim"
what_makes_it_special: "The direct successor to both Semantic Kernel and AutoGen (created by the same teams), merging AutoGen's simple agent abstractions with Semantic Kernel's enterprise-grade features. Adds graph-based workflows for explicit multi-agent orchestration, robust state management, durability, human-in-the-loop control, OpenTelemetry observability, declarative YAML agents, and an interactive DevUI for development/debugging."
---

Microsoft merged its two agent lineages — AutoGen's research abstractions and Semantic Kernel's enterprise machinery — into a single framework maintained by the same teams, so organizations no longer choose between them. Core mechanics center on graph-based workflows that connect agents and functions with typed state, checkpoints, and human-in-the-loop nodes, while middleware intercepts agent actions and MCP supplies tools. A batteries-included Harness Agent adds planning, todo tracking, context compaction, and tool approval for long multi-step tasks, and declarative YAML lets agents be defined without code. Distribution follows conventional SDK channels — Microsoft.Agents.AI for .NET, agent-framework on PyPI, and a public-preview Go module — with OpenTelemetry observability and a DevUI for stepping through workflow graphs. The audience is enterprise .NET and Python teams standardizing on Microsoft Foundry, Azure OpenAI, OpenAI, Anthropic, or Ollama; teams migrating from AutoGen or Semantic Kernel use it as the consolidation path.
