---
name: "GEAR"
slug: "gear"
layout: "agent.njk"
category: "agent-sdk"
maker: "rsi-gear"
license: "MIT"
url: "https://github.com/rsi-gear/gear"
source_code_url: "https://github.com/rsi-gear/gear"
source_available: "True"
homepage: "https://rsi-gear.github.io/"
docs_url: "https://rsigear.xyz/docs/gear"
download_url: null
install_method: "npm install --global rsi-gear@latest agent-hitch@latest (plus a task-agent runtime such as @deepseek-ai/dsh); or build matching source and use the Python SDK"
platforms:
  - "CLI"
autonomy_level: []
specialization: "general"
language: "TypeScript"
first_released: "2026-08-18"
current_release: "2026-11-18"
maintained: "active"
mcp_support: "False"
plugin_support: "True"
claude_code_plugin: null
subagents: "False"
hooks: "True"
plan_mode: null
plugin_docs_url: null
config_docs_url: "https://rsigear.xyz/docs/gear/configuration"
model_providers: "Any: task agent and Meta agent are user-configured existing agents with their own providers (e.g. DSH + Luna, Codex + Astra, Pi)"
pricing: "free"
stars: "477"
sources:
  - "hackernews"
last_verified: "2026-11-19"
date_added: "2026-11-19"
what_makes_it_special: "An open evolutionary architecture for recursive self-improvement of LLM agent harnesses: seven callable optimization algorithms (GEPA, RandomSearch, OPRO, ACE, RRSI, DarwinX, Harness2) evolve an agent's prompts, tools, and workflows against a benchmark, with the task agent and the Meta agent allowed to use different models."
---

GEAR starts from the observation that a model's harness — its instructions, tools, and workflows — is as decisive as the model, and that a harness can be evolved with feedback from real task evaluations. The framework runs a two-level loop: an inner loop in which a task agent executes benchmark tasks under a fixed harness configuration, and an outer loop in which a Meta agent analyzes trajectories and evaluation results, proposes candidate harness modifications, and retains the best candidate per the configured objective. Optimization touches only the components the user authorizes — prompts and policies, tools and hooks, skills and workflows, context management, with model-weight training experimental — and task execution runs through the separate Hitch evaluation runner, so GEAR itself never runs the tasks it scores. Teams use it through the Python SDK's Project.refine, the gear CLI, or a Refine Skill installed into Codex, Claude Code, or DSH, optimizing their own benchmarks in Harbor format.
