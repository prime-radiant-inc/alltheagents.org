---
name: "invincat"
slug: "invincat"
layout: "agent.njk"
category: "agent"
maker: "dog-qiuqiu"
license: "MIT"
url: "https://github.com/dog-qiuqiu/invincat"
source_code_url: "https://github.com/dog-qiuqiu/invincat"
source_available: "True"
platforms:
  - "CLI"
first_released: "2026-04-16"
current_release: "2026-05-26"
stars: "153"
language: "Python"
homepage: null
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: "False"
subagents: "True"
hooks: "no"
plan_mode: "True"
model_providers: "OpenAI, Anthropic, Google, DeepSeek, OpenRouter"
pricing: "Free / open-source"
install_method: "pip install invincat-cli (Python 3.11+); or clone + pip install -e ."
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "github_deep"
what_makes_it_special: "Terminal-native AI coding assistant with hierarchical memory (user + project scopes, background memory agent), goal mode for long-running objectives, 4 built-in subagents (explorer, worker, researcher, document-worker), skills system (docx/pdf/pptx/xlsx), WeCom bot daemon for remote turns, scheduled tasks in natural language."
---

invincat targets developers who want an agent that remembers and persists rather than restarting each session. Memory splits into user and project scopes, with a background agent distilling learnings after non-trivial turns and an optional dedicated memory model. Plan mode produces a read-only, approval-gated checklist before implementation; goal mode keeps the agent driving toward long-running objectives across turns, with state persisted per thread. Four built-in subagents split exploration, implementation, research, and office-document work, and a WeCom bridge lets enterprise-WeChat messages drive sessions remotely. Scheduled tasks accept natural-language timing, and skills handle PDF, DOCX, PPTX, and XLSX work.
