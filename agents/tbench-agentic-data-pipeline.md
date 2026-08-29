---
name: "tbench-agentic-data-pipeline"
slug: "tbench-agentic-data-pipeline"
layout: "agent.njk"
category: "other"
maker: "Danau5tin"
license: null
url: "https://github.com/Danau5tin/tbench-agentic-data-pipeline"
source_code_url: "https://github.com/Danau5tin/tbench-agentic-data-pipeline"
source_available: "True"
platforms:
  - "CLI"
first_released: "2025-07-26"
current_release: "2025-07-28"
stars: "73"
language: "Python"
homepage: null
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "n/a"
subagents: "True"
hooks: "no"
plan_mode: "no"
model_providers: "Claude (Anthropic)"
pricing: "free"
install_method: "git clone then uv sync"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/Danau5tin/tbench-agentic-data-pipeline"
maintained: "dormant"
sources:
  - "github_topic4"
what_makes_it_special: "Multi-agent synthetic data generation pipeline that produces validated training data for terminal-based coding tasks for RL training. Uses 20+ Claude Code instances working in parallel through three specialized agent stages (idea generation, datapoint building, quality review) coordinated by a central Task Manager. Generated 331+ validated datapoints across software engineering, sysadmin, security, and other categories. Docker-based validation pipeline (build, test discovery, fail-first checks, weight validation). Not a general-purpose coding agent harness."
---

The pipeline exists because RL training for terminal agents needs large quantities of verified, executable tasks, and hand-curation does not scale. It turns Terminal Bench seed tasks into training datapoints through a three-stage agent workforce: idea-generation agents diversify seed tasks, datapoint-builder agents construct each task's dockerfile, tests, and weights and iterate until validation passes, and quality-review agents approve or reject the result. A central Task Manager hands out work atomically over a shared filesystem, tracks parent-child provenance, and recovers from timeouts, while validation requires tests to fail before any fix and weights to normalize. The output — 331+ validated datapoints spanning software engineering, sysadmin, security, and debugging — fed the author's terminal-bench-rl training work. It is tooling for RL data production rather than a user-facing agent, and it has no license file.
