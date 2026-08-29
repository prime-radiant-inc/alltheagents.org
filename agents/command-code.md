---
name: "Command Code"
slug: "command-code"
layout: "agent.njk"
category: "agent"
maker: "CommandCodeAI"
license: "Source Available"
url: "https://github.com/CommandCodeAI/command-code"
source_code_url: "https://github.com/CommandCodeAI/command-code"
source_available: "True"
platforms:
  - "CLI"
first_released: "2017-12-20"
current_release: "2026-08-15"
stars: null
language: null
homepage: "https://commandcode.ai"
mcp_support: null
plugin_support: null
claude_code_plugin: null
subagents: null
hooks: null
plan_mode: null
model_providers: "Anthropic, OpenAI, DeepSeek, GLM, Kimi"
pricing: "freemium"
install_method: "npm i -g command-code"
docs_url: "https://commandcode.ai/docs"
plugin_docs_url: null
config_docs_url: null
download_url: "https://www.npmjs.com/package/command-code"
maintained: "active"
sources:
  - "jqueryscript"
  - "brad"
what_makes_it_special: "Meta neuro-symbolic AI model called taste-1 that continuously learns your coding preferences and style from interactions; learned taste profile is portable and can be shared with your team using npx taste push/pull."
---

Coding agents apply generic conventions, so teams keep re-explaining their own style in rules files that drift out of date. Command Code treats those preferences as a learning problem: its taste-1 model observes accepted, rejected, and edited outputs, maintains a per-developer taste profile, and uses it to shape future generations. The profile is portable - developers push it to a registry and teammates pull it, so a new engineer inherits the team's taste without reading a rules document. Day to day it runs as a terminal agent with slash commands, bash mode, and file-path completion, capable of shipping full-stack projects, fixing bugs, writing tests, and refactoring. Solo developers use a free tier; paid plans bundle access to Anthropic, OpenAI, Google, DeepSeek, Kimi, and GLM models.
