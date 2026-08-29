---
name: "AutoBE"
slug: "autobe"
layout: "agent.njk"
category: "agent"
maker: "wrtnlabs"
license: "AGPL-3.0"
url: "https://github.com/wrtnlabs/autobe"
source_code_url: "https://github.com/wrtnlabs/autobe"
source_available: "True"
platforms:
  - "CLI"
  - "Autonomous"
first_released: "2025-04-28"
current_release: "2026-06-24"
stars: null
language: "TypeScript"
homepage: "https://autobe.dev"
mcp_support: "False"
plugin_support: "False"
claude_code_plugin: "False"
subagents: "True"
hooks: "False"
plan_mode: "yes"
model_providers: "OpenAI,Anthropic,Google,Qwen,GLM,MiniMax,Kimi"
pricing: "open-source"
install_method: "git clone + pnpm install + pnpm run playground"
docs_url: "https://autobe.dev/docs/"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/wrtnlabs/autobe"
maintained: "active"
sources:
  - "jqueryscript"
what_makes_it_special: "AI backend builder that generates 100% compilable NestJS+Prisma backends via a waterfall pipeline of 40+ specialized agents (Analyze, Database, Interface, Test, Realize)."
---

AutoBE, by Wrtn Labs, generates complete TypeScript backends (NestJS + Prisma) from natural-language requirements, aiming at 100% compilable output rather than probabilistic code generation. Its waterfall pipeline moves through Analyze, Database, Interface, Test, and Realize phases, each handled by specialized agents and validated by AI-friendly compilers that check language-neutral ASTs against type schemas before any code is emitted, with the option to stop at any phase (spec-only, API design only, etc.). Generated backends include a type-safe client SDK, and a benchmark harness scores 13+ models across todo/reddit/shopping/ERP projects with live results at autobe.dev/benchmark. The system is TypeScript (AGPL-3.0 for the generator; generated applications can be relicensed freely), run via a WebSocket playground or the @autobe/agent library, and consumes 30M-250M+ tokens per project. It targets backend teams wanting spec-driven, compilation-guaranteed service generation.
