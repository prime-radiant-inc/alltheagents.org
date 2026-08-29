---
name: "CodeActAgent"
slug: "codeactagent"
layout: "agent.njk"
category: "agent"
maker: "xingyaoww"
license: "MIT"
url: "https://github.com/xingyaoww/code-act"
source_code_url: "https://github.com/xingyaoww/code-act"
source_available: "True"
platforms: []
first_released: "2024-01-13"
current_release: "2024-05-23"
stars: "1698"
language: "Python"
homepage: null
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "OpenAI-compatible (vLLM, llama.cpp)"
pricing: "open-source"
install_method: "docker"
docs_url: "https://github.com/xingyaoww/code-act/tree/main/docs"
plugin_docs_url: null
config_docs_url: null
download_url: "https://huggingface.co/xingyaoww"
maintained: "dead"
sources:
  - "jim"
what_makes_it_special: "Research project (ICML 2024) proposing executable Python code as a unified action space for LLM agents instead of JSON/text. Agents can revise prior actions or emit new ones through multi-turn interpreter interactions. Up to 20% higher success rate vs Text/JSON across 17 LLMs. Ships CodeActInstruct (7k instruction-tuning dataset) and CodeActAgent models (Mistral-7b recommended, Llama-2-7b) plus a containerized Jupyter kernel execution engine and chat UI."
---

CodeAct demonstrated that letting an LLM emit executable Python instead of JSON or structured text produces stronger agents, because the model can compose actions, inspect results, and revise prior steps over multiple interpreter turns. The repository ships the full research stack: CodeActInstruct, a 7k multi-turn instruction-tuning dataset on Hugging Face; fine-tuned CodeActAgent models on Mistral-7B and Llama-2-7B; the M3ToolEval benchmark tooling; and a Dockerized Jupyter-kernel execution engine behind a chat UI, deployable with vLLM, llama.cpp, Ollama, or Kubernetes. It is a paper artifact rather than a maintained product: 31 commits, no releases, and no updates after April 2024. Its lasting influence is architectural — the code-as-action design carried into OpenHands, built by the same author.
