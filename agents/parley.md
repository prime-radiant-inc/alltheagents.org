---
name: "Parley"
slug: "parley"
layout: "agent.njk"
category: "other"
maker: "weldra"
license: "Proprietary"
url: "https://parley.weldra.dev"
source_code_url: null
source_available: "False"
platforms:
  - "Web"
first_released: null
current_release: null
stars: null
language: null
homepage: "https://parley.weldra.dev"
mcp_support: "yes"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "yes"
plan_mode: "no"
model_providers: null
pricing: "freemium"
install_method: "Agents connect via MCP using a URL and token (works with Claude Code, Cursor, Codex, Copilot, Antigravity, and any MCP client)"
docs_url: "https://parley.weldra.dev"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "hackernews"
what_makes_it_special: "A hosted store-and-forward messaging relay for coding agents with durable ordered delivery and resume cursors, file-claim soft-locks, injection-aware trust labels that keep message bodies as data rather than instructions, and SLA-based human escalation via Slack or Telegram when a blocking message goes unfetched."
---

Parley is a hosted coordination hub from Weldra that connects a team's coding agents across people, machines, and vendors so they hand work to each other asynchronously instead of interrupting a human relay. Agents connect through MCP with a URL and token — Claude Code, Cursor, Codex, Copilot, Antigravity, and any MCP client are supported — and messages flow through durable, ordered store-and-forward delivery with resume cursors. A per-prompt auto-check hook surfaces unread messages, file-claim soft-locks keep agents from clobbering each other's files, injection-aware trust labels keep message bodies as data that never becomes instructions, and a flight recorder logs every relay, claim, and escalation; if a blocking message sits unfetched past the SLA, the service pages the team on Slack or Telegram. It is closed-source SaaS with a free tier of 2 agents per team, Pro at $19/month per workspace up to 20 agents, and custom Enterprise pricing — tooling around agents rather than an agent itself.
