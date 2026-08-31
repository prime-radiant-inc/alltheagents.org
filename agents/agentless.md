---
name: "Agentless"
slug: "agentless"
layout: "agent.njk"
category: "other"
maker: "OpenAutoCoder"
license: "MIT"
url: "https://github.com/OpenAutoCoder/Agentless"
source_code_url: "https://github.com/OpenAutoCoder/Agentless"
source_available: "True"
platforms:
  - "CLI"
  - "Autonomous"
first_released: "2024-06-30"
current_release: "2024-12-22"
stars: null
language: "Python"
homepage: null
mcp_support: "False"
plugin_support: "False"
claude_code_plugin: "False"
subagents: "False"
hooks: "False"
plan_mode: "False"
model_providers: "OpenAI,Anthropic"
pricing: "open-source"
install_method: "git clone + conda env + pip install -r requirements.txt"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "jqueryscript"
  - "brad"
  - "ishandutta"
what_makes_it_special: "Agentless approach to automated software repair (SWE-bench): hierarchical fault localization, multi-patch diff sampling, and test-based patch selection without any agent loop."
---

The project demonstrates that LLM-based automated program repair does not require an agentic control loop. Its localization stage narrows from files to classes and functions to concrete edit locations; the repair stage samples many candidate diffs at those locations; and a validation stage runs regression and generated reproduction tests to re-rank and select the final patch. This decomposition keeps behavior inspectable and costs low, achieving 40.7% on SWE-bench Lite and 50.8% on SWE-bench Verified with Claude 3.5 Sonnet. Researchers use it as a baseline for agentic repair systems, and its SWE-bench Lite and Verified runs are published as reproducible artifacts. It is research software driven by an OpenAI-compatible API key, distributed as a Python 3.11 codebase under MIT.
