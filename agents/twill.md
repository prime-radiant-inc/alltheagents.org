---
name: "Twill"
slug: "twill"
layout: "agent.njk"
category: "multiplexer"
maker: "Twill"
license: "Proprietary"
url: "https://twill.ai"
source_code_url: null
source_available: "No"
platforms:
  - "Web"
  - "Autonomous"
first_released: null
current_release: null
stars: null
language: null
homepage: "https://twill.ai"
mcp_support: "yes"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "Anthropic (Claude), OpenAI (GPT) for hard tasks; Qwen, Kimi, GLM open-source models for routine work — user's own keys at provider rates"
pricing: "usage"
install_method: "Web app, desktop app, or scriptable CLI"
docs_url: "https://twill.ai"
plugin_docs_url: null
config_docs_url: null
download_url: "https://twill.ai"
maintained: "active"
sources:
  - "hackernews"
what_makes_it_special: "A YC-backed 'software factory' that turns triggers (GitHub PR/issue, Slack, Linear, CLI) into pull requests: each task forks a fully provisioned copy of the company environment — repo, deps, running app, seeded database — where a coding agent (Claude Code, Codex CLI, or OpenCode) executes with proof attached (test results like '142 pass'), supports multi-repo reasoning across frontend/backend/infra, and runs recurring automations against GitHub, GCP, AWS, Sentry, Linear, Slack, Notion, and Datadog."
---

Twill exists because handing real tickets to coding agents requires more than the agent: the environment must be cloned, dependencies installed, the app running, and the database seeded before useful work starts. Each incoming task from GitHub, Slack, Linear, or the CLI forks an isolated, pre-warmed copy of the whole company environment — supporting multi-repo setups so an agent can reason across frontend, backend, workers, and infrastructure in one task — and the selected coding agent works inside it, installing packages, running Docker, seeding data, and running tests. Results come back as pull requests with evidence attached, so review centers on test output rather than diffs alone. Recurring automations (incident triage, cloud resource checks, doc updates, follow-ups) run on schedule against the same machinery. Engineering teams use it via web, desktop, or CLI, paying with their own provider keys; YC-backed, with a free Pro tier for open-source maintainers.
