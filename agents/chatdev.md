---
name: "ChatDev"
slug: "chatdev"
layout: "agent.njk"
category: "agent"
maker: "OpenBMB"
license: "Apache-2.0"
url: "https://github.com/OpenBMB/ChatDev"
source_code_url: "https://github.com/OpenBMB/ChatDev"
source_available: "Yes"
platforms:
  - "IDE"
first_released: "2023-08-28"
current_release: "2026-07-24"
stars: "34058"
language: "Python"
homepage: "https://arxiv.org/abs/2307.07924"
mcp_support: "yes (mcp_example directory, Blender MCP integration)"
plugin_support: "yes"
claude_code_plugin: "no"
subagents: "yes"
hooks: "no"
plan_mode: "no"
model_providers: "BYOK (any LLM provider via configurable API_KEY and BASE_URL)"
pricing: "open-source"
install_method: "pip (uv sync), npm (frontend), docker"
docs_url: "https://github.com/OpenBMB/ChatDev/blob/main/docs/user_guide/en/index.md"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/OpenBMB/ChatDev"
maintained: "active"
sources:
  - "e2b"
  - "jim"
what_makes_it_special: "A zero-code multi-agent orchestration platform with visual workflow canvas and drag-and-drop agent orchestration; evolved from a 'Virtual Software Company' into a general-purpose platform for data visualization, 3D generation, game development, and deep research."
---

ChatDev began as a research project from Tsinghua NLP and ModelBest simulating a virtual software company: LLM agents take on roles like CEO, CTO, and programmer, collaborating through a chain-shaped 'ChatChain' topology to move a one-line idea through design, coding, testing, and documentation. The project has since broadened beyond software into a general multi-agent platform, releasing ChatDev 2.0 with a drag-and-drop visual workflow canvas where agents are configured via YAML and composed through a web UI, targeting applications from 3D generation and game development to deep research. Under the hood it evolved from chain topologies to DAG-based multi-agent collaboration networks (MacNet) that scale to thousands of agents, backed by a series of research papers and an active OpenBMB community. Researchers in multi-agent collaboration and developers exploring agent-based software automation are its primary users; it is open source under Apache-2.0, installable via pip or Docker, with an MCP example directory included.
