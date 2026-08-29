---
name: "HyperAgent"
slug: "hyperagent"
layout: "agent.njk"
category: "agent"
maker: "FSoft-AI4Code"
license: "MIT"
url: "https://github.com/FSoft-AI4Code/HyperAgent"
source_code_url: "https://github.com/FSoft-AI4Code/HyperAgent"
source_available: "True"
platforms: []
first_released: "2023-11-23"
current_release: "2024-12-10"
stars: "252"
language: "Python"
homepage: null
mcp_support: "False"
plugin_support: "False"
claude_code_plugin: "False"
subagents: "True"
hooks: "False"
plan_mode: "True"
model_providers: "Anthropic (extensible via api_type and base_url)"
pricing: "Free / open-source"
install_method: "conda create -n hyperagent python=3.10 then pip3 install -e . (requires pre-installing Zoekt + universal-ctags)"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/FSoft-AI4Code/HyperAgent"
maintained: "dormant"
sources:
  - "github_topic"
what_makes_it_special: "First generalist SE agent handling multiple task types (GitHub issue resolution, repo-level code generation, fault localization, program repair) across multiple programming languages (Python & Java). Multi-agent architecture (Planner, Navigator, Code Editor, Executor) mimicking human developer workflows with state-of-the-art results on SWE-Bench Verified (31.4%), RepoExec (53.3% Pass@5), and Defects4J (249 bugs fixed). Last commit November 2024."
---

HyperAgent came out of FPT Software's AI4Code research group as a generalist alternative to single-purpose repair or localization systems: one four-agent pipeline switches between patch generation and fault-prediction modes depending on the task. A Planner decomposes the issue, a Navigator locates relevant code using Zoekt and universal-ctags indexes, a Code Editor writes changes, and an Executor runs them in a Jupyter kernel, with each agent configurable to a different LLM. It reported 31.4% on SWE-Bench Verified, 25% on Lite, 53.3% Pass@5 on RepoExec, and 249 fixed Defects4J bugs. The repo has seen no commits since November 2024 and functions as archived research code accompanying the arXiv paper.
