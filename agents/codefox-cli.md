---
name: "CodeFox-CLI"
slug: "codefox-cli"
layout: "agent.njk"
category: "other"
maker: "codefox-lab"
license: "MIT"
url: "https://github.com/codefox-lab/CodeFox-CLI"
source_code_url: "https://github.com/codefox-lab/CodeFox-CLI"
source_available: "True"
platforms:
  - "CLI"
  - "Web"
first_released: "2026-02-16"
current_release: "2026-03-22"
stars: "43"
language: "Python"
homepage: "http://code-fox.online"
mcp_support: null
plugin_support: null
claude_code_plugin: null
subagents: null
hooks: null
plan_mode: null
model_providers: "Ollama, Gemini, OpenRouter"
pricing: "free"
install_method: "uv tool install codefox or python3 -m pip install codefox"
docs_url: "https://github.com/codefox-lab/CodeFox-CLI/wiki"
plugin_docs_url: null
config_docs_url: "https://github.com/codefox-lab/CodeFox-CLI/wiki"
download_url: "https://github.com/codefox-lab/CodeFox-CLI"
maintained: "active"
sources:
  - "github_topic3"
what_makes_it_special: "Diff-aware AI code review tool that uses relevant codebase context rather than isolated files. CLI-first design suited for terminal and CI/CD workflows. Runs locally with Ollama for privacy or with cloud LLMs. Configurable review focus (security, performance, style) and can suggest fixes, not just flag issues."
---

CodeFox-CLI is built for review workflows in the terminal and CI rather than in-editor assistance. For each change it collects the git diff, retrieves related codebase context using fastembed embeddings, and produces prioritized findings with optional fix suggestions. Review focus is configurable — security, performance, style — and inference runs either fully local through Ollama or through cloud providers Gemini and OpenRouter, with fastembed handling embeddings. It integrates as a GitHub Action ('CodeFox AI Review') and with GitLab pipelines, and configuration (providers, models, review rules, prompts) is documented in a GitHub wiki. The project is an MIT-licensed Python package on PyPI, installed via pip or uv.
