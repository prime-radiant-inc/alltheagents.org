---
name: "Plandex"
slug: "plandex"
layout: "agent.njk"
category: "agent"
maker: "plandex-ai"
license: "MIT"
url: "https://github.com/plandex-ai/plandex"
source_code_url: "https://github.com/plandex-ai/plandex"
source_available: "True"
platforms:
  - "CLI"
first_released: "2023-10-24"
current_release: "2025-10-03"
stars: null
language: "Go"
homepage: "https://plandex.ai"
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "True"
model_providers: "Anthropic, OpenAI, Google, OpenRouter, open source providers"
pricing: "Free / open-source; self-hosted with your own API keys"
install_method: "curl -sL https://plandex.ai/install.sh | bash"
docs_url: "https://docs.plandex.ai/"
plugin_docs_url: null
config_docs_url: null
download_url: "https://plandex.ai/install.sh"
maintained: "active"
sources:
  - "jqueryscript"
  - "brad"
  - "jim"
  - "ishandutta"
  - "tiennm"
what_makes_it_special: "2M token effective context window with tree-sitter project maps (30+ languages); cumulative diff sandbox separating AI changes from project files until ready; full version control for plans with branches; handles very large projects."
---

Plandex was built for large, multi-file changes that outgrow chat-window coding: tasks spanning dozens of files where a single bad edit deep in the sequence ruins the result. Its core mechanism is a cumulative diff sandbox — AI changes accumulate separately from project files until explicitly applied, with command execution controlled so missteps are easy to roll back — plus full version control over plans, including branches for trying alternative approaches or comparing models on the same task. A 2M-token effective context window over tree-sitter project maps handles codebases of 20M+ tokens, and autonomy is configurable from full-auto mode (with auto-debugging through Chrome for browser apps) down to step-by-step approval. Plandex Cloud wound down in October 2025, leaving self-hosted/local mode with your own API keys as the supported path, and the MIT-licensed v2 remains maintained for that audience.
