---
name: "landing page"
slug: "landing-page"
layout: "agent.njk"
category: "other"
maker: null
license: "MIT"
url: "https://www.microsoft.com/en-us/research/project/autogen/"
source_code_url: null
source_available: "True"
platforms:
  - "Web"
first_released: null
current_release: null
stars: null
language: "Python, .NET"
homepage: null
mcp_support: "True"
plugin_support: null
claude_code_plugin: null
subagents: null
hooks: null
plan_mode: null
model_providers: "OpenAI, Azure OpenAI"
pricing: "Free / open-source"
install_method: "pip install -U 'autogen-agentchat' 'autogen-ext[openai]'"
docs_url: "https://microsoft.github.io/autogen/"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/microsoft/autogen"
maintained: "active"
sources:
  - "jim"
what_makes_it_special: "Associated link: the Microsoft Research project page for AutoGen, an open-source programming framework for building multi-agent AI applications with an asynchronous, event-driven architecture enabling scalable, distributed agentic workflows; supports MCP servers via McpWorkbench"
---

AutoGen is Microsoft Research's framework for constructing multi-agent applications, and its project page catalogs the architecture rather than shipping an agent itself. Version 0.4 rebuilt the library around asynchronous, event-driven message passing so agents cooperate through request/response and event patterns, with pluggable agents, tools, memory, and models, OpenTelemetry tracing, and build-time type checking. Distributed agent networks can span organizational boundaries, which is the feature that distinguishes it from single-process agent libraries. Researchers and engineering teams use it as the substrate for their own agent applications rather than as a ready coding harness.
