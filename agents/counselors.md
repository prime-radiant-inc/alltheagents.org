---
name: "counselors"
slug: "counselors"
layout: "agent.njk"
category: "multiplexer"
maker: "aarondfrancis"
license: "MIT"
url: "https://github.com/aarondfrancis/counselors"
source_code_url: "https://github.com/aarondfrancis/counselors"
source_available: "True"
homepage: null
docs_url: "https://github.com/aarondfrancis/counselors#readme"
download_url: "https://github.com/aarondfrancis/counselors/releases"
install_method: "npm install -g counselors (Node 20+); brew install aarondfrancis/homebrew-tap/counselors; or curl -fsSL https://github.com/aarondfrancis/counselors/raw/main/install.sh | bash"
platforms:
  - "CLI"
autonomy_level: []
specialization: "general"
language: "TypeScript"
first_released: "2026-02-09"
current_release: "2026-02-27"
maintained: "dormant"
mcp_support: "False"
plugin_support: "False"
claude_code_plugin: null
subagents: "True"
hooks: "False"
plan_mode: "False"
plugin_docs_url: null
config_docs_url: null
model_providers: "Claude Code, OpenAI Codex, Gemini CLI, Amp, or custom CLIs — no direct API calls, each installed CLI brings its own provider"
pricing: "free"
stars: "671"
sources:
  - "github-issue"
last_verified: "2026-11-18"
date_added: "2026-11-18"
what_makes_it_special: "No MCP servers, no direct API integrations, no complex configuration. It just calls your locally installed CLI tools."
---

counselors exists to answer a different question from most parallel-agent tools: not how to split work across agents, but what several models think about the same question. It sends one prompt to every configured coding agent at once and collects their independent responses — a council of advisors for reviewing a plan, double-checking a refactor, or comparing approaches before committing to one. The TypeScript CLI wraps the first-party tools already installed on the machine, dispatches prompts in parallel with read-only sandboxing on by default, and writes each agent's response, a run manifest, and a synthesized summary into a structured output directory; a multi-round loop mode feeds earlier rounds' outputs back to every agent so later rounds refine instead of repeat, and a /counselors skill template lets a primary agent such as Claude Code gather context, dispatch, and synthesize without the developer leaving the editor. It is built for developers who already run several agent subscriptions and would rather see where the models disagree than trust one answer.
