---
name: "cortex"
slug: "cortex"
layout: "agent.njk"
category: "other"
maker: "urbint"
license: "MIT"
url: "https://github.com/urbint/cortex"
source_code_url: "https://github.com/urbint/cortex"
source_available: "True"
platforms: []
first_released: "2017-04-14"
current_release: "2022-09-14"
stars: "383"
language: "Elixir"
homepage: null
mcp_support: "no"
plugin_support: "True"
claude_code_plugin: "False"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "None (deterministic file-watcher, no AI)"
pricing: "Free / open-source"
install_method: "Add {:cortex, '~> 0.1', only: [:dev, :test]} to mix.exs"
docs_url: "https://github.com/urbint/cortex#readme"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/urbint/cortex"
maintained: "dead"
sources:
  - "github_deep"
what_makes_it_special: "Intelligent coding assistant for Elixir that automatically recompiles/reloads modified files and runs the appropriate tests, with pluggable adapters for custom builds and a focus mode for filtering test runs."
---

The cortex entry in this census is Urbint's Elixir development tool, whose 'intelligent coding assistant' description dates from 2017 and has nothing to do with LLMs. Running alongside `iex -S mix` as a dev dependency, it watched the filesystem, recompiled and hot-reloaded modified modules in the running session, and triggered the relevant tests automatically under MIX_ENV=test, removing the manual compile-test cycle from Elixir work. Pluggable adapters let teams wire custom build steps, and commands like Cortex.all and Cortex.focus scoped what reran. Development wound down years before Urbint archived the repository on November 25, 2025. It appears in the census as 'other': real developer automation whose name and tagline merely collide with the modern agent vocabulary.
