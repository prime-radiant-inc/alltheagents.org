---
name: "MapCoder"
slug: "mapcoder"
layout: "agent.njk"
category: "agent"
maker: "Md-Ashraful-Pramanik"
license: "MIT"
url: "https://github.com/Md-Ashraful-Pramanik/MapCoder"
source_code_url: "https://github.com/Md-Ashraful-Pramanik/MapCoder"
source_available: "True"
platforms: []
first_released: "2024-04-29"
current_release: "2025-02-12"
stars: "194"
language: "Python"
homepage: null
mcp_support: "False"
plugin_support: "False"
claude_code_plugin: "False"
subagents: "True"
hooks: "no"
plan_mode: "True"
model_providers: "OpenAI, Azure"
pricing: "Free / open-source"
install_method: "git clone; pip install -r requirements.txt; set up .env; python src/main.py"
docs_url: "https://md-ashraful-pramanik.github.io/mapcoder.github.io/"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "dormant"
sources:
  - "github_topic4"
what_makes_it_special: "Multi-agent code generation framework for competitive programming using four LLM agents (retrieval, planning, coding, debugging) with an adaptive agent traversal schema that dynamically cascades; achieved SOTA pass@1 on 8 benchmarks (HumanEval 93.9%, MBPP 83.1%, CodeContests 28.5%); accepted at ACL 2024. Repo explicitly states it will no longer be maintained (successor is CodeSIM)."
---

MapCoder replicated the human competitive-programming cycle across four LLM agents: a retrieval agent recalls similar solved problems from the model's own memory (no external retriever), a planner produces step-by-step solutions conditioned on those examples, a coding agent translates plans into code tested against sample I/O, and a debugging agent fixes failures using the plan as context. The adaptive traversal scheme lets agents cascade and retry dynamically rather than follow a fixed flow, which drove state-of-the-art pass@1 on eight benchmarks at publication (93.9% HumanEval, 83.1% MBPP with GPT-4). The ACL 2024 paper documents the method, and the authors have ended maintenance in favor of their successor, CodeSIM.
