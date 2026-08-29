---
name: "Dagger"
slug: "dagger"
layout: "agent.njk"
category: "other"
maker: "dagger"
license: "Apache-2.0"
url: "https://github.com/dagger/dagger"
source_code_url: "https://github.com/dagger/dagger"
source_available: "Yes"
platforms:
  - "Web"
first_released: "2019-11-20"
current_release: "2026-08-19"
stars: "16182"
language: "Go"
homepage: "https://dagger.io"
mcp_support: null
plugin_support: null
claude_code_plugin: null
subagents: null
hooks: null
plan_mode: null
model_providers: null
pricing: "open-source (Apache-2.0)"
install_method: "brew"
docs_url: "https://docs.dagger.io"
plugin_docs_url: null
config_docs_url: null
download_url: "https://docs.dagger.io/install"
maintained: "active"
sources:
  - "namphuong"
what_makes_it_special: "Programmable, local-first automation engine for software delivery that provides SDKs in 8 languages, typed artifacts, incremental content-addressed caching, and built-in OpenTelemetry tracing — allowing the same workflows to run identically across local, CI, and cloud environments."
---

Dagger is a programmable automation engine for software delivery: teams write build, test, and deploy pipelines as code using SDKs in Go, Python, TypeScript, PHP, Java, .NET, Elixir, or Rust, and the engine executes each operation in containerized, sandboxed steps with incremental content-addressed caching. Every operation emits OpenTelemetry traces, which gives CI-grade observability without extra instrumentation, and pipelines run identically locally, in CI, or in Dagger Cloud. Although its core identity is CI/CD infrastructure rather than an agent, the project now embraces LLM workflows — including first-class support for wiring coding agents into DAG pipelines — which is why it appears in harnesses-adjacent catalogs. It is Apache-2.0, written in Go, and widely used by platform teams replacing brittle YAML pipelines.
