# Dossier: Kimi Code CLI (census_slug: kimi-code-cli)

Compiled 2026-08-21 (data pulls 2026-08-21/22 UTC). Facts only. Null convention: "null = not researched"; "False/none = researched and absent". Sources [Sn] in section 7.

## 1. Identity

- name: Kimi Code CLI (product family "Kimi Code"; the CLI binary is `kimi`)
- maker: Moonshot AI (company; Beijing, China; founded 2023) [S15][S16]
- **Repo situation (the census's central question):** there are two repos.
  - **Current repo: https://github.com/MoonshotAI/kimi-code** — TypeScript monorepo, created 2026-05-22, MIT license, 6,996 stars, actively developed (pushed 2026-08-22; release 0.38.0 on 2026-08-20) [S1][S3]. This is what Paseo links, and it is correct.
  - **Legacy repo: https://github.com/MoonshotAI/kimi-cli** — Python, created 2025-10-15, Apache-2.0, 11,236 stars. Its README carries an IMPORTANT banner: "Kimi CLI is evolving into Kimi Code CLI" (linking MoonshotAI/kimi-code), same team, auto-migrates config/sessions, "will be gradually wound down; the docs and existing installations remain available" [S2]. Not archived (archived=false); last push 2026-08-03; last release 1.49.0 on 2026-07-16 [S1].
  - So: the product was **rewritten Python→TypeScript and moved repos in May 2026**, not abandoned. The docs migration page confirms: "major version upgrade — moving from Python/uv to Node.js"; `kimi migrate` carries over config, MCP servers, and sessions [S6].
- product URL: https://www.kimi.com/code/ (product page); docs https://moonshotai.github.io/kimi-code/en/ (repo homepage field points at https://www.kimi.com/code/docs/) [S1][S13]
- license: MIT (kimi-code) [S1][S3]; legacy kimi-cli is Apache-2.0 [S1]
- open source? True — full source of the CLI, ACP adapter, agent core, VS Code extension app, and local server is in the monorepo (source_available: True; MIT) [S3][S4]
- first public release: legacy Kimi CLI — repo created 2025-10-15; first PyPI upload (kimi-cli 0.35) 2025-10-22 [S1][S7]. New Kimi Code CLI — repo created 2026-05-22; first changelog release 0.2.0 on 2026-05-26; npm package @moonshot-ai/kimi-code created 2026-05-22 [S1][S5][S9]. Press covered the new CLI 2026-06-06 [S14].
- latest release: **0.38.0, 2026-08-20** (GitHub release `@moonshot-ai/kimi-code@0.38.0`; npm dist-tag latest 0.38.0; 68 GitHub releases / 69 npm versions since May 2026) [S1][S5][S9]
- what it is:
  - Form factors: terminal TUI (primary); `kimi web` local server exposing a browser web UI plus experimental REST API (`/api/v1`) and WebSocket stream [S12]; VS Code extension ("Kimi Code", publisher moonshot-ai) [S10]; IDE integration via first-party ACP (`kimi acp`) for Zed, JetBrains — and the docs explicitly document Paseo setup [S11].
  - Models: works out of the box with Moonshot's Kimi models via Kimi Code OAuth subscription or Moonshot platform API key; **BYO models supported** via provider types `anthropic`, `openai`, `openai_responses`, `google-genai`, `vertexai`, plus a models.dev catalog importer for third-party vendors (DeepSeek, Qwen, etc.); Bedrock/Cohere proprietary protocols refused [S8].
  - Pricing: free to install (MIT); usage via Kimi Code subscription tiers or pay-as-you-go platform API key (see section 2 pricing row); other providers billed by their own vendors [S4][S8][S17].
  - Install: `curl -fsSL https://code.kimi.com/kimi-code/install.sh | bash` (macOS/Linux; no Node required, checksum-verified binary) / PowerShell script on Windows (requires Git Bash) / `npm install -g @moonshot-ai/kimi-code` (Node >= 22.19.0) [S4][S5].
  - Default autonomy: read-only operations run without confirmation; file modifications and shell commands ask for approval; "Approve for this session" and permanent `[[permission.rules]]` in config.toml; Plan mode (Shift-Tab), YOLO mode (`/yolo`, auto-approves regular calls but still asks for sensitive files/plan exits), Auto mode (`/auto`, fully unattended) [S5][S18].
  - Language/runtime: TypeScript on Node.js; repo language TypeScript [S1][S5]. Legacy repo is Python [S1].

## 2. Adoption evidence

| metric / claim | value | as-of | source | type |
|---|---|---|---|---|
| GitHub stars, MoonshotAI/kimi-cli (legacy) | 11,236 (forks 1,296; subscribers 58; open issues 834) | 2026-08-21 | [S1] | independently observable |
| GitHub stars, MoonshotAI/kimi-code (current) | 6,996 (forks 1,111; subscribers 30; open issues 1,167) | 2026-08-21 | [S1] | independently observable |
| Commit cadence, kimi-code | 1,265 commits since 2026-05-23 (repo's entire ~13-week life); pushed 2026-08-22 | 2026-08-22 | [S1] | independently observable |
| Commit cadence, kimi-cli | 24 commits since 2026-05-23; last commit 2026-08-03 | 2026-08-21 | [S1] | independently observable |
| Contributors (incl. anonymous) | kimi-code 51; kimi-cli 71 | 2026-08-21 | [S1] | independently observable |
| Releases | kimi-code 68 GitHub releases since 2026-05-26 (multiple per week); kimi-cli 102 releases, last 1.49.0 2026-07-16 | 2026-08-21 | [S1][S9] | independently observable |
| npm weekly downloads, @moonshot-ai/kimi-code | 33,868 (2026-08-14..20) | 2026-08-20 | [S5] | independently observable |
| npm monthly downloads, @moonshot-ai/kimi-code | 132,153 (2026-07-22..08-20) | 2026-08-20 | [S5] | independently observable |
| PyPI downloads, kimi-cli (legacy) | 166,551 last month; 32,363 last week — legacy installs still substantial | 2026-08-21 | [S7] | independently observable |
| PyPI downloads, kimi-code (stub package, same 1.49.0 lineage) | 1,625 last month | 2026-08-21 | [S7] | independently observable |
| Homebrew installs | kimi-code formula: 2,884 (30d), 5,544 (90d = all-time, new formula); kimi-cli: 137 (30d), 8,718 (365d) | 2026-08-21 | [S19] | independently observable |
| VS Code Marketplace, moonshot-ai.kimi-code ("Kimi Code") | 536,510 installs; released 2026-01-23; last updated 2026-08-14; 23 ratings avg 3.39 | 2026-08-21 | [S10] | independently observable |
| Unrelated npm name collision | npm package `kimi-code` (4,064 weekly) is a third-party whitesmith proxy wrapper for claude-code, NOT Moonshot's | 2026-08-20 | [S5] | independently observable |
| Kimi K3 model launch (powers Kimi Code) | announced 2026-07-16; 2.8T-param MoE, 1M context; open weights 2026-07-27 | 2026-07-16/27 | [S20][S21] | maker-claimed (specs) / press |
| K3 benchmark claims | 81.2 FrontierSWE, 88.3 Terminal-Bench 2.0 (model, not harness); #1 in an arena blind frontend-coding ranking at launch | 2026-07 | [S20] | maker-claimed / third-party leaderboard |
| Demand signal | Moonshot paused new K3 subscription sign-ups 2026-07-20, ~48h after launch, citing GPU capacity | 2026-07-20 | [S20] | press (maker statement) |
| Kimi K2.6 usage | #2 most-used model on OpenRouter (per TechCrunch, May 2026) | 2026-05-07 | [S16] | third-party (OpenRouter), via press |
| Company ARR | >$200M annual recurring revenue (April 2026; crossed $100M in March 2026) — company-wide (chatbot + API), not CLI-specific | 2026-04 | [S15][S16] | maker-claimed via press |
| Company funding | ~$2B raised at $20B valuation (May 2026, TechCrunch); reported pre-IPO talks targeting up to $50B pre-money + HK listing (Aug 2026, unconfirmed) | 2026-05-07 / 2026-08 | [S16][S22] | press / rumor |
| Pricing (Kimi Code plan) | third-party aggregators list tiers: Adagio free (K2.7-class), Andante ¥49/mo, Moderato ¥99 (unlocks K3), Allegretto ¥199, Allegro ¥699; USD: Moderato $19, Allegretto $39, Allegro $99, Vivace $199/mo (annual discounts). Official pricing page not machine-readable (see §6) | 2026-08 | [S17] | third-party-reported; official page unreachable |
| Internal use case study | Moonshot used Kimi Code CLI (K2.5) for a moonshot.ai visual refactor; published 2026-08-12; no adoption numbers | 2026-08-12 | [S23] | maker-claimed |
| Community | GitHub Discussions enabled on kimi-cli, not on kimi-code; no Discord/subreddit counts found | 2026-08-21 | [S1] | independently observable / null |

## 3. Plugin interface (PRI-2925)

- mcp_support: **client** — stdio, HTTP, legacy SSE transports; `mcp.json` at user (`~/.kimi-code/`) and project (`.kimi-code/`) level; interactive `/mcp-config` (AI-assisted, no hand-edited JSON) incl. OAuth (`/mcp-config login <server>`); tool allow/deny lists, timeouts, permission rules `mcp__<server>__<tool>` with wildcards; workspace-trust prompt for project-level servers; plugins can declare MCP servers. Not an MCP server itself (the `kimi web` REST/WS API is not MCP) [S24]. Evidence: https://moonshotai.github.io/kimi-code/en/customization/mcp
- plugin_support: **True** — full plugin system: manifest (`kimi.plugin.json`) bundling Agent Skills, custom agents, hooks, MCP servers, system-prompt instructions, and slash commands; `/plugins` manager with **Official** (Kimi-maintained marketplace), **Curated** (partner plugins), and **Custom** tabs; install from GitHub URL/tag/commit, zip, or local path; custom marketplace JSON via `KIMI_CODE_PLUGIN_MARKETPLACE_URL`; trust level surfaced per install; official plugins include Kimi Datasource (financial/government data feeds), Kimi WebBridge (browser extension), Kimi Computer Use [S25][S2-README]. Evidence: https://moonshotai.github.io/kimi-code/en/customization/plugins
- claude_code_plugin: **partial** — not the Claude Code plugin/marketplace format, but deliberately interoperable at the pieces level: skills use `SKILL.md`-with-frontmatter directories and are scanned from generic cross-tool dirs `~/.agents/skills/` and `.agents/skills/` (as well as `~/.kimi-code/skills/`); agent-file parsing explicitly "keeps Claude Code-style agent files loadable" (unknown fields like Claude Code's `model` ignored); a built-in **`/import-from-cc-codex`** command imports Claude Code and Codex instructions, Skills, and MCP settings; workspace instructions come from `AGENTS.md` (`/init` generates AGENTS.md; no CLAUDE.md support found in docs — the repo's own CLAUDE.md is for contributors) [S26][S27][S28]
- subagents: **True** — built-in `coder` / `explore` (read-only) / `plan` (no shell) sub-agents in isolated contexts; parallel + background execution with auto-return of results; custom agents as Markdown+frontmatter (`name`, `description`, `whenToUse`, `tools`, `disallowedTools`, `subagents` allowlist, `override`) discovered from project/user/extra/plugin scopes; delegation chains terminate by default (built-ins cannot re-delegate); `/secondary-model` picks a separate default model for subagents [S27]. Evidence: https://moonshotai.github.io/kimi-code/en/customization/agents
- hooks: **True** — `[[hooks]]` rules in config.toml (event, regex matcher, command, timeout); ~20 events incl. UserPromptSubmit, PreToolUse, PostToolUse(Failure), PermissionRequest/Result, SessionStart/End/Heartbeat, SubagentStart/Stop, TaskStarted, Stop, StopFailure, Interrupt, Pre/PostCompact, Notification; blockable events: PreToolUse, Stop, UserPromptSubmit (exit code 2 or JSON `permissionDecision: deny`); fail-open by design; plugins can ship hooks [S29]. Evidence: https://moonshotai.github.io/kimi-code/en/customization/hooks
- plan_mode: **True** — Shift-Tab or `/plan`; agent produces a plan and waits for approve/reject/revise before modifying files; exiting Plan mode requires confirmation even under YOLO (Auto mode auto-approves plan exits) [S18]. Evidence: https://moonshotai.github.io/kimi-code/en/guides/interaction
- plugin_docs_url: https://moonshotai.github.io/kimi-code/en/customization/plugins
- config_docs_url: https://moonshotai.github.io/kimi-code/en/configuration/config-files
- ACP support: **yes, first-party** — `kimi acp` subcommand speaks Agent Client Protocol over stdio; capability matrix published (stable agent-side methods 10/12 incl. session/new/load/resume/prompt/cancel/list, image prompts, MCP forwarding http/stdio/sse; terminal reverse-RPC not implemented); docs give setup for Zed, JetBrains, and **Paseo** by name (`command: ["kimi","acp"]`; Paseo doesn't drive login, so log in in the terminal first) [S11][S30]. The legacy kimi-cli also shipped `kimi acp` [S2].
- SDK: **partial** — monorepo contains `packages/node-sdk` (unpublished status not researched); separate repo MoonshotAI/kimi-agent-sdk ("programmatic interface to interact with the Kimi CLI", 571 stars) last pushed 2026-05-29 and targets the legacy CLI's Wire mode (plus kimi-agent-rs, a Rust Wire-mode agent server) [S1][S3]. The supported programmatic surfaces for the new CLI are `kimi -p` print mode and the experimental `kimi web` REST/WebSocket API [S12].

## 4. Claimed differentiation (raw material for PRI-2927)

- tagline (repo/docs, verbatim): "The Starting Point for Next-Gen Agents" [S1][S13]
- one-liner (README): AI coding agent in your terminal — reads/edits code, runs shell commands, searches files, fetches web pages, "and choose[s] the next step based on the feedback it receives"; works out of the box with Kimi models, configurable for other providers [S4]
- maker claims (README "Key Features", paraphrased) [S4]:
  1. Single-binary install — no Node.js setup or global-module conflicts.
  2. "Blazing-fast startup" — TUI ready in milliseconds.
  3. Purpose-built TUI tuned for long, focused agent sessions.
  4. **Video input** — drop a screen recording/demo clip into chat (turn a clip into a LUT, a recording into working code); Kimi provider supports video upload [S8].
  5. AI-native MCP configuration — add/edit/authenticate MCP servers conversationally via `/mcp-config`, no JSON editing.
  6. Rich plugin ecosystem — skills, MCP servers, data sources from marketplace or any GitHub repo, trust level surfaced up front.
  7. Subagents (`coder`/`explore`/`plan`) for focused, parallel work in isolated contexts.
  8. Lifecycle hooks; and first-class editor/IDE integration via ACP (`kimi acp` for Zed, JetBrains, any ACP client).
- product-page claims (kimi.com/code, Chinese, paraphrased): a code-focused subscription built on Kimi K3 (1M context); compatible with many dev workflows (terminal, IDE, CLI); faster, more stable responses for programming tasks [S13]
- audience: developers working in the terminal and ACP-capable IDEs; Chinese and international (bilingual docs en/zh; OAuth via kimi.com and kimi.ai) [S4][S9]
- goal/roadmap artifact: repo GOAL.md (Chinese) specs an autonomous "goal mode" (structured goal state machine driving multi-turn unattended execution) [S3]; third-party pricing pages list "Goal Mode" as a higher-tier plan feature [S17]

## 5. Company & contact targets (PRI-2929) — company-level only

- company: Moonshot AI (Beijing, China; Chinese name 月之暗面 / Moonshot AI); founded 2023 [S15][S16]
- funding stage: late private; ~$2B raised at $20B valuation (May 2026, TechCrunch); press reports Aug 2026 pre-IPO round talks targeting up to $50B pre-money and a Hong Kong listing (unconfirmed) [S16][S22]
- size: not researched (null)
- publicly named leadership: **Yang Zhilin — founder & CEO** (named in TechCrunch/Dealroom coverage of the company's own funding announcements; ex-CMU PhD, previously Google/Meta AI) [S16][S15]. No CTO/head-of-product/DevRel/partnerships names found in English-language official materials — null (not researched deeper; Moonshot has no English team page found).
- contact: GitHub issues on MoonshotAI/kimi-code; security via SECURITY.md in repo [S4]. Platform/API business via platform.moonshot.ai (null — not researched).

## 6. Open questions / conflicts (incl. census-entry errors)

- **Census `maintained: "abandoned"` — WRONG.** The product is very actively maintained: successor repo MoonshotAI/kimi-code has 1,265 commits and 68 releases since 2026-05-26, latest 0.38.0 on 2026-08-20, pushed 2026-08-22 [S1][S9]. Only the legacy Python repo is winding down — and even it is not archived and was pushed as recently as 2026-08-03 [S1][S2]. Correct value: maintained (with a note that kimi-cli is the deprecated predecessor).
- **Census `url`/`source_code_url` = github.com/MoonshotAI/kimi-cli — outdated.** Current repo is https://github.com/MoonshotAI/kimi-code (Paseo's link is the right one). The rename is a repo migration + Python→TypeScript rewrite by the same team; README banner and `kimi migrate` command document the succession [S2][S6].
- Census `license: "Apache-2.0"` — new repo is **MIT**; Apache-2.0 applies only to legacy kimi-cli [S1][S3].
- Census `language: "Python"` — now **TypeScript** (Node.js >= 22.19.0) [S1][S5].
- Census `install_method: "pip install kimi-cli"` — current install is the curl/PowerShell script or `npm install -g @moonshot-ai/kimi-code`; pip/PyPI belongs to the legacy CLI [S4][S7].
- Census `first_released: "2025-10-15"` — that is the kimi-cli repo creation date; first PyPI upload was 2025-10-22; the current-generation CLI first released 2026-05-26 (0.2.0) [S1][S7][S9]. Defensible if "first release" means the product line; say which.
- Census `current_release: "2026-08-03"` — that is the legacy repo's last push date, not a release; actual latest release is 0.38.0, 2026-08-20 [S1][S9].
- Census `homepage`/`docs_url` (moonshotai.github.io/kimi-cli/) — current docs are https://moonshotai.github.io/kimi-code/en/ and product page https://www.kimi.com/code/ [S1][S13].
- Census `stars: null` → kimi-cli 11,236 / kimi-code 6,996 (2026-08-21) [S1]. Census plugin fields all null → filled in §3 (plugin_support True, claude_code_plugin partial, subagents True, hooks True, plan_mode True).
- Census prose says "VS Code extension, Zsh integration" — Zsh plugin (zsh-kimi-cli) belongs to the legacy CLI (last pushed 2025-10-27); not documented for the new CLI [S1][S2].
- `kimi acp` (Paseo's driver) is present and documented in **both** generations; Paseo is named in the official IDE docs [S11].
- Official pricing page (https://www.kimi.com/membership/pricing) renders via JS and returned only a title to fetching; tier names/prices in §2 come from third-party aggregator pages and could not be verified against an official source [S17]. Unreachable source.
- Kimi Code plan tier structure/quotas, `packages/node-sdk` publication status, Moonshot headcount, and any official Chinese-language launch post for kimi-code were not researched further (null).
- npm name collision: bare `kimi-code` on npm is an unrelated third-party claude-code proxy; only `@moonshot-ai/kimi-code` is official [S5].
- K3 benchmark numbers (FrontierSWE 81.2, Terminal-Bench 2.0 88.3) are maker-reported model scores relayed by press/aggregators, and describe the model, not this harness [S20].

## 7. Sources

1. [S1] api.github.com/repos/MoonshotAI/{kimi-cli,kimi-code} (+releases, commits, contributors Link headers; org repo list) — stars, dates, licenses, cadence (2026-08-21/22)
2. [S2] MoonshotAI/kimi-cli README (via GitHub API) — deprecation banner, legacy features, `kimi acp`; [S2-README] legacy feature list
3. [S3] MoonshotAI/kimi-code repo tree + GOAL.md + apps/kimi-code/package.json — monorepo contents, MIT, goal-mode spec
4. [S4] MoonshotAI/kimi-code README — tagline, features, install, license, community
5. [S5] registry.npmjs.org + api.npmjs.org downloads — @moonshot-ai/kimi-code versions/dates/downloads; `kimi-code` collision
6. [S6] docs guides/migration.md — Python→Node rewrite, `kimi migrate`
7. [S7] pypi.org/pypi/{kimi-cli,kimi-code}/json + pypistats.org — first uploads, versions, download counts
8. [S8] docs configuration/providers.md — provider types, BYO models, models.dev import, video upload
9. [S9] docs release-notes/changelog.md — 0.2.0 (2026-05-26) through 0.38.0 (2026-08-20), OAuth kimi.ai/kimi.com
10. [S10] VS Code Marketplace extensionquery API (moonshot-ai.kimi-code) — 536,510 installs, dates, ratings
11. [S11] docs guides/ides.md — Zed/JetBrains/Paseo ACP setup
12. [S12] docs guides/server.md — `kimi web` web UI, REST/WS API (experimental)
13. [S13] https://www.kimi.com/code/ — product page, K3/K2.7 Code, install, pricing link
14. [S14] MarkTechPost 2026-06-06 — press coverage of kimi-code release
15. [S15] Dealroom note — $2B at $20B, $200M ARR (Apr 2026), founder bio
16. [S16] TechCrunch 2026-05-07 — $2B raise, $20B valuation, ARR, OpenRouter #2, Yang Zhilin
17. [S17] codingplan.org/en/plans/kimi + hvoy.ai/codeagentswarm aggregators (via search) — plan tiers/prices (third-party)
18. [S18] docs guides/interaction.md — approval flow, Plan/YOLO/Auto modes
19. [S19] formulae.brew.sh/api/formula/{kimi-cli,kimi-code}.json — Homebrew installs
20. [S20] web search results: BigGo/morphllm/Northflank/explainx on K3 — launch 2026-07-16, specs, benchmarks, subscription pause
21. [S21] VentureBeat (via search) — K3 open weights 2026-07-27, largest open-source model claim
22. [S22] BigGo Finance (via search) — pre-IPO $50B target, HK listing (rumor)
23. [S23] https://www.kimi.ai/resources/shipping-a-refactor-of-moonshot-ai-with-kimi-code-cli (2026-08-12) — internal case study
24. [S24] docs customization/mcp.md — MCP client details, /mcp-config, OAuth, trust prompt
25. [S25] docs customization/plugins.md — plugin manifest, marketplace tabs, official plugins, security model
26. [S26] docs customization/skills.md — SKILL.md format, ~/.agents/skills cross-tool dirs
27. [S27] docs customization/agents.md — subagents, custom agent files, Claude Code-style files loadable
28. [S28] docs reference/slash-commands.md — /init generates AGENTS.md; /import-from-cc-codex
29. [S29] docs customization/hooks.md — events, blocking, fail-open
30. [S30] docs reference/kimi-acp.md — ACP capability matrix, method coverage

## Inclusion check (Jesse's test)

**Yes** — Kimi Code CLI is a first-party coding agent with its own agentic loop (reads/edits files, runs shell commands, dispatches subagents, iterates on feedback; the loop lives in the open-source agent-core packages), not a wrapper around someone else's agent [S4][S3].
