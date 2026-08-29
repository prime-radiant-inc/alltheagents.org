---
name: "Octofriend"
slug: "octofriend"
layout: "agent.njk"
category: "agent"
maker: "synthetic-lab"
license: "MIT"
url: "https://github.com/synthetic-lab/octofriend"
source_code_url: "https://github.com/synthetic-lab/octofriend"
source_available: "Yes"
platforms:
  - "CLI"
first_released: "2025-03-25"
current_release: "2026-08-20"
stars: "998"
language: "TypeScript"
homepage: null
mcp_support: "yes"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: null
pricing: "BYOK"
install_method: "npm install --global octofriend"
docs_url: "https://github.com/synthetic-lab/octofriend#readme"
plugin_docs_url: null
config_docs_url: null
download_url: "https://www.npmjs.com/package/octofriend"
maintained: "active"
sources:
  - "hackernews"
what_makes_it_special: "Ships open-sourced, custom-trained autofix models (diff-apply and fix-json on Hugging Face) that repair mangled JSON tool calls and bad diffs from any coding model — plus zero telemetry and mid-conversation model switching."
---

Octofriend is a terminal coding assistant built around tolerating weak or eccentric models rather than assuming a frontier provider. Two fine-tuned open-source models automatically repair the broken tool calls and malformed diffs that smaller models produce, so users can run cheaper or local models without the loop collapsing. It works with any OpenAI- or Anthropic-compatible API plus local runtimes, and models can be swapped mid-conversation when one gets stuck. Rules files, session resume, image attachments, Docker sandboxing, MCP servers, and automatic LSP integration round out the feature set. The project is MIT-licensed with a zero-telemetry privacy stance and recommends its own zero-data-retention Synthetic provider.
