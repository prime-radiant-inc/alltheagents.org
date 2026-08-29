---
name: "AutoPR"
slug: "autopr"
layout: "agent.njk"
category: "agent"
maker: "irgolic"
license: "MIT"
url: "https://github.com/irgolic/AutoPR"
source_code_url: "https://github.com/irgolic/AutoPR"
source_available: "True"
platforms:
  - "Autonomous"
first_released: "2023-03-18"
current_release: "2026-03-05"
stars: "1371"
language: "Python"
homepage: "https://autopr.com"
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "yes"
model_providers: "OpenAI"
pricing: "open-source"
install_method: "docker"
docs_url: "https://github.com/irgolic/AutoPR/blob/main/USAGE.md"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/marketplace/actions/automatic-pull-request"
maintained: "dead"
sources:
  - "e2b"
  - "jim"
what_makes_it_special: "First bot to autonomously generate pull requests in response to GitHub issues (triggered via label). Built with Guardrails for structured LLM output. Worked ~20% of the time. Now archived."
---

AutoPR, created in early 2023 by irgolic, was among the first bots to autonomously generate pull requests in response to GitHub issues: adding a label containing 'AutoPR' triggered a pipeline that drafted a plan, wrote the code, and opened a pull request, all built on the Guardrails library for structured LLM output. Its author has been candid that it worked about 20% of the time, with known failure modes including incorrect code references and calls to nonexistent functions, and support never extended beyond GitHub. The repository was archived on March 5, 2026 and is preserved read-only as a piece of agent history from the early ChatGPT-era. Its historical value lies in documenting how autonomous PR generation worked before dedicated harnesses matured, and its limitations (duplicated lines, nonexistent function calls) illustrate why later systems added verification layers.
