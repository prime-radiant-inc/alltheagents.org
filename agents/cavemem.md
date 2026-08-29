---
name: "cavemem"
slug: "cavemem"
layout: "agent.njk"
category: "other"
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
maintained: "dormant"
sources:
  - "github_deep"
what_makes_it_special: "Cross-agent persistent memory for coding assistants. Hooks fire at session boundaries, compress observations with caveman grammar (~75% fewer prose tokens, code/paths preserved byte-for-byte, round-trip expandable), write to local SQLite. Agents query their own history via stdio MCP server (search, timeline, get_observations, list_sessions, enrich). Hooks: SessionStart, UserPromptSubmit, PostToolUse, Stop, SessionEnd (Claude Code); partial for Codex, Copilot, Augment; query-only for Cursor/Gemini CLI/Antigravity/IBM Bob. Local SQLite + FTS5 + vector hybrid search. Cross-IDE installers covering 9 coding assistants. NOTE: Frozen August 2026 — no longer in active development; core lives on in the 'caveman' repo."
---

cavemem exists because coding agents lose context between sessions, forcing them to re-derive decisions and repeat mistakes. It installs hook handlers across nine coding assistants — Claude Code, OpenCode, Codex CLI, GitHub Copilot, and Augment get full capture, while Cursor, Gemini CLI, Antigravity, and IBM Bob get query-only access — and fires at session boundaries to compress observations before writing them to a local SQLite database. Agents retrieve their own history through an MCP server exposing search, timeline, and observation tools, with hybrid FTS5 keyword and vector search over the store. All data stays local by default, with embeddings handled by a local provider, Ollama, or OpenAI, and private blocks redacted before compression. The project froze in August 2026, with its compressed-memory core carried forward in the author's actively developed caveman repository.
