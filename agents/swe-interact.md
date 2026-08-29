---
name: "SWE-Interact"
slug: "swe-interact"
layout: "agent.njk"
category: "other"
maker: "scaleapi"
license: "Apache-2.0"
url: "https://github.com/scaleapi/SWE-Interact"
source_code_url: "https://github.com/scaleapi/SWE-Interact"
source_available: "True"
platforms: []
first_released: "2026-06-29"
current_release: "2026-06-30"
stars: "24"
language: "Shell"
homepage: null
mcp_support: "False"
plugin_support: "False"
claude_code_plugin: "False"
subagents: "False"
hooks: "False"
plan_mode: "False"
model_providers: "OpenAI, Anthropic, Google, Kimi"
pricing: "Free / open-source"
install_method: "git clone Harbor repo, uv tool install ., then set up Modal (uv pip install modal + modal setup)"
docs_url: "https://arxiv.org/abs/2606.30573"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/scaleapi/SWE-Interact"
maintained: "active"
sources:
  - "github_topic2"
what_makes_it_special: "Benchmark of 75 tasks evaluating coding agents on realistic multi-turn, user-driven software engineering sessions using a simulated user (GPT-5.5) that interacts with the agent across turns, plus rubric-based grading (Anthropic Opus) — moving beyond single-turn benchmark evaluation toward authentic developer-agent collaboration."
---

SWE-Interact, from Scale AI, rethinks SWE evaluation around how engineers actually work with agents: long sessions in which requirements shift and the user supplies context. Its 75 tasks run inside the Harbor harness on Modal sandboxes, where a simulated user model converses with the coding agent over many turns, and success is decided by rubric-based grading from a separate judge model rather than by hidden unit tests alone. The design deliberately stresses behaviors single-turn benchmarks miss — clarifying requirements, recovering from changed instructions, and communicating trade-offs. Run configs cover single-turn baselines and multi-turn sessions for agents such as Codex and Claude Code, and the accompanying paper (arXiv 2606.30573) motivates the user-driven framing. Teams benchmarking coding agents for interactive, multi-turn use are the audience.
