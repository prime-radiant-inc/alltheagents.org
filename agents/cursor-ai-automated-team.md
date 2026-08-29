---
name: "Cursor AI Automated Team"
slug: "cursor-ai-automated-team"
layout: "agent.njk"
category: "other"
maker: "joinwell52-AI"
license: "NOASSERTION"
url: "https://github.com/joinwell52-AI/joinwell52"
source_code_url: "https://github.com/joinwell52-AI/joinwell52"
source_available: "True"
platforms:
  - "IDE"
first_released: "2026-03-29"
current_release: "2026-08-20"
stars: "4"
language: "JavaScript"
homepage: "https://joinwell52-ai.github.io/joinwell52/"
mcp_support: "True"
plugin_support: "False"
claude_code_plugin: "False"
subagents: "True"
hooks: "True"
plan_mode: "False"
model_providers: "Cursor SDK / Cursor API"
pricing: "Free / open-source"
install_method: "git clone https://github.com/joinwell52-AI/joinwell52.git && cd joinwell52 && npm ci && npm run demo && npm run tmpa:s1.0:conformance"
docs_url: "https://joinwell52-ai.github.io/joinwell52/"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/joinwell52-AI/joinwell52.git"
maintained: "active"
sources:
  - "caramaschi"
what_makes_it_special: "TMPA (Textual Multi-Agent Process Architecture) — vendor-neutral governance architecture for long-running work performed by AI agents and humans. Treats AI agent work as durable governance objects rather than facts trapped in chat/model sessions. Reconstructs lifecycle, authority, conflicts, and audit state from inspectable text evidence. Four-role fixed team (PM/DEV/OPS/QA) with EVAL observing independently."
---

joinwell52 publishes TMPA, a vendor-neutral governance architecture aimed at the gap between agent traces (what ran) and accountability (who was responsible and why results were accepted). The repository holds the Core S1.0 specification, conformance schemas and fixtures, a Node.js reference Reader that reconstructs work objects from evidence, and research write-ups, with the related FCoP coordination protocol and a frozen historical implementation of the CodeFlowMu product kept in separate MIT-licensed repos. The current commercial product line is closed-source. Community traction is minimal (single-digit stars), the evidence is self-run rather than independently certified, and the audience is researchers and governance teams evaluating agent accountability frameworks.
