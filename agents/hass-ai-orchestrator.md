---
name: "HASS-AI-Orchestrator"
slug: "hass-ai-orchestrator"
layout: "agent.njk"
category: "other"
maker: "ITSpecialist111"
license: "MIT"
url: "https://github.com/ITSpecialist111/HASS-AI-Orchestrator"
source_code_url: "https://github.com/ITSpecialist111/HASS-AI-Orchestrator"
source_available: "True"
platforms:
  - "Autonomous"
first_released: "2025-12-15"
current_release: "2026-07-11"
stars: "58"
language: "Python, TypeScript"
homepage: "https://github.com/ITSpecialist111/HASS-AI-Orchestrator"
mcp_support: "True"
plugin_support: "False"
claude_code_plugin: "False"
subagents: "True"
hooks: "False"
plan_mode: "True"
model_providers: "Ollama, OpenAI, Anthropic, GitHub Models, Microsoft Foundry"
pricing: "Free/open source add-on (users supply their own models/API keys)"
install_method: "Home Assistant add-on: Settings -> Add-ons -> Add-on Store -> Repositories -> add https://github.com/ITSpecialist111/HASS-AI-Orchestrator -> install AI Orchestrator"
docs_url: "https://github.com/ITSpecialist111/HASS-AI-Orchestrator/blob/main/ai-orchestrator/README.md"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "agent_infra"
what_makes_it_special: "Policy-aware control plane for the home combining LLM reasoning with deterministic safety controls: Model proposes, Code validates, Humans remain in control, Home Assistant executes. Dry-run-by-default, schema validation, plan interception/approval, atomic checkpointed replay, audit trails, sandboxed generated dashboards, episodic memory (RAG via ChromaDB)."
---

HASS-AI-Orchestrator brings LLM reasoning to Home Assistant without giving the model unsupervised control. An agent observes entity states, areas, and device metadata, then proposes changes as recorded intents with risk summaries; a deterministic kernel validates each proposal against tool schemas, domain allowlists, and blocked domains (such as shell_command), and a human approves before checkpointed, replayable execution — the model never holds authority over what actually runs. Three reasoning profiles (Rapid, Balanced, Deep) trade iteration depth against latency on a single local or cloud model, and proactive triggers fire on schedules or state changes with cooldowns. Memory combines ChromaDB-backed entity knowledge and past episodes with RAG over manuals, and a React dashboard handles audits, approvals, and generated dashboards in a sandboxed studio. It targets Home Assistant users who want agentic automation under explicit human policy control.
