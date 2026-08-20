---
name: "par"
slug: "par"
layout: "agent.njk"
category: "agent"
maker: "jcz2020"
license: "MIT"
url: "https://github.com/jcz2020/par"
source_code_url: "https://github.com/jcz2020/par"
source_available: True
platforms:
  - "IDE"
first_released: "2026-05-28"
current_release: "2026-08-14"
stars: "67"
language: "OCaml"
homepage: "https://jcz2020.github.io/par/"
mcp_support: True
plugin_support: True
claude_code_plugin: False
subagents: True
hooks: True
plan_mode: null
model_providers: "OpenAI, Anthropic, Ollama"
pricing: "Free/open-source (MIT)"
install_method: "pip install par-runtime (Python); opam pin add par https://github.com/jcz2020/par.git (OCaml); curl installer script; or build from source (git clone + make install-dev)"
docs_url: "https://jcz2020.github.io/par/"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "github_topic4"
what_makes_it_special: "Modular, type-safe agent runtime for building LLM-powered applications ('LangChain + LangGraph for OCaml'). Written in OCaml 5.4 using Eio structured concurrency (no callback hell, compile-time type safety), usable from both OCaml and Python. Features type-safe shell commands (ADT-based, injection-free), structured concurrency with no orphan fibers, 23 built-in tools, and 9 middleware."
---

Modular, type-safe agent runtime for building LLM-powered applications ('LangChain + LangGraph for OCaml'). Written in OCaml 5.4 using Eio structured concurrency (no callback hell, compile-time type safety), usable from both OCaml and Python. Features type-safe shell commands (ADT-based, injection-free), structured concurrency with no orphan fibers, 23 built-in tools, and 9 middleware.
