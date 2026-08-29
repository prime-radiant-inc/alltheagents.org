---
name: "TrueForge"
slug: "trueforge"
layout: "agent.njk"
category: "agent-sdk"
maker: "truefoundry"
license: "MIT"
url: "https://github.com/truefoundry/trueforge"
source_code_url: "https://github.com/truefoundry/trueforge"
source_available: "True"
platforms:
  - "CLI"
  - "Web"
first_released: "2026-07-23"
current_release: "2026-08-27"
stars: 4821
language: "TypeScript"
homepage: "https://trueforge.dev"
mcp_support: "yes"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "yes"
hooks: "no"
plan_mode: "no"
model_providers: "OpenAI, Anthropic, Google Gemini, any OpenAI-compatible endpoint"
pricing: "free"
install_method: "npx (Node >= 22.14), Docker/Docker Compose, or Helm chart on Kubernetes"
docs_url: "https://trueforge.dev"
plugin_docs_url: null
config_docs_url: null
download_url: "https://www.npmjs.com/package/@truefoundry/trueforge-sdk"
maintained: "active"
sources:
  - "hackernews"
what_makes_it_special: "The runtime layer that turns an LLM into a working agent — model calls, MCP tools, skills, sandboxing, approvals, context management, and session state — exposed three ways: a bundled chat UI, an HTTP API with a TypeScript SDK, and an embeddable UI SDK. Runs in local single-process mode with SQLite or hosted mode with Postgres and Redis."
---

TrueForge is TrueFoundry's open-source agent harness: the execution loop behind an agent rather than an agent product itself. It handles model calls across OpenAI, Anthropic, Gemini, and OpenAI-compatible endpoints; remote MCP servers with OAuth; git-backed skills; sandboxing-as-a-tool via Daytona; human approval checkpoints; and context engineering including subagents, deferred tool loading, a Code Mode, and compaction. The same runtime is exposed as a bundled chat UI, an HTTP API with the @truefoundry/trueforge-sdk TypeScript package, and an embeddable @truefoundry/trueforge-ui component, so teams can ship an agent product on top without owning the loop. Local mode runs as a single process with SQLite for development, while hosted mode scales out with Postgres and Redis via Docker Compose or a Helm chart on Kubernetes. Its users are platform teams embedding agents into their own products rather than developers looking for a ready-made coding assistant.
