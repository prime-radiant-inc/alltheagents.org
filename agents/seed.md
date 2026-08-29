---
name: "Seed"
slug: "seed"
layout: "agent.njk"
category: "agent"
maker: "vivekhaldar"
license: "Sovereign Source License v0.3"
url: "https://github.com/vivekhaldar/seed"
source_code_url: "https://github.com/vivekhaldar/seed"
source_available: "True"
platforms:
  - "CLI"
first_released: "2026-08-20"
current_release: null
stars: 102
language: "Python"
homepage: null
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "OpenAI (Codex), Anthropic, Google Gemini, OpenRouter (via the llm library)"
pricing: "free"
install_method: "uvx --from git+https://github.com/vivekhaldar/seed.git seed"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "hackernews"
what_makes_it_special: "A single Python file whose agent has exactly one tool — exec — and must grow every other capability by editing its own self/ directory of markdown and scripts between sessions. Each planted directory becomes a different, diverging agent, and the git repo history is part of the agent's identity."
---

Seed is Vivek Haldar's deliberately minimal agent experiment: one Python file that calls a language model with a single tool, exec, and nothing else, drawing on McCarthy's metacircular evaluator and homoiconicity as its design inspiration. Everything a framework normally provides — tools, memory, skills, conventions — must be grown by the agent itself into a self/ directory it can edit; sessions are otherwise ephemeral, so anything not written to self/ is lost, and verbatim transcripts accumulate in self/sessions/ as a flight recorder the agent may learn to study. Planting via uvx copies seed.py into a fresh directory, germinates self/SELF.md, and initializes a git repo; each directory grows a different agent, making it less a product than a probe into how much structure an agent can bootstrap on its own. Models route through Simon Willison's llm library, defaulting to openai-codex/gpt-5.6-sol with the ChatGPT login from the Codex CLI.
