---
name: "DeepSeek Coder"
slug: "deepseek-coder"
layout: "agent.njk"
category: "other"
maker: "DeepSeek"
license: "MIT"
url: "https://github.com/deepseek-ai/DeepSeek-Coder"
source_code_url: "https://github.com/deepseek-ai/DeepSeek-Coder"
source_available: "True"
platforms:
  - "CLI"
  - "API"
first_released: "2023-11"
current_release: "DeepSeek-Coder-Instruct (January 2024)"
stars: null
language: "Python"
homepage: "https://www.deepseek.com/"
mcp_support: null
plugin_support: null
claude_code_plugin: null
subagents: null
hooks: null
plan_mode: null
model_providers: null
pricing: null
install_method: "pip install -r requirements.txt"
docs_url: "https://www.deepseek.com/"
plugin_docs_url: null
config_docs_url: null
download_url: "https://huggingface.co/deepseek-ai"
maintained: "active"
sources:
  - "bing_ddg_chinese"
what_makes_it_special: "A family of code LLMs (1B-33B) trained from scratch on 2T tokens (87% code, 13% NL) for code completion, insertion, chat, and repository-level completion. 16K context with fill-in-the-blank; 7B matches CodeLlama-34B; 33B instruct beats GPT-3.5-turbo on HumanEval; supports 87+ languages. A model, not an agent harness."
---

DeepSeek Coder is a series of open-weight code language models from 1.3B to 33B parameters, trained from scratch on two trillion tokens dominated by source code in roughly 90 programming languages plus English and Chinese. The training mix includes a project-level repository corpus and a fill-in-the-blank objective, giving the models 16K-context completion and infilling behavior that made them useful for IDE-style completion as well as chat. Released as Base and Instruct checkpoints (the Instruct variants arrived January 2024), they set open-source records at the time on HumanEval and related benchmarks. The models are consumed through Hugging Face weights, the DeepSeek API, or local runtimes — by other harnesses rather than as one — and the repository's own activity wound down as DeepSeek moved to later model generations.
