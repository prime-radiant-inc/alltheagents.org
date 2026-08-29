---
name: "multi-agent-ai-sdr-flink-orchestrator"
slug: "multi-agent-ai-sdr-flink-orchestrator"
layout: "agent.njk"
category: "other"
maker: "thefalc"
license: "MIT"
url: "https://github.com/thefalc/multi-agent-ai-sdr-flink-orchestrator"
source_code_url: "https://github.com/thefalc/multi-agent-ai-sdr-flink-orchestrator"
source_available: "True"
platforms: []
first_released: "2025-03-03"
current_release: "2025-05-19"
stars: "46"
language: "Python (agents) and JavaScript/TypeScript (NextJS web app)"
homepage: null
mcp_support: null
plugin_support: null
claude_code_plugin: null
subagents: "True"
hooks: null
plan_mode: null
model_providers: "OpenAI, Azure OpenAI"
pricing: null
install_method: "git clone; web app via npm install && npm run dev; agents app via Python venv, pip install -r requirements.txt, uvicorn app.main:app --reload. Requires Confluent Cloud, Azure OpenAI API key, MongoDB"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/thefalc/multi-agent-ai-sdr-flink-orchestrator"
maintained: "dormant"
sources:
  - "agent_infra"
what_makes_it_special: "Demo app for event-driven multi-agent Sales Development Representative (SDR) workflow. Uses Apache Flink SQL with external LLM model inference as the orchestrator (rather than a traditional agent framework). 5 agents: Lead Ingestion, Lead Scoring, Active Outreach, Nurture Campaign, Send Email. Event-driven architecture using Confluent Cloud/Kafka. Examples for both Autogen and LangGraph. Only 9 commits, low activity. NOTE: This is a multi-agent demo app, not a coding agent harness."
---

The repository demonstrates an architectural idea rather than a product: using Apache Flink SQL, running on Confluent Cloud, as the orchestrator of a multi-agent sales workflow instead of a conventional agent framework. Five agents — lead ingestion, lead scoring, active outreach, nurture campaigns, and email sending — process leads as events on Kafka topics, with a machine-learning router model deciding which agent handles each message; Next.js handles lead capture and MongoDB stores state, while Python agent services expose the LLM logic. Parallel implementations under autogen-example and langgraph-example show the same workflow in two agent frameworks. As a sales automation demo it has nothing to do with coding agents — no code is generated or modified — and its nine commits and lack of releases mark it as a personal demo accompanying the author's write-ups. Its value is as a reference for event-driven multi-agent orchestration rather than as an installable harness.
