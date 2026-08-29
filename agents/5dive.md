---
name: "5dive"
slug: "5dive"
layout: "agent.njk"
category: "multiplexer"
maker: "5dive-ai"
license: "MIT"
url: "https://github.com/5dive-ai/5dive"
source_code_url: "https://github.com/5dive-ai/5dive"
source_available: "True"
platforms:
  - "IDE"
first_released: "2026-05-15"
current_release: "2026-08-20"
stars: "52"
language: "Bash"
homepage: "https://5dive.ai"
mcp_support: "no"
plugin_support: "True"
claude_code_plugin: "False"
subagents: "True"
hooks: "True"
plan_mode: "no"
model_providers: "Anthropic Claude, OpenAI Codex, Google Antigravity, xAI Grok, Cognition Devin, OpenRouter, DeepSeek, Moonshot/Kimi, Qwen, Z.ai/GLM"
pricing: "Free / open-source (MIT); managed VM available at 5dive.ai (pricing not specified)"
install_method: "curl -fsSL https://install.5dive.ai | sudo bash; then sudo 5dive init (Linux with systemd required)"
docs_url: "https://5dive.ai/docs/5dive-cli"
plugin_docs_url: null
config_docs_url: null
download_url: "https://install.5dive.ai"
maintained: "active"
sources:
  - "brad"
what_makes_it_special: "Runs a 'company of AI agents' on a Linux server you own - each agent is its own Linux user running an official agentic AI CLI as a systemd service, coordinating through a shared bash CLI and SQLite task queue; pings your phone via Telegram only when a human decision is needed."
---

5dive exists for people who want a fleet of coding agents working unattended on hardware they control, without adopting a proprietary platform. Installation is a curl script plus 5dive init on any systemd Linux box; each named agent becomes its own Linux user running an official agent CLI (claude, codex, antigravity, grok, devin, hermes, opencode, pi, and others) as a systemd service, coordinating through a shared bash CLI and SQLite task queue. Agents sit on an org chart, hand off tasks through a shared backlog, and hit human approval gates when work needs a decision — the only moment a Telegram ping reaches the owner. Self-hosting engineers and small teams running long-lived autonomous agents are the users, with a managed option at 5dive.ai.
