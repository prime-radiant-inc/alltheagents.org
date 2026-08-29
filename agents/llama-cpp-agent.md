---
name: "LLama Cpp Agent"
slug: "llama-cpp-agent"
layout: "agent.njk"
category: "agent-sdk"
maker: "Maximilian-Winter"
license: "MIT"
url: "https://github.com/Maximilian-Winter/llama-cpp-agent"
source_code_url: "https://github.com/Maximilian-Winter/llama-cpp-agent"
source_available: "yes"
platforms: []
first_released: "2023-12-29"
current_release: "2026-03-09"
stars: "656"
language: "Python"
homepage: null
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "llama-cpp-python, llama.cpp server, TGI, vLLM"
pricing: "open-source"
install_method: "pip"
docs_url: "https://llama-cpp-agent.readthedocs.io/en/latest/"
plugin_docs_url: null
config_docs_url: null
download_url: "https://pypi.org/project/llama-cpp-agent/"
maintained: "dormant"
sources:
  - "jim"
what_makes_it_special: "Python framework for interacting with LLMs — chat, function calling, structured output, RAG, and agentic chains with tools. Key differentiator is guided sampling via grammars and JSON schema generation, enabling most 7B LLMs (even those not fine-tuned for function calling) to perform structured output and function calling. Supports parallel function calling, RAG with ColBERT reranking, and predefined message formatters for many model families (Mistral, ChatML, Vicuna, Llama 2/3, Phi-3, DeepSeek Coder v2). NOTE: No longer maintained — author recommends using ToolAgents instead."
---

The framework addressed a practical problem from the era before function calling was widespread: small local models frequently emitted malformed JSON, so agent chains built on them were unreliable. By constraining token sampling with grammars and JSON schemas during inference, it made structured output and tool invocation a decoding-time guarantee rather than a learned behavior. Developers building local assistants, RAG applications, and tool-using chains on llama.cpp-class hardware used it to add those capabilities without fine-tuning. The project has been abandoned; the author now points users to ToolAgents and other maintained Python agent frameworks.
