---
name: "cavemem"
slug: "cavemem"
layout: "agent.njk"
category: "agent"
maker: "JuliusBrussee"
license: "MIT"
url: "https://github.com/JuliusBrussee/cavemem"
source_code_url: "https://github.com/JuliusBrussee/cavemem"
source_available: "yes"
platforms:
  - "IDE"
first_released: "2026-04-18"
current_release: "2026-08-14"
stars: "674"
language: "TypeScript"
homepage: "https://caveman.so/"
mcp_support: "yes (stdio)"
plugin_support: "yes"
claude_code_plugin: "no"
subagents: "no"
hooks: "yes"
plan_mode: "no"
model_providers: "local, ollama, openai (embeddings)"
pricing: "open-source"
install_method: "npm"
docs_url: "https://caveman.so/"
plugin_docs_url: null
config_docs_url: null
download_url: "https://www.npmjs.com/package/cavemem"
maintained: "abandoned"
sources:
  - "github_deep"
what_makes_it_special: "Cross-agent persistent memory for coding assistants. Hooks fire at session boundaries, compress observations with caveman grammar (~75% fewer prose tokens, code/paths preserved byte-for-byte, round-trip expandable), write to local SQLite. Agents query their own history via stdio MCP server (search, timeline, get_observations, list_sessions, enrich). Hooks: SessionStart, UserPromptSubmit, PostToolUse, Stop, SessionEnd (Claude Code); partial for Codex, Copilot, Augment; query-only for Cursor/Gemini CLI/Antigravity/IBM Bob. Local SQLite + FTS5 + vector hybrid search. Cross-IDE installers covering 9 coding assistants. NOTE: Frozen August 2026 — no longer in active development; core lives on in the 'caveman' repo."
---

Cross-agent persistent memory for coding assistants. Hooks fire at session boundaries, compress observations with caveman grammar (~75% fewer prose tokens, code/paths preserved byte-for-byte, round-trip expandable), write to local SQLite. Agents query their own history via stdio MCP server (search, timeline, get_observations, list_sessions, enrich). Hooks: SessionStart, UserPromptSubmit, PostToolUse, Stop, SessionEnd (Claude Code); partial for Codex, Copilot, Augment; query-only for Cursor/Gemini CLI/Antigravity/IBM Bob. Local SQLite + FTS5 + vector hybrid search. Cross-IDE installers covering 9 coding assistants. NOTE: Frozen August 2026 — no longer in active development; core lives on in the 'caveman' repo.
