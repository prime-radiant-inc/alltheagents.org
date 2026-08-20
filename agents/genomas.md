---
name: "GenoMAS"
slug: "genomas"
layout: "agent.njk"
category: "agent"
maker: "Liu-Hy"
license: "MIT"
url: "https://github.com/Liu-Hy/GenoMAS"
source_code_url: "https://github.com/Liu-Hy/GenoMAS"
source_available: True
platforms: []
first_released: "2024-05-13"
current_release: "2026-04-20"
stars: "134"
language: "Python"
homepage: "https://liu-hy.github.io/GenoMAS/"
mcp_support: null
plugin_support: null
claude_code_plugin: False
subagents: True
hooks: null
plan_mode: True
model_providers: "OpenAI, Anthropic, Google Gemini, Ollama, Novita API"
pricing: "Free (MIT); running full benchmark costs ~$300+ in API fees"
install_method: "conda create -n genomas python=3.10; pip install -r requirements.txt; copy env.example to .env and fill API keys"
docs_url: "https://liu-hy.github.io/GenoMAS/"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/Liu-Hy/GenoMAS"
maintained: "active"
sources:
  - "jim"
what_makes_it_special: "Multi-agent framework for scientific discovery via code-driven gene expression analysis; official implementation of arXiv paper; achieves 60.38% F1 on GenoTEX benchmark; role-specific model assignment (Code Reviewer, Domain Expert, Data Engineer, Statistician, Planning)"
---

Multi-agent framework for scientific discovery via code-driven gene expression analysis; official implementation of arXiv paper; achieves 60.38% F1 on GenoTEX benchmark; role-specific model assignment (Code Reviewer, Domain Expert, Data Engineer, Statistician, Planning)
