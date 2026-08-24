# Standardized differentiation extraction: crow-cli

Run 2026-08-24 against official materials only (see Sources).

1. **One-sentence self-description:** An Agent Client Protocol coding agent for the terminal and ACP-compatible editors that reads and edits code, runs commands, searches the web, and remembers work across sessions.

2. **Claimed differentiators** (by prominence):
   - Persistence as the point: every session in a local sqlite database with full-text search; "Most agent toolkits treat persistence as an afterthought" — capability/workflow — https://github.com/crow-cli/crow-cli#readme
   - Multi-agent delegation via shared memory: any agent can list, search, and read other agents' sessions through three memory tools; the sqlite file is the integration point — capability — README
   - ACP-native with no proprietary protocol; works in any ACP client (Zed config documented) — openness/integration — README, https://crow-ai.dev/
   - Tools-as-MCP: the agent's own toolbox is a bundled MCP server, and any external MCP server's tools mount alongside automatically — capability/openness — README
   - Self-hosted web search out of the box (maintained SearXNG docker config) plus BYO keys/models via OpenAI-compatible providers — openness — README, site

3. **Stated audience:** users of ACP editors and open-source agent tooling who want data ownership and local infrastructure control — https://crow-ai.dev/. No role or team-size claims.

4. **Positioning against others:** "Most agent toolkits treat persistence as an afterthought" (category allusion, no competitor named) — README; site notes its preferred Zed fork comes with "no affiliation with Zed Industries".

5. **Evidence offered for claims:** none offered — no benchmarks, user numbers, or customers; the README's visible three-tier test suite (unit/integration/live-LLM e2e) is the closest thing to offered evidence.

6. **Notable silences:** no plan/read-only mode; no hooks; no approval/permission modes documented for CLI use; no sandboxing; no enterprise features; no pricing page (free/MIT implied); no model benchmark or provider count claims; skill distribution admitted unfinished.

7. **Confidence:** medium — README is detailed and candid, but the website adds claims (skill catalog, editor framing) that run ahead of the repo, and there is no launch post; positioning is inferred mostly from one document.

Sources: https://github.com/crow-cli/crow-cli (README, pyproject.toml); https://crow-ai.dev/ (site + /docs/skills/); https://github.com/crow-cli (org description).
