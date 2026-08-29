---
name: "AutoStartup"
slug: "autostartup"
layout: "agent.njk"
category: "agent"
maker: "jawerty"
license: null
url: "https://github.com/jawerty/AutoStartup"
source_code_url: "https://github.com/jawerty/AutoStartup"
source_available: "True"
platforms:
  - "IDE"
first_released: "2023-08-17"
current_release: "2023-08-17"
stars: "60"
language: "Python"
homepage: null
mcp_support: "False"
plugin_support: "False"
claude_code_plugin: "False"
subagents: "False"
hooks: "False"
plan_mode: "False"
model_providers: "Llama 2 (via HuggingFace)"
pricing: "Free/open source (requires own GPU or Google Colab)"
install_method: "pip3 install -r requirements.txt && python3 main.py (or Google Colab notebook)"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/jawerty/AutoStartup"
maintained: "dormant"
sources:
  - "github_topic2"
what_makes_it_special: "100% Llama 2 inference with no OpenAI API keys needed; autonomously generates startup ideas, business plans, and React codebases from simple user intuition using lean startup methodologies (criticize loops, investor approval, pivoting)."
---

AutoStartup was a 2023 experiment by jawerty (Jared Vasquez) exploring whether a startup could be generated end-to-end from a one-line intuition using only locally hosted Llama 2 - no OpenAI keys. A criticize-revise-pitch loop (AutoGPT-style) iterates a business plan against an investor prompt until approval, then generates a React codebase via the author's 10x-React-Engineer project, with vector-search memory pairing past successes and criticisms into future pitches. Llama 2 13B inference runs locally or via a provided Colab notebook, making the whole pipeline local and key-free. The project was a demo built during a livestream, is admittedly buggy, and has seen only six commits. It is of historical interest as an early fully-local autonomous startup generator rather than a maintained tool.
