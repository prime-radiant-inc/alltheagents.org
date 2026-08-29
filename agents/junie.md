---
name: "junie"
slug: "junie"
layout: "agent.njk"
category: "agent"
maker: "JetBrains"
license: "Proprietary (JetBrains)"
url: "https://github.com/JetBrains/junie"
source_code_url: "https://github.com/JetBrains/junie"
source_available: "False"
platforms:
  - "CLI"
  - "IDE"
first_released: "2025-04-07"
current_release: "2026-08-19"
stars: "397"
language: "Shell"
homepage: "https://junie.jetbrains.com"
mcp_support: null
plugin_support: null
claude_code_plugin: "False"
subagents: null
hooks: null
plan_mode: "yes"
model_providers: "Anthropic, OpenAI, Google, xAI, OpenRouter, Copilot"
pricing: "freemium"
install_method: "curl -fsSL https://junie.jetbrains.com/install.sh | bash (macOS/Linux), Homebrew, or npm install -g @jetbrains/junie"
docs_url: "https://junie.jetbrains.com/docs/"
plugin_docs_url: null
config_docs_url: null
download_url: "https://junie.jetbrains.com/install.sh"
maintained: "active"
sources:
  - "github_topic2"
what_makes_it_special: "LLM-agnostic terminal-native AI coding agent by JetBrains; IDE/CI-CD integration; GitHub Action for auto-responding to issues/PRs/CI failures; multiple update channels (stable, EAP, nightly, experimental)."
---

This repository is the front door for Junie, JetBrains' LLM-agnostic coding agent — installer scripts for stable, EAP, nightly, and experimental channels, version registries, and issue tracking, while the agent implementation itself stays closed under JetBrains AI Service Terms. The agent runs in terminals, JetBrains IDEs, and CI: a GitHub Action lets Junie respond to issues, review PRs, and react to CI failures autonomously. Authentication goes through JetBrains Account, Junie API keys, or BYOK across Anthropic, OpenAI, Google, xAI, OpenRouter, and Copilot. Users track bugs via /feedback or GitHub issues, and the Discord community handles support alongside docs at junie.jetbrains.com/docs.
