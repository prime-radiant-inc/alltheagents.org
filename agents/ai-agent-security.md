---
name: "Ai-Agent-Security"
slug: "ai-agent-security"
layout: "agent.njk"
category: "other"
maker: "SecurityLab-UCD"
license: null
url: "https://github.com/SecurityLab-UCD/ai-agent-security"
source_code_url: "https://github.com/SecurityLab-UCD/ai-agent-security"
source_available: "True"
platforms: []
first_released: "2024-04-18"
current_release: "2024-12-15"
stars: "6"
language: "Python"
homepage: "https://arxiv.org/pdf/2406.08689"
mcp_support: "False"
plugin_support: "False"
claude_code_plugin: "False"
subagents: "False"
hooks: "False"
plan_mode: "False"
model_providers: "OpenAI"
pricing: "Free / open-source (research project)"
install_method: "source ./env.sh && pip install -r requirements.txt && cd HE_data && python HE_data.py && cd ../"
docs_url: "https://arxiv.org/pdf/2406.08689"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/SecurityLab-UCD/ai-agent-security"
maintained: "dormant"
sources:
  - "jim"
what_makes_it_special: "Research demo implementing homomorphic encryption as a defense for AI agents, presented at RAIE'25 (ICSE 2025 workshop). Includes SSN agent and HE agent demos showing encryption-based protection of sensitive data. Paper-accompanying research artifact with only 23 commits."
---

Agents that handle sensitive data leak it through prompts and context, and this repository explores one defensive idea: run the agent's reasoning over homomorphically encrypted values so the LLM never sees plaintext. The HE agent demo performs sum or product tasks on encrypted data through OpenAI models, with documented limits (results above 400 fail with the default encryptor) and a known indexing bug; a second demo shows encrypted protection of SSN data. The code accompanies 'Security of AI Agents' (arXiv:2406.08689) presented at the RAIE workshop at ICSE 2025 by UC Davis Security Lab researchers, with sandbox evaluation code maintained in a separate AgentBench fork. Its audience is security researchers evaluating encryption-based agent defenses, not developers choosing a coding tool.
