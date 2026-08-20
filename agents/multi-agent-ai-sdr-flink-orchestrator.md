---
name: "multi-agent-ai-sdr-flink-orchestrator"
slug: "multi-agent-ai-sdr-flink-orchestrator"
layout: "agent.njk"
category: "agent"
maker: "thefalc"
license: "MIT"
url: "https://github.com/thefalc/multi-agent-ai-sdr-flink-orchestrator"
source_code_url: "https://github.com/thefalc/multi-agent-ai-sdr-flink-orchestrator"
source_available: True
platforms: []
first_released: "2025-03-03"
current_release: "2025-05-19"
stars: "46"
language: "Python (agents) and JavaScript/TypeScript (NextJS web app)"
homepage: null
mcp_support: null
plugin_support: null
claude_code_plugin: null
subagents: True
hooks: null
plan_mode: null
model_providers: "OpenAI, Azure OpenAI"
pricing: null
install_method: "git clone; web app via npm install && npm run dev; agents app via Python venv, pip install -r requirements.txt, uvicorn app.main:app --reload. Requires Confluent Cloud, Azure OpenAI API key, MongoDB"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/thefalc/multi-agent-ai-sdr-flink-orchestrator"
maintained: "abandoned"
sources:
  - "agent_infra"
what_makes_it_special: "Demo app for event-driven multi-agent Sales Development Representative (SDR) workflow. Uses Apache Flink SQL with external LLM model inference as the orchestrator (rather than a traditional agent framework). 5 agents: Lead Ingestion, Lead Scoring, Active Outreach, Nurture Campaign, Send Email. Event-driven architecture using Confluent Cloud/Kafka. Examples for both Autogen and LangGraph. Only 9 commits, low activity. NOTE: This is a multi-agent demo app, not a coding agent harness."
---

Demo app for event-driven multi-agent Sales Development Representative (SDR) workflow. Uses Apache Flink SQL with external LLM model inference as the orchestrator (rather than a traditional agent framework). 5 agents: Lead Ingestion, Lead Scoring, Active Outreach, Nurture Campaign, Send Email. Event-driven architecture using Confluent Cloud/Kafka. Examples for both Autogen and LangGraph. Only 9 commits, low activity. NOTE: This is a multi-agent demo app, not a coding agent harness.
