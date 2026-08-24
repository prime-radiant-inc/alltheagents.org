# Dossier: Claude Code (census_slug: claude-code)

Compiled 2026-08-21. Facts only. Null convention: "null = not researched"; "False/none = researched and absent". Each non-obvious fact carries a source [Sn] (see section 7) and an as-of date.

## 1. Identity

- name: Claude Code
- maker: Anthropic PBC (company; legal name "Anthropic Public Benefit Corporation"); HQ San Francisco, CA, USA [S25][S29][S30] (as-of 2026-08-21)
- product URL: https://claude.com/product/claude-code (code.claude.com 302-redirects here) [S14]; docs home https://code.claude.com/docs/en/overview [S2]
- repo URL: https://github.com/anthropics/claude-code [S1]
- license: proprietary. Repo LICENSE.md: "(c) Anthropic PBC. All rights reserved. Use is subject to Anthropic's Commercial Terms of Service" [S3] (as-of 2026-08-21). npm package license field: "SEE LICENSE IN README.md" [S5]. GitHub API reports license: null [S4].
- open source? False. source_available: partial — the GitHub repo holds issues, CHANGELOG, plugins/examples, devcontainer, GitHub Action; the CLI ships as a native binary (npm package downloads a per-platform binary) [S13]. Core agent source is not published [S1][S13]. Agent SDK repos (claude-agent-sdk-python 7,949 stars; claude-agent-sdk-typescript 1,711 stars) are public wrappers [S4] (as-of 2026-08-21).
- first public release: 2025-02-24, "limited research preview" announced alongside Claude 3.7 Sonnet [S11]; first npm version 0.2.6 published 2025-02-24 [S5]; GitHub repo created 2025-02-22 [S4]. General availability 2025-05-22 (Claude 4 launch post) [S12].
- latest release: v2.1.239, 2026-08-21 (GitHub release tag published 2026-08-21T19:54Z; npm latest 2.1.239 published 2026-08-21T17:18Z) [S4][S5]. 494 npm versions published to date [S5].
- what it is:
  - Form factors: terminal CLI (primary); VS Code extension (also installable in Cursor); JetBrains plugin; standalone Desktop app (macOS, Windows, Linux beta); web at claude.ai/code plus iOS/Android Claude app; GitHub Actions and GitLab CI/CD; Slack (@Claude); Chrome extension; cloud "Routines" (scheduled/background); self-hosted cloud runners (Team/Enterprise beta) [S2][S20] (as-of 2026-08-21).
  - Models: Anthropic Claude models only (Opus/Sonnet/Haiku tiers, incl. Opus 4.8, Sonnet 5, Fable 5 per docs/leaderboards); reachable via Anthropic API/claude.ai login, or via Amazon Bedrock, Google Cloud Agent Platform (Vertex), Microsoft Foundry [S13][S2]. No BYO non-Anthropic models in official docs (none found).
  - Pricing: included in Claude Pro ($17/mo annual, $20 monthly), Max 5x ($100/mo), Max 20x ($200/mo), Team Standard ($20/$25 per seat), Team Premium ($100/$125 per seat), Enterprise; or API pay-as-you-go via Console/API key. Free plan does not include Claude Code [S9][S13][S14] (as-of 2026-08-21).
  - Install: native installer `curl -fsSL https://claude.ai/install.sh | bash` (macOS/Linux/WSL), `irm https://claude.ai/install.ps1 | iex` (Windows), `brew install --cask claude-code`, `winget install Anthropic.ClaudeCode`, signed apt/dnf/apk repos, or `npm install -g @anthropic-ai/claude-code` (README labels npm "deprecated"; docs still document it; npm package now pulls a native binary and requires Node 22+ as of v2.1.198) [S1][S13] (as-of 2026-08-21).
  - Default autonomy: permission modes `default` (Manual: asks before edits/shell/network), `acceptEdits`, `plan`, `auto` (a classifier model reviews actions), `dontAsk`, `bypassPermissions`. Since 2026-08-14, `auto` is the default starting mode for new sessions on Pro, Max and Team plans; API-key/Console sessions start in Manual unless configured [S19][S20]. Bash sandboxing (OS-level filesystem/network isolation) available on macOS/Linux/WSL2 [S8][S13].
  - Repo language per GitHub API: Python (repo is mostly scripts/plugins; product is a native binary) [S4].

## 2. Adoption evidence

| metric / claim | value | as-of | source | type |
|---|---|---|---|---|
| GitHub stars | 142,288 | 2026-08-21 | [S4] | independently observable |
| GitHub forks | 22,815 | 2026-08-21 | [S4] | independently observable |
| GitHub watchers (subscribers) | 869 | 2026-08-21 | [S4] | independently observable |
| GitHub open issues | 15,044 | 2026-08-21 | [S4] | independently observable |
| GitHub issues ever filed (search API) | 85,916 | 2026-08-21 | [S4] | independently observable |
| GitHub contributors (incl. anonymous) | 55 | 2026-08-21 | [S4] | independently observable |
| Commits, last 90 days (since 2026-05-23) | 96 | 2026-08-21 | [S4] | independently observable |
| Releases | roughly daily; v2.1.237/238/239 on Aug 20-21 2026 | 2026-08-21 | [S4] | independently observable |
| npm weekly downloads, @anthropic-ai/claude-code | 18,259,096 (2026-08-13..19) | 2026-08-19 | [S6] | independently observable |
| npm monthly downloads, @anthropic-ai/claude-code | 64,278,730 (2026-07-21..08-19) | 2026-08-19 | [S6] | independently observable |
| npm weekly downloads, @anthropic-ai/claude-agent-sdk | 8,037,280 | 2026-08-19 | [S6] | independently observable |
| npm monthly downloads, @anthropic-ai/claude-agent-sdk | 36,965,248 | 2026-08-19 | [S6] | independently observable |
| Homebrew cask installs (claude-code), 30d / 90d / 365d | 71,071 / 251,460 / 1,107,061; #2 cask overall (3.10% of cask installs); claude-code@latest 10,321 (30d) | 2026-08-21 | [S7] | independently observable |
| VS Code Marketplace installs (anthropic.claude-code) | 23,728,426 installs; 762 ratings, avg 3.72 | 2026-08-21 | [S31] | independently observable |
| JetBrains Marketplace downloads (plugin 27310 "Claude Code [Beta]") | 4,604,872 | 2026-08-21 | [S32] | independently observable |
| anthropics/claude-plugins-official stars / forks | 33,793 / 3,846 (created 2025-11-20) | 2026-08-21 | [S4] | independently observable |
| anthropics/claude-code-action stars | 8,691 | 2026-08-21 | [S4] | independently observable |
| claude-agent-sdk-python / -typescript stars | 7,949 / 1,711 | 2026-08-21 | [S4] | independently observable |
| PyPI downloads, claude-agent-sdk | null (pypistats.org returned 429 rate-limit on three attempts) | 2026-08-21 | [S33] | unreachable |
| Run-rate revenue | >$500M, usage up >10x in 3 months since May 2025 launch | 2025-09-02 | [S23] | maker-claimed |
| Run-rate revenue | $1B, ~6 months after GA | 2025-12-03 | [S24] | maker-claimed |
| Run-rate revenue | >$2.5B, "more than doubled since the beginning of 2026" | 2026-02-12 | [S21] | maker-claimed |
| Weekly active users | "doubled since January 1" (no absolute figure) | 2026-02-12 | [S21] | maker-claimed |
| Business subscriptions | quadrupled since start of 2026; enterprise > half of Claude Code revenue | 2026-02-12 | [S21][S27] | maker-claimed |
| Share of GitHub public commits | "4% of all GitHub public commits", doubled in one month — cited by Anthropic as "a recent analysis" (SemiAnalysis, 2026-02) | 2026-02-12 | [S21][S34] | third-party analysis, repeated by maker |
| Usage study dataset | ~400,000 sessions from ~235,000 users (Oct 2025-Apr 2026); ~10 Claude actions per user prompt | 2026-06-16 | [S28] | maker-claimed |
| Anthropic company run-rate | $14B (Feb 2026) -> $47B (May 2026) | 2026-05-28 | [S21][S22] | maker-claimed |
| "$8B Claude Code run-rate (May 2026)" | appears only in analyst/aggregator pages (FutureSearch etc.); no Anthropic source found | 2026-08-21 | [S35] | unverified third-party |
| "4.2M weekly active developers / 1,400 enterprise orgs" | appears only on aggregator stats pages; no Anthropic source found | 2026-08-21 | [S35] | unverified third-party |
| Public customers / case studies (Claude Code-tagged) | Rakuten (7h autonomous run; 24->5 days; 79% TTM cut), Ramp (1M+ AI lines in 30 days; 50% weekly active engineers), Deepgram, League, DoorDash, Spotify; product page logos: Ramp, Intercom, Notion, GitLab, Dynatrace, Kubernetes, Heroku, Stripe, Elastic, Terraform, Sentry, AWS, MongoDB, Atlassian, Datadog, GitHub, Vercel, New Relic; Bun post names Netflix, Spotify, KPMG, L'Oreal, Salesforce | 2026-08-21 | [S14][S15][S16][S17][S24] | maker-claimed |
| Funding / valuation (company) | Series G $30B at $380B post (2026-02-12); Series H $65B at $965B post (2026-05-28); confidential S-1 reportedly filed 2026-06-01 | 2026-05-28 | [S21][S22][S26] | maker-claimed (round) / press |
| Acquisition | Anthropic acquired Bun (JS runtime) to accelerate Claude Code infrastructure | 2025-12-03 | [S24] | maker-claimed |
| Community: Discord | "Claude Developers" Discord linked from README; member count not retrievable without joining | 2026-08-21 | [S1] | null (not obtainable) |
| Community: GitHub Discussions | not enabled on repo (API has_discussions null/false) | 2026-08-21 | [S4] | independently observable |
| Benchmark: Terminal-Bench 2.1 (agent leaderboard) | #1 Claude Code + Fable 5 83.8% (2026-06-07); also #5 (Opus 4.8, 78.9%), #10 (Sonnet 5, 74.6%), #12 (Opus 4.7, 68.9%) | 2026-08-21 | [S36] | independently observable (third-party leaderboard) |
| Benchmark: SWE-bench | not researched for the harness (SWE-bench reports models, not Claude Code) | — | — | null |
| Third-party ACP adapter downloads | @agentclientprotocol/claude-agent-acp 928,682 npm weekly; @zed-industries/claude-code-acp 14,262 weekly | 2026-08-19 | [S6] | independently observable |
| Press | Constellation Research (2026-02-12) and Reuters (Feb 2026, via search) on $2.5B run-rate; TechCrunch on Series H | 2026-08-21 | [S27][S22][S35] | press |

## 3. Plugin interface (PRI-2925)

- mcp_support: **client** (connects to MCP servers over http/streamable-http, sse (deprecated), stdio, ws; scopes local/project/user; OAuth for http; managed-settings controls). Docs do not describe Claude Code itself as an MCP server (an earlier `claude mcp serve` is not in the current MCP page) [S8-MCP] (as-of 2026-08-21). Evidence: https://code.claude.com/docs/en/mcp
- plugin_support: **True** — plugins are directories with `.claude-plugin/plugin.json` plus `skills/`, `commands/`, `agents/`, `hooks/hooks.json`, `.mcp.json`, `.lsp.json`, `monitors/`, `bin/`, `settings.json`; distributed via marketplaces (`marketplace.json` in git repos, zip archives, local paths); Anthropic runs `claude-plugins-official` (auto-registered) and `claude-plugins-community` (reviewed submissions); `claude plugin init/validate`, `--plugin-dir`, `--plugin-url` [S10][S18] (as-of 2026-08-21). Standalone `.claude/` skills/agents/hooks also supported.
- claude_code_plugin: **yes** — this is the reference implementation of the format [S10].
- subagents: **True** — built-in Explore / Plan / general-purpose; custom agents as Markdown+frontmatter in `.claude/agents/`, `~/.claude/agents/`, plugins, `--agents` flag; background by default, up to 20 concurrent (configurable), nesting depth 3, worktree isolation, per-agent model/tools/permissionMode/memory/hooks/MCP; forks (`/subtask`); agent teams (multi-session), dynamic workflows, cross-session messaging (v2.1.224) [S9-SUB][S20] (as-of 2026-08-21). Evidence: https://code.claude.com/docs/en/sub-agents
- hooks: **True** — events include SessionStart, SessionEnd, Setup, UserPromptSubmit, UserPromptExpansion, Stop, StopFailure, PreToolUse, PermissionRequest, PermissionDenied, PostToolUse, PostToolUseFailure, PostToolBatch, SubagentStart/Stop, TeammateIdle, TaskCreated/Completed, InstructionsLoaded, ConfigChange, CwdChanged, DirectoryAdded, FileChanged, PreCompact/PostCompact, Elicitation/ElicitationResult, Notification, MessageDisplay, WorktreeCreate/Remove; handler types command, http, mcp_tool, prompt, agent; can block/modify input [S8-HOOKS] (as-of 2026-08-21). Evidence: https://code.claude.com/docs/en/hooks
- plan_mode: **True** — `plan` permission mode: reads files and runs read-only/classifier-approved commands, no edits; Shift+Tab, `/plan`, `--permission-mode plan`; plan approval switches mode [S19]. Evidence: https://code.claude.com/docs/en/permission-modes
- plugin_docs_url: https://code.claude.com/docs/en/plugins (reference: https://code.claude.com/docs/en/plugins-reference; marketplaces: https://code.claude.com/docs/en/plugin-marketplaces)
- config_docs_url: https://code.claude.com/docs/en/settings (permissions: https://code.claude.com/docs/en/permissions)
- ACP support: **no first-party**. Official docs index (llms.txt) has no ACP page [S2-LLMS]. Third-party adapters exist: zed-industries/claude-code-acp (Zed-built, Sept 2025, wraps the Claude Agent SDK, Apache-licensed) and its successor agentclientprotocol/claude-agent-acp (2,409 stars) [S37][S38] (as-of 2026-08-21). Anthropic's SDK branding rules forbid third parties calling SDK-based agents "Claude Code" [S9-SDK].
- SDK: **yes** — Claude Agent SDK (formerly Claude Code SDK, GA May 2025) for Python and TypeScript; same tools/agent loop/hooks/subagents/MCP/plugins as the CLI; other languages via `claude -p --output-format json` subprocess; governed by Commercial Terms; third-party products may not offer claude.ai login [S9-SDK][S12] (as-of 2026-08-21).

## 4. Claimed differentiation (raw material for PRI-2927)

- tagline (README, verbatim-short): "An agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster" — https://github.com/anthropics/claude-code [S1]
- tagline (product page): "Work with Claude directly in your codebase. Build, debug, and ship from your terminal, IDE, Slack, web, and more." — https://claude.com/product/claude-code [S14]
- docs one-liner: reads codebase, edits files, runs commands, integrates with dev tools; available in terminal, IDE, desktop app, browser — https://code.claude.com/docs/en/overview [S2]
- maker claims (paraphrased):
  1. Terminal-native, Unix-philosophy composable: pipe logs in, run in CI, chain with tools (`claude -p`) [S2].
  2. One engine, many surfaces: CLAUDE.md, settings, MCP servers carry across terminal, IDE, desktop, web, mobile, Slack, CI; sessions move between surfaces (Remote Control, `--teleport`, `/desktop`) [S2].
  3. Maps/explains whole codebases via agentic search; multi-file edits with codebase understanding [S14].
  4. Runs locally, asks permission before file changes (product page) — while docs now default Pro/Max/Team sessions to auto mode with a classifier [S14][S19][S20].
  5. Deep customization: CLAUDE.md memory + auto-memory, skills, hooks, plugins/marketplaces, subagents, agent teams, dynamic workflows ("write its own harness on the fly") [S2][S10][S39].
  6. Parallel/background autonomy: subagents, background agents, cloud sessions, Routines, scheduled tasks, channels that push events into sessions [S2].
  7. Enterprise controls: managed settings, marketplace allowlists, sandboxing, Bedrock/Vertex/Foundry, self-hosted cloud runners, signed binaries/repos [S8][S13][S20].
  8. Growth/usage evidence offered: $2.5B run-rate, WAU doubled, customer stories (Rakuten, Ramp, Notion, etc.) [S21][S14][S15][S16].
- audience: developers ("helps you code faster"); individual devs (Pro), teams/enterprises (Max/Team/Enterprise), "power users in larger codebases"; launch post: developers, to learn how they use Claude for coding [S1][S14][S11].

## 5. Company & contact targets (PRI-2929) — company-level only

- legal name: Anthropic PBC / Anthropic Public Benefit Corporation [S25][S3]
- HQ: San Francisco, CA (Wikipedia: 500 Howard St; JetBrains vendor record lists 548 Market St) [S29][S32]
- size: ~2,500 (Wikipedia 2026) to ~4,000-5,000 (third-party trackers, Mar 2026) employees — estimates vary [S29][S30]
- funding stage: late private; Series H $65B at $965B post-money (2026-05-28); press reports confidential S-1 filed 2026-06-01 [S22][S26]
- publicly named leadership (only as named on anthropic.com):
  - Dario Amodei — CEO & co-founder (board list on anthropic.com/company; CEO title per Wikipedia) [S25][S29]
  - Daniela Amodei — President & Co-Founder [S40][S41]
  - Rahul Patil — Chief Technology Officer (joined 2025-10-07) [S41]
  - Sam McCandlish — Chief Architect (formerly CTO) [S41]
  - Krishna Rao — Chief Financial Officer [S21][S22]
  - Mike Krieger — Chief Product Officer (moved to Labs, Jan 2026) [S24][S42]
  - Ami Vora — leads Product organization (from Jan 2026) [S42]
  - Angela Jiang — Head of Product [S40]
  - Katelyn Lesse — Head of Platform [S40]
  - Boris Cherny — Head of Claude Code [S43][S44]
  - Cat Wu — Head of Product, Claude Code (as of 2025-03-27 webinar) [S44]
  - Thariq Shihipar — AI Product Lead (bylined "A harness for every task", 2026-06-02) [S39]
  - Paul Smith — Chief Commercial Officer [S40]
  - Steve Corfield — Head of Global Business Development & Partnerships [S40]
  - Dan Rosenthal — Global Head of Cloud Partnerships [S40]
  - Rich O'Connell — Head of Alliances [S40]
  - DevRel lead: none found named on anthropic.com (careers pages advertise DevRel roles) [S45] — researched, absent.
- contact: partnerships via https://www.anthropic.com/contact-sales (SDK docs point here) [S9-SDK]

## 6. Open questions / conflicts

- Existing census `stars: null` — GitHub API shows 142,288 stars (2026-08-21) [S4]; census prose already says "142k stars, 731 commits" — commit count not re-verified (repo shows 96 commits in last 90 days).
- Existing census `license: "Closed Source"` / `source_available: True` — LICENSE.md is all-rights-reserved; only the repo scaffolding (issues, plugins, action, changelog) is public. "source_available: True" overstates; suggest "partial" [S3][S13].
- Existing census `language: "TypeScript, JavaScript (Node.js)"` — GitHub reports the repo language as Python; the shipped CLI is a native binary (npm wrapper no longer runs via Node) [S4][S13]. Field is ambiguous (repo vs product).
- Existing census `platforms: ["CLI"]` — official surfaces also include VS Code, JetBrains, Desktop app, web, mobile, Slack, GitHub/GitLab CI, Chrome [S2].
- Existing census `first_released: "2025-02-22"` — that is the repo creation date; public announcement/first npm publish was 2025-02-24 [S11][S5].
- Existing census `current_release: "2026-08-20"` — now v2.1.239 on 2026-08-21 [S4].
- Existing census `plugin_docs_url`/`config_docs_url`/`pricing`: null — filled above.
- Existing census `install_method` says npm is "(deprecated)" — README says deprecated; docs still document npm and say it installs the same native binary [S1][S13]. Minor.
- Existing census `mcp_support: True` — more precisely "client"; no current first-party MCP-server mode found in docs [S8-MCP].
- Maker product page says Claude Code "asks permission before file changes" while docs state auto mode (classifier) is now the default on Pro/Max/Team since 2026-08-14 [S14][S20]. Positioning vs behavior diverge.
- "$8B run-rate (May 2026)", "4.2M weekly active developers", "1,400 enterprise orgs" circulate on aggregator stats sites with no Anthropic source found; Anthropic's last Claude Code-specific disclosure located is $2.5B on 2026-02-12 [S21][S35]. Series H post gives company run-rate only [S22].
- "4% of GitHub public commits" is SemiAnalysis' estimate, repeated by Anthropic as "a recent analysis" [S21][S34].
- Discord member count and PyPI downloads for claude-agent-sdk were not obtainable (no public count; pypistats 429).
- Employee count varies 2,500-5,000 across sources [S29][S30].
- Leadership titles are as of the dated pages cited; roles may have changed (e.g., Krieger to Labs).

## 7. Sources

1. [S1] https://github.com/anthropics/claude-code (README via raw.githubusercontent.com) — tagline, install, Discord, data policy
2. [S2] https://code.claude.com/docs/en/overview — surfaces, features, install, positioning; [S2-LLMS] https://code.claude.com/docs/llms.txt — docs index (no ACP page)
3. [S3] https://raw.githubusercontent.com/anthropics/claude-code/main/LICENSE.md — all rights reserved
4. [S4] https://api.github.com/repos/anthropics/claude-code (+ releases, contributors, commits, search/issues; gh api for related repos) — stars/forks/dates
5. [S5] https://registry.npmjs.org/@anthropic-ai/claude-code — versions, first/latest publish dates, license field
6. [S6] https://api.npmjs.org/downloads/point/last-week|last-month/... — npm download counts
7. [S7] https://formulae.brew.sh/api/cask/claude-code.json and /api/analytics/cask-install/30d.json — Homebrew installs
8. [S8] https://code.claude.com/docs/en/permissions — modes, sandbox; [S8-MCP] https://code.claude.com/docs/en/mcp — MCP client details; [S8-HOOKS] https://code.claude.com/docs/en/hooks — hook events/types
9. [S9-SUB] https://code.claude.com/docs/en/sub-agents — subagents; [S9-SDK] https://code.claude.com/docs/en/agent-sdk/overview — Agent SDK, branding, terms
10. [S10] https://code.claude.com/docs/en/plugins — plugin format, marketplaces
11. [S11] https://www.anthropic.com/news/claude-3-7-sonnet — 2025-02-24 research preview
12. [S12] https://www.anthropic.com/news/claude-4 — 2025-05-22 GA, SDK, IDE extensions
13. [S13] https://code.claude.com/docs/en/setup — install methods, requirements, auth, binaries
14. [S14] https://claude.com/product/claude-code — product page claims, logos, pricing
15. [S15] https://claude.com/customers/rakuten — Rakuten numbers
16. [S16] https://claude.com/customers/ramp — Ramp numbers
17. [S17] https://claude.com/customers — case-study list by product
18. [S18] https://code.claude.com/docs/en/plugin-marketplaces — marketplace format, managed restrictions
19. [S19] https://code.claude.com/docs/en/permission-modes — mode table, plan mode, auto default
20. [S20] https://code.claude.com/docs/en/whats-new/2026-w32 — auto mode default 2026-08-14, cross-session messaging, self-hosted
21. [S21] https://www.anthropic.com/news/anthropic-raises-30-billion-series-g-funding-380-billion-post-money-valuation — $2.5B, WAU doubled, 4% commits, CFO
22. [S22] https://www.anthropic.com/news/series-h — $65B/$965B, $47B run-rate
23. [S23] https://www.anthropic.com/news/anthropic-raises-series-f-at-usd183b-post-money-valuation — $500M run-rate Sept 2025
24. [S24] https://www.anthropic.com/news/anthropic-acquires-bun-as-claude-code-reaches-usd1b-milestone — $1B, Bun, Krieger CPO
25. [S25] https://www.anthropic.com/company — PBC, board names
26. [S26] https://techcrunch.com/2026/05/28/anthropic-raises-65-billion-nears-1t-valuation-ahead-of-ipo/ — press on Series H
27. [S27] https://www.constellationr.com/insights/news/anthropics-claude-code-revenue-doubled-jan-1 — press recap of Series G numbers
28. [S28] https://www.anthropic.com/research/claude-code-expertise — 400k-session usage study
29. [S29] https://en.wikipedia.org/wiki/Anthropic — HQ, CEO, employees
30. [S30] web search results on employee count (Revelio/jobsbyculture) — size estimates
31. [S31] https://marketplace.visualstudio.com/_apis/public/gallery/extensionquery (anthropic.claude-code) — VS Code installs
32. [S32] https://plugins.jetbrains.com/api/plugins/27310 — JetBrains downloads, vendor address
33. [S33] https://pypistats.org/api/packages/claude-agent-sdk/recent — rate-limited, unreachable
34. [S34] https://newsletter.semianalysis.com/p/claude-code-is-the-inflection-point (via search) — 4% commits origin
35. [S35] web search results (getpanto, serpsculpt, futuresearch, memeburn) — unverified aggregator numbers
36. [S36] https://www.tbench.ai/leaderboard/terminal-bench/2.1 — Terminal-Bench 2.1 placements
37. [S37] https://zed.dev/blog/claude-code-via-acp — Zed-built ACP adapter, 2025-09-03
38. [S38] https://github.com/agentclientprotocol/claude-agent-acp (README via raw) — ACP adapter over Agent SDK
39. [S39] https://claude.com/blog/a-harness-for-every-task-dynamic-workflows-in-claude-code — dynamic workflows, byline
40. [S40] https://www.anthropic.com/events/anthropic-partner-kickoff-2026 — partnership/product leadership titles
41. [S41] https://www.anthropic.com/news/rahul-patil-joins-anthropic — CTO, President, Chief Architect
42. [S42] https://www.anthropic.com/news/introducing-anthropic-labs — Krieger, Vora
43. [S43] https://www.anthropic.com/webinars/claude-code-for-financial-services-boris-cherny — "Head of Claude Code"
44. [S44] https://www.anthropic.com/webinars/claude-code-live — Cat Wu, Boris Cherny titles
45. [S45] web search: anthropic.com DevRel — job postings only, no named lead
46. https://claude.com/pricing — plan prices
47. https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md — v2.1.239 notes

## Inclusion check (Jesse's test)

**Yes** — Claude Code is a first-party agent with its own agentic loop (reads/edits files, runs shell, iterates to completion; the same loop is exposed as the Claude Agent SDK), not a wrapper around another agent [S2][S9-SDK].
