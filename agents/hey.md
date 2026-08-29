---
name: "hey"
slug: "hey"
layout: "agent.njk"
category: "other"
maker: "lnxpy"
license: "MIT"
url: "https://github.com/lnxpy/hey"
source_code_url: "https://github.com/lnxpy/hey"
source_available: "True"
platforms: []
first_released: "2023-04-18"
current_release: "2026-08-16"
stars: "234"
language: "Python"
homepage: "https://pypi.org/project/hey-mindsdb/"
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "MindsDB mdb.ai,OpenAI-compatible"
pricing: "Free"
install_method: "pip install -U hey-mindsdb"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://pypi.org/project/hey-mindsdb/"
maintained: "active"
sources:
  - "github_topic2"
what_makes_it_special: "Free CLI-based AI assistant for pair programming powered by LLMs; defaults to MindsDB's mdb.ai with free tokens; supports quick ask commands and editor-based mode for longer prompts."
---

hey is a small Python CLI that answers questions from an LLM in the terminal. It supports a one-shot mode (hey ask "...") and an editor-based mode for longer prompts, with configuration for the service URL, model, system prompt, and output styling; the default endpoint is MindsDB's mdb.ai, chosen because it offers free tokens, but any OpenAI-compatible base URL and key work. There is no tool use, file access, or agentic behavior — it is a question-and-answer client styled with rich. Built for a hackathon, it remains a lightweight personal utility rather than an actively developed product, and it suits users who want a zero-config way to query an LLM from the shell.
