---
name: "PyCodeAGI"
slug: "pycodeagi"
layout: "agent.njk"
category: "agent"
maker: "chakkaradeep"
license: null
url: "https://github.com/chakkaradeep/pyCodeAGI"
source_code_url: "https://github.com/chakkaradeep/pyCodeAGI"
source_available: "True"
platforms: []
first_released: "2023-04-16"
current_release: "2023-05-04"
stars: "185"
language: "Python"
homepage: null
mcp_support: "False"
plugin_support: "False"
claude_code_plugin: "False"
subagents: "False"
hooks: "False"
plan_mode: "False"
model_providers: null
pricing: "Free / open source"
install_method: "pip install -r requirements.txt (inferred from requirements.txt)"
docs_url: "https://github.com/chakkaradeep/pyCodeAGI#readme"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/chakkaradeep/pyCodeAGI"
maintained: "dormant"
sources:
  - "jim"
what_makes_it_special: "Early experimental AGI that generates a Python app from a user description. Uses LangChain and adopts the BabyAGI concept from @yoheinakajima. Very early-stage project with only 11 commits."
---

PyCodeAGI was one of the early 2023 experiments that applied the BabyAGI task-loop pattern to software generation: describe the app you want, and the agent decomposes the goal into tasks, executes them with GPT-4 via LangChain, and iterates toward a working Python application. The implementation is minimal — a main script, a GPT-4 variant, and a config file — reflecting the era when agent projects fit in a few hundred lines. It adopted the task-driven loop Yohei Nakajima published as BabyAGI and pointed it at code generation rather than general research tasks. Development stopped after eleven commits in May 2023, and the README still describes the project as just started. Its main interest now is historical, as an early data point in the line from BabyAGI-style loops to modern coding agents.
