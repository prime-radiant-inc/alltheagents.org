---
name: "Comet"
slug: "comet"
layout: "agent.njk"
category: "other"
maker: "Comet"
license: "Apache-2.0"
url: "https://comet.com"
source_code_url: null
source_available: "True"
platforms:
  - "IDE"
  - "Web"
first_released: "2025"
current_release: "2026"
stars: null
language: "Python, TypeScript, Java"
homepage: null
mcp_support: "True"
plugin_support: null
claude_code_plugin: null
subagents: null
hooks: null
plan_mode: null
model_providers: "Model-agnostic platform (integrations for OpenAI, Anthropic, LangChain, LlamaIndex, and 60+ others)"
pricing: "Free tier (no credit card required); paid plans available"
install_method: "pip install opik (open-source self-host); or SaaS at comet.com"
docs_url: "https://www.comet.com/docs/opik/"
plugin_docs_url: null
config_docs_url: "https://www.comet.com/docs/opik/integrations/mcp-server"
download_url: "https://github.com/comet-ml/opik"
maintained: "active"
sources:
  - "web_search_multilingual"
what_makes_it_special: "LLM observability and MLOps platform (Opik), not a coding agent harness. Features an 'Ollie' agent that recommends code fixes from trace data, tracks spend for coding agents like Claude Code, and offers an MCP server giving coding agents access to trace data and diagnostics. Open source under Apache-2.0."
---

Once coding agents run inside engineering organizations, their behavior and their spending need the same observability as production services. Opik, Comet's open-source LLM operations platform, ingests every agent step through more than sixty integrations, detects silent failures across traces, groups recurring issues, and surfaces root causes; its Ollie agent inspects those traces - tool calls, context retrieval, prompts - and proposes concrete code or prompt fixes. Test suites with golden datasets and LLM-as-judge metrics validate changes before deployment, and an AI Spend Tracker gives engineering leads visibility into Claude Code and Codex spending. The core is open source (comet-ml/opik, 21k+ stars) with a managed cloud and enterprise deployment options. ML and platform teams at companies like Uber, Netflix, and Etsy use it to monitor LLM applications, including coding-agent fleets.
