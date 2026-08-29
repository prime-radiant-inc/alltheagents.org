---
name: "StarCoder"
slug: "starcoder"
layout: "agent.njk"
category: "other"
maker: "BigCode"
license: "Apache-2.0 (code); BigCode OpenRAIL-M (model weights)"
url: "https://huggingface.co/bigcode/starcoder"
source_code_url: "https://github.com/bigcode-project/starcoder"
source_available: "True"
platforms:
  - "CLI"
  - "API"
first_released: "2023-05"
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
install_method: "pip install -r requirements.txt"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://huggingface.co/bigcode/starcoder"
maintained: "dormant"
sources:
  - "bing_ddg_chinese"
what_makes_it_special: "A code language model trained on 80+ programming languages plus GitHub issues, commits, and notebooks. Supports 8-bit loading under 20GB RAM and has a C++ implementation (starcoder.cpp). Superseded by StarCoder2; repo inactive since May 2023. A model, not an agent harness."
---

StarCoder was the BigCode community's flagship code model, trained on The Stack v1.2 plus GitHub issues, commits, and notebooks with fill-in-the-middle and an 8,192-token context, and it could be quantized to 8-bit to run under 20GB of RAM. It is a base model, not an instruction follower — the model card warns that direct 'write a function' prompts underperform — and it seeded an ecosystem that included starcoder.cpp for CPU inference. The model is governed by the BigCode OpenRAIL-M license with gated access, and the training corpus and code were released openly to enable audit and repurposing. The lineage continued with StarCoder2 in 2024, and the original repository has been inactive since mid-2023. It is a model, not a harness, and belongs in this census only as a categorization reference.
