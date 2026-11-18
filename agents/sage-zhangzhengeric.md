---
name: "Sage"
slug: "sage-zhangzhengeric"
layout: "agent.njk"
category: "agent"
maker: "ZHangZHengEric"
license: "MIT"
url: "https://github.com/ZHangZHengEric/Sage"
source_code_url: "https://github.com/ZHangZHengEric/Sage"
source_available: "True"
homepage: "https://zhangzhengeric.github.io/Sage/"
docs_url: "https://zhangzhengeric.github.io/Sage/en/"
download_url: "https://github.com/ZHangZHengEric/Sage/releases/latest"
install_method: "Download the Desktop installer from GitHub releases (macOS arm64/x86_64, Windows x86_64, Linux arm64/x86_64; Python backend bundled), or run from source: git clone, python -m pip install -e '.[desktop]' plus Flutter for Desktop, or -e '.[server]' plus MySQL and Node.js 22.12+ for Server"
platforms:
  - "Desktop"
  - "Web"
autonomy_level:
  - "agentic"
  - "autonomous-background"
specialization: "general"
language: "Python"
first_released: "2025-05-25"
current_release: "2026-11-13"
maintained: "active"
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: null
subagents: "True"
hooks: "True"
plan_mode: "True"
plugin_docs_url: "https://zhangzhengeric.github.io/Sage/en/architecture/PLUGINS.html"
config_docs_url: "https://zhangzhengeric.github.io/Sage/en/CONFIGURATION.html"
model_providers: "OpenAI Chat Completions, OpenAI Responses, Anthropic Messages, Gemini GenerateContent"
pricing: "free"
stars: "1217"
sources:
  - "github-issue"
last_verified: "2026-11-18"
date_added: "2026-11-18"
what_makes_it_special: "Sage provides an agent runtime and a separate Runner–Evaluator–Tuner workflow for evaluating versioned Agent-package changes. Candidate versions and evaluation evidence are retained, while adoption remains an explicit user decision."
---

Sage is an RSI Agent Harness: a Python runtime (SAgents) executes versioned Agent packages — instructions, model routes, tools, and Skills declared in YAML — reached through a Flutter desktop app with an agent workspace and PTY terminal, a multi-user web server with Agent Studio, or direct embedding in a Python application. Runs stream tool progress through built-in file, shell, planning, and MCP tools under host-managed sandboxes, with stateful sessions, approval pauses, and multi-agent teams. On top of that runtime, the RSI workflow runs controlled improvement experiments: runner sessions execute the current package, independent evaluator sessions grade real executions against rubrics, and a tuner proposes in-scope edits that a human then applies or discards by hand. The MIT-licensed project is developed by a small contributor team around Eric ZZ (ZHangZHengEric), ships installers for macOS, Windows, and Linux alongside a GitHub Pages docs site and Slack community, and suits developers who want a self-hosted harness whose improvement loop they can inspect and veto.
