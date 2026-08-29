---
name: "self-improving-agents"
slug: "self-improving-agents"
layout: "agent.njk"
category: "agent"
maker: "BetterForAll"
license: "MIT"
url: "https://github.com/BetterForAll/self-improving-agents"
source_code_url: "https://github.com/BetterForAll/self-improving-agents"
source_available: "True"
platforms:
  - "IDE"
first_released: "2026-04-04"
current_release: "2026-04-09"
stars: "210"
language: "Python"
homepage: null
mcp_support: "False"
plugin_support: "False"
claude_code_plugin: "False"
subagents: "True"
hooks: null
plan_mode: null
model_providers: "Google Gemini"
pricing: "Free / open-source"
install_method: "pip install -r requirements.txt; create .env with GEMINI_API_KEY"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "agent_infra"
what_makes_it_special: "Research presenting 4 progressive levels of self-improving code agents; the Arena Loop (L4) uses adversarial co-evolution where code agents and test agents compete, demonstrating that agents scoring 90-100% on original tests dropped to 62-66% under adversarial suites. L3 agents rewrite their own source code with crash-recovery validation."
---

The repository is a controlled comparison of self-improvement strategies for coding agents, built as four progressively more complex loops: an LLM improving a solution against a benchmark, the same loop with an explanatory reviewer, an agent rewriting its own source, and finally an arena where code agents and test agents co-evolve. Tasks ship as small self-contained problems (snake, support, email validation) with checkpoint and resume, and new tasks slot in via a config/benchmark folder, making the ladder reproducible by others. The experiment harness is Gemini-driven Python with CLI runners, and results are framed as research findings rather than product features. With 23 commits and a single contributor it is a personal research artifact, but a documented and runnable one. It suits researchers studying self-improvement dynamics and educators demonstrating the verifiable-rewards pattern.
