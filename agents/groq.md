---
name: "Groq"
slug: "groq"
layout: "agent.njk"
category: "other"
maker: null
license: "Proprietary"
url: "https://groq.com/"
source_code_url: null
source_available: "False"
platforms:
  - "Web"
first_released: null
current_release: null
stars: null
language: null
homepage: "https://groq.com"
mcp_support: null
plugin_support: null
claude_code_plugin: null
subagents: null
hooks: null
plan_mode: null
model_providers: "Groq"
pricing: "usage"
install_method: "n/a — hosted API (console.groq.com)"
docs_url: "https://console.groq.com/docs/tool-use"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "jim"
what_makes_it_special: "GroqCloud API endpoints support tool use for programmatic execution of specified operations through requests with explicitly defined operations"
---

Groq operates an inference cloud built on its custom LPU processor, now paired with NVIDIA GPUs, selling low-latency model serving rather than any agent product of its own. Its API exposes tool-use endpoints so that external coding agents can execute function calls against models hosted on Groq's hardware, which is why the entry appears here: coding agents like Groq Code CLI consume its endpoints rather than Groq itself looping over tools. The company positions its capacity as infrastructure for agent workloads, with the developer console providing keys, usage dashboards, and documentation for tool-use requests. In a census of harnesses, Groq is the upstream gateway layer — closer to model provisioning than to software-building agents.
