---
name: "recursive-coding-agents"
slug: "recursive-coding-agents"
layout: "agent.njk"
category: "other"
maker: "rawwerks"
license: "NOASSERTION"
url: "https://github.com/rawwerks/recursive-coding-agents"
source_code_url: "https://github.com/rawwerks/recursive-coding-agents"
source_available: "True"
platforms:
  - "Web"
first_released: "2026-06-16"
current_release: "2026-06-30"
stars: "22"
language: "TypeScript"
homepage: null
mcp_support: "False"
plugin_support: "False"
claude_code_plugin: "False"
subagents: "no"
hooks: "False"
plan_mode: "False"
model_providers: null
pricing: "Free / open-source"
install_method: null
docs_url: "https://recursivecodingagents.com"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/rawwerks/recursive-coding-agents"
maintained: "active"
sources:
  - "github_topic3"
what_makes_it_special: "Public talk website, RLM rubric, and calibration examples for the 'Recursive Coding Agents' talk at AI Engineer World's Fair 2026. Provides a concrete seven-gate RLM rubric with judging methodology and verdict-shaped calibration examples to distinguish true Recursive Language Model systems from imposters."
---

Recursive Coding Agents is the companion artifact to Raymond Weitekamp's AI Engineer World's Fair 2026 talk on recursive language models — systems where the model manages its own context programmatically rather than holding everything in the window. The repository publishes the RLM definition, a seven-gate rubric for judging whether a system qualifies, and a judging methodology that scores by the shape of an agent's run rather than by product label. Its most distinctive content is the calibration sets: paired examples of runs that satisfy the rubric and near-miss counterexamples — drawn from Claude dynamic workflows and OpenProse — that show how close a system can get while still failing a gate. The site itself is a SvelteKit slide deck deployed on Cloudflare Workers, with all-rights-reserved licensing and no contribution path. Agent researchers use it as shared vocabulary for evaluating whether a harness genuinely implements the RLM pattern.
