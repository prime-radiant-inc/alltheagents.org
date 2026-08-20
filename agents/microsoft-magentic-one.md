---
name: "Microsoft Magentic-One"
slug: "microsoft-magentic-one"
layout: "agent.njk"
category: "agent"
maker: null
license: "MIT"
url: "https://www.microsoft.com/en-us/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks/"
source_code_url: null
source_available: "Yes"
platforms: []
first_released: null
current_release: null
stars: null
language: "Python"
homepage: null
mcp_support: null
plugin_support: null
claude_code_plugin: null
subagents: "yes (Orchestrator + WebSurfer + FileSurfer + Coder + ComputerTerminal)"
hooks: null
plan_mode: "yes (Orchestrator with Task Ledger and Progress Ledger for planning and re-planning)"
model_providers: "OpenAI (GPT-4o, o1-preview); model-agnostic"
pricing: "open-source"
install_method: "pip install \"autogen-agentchat\" \"autogen-ext[magentic-one,openai]\""
docs_url: "https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/magentic-one.html"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/microsoft/autogen"
maintained: "active"
sources:
  - "jim"
what_makes_it_special: "A generalist multi-agent system with a modular, plug-and-play design where agents can be added/removed without reworking the system. An Orchestrator leads four specialized agents (WebSurfer, FileSurfer, Coder, ComputerTerminal) with error recovery through re-planning. Achieves competitive performance on GAIA, AssistantBench, and WebArena benchmarks without task-specific modifications. Now integrated into autogen-agentchat as MagenticOneGroupChat."
---

A generalist multi-agent system with a modular, plug-and-play design where agents can be added/removed without reworking the system. An Orchestrator leads four specialized agents (WebSurfer, FileSurfer, Coder, ComputerTerminal) with error recovery through re-planning. Achieves competitive performance on GAIA, AssistantBench, and WebArena benchmarks without task-specific modifications. Now integrated into autogen-agentchat as MagenticOneGroupChat.
