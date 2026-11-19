---
name: "dsh-superagent"
slug: "dsh-superagent"
layout: "agent.njk"
category: "multiplexer"
maker: "deepseek-ai"
license: "MIT"
url: "https://github.com/deepseek-ai/dsh-superagent-prototype"
source_code_url: "https://github.com/deepseek-ai/dsh-superagent-prototype"
source_available: "True"
homepage: null
docs_url: "https://github.com/deepseek-ai/dsh-superagent-prototype/blob/main/docs/000-philosophy.md"
download_url: null
install_method: "Run inside DeepSeek Harness as a bundle/plugin: clone the repo, then have your coding agent read SETUP.md and follow it (installs the dsh-superagent profile into DSH; needs Node.js 22.19+/24+, pnpm, git, tmux, Python 3.8+, GitHub CLI)"
platforms:
  - "Autonomous"
autonomy_level:
  - "agentic"
  - "autonomous-background"
specialization: "general"
language: "TypeScript"
first_released: "2026-10-31"
current_release: "2026-11-03"
maintained: "active"
mcp_support: null
plugin_support: "True"
claude_code_plugin: null
subagents: "True"
hooks: "True"
plan_mode: null
plugin_docs_url: null
config_docs_url: "https://github.com/deepseek-ai/dsh-superagent-prototype/blob/main/docs/006-deployment.md"
model_providers: "DeepSeek Harness — the host runs the agent sessions and brings the model provider; workers use the dsh-superagent-worker preset, subagents DSH's standard preset"
pricing: "free"
stars: "23835"
sources:
  - "hackernews"
last_verified: "2026-11-19"
date_added: "2026-11-19"
what_makes_it_special: "A proactive one-repo agent that listens to GitHub (and optionally Feishu), opens a work item for each allowed request, runs it in its own DeepSeek Harness session and directory, and answers in the original conversation with a pull request — with an authorization gate so it acts only when asked or when a team-written rule allows."
---

dsh-superagent grew out of DeepSeek's own day-to-day development, with much of the engineering done by coding agents, and is published as a research prototype for one GitHub repository rather than a product: it is a bundle that runs inside DeepSeek Harness (DSH). It listens to GitHub and optionally Feishu; when someone the policy allows asks for work, an assessor session decides whether to accept, the engine opens a Ticket with a mandate, and an executor session — its own DSH session and directory, typically a git worktree — does the work and answers in the original conversation, often with a pull request. A web panel shows what needs a person, and the philosophy doc drives the design: take as little human attention as possible, so the agent acts only when asked or when a team-written rule allows, and speaks only when someone must act. The README is explicit that it is research code adapted for publication, not identical to the internal version, and asks operators to review and adapt it; the intended user is a team that wants to hand one repository's intake and delivery to an agent and watch the tickets flow. The coding itself belongs to DSH: worker subagents use the host's standard preset, and dsh-superagent owns intake, authorization, ticket lifecycle, and delivery.
