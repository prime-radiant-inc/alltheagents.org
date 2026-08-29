---
name: "Llm_Rag"
slug: "llm-rag"
layout: "agent.njk"
category: "other"
maker: "dongdongunique"
license: "MIT"
url: "https://github.com/dongdongunique/LLM_RAG"
source_code_url: "https://github.com/dongdongunique/LLM_RAG"
source_available: "True"
platforms: []
first_released: "2024-11-24"
current_release: "2025-01-01"
stars: "9"
language: "Python"
homepage: null
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "OpenAI (GPT)"
pricing: "open-source"
install_method: "pip install -U -r requirements.txt"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "jim"
what_makes_it_special: "Retrieval-Augmented Generation (RAG) system using FAISS for vector-based retrieval and GPT for generative responses. Gradio-powered UI for document uploading, searching, and CRUD operations on document chunks. Modular design to support other LLMs (e.g., HuggingFace)."
---

Built as homework for an Advanced Database course, LLM_RAG demonstrates the standard RAG pipeline end to end: documents are chunked and embedded into a FAISS index, similarity search retrieves context for GPT, and a Gradio interface handles upload, search, and chunk-level CRUD. Both a CLI entry point and a web interface are provided, and the modular design leaves room for swapping in Hugging Face models alongside the default OpenAI backend. It serves as an educational reference for RAG mechanics rather than production software; the project has seen no meaningful activity since early 2025.
