---
name: "MetaGPT"
slug: "metagpt"
layout: "agent.njk"
category: "agent"
maker: "FoundationAgents"
license: "MIT"
url: "https://github.com/geekan/MetaGPT"
source_code_url: "https://github.com/geekan/MetaGPT"
source_available: "Yes"
platforms:
  - "IDE"
  - "Autonomous"
first_released: "2023-06-30"
current_release: "2026-01-21"
stars: "69901"
language: "Python"
homepage: "https://atoms.dev/"
mcp_support: null
plugin_support: null
claude_code_plugin: null
subagents: "yes"
hooks: null
plan_mode: null
model_providers: "OpenAI, Azure, Ollama, Groq"
pricing: "open-source"
install_method: "pip, docker"
docs_url: "https://docs.deepwisdom.ai/main/en/"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/FoundationAgents/MetaGPT"
maintained: "active"
sources:
  - "e2b"
  - "jim"
  - "caramaschi"
  - "vinkius"
  - "brandonhimpfen"
what_makes_it_special: "Simulates an entire software company as a multi-agent system with specialized roles (product manager, architect, project manager, engineer) following standardized operating procedures; takes a one-line requirement and produces complete project outputs."
---

MetaGPT was built on the observation that LLMs produce incoherent software when asked for code directly, but produce far better results when forced through the intermediate artifacts a real team would create. A one-line requirement passes through product-manager, architect, and project-manager roles that emit user stories, competitive analysis, data structures, and API specifications before the engineer role writes code, with the pipeline exposed both as a CLI command and as a Python generate_repo call returning a ProjectRepo object. A DataInterpreter role extends the same machinery to data-analysis tasks. The project moved from the geekan personal account to the FoundationAgents organization and remains under MIT with a config2.yaml supporting OpenAI, Azure, Ollama, and Groq endpoints. Academic adoption (the ICLR 2024 paper and AFlow, an ICLR 2025 oral) keeps it a research substrate, while the commercial descendant MGX at mgx.dev carries the productized variant; teams use both to generate complete small projects from one-line requirements and as a multi-agent research substrate.
