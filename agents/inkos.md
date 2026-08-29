---
name: "InkOS"
slug: "inkos"
layout: "agent.njk"
category: "agent"
maker: "Narcooo"
license: "AGPL-3.0"
url: "https://github.com/Narcooo/inkos"
source_code_url: "https://github.com/Narcooo/inkos"
source_available: "True"
platforms:
  - "CLI"
  - "Autonomous"
first_released: "2026-03-12"
current_release: "2026-08-17"
stars: "9137"
language: "TypeScript"
homepage: null
mcp_support: "no"
plugin_support: "yes"
claude_code_plugin: "no"
subagents: "yes"
hooks: "no"
plan_mode: "yes"
model_providers: "Google Gemini, Moonshot, MiniMax, Zhipu, Bailian, DeepSeek, SiliconFlow, Volcengine, Tencent Hunyuan, Wenxin, iFlytek Spark, OpenRouter, Ollama, LM Studio"
pricing: "open-source"
install_method: "npm"
docs_url: "https://github.com/Narcooo/inkos/blob/master/README.en.md"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "caramaschi"
what_makes_it_special: "Story Creation AI Agent system for novels, scripts, interactive film/games, and translation. Unified pi-agent harness integrating chat agents, deterministic pipelines, and structured tool execution. 37-dimension continuity auditing with built-in anti-AI-detection writing. Structured state management with Zod schema validation, SQLite FTS5/BM25 retrieval, atomic file commits. Interactive open-world play mode. Multi-line plot branching without modifying canon. Style fingerprint cloning. Per-agent model routing. 15 built-in SKILL.md skills. KIMI Open Source partner (sponsored by Moonshot AI)."
---

InkOS applies agent-harness mechanics to long-form fiction, where continuity across hundreds of chapters is the core problem. Each chapter runs a plan, compose, write, audit, revise pipeline over a three-layer memory (JSON state, Markdown projections, SQLite time-series), with 37 continuity checks and deliberate 'de-AI-flavor' rewriting. Beyond novels, it ships one-shot short stories, an interactive open-world play mode with world contracts, style imitation via analyze/import, and EPUB export. Fifteen SKILL.md skills are built in, and per-agent model routing lets the Writer run on one provider while the Auditor uses another. Writers, web-fiction studios, and interactive-fiction developers use its Studio web UI, TUI, or daemon mode with Telegram and Feishu notifications.
