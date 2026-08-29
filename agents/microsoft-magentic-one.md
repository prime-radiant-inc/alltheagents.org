---
name: "Microsoft Magentic-One"
slug: "microsoft-magentic-one"
layout: "agent.njk"
category: "agent-sdk"
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
install_method: "pip install 'autogen-agentchat' 'autogen-ext[magentic-one,openai]'"
docs_url: "https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/magentic-one.html"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/microsoft/autogen"
maintained: "active"
sources:
  - "jim"
what_makes_it_special: "A generalist multi-agent system with a modular, plug-and-play design where agents can be added/removed without reworking the system. An Orchestrator leads four specialized agents (WebSurfer, FileSurfer, Coder, ComputerTerminal) with error recovery through re-planning. Achieves competitive performance on GAIA, AssistantBench, and WebArena benchmarks without task-specific modifications. Now integrated into autogen-agentchat as MagenticOneGroupChat."
---

Magentic-One came out of Microsoft Research as a demonstration that a small set of generalist agents, well-coordinated, could match specialized systems on open-ended tasks — GAIA, AssistantBench, and WebArena — without task-specific tuning. The Orchestrator keeps a Task Ledger of facts, guesses, and the current plan in an outer loop, re-planning when progress stalls, and an inner Progress Ledger that each step assigns the next subtask to one of four specialists: a Chromium-driving WebSurfer using accessibility-tree and set-of-marks prompting, a FileSurfer reading documents through markdown previews, a Coder, and a ComputerTerminal. Specialists are interchangeable — the system keeps working when one is swapped or removed — and per-agent model assignments allow heterogeneous LLM configurations. It ships as part of autogen-agentchat (MagenticOneGroupChat) with AutoGenBench for isolated, repeated benchmark runs, and Microsoft positions it for research use inside sandboxed containers with human monitoring rather than as a production harness.
