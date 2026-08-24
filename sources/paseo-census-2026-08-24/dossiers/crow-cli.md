# Dossier: crow-cli (census_slug: crow-cli)

Compiled 2026-08-24. Facts only. Null convention: "null = not researched"; "False/none = researched and absent". Sources [Sn] in section 7. NOT in census — proposed new-entry frontmatter at the end of section 6. Small individual project — research kept proportionate.

## 1. Identity

- name: Crow / crow-cli (PyPI `crow-cli`; GitHub org `crow-cli`, org description "Minimal ACP Agent")
- maker: individual — GitHub user **odellus**, public name "Thomas Wood", bio "Applied mathematician, Chief scientist @phytomech", location "Live Oak, FL"; the crow-ai.dev site names him as its creator (site summary rendered him "CTO at Phytomech" — his GitHub bio says Chief Scientist). Crow is a personal project under its own GitHub org (org location "United States of America", 6 followers), not a Phytomech product as far as reachable materials show [S2][S3][S9] (as-of 2026-08-24)
- product URL: https://crow-ai.dev/ | repo URL: https://github.com/crow-cli/crow-cli
- license: MIT (GitHub API + README License section) [S1][S4]
- open source? True. source_available: True — full source; sibling repos crow-ui (Rust ACP client, 3 stars) and crow-ade (TypeScript, 1 star) in the same org [S1][S8]
- first public release: repo created 2026-02-05; first PyPI release 0.1.0 on 2026-03-01 [S1][S6]
- latest release: v0.1.37, 2026-08-24 (GitHub release + PyPI same version); 31 PyPI versions in ~6 months; repo pushed 2026-08-24 [S5][S6][S1]
- what it is:
  - Form factor: terminal CLI (`crow-cli run` one-shot, `-i` REPL) + ACP agent server for editors (`crow-cli acp`, e.g. Zed custom agent); companion Rust ACP client (crow-ui) and "Crow ADE" exist as separate early repos [S4][S8]
  - Models: BYO via any OpenAI-compatible provider (OpenRouter, OpenAI, own endpoint) configured in `~/.agents/crow/config.yaml`; built on the `openai` Python SDK [S4][S7]
  - Pricing: free, MIT; user supplies API keys ("bring your own keys, bring your own models" per site) [S4][S9]
  - Install: clone + `uv tool install . --python 3.14` (README); site offers `curl -fsSL crow-ai.dev/install.sh | bash`; PyPI package exists. Requirements: Python 3.14+, uv, Docker (for the bundled SearXNG web-search service) [S4][S9][S6]
  - Default autonomy: not explicitly documented in README (no approval-mode section found); ACP mode defers permissioning to the client's capabilities; "cancellable tasks with fine-grained supervision" is a site claim [S4][S9] — null on exact default prompting behavior
  - Language: Python [S1]

## 2. Adoption evidence

For a project this size, "no signals found" is itself the finding: adoption is minimal and early.

| metric / claim | value | as-of | source | type |
|---|---|---|---|---|
| GitHub stars | 56 | 2026-08-24 | [S1] | independently observable |
| GitHub forks / watchers / open issues | 5 / 1 / 0 | 2026-08-24 | [S1] | independently observable |
| Contributors | 2 identities, one person: odellus 402 commits + "Thomas Wood" 2 (anon) — solo project | 2026-08-24 | [S5] | independently observable |
| PyPI downloads `crow-cli` | 1,035/month; 155/week; 86/day | 2026-08-24 | [S6] | independently observable |
| GitHub release-asset downloads | 0-9 per release (most 0) | 2026-08-24 | [S5] | independently observable |
| Release cadence | 31 PyPI versions 2026-03-01 → 2026-08-24; multiple GitHub releases per week in Aug 2026 | 2026-08-24 | [S5][S6] | independently observable |
| Hacker News | 1 submission ("Crow-CLI: Minimal MCP based ACP agent"), 1 point, 2026-04-30 | 2026-08-24 | [S10] | independently observable |
| Community channels | none found (no Discord/Slack linked in README) | 2026-08-24 | [S4] | researched, absent |
| Maker usage claims / customers / funding / benchmarks / press | none found | 2026-08-24 | [S4][S9][S10] | researched, absent |

## 3. Plugin interface (PRI-2925)

- mcp_support: **both, in an unusual shape** — the agent's own tools are served by a bundled MCP server (`crow-cli mcp`: read/write/edit, terminal, web_search/web_fetch via SearXNG, webcam/image vision, memory tools), and users can register any external MCP server in config.yaml, its tools appearing alongside automatically ("Extensible by design"). So: MCP client for external servers AND ships an MCP server — though the server exists to provide its own tools, not to expose the agent to others. README warns tool names are not namespaced (collision risk) [S4] (as-of 2026-08-24). Evidence: https://github.com/crow-cli/crow-cli#readme
- plugin_support: **partial** — Skills: reusable skill directories with `SKILL.md` loaded from `~/.agents/skills/`; README: "Skill distribution is still being worked out; today skills are local directories"; site mentions a public skill catalog (crow-ai.dev/docs/skills/) [S4][S9]
- claude_code_plugin: **partial** — consumes the open `SKILL.md` skills convention (same format family Claude Code uses) from `~/.agents/skills/`; no `.claude/` discovery or Claude Code plugin-format support found [S4]
- subagents: **True** — multi-agent delegation is the core design: launch a worker agent, then any agent can read its session via the shared sqlite memory tools (`list_sessions`, `query_memory`, `query_session`); "agents recall past conversations and can delegate work to one another" [S4]
- hooks: **False** — no lifecycle-hook system found in README or pyproject (researched in reachable materials, absent) [S4]
- plan_mode: **False** — no plan/read-only mode found in README (researched in reachable materials, absent) [S4]
- plugin_docs_url: https://crow-ai.dev/docs/skills/ (skills; per site) — no dedicated plugin doc in repo
- config_docs_url: https://github.com/crow-cli/crow-cli#configuration (`~/.agents/crow/config.yaml`)
- ACP support: **yes, first-party and identity-defining** — `crow-cli acp` runs the agent as an ACP server; depends on the official `agent-client-protocol[http]` Python SDK (>=0.12.0); detects client capabilities (terminals, file read/write) and uses native ACP versions, falling back to its MCP tools otherwise; documented Zed config [S4][S7]
- SDK: **none found** — a Python package importable in principle, but no documented SDK surface (researched, absent) [S4][S7]

## 4. Claimed differentiation (raw material for PRI-2927)

- tagline: org description (verbatim): "Minimal ACP Agent" [S3]; site (verbatim, per fetch): "multi-agent editor with shared memory and orchestration" [S9]; repo description: "MCP based ACP agent" [S1]
- maker claims (paraphrased, README + site) [S4][S9]:
  1. Persistence as the point, not an afterthought: every session in a local sqlite db (FTS5/BM25 search, WAL, schema v5); "the sqlite file is the integration point" — no service to run
  2. Multi-agent delegation through shared memory: any agent can list sessions, search all past conversations, and read another agent's session; memorable coolname session ids
  3. ACP-native, no proprietary protocol; works in any ACP client (Zed documented; org maintains a fork/client of its own, crow-ui)
  4. Tools-as-MCP architecture: agent's own toolbox is an MCP server; any external MCP server's tools mount alongside automatically
  5. Self-hosted web search out of the box: ships a maintained SearXNG docker config
  6. Multimodal: vision input incl. webcam capture tool
  7. BYO keys/models via OpenAI-compatible providers; user retains infrastructure control
  8. Streaming ReAct loop with tool calling, cancellation, conversation compaction; full test tiers incl. live-LLM e2e
- audience: users of ACP editors and open-source agent tooling who want data ownership/local persistence [S9]. No role/team-size claims (researched, absent).

## 5. Company & contact targets (PRI-2929)

- Not a company. Individual maintainer: GitHub **odellus** ("Thomas Wood", 70 followers); the project has its own GitHub org (crow-cli, created 2026-03-01, 10 public repos incl. forks of alacritty/ollama/llama.cpp) [S2][S3]. Per instruction, only the public identity is recorded; his employer (Phytomech) appears in his public bio but Crow shows no Phytomech affiliation.
- Contact paths the project offers: GitHub issues [S7]
- Funding: none found (researched, absent)

## 6. Open questions / conflicts

- Brief said tagline "Minimal ACP Native Coding Agent" and command `crow-cli acp` — command confirmed verbatim [S4]; the org self-description is "Minimal ACP Agent" and the repo's is "MCP based ACP agent"; the exact briefed phrase was not found but is consistent.
- Site vs README install: site offers `curl -fsSL crow-ai.dev/install.sh | bash`; README documents only clone + uv (and PyPI exists). Which is canonical is unclear; the install.sh contents were not inspected.
- Docker + Python 3.14 + SearXNG requirement is an unusually heavy prerequisite stack for a "minimal" agent — factual observation from README requirements [S4].
- Default approval behavior (does it ask before edits/shell in CLI mode?) not documented in README — null, would need running it.
- "Public skill catalog" (site) vs "skill distribution is still being worked out" (README) — mild tension; README is likely the more current ground truth [S4][S9].
- crow-ade and crow-ui (the "multi-agent editor" the site leads with) are 1- and 3-star early repos; the site's editor framing runs ahead of the visible code maturity.
- pyproject description is literally "Add your description here" — packaging hygiene signal [S7].
- Proposed new census entry (per _TEMPLATE.md schema v1.1):

```yaml
---
name: "Crow"
slug: "crow-cli"
layout: "agent.njk"
category: "agent"
maker: "odellus"           # new makers.json record: maker_type individual, country US, makes_models false, revenue_model []
license: "MIT"
url: "https://crow-ai.dev/"
source_code_url: "https://github.com/crow-cli/crow-cli"
source_available: True
homepage: "https://crow-ai.dev/"
docs_url: "https://crow-ai.dev/docs/"
download_url: "https://pypi.org/project/crow-cli/"
install_method: "curl -fsSL crow-ai.dev/install.sh | bash (site); or clone + uv tool install (README); Python 3.14+, uv, Docker for SearXNG"
platforms: ["CLI"]
autonomy_level: ["agentic"]
specialization: "general"
language: "Python"
first_released: "2026-03-01"   # first PyPI release; repo created 2026-02-05
current_release: "2026-08-24"  # v0.1.37
maintained: "active"
mcp_support: True              # client for external servers; own tools shipped as a bundled MCP server
plugin_support: "partial"      # SKILL.md skills from ~/.agents/skills; distribution "still being worked out"
claude_code_plugin: "partial"  # shares the SKILL.md convention; no .claude/ or plugin-format support
subagents: True
hooks: False
plan_mode: False
plugin_docs_url: "https://crow-ai.dev/docs/skills/"
config_docs_url: "https://github.com/crow-cli/crow-cli#configuration"
model_providers: "BYO via OpenAI-compatible endpoints (OpenRouter, OpenAI, custom)"
pricing: "free"
github_stars: "56"
sources: ["paseo-acp-catalog"]
last_verified: "2026-08-24"
what_makes_it_special: "Solo-built Python ACP agent whose defining bet is persistence: every session lives in a shared local sqlite database with full-text search, so multiple agents can delegate work and read each other's sessions; its own toolbox ships as an MCP server and it bundles self-hosted SearXNG web search."
---
```

## 7. Sources

1. [S1] https://api.github.com/repos/crow-cli/crow-cli — stars, forks, dates, license, language, description
2. [S2] https://api.github.com/users/odellus — maker public identity
3. [S3] https://api.github.com/orgs/crow-cli (+ /users/crow-cli/repos) — org identity, sibling repos
4. [S4] https://raw.githubusercontent.com/crow-cli/crow-cli/main/README.md — architecture, ACP/MCP/skills, memory design, requirements, license
5. [S5] https://api.github.com/repos/crow-cli/crow-cli/releases + /contributors — releases, asset downloads, contributor split
6. [S6] https://pypi.org/pypi/crow-cli/json + https://pypistats.org/api/packages/crow-cli/recent — versions, dates, downloads
7. [S7] https://raw.githubusercontent.com/crow-cli/crow-cli/main/pyproject.toml — dependencies (agent-client-protocol, openai, fastmcp), version
8. [S8] https://api.github.com/repos/crow-cli/crow-ade — sibling editor repo status
9. [S9] https://crow-ai.dev/ (WebFetch summary) — tagline, creator, install.sh, differentiator claims
10. [S10] https://hn.algolia.com/api/v1/search?query=%22crow-cli%22 — HN signal (1 point)

## Inclusion check (Jesse's test)

**Yes** — crow-cli implements its own agentic loop ("a streaming ReAct loop with tool calling, cancellation, conversation compaction, and multimodal input", src/crow_cli project layout lists "ACP server, ReAct loop, CLI") calling OpenAI-compatible LLMs directly via the `openai` SDK with its own MCP-served toolbox; `crow-cli acp` exposes that native loop, wrapping no other vendor's agent [S4][S7].
