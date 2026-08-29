---
name: "race-condition"
slug: "race-condition"
layout: "agent.njk"
category: "other"
maker: "GoogleCloudPlatform"
license: "Apache-2.0"
url: "https://github.com/GoogleCloudPlatform/race-condition"
source_code_url: "https://github.com/GoogleCloudPlatform/race-condition"
source_available: "True"
platforms:
  - "Web"
  - "Autonomous"
first_released: "2026-03-27"
current_release: "2026-08-17"
stars: "221"
language: "Go (gateway/services), Python (AI agents), TypeScript/Angular (frontend)"
homepage: "https://developers.google.com/solutions/learn/race-condition"
mcp_support: "True"
plugin_support: null
claude_code_plugin: null
subagents: "True"
hooks: "no"
plan_mode: "no"
model_providers: "Gemini (Vertex AI),Ollama,vLLM on GKE"
pricing: "Free"
install_method: "git clone the repo, then make init"
docs_url: "https://developers.google.com/solutions/learn/race-condition"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/GoogleCloudPlatform/race-condition"
maintained: "active"
sources:
  - "github_topic3"
what_makes_it_special: "Multi-agent marathon simulation where AI agents (Planner, Simulator, Runners) plan a Las Vegas marathon route, simulate environment (weather, traffic, crowds), and race autonomously over the A2A protocol; demoed at Google Cloud Next '26 Developer Keynote."
---

Race-condition is the open-source release of the multi-agent marathon simulation Google demoed at Cloud Next '26, published as a deployable reference architecture rather than a product. Planner agents design a race course using Google Maps MCP tools, GIS data, and financial modeling; a Simulator agent advances the environment tick by tick; and Runner agents make per-tick pacing decisions, communicating over the A2A protocol through a Go WebSocket gateway that batches traffic from hundreds of concurrent runners. Three planner variants — baseline, LLM-as-judge evaluation, and AlloyDB-backed memory — demonstrate progressive capability additions, while a deterministic autopilot runner provides a zero-API-cost baseline. The frontend can replay recorded agent streams indistinguishably from live runs, a reliability measure from the keynote that doubles as a free testing path. Google Cloud engineers use it as a starting template for building A2A-based multi-agent systems on Cloud Run and Vertex AI.
