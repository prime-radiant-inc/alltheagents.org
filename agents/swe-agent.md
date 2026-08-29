---
name: "SWE-agent"
slug: "swe-agent"
layout: "agent.njk"
category: "agent"
maker: "SWE-agent"
license: "MIT"
url: "https://github.com/SWE-agent/SWE-agent"
source_code_url: "https://github.com/SWE-agent/SWE-agent"
source_available: "True"
platforms:
  - "CLI"
  - "Autonomous"
first_released: "2024-04-02"
current_release: "2026-08-17"
stars: null
language: "Python"
homepage: "https://swe-agent.com"
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "n/a"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "GPT-4o, Claude Sonnet 4, open-weights models (SWE-agent-LM-32b), your LM of choice"
pricing: "Free / open source (MIT)"
install_method: "From source via pip (pyproject.toml), or GitHub Codespaces"
docs_url: "https://swe-agent.com"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/SWE-agent/SWE-agent"
maintained: "dormant"
sources:
  - "jqueryscript"
  - "flatlogic"
  - "brad"
  - "ishandutta"
  - "tiennm"
what_makes_it_special: "Takes a GitHub issue and tries to automatically fix it using your LM of choice. State-of-the-art on SWE-bench among open-source projects (NeurIPS 2024). Configurable via a single YAML file. Development effort has shifted to mini-swe-agent which has superseded SWE-agent."
---

SWE-agent was built to answer a research question: does the interface an LM uses to operate on a repository matter as much as the model behind it? Its answer was a custom Agent-Computer Interface — compact file viewers, search tools with bounded output, and guarded edit commands — which drove state-of-the-art SWE-bench results at publication and a NeurIPS 2024 paper. In operation the agent receives a GitHub issue, explores a sandboxed copy of the repository with its custom shell tools, edits files, and runs tests before emitting a patch; all behavior is configured through a single YAML file. Beyond issue fixing, the same scaffold powers cybersecurity research through its EnIGMA configuration. Development attention has moved to mini-swe-agent, which the README explicitly recommends as the successor, leaving SWE-agent in maintenance mode.
