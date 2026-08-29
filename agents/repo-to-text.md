---
name: "Repo-To-Text"
slug: "repo-to-text"
layout: "agent.njk"
category: "other"
maker: "kirill-markin"
license: "MIT"
url: "https://github.com/kirill-markin/repo-to-text"
source_code_url: "https://github.com/kirill-markin/repo-to-text"
source_available: "True"
platforms: []
first_released: "2024-06-08"
current_release: "2026-08-12"
stars: "211"
language: "Python"
homepage: "https://pypi.org/project/repo-to-text/"
mcp_support: "False"
plugin_support: "False"
claude_code_plugin: "False"
subagents: "False"
hooks: null
plan_mode: null
model_providers: "none (offline converter; makes no LLM API calls)"
pricing: "Free / open-source"
install_method: "pip install repo-to-text (or via Docker: docker compose build)"
docs_url: "https://pypi.org/project/repo-to-text/"
plugin_docs_url: null
config_docs_url: null
download_url: "https://pypi.org/project/repo-to-text/"
maintained: "active"
sources:
  - "jim"
what_makes_it_special: "Generates an XML-formatted text representation of an entire repository (directory tree + file contents) and copies it to the clipboard, optimized for pasting codebases into LLMs for development and debugging."
---

Repo-To-Text exists because pasting a codebase into a chat window loses the structure models need: it walks the repository, emits the directory tree plus file contents wrapped in XML tags, and copies the result to the clipboard or stdout. Selection follows gitignore semantics extended with its own settings file, so generated artifacts and vendored code can be excluded without touching the real .gitignore. A maximum word count per file splits oversized outputs deterministically. Python developers working with chat-based LLMs use it to hand a whole project to a model in one paste, and its Docker packaging lets CI jobs produce the same snapshot reproducibly. It deliberately contains no agent logic — conversion happens once, locally, before any model sees the text.
