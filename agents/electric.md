---
name: "electric"
slug: "electric"
layout: "agent.njk"
category: "other"
maker: "electric-sql"
license: "Apache-2.0"
url: "https://github.com/electric-sql/electric"
source_code_url: "https://github.com/electric-sql/electric"
source_available: "True"
platforms: []
first_released: "2022-06-01"
current_release: "2026-08-14"
stars: "10329"
language: "Elixir, TypeScript"
homepage: "https://electric.ax"
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: null
pricing: "open-source"
install_method: "docker"
docs_url: "https://electric-sql.com/docs"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "agent_infra"
what_makes_it_special: "Real-time sync engine for Postgres (not a coding agent). Uses 'Shapes' for partial replication, fan-out, and data delivery from Postgres to clients. Core protocol is a low-level HTTP API integrating with CDNs for scalable delivery. CRDT-based sync. Positioned as 'the agent platform built on sync' -- enables apps and AI agents to work with live local data."
---

Electric grew out of the observation that most applications need only a slice of a Postgres database, delivered live, and that no existing tool handled partial replication plus massive fan-out. The sync service streams shape logs (rows matching a shape definition, with position tracking for resume) over an HTTP API designed to be cached by CDNs, so a single Postgres primary can serve read-path sync to very large client counts without exposing Postgres itself. Clients consume shapes directly over HTTP or through TypeScript packages with framework bindings like the React useShape hook. Its users are web and mobile application teams building local-first or collaborative products, and the project has more recently positioned the same sync machinery as a data layer for AI agents that need live application data.
