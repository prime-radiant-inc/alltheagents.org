# Dossier: Autohand Code CLI (census_slug: autohand-code-cli)

Compiled 2026-08-24. Facts only. Null convention: "null = not researched"; "False/none = researched and absent". Sources [Sn] in section 7. Small project — research kept proportionate.

## 1. Identity

- name: Autohand Code CLI (canonical command `autohand`; also installs as `autohand-code` and `agent`)
- maker: company — **Autohand AI** (GitHub org `autohandai`, location "New Zealand", 41 followers; COMMERCIAL.md names "Autohand AI LLC") [S1][S9] (as-of 2026-08-24)
- product URL: https://www.autohand.ai/cli/ (repo homepage field: https://www.autohand.ai/code/) [S2] — both return HTTP 403 to plain fetchers; the site is JS-rendered, page title "Autohand CLI | Your Codebase, Understood at Scale" [S10]
- repo URL: https://github.com/autohandai/code-cli
- license: Apache-2.0 per GitHub API and README, BUT with a maker-imposed carve-out: companies with ARR > USD $5M "must obtain a commercial license from Autohand AI LLC" (COMMERCIAL.md) — effectively dual licensing, not plain Apache-2.0 [S2][S3][S9] (as-of 2026-08-24)
- open source? source_available: True — full source in repo; also a separate ACP adapter repo (autohandai/autohand-acp) and SDK repos [S2][S5]
- first public release: repo created 2025-12-12 [S2]; latest release: v0.9.7-alpha.d24c4e6, 2026-08-21; repo pushed 2026-08-23 [S2][S4] (as-of 2026-08-24)
- what it is:
  - Form factor: terminal CLI/REPL (Bun + Ink TUI) with one-shot command mode for CI/CD; VS Code extension; native ACP mode for Zed/JetBrains; iOS companion app pairing (`/go`) for remote steer/monitor; `/squad` multi-agent runtime [S3] (as-of 2026-08-24)
  - Models: BYO multi-provider — README lists OpenRouter, LLMGateway, OpenAI, AWS Bedrock, DeepSeek, Azure Foundry Models, Z.ai, and local models [S3]
  - Pricing: free open source for individuals/non-profits/edu/OSS/companies under $5M ARR; commercial license above that [S9]
  - Install: `curl -fsSL https://autohand.ai/install.sh | bash`; `brew install autohandai/code/autohand-code`; clone + Bun build [S3]
  - Default autonomy: interactive with approval before risky operations; Shift+Tab cycles edit / plan / YOLO / auto modes; `--yes`, `--unrestricted`, `--restricted`, `--dry-run`, `--auto-commit` flags [S3]
  - Language: TypeScript (Bun runtime) [S2]
  - Notable installer behavior (README's own words, paraphrased): every Autohand installer scans every writable directory on PATH and replaces any existing `agent` command it finds — from any tool, not just Autohand's own — automatically and without prompting [S3]

## 2. Adoption evidence

| metric / claim | value | as-of | source | type |
|---|---|---|---|---|
| GitHub stars | 178 | 2026-08-24 | [S2] | independently observable |
| GitHub forks / watchers | 26 / 3 | 2026-08-24 | [S2] | independently observable |
| GitHub open issues | 103 | 2026-08-24 | [S2] | independently observable |
| Contributors | 3 total: igorcosta 1,240 commits (~96%), rest bots (github-actions 32, dependabot 14) — effectively a solo project inside a company shell | 2026-08-24 | [S4] | independently observable |
| npm `autohand-cli` downloads | 4,784/week; 26,394/month | 2026-08-24 (weeks ending 2026-08-23) | [S6] | independently observable |
| npm `@autohandai/autohand-acp` downloads | 606/week; 1,767/month | 2026-08-24 | [S6] | independently observable |
| Release-asset downloads | latest stable v0.9.6 (2026-08-12): 342; alphas: 6-40 each | 2026-08-24 | [S4] | independently observable |
| VS Code marketplace (AutohandAI.vscode-autohand) | 189 installs, 314 downloads, 1 rating (5.0); released 2026-02-03, last updated 2026-02-26 | 2026-08-24 | [S8] | independently observable |
| Hacker News | one "Autohand" story, 1 point, 0 comments (2026-01-13); no traction found | 2026-08-24 | [S7] | independently observable |
| Discord | server exists (discord.gg/ZM3TCtwCwG); member count not researched | 2026-08-24 | [S3] | null (size) |
| Maker usage claims / customers / funding / benchmarks | none found in README or reachable materials | 2026-08-24 | [S3] | researched, absent |

## 3. Plugin interface (PRI-2925)

- mcp_support: **client** — `/mcp` and `/mcp install` slash commands ("Install community MCP servers"); ACP adapter README lists "MCP Integration: Connect to HTTP/SSE MCP servers". No server mode found [S3][S5] (as-of 2026-08-24)
- plugin_support: **True** — three layers: (a) Agent Skills (modular instruction packages, `/skills` new/use/install/search/trending, auto-generation via `--auto-skill`, community registry skilled.autohand.ai); (b) Code Extensions — declarative manifest packages contributing tools, focused agents, skills; reviewed runtime extensions with `--trust` can register slash commands, Ink UI, hooks, providers, permission policy (`autohand extensions install/validate/list`); (c) MCP servers [S3]. Evidence: https://github.com/autohandai/code-cli/blob/main/docs/extensions.md
- claude_code_plugin: **partial** — skills are "Compatible with Codex and Claude skill formats" (README, Skills section); no Claude Code plugin/marketplace format support found [S3] (census says False — see section 6)
- subagents: **True** — `spawn_subagent` tool ("Delegate tasks to focused agents"), `/agents definitions`, `/squad` local multi-agent team runtime [S3]
- hooks: **True (with nuance)** — `/hooks` manages *git* hooks; runtime extensions can register hooks; README lists "skills, hooks, and provider configuration" as extensibility. Claude-Code-style lifecycle-hook config not specifically located [S3]
- plan_mode: **True** — plan mode in the Shift+Tab edit/plan/YOLO/auto cycle [S3]
- plugin_docs_url: https://github.com/autohandai/code-cli/blob/main/docs/extensions.md (skills: docs/agent-skills.md; authoring: docs/extension-authoring.md)
- config_docs_url: https://github.com/autohandai/code-cli/blob/main/docs/config-reference.md (18 language translations)
- ACP support: **yes, two routes** — (a) native: `autohand --acp` / `--mode acp` runs "Agent Client Protocol over stdio"; docs/guides/ACP.md covers Zed, JetBrains IDEs, JetBrains Air; (b) legacy npm adapter `@autohandai/autohand-acp` (the package named in the Paseo catalog) — a separate small TypeScript shim whose only dependency is `@agentclientprotocol/sdk`, which requires the `autohand` CLI installed and spawns it (`AUTOHAND_CMD`, default `autohand`); single version 0.2.1 published 2026-01-29, adapter repo unpushed since 2026-01-17 [S3][S5][S6] (as-of 2026-08-24)
- SDK: **yes** — "Code Agent SDK", explicitly a "CLI wrapper implementation" (`@autohandai/agent-sdk`, npm desc), beta packages for TypeScript, Go, Python, Java, Swift [S3][S6]

## 4. Claimed differentiation (raw material for PRI-2927)

- tagline: repo description (verbatim): "Autohand Code CLI - Ultra fast self evolving coding agent that runs in your terminal" [S2]; site title: "Your Codebase, Understood at Scale" [S10]; README bold lede: "A fast, self-improving terminal-native AI coding agent for planning, reflecting, remembering, editing, testing, and automating work across your codebase." [S3]
- maker claims (paraphrased, from README "Why Autohand Code CLI?" and features) [S3]:
  1. Self-improving: auto-generates project-specific skills from codebase analysis (`--auto-skill`, `/learn` skill advisor)
  2. Speed: "Ultra fast", Bun + Ink, optimized responsive sessions
  3. Extensibility stack: skills + declarative Code Extensions + MCP + community registries (skilled.autohand.ai, trending/search)
  4. Multi-agent: `/squad` team runtime, `spawn_subagent`
  5. iOS app pairing for remote control/steering of sessions (`/go --steer`)
  6. Multi-provider, incl. local models; no lock-in
  7. Safe execution: approval before risky ops, permission modes, dry-run
  8. Polyglot SDK (5 languages) + JSON-lines streaming output for CI/automation
- audience: developers in the terminal, plus CI/CD automation; docs in 18 languages suggest international ambition [S3]. No team-size claims (researched, absent).

## 5. Company & contact targets (PRI-2929)

- Company: Autohand AI (LLC per COMMERCIAL.md), New Zealand (GitHub org location); org email hey@autohand.ai; org created 2023-07-09, 32 public repos [S1][S9]
- Publicly named leadership: **Igor Costa — "Founder and CEO @autohandai"** (his own public GitHub bio; company field "Autohand AI") [S11] (as-of 2026-08-24). No other named staff found; commit history is consistent with a single-person company.
- Funding: none found (researched, absent)

## 6. Open questions / conflicts

- Census `claude_code_plugin: False` — README states skills are "Compatible with Codex and Claude skill formats"; "partial" is more accurate (skills format yes, plugin/marketplace format no) [S3].
- Census `plugin_docs_url: null` / `config_docs_url: null` — both exist (docs/extensions.md, docs/config-reference.md); filled in section 3.
- Census `current_release: "2026-08-19"` — v0.9.7-alpha.d24c4e6 published 2026-08-21 [S4].
- Census `platforms` includes "Web" — no web form factor found in README (CLI, VS Code, ACP editors, iOS pairing, CI). "Web" unverified; iOS companion is the closest thing.
- Census `model_providers` lists "Autohand AI" and "Ollama, llama.cpp, MLX" — README's current provider list is OpenRouter, LLMGateway, OpenAI, AWS Bedrock, DeepSeek, Azure Foundry Models, Z.ai, "local models"; an Autohand-hosted provider and the specific local backends were not verified from reachable materials (site 403s).
- License tension: GitHub/README say Apache-2.0, but COMMERCIAL.md imposes an ARR-gated commercial requirement Apache-2.0 itself does not permit restricting; treat as dual/source-available-with-conditions rather than plain Apache-2.0 [S9].
- Installer clobbers any pre-existing `agent` binary on PATH from other vendors, silently, per the README's own description — factual, maker-documented, and unusual; relevant to any trust assessment [S3].
- The Paseo-cataloged npm ACP adapter (0.2.1, Jan 2026, repo dormant) predates the CLI's native `--acp` mode; which one Paseo currently invokes determines whether its integration path is live or stale.
- autohand.ai (product + pricing pages) unreachable: HTTP 403 to WebFetch and JS-rendered shell via curl; only the page title recovered. Pricing/company pages unverified first-hand [S10].
- ~26k npm downloads/month vs 178 stars and 1-point HN: downloads may include CI noise; star/HN/marketplace signals point to a small real user base.

## 7. Sources

1. [S1] https://api.github.com/orgs/autohandai — org identity, NZ, email, created 2023
2. [S2] https://api.github.com/repos/autohandai/code-cli — stars, forks, dates, license, language, description, homepage
3. [S3] https://raw.githubusercontent.com/autohandai/code-cli/main/README.md — features, install, skills/extensions/MCP/ACP/squad, license section, installer `agent`-replacement note
4. [S4] https://api.github.com/repos/autohandai/code-cli/releases + /contributors — releases, asset downloads, contributor split
5. [S5] https://raw.githubusercontent.com/autohandai/autohand-acp/main/README.md + https://api.github.com/repos/autohandai/autohand-acp — adapter mechanics, requirements, repo staleness
6. [S6] https://registry.npmjs.org/@autohandai/autohand-acp, /autohand-cli search, /@autohandai/agent-sdk + api.npmjs.org download points — package metadata and downloads
7. [S7] https://hn.algolia.com/api/v1/search?query=Autohand — HN signal (absent)
8. [S8] VS Code Marketplace extensionquery API (AutohandAI.vscode-autohand) — installs/ratings
9. [S9] https://raw.githubusercontent.com/autohandai/code-cli/main/COMMERCIAL.md — ARR $5M commercial-license terms, "Autohand AI LLC"
10. [S10] https://www.autohand.ai/cli/ — 403 to WebFetch; curl with browser UA returned JS shell, title only
11. [S11] https://api.github.com/users/igorcosta — founder/CEO public bio

## Inclusion check (Jesse's test)

**Yes** — Autohand Code CLI is a genuine agent with its own agentic loop ("Combines reasoning, file edits, shell commands, and web context in one loop"; own tool set, skills, subagents, implemented in TypeScript/Bun) [S3]. The Paseo-cataloged npm package `@autohandai/autohand-acp` is itself a thin ACP shim (sole dep: the ACP SDK; spawns the locally installed `autohand` binary), but it wraps Autohand's *own* agent, not someone else's — and the CLI now ships native `--acp` anyway. Verdict applies to the product; the standalone adapter package alone would fail the test [S5][S3].
