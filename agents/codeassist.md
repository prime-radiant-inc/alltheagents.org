---
name: "codeassist"
slug: "codeassist"
layout: "agent.njk"
category: "other"
maker: "gensyn-ai"
license: "MIT"
url: "https://github.com/gensyn-ai/codeassist"
source_code_url: "https://github.com/gensyn-ai/codeassist"
source_available: "yes"
platforms: []
first_released: "2025-10-31"
current_release: "2026-03-02"
stars: "702"
language: "Python"
homepage: null
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "None (trains a local model from user interaction)"
pricing: "open-source"
install_method: "docker"
docs_url: "https://docs.gensyn.ai/testnet/codeassist"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "dormant"
sources:
  - "github_topic5"
what_makes_it_special: "Completely private, local AI coding assistant by Gensyn that writes directly in your editor and learns from every keystroke. Continuous learning from interaction (every keystroke, edit, deletion, or untouched output is a training signal). Apprentice model — behaves like a collaborator learning your craft. Trains a personal local model checkpoint per episode and optionally uploads to HuggingFace. NOTE: Project appears sunset — 'As we shift focus to Mainnet, we have stopped tracking new CodeAssist participation on Testnet.'"
---

CodeAssist was Gensyn's demonstration of decentralized training applied to coding assistance: a local assistant that writes directly into the editor relative to the cursor and adapts to the user's style through reinforcement signals from every keystroke, acceptance, and deletion. Each interaction episode trains a personal model checkpoint on the local machine, optionally uploaded to Hugging Face, with no code leaving the machine. Operationally it functioned as Gensyn's Testnet participation app, where users solved practice problems and earned on-chain participation credit, tying model improvement to network participation. Gensyn has stopped tracking new CodeAssist participation as the network shifts to Mainnet, and the repository — 27 commits, no releases — is no longer under development.
