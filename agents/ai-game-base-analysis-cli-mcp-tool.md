---
name: "ai_game_base_analysis_cli_mcp_tool"
slug: "ai-game-base-analysis-cli-mcp-tool"
layout: "agent.njk"
category: "other"
maker: "pirua-game"
license: "Apache-2.0"
url: "https://github.com/pirua-game/ai_game_base_analysis_cli_mcp_tool"
source_code_url: "https://github.com/pirua-game/ai_game_base_analysis_cli_mcp_tool"
source_available: "True"
platforms: []
first_released: "2026-03-22"
current_release: "2026-04-12"
stars: "63"
language: "Python, C#"
homepage: null
mcp_support: "True"
plugin_support: null
claude_code_plugin: null
subagents: null
hooks: null
plan_mode: null
model_providers: "Ollama (local LLM), configurable via gdep config"
pricing: "Free / open source (Apache-2.0)"
install_method: "One-click: install.bat (Windows) / install.sh (macOS/Linux); Manual: pip install -e . in gdep-cli/; MCP: npm install -g gdep-mcp"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://pypi.org/project/gdep/"
maintained: "active"
sources:
  - "github_topic2"
what_makes_it_special: "Game codebase analysis tool analyzing Unity/UE5/Axmol/.NET/C++ projects in <0.5s; provides dependency graphs, impact analysis, circular dep detection, dead code detection, call flow tracing (C++ to Blueprint), lint (19 anti-pattern rules), architecture advice, wiki cache for AI agents"
---

Game codebases defeat ordinary static analysis because logic is split between scripts and engine assets, so the tool pairs a .NET parser (gdep.dll) with a Python CLI (gdep) and an npm-distributed MCP server (gdep-mcp). It builds dependency graphs, impact analysis, circular-dependency and dead-code detection, and call-flow tracing, then exposes them as MCP tools such as analyze_impact_and_risk and trace_gameplay_flow for Claude Desktop, Cursor, or any MCP client. A gdep init step writes a .gdep/AGENTS.md file so agents pick up project context automatically. Solo-dev team, 65 stars, Apache-2.0, distributed on PyPI and npm with multi-language READMEs.
