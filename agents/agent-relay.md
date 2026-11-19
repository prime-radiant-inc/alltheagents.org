---
name: "agent-relay"
slug: "agent-relay"
layout: "agent.njk"
category: "multiplexer"
maker: "saranyan"
license: "MIT"
url: "https://github.com/saranyan/agent-relay"
source_code_url: "https://github.com/saranyan/agent-relay"
source_available: "True"
homepage: null
docs_url: "https://github.com/saranyan/agent-relay/blob/main/README.md"
download_url: null
install_method: "git clone https://github.com/saranyan/agent-relay.git && cd agent-relay, then bin/relay init --participants codex claude and bin/relay console (requires macOS, Python 3.11+)"
platforms:
  - "CLI"
  - "Web"
autonomy_level: []
specialization: "general"
language: "Python"
first_released: "2026-10-25"
current_release: "2026-10-25"
maintained: "dormant"
mcp_support: "False"
plugin_support: "False"
claude_code_plugin: null
subagents: "False"
hooks: "False"
plan_mode: "False"
plugin_docs_url: null
config_docs_url: null
model_providers: "agents bring their own providers; the relay supplies none (tested with Claude Code and Codex)"
pricing: "free"
stars: "11"
sources:
  - "hackernews"
last_verified: "2026-11-19"
date_added: "2026-11-19"
what_makes_it_special: "Carries each turn between coding sessions from different vendors — one leads, one follows — recording every message and decision as a durable, hash-chained record that stops the loop whenever a human decision is needed."
---

agent-relay exists because sessions from different vendors cannot hand work to each other: Codex can hand off to Codex, Claude to Claude, but when you use Codex for planning and review and Claude Code for implementation, you are the one copying plans, results and reviews between terminals. The relay carries the turns for you: one session leads, the other follows, and a foreground controller passes each turn across through explicit adapters, records it on a durable on-disk bus, and stops whenever something needs your decision — a web console (down to phone width, loopback-only) shows what the managed session is doing and pauses the loop with an answer box when a question comes in. The routes it starts are locked down where it can: a Claude Code follower runs with no tools at all, or only Read, Edit, Write, Glob and Grep inside a macOS sandbox, and cannot start subagents or run commands. The README is explicit about the view from outside: what a session does inside a turn — tool loops, subagents, long commands — is invisible to the relay, which counts hand-offs rather than work. Use cases include plan-build-review loops where Codex writes and reviews and Claude implements, bounded jobs you can walk away from, and a replayable audit trail of agent work. The project is a documented prototype (live hand-offs verified once, 2026-10-25, with Codex leading Claude Code) with an adapter contract designed so other coding agents could plug in.
