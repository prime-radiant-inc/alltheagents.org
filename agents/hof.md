---
name: "hof"
slug: "hof"
layout: "agent.njk"
category: "other"
maker: "hofstadter-io"
license: "Apache-2.0"
url: "https://github.com/hofstadter-io/hof"
source_code_url: "https://github.com/hofstadter-io/hof"
source_available: "True"
platforms:
  - "IDE"
first_released: "2020-02-06"
current_release: "2026-05-05"
stars: "613"
language: "Go"
homepage: "https://hofstadter.io"
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "none (hof chat is alpha, provider not documented)"
pricing: "open-source"
install_method: "brew"
docs_url: "https://docs.hofstadter.io"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/hofstadter.io/hof/releases"
maintained: "active"
sources:
  - "github_topic4"
what_makes_it_special: "Unifies data models, schemas, deterministic and agentic code generation, and a task/DAG workflow engine all powered by CUE. Includes a TUI, chat-based AI co-creation, and VS Code extension."
---

hof is a Go CLI built on the CUE constraint language that combines schema definition, data modeling, code generation, and workflow execution in one tool. Schemas and values declared in CUE feed deterministic template-based generation (hof gen), versioned data models with checkpointing and diffing (hof datamodel), and a DAG task engine (hof flow) built on cue/flow, so code generation, validation, and automation all read from the same source of truth. An alpha chat mode adds LLM-assisted code generation alongside the template engine, and a TUI supports interactive exploration of CUE values. It is used by teams that want generated code, APIs, and workflow definitions to stay consistent with a single declarative model, with the AI chat positioned as a complement to — not a replacement for — the deterministic pipeline.
