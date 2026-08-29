---
name: "Multi-Agent-AI-System"
slug: "multi-agent-ai-system"
layout: "agent.njk"
category: "other"
maker: "FareedKhan-dev"
license: "MIT"
url: "https://github.com/FareedKhan-dev/Multi-Agent-AI-System"
source_code_url: "https://github.com/FareedKhan-dev/Multi-Agent-AI-System"
source_available: "True"
platforms: []
first_released: "2025-05-31"
current_release: "2025-05-31"
stars: "373"
language: "Python"
homepage: "https://medium.com/@fareedkhandev/6cb70487cd81"
mcp_support: null
plugin_support: null
claude_code_plugin: null
subagents: "True"
hooks: null
plan_mode: null
model_providers: "OpenAI"
pricing: "Free / open-source"
install_method: "git clone, pip install -r requirements.txt"
docs_url: "https://langchain-ai.github.io/langgraph/"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/FareedKhan-dev/Multi-Agent-AI-System"
maintained: "active"
sources:
  - "github_topic3"
what_makes_it_special: "Multi-agent AI customer support system using LangGraph + LangSmith supervisor-based orchestration with two subagents (music catalog, invoice/billing), human-in-the-loop verification, persistent short/long-term memory, and structured agent evaluation. (Not a coding agent — it's a customer support system tutorial.)"
---

This is a tutorial artifact, not a tool: Fareed Khan's repository accompanies a Medium walkthrough of building supervisor-based multi-agent systems with LangGraph and LangSmith, using the Chinook digital-music sample database as its domain. A supervisor routes queries between two ReAct subagents — one for the music catalog, one for invoice and billing — with human-in-the-loop verification interrupting the flow until a customer's identity is confirmed before invoice access, and memory split between short-term checkpointing and a long-term store that persists user music preferences between sessions. LangSmith datasets and evaluators grade final responses, and the write-up compares supervisor versus swarm architectures. The code lives in one notebook plus a utility file, last touched in 2025, and exists to be read alongside the blog post rather than deployed. It entered the census through keyword matching on 'multi-agent system' and is neither a coding agent nor a harness.
