---
name: "SWE-ReX"
slug: "swe-rex"
layout: "agent.njk"
category: "other"
maker: "SWE-agent"
license: "MIT"
url: "https://github.com/SWE-agent/SWE-ReX"
source_code_url: "https://github.com/SWE-agent/SWE-ReX"
source_available: "True"
platforms:
  - "Web"
first_released: "2024-10-14"
current_release: "2026-08-17"
stars: "576"
language: "Python"
homepage: "https://swe-rex.com/"
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: null
pricing: "open-source"
install_method: "pip"
docs_url: "https://swe-rex.com/"
plugin_docs_url: null
config_docs_url: null
download_url: "https://pypi.org/project/swe-rex/"
maintained: "active"
sources:
  - "github_topic2"
what_makes_it_special: "Runtime interface for sandboxed shell environments allowing AI agents to run any command locally or remotely (Docker, AWS, Modal, etc.) with identical agent code; supports massively parallel agent runs, interactive CLI tools (ipython, gdb), and multiple parallel shell sessions; disentangles agent logic from infrastructure"
---

SWE-ReX came out of the SWE-agent project's observation that infrastructure churn, not model capability, caused most harness failures at scale. It defines a runtime interface between an agent and its shell: a persistent, sandboxed process manager that detects command completion, extracts output and exit codes, supports interactive programs like ipython and gdb, and keeps several shell sessions open per agent. The same agent code runs locally or against Docker containers, AWS Fargate, or Modal sandboxes, with a pluggable backend interface for adding more, which is what lets benchmark sweeps fan out to dozens of instances in parallel. The project is MIT-licensed, installable from PyPI with per-backend extras, and documented at swe-rex.com. Agent-framework builders — including mini-SWE-agent and SWE-smith — embed it rather than reimplementing sandbox plumbing.
