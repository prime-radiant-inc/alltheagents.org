---
name: "LegalGraphRAG"
slug: "legalgraphrag"
layout: "agent.njk"
category: "agent"
maker: "XMUDeepLIT"
license: null
url: "https://github.com/XMUDeepLIT/LegalGraphRAG"
source_code_url: "https://github.com/XMUDeepLIT/LegalGraphRAG"
source_available: True
platforms: []
first_released: "2026-03-16"
current_release: "2026-08-03"
stars: "50"
language: "Python"
homepage: "https://arxiv.org/abs/2605.28120"
mcp_support: False
plugin_support: False
claude_code_plugin: False
subagents: False
hooks: False
plan_mode: False
model_providers: "Qwen3-8B, Qwen2.5-7B-Instruct, DeepSeek-V3, GPT-4o-mini, InternLM3, GLM-4"
pricing: null
install_method: "pip install -r requirements.txt; cp env.example .env; python run.py --model <model> --datasets <dataset>"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "github_topic4"
what_makes_it_special: "Evaluation framework for legal judgment prediction integrating multi-agent graph retrieval-augmented generation (RAG); computes charge, law-article, and imprisonment prediction metrics on CAIL/CMDL datasets using a 14,049-case graph corpus."
---

Evaluation framework for legal judgment prediction integrating multi-agent graph retrieval-augmented generation (RAG); computes charge, law-article, and imprisonment prediction metrics on CAIL/CMDL datasets using a 14,049-case graph corpus.
