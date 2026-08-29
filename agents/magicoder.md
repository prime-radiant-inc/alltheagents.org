---
name: "Magicoder"
slug: "magicoder"
layout: "agent.njk"
category: "other"
maker: "ISE-UIUC"
license: "MIT"
url: "https://github.com/ise-uiuc/magicoder"
source_code_url: "https://github.com/ise-uiuc/magicoder"
source_available: "True"
platforms:
  - "CLI"
  - "API"
first_released: "2023-11-01"
current_release: null
stars: null
language: "Python"
homepage: null
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: null
pricing: "open-source"
install_method: null
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://huggingface.co/ise-uiuc"
maintained: "dormant"
sources:
  - "bing_ddg_chinese"
what_makes_it_special: "A code-generation model family empowered by OSS-Instruct, which uses open-source code snippets to generate low-bias, high-quality instruction data, mitigating inherent biases in LLM-synthesized data. Magicoder-S-DS-6.7B outperforms GPT-3.5-turbo and Gemini Ultra on HumanEval. A model, not an agent harness."
---

Magicoder attacked a data-quality problem in code-model training: instruction data synthesized purely by LLMs inherits their biases and blind spots, so the UIUC team instead seeded generation with randomly sampled snippets from real open-source code, producing 75K diverse instruction-response pairs that became the OSS-Instruct dataset. Models fine-tuned from DeepSeek and Llama-2 bases with this data (plus an Evol-Instruct set) reached state-of-the-art 6.7B-class HumanEval scores at release. ML researchers and practitioners training or serving local code models use the released checkpoints, datasets, and method; the ICML 2024 paper documents the approach. It is model and dataset work, with no agentic loop of any kind.
