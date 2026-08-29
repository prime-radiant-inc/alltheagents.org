---
name: "postal"
slug: "postal"
layout: "agent.njk"
category: "agent"
maker: "andrefetch"
license: "GPL-3.0"
url: "https://github.com/andrefetch/postal"
source_code_url: "https://github.com/andrefetch/postal"
source_available: "True"
platforms:
  - "CLI"
first_released: "2026-06-26"
current_release: "2026-08-17"
stars: "104"
language: "Python"
homepage: "https://postalcli.vercel.app"
mcp_support: "True"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "True"
hooks: "True"
plan_mode: "True"
model_providers: "OpenRouter (Claude, OpenAI, Deepseek, Kimi, free smaller models)"
pricing: "Free / open-source (pay your own OpenRouter API costs)"
install_method: "pip install postalcli"
docs_url: "https://github.com/andrefetch/postal/tree/main/docs"
plugin_docs_url: null
config_docs_url: "https://github.com/andrefetch/postal/tree/main/docs"
download_url: "https://github.com/andrefetch/postal"
maintained: "active"
sources:
  - "github_topic3"
what_makes_it_special: "Bring-any-model via OpenRouter; six graduated approval policies with dangerous-command rejection; context pruning + history compaction for long sessions; per-turn session checkpointing with /rewind; readable object-oriented Python codebase; modular component-based Rich TUI"
---

Postal targets developers who want a terminal coding agent with fine-grained control over autonomy rather than an all-or-nothing auto mode. Its loop runs plan, read, edit, and bash tools with every mutating action passing one of six approval policies, switched mid-session with /approval, while dangerous commands are rejected outright regardless of policy. Sessions are checkpointed after every turn, so /rewind can roll conversation state back to any point, and long sessions survive through context pruning plus automatic compaction into a continuation brief when the window fills. Five subagents handle investigation, review, architecture, test writing, and debugging, each subject to the same approval gates. It runs on OpenRouter alone, so users pay their own API costs, and it picks up AGENTS.md per project automatically.
