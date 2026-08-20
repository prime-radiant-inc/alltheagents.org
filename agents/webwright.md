---
name: "Webwright"
slug: "webwright"
layout: "agent.njk"
category: "agent"
maker: "microsoft"
license: "MIT"
url: "https://github.com/microsoft/Webwright"
source_code_url: "https://github.com/microsoft/Webwright"
source_available: True
platforms:
  - "Web"
first_released: "2026-04-08"
current_release: "2026-08-03"
stars: "5930"
language: "Python"
homepage: null
mcp_support: "no"
plugin_support: "yes"
claude_code_plugin: "yes"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "OpenAI, Anthropic, OpenRouter"
pricing: "open-source"
install_method: "pip"
docs_url: "https://microsoft.github.io/Webwright/"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "github_topic2"
what_makes_it_special: "Code-as-action browser agent: instead of predicting one browser action at a time, the LLM writes and debugs Playwright scripts via a terminal, treating the browser as disposable and code+logs as the persistent workspace artifact. Ultra-minimal (~450-line core, no hidden frameworks — just httpx/pydantic/playwright/typer). Skill Factory distills solved scripts into reusable, verified, parameterized code skills that run standalone without a model. SOTA: 86.7% on Online-Mind2Web. Ships Claude Code and Codex plugin manifests."
---

Code-as-action browser agent: instead of predicting one browser action at a time, the LLM writes and debugs Playwright scripts via a terminal, treating the browser as disposable and code+logs as the persistent workspace artifact. Ultra-minimal (~450-line core, no hidden frameworks — just httpx/pydantic/playwright/typer). Skill Factory distills solved scripts into reusable, verified, parameterized code skills that run standalone without a model. SOTA: 86.7% on Online-Mind2Web. Ships Claude Code and Codex plugin manifests.
