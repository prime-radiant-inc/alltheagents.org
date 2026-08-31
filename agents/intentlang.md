---
name: "intentlang"
slug: "intentlang"
layout: "agent.njk"
category: "agent-sdk"
maker: "l3yx"
license: "MIT"
url: "https://github.com/l3yx/intentlang"
source_code_url: "https://github.com/l3yx/intentlang"
source_available: "True"
platforms: []
first_released: "2025-12-27"
current_release: "2026-01-11"
stars: "93"
language: "Python"
homepage: null
mcp_support: "no"
plugin_support: null
claude_code_plugin: null
subagents: null
hooks: null
plan_mode: null
model_providers: "Any OpenAI-compatible (DeepSeek, Alibaba DashScope, Zhipu BigModel)"
pricing: "Free / open-source (MIT)"
install_method: "pip install intentlang | uv add intentlang"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "github_topic4"
what_makes_it_special: "AI-Native, Intent-Oriented Programming Language built on Python; first framework to formally represent human intent as structured elements (Intent IR: Goal, Contexts, Tools, Input, Strategy, Constraints, Output); AI generates and executes Python code directly in the host runtime manipulating real objects without serialization (abandons function calling); data/instruction separation eliminates token limit/cost issues; embedded execution shares host process space (DB connections, browser instances injectable as tools); zero learning cost (Python itself is the DSL)."
---

Intentlang replaces the tool-call round trip with embedded code execution: the model receives an intent's metadata (never the data), generates Python, and that code manipulates real host objects — live database connections, browser sessions — through an embedded REPL with top-level await and error self-correction. The Intent IR (goal, contexts, tools, input, strategy, constraints, output) structures what the model sees, and data never enters the prompt, which sidesteps token costs on large inputs. Any Python object can serve as a tool, so frameworks integrate by injection rather than adapter. It targets developers building agents who find function-calling loops lossy, though executing model-written code demands sandboxing; the project remains a young solo experiment.
