# Dossier: Minion Code (proposed census_slug: minion-code)

Compiled 2026-08-21. Facts only. Null convention: "null = not researched"; "False/none = researched and absent". NOT currently in the census — proposed new-entry frontmatter at the end. Small individual project — research kept proportionate.

## 1. Identity

- name: Minion Code (README styles it "MinionCodeAgent"; CLI binary `mcode`; PyPI `minion-code`)
- maker: individual — GitHub user **femto** (PyPI owner "femtowin"); public profile shows no name, company, location, or bio; 384 public repos, 71 followers, account since 2008 [S3][S4] (as-of 2026-08-21). No company entity found (researched, absent).
- product URL / repo URL: https://github.com/femto/minion-code (no separate homepage) [S1]
- license: **conflict** — GitHub API detects AGPL-3.0; README and PyPI metadata say MIT [S1][S2][S5]. See section 6.
- open source? True. source_available: True — full source on GitHub, published on PyPI [S1][S5].
- first public: repo created 2025-10-15 [S1]; first PyPI release 0.1.0 on 2025-10-29 [S5].
- latest release: 0.1.44, 2026-03-15 (PyPI); repo last push also 2026-03-15 — **no activity in ~5 months** as of 2026-08-21 [S5][S1].
- what it is:
  - Form factor: terminal CLI (`mcode`), plus an ACP stdio server (`mcode acp`) for editors like Zed; optional textual TUI dependency [S2][S5].
  - Self-description: "minion's implementation of Claude Code" (repo description) — a pre-configured coding agent built on the maker's own Minion agent framework (`minionx` on PyPI; repo femto/minion, 149 stars, MIT) [S1][S2][S6].
  - Own agentic loop with 12+ built-in tools: file read/write/search, shell execution, Python interpreter, web search; conversation-history management; autonomous tool-use decisions [S2] (maker-described).
  - Models: BYO via the Minion framework's `config.yaml` (examples cite GPT-4o, Claude 3.5 Sonnet); direct deps on both `anthropic` and `openai` SDKs [S2][S5].
  - Pricing: free, open source, BYO API keys [S2].
  - Install: `pip install minionx` then `pip install minion-code` (README shows dev-mode `pip install -e .`); Paseo catalog command `uvx --from minion-code minion-code acp` [S2][task brief].
  - Default autonomy: built-in "security checks for dangerous commands"; per-session permissions in ACP mode; no detailed approval model documented [S2][S5] (maker-described, not independently tested).
  - Language: Python [S1].

## 2. Adoption evidence

| metric / claim | value | as-of | source | type |
|---|---|---|---|---|
| GitHub stars | 39 | 2026-08-21 | [S1] | independently observable |
| GitHub forks | 1 | 2026-08-21 | [S1] | independently observable |
| GitHub watchers (subscribers) | 0 | 2026-08-21 | [S1] | independently observable |
| GitHub open issues | 0 | 2026-08-21 | [S1] | independently observable |
| PyPI downloads `minion-code` | 499/month; 173/week | 2026-08-21 | [S7] | independently observable (incl. mirror/CI noise — real user base likely tiny) |
| Parent framework femto/minion stars | 149 | 2026-08-21 | [S6] | independently observable (context, not minion-code adoption) |
| Maker usage claims | none found | 2026-08-21 | [S2] | researched, absent |
| Funding / customers / community server / press | none found (no Discord or community links in README) | 2026-08-21 | [S2] | researched, absent |
| Ecosystem listing: Paseo | in Paseo's ACP catalog | 2026-08-21 | task brief | independently observable |
| Benchmark placements | none found | 2026-08-21 | [S2] | researched, absent |

## 3. Plugin interface (PRI-2925)

- mcp_support: **client** — loads MCP tools from a JSON config file (`mcode --config MCP.JSON`); no server mode found [S2][S5]. Evidence: https://github.com/femto/minion-code (README)
- plugin_support: **False (researched, absent)** — no skills/plugin/extension system beyond MCP tool loading; extensibility is programmatic via `MinionCodeAgent.create()` and the Minion framework [S2][S5].
- claude_code_plugin: **no** — despite being described as an implementation of Claude Code, no evidence it reads `.claude/` dirs, CLAUDE.md, skills, or the plugin format [S2] (as-of 2026-08-21; README-level check only).
- subagents: **none found** — not mentioned in README/PyPI materials [S2][S5]. (The underlying Minion framework's capabilities not audited — null.)
- hooks: **none found** [S2][S5].
- plan_mode: **none found** [S2][S5].
- plugin_docs_url: none (no docs site; README only). config_docs_url: https://github.com/femto/minion-code (README; model config defers to Minion framework `config.yaml`).
- ACP support: **yes, first-party** — `mcode acp` starts an ACP stdio server; `agent-client-protocol>=0.7.0` is a direct dependency; Zed integration documented; this is how Paseo drives it [S2][S5].
- SDK: **partial** — usable as a Python library (`MinionCodeAgent.create()`, "one-line creation"); the general-purpose SDK is the separate Minion framework [S2][S6].

## 4. Claimed differentiation (raw material for PRI-2927)

- tagline (repo description, verbatim): "minion's implementation of Claude Code" [S1]; README: "An enhanced AI code assistant built on the Minion framework, pre-configured with rich development tools, optimized for code development tasks." [S2]
- maker claims (paraphrased):
  1. Batteries included: pre-configured with 12+ development tools vs. manual agent/tool setup [S2].
  2. "One-line creation, no complex configuration" — immediate usability as a library or CLI [S2].
  3. Built on the maker's own Minion "high performance agent framework that can do everything" [S6].
  4. Editor integration via ACP (Zed) and extensibility via MCP tool loading [S2].
  5. Safety: command-execution restrictions / dangerous-command checks [S2].
- audience: developers who want a ready-made coding agent without assembling one from a framework [S2]. No team-size or stack claims (researched, absent).

## 5. Company & contact targets (PRI-2929)

- Not a company. Individual maintainer: GitHub **femto** / PyPI **femtowin**; profile is intentionally minimal (no public name, employer, or location) [S3][S4]. Public repo identity only, per instruction.
- Contact paths: GitHub issues only [S1].
- Funding stage: none found (researched, absent).

## 6. Open questions / conflicts

- License conflict: GitHub's license detection says AGPL-3.0 [S1] while README text and PyPI classifier say MIT [S2][S5]. Possibly the LICENSE file was switched at some point or README is stale; record as "AGPL-3.0 (repo) / MIT (PyPI)" until the LICENSE file is read directly.
- Maintenance: repo and PyPI both silent since 2026-03-15 (~5 months) — dormant-leaning; Paseo lists it as a live provider regardless.
- "Minion" naming: PyPI framework package is `minionx` (not `minion`); repo is femto/minion. The rename/collision history not researched (null).
- Whether the ACP permission flow actually prompts before file edits/shell was not independently tested (maker-described only).
- The underlying Minion framework's own features (subagents? planning?) not audited — minion-code materials alone show none.

## 7. Sources

1. [S1] https://api.github.com/repos/femto/minion-code — stars, license detection, dates, description
2. [S2] https://raw.githubusercontent.com/femto/minion-code/main/README.md — features, tools, install, ACP/MCP, claims
3. [S3] https://api.github.com/users/femto — maker public identity (minimal)
4. [S4] https://pypi.org/pypi/minion-code/json (owner field) — PyPI owner femtowin
5. [S5] https://pypi.org/pypi/minion-code/json — versions, dates, license classifier, deps, entry points
6. [S6] https://api.github.com/repos/femto/minion — parent framework stars, MIT, description
7. [S7] https://pypistats.org/api/packages/minion-code/recent — downloads

## Inclusion check (Jesse's test)

**Yes** — Minion Code can create and modify software using an LLM with its own agentic loop: the loop and tools (file ops, shell, Python exec) are implemented in the maker's own Minion framework plus this package, not wrapped around another vendor's agent; `mcode acp` exposes that native loop [S2][S5][S6]. Caveat: adoption is near-zero and the project looks dormant since 2026-03-15.

## Proposed census frontmatter (per hc/agents/_TEMPLATE.md — do not write into hc/)

```yaml
name: "Minion Code"
slug: "minion-code"
layout: "agent.njk"
category: "agent"
maker: "femto"                 # individual; GitHub femto / PyPI femtowin; no public name
license: "MIT (PyPI) / AGPL-3.0 per GitHub detection — unresolved conflict"
url: "https://github.com/femto/minion-code"
source_code_url: "https://github.com/femto/minion-code"
source_available: true
homepage: null                 # researched: none beyond the repo
docs_url: "https://github.com/femto/minion-code"
download_url: "https://pypi.org/project/minion-code/"
install_method: "pip install minionx minion-code; uvx --from minion-code minion-code acp"
platforms: ["CLI"]
autonomy_level: ["agentic"]
specialization: "general"
language: "Python"
first_released: "2025-10-29"   # first PyPI release (repo created 2025-10-15)
current_release: "2026-03-15"
maintained: "dormant"          # no commits or releases in ~5 months as of 2026-08-21
mcp_support: "client (JSON config tool loading)"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no (none documented)"
hooks: "no (none documented)"
plan_mode: "no (none documented)"
plugin_docs_url: null
config_docs_url: "https://github.com/femto/minion-code"
model_providers: "BYO via Minion framework config (Anthropic, OpenAI cited)"
pricing: "BYOK"
github_stars: 39
sources: ["paseo-acp-catalog"]
last_verified: "2026-08-21"
what_makes_it_special: "A solo-built 'implementation of Claude Code' on the author's own Minion agent framework: a pre-configured 12-tool coding agent with an ACP server for Zed, aimed at zero-setup use."
```
