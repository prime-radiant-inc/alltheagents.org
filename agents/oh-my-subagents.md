---
name: "Oh My Subagents"
slug: "oh-my-subagents"
layout: "agent.njk"
category: "multiplexer"
maker: "ringlochid"
license: "MIT"
url: "https://github.com/ringlochid/oh-my-subagents"
source_code_url: "https://github.com/ringlochid/oh-my-subagents"
source_available: "True"
homepage: "https://ringlochid.me/oh-my-subagents/"
docs_url: "https://ringlochid.me/oh-my-subagents/"
download_url: null
install_method: "pipx install oh-my-subagents, then oms init and oms service install (Python 3.12+; Linux, macOS 13+, Windows 11 x64)"
platforms:
  - "CLI"
  - "Web"
autonomy_level: []
specialization: "general"
language: "Python"
first_released: "2026-07-20"
current_release: "2026-08-30"
maintained: "active"
mcp_support: "True"
plugin_support: "False"
claude_code_plugin: null
subagents: "True"
hooks: "True"
plan_mode: "False"
plugin_docs_url: null
config_docs_url: "https://ringlochid.me/oh-my-subagents/reference/configuration/"
model_providers: "Brings no models: drives the Codex and Claude Code CLIs as Task providers, each with its own accounts and authentication; the separate Operator agent can be either"
pricing: "free"
stars: "181"
sources:
  - "hackernews"
last_verified: "2026-11-19"
date_added: "2026-11-19"
what_makes_it_special: "Turns ad-hoc subagent delegation into durable, accountable teams: delegated Waves, parent waits, child Assignments, and Checkpoints commit to a controller-owned database (SQLite or Postgres), so interrupted runs recover without discarding accepted history, and recursive Manager delegation needs no hidden global polling loop."
---

Oh My Subagents (OMS), renamed from the earlier Banksia release, addresses the operational fragility of ad-hoc subagent delegation — where a parent spawns children, polls them, and loses the only account of what happened when a terminal closes. It is a standalone Python application: the oms CLI installs a per-user background service (systemd user unit, macOS LaunchAgent, or Windows Scheduled Task) that supervises team runs and serves a local web Console, with a separate conversational Operator agent able to draft workflows and control runs through the same controller-owned operations. Teams are reusable, published trees of named responsibilities shaped visually in Workflow Studio; at run time Managers (Codex or Claude Code members, each launched with the provider's own accounts and auth) decide sequentially, in parallel fan-out, or review-and-repair iterations, while the controller persists waits, waves, and Checkpoints so the parent continues with complete returns even after a provider interruption. Eight provider-neutral starter workflows cover production feature delivery, incident investigation, migration, research briefs, security audits, and competing prototypes. Its users are developers running consequential multi-agent tasks who want one accountable Result from the lead, typed Human Requests instead of chat polling, and recovery that never fabricates completion.
