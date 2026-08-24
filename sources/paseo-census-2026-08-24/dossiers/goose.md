# Dossier: goose (census_slug: goose)

Compiled 2026-08-21. Facts only. Null convention: "null = not researched"; "False/none = researched and absent". Each non-obvious fact carries a source [Sn] (see section 7) and an as-of date.

## 1. Identity

- name: goose (styled lowercase; launched as "codename goose") [S1][S12]
- maker: originated at Block, Inc. (company; NYSE: XYZ; principal office Oakland, CA, USA; no designated HQ since 2021) [S12][S27]. Since 2025-12-09 the project is donated to / stewarded by the Agentic AI Foundation (AAIF), a Linux Foundation directed fund; GOVERNANCE.md: "Founded by Block, stewarded by AAIF", legal home LF Projects, LLC [S13][S14][S15] (as-of 2026-08-21). Org form: company-originated, now foundation-governed open-source project.
- product URL: https://goose-docs.ai/ (current). https://block.github.io/goose/ still returns 200 for the root but deep links under it 404; the docs-move post says old links redirect [S15][S28] (as-of 2026-08-21).
- repo URL: https://github.com/aaif-goose/goose (github.com/block/goose returns HTTP 301 to it) [S4][S28] (as-of 2026-08-21)
- license: Apache-2.0 (GitHub API license key apache-2.0; README badge; Homebrew formula) [S4][S1][S7]. Note: goose-docs.ai/llms.txt still says "MIT licensed" in one bullet — stale/inconsistent [S3].
- open source? True. source_available: True — full Rust source (crates), desktop Electron app, docs, and the ACP TUI are in the one repo [S4][S1].
- first public release: repo created 2024-08-23; first GitHub release v0.9.0 2024-09-10 (Python-era goose); public launch of the Rust rewrite "codename goose" v1.0.0 on 2025-01-28 with desktop app + CLI [S4][S5][S12] (as-of 2026-08-21). Block's Q1-2026 shareholder letter says development began "in early 2024" [S24].
- latest release: v1.47.0, published 2026-08-21T18:14Z (GitHub Releases); 147 releases total (12 in 2024, 86 in 2025, 49 so far in 2026); 12 releases since 2026-05-23 [S5] (as-of 2026-08-21). Homebrew cask/formula already at 1.47.0 [S7].
- what it is:
  - Form factors: native desktop app (macOS, Linux, Windows; Electron), CLI (`goose`), HTTP/ACP server mode (`goose serve`, "remote goose server" driven from Desktop), ACP agent mode (`goose acp`) for editors such as Zed, and an early-stage npm TUI (`@aaif/goose`, 0.20.1) that launches the ACP server [S1][S2][S9][S10][S20][S11] (as-of 2026-08-21). README: "desktop app, CLI, and API".
  - Models: BYO / multi-provider — README says "15+ providers"; the providers page lists ~40 API providers (Anthropic, OpenAI, Google Gemini, Bedrock, Azure OpenAI/AI Foundry, Vertex, Databricks, Groq, Mistral, OpenRouter, xAI, Cerebras, Snowflake, etc.), local/no-key options (Ollama, LM Studio, Docker Model Runner), subscription logins (ChatGPT device flow, GitHub Copilot device flow), a "CLI provider" (cursor-agent) and "ACP providers" that drive Claude Code, Codex, Amp or Pi as the model backend [S1][S8][S18] (as-of 2026-08-21). Quickstart recommends Tetrate Agent Router with GPT-5 and $10 free credits [S21]. Multi-model: separate planner model (`GOOSE_PLANNER_PROVIDER/MODEL`), lead/worker and per-turn switching [S19][S17].
  - Pricing: free, Apache-2.0; user pays their own model-provider costs (BYO key or existing subscriptions via ACP providers) [S1][S8][S18]. No paid tier found (researched, absent).
  - Install: CLI `curl -fsSL https://github.com/aaif-goose/goose/releases/download/stable/download_cli.sh | bash` (macOS/Linux/Git-Bash), PowerShell script on Windows, `brew install block-goose-cli`; Desktop: `brew install --cask block-goose`, DMG/ZIP/DEB/RPM/Flatpak from GitHub Releases; `goose update` for CLI updates; `GOOSE_VERSION` pin [S9] (as-of 2026-08-21). Homebrew names still carry the "block-" prefix [S7].
  - Default autonomy: four modes — "Completely Autonomous" (default: edits, deletes, shell, extensions without approval), Manual Approval, Smart Approval (risk-based), Chat Only; switchable with `/mode auto|smart_approve|approve|chat`; per-tool overrides Always Allow / Ask Before / Never Allow [S16][S22] (as-of 2026-08-21).
  - Repo language per GitHub API: Rust [S4].

## 2. Adoption evidence

| metric / claim | value | as-of | source | type |
|---|---|---|---|---|
| GitHub stars | 53,184 (REST) / 53,200 (GraphQL, later same day) | 2026-08-21 | [S4][S29] | independently observable |
| GitHub forks | 6,064 / 6,066 | 2026-08-21 | [S4][S29] | independently observable |
| GitHub watchers (subscribers) | 294 | 2026-08-21 | [S4] | independently observable |
| GitHub open issues+PRs (open_issues_count) | 238 | 2026-08-21 | [S4] | independently observable |
| GitHub issues ever (search API) / PRs ever | 2,816 / 8,315 | 2026-08-21 | [S4] | independently observable |
| GitHub contributors (incl. anonymous) | 615 | 2026-08-21 | [S4] | independently observable |
| Commits, last 90 days (since 2026-05-23) | 870 | 2026-08-21 | [S4] | independently observable |
| Releases | 147 total; 12 since 2026-05-23 (~weekly); v1.47.0 on 2026-08-21 | 2026-08-21 | [S5] | independently observable |
| GitHub release-asset downloads, all releases summed | 1,532,005 (largest: v1.12.0 454,672; "canary" 70,541; v1.45.0 59,813; v1.43.0 50,781) | 2026-08-21 | [S5] | independently observable (counts only direct GitHub asset downloads; brew/script installs that pull from releases are included, package-manager installs elsewhere are not) |
| GitHub Discussions | enabled; 275 discussions total | 2026-08-21 | [S29] | independently observable |
| Homebrew cask `block-goose` installs, 30d / 90d / 365d | 1,116 / 2,851 / 11,025 (rank #297 of casks, 0.05% at 30d) | 2026-08-21 | [S7] | independently observable |
| Homebrew formula `block-goose-cli` installs, 30d / 90d / 365d | 2,197 / 6,781 / 32,426 (rank #885 at 30d) | 2026-08-21 | [S7] | independently observable |
| npm `@aaif/goose` (ACP TUI, early-stage) weekly / monthly downloads | 174 (2026-08-14..20) / 4,474 (2026-07-22..08-20); 10 versions, first published 2026-03-31 | 2026-08-20 | [S11] | independently observable |
| Discord "goose" server | 6,243 members, 626 online | 2026-08-21 | [S6] | independently observable |
| Homepage counters | "45,000+ GitHub stars", "500+ contributors", "70+ MCP extensions" | 2026-08-21 (page text) | [S2] | maker-claimed (stale vs 53k observable) |
| Docs extension directory pages | 65 `/docs/mcp/*` pages in sitemap; README says "70+ extensions" | 2026-08-21 | [S3][S1] | independently observable / maker-claimed |
| Linux Foundation Insights health badge | "Excellent" | 2026-08-21 | [S1] | third-party (LF) |
| Early traction | "approaching 10,000 GitHub stars" ~6 weeks after launch; top-trending on GitHub for weeks | 2025-03-17 | [S25] | press (Forbes) |
| Block internal: origin | "began developing goose" in early 2024; "first agentic harness to enable foundation models to execute work across an enterprise" | 2026-05-07 | [S24] | maker-claimed (Block Q1-2026 shareholder letter) |
| Block internal: productivity | production code changes per engineer up >2.5x vs January (mid-April 2026); Builderbot + other AI tools reviewed >90% of production code change requests (first two weeks of April 2026); Builderbot >200,000 ops/day and 15% of production code changes "nearly fully autonomously"; 100% of Block employees use AI tools (early April 2026) | 2026-05-07 | [S24] | maker-claimed (Block; Builderbot is a Block internal system built on goose per Q2 letter) |
| Block internal: Q2 2026 | "built goose in early 2024 to work with any model"; led to Builderbot for orchestration across Block's codebase; in June 2026 "agentic AI helped write and review nearly all" production code changes | 2026-08-05 | [S26] | maker-claimed (Block Q2-2026 shareholder letter) |
| Block internal: code changes per engineer | +150% year-to-date (Q2 2026 earnings call, per press) | 2026-08-06 | [S30] | press report of maker statement |
| Block workforce | cut ~40% (>10,000 to <6,000) on 2026-02-26; Dorsey letter cites "the tools we're building"; press links it to goose | 2026-02-26 | [S31][S32] | press / maker letter (goose not named in quoted letter text) |
| Public customers / case studies | none on homepage (no logos) [S2]. Block-internal use cases in goose blog: detection engineering with Panther MCP, "MCP in the Enterprise: Real World Adoption at Block" [S23]. Forbes 2025: Block sales analysis, content, onboarding [S25]. AAIF members (not goose customers): AWS, Anthropic, Bloomberg, Cloudflare, Google, Microsoft, OpenAI + Gold/Silver tiers [S14] | 2026-08-21 | [S2][S23][S25][S14] | maker-claimed / press |
| Funding / valuation | n/a — not a company; Block, Inc. public (XYZ), revenue US$24.2B (2025) [S27]; goose donated to AAIF 2025-12-09 [S14] | 2026-08-21 | [S27][S14] | public filings / press release |
| Benchmarks | goose is one of the harness options in Terminal-Bench's agent set (alongside Claude Code, Codex CLI, Terminus) per Epoch AI; no specific goose placement located on tbench.ai 2.0/2.1 or SWE-bench in this pass | 2026-08-21 | [S33] | third-party (placement: null = not located) |
| Third-party adapters | Zed registry entry for goose ACP agent (docs) [S10]; goose listed in ACP ecosystem | 2026-08-21 | [S10] | independently observable |
| Press | Fortune (2025-01-28 launch), Forbes (2025-03-17), SiliconANGLE/diginomica (AAIF, 2025-12), SF Standard / Fortune (2026-02 layoffs), Cointelegraph (Q2 2026) | 2026-08-21 | [S34][S25][S35][S31][S30] | press |
| Ranking among tracked harnesses (Trendshift badge id 25298) | badge present; rank not read | 2026-08-21 | [S1] | null |

## 3. Plugin interface (PRI-2925)

- mcp_support: **both (client primary)** — goose is an MCP client: extensions are MCP servers over stdio (npx/uvx/jbang/docker/goosed), Streamable HTTP, or raw YAML config; MCP Apps/MCP-UI, elicitation, roots, sampling documented; extension directory at goose-docs.ai/extensions and `goose://extension` deep links [S36][S3]. Server side: goose's built-in extensions (developer, memory, computer-controller, etc.) "are MCP servers in their own right" and can be run by other agents (`goosed mcp <name>`) [S36]. Evidence: https://goose-docs.ai/docs/getting-started/using-extensions (as-of 2026-08-21)
- plugin_support: **True** — (a) Extensions = MCP servers (built-in, platform, and 3rd-party; directory at /extensions) [S36]; (b) Plugins = a directory with `plugin.json` (at root, `.plugin/`, or `.goose-plugin/`) bundling `skills/` (SKILL.md) and `hooks/hooks.json`; installed with `goose plugin install <git-url>` (optional `--auto-update`), stored in `~/.agents/plugins/` or `<project>/.agents/plugins/`; docs say it supports "Open Plugins" and Gemini extensions; no marketplace/registry for plugins [S37]; (c) Skills (SKILL.md, agentskills-compatible) from `~/.agents/skills/`, `.agents/skills/`, plugins, with legacy `.goose/skills/`, `.claude/skills/`, `~/.claude/skills/` [S38]; (d) Recipes (YAML/JSON task templates with params, extensions, subrecipes, response schema; deep links; cookbook at /recipes) [S39]; (e) custom agents as Markdown+frontmatter in `~/.agents/agents/`, `.agents/agents/`, legacy `.claude/agents/` [S40]; (f) custom distributions (CUSTOM_DISTROS.md) [S1] (as-of 2026-08-21).
- claude_code_plugin: **partial** — reads Claude-Code-style skills from `.claude/skills/` and `~/.claude/skills/` (documented as backward-compat), custom agents from `.claude/agents/`, and `CLAUDE.md` only if added via `CONTEXT_FILE_NAMES` env var (defaults are `AGENTS.md` then `.goosehints`); hooks.json schema mirrors Claude Code's event/matcher/command shape; plugin manifest is `plugin.json` at root/`.plugin/`/`.goose-plugin/` — the `.claude-plugin/` directory and Claude Code marketplaces are not mentioned in goose docs (researched, absent) [S37][S38][S40][S41] (as-of 2026-08-21).
- subagents: **True** — the `summon` platform extension provides `delegate` and `load` tools; the agent decides to delegate or is asked; sequential by default, parallel on request; isolated sessions; `GOOSE_SUBAGENT_MAX_TURNS` (default 25), 5-minute default timeout; Desktop and CLI; subrecipes can also run in parallel instances; "Goosetown" parallel-agent pattern on the blog [S42][S39][S23]. Evidence: https://goose-docs.ai/docs/guides/context-engineering/subagents (as-of 2026-08-21)
- hooks: **True** — 12 events: SessionStart, SessionEnd, Stop, UserPromptSubmit, PreToolUse, PreToolUseResult, PostToolUse, PostToolUseFailure, BeforeReadFile, AfterFileEdit, BeforeShellExecution, AfterShellExecution; only handler type `command` (sh -c); PreToolUse can block (exit 2 or `{"decision":"block"}`), Stop can block; others observe-only; configured in a plugin's `hooks/hooks.json`; SubagentStart/Stop "not currently emitted" (docs dated May 2026) [S43]. Evidence: https://goose-docs.ai/docs/guides/context-engineering/hooks (as-of 2026-08-21)
- plan_mode: **True (partial)** — CLI `/plan` enters a planning mode that asks clarifying questions and produces a plan; `/endplan` exits; optional separate planner model via `GOOSE_PLANNER_PROVIDER`/`GOOSE_PLANNER_MODEL`; plan prompt template `plan.md` editable; Desktop has no toggle (prompt "create a plan"); docs do not describe it as a read-only/no-edit permission mode — the read-only equivalent is "Chat Only" mode [S44][S16]. Evidence: https://goose-docs.ai/docs/guides/context-engineering/creating-plans (as-of 2026-08-21)
- plugin_docs_url: https://goose-docs.ai/docs/guides/context-engineering/plugins (extensions: https://goose-docs.ai/docs/getting-started/using-extensions ; skills: https://goose-docs.ai/docs/guides/context-engineering/using-skills ; recipes: https://goose-docs.ai/docs/guides/recipes/)
- config_docs_url: https://goose-docs.ai/docs/guides/config-files (permissions: https://goose-docs.ai/docs/guides/managing-tools/goose-permissions ; env vars: https://goose-docs.ai/docs/guides/environment-variables)
- ACP support: **yes, both directions** — as ACP agent/server: `goose acp` (stdio JSON-RPC) for Zed and other ACP clients; auto-loads the client's `context_servers` MCP config [S10]; as ACP client/consumer: "ACP providers" (claude-acp, codex-acp, amp-acp, pi-acp) let goose use another agent as its model backend, passing goose extensions through as MCP servers [S18]; `goose serve` exposes an authenticated HTTP `/acp` endpoint for remote Desktop use [S20]; repo topics include `acp` [S4] (as-of 2026-08-21).
- SDK: **partial** — README advertises "an API to embed it anywhere"; `goose serve`/goosed HTTP+ACP server and `goose acp` are the integration surfaces; no official language SDK documented on the remote-server page (researched, absent) [S1][S20]. Recipes/`goose run` provide headless automation [S39].

## 4. Claimed differentiation (raw material for PRI-2927)

- tagline (README/homepage, verbatim-short): "your native open source AI agent — desktop app, CLI, and API — for code, workflows, and everything in between" — https://github.com/aaif-goose/goose ; https://goose-docs.ai/ [S1][S2]
- GitHub description: "an open source, extensible AI agent that goes beyond code suggestions - install, execute, edit, and test with any LLM" [S4]
- quickstart one-liner: extensible open source AI agent that automates coding tasks [S21]
- maker claims (paraphrased):
  1. General-purpose, not only code — research, writing, automation, data analysis [S1][S2].
  2. Runs on your machine ("local-first"), native desktop app for macOS/Linux/Windows plus full CLI plus API; built in Rust for performance/portability [S1][S2][S3].
  3. Model choice: 15+ providers (docs list ~40), API keys or existing Claude/ChatGPT/Gemini subscriptions via ACP/CLI providers; "not bound to specific models" is a governance value [S1][S8][S13].
  4. Extensible via the MCP open standard: "70+ extensions", MCP Apps with interactive UIs [S1][S2].
  5. Recipes — portable YAML workflows shareable across a team, with deep links and subrecipes [S2][S39].
  6. Subagents for parallel task handling [S2][S42].
  7. Security features: prompt-injection detection, "sandbox mode", adversary mode (independent reviewer agent), extension allowlists, per-tool permissions [S2][S45][S22].
  8. Open governance: Apache-2.0, part of AAIF at the Linux Foundation, "plan and build in the open" [S1][S13][S15]; launch framing: open, modular, interoperable via MCP, choice of LLM provider [S12].
- audience: developers first (launch: "first use cases ... software engineering", Block engineers and the open source community [S12]); homepage/README broaden to anyone needing research, writing, automation, data analysis [S1][S2]; enterprise angles via allowlists, custom distributions, remote server [S1][S20].

## 5. Company & contact targets (PRI-2929) — company-level only

- legal name: Block, Inc. (formerly Square, Inc.); NYSE: XYZ (ticker changed from SQ Jan 2025) [S27]
- HQ: Oakland, California (principal office; company states no designated HQ since 2021) [S27]
- size: ~6,000 employees after the 2026-02-26 reduction (from >10,000; 11,372 at end-2024) [S27][S31]; revenue US$24.2B (2025) [S27]
- funding stage: public company [S27]
- project home: Agentic AI Foundation (AAIF), Linux Foundation; Block is a Platinum member; goose governance: 7 core maintainers + 5 maintainers (MAINTAINERS.md lists GitHub handles without affiliations); tie-breaker named in GOVERNANCE.md is Bradley Axen [S13][S14][S46]
- publicly named leadership (only as named by Block / goose's own materials):
  - Jack Dorsey — "Block Head and Chairperson" (Block; Wikipedia summarising company filings) [S27]
  - Dhanji Prasanna — CTO, Block (quoted in Block's launch post) [S12]
  - Manik Surtani — Head of Open Source, Block (quoted in LF/AAIF press release; Fortune calls him Open Source Lead) [S14][S34]
  - Bradley Axen — named in goose GOVERNANCE.md as tie-breaking core maintainer (Forbes: Tech Lead for AI and Data Platform) [S13][S25]
  - Michael Neale — Principal Engineer (goose blog byline, AAIF-move post) [S15][S23]
  - Angie Jones — Head of Developer Relations (goose-docs.ai authors page; 17 posts) [S23]
  - DevRel team named on goose blog authors page: Rizel Scarlett, Adewale Abati, Amanda Martin, Debbie O'Brien, W Ian Douglas (Staff Developer Advocates); Ebony Louis (Developer Advocate); Tania Chakraborty (Senior Technical Community Manager) [S23]
  - Head of partnerships/ecosystem: none found named in goose/Block materials for goose specifically (researched, absent). AAIF is the neutral ecosystem body [S14].
- contact: community via Discord https://discord.gg/n8R5VaWDAn, GitHub Discussions; AAIF https://aaif.io/ [S1][S14]

## 6. Open questions / conflicts

- Existing census `maker: "aaif-goose"` — that is the GitHub org, not the maker. Maker is Block, Inc. (originator) with governance now at AAIF/Linux Foundation; roster says Block [S12][S14][S13].
- Existing census `url`/`source_code_url`: github.com/aaif-goose/goose — correct; block/goose 301-redirects [S28]. Roster `primary_url` https://block.github.io/goose/ is stale: root still serves but deep links 404; canonical is https://goose-docs.ai/ [S28][S15].
- Existing census `first_released: "2024-08-23"` — that is repo creation; first release v0.9.0 2024-09-10; public launch (v1.0.0) 2025-01-28 [S4][S5][S12].
- Existing census `current_release: "2026-08-20"` — v1.47.0 was published 2026-08-21T18:14Z [S5].
- Existing census `stars: null` — 53,184 on 2026-08-21 [S4]. Homepage's own "45,000+" is stale [S2].
- Existing census `platforms: ["CLI","Desktop"]` — also server/API (`goose serve`), ACP agent mode (Zed etc.), npm TUI [S20][S10][S11].
- Existing census `claude_code_plugin/subagents/hooks/plan_mode: null` — filled above: partial / True / True / True(partial).
- Existing census `plugin_docs_url`/`config_docs_url`/`download_url: null` — filled above; download_url = https://goose-docs.ai/docs/getting-started/installation or https://github.com/aaif-goose/goose/releases.
- Existing census `model_providers: "... and 15+ more"` — README says 15+ providers total; docs list ~40 API providers + local + CLI/ACP providers [S1][S8].
- Existing census `install_method` — fine; add `brew install block-goose-cli` / `--cask block-goose` [S9].
- Existing census `license: Apache-2.0` correct; but goose-docs.ai/llms.txt says "MIT licensed" — docs inconsistency [S3].
- Existing census `mcp_support: True` — more precisely client (primary) + built-in extensions usable as MCP servers [S36].
- Existing census `plugin_support: True` — yes, but note goose has four distinct mechanisms (MCP extensions, plugins, skills, recipes) [S36][S37][S38][S39].
- "Open Plugins" in goose docs vs AAIF "Agent Plugins 1.0" (2026-08-06) — the AAIF spec post does not list goose among adopters (VS Code, Cursor, Copilot, Codex, Kiro); whether goose's plugin.json is the same spec is unverified [S37][S47].
- Homepage says "sandbox mode" but the security guide index documents prompt-injection detection, adversary mode, allowlist — a sandbox/container page (containerization / container-use MCP) was not verified in this pass [S2][S45].
- Block's 2026 internal metrics are about Block's AI program broadly (goose + Builderbot + "other AI tools"); only the Q2 letter explicitly chains goose -> Builderbot -> "nearly all" code changes [S24][S26]. Press claims such as "8-10 hours saved per engineer per week" and "40% more code per person" were not located in a Block primary source in this pass (Forbes 403'd) [S31][S32].
- Benchmark placements for goose (Terminal-Bench, SWE-bench) not located — null, not "absent".
- Maintainer company affiliations not published (MAINTAINERS.md has handles only) [S46].
- Block Q1/Q2 letters were read from PDFs; SEC 8-K HTML returned 403 to the fetcher [S24][S26][S48].
- Forbes 2026-04-01 returned 403; its claims are represented only via search snippets [S32].

## 7. Sources

1. [S1] https://raw.githubusercontent.com/aaif-goose/goose/main/README.md (raw/goose_readme.md) — tagline, claims, install, Discord, AAIF, badges
2. [S2] https://goose-docs.ai/ — homepage tagline, counters (45k+ stars, 500+ contributors, 70+ extensions), features
3. [S3] https://goose-docs.ai/llms.txt and https://goose-docs.ai/sitemap.xml (raw/goose_llms.txt, goose_sitemap.txt) — docs index, MIT wording, 65 MCP pages
4. [S4] https://api.github.com/repos/aaif-goose/goose (+ contributors, commits?since=2026-05-23, search/issues) — stars/forks/dates/contributors/commits
5. [S5] https://api.github.com/repos/aaif-goose/goose/releases (raw/goose_gh_releases*.json) — release dates, asset download counts, v1.47.0 notes
6. [S6] https://discord.com/api/v9/invites/n8R5VaWDAn?with_counts=true — Discord member count
7. [S7] https://formulae.brew.sh/api/cask/block-goose.json, /api/formula/block-goose-cli.json, /api/analytics/cask-install/{30d,90d,365d}.json, /api/analytics/install/{30d,90d,365d}.json — Homebrew versions and installs
8. [S8] https://goose-docs.ai/docs/getting-started/providers — provider list, free tiers, subscriptions
9. [S9] https://goose-docs.ai/docs/getting-started/installation — install methods
10. [S10] https://goose-docs.ai/docs/guides/acp-clients — `goose acp`, Zed
11. [S11] https://registry.npmjs.org/@aaif/goose and https://api.npmjs.org/downloads/point/last-week|last-month/@aaif/goose — npm TUI package, downloads
12. [S12] https://block.xyz/inside/block-open-source-introduces-codename-goose — 2025-01-28 launch, CTO quote, Apache-2.0
13. [S13] https://raw.githubusercontent.com/aaif-goose/goose/main/GOVERNANCE.md — stewardship, roles, tie-breaker, values
14. [S14] https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation — 2025-12-09 AAIF, Block quote, members
15. [S15] https://goose-docs.ai/blog/2026/04/07/goose-moves-to-aaif/ — org/docs move, byline
16. [S16] https://goose-docs.ai/docs/guides/managing-tools/goose-permissions — modes, default autonomous
17. [S17] https://goose-docs.ai/docs/guides/multi-model/ — planner/executor, multi-model
18. [S18] https://goose-docs.ai/docs/guides/acp-providers — claude-acp, codex-acp, amp-acp, pi-acp
19. [S19] https://goose-docs.ai/docs/guides/context-engineering/creating-plans — (see S44)
20. [S20] https://goose-docs.ai/docs/guides/remote-goose-server — `goose serve`, /acp endpoint, no SDK
21. [S21] https://goose-docs.ai/docs/quickstart — one-liner, Tetrate default, $10 credit
22. [S22] https://goose-docs.ai/docs/guides/managing-tools/tool-permissions — per-tool allow/ask/never
23. [S23] https://goose-docs.ai/blog/authors (raw/goose_blog_authors.html) — DevRel names/titles, blog posts on Block usage
24. [S24] https://s29.q4cdn.com/628966176/files/doc_financials/2026/q1/Block_Q1-2026-Shareholder-Letter.pdf (2026-05-07) — goose origin, 2.5x, Builderbot 90%/15%/200k ops, 100% employees
25. [S25] https://www.forbes.com/sites/torconstantino/2025/03/17/jack-dorseys-ai-assistant--goose-is-taking-off-in-open-source-circles/ — ~10k stars at 6 weeks, Block names/titles
26. [S26] https://s29.q4cdn.com/628966176/files/doc_financials/2026/q2/Q2-2026-Shareholder-Letter.pdf (2026-08-05) — "built goose in early 2024", Builderbot, nearly all code changes in June
27. [S27] https://en.wikipedia.org/wiki/Block,_Inc. — legal name, HQ, ticker, employees, revenue, Dorsey title
28. [S28] curl -I https://github.com/block/goose ; https://block.github.io/goose/ ; /docs/quickstart — redirects / 404
29. [S29] gh api graphql repository(aaif-goose/goose){discussions{totalCount} stargazerCount forkCount} — discussions 275
30. [S30] https://cointelegraph.com/markets/block-raises-2026-outlook-strong-quarter-says-ai-touches-nearly-all-code (2026-08-06) — +150% per engineer (call), June "nearly all"
31. [S31] https://sfstandard.com/2026/02/26/block-lays-off-staff/ — 40% cut, Dorsey letter quotes
32. [S32] https://www.forbes.com/sites/josipamajic/2026/04/01/... (403; via search snippets) and https://www.fortune.com/2026/02/27/jack-dorsey-block-40-percent-layoff-ai-intelligence-tools-smaller-team — layoffs/AI framing
33. [S33] https://epoch.ai/benchmarks/terminal-bench (via search) — goose as a Terminal-Bench harness option
34. [S34] https://fortune.com/2025/01/28/ai-deepseek-block-jack-dorsey-cash-app-open-source-goose-agent/ — launch coverage, OSPO of five engineers
35. [S35] https://siliconangle.com/2025/12/09/linux-foundation-announces-agentic-ai-foundation-joined-anthropic-openai-block/ ; https://diginomica.com/anthropic-openai-and-block-donate-ai-agent-projects-new-linux-foundation-body — AAIF press
36. [S36] https://goose-docs.ai/docs/getting-started/using-extensions — MCP transports, built-ins, directory, deep links, extensions as MCP servers
37. [S37] https://goose-docs.ai/docs/guides/context-engineering/plugins — plugin.json, skills+hooks, install, locations
38. [S38] https://goose-docs.ai/docs/guides/context-engineering/using-skills — SKILL.md, directories incl. .claude/skills
39. [S39] https://goose-docs.ai/docs/guides/recipes/ — recipe format, subrecipes, cookbook
40. [S40] https://goose-docs.ai/docs/guides/context-engineering/custom-agents — agents dirs incl. .claude/agents
41. [S41] https://goose-docs.ai/docs/guides/context-engineering/using-goosehints — AGENTS.md/.goosehints, CONTEXT_FILE_NAMES (CLAUDE.md)
42. [S42] https://goose-docs.ai/docs/guides/context-engineering/subagents — summon/delegate, limits
43. [S43] https://goose-docs.ai/docs/guides/context-engineering/hooks — 12 events, command handler, blocking
44. [S44] https://goose-docs.ai/docs/guides/context-engineering/creating-plans — /plan, /endplan, planner model
45. [S45] https://goose-docs.ai/docs/guides/security/ — prompt injection detection, adversary mode, allowlist
46. [S46] https://raw.githubusercontent.com/aaif-goose/goose/main/MAINTAINERS.md — 7 core + 5 maintainers, no affiliations
47. [S47] https://aaif.io/blog/from-skills-and-tools-to-portable-agent-plugins (2026-08-06) — Agent Plugins 1.0 adopters (goose not listed)
48. [S48] https://www.sec.gov/Archives/edgar/data/0001512673/000119312526335117/d91486dex991.htm — 403 to fetcher (unreachable)
49. https://goose-docs.ai/extensions/ — directory page (client-rendered; count not readable)
50. https://insights.linuxfoundation.org/api/badge/health-score?project=goose — "Excellent" badge

## Inclusion check (Jesse's test)

**Yes** — goose is a first-party agent with its own agentic loop (Rust core: reads/edits files, runs shell via the built-in developer extension, iterates; plans, subagents, recipes), not a wrapper; it can additionally wrap other agents as "ACP providers" but that is optional [S1][S36][S18][S42].
