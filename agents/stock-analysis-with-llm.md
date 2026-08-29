---
name: "Stock-Analysis-With-Llm"
slug: "stock-analysis-with-llm"
layout: "agent.njk"
category: "other"
maker: "bauer-jan"
license: "MIT"
url: "https://github.com/bauer-jan/stock-analysis-with-llm"
source_code_url: "https://github.com/bauer-jan/stock-analysis-with-llm"
source_available: "True"
platforms:
  - "IDE"
first_released: "2024-11-24"
current_release: "2024-11-24"
stars: "71"
language: "Python"
homepage: null
mcp_support: "False"
plugin_support: null
claude_code_plugin: "False"
subagents: null
hooks: null
plan_mode: "False"
model_providers: "Amazon Bedrock (Anthropic Claude 3)"
pricing: "Free/open-source (incurs AWS usage costs; can be high for large indexes)"
install_method: "cdk deploy in infrastructure folder, run deploy_agents.py, configure Action Groups in AWS Bedrock Console, update src/config.ini and redeploy"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "dormant"
sources:
  - "jim"
what_makes_it_special: "Automated stock analysis and portfolio management system using AWS Bedrock Agents with Anthropic Claude 3. Analyzes stocks across S&P 500, Nasdaq 100, and EURO STOXX 50 using balance sheets, technical indicators, news, and market sentiment, then provides BUY/SELL recommendations and portfolio updates. Two modules: Stock Analyst and Portfolio Manager. Only 1 commit (one-time upload)."
---

The repository wires Amazon Bedrock Agents into a financial workflow: a Stock Analyst module ranks equities across major indices using balance-sheet data, technical indicators, and news, while a Portfolio Manager module applies those recommendations to a simulated portfolio, with user prompts able to steer selection and weighting. Action groups run through Lambda, market data comes from Yahoo Finance, results persist in DynamoDB, and EventBridge schedules ECS tasks on a weekly cadence; no real trades are executed. Infrastructure is defined in AWS CDK with a Python script registering the agents in the Bedrock console. It is a single-commit demonstration with no follow-up development, and it appears in this census only as a misfiled entry — nothing in it creates or modifies code.
