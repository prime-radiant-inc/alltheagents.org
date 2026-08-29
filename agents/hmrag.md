---
name: "HMRAG"
slug: "hmrag"
layout: "agent.njk"
category: "other"
maker: "ocean-luna"
license: "Apache-2.0"
url: "https://github.com/ocean-luna/HMRAG"
source_code_url: "https://github.com/ocean-luna/HMRAG"
source_available: "True"
platforms: []
first_released: "2025-04-13"
current_release: "2025-07-23"
stars: "112"
language: "Python"
homepage: null
mcp_support: "False"
plugin_support: "True"
claude_code_plugin: "no"
subagents: "True"
hooks: "no"
plan_mode: "no"
model_providers: "Ollama,Hugging Face,OpenAI"
pricing: "Free/open-source research project"
install_method: "conda create --name hmrag python=3.10; conda activate hmrag; pip install -r requirements.txt (or conda env create -f environment.yml)"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/ocean-luna/HMRAG"
maintained: "active"
sources:
  - "github_topic4"
what_makes_it_special: "Hierarchical Multi-Agent Multimodal RAG framework with three-tiered architecture (Decomposition Agent -> Multi-source Retrieval Agents -> Decision Agent); plug-and-play retrieval modules for vector/graph/web databases; consistency voting + Expert Model Refinement to resolve discrepancies; accepted at ACM MM 2025; built on LightRAG; demonstrated zero-shot multimodal QA on ScienceQA."
---

HMRAG is the research code accompanying a peer-reviewed paper on hierarchical multi-agent retrieval-augmented generation. A Decomposition Agent rewrites complex queries into sub-tasks; retrieval agents work in parallel across three source types — vector databases, multimodal knowledge graphs via LightRAG, and web search — with plug-and-play retrieval modules; and a Decision Agent fuses candidate answers through consistency voting plus an expert-model refinement step when sources conflict. The framework was evaluated on multimodal QA benchmarks (notably ScienceQA), demonstrating gains from combining structured, unstructured, and graph-based retrieval in one pipeline. It is a research artifact with light maintenance, distributed via conda/pip, and is not aimed at coding workflows.
