---
name: "Simmer"
slug: "simmer"
layout: "agent.njk"
category: "other"
maker: "2389-research"
license: "MIT"
url: "https://github.com/2389-research/simmer"
source_code_url: "https://github.com/2389-research/simmer"
source_available: "True"
platforms:
  - "IDE"
first_released: null
current_release: null
stars: "14"
language: null
homepage: null
mcp_support: "no"
plugin_support: "yes (Claude Code plugin)"
claude_code_plugin: "yes"
subagents: "yes (judge board of multiple agents)"
hooks: "no"
plan_mode: "no"
model_providers: "Claude (via Claude Code)"
pricing: "free"
install_method: "/plugin marketplace add 2389-research/claude-plugins, then /plugin install simmer@2389-research"
docs_url: null
maintained: "active"
sources:
  - "user_reported"
what_makes_it_special: "Iterative artifact refinement for Claude Code where a judge board constructs problem-specific judges that read the code, understand the problem, and propose one high-leverage fix per round (ASI), with best-so-far always preserved. Works on any artifact — documents, prompts, pipelines, configs, workspaces."
---

Simmer is a Claude Code plugin for iterative artifact refinement, and the agent loop stays with Claude Code. Its mechanism is a judge board that constructs problem-specific judges: each judge reads the code, understands the problem at hand, and proposes exactly one high-leverage fix per round — the Asymmetric Single Improvement (ASI) step — with the best-so-far artifact always preserved so rounds can only improve, never regress. The refinement target is not limited to code; it works on documents, prompts, pipelines, configs, and whole workspaces. Sibling plugins in the same family, like cookoff and omakase-off, take related approaches. The audience is Claude Code users who want a structured, non-destructive improvement loop for any artifact they care about.
