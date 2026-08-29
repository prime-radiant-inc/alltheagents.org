---
name: "GenoMAS"
slug: "genomas"
layout: "agent.njk"
category: "other"
maker: "Liu-Hy"
license: "MIT"
url: "https://github.com/Liu-Hy/GenoMAS"
source_code_url: "https://github.com/Liu-Hy/GenoMAS"
source_available: "True"
platforms: []
first_released: "2024-05-13"
current_release: "2026-04-20"
stars: "134"
language: "Python"
homepage: "https://liu-hy.github.io/GenoMAS/"
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "False"
subagents: "True"
hooks: "no"
plan_mode: "True"
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

GenoMAS automates gene-expression analysis — the kind of multi-step statistical and bioinformatics work that normally takes a trained analyst — by having LLM agents write and run the analysis code themselves. Its generic framework prescribes typed messaging between role-specialized agents, each of which can plan, write code, execute it, debug failures, and backtrack through a notebook-style workflow, with different models assigned per role from OpenAI, Anthropic, Gemini, Ollama, or Novita. The headline implementation analyzes GEO/TCGA transcriptomic data for gene-trait associations while controlling confounders, and the official implementation reproduces the paper's 60.38% F1 on GenoTEX. Published as the arXiv 2507.21035 artifact from UIUC and UC San Diego, it targets computational biology researchers rather than software developers.
