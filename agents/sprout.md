---
name: "Sprout"
slug: "sprout"
layout: "agent.njk"
category: "agent"
maker: "prime-radiant-inc"
license: "Proprietary"
url: "https://github.com/prime-radiant-inc/sprout"
source_code_url: "https://github.com/prime-radiant-inc/sprout"
source_available: "True"
homepage: null
docs_url: "https://github.com/prime-radiant-inc/sprout#readme"
download_url: null
install_method: "git clone https://github.com/prime-radiant-inc/sprout && cd sprout && bun install"
platforms:
  - "CLI"
  - "Web"
autonomy_level:
  - "agentic"
specialization: "general"
language: "TypeScript"
first_released: "2026-02-25"
current_release: "2026-08-06"
maintained: "active"
mcp_support: "True"
plugin_support: "False"
claude_code_plugin: null
subagents: "True"
hooks: "False"
plan_mode: "False"
plugin_docs_url: null
config_docs_url: null
model_providers: "Anthropic, OpenAI, OpenAI Codex, Google"
pricing: "free"
stars: "111"
sources:
  - "github-issue"
last_verified: "2026-09-18"
date_added: "2026-09-18"
what_makes_it_special: "A recursive coding agent whose root never calls a tool itself: every action is a delegation to a specialist subagent, and repeated failures trigger an async learning pass that mutates a git-backed agent genome."
---

Sprout is an experiment in pushing delegation to its limit. A root agent takes a goal, breaks it into subgoals, and hands each to a specialist; specialists can delegate further, so only leaf agents ever touch the eight immutable kernel primitives (read_file, write_file, edit_file, apply_patch, exec, grep, glob, fetch). A verifier and a debugger check work before it lands, and a quartermaster meta-agent can answer what exists, plan how to do something, or fabricate a new specialist at runtime, which is how the roster grows. Stumbles, timeouts, and retries are detected automatically: three repeats of the same mistake or two unresolved errors trigger an asynchronous learning pass that mutates the agent genome, a git-backed store of agent definitions, memories, and routing rules where every change is committed for audit and rollback. Agents talk over a WebSocket pub/sub bus and can run as separate processes; the whole thing runs as an Ink terminal UI or a browser UI on port 7777, maps abstract model tiers onto Anthropic, OpenAI, OpenAI Codex, and Google, and reaches MCP servers through a bundled client. The README reports a 3.7% average stumble rate across 2,201 tracked sessions, and is honest that this is early-stage work aimed at developers curious about recursive multi-agent architectures rather than anyone wanting a finished product.
