---
name: "OpenCodeReview"
slug: "opencodereview"
layout: "agent.njk"
category: "agent"
maker: "alibaba"
license: "Apache-2.0"
url: "https://github.com/alibaba/open-code-review"
source_code_url: "https://github.com/alibaba/open-code-review"
source_available: "Yes"
platforms:
  - "CLI"
first_released: "2026-05-18"
current_release: "2026-08-19"
stars: "20868"
language: "Go"
homepage: "https://open-codereview.ai"
mcp_support: "yes (transport not documented; MCP server at open-codereview.ai/docs/mcp)"
plugin_support: "yes (plugins for Claude Code, Codex, Cursor, OpenCode, VSCode extension)"
claude_code_plugin: "yes (review slash commands plugin)"
subagents: "yes (smart file bundling, each bundle runs as a sub-agent with isolated context)"
hooks: null
plan_mode: null
model_providers: "OpenAI, Anthropic, BYOK (custom endpoints)"
pricing: "open-source (Apache-2.0), BYOK"
install_method: "npm"
docs_url: "https://open-codereview.ai/docs"
plugin_docs_url: "https://github.com/alibaba/open-code-review/blob/main/plugins/open-code-review/README.md"
config_docs_url: "https://open-codereview.ai/docs/configuration"
download_url: "https://www.npmjs.com/package/@alibaba-group/open-code-review"
maintained: "active"
sources:
  - "brad"
what_makes_it_special: "Hybrid architecture code review tool combining deterministic engineering pipelines with an LLM agent, achieving higher precision than general-purpose agents while using ~1/9 of the tokens. Battle-tested at Alibaba scale, serving tens of thousands of developers."
---

Hybrid architecture code review tool combining deterministic engineering pipelines with an LLM agent, achieving higher precision than general-purpose agents while using ~1/9 of the tokens. Battle-tested at Alibaba scale, serving tens of thousands of developers.
