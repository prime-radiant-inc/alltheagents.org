---
name: "DuetGPT"
slug: "duetgpt"
layout: "agent.njk"
category: "agent"
maker: "kristoferlund"
license: "MIT"
url: "https://github.com/kristoferlund/duet-gpt"
source_code_url: "https://github.com/kristoferlund/duet-gpt"
source_available: "True"
platforms:
  - "Autonomous"
first_released: "2023-05-25"
current_release: "2023-06-19"
stars: "168"
language: "TypeScript"
homepage: null
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "OpenAI"
pricing: "Free/open-source (bring your own OpenAI API key)"
install_method: "npm install -g duet-gpt"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/kristoferlund/duet-gpt"
maintained: "dormant"
sources:
  - "jim"
what_makes_it_special: "Semi-autonomous conversational CLI coding assistant using OpenAI function calling (no LangChain); AI proposes commands, developer approves, then auto-execution; can also serve as a general bash helper."
---

DuetGPT is a deliberately minimal take on the AI pair programmer: a conversation where the model's proposed shell commands and file edits are shown for approval and then executed verbatim, with no LangChain layer and no guardrails beyond the developer's own judgment. It ships as one npm package, asks for an OpenAI key on first run, and works equally well as a general bash helper — writing scripts, grepping trees, drafting PR descriptions from commit logs. The warning in its own README about the absence of guardrails is the design statement: approval is the only safety mechanism. It found its audience among developers experimenting with GPT-4 function calling in 2023; the repo has not been updated since June 2023.
