---
name: "fusil"
slug: "fusil"
layout: "agent.njk"
category: "other"
maker: "devdanzin"
license: "GPL-2.0"
url: "https://github.com/devdanzin/fusil"
source_code_url: "https://github.com/devdanzin/fusil"
source_available: "True"
platforms: []
first_released: "2024-11-08"
current_release: "2026-08-19"
stars: "40"
language: "Python"
homepage: null
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: null
pricing: "open-source"
install_method: "pip install -e '.[numpy,h5py]' (requires Python 3.13+)"
docs_url: "https://github.com/devdanzin/fusil"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/devdanzin/fusil"
maintained: "active"
sources:
  - "github_topic4"
what_makes_it_special: "Revived Python fuzzing framework focused on finding crashes in CPython, C-extension modules, the CPython Tier-2 JIT, and OOM error paths. Multi-agent async-message-based fuzzing architecture with adaptive aggressivity driven by per-session scoring. Generates standalone test scripts run as sandboxed child processes. NOTE: This is a fuzzing framework, not a coding agent harness."
---

The original fusil fuzzing framework by Victor Stinner was dormant for years; this revival concentrates it on hunting crashes in CPython, C-extension modules, the Tier-2 JIT, and allocation-failure error paths. Sessions compose agents that exchange asynchronous messages, with per-session scores driving adaptive aggressivity, and each fuzzing session emits a standalone test script executed as a sandboxed child process with memory, CPU, and process limits plus privilege dropping. Only the Python fuzzing path (fusil-python-threaded, fusil.python, fusil.python.jit) is actively developed and tested, while historical fuzzers for Firefox, PHP, and mplayer sit in notworking/ directories. It serves CPython contributors looking for JIT and OOM-edge crashes, not application developers.
