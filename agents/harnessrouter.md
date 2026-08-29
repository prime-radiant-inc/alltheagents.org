---
name: "HarnessRouter"
slug: "harnessrouter"
layout: "agent.njk"
category: "multiplexer"
maker: "harnessrouter"
license: "Apache-2.0"
url: "https://github.com/harnessrouter/harnessrouter"
source_code_url: "https://github.com/harnessrouter/harnessrouter"
source_available: "True"
platforms:
  - "Web"
  - "CLI"
first_released: "2026-08-09"
current_release: "2026-08-28"
stars: 634
language: "Python"
homepage: "https://harnessrouter.ai/"
mcp_support: null
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "BYOK — delegates to the installed harnesses (Codex, Claude Code, Hermes, Pi, DeepSeek Harness, OpenCode)"
pricing: "free"
install_method: "docker run harnessrouter/harnessrouter (console on port 3000, loopback-bound by default)"
docs_url: "https://github.com/harnessrouter/harnessrouter/blob/main/README.md"
plugin_docs_url: null
config_docs_url: null
download_url: "https://hub.docker.com/r/harnessrouter/harnessrouter"
maintained: "active"
sources:
  - "hackernews"
what_makes_it_special: "The reference implementation of the Unified Harness Protocol (UHP), an open standard: it runs multiple agent harnesses through one OpenAI Responses-compatible API with sessions, streaming, cancellation, idempotency, and failure handling, so any harness is callable uniformly. Bring your own keys, no account, no cloud, no telemetry."
---

HarnessRouter Community Edition is the self-hosted Apache-2.0 sibling of the hosted HarnessRouter Cloud, and its purpose is to make every agent CLI look identical to callers. The Docker container installs Codex, Claude Code, Hermes, Pi, DeepSeek Harness, and OpenCode on first run (each under its own upstream license — the CLIs are not redistributed), then exposes them through a single OpenAI Responses-compatible API at /v1/responses with harness CRUD, sessions, streaming, cancellation, idempotency, and failure handling, plus a thin web console over the same API. The project is also the reference implementation of the Unified Harness Protocol, an open standard (spec version 2026-08-11) that this repo passes at conformance class Full. Sessions run as real POSIX workspaces with bash and git, isolated per session, with state in SQLite on a Docker volume; it is built for teams that want to script or productize multiple harnesses behind one gateway on their own infrastructure.
