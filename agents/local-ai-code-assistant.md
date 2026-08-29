---
name: "local-ai-code-assistant"
slug: "local-ai-code-assistant"
layout: "agent.njk"
category: "agent"
maker: "MIKOTOKAWAII25"
license: "MIT"
url: "https://github.com/MIKOTOKAWAII25/local-ai-code-assistant"
source_code_url: "https://github.com/MIKOTOKAWAII25/local-ai-code-assistant"
source_available: "False"
platforms: []
first_released: "2026-06-28"
current_release: "2026-08-20"
stars: "121"
language: "HTML"
homepage: null
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "False"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "Hugging Face, Ollama, local GGUF/GPTQ"
pricing: "Free (MIT)"
install_method: "Download from release page; extract; run executable; select models from built-in model browser or point to local files"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://mikotokawaii25.github.io/local-ai-code-assistant/"
maintained: "active"
sources:
  - "github_topic5"
what_makes_it_special: "Desktop AI 'weaver' (CodeLoom) for multi-model development; orchestrates multiple open-source LLMs (Mistral, Llama, Phi) into a single fully offline desktop coding environment; multi-weave architecture with up to 5 concurrent model sessions; contextual thread fusion between models; privacy-first with no telemetry; cross-platform with 12-language UI"
---

CodeLoom is built for developers who want multi-model AI assistance with zero cloud dependency: all inference runs locally through llama.cpp, ExLlama, or MLX backends, with no telemetry, accounts, or network calls. The loom metaphor is structural, not decorative - warp slots hold large models for architecture and refactoring while weft slots run 1-3B models for fast completion, and a cross-thread shuttle passes context between them so a small model's draft can be refined by a larger one. Up to five concurrent sessions can debate or collaborate, and prompt looms fan one task out to several models for parallel review. Models import from Hugging Face, Ollama, or local GGUF/GPTQ files with automatic quantization selection based on available VRAM. The repository is primarily a distribution and marketing page (the actual code ships as release downloads), and its Claude-related SEO tags contradict the open-models pitch, warranting caution.
