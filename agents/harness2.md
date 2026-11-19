---
name: "Harness²"
slug: "harness2"
layout: "agent.njk"
category: "agent-sdk"
maker: "google-research"
license: "Apache-2.0"
url: "https://github.com/google-research/harness2"
source_code_url: "https://github.com/google-research/harness2"
source_available: "True"
homepage: "https://harness2.github.io"
docs_url: "https://github.com/google-research/harness2/tree/main/docs"
download_url: null
install_method: "uv venv --python 3.12 .venv && uv pip install -e '.[render]' from the repository root (Linux, Python 3.12, uv; Node 20+ and Google Cloud CLI for model-backed runs)"
platforms:
  - "CLI"
autonomy_level: []
specialization: "general"
language: "Python"
first_released: "2026-10-06"
current_release: "2026-11-02"
maintained: "active"
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: null
subagents: "True"
hooks: "True"
plan_mode: null
plugin_docs_url: null
config_docs_url: null
model_providers: "Drives external executors with fixed weights: OpenCode (default) or Codex (--substrate cx), configured for Vertex Gemini solver/judge and Vertex Claude or Gemini improver; LAB also supports the upstream judge's direct providers"
pricing: "free"
stars: "24403"
sources:
  - "hackernews"
last_verified: "2026-11-19"
date_added: "2026-11-19"
what_makes_it_special: "A plug-and-play framework for recursive agent harnessing: task-level recursion refines the execution harness per task with a contrastive Propose–Probe–Compose step (no ground-truth feedback), while a persistent improvement harness accumulates adopted harnesses and lessons to guide future refinement. Eight editable components — system prompt, guardrails, memory, tool guidance, subagents, skills, scripts, and plugins — are materialized into OpenCode or Codex and benchmarked on JobBench, LAB, and WorkBuddy-Bench."
---

Harness² is Google Research's answer to a harness-design problem: agents keep meeting tasks their harness was never designed for, so instead of freezing one harness it optimizes the harness itself. The framework connects two recursions with model weights fixed. Task-level recursion runs a Propose–Probe–Compose step — a harness editor proposes invariant and domain-specific edits, candidate probes execute them on the same task, and a composer builds a refined harness from behavioral contrasts between executions, with no ground-truth feedback. Harnessing-level recursion feeds every adopted harness and evidence-supported lesson into a persistent improvement harness that guides the next task's refinement. The unit of optimization is a tree of eight editable components (system prompt, guardrails, memory, tool guidance, subagents, skills, scripts, plugins) that Harness² materializes as substrate-native files for an executor — OpenCode by default, Codex via --substrate cx — and its Python package ships the CLI, benchmark adapters, and judge plumbing as installable primitives, while the coding loop itself always belongs to the executor it drives. Researchers report gains up to 11.5 points on WorkBuddy-Bench and 11.8 percentage points on LAB's partial pass rate from a single step; the paper (arXiv 2610.14224) and the disclaimer mark it as research code, not an officially supported Google product.
