---
name: "django-completion"
slug: "django-completion"
layout: "agent.njk"
category: "other"
maker: "soldatov-ss"
license: "MIT"
url: "https://github.com/soldatov-ss/django-completion"
source_code_url: "https://github.com/soldatov-ss/django-completion"
source_available: "True"
platforms: []
first_released: "2026-04-25"
current_release: "2026-08-01"
stars: "40"
language: "Python"
homepage: "https://soldatov-ss.github.io/django-completion/"
mcp_support: "False"
plugin_support: "False"
claude_code_plugin: "False"
subagents: "False"
hooks: null
plan_mode: "False"
model_providers: null
pricing: "Free"
install_method: "pip install django-completion or uv add django-completion; add django_completion to INSTALLED_APPS; then python manage.py autocomplete install"
docs_url: "https://soldatov-ss.github.io/django-completion/"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/soldatov-ss/django-completion"
maintained: "active"
sources:
  - "github_topic4"
what_makes_it_special: "Django manage.py context tool for coding agents and tab completion. Provides a cache file (.django-completion-cache.json) that AI agents read to learn all management commands, flags, and migration names without booting Django (readable in under a millisecond). Works even when settings are broken or dependencies are missing. No telemetry, network calls, or database access. Also provides project-aware bash/zsh tab completion for custom commands, flags, app labels, and migration names."
---

Coding agents routinely misinvoke django-admin because the available commands, flags, and migration names live only in --help output, which is expensive to discover at runtime. django-completion pre-computes that inventory into a JSON cache in the repo, so an agent reads one small file and emits correct manage.py commands and migration references on the first try. The same cache powers zsh/bash tab completion for human developers, which keeps the tool useful outside agent workflows. It is aimed at Django maintainers who wire context files into their agents' system prompts or toolchains.
