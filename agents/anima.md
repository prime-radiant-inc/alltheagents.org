---
name: "Anima"
slug: "anima"
layout: "agent.njk"
category: "other"
maker: "Fullive-AI"
license: "Apache-2.0"
url: "https://github.com/Fullive-AI/Anima"
source_code_url: "https://github.com/Fullive-AI/Anima"
source_available: "True"
platforms: []
first_released: "2026-06-01"
current_release: "2026-08-01"
stars: "1038"
language: "Python, TypeScript"
homepage: null
mcp_support: "no"
plugin_support: "yes"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "yes"
model_providers: "OpenAI-compatible (OpenAI, DeepSeek, Doubao, Anthropic via proxy, local Ollama)"
pricing: "open-source"
install_method: "docker"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "agent_infra"
what_makes_it_special: "Open-source Agent OS for hardware intelligence that discovers smart home devices, maintains device state, and uses an LLM Brain to plan context-aware actions within safety boundaries. Zero-config auto device discovery (Xiaomi QR login), evidence-based layered long-term memory that learns user preferences, domain-specific Skill knowledge packages per device type, and local-first runtime. Currently supports Xiaomi/Mi Home (MIoT) devices."
---

Anima (Latin for soul) gives smart homes an LLM brain that discovers devices on the local network, maintains their state, and plans actions within explicit skill boundaries and safety rules — conservative by default for high-risk devices like locks. A LangGraph planner merges environment state, device state, long-term memory (candidate facts promoted to confirmed), and skill packages into action plans executed through protocol adapters, currently Xiaomi MIoT with QR-login token handling. Any OpenAI-compatible provider works (OpenAI, DeepSeek, Doubao, Ollama), and a React dashboard plus REST API expose the loop. Apache-2.0, Docker-first deployment, only six commits since its June 2026 debut but 1.1k stars, with Matter/Home Assistant adapters and multi-user permissions on the roadmap.
