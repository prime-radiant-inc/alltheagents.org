---
name: "CrewAI"
slug: "crewai"
layout: "agent.njk"
category: "agent-sdk"
maker: "crewAIInc"
license: "MIT"
url: "https://github.com/joaomdmoura/crewai"
source_code_url: "https://github.com/joaomdmoura/crewai"
source_available: "Yes"
platforms:
  - "Autonomous"
first_released: "2023-10-27"
current_release: "2026-08-20"
stars: "57338"
language: "Python"
homepage: "https://crewai.com"
mcp_support: "yes (MCP/A2A support)"
plugin_support: "yes"
claude_code_plugin: "yes"
subagents: "yes"
hooks: "partial (event-driven Flows with @start/@listen/@router)"
plan_mode: "partial (hierarchical process with manager agent)"
model_providers: "OpenAI, Ollama, LM Studio, BYOK"
pricing: "freemium (open source core; commercial CrewAI AMP Suite)"
install_method: "pip (uv pip install crewai)"
docs_url: "https://docs.crewai.com"
plugin_docs_url: null
config_docs_url: null
download_url: "https://pypi.org/project/crewai/"
maintained: "active"
sources:
  - "e2b"
  - "jim"
  - "brandonhimpfen"
what_makes_it_special: "Combines two complementary paradigms -- autonomous role-based Crews and event-driven deterministic Flows -- letting developers balance agent autonomy with precise control in Python-native code, bridging prototype-to-production."
---

CrewAI emerged to give Python developers a native way to compose teams of LLM agents without stitching together orchestration glue by hand. Its two primitives cover opposite needs: Crews let role-defined agents with goals and tools collaborate autonomously, while Flows encode event-driven workflows where each step is explicit and testable. Agents declare tools, can interoperate through MCP and A2A, and the optional CrewAI AMP control plane adds enterprise deployment on top of the MIT-licensed core. With roughly 58,000 stars and a 100k+ certified-developer program, it is used both by teams building production automation and by the large ecosystem of tutorials and courses built around it.
