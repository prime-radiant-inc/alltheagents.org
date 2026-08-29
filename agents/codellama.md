---
name: "CodeLlama"
slug: "codellama"
layout: "agent.njk"
category: "other"
maker: "Meta AI"
license: "Llama 2 Community License"
url: "https://github.com/meta-ai/codellama"
source_code_url: "https://github.com/meta-ai/codellama"
source_available: "True"
platforms:
  - "CLI"
  - "API"
first_released: "2023-08-24"
current_release: null
stars: null
language: "Python"
homepage: null
mcp_support: null
plugin_support: null
claude_code_plugin: null
subagents: null
hooks: null
plan_mode: null
model_providers: null
pricing: null
install_method: "Clone repo, pip install -e . in conda env; download weights via download.sh with signed URL from Meta"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "dead"
sources:
  - "bing_ddg_chinese"
what_makes_it_special: "A family of Llama-2-based code models (7B/13B/34B/70B) with code infilling (7B & 13B), up to 100k token input context, and three flavors: foundation, Python-specialized, and instruction-following. State-of-the-art among open code models at release. GitHub repo archived by owner on Jul 1, 2025. A model, not an agent harness."
---

Code Llama was Meta's family of code-specialized large language models built on Llama 2, released in sizes from 7B to 70B in three variants: foundation, Python-specialized, and instruction-following. The 7B and 13B variants support infilling for editor-style fill-in-the-middle completion, and all sizes accept input contexts up to 100,000 tokens, which was unusually long for code models at the August 2023 release. The repository provides inference code and a download script for the gated weights rather than any agent tooling; applications consumed the models through their own harnesses. Meta archived the repository on July 1, 2025 as the model line aged out.
