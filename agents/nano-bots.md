---
name: "Nano-Bots"
slug: "nano-bots"
layout: "agent.njk"
category: "agent"
maker: "icebaker"
license: null
url: "https://github.com/icebaker/nano-bots"
source_code_url: "https://github.com/icebaker/nano-bots"
source_available: "True"
platforms:
  - "IDE"
first_released: "2023-06-02"
current_release: "2023-06-04"
stars: "7"
language: "YAML, Ruby"
homepage: "https://nbots.io"
mcp_support: "no"
plugin_support: "True"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "OpenAI ChatGPT, Google Gemini"
pricing: "free"
install_method: "Download a YAML cartridge from the repo (or copy its contents), then run via an implementation (CLI, API, editor plugin, or Clinic live editor)"
docs_url: "https://spec.nbots.io/"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/icebaker/nano-bots/tree/main/cartridges"
maintained: "active"
sources:
  - "jim"
what_makes_it_special: "Repository for Nano Bots' Cartridges — small AI-powered bots shareable as a single YAML file, supporting multiple LLM providers and tool/function calling. Implementations exist for Sublime Text and VS Code, plus a CLI, API, and Clinic live editor. Recommends CC0-1.0 for individual cartridges."
---

Nano Bots defines bots as single YAML cartridge files that anyone can download, copy, or author and run through any conforming implementation. The specification covers adapters, provider configuration, tool/function calling, and a marketplace metadata section with tags and honestly auto-generated sample outputs. A profile.yml convention organizes community cartridges under author namespaces on nbots.io. Because prompts' intellectual property status is unsettled, the project recommends authors license individual cartridges under SPDX terms such as CC0-1.0. The repo itself has only nine commits, and the cartridge collection has not changed since mid-2023.
