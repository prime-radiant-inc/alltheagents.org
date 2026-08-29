---
name: "par"
slug: "par"
layout: "agent.njk"
category: "agent-sdk"
maker: "jcz2020"
license: "MIT"
url: "https://github.com/jcz2020/par"
source_code_url: "https://github.com/jcz2020/par"
source_available: "True"
platforms:
  - "IDE"
first_released: "2026-05-28"
current_release: "2026-08-14"
stars: "67"
language: "OCaml"
homepage: "https://jcz2020.github.io/par/"
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: "False"
subagents: "True"
hooks: "True"
plan_mode: "no"
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

PAR positions itself as the agent plumbing layer that OCaml's ecosystem lacked, handling the ReAct loop, tool dispatch, multi-provider LLM calls, persistence, and an event bus so developers write only tools and workflows. Its OCaml 5.4 core uses effects and Eio structured concurrency, eliminating orphan fibers and callback nesting, and compiles shell commands into a type-safe ADT that rules out injection at compile time. Nine built-in middleware cover logging, retry, rate limiting, timeouts, argument and output validation, PII masking, and sanitization at every model and tool boundary, while SQLite persistence and an audit log make runs reproducible. Python bindings on PyPI open the runtime to the larger ecosystem, and a companion project, par-code, builds a CLI coding agent on top. Its audience is OCaml developers and Python teams that want a verified, concurrency-safe agent substrate.
