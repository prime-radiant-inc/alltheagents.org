---
name: "Breakaway Agent"
slug: "breakaway-agent"
layout: "agent.njk"
category: "agent"
maker: "2389-research"
license: null
url: "https://github.com/2389-research/breakaway-agent"
source_code_url: "https://github.com/2389-research/breakaway-agent"
source_available: "True"
platforms:
  - "CLI"
first_released: null
current_release: null
stars: "2"
language: "TypeScript"
homepage: null
mcp_support: "no"
plugin_support: "yes (swappable policy, context strategy, tools, system prompt)"
claude_code_plugin: "no"
subagents: "yes (spawn_agent tool with depth cap)"
hooks: "no"
plan_mode: "no"
model_providers: "OpenAI-compatible (configurable via .env)"
pricing: "free"
install_method: "git clone, bun install"
docs_url: null
maintained: "active"
sources:
  - "user_reported"
what_makes_it_special: "Deliberately tiny, hackable code agent and experiment platform with a policy-blind core loop (~165 lines in src/agent.ts) where all behavior is injected via a Policy object — error policy, max turns, context strategy, and tools are all user-editable. Runs in YOLO mode with no permission prompts, supports self-modification via SIGHUP/SIGUSR2 hot-reload, and detached subagents."
---

Breakaway Agent is a deliberately small experiment bed for people who want to study and reshape the agent loop itself. Built on Bun, the core loop lives in roughly 165 lines of TypeScript and exposes only five tools — read_file, write_file, edit_file, bash, and spawn_agent — with every behavioral knob (error policy, max turns, context strategy, system prompt, tool set) injected through a swappable Policy object rather than hardcoded. It runs in YOLO mode with no permission prompts, so it is comfortable executing long unattended runs, and it treats its own code as mutable: a SIGHUP or SIGUSR2 hot-reload re-reads its configuration and policy without dropping the session, making self-modification part of the workflow. Detached subagents fan out via spawn_agent under a depth cap. The audience is researchers and tinkerers exploring agent-loop design, not users who want a polished out-of-the-box coding assistant.
