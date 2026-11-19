---
name: "Agensh"
slug: "agensh"
layout: "agent.njk"
category: "multiplexer"
maker: "microsoft"
license: "MIT"
url: "https://github.com/microsoft/Agensh"
source_code_url: "https://github.com/microsoft/Agensh"
source_available: "True"
homepage: null
docs_url: "https://github.com/microsoft/Agensh#readme"
download_url: null
install_method: "git clone + Docker Compose on Linux (Docker Engine, Compose v2, systemd, cgroup v2; passwordless sudo for Docker); launch a team with python3 -m agensh.project run against a project.toml, selecting the per-worker harness with --agent-harness copilot|pi|codex|claude"
platforms:
  - "Autonomous"
autonomy_level:
  - "autonomous-background"
specialization: "general"
language: "Python"
first_released: "2026-08-27"
current_release: "2026-11-03"
maintained: "active"
mcp_support: null
plugin_support: null
claude_code_plugin: null
subagents: "True"
hooks: null
plan_mode: null
plugin_docs_url: null
config_docs_url: null
model_providers: "GitHub Copilot CLI (default), Pi, OpenAI Codex, or Claude Code as the per-worker harness — each brings its own model provider (gpt-5.6-sol default via the gateway, per-worker models configurable)"
pricing: "free"
stars: "931"
sources:
  - "hackernews"
last_verified: "2026-11-19"
date_added: "2026-11-19"
what_makes_it_special: "A decentralized multi-agent harness that scales one GitHub repository's work across up to 1,024 agents with no central orchestrator: workers discover and claim sub-tasks through a Gitea workspace, Mattermost messaging, and shared context, and the accompanying paper reports ProgramBench pass rates improving ~49% from 1 agent to 128."
---

Agensh is Microsoft's answer to the question of how much of a software project a team of agents can finish when nobody coordinates them centrally: it scales to 1,024 workers that each gather context, claim sub-tasks, take action, verify results, and merge progress asynchronously, connected by a shared workspace (Gitea), a messaging interface (Mattermost), and a shared-context mechanism adapted from DeLM. A run is defined by a TOML project file that names the upstream repo, the goal, acceptance commands, worker count, token budget, and coordination rules (planning worker, peer-review paths), and a team launches as a set of Docker Compose projects on one Linux host; the arXiv paper (2609.26781, September 2026) reports the experiments behind the design, including Pandoc test-pass rates rising from 33.89% with one agent to 55.06% with 1,024 under a six-hour budget. Each worker runs a real coding harness inside its container — Copilot CLI by default, with Pi, Codex, and Claude Code selectable at launch through adapters — so the harnesses bring their own models and tools, and Agensh contributes the coordination loop rather than the coding. The release ships the harness, the experiment launch scripts, a reproduction guide, and a software-project pack that delivers the finished main branch back upstream as a pull request, aimed at researchers studying agent-team scaling and teams wanting to point a fleet at one repository.
