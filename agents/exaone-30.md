---
name: "Exaone-3.0"
slug: "exaone-30"
layout: "agent.njk"
category: "other"
maker: "LG-AI-EXAONE"
license: "EXAONE AI Model License Agreement 1.1 - NC (Non-Commercial)"
url: "https://github.com/LG-AI-EXAONE/EXAONE-3.0"
source_code_url: "https://github.com/LG-AI-EXAONE/EXAONE-3.0"
source_available: "True"
platforms: []
first_released: "2024-08-05"
current_release: "2024-08-08"
stars: "181"
language: "Python"
homepage: "https://huggingface.co/LGAI-EXAONE/EXAONE-3.0-7.8B-Instruct"
mcp_support: "False"
plugin_support: "False"
claude_code_plugin: "False"
subagents: "False"
hooks: "False"
plan_mode: "False"
model_providers: null
pricing: "Free for non-commercial use (EXAONE NC license)"
install_method: "Install via HuggingFace transformers: AutoModelForCausalLM.from_pretrained('LGAI-EXAONE/EXAONE-3.0-7.8B-Instruct')"
docs_url: "https://github.com/LG-AI-EXAONE/EXAONE-3.0#readme"
plugin_docs_url: null
config_docs_url: null
download_url: "https://huggingface.co/LGAI-EXAONE/EXAONE-3.0-7.8B-Instruct"
maintained: "dormant"
sources:
  - "jim"
what_makes_it_special: "Bilingual (English and Korean) generative LLM with 7.8B parameters by LG AI Research, pre-trained on 8T tokens. Not a coding agent harness — it is a standalone language model. Competitive performance against Llama 3.1 8B, Gemma 2 9B, QWEN 2 7B, and others, particularly strong on Korean benchmarks."
---

EXAONE 3.0 was LG AI Research's mid-size bilingual model, released in August 2024 in both pre-trained and instruction-tuned 7.8B forms after pre-training on 8 trillion tokens. Its instruction-tuned variant posted competitive results against larger models on Korean-language benchmarks, which made it a common base for Korean-language research and fine-tuning work. The EXAONE AI Model License 1.1 - NC restricted use to non-commercial purposes, and a license revision in August 2024 aimed at supporting the research ecosystem. The repository itself saw only a handful of commits around launch and has been inactive since August 2024, with LG's newer EXAONE releases superseding it under the same organization.
