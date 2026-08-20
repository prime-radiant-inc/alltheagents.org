---
name: "Syncode"
slug: "syncode"
layout: "agent.njk"
category: "agent"
maker: "structuredllm"
license: "MIT"
url: "https://github.com/uiuc-focal-lab/syncode"
source_code_url: "https://github.com/uiuc-focal-lab/syncode"
source_available: True
platforms: []
first_released: "2023-09-04"
current_release: "2026-01-19"
stars: "339"
language: "Python"
homepage: "https://structuredllm.com"
mcp_support: False
plugin_support: False
claude_code_plugin: False
subagents: False
hooks: False
plan_mode: False
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

Grammar-guided generation framework for LLMs ensuring outputs are syntactically valid per Context-Free Grammars (CFG) and Regex. Pre-computes masks for speed (~10% overhead), handles general-purpose languages including non-context-free fragments (Python indentation, Go end-of-scope), and reports 99% JSON accuracy with Gemma-2b.
