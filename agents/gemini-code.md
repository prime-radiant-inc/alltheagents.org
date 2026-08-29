---
name: "gemini-code"
slug: "gemini-code"
layout: "agent.njk"
category: "agent"
maker: "raizamartin"
license: "MIT"
url: "https://github.com/raizamartin/gemini-code"
source_code_url: "https://github.com/raizamartin/gemini-code"
source_available: "True"
platforms: []
first_released: "2025-03-29"
current_release: "2025-03-31"
stars: "546"
language: "Python"
homepage: null
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "Google"
pricing: "BYOK"
install_method: "pip install gemini-code"
docs_url: "https://blossom-tarsier-434.notion.site/Gemini-Code-1c6c13716ff180db86a0c7f4b2da13ab"
plugin_docs_url: null
config_docs_url: null
download_url: "https://pypi.org/project/gemini-code/"
maintained: "active"
sources:
  - "github_deep"
what_makes_it_special: "Terminal-based AI coding assistant powered by Gemini that uses the model's native function calling to automatically execute file, system, and test operations behind the scenes, aiming for a Claude Code-like experience."
---

gemini-code was one of the first community attempts to reproduce the Claude Code experience on Google's models: a Python terminal assistant that chats, plans in-model, and invokes file, directory, shell, lint, and pytest tools automatically through Gemini's function-calling API. Sessions keep history and render markdown, users can switch models with --model, and installation is a single pip install with a Google API key. Development stopped almost where it started — 13 commits across two days in March 2025, no releases, and six open issues — so it survives as a compact reference implementation of a function-calling coding loop rather than a working tool.
