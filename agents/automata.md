---
name: "Automata"
slug: "automata"
layout: "agent.njk"
category: "agent"
maker: "emrgnt-cmplxty"
license: "Apache-2.0"
url: "https://github.com/emrgnt-cmplxty/automata"
source_code_url: "https://github.com/emrgnt-cmplxty/automata"
source_available: "yes"
platforms:
  - "IDE"
  - "Autonomous"
first_released: "2023-06-20"
current_release: "2023-09-05"
stars: "681"
language: "Python"
homepage: "https://github.com/emrgnt-cmplxty/automata"
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "OpenAI"
pricing: "open-source"
install_method: "pip"
docs_url: "https://automata.readthedocs.io/en/latest/"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/emrgnt-cmplxty/automata"
maintained: "dead"
sources:
  - "e2b"
what_makes_it_special: "Self-coding agent designed to evolve into a fully autonomous, self-programming AI system. Combines LLMs (GPT-4) with a vector database to document, search, and write code. Goal is a completely autonomous, self-programming software engineer that generates its own documentation and code indices to continuously build its expertise and autonomy. NOTE: Repo archived by owner on Mar 16, 2024 (read-only). Install via Poetry or Docker."
---

Automata was an early (2023) attempt at a self-coding agent aimed at eventually becoming a fully autonomous, self-programming AI system. It combined GPT-4-class LLMs with a vector database and SCIP-derived code symbol graphs, letting agents document, search, and write code via toolkits and code/doc embeddings. The project explored how an agent could index its own codebase (symbol code and doc embeddings, SCIP-based symbol graphs) and use that index for retrieval-augmented coding. Development stalled and the repository was archived on March 16, 2024, remaining as a snapshot of the pre-tooling era of autonomous coding experiments. Its ideas influenced later work by the same author (emrgnt-cmplxty) on memory-augmented systems.
