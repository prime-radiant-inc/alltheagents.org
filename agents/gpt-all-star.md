---
name: "gpt-all-star"
slug: "gpt-all-star"
layout: "agent.njk"
category: "agent"
maker: "kyaukyuai"
license: "MIT"
url: "https://github.com/kyaukyuai/gpt-all-star"
source_code_url: "https://github.com/kyaukyuai/gpt-all-star"
source_available: "True"
platforms:
  - "Web"
  - "Autonomous"
first_released: "2023-12-20"
current_release: "2026-08-13"
stars: "238"
language: "Python"
homepage: "https://kyaukyuai.github.io/gpt-all-star/"
mcp_support: "False"
plugin_support: "False"
claude_code_plugin: "False"
subagents: "True"
hooks: "False"
plan_mode: "True"
model_providers: "OpenAI, Azure OpenAI, Anthropic"
pricing: "Free / open-source"
install_method: "pip install gpt-all-star; or Docker + Poetry for development"
docs_url: "https://kyaukyuai.github.io/gpt-all-star/"
plugin_docs_url: null
config_docs_url: null
download_url: "https://pypi.org/project/gpt-all-star/"
maintained: "active"
sources:
  - "github_topic"
what_makes_it_special: "AI-powered code generation tool for scratch development of web applications using a team collaboration of autonomous AI agents — users assemble a group of AI agents, choose leaders for each step, leaders create action plans, and team members work together to complete every task. Supports Plan-and-Solve Prompting via --plan_and_solve flag."
---

The project frames app generation as team management: the user picks which AI agents join the team and who leads each phase, and leaders break work into tasks that agent members execute toward a finished React application. It is built on LangChain/LangGraph in Python, supports OpenAI, Azure OpenAI, and Anthropic models, and ships as a pip package with a companion Streamlit web UI for watching the team work. Development has been quiet since its 2023-2024 burst of activity, with the last release activity trailing off and open PRs unmerged, and output quality is bounded by its validated stack of React plus Chakra UI plus JavaScript. It remains a readable demonstration of agentic team workflows more than a production tool.
