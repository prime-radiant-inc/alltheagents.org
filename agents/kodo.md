---
name: "kodo"
slug: "kodo"
layout: "agent.njk"
category: "multiplexer"
maker: "ikamensh"
license: "MIT"
url: "https://github.com/ikamensh/kodo"
source_code_url: "https://github.com/ikamensh/kodo"
source_available: "True"
platforms:
  - "CLI"
  - "Autonomous"
first_released: "2026-02-18"
current_release: "2026-07-18"
stars: "128"
language: "Python"
homepage: null
mcp_support: null
plugin_support: "True"
claude_code_plugin: "False"
subagents: "True"
hooks: null
plan_mode: "True"
model_providers: "Claude Code, Cursor, OpenAI Codex, Gemini CLI, Kimi, Kiro; Gemini API or Anthropic API as orchestrator"
pricing: "Free (MIT); uses existing subscriptions; API orchestrator costs ~$0.13/run (Gemini Flash)"
install_method: "Install uv; uv tool install kodo-agent"
docs_url: "https://github.com/ikamensh/kodo/blob/dev/docs/providers.md"
plugin_docs_url: null
config_docs_url: null
download_url: "https://pypi.org/project/kodo-agent/"
maintained: "active"
sources:
  - "brad"
what_makes_it_special: "Autonomous multi-agent coding orchestrator that runs overnight on Claude Code Max subscription; orchestrator (Gemini Flash or Claude API) directs AI coding agents through work cycles with independent verification by architect + tester agents; supports goal-based building, testing like a real user, and code review/improvement modes; custom teams via team.json"
---

kodo exists to convert idle-night time and flat-rate agent subscriptions into finished, verified work: an orchestrator LLM delegates tasks to coding agents through work cycles with role separation (workers, architect verifier, testers), optionally parallelized across git worktrees. Modes include goal-building runs, kodo test for user-style bug hunting, and kodo --improve for senior-developer-style review with --fix-from to repair earlier findings. Because agents run with bypassPermissions, the docs direct users to commit or back up first. Individual developers on Claude Code Max subscriptions use it for unattended feature work and codebase improvement.
