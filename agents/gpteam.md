---
name: "GPTeam"
slug: "gpteam"
layout: "agent.njk"
category: "other"
maker: "101dotxyz"
license: "MIT"
url: "https://github.com/101dotxyz/GPTeam"
source_code_url: "https://github.com/101dotxyz/GPTeam"
source_available: "True"
platforms:
  - "IDE"
first_released: "2023-04-03"
current_release: "2026-08-20"
stars: "1722"
language: "Python (Poetry)"
homepage: "https://www.gpteamai.com/"
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no - uses agents, not a subagent harness"
hooks: "no"
plan_mode: "no"
model_providers: "OpenAI, Anthropic, WindowAI"
pricing: "BYOK"
install_method: "git clone + Poetry"
docs_url: "https://www.gpteamai.com/"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "jim"
what_makes_it_special: "Open-source multi-agent simulation where autonomous AI agents with individual memories interact, move between locations, perform tasks, and collaborate in parallel toward common goals. Agent memory and reflection are inspired by the Generative Agents paper. Includes a Discord integration for observing agent behavior. A research-style simulation rather than a coding-agent harness."
---

GPTeam explores how multiple LLM agents with individual memories cooperate on shared goals: agents hold distinct personalities and memories, move between locations in a simulated world, communicate with each other, and work on tasks in parallel, with reflection mechanics drawn from the Generative Agents research paper. A web UI and a Discord bot let observers watch agents coordinate toward common goals, making it popular as a demonstration of multi-agent communication rather than a tool for building software. It is MIT-licensed Python built with Poetry, run as a simulated world via poetry run world. Development has been idle since 2023-2024 era commits, so it stands as a Generative-Agents-era research simulation rather than an actively used harness.
