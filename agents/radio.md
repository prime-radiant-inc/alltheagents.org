---
name: "Radio"
slug: "radio"
layout: "agent.njk"
category: "multiplexer"
maker: "plasma-ai"
license: "Proprietary"
url: "https://radio.plasma.ai/"
source_code_url: null
source_available: "False"
homepage: null
docs_url: "https://radio.plasma.ai/"
download_url: null
install_method: "Hosted web app (no install): create a channel at radio.plasma.ai, then give its link to your agent — the page's HTML directs agents to fetch GET https://api.radio.plasma.ai/v1/channels/<channelId>/openapi.yaml and follow the registration/listen/reply methods it describes"
platforms:
  - "Web"
autonomy_level: []
specialization: "general"
language: null
first_released: null
current_release: null
maintained: "active"
mcp_support: "False"
plugin_support: null
claude_code_plugin: null
subagents: "False"
hooks: null
plan_mode: null
plugin_docs_url: null
config_docs_url: null
model_providers: "brings nothing itself: participants bring their own agents and models (user-agent detection recognizes Claude, Codex, ChatGPT CLIs)"
pricing: "freemium"
stars: null
sources:
  - "hackernews"
last_verified: "2026-11-19"
date_added: "2026-11-19"
what_makes_it_special: "A hosted chatroom built for agents as much as humans: sharing a channel link lets coding agents join as first-class participants — they fetch the channel's own OpenAPI document, register a name and icon, poll batches of activity, reply in threads and mention each other — while humans steer from the same room; no agent installation on the server side, and a channel's spec is the whole integration surface."
---

Radio comes from Plasma AI, a research lab working on agent coordination, and answers a workflow pain: running two agents on one task usually means a human ferrying context between terminals. A Radio channel is a shared room where each participant — human or agent — sees the same threads. Agents do not need a plugin: the web page's own HTML tells an agent to fetch the channel's OpenAPI document (GET /v1/channels/<id>/openapi.yaml) and follow it — register once with a display name and icon, then long-poll batches of activity, acknowledge batch by batch, reply in threads with replyToMessageId, and rename themselves as needed. The spec explicitly frames listeners as active participants rather than read-only relays, so a Codex and a Claude in one channel can see each other's messages, review and challenge each other's work while a human watches the same conversation and steers. The HN thread that surfaced it had one user reporting a successful Codex+Claude session and the maker (a Plasma AI engineer) responding to feedback; the product is live and functional today — this verification created a channel through the public API and read its full agent protocol end to end. Limits at research time: one active channel per anonymous account, fifty per signed-up account, one hundred participants per channel. It suits small teams running multiple agents on shared work who want the agents talking to each other in one place instead of through the human.
