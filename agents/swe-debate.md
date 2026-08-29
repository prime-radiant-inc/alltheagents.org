---
name: "SWE-Debate"
slug: "swe-debate"
layout: "agent.njk"
category: "other"
maker: "YerbaPage"
license: "Apache-2.0"
url: "https://github.com/YerbaPage/SWE-Debate"
source_code_url: "https://github.com/YerbaPage/SWE-Debate"
source_available: "True"
platforms: []
first_released: "2025-07-19"
current_release: "2025-11-11"
stars: "33"
language: "Python"
homepage: null
mcp_support: "False"
plugin_support: "False"
claude_code_plugin: "False"
subagents: "True"
hooks: "False"
plan_mode: "False"
model_providers: "OpenAI, OpenAI-compatible (examples use DeepSeek via deepseek/deepseek-chat)"
pricing: "Free/open source"
install_method: "Clone repo, pip install -r localization/requirements.txt, pip install moatless-tree-search, copy .env.example to .env and configure API key"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/YerbaPage/SWE-Debate"
maintained: "active"
sources:
  - "github_topic2"
what_makes_it_special: "Competitive multi-agent debate framework for software issue resolution. Uses competitive multi-agent debate where multiple expert agents collaborate and debate, combined with a graph-driven Entity Localization Pipeline and MCTS-based search (via Moatless framework). Accepted at ICSE 2026."
---

SWE-Debate applies competitive debate to the two hardest stages of automated issue resolution: finding the right code and deciding what to change. An Entity Localization Pipeline extracts classes, methods, and variables from the issue, walks code dependency graphs to build localization chains, and hands candidates to a multi-agent stage where five expert agents debate over three rounds to consolidate a fault localization and repair plan; a ReAct-style coding agent then executes the plan under moatless-tree-search with a value function scoring branches. The code is a compact research artifact (Apache-2.0, ICSE 2026) driven by any OpenAI-compatible endpoint, with examples configured for DeepSeek, and trajectories persist as JSON. It targets SWE-bench researchers studying whether structured disagreement among agents outperforms single-agent localization.
