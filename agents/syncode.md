---
name: "Syncode"
slug: "syncode"
layout: "agent.njk"
category: "other"
maker: "structuredllm"
license: "MIT"
url: "https://github.com/uiuc-focal-lab/syncode"
source_code_url: "https://github.com/uiuc-focal-lab/syncode"
source_available: "True"
platforms: []
first_released: "2023-09-04"
current_release: "2026-01-19"
stars: "339"
language: "Python"
homepage: "https://structuredllm.com"
mcp_support: "False"
plugin_support: "False"
claude_code_plugin: "False"
subagents: "False"
hooks: "False"
plan_mode: "False"
model_providers: "HuggingFace models (code, chat, instruct)"
pricing: "Free/open-source (MIT)"
install_method: "pip install syncode (or pip install git+https://github.com/structuredllm/syncode.git)"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/structuredllm/syncode"
maintained: "active"
sources:
  - "jim"
what_makes_it_special: "Grammar-guided generation framework for LLMs ensuring outputs are syntactically valid per Context-Free Grammars (CFG) and Regex. Pre-computes masks for speed (~10% overhead), handles general-purpose languages including non-context-free fragments (Python indentation, Go end-of-scope), and reports 99% JSON accuracy with Gemma-2b."
---

SynCode is a constrained-decoding library from UIUC that forces LLM output to conform to a Context-Free Grammar, with soundness and completeness guarantees — every produced token sequence satisfies the grammar. It works as a logit processor over HuggingFace models: an incremental LR(1)/LALR(1) parser tracks grammar state, and a pre-computed DFA mask store hides invalid tokens at each step, adding roughly 10% generation overhead while reporting 99% JSON validity with small models. Built-in grammars cover Python, Go, Java, SQL, and JSON, and the framework handles constructs beyond plain CFGs, such as Python's indentation-sensitivity and Go's brace-scoping. It ships as a pip package aimed at researchers generating structured or syntactically valid code, with the design published in an arXiv paper (2403.01632). It is not an agent: there is no tool loop, only constrained decoding.
