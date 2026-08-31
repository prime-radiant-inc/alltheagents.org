---
name: "Agents by Hugging Face"
slug: "agents-by-hugging-face"
layout: "agent.njk"
category: "agent-sdk"
maker: null
license: "Apache-2.0"
url: "https://huggingface.co/docs/transformers/main_classes/agent"
source_code_url: null
source_available: "True"
platforms:
  - "IDE"
  - "Web"
first_released: null
current_release: null
stars: null
language: "Python"
homepage: null
mcp_support: "no"
plugin_support: "True"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "Hugging Face (HfApiEngine / Inference API), Local (TransformersEngine)"
pricing: "Free / open-source"
install_method: "pip install transformers (stable); or install from source for the main version"
docs_url: "https://huggingface.co/docs/transformers/main/en/main_classes/agent"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/huggingface/transformers"
maintained: "active"
sources:
  - "jim"
what_makes_it_special: "Experimental agent API in Hugging Face Transformers offering CodeAgent (one-shot code generation and execution) and ReactAgent (step-by-step ReAct with JSON or Python tool calls); integrates with Gradio, Langchain, Hugging Face Spaces, and HF Hub tools via ToolCollection"
---

As LLMs gained tool-use competence, Hugging Face added an agents module to Transformers so models could chain its ecosystem of tools — text downloaders, speech-to-text, image generation, and community tools from the Hub — inside a reasoning loop. ReactAgent follows the think-act-observe pattern with JSON tool calls; CodeAgent instead has the model emit Python code that runs in a restricted interpreter with access limited to the toolbox and safe built-ins, which lets one generation invoke several tools. Custom tools plug in via the agent.tool decorator or load_tool from the Hub. The API was later deprecated and removed from Transformers in favor of the dedicated smolagents library, which carries the same CodeAgent and tool-calling design forward. Its main audience today is people reading older codebases and papers built on the Transformers agents API.
