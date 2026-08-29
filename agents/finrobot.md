---
name: "FinRobot"
slug: "finrobot"
layout: "agent.njk"
category: "other"
maker: "AI4Finance-Foundation"
license: "Apache-2.0"
url: "https://github.com/AI4Finance-Foundation/FinRobot"
source_code_url: "https://github.com/AI4Finance-Foundation/FinRobot"
source_available: "True"
platforms: []
first_released: "2024-02-27"
current_release: "2026-07-27"
stars: "7812"
language: "Python"
homepage: "https://finrobot.ai"
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "yes"
hooks: "no"
plan_mode: "no"
model_providers: "OpenAI"
pricing: "open-source"
install_method: "pip"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "agent_infra"
what_makes_it_special: "Open-source AI agent platform for financial applications (not a coding agent). Automates equity research, investment analysis, and valuation. Strict separation of deterministic financial computation (pure-Python operators) from LLM-based narration -- all financial numbers are code-calculated, not LLM-generated, with full provenance tracking. Multi-agent architecture: 1 Lead Agent, 5 role-based sub-agents (Data, Analysis, Modeling, Synthesis, Report), and 3 debate agents (Bull, Bear, Judge) for investment reasoning. Generates professional equity research reports with DCF, DDM, LBO, comps, WACC, and Monte Carlo analysis. Commercial FinRobot Pro available at finrobot.ai."
---

FinRobot, from the AI4Finance Foundation, applies multi-agent LLM architecture to investment research: a lead orchestrator coordinates role-based pipeline agents through equity research, valuation (DCF, comps, LBO), and risk assessment, with debate agents arguing against drafts before reports finalize. Its design principle separates deterministic computation from narrative generation — Python operators compute every number, and LLMs only shape the reasoning and prose around them, which addresses the reliability problem of LLM-generated financial figures. The project ships as a Python package plus a Tauri/React desktop frontend and is documented in an ICAIF 2024 paper. Its users are quantitative researchers, financial analysts, and academics experimenting with agentic workflows for investment analysis.
