---
name: "The Factory"
slug: "the-factory"
layout: "agent.njk"
category: "multiplexer"
maker: "akashgit"
license: "MIT"
url: "https://github.com/akashgit/remote-factory"
source_code_url: "https://github.com/akashgit/remote-factory"
source_available: "True"
platforms:
  - "Autonomous"
first_released: "2026-04-11"
current_release: "2026-08-20"
stars: "61"
language: "Python"
homepage: "https://akashgit.github.io/remote-factory/"
mcp_support: "no"
plugin_support: "True"
claude_code_plugin: "True"
subagents: "True"
hooks: "no"
plan_mode: "True"
model_providers: "Claude Code, OpenAI Codex, Bob Shell (IBM)"
pricing: "open-source"
install_method: "uv tool install git+https://github.com/akashgit/remote-factory.git"
docs_url: "https://akashgit.github.io/remote-factory/"
plugin_docs_url: null
config_docs_url: "https://github.com/akashgit/remote-factory/blob/main/docs/configuration.md"
download_url: "https://github.com/akashgit/remote-factory"
maintained: "active"
sources:
  - "brad"
what_makes_it_special: "Domain-agnostic multi-agent software design and evolution harness; describes workflows as Pydantic DAG graphs; executes in 3 modes (Headless Executor, Interactive CEO orchestrating specialist subagents, Outer Loop evolving workflow topologies via MAP-Elites); self-evolving via ACE (Autonomous Context Engineering); distributed as a Claude Code plugin"
---

The Factory (repo: remote-factory) treats software design itself as something agents can improve: it expresses development workflows as Pydantic DAG graphs whose nodes are agents, functions, gates, forks, and joins, then executes those graphs in two ways — a headless executor that walks the graph deterministically, or an interactive 'CEO' agent that follows SKILL.md playbooks while directing eight specialist subprocesses (Researcher, Strategist, Builder, Health Checker, Code Reviewer, Adversarial Tester, Archivist, Failure Analyst). The distinguishing layer is its Outer Loop: MAP-Elites-style evolution mutates the workflow DAGs themselves — nodes, edges, prompts — and evaluates candidates against benchmarks such as SWE-bench, TerminalBench, and its own FeatureBench, selecting workflows by measured test pass rates; a meta mode applies the same improvement loop to the factory's own codebase via ACE (Autonomous Context Engineering). Distribution is as a Claude Code plugin (uv tool install plus /plugin install) or via uv CLI with a Codex runner option. Researchers and practitioners experimenting with self-improving agent pipelines are the target audience.
