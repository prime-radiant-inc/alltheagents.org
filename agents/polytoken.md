---
name: "polytoken"
slug: "polytoken"
layout: "agent.njk"
category: "agent"
maker: "ed3d"
license: "Proprietary"
url: "https://polytoken.dev/"
source_code_url: null
source_available: "False"
homepage: null
docs_url: "https://docs.polytoken.dev/"
download_url: "https://docs.polytoken.dev/installation/downloads/"
install_method: "curl -fsS https://get.polytoken.dev | bash"
platforms:
  - "CLI"
autonomy_level:
  - "agentic"
specialization: "general"
language: null
first_released: "2026-06-18"
current_release: "2026-09-16"
maintained: "active"
mcp_support: "True"
plugin_support: null
claude_code_plugin: null
subagents: "True"
hooks: "True"
plan_mode: "True"
plugin_docs_url: null
config_docs_url: "https://docs.polytoken.dev/reference/configuration/"
model_providers: "Anthropic, OpenAI, OpenAI Codex, Azure OpenAI, plus any Anthropic- or OpenAI-compatible endpoint; the built-in catalog also covers z.ai, DeepSeek, Mistral, Moonshot/Kimi, Ollama Cloud, OpenRouter, DeepInfra, Fireworks AI, QwenCloud, OpenCode Go, Umans, Neuralwatt, and Kagi"
pricing: "free"
stars: null
sources:
  - "github-issue"
last_verified: "2026-09-18"
date_added: "2026-09-18"
what_makes_it_special: "A proprietary local-first coding agent that runs as a background daemon, so the terminal UI and any protocol client are only front ends onto the same session. Prompts, facets, skills, hooks, and themes all ship as plain files you can read, copy, and replace."
---

Polytoken exists because its author wanted a coding harness that no vendor can take away, and the homepage argues that case in the first person rather than with a feature list. The shape of the product follows: a long-running daemon owns conversations, permissions, and tool execution on your machine, while the terminal UI attaches to it as a client, which is why a session survives a front end that dies and can be reattached later. Almost everything the model sees is editable text. Facets are Markdown personas that swap the system prompt and the tool set; the shipped plan facet investigates with read-only shell access, writes a handoff plan, runs a plan-reviewer, and asks before work moves into the execute facet; skills use the Agent Skills SKILL.md format and load from project or global directories; hooks fire on lifecycle events such as post_clear. A zero-config first run walks you through creating a provider and configuring web search, and the provider list is broad by design — the author's own setup orchestrates GLM-5.2 through z.ai over a pile of GPT 5.6 and DeepSeek V4 Flash models, and custom Anthropic- or OpenAI-compatible endpoints are first-class. It installs as a checksum-verified binary for Linux and macOS on amd64 and arm64 and is free under a proprietary end-user license, which makes it a fit for developers who want to own the loop without giving up a polished terminal UI.
