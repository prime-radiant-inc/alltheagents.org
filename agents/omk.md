---
name: "OMK"
slug: "omk"
layout: "agent.njk"
category: "agent"
maker: "dmae97"
license: "MIT"
url: "https://github.com/dmae97/open-multi-agent-kit"
source_code_url: "https://github.com/dmae97/open-multi-agent-kit"
source_available: "True"
platforms:
  - "CLI"
  - "IDE"
first_released: "2026-04-30"
current_release: "2026-08-16"
stars: "134"
language: "TypeScript"
homepage: null
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: "False"
subagents: "True"
hooks: "True"
plan_mode: "True"
model_providers: "Codex, Claude Code, OpenCode, Kimi, GLM/ZAI, xAI/Grok, NVIDIA NIM, local providers"
pricing: "Free (MIT)"
install_method: "npm install -g open-multi-agent-kit --ignore-scripts; or npx --ignore-scripts open-multi-agent-kit; requires Node.js 22.19+"
docs_url: "https://github.com/dmae97/omk/blob/main/packages/coding-agent/docs/index.md"
plugin_docs_url: null
config_docs_url: null
download_url: "https://www.npmjs.com/package/open-multi-agent-kit"
maintained: "active"
sources:
  - "brad"
what_makes_it_special: "Provider-neutral multi-agent control plane with a 4-step loop (Scope, Route, Verify, Replay); turns goals into bounded DAGs with owned paths; evidence-gated completion prevents parallel agents from overwriting each other; keeps routing separate from execution contract"
---

OMK is a provider-neutral coding-agent harness organized around four phases: scope goals into bounded DAGs, route work through a provider-neutral model registry, verify completion with evidence-gated build/test/audit gates, and replay with durable receipts. Sandbox isolation is on by default, with network-blocked OS sandboxing for shell commands. The project is unusually explicit about its limits, documenting a prior release's fabricated evidence and refusing to treat prompt agreement as a correctness verdict. It builds on Mario Zechner's pi harness via the oh-my-pi fork, with optional orchestration extensions on top of the default single-agent loop. Release notes are detailed and development is active, though the contributor base is a single author.
