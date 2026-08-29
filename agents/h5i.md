---
name: "h5i"
slug: "h5i"
layout: "agent.njk"
category: "other"
maker: "h5i-dev"
license: "Apache-2.0"
url: "https://github.com/h5i-dev/h5i"
source_code_url: "https://github.com/h5i-dev/h5i"
source_available: "True"
platforms:
  - "Web"
first_released: "2026-03-11"
current_release: "2026-08-19"
stars: "535"
language: "Rust"
homepage: "https://h5i.dev"
mcp_support: "no"
plugin_support: "yes"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "none"
pricing: "open-source"
install_method: "curl -fsSL https://h5i.dev/install.sh | sh  (or cargo install --path .)"
docs_url: "https://h5i.dev/"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/h5i-dev/h5i/releases/latest"
maintained: "active"
sources:
  - "brad"
what_makes_it_special: "Auditable sandbox for AI coding agents with multiple isolation tiers (workspace, process, supervised, container via rootless Podman, microvm via microsandbox). Includes isolated browser control, end-to-end encrypted P2P sharing, reviewable patches/logs, eBPF runtime detection, and self-hosted runners. Local-first, no SaaS."
---

h5i gives AI agents a browser and execution environment they cannot quietly exceed. Its browser engine is written in Rust without Chromium or V8, acting as its own HTTP client so that each network request is logged as an allow/deny decision before bytes move, producing an audit receipt that distinguishes what the engine claims from what the host observed. The same project provides 'boxes' — sandboxed git worktrees holding code, toolchain, and agent — that can run at five isolation levels (plain workspace, Landlock-seccomp process sandbox, network-namespaced supervised mode, rootless Podman container, or microsandbox microVM), with mandatory escalation rather than silent downgrades. Sessions produce reviewable request logs and audit artifacts, and boxes support encrypted peer-to-peer sharing plus a multi-agent forum mode. It targets teams that need to let agents browse and execute with verifiable evidence of what they actually did.
