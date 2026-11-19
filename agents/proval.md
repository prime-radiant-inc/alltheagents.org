---
name: "Proval"
slug: "proval"
layout: "agent.njk"
category: "agent"
maker: "seoes"
license: "AGPL-3.0"
url: "https://github.com/seoes/proval"
source_code_url: "https://github.com/seoes/proval"
source_available: "True"
homepage: "https://proval.app"
docs_url: "https://proval.app/docs"
download_url: null
install_method: "Docker Compose with ghcr.io/seoes/proval:latest (ports 7900 dashboard / 7901 webhook, ENCRYPTION_KEY from openssl rand -base64 32, SQLite on /data); plain docker run and a Kubernetes example are documented"
platforms:
  - "Web"
  - "Autonomous"
autonomy_level:
  - "autonomous-background"
specialization: "code-review"
language: "TypeScript"
first_released: "2026-07-05"
current_release: "2026-11-17"
maintained: "active"
mcp_support: "False"
plugin_support: "False"
claude_code_plugin: null
subagents: "True"
hooks: null
plan_mode: null
plugin_docs_url: null
config_docs_url: null
model_providers: "Any OpenAI-compatible Chat Completions endpoint (OpenAI, Ollama, llama.cpp, vLLM, internal gateways) and Anthropic Messages endpoints, BYOK; OpenAI-compatible is the primary path, Anthropic and Gemini planned as first-class"
pricing: "free"
stars: "135"
sources:
  - "hackernews"
last_verified: "2026-11-19"
date_added: "2026-11-19"
what_makes_it_special: "A self-hosted code-review agent you point at your own Git host and your own models — GitLab, Forgejo and GitHub with inline single- and multi-line comments — that fans each pull request out to specialist sub-agents exploring the codebase in parallel, then consolidates findings by severity, reviews issues and replies in threads, and logs token usage per action."
---

Proval came out of a personal gap its author names directly: as a homelab user running his own GitLab, he could not find a self-hosted code-review agent that worked with it and with his own LLMs, so he built one. It is a Docker-first service: one Compose file brings up a dashboard on port 7900 and a webhook receiver on 7901, SQLite on a volume, and a random encryption key — under ten lines and three minutes, on your own network, with nothing leaving it. GitLab, Forgejo and GitHub are the supported hosts (Gitea and Codeberg via Forgejo-compatible APIs), and the model is yours: any OpenAI-compatible Chat Completions endpoint — OpenAI, Ollama, llama.cpp, vLLM or an internal gateway — or an Anthropic Messages endpoint, with local models as a first-class case rather than an afterthought. When a pull request gets a meaningful push, Proval reads the diff, groups the changed files into review units, and runs specialist sub-agents in parallel, each exploring the codebase on its own so cross-file issues and hidden dependencies surface; a writing agent consolidates findings grouped by severity and posts them as inline comments on the affected lines, single- or multi-line, in the host's native format. It answers issues when they open, replies when someone comments back (every message or @mention only, your choice), reads thread context before responding, and logs every review, reply and comment with token usage so model costs are visible. The author is upfront that it is early, with rough edges and a public list of planned features (auth, SSO, rate limits, custom prompts). It suits teams and homelabbers who want PR review on infrastructure they control, with models they already own.
