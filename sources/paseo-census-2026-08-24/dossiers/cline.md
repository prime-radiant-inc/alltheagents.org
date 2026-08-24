# Dossier: Cline (census_slug: cline)

Compiled 2026-08-21. Facts only. Null convention: "null = not researched"; "False/none = researched and absent". Each non-obvious fact carries a source [Sn] (see section 7) and an as-of date. Surfaces are labelled: **EXT** = VS Code / Open VSX extension (id saoudrizwan.claude-dev), **JB** = JetBrains plugin, **CLI** = `cline` npm CLI, **SDK** = @cline/sdk, **KANBAN** = cline/kanban web board, **DESKTOP** = Cline Desktop app, **CLOUD** = hosted Cline account / credits / ClinePass / Cline API / Enterprise console.

## 1. Identity

- name: Cline (launched as "Claude Dev"; renamed Cline in Oct 2024; extension id still `saoudrizwan.claude-dev`) [S1][S38] (as-of 2026-08-21)
- maker: Cline Bot Inc. (company). HQ San Francisco, CA per funding press coverage [S24]; JetBrains vendor record lists a Wilmington, DE registered address, country US [S8]. README copyright "Apache 2.0 (c) 2026 Cline Bot Inc." [S1]
- product URL: https://cline.bot ; CLI page https://cline.bot/cli ; docs https://docs.cline.bot [S1][S12]
- repo URL: https://github.com/cline/cline (monorepo: `apps/cli`, `apps/vscode`, `apps/cline-hub`, `apps/examples`, `sdk/`, `evals/`, `docs/`) [S2][S5] (as-of 2026-08-21)
- license: Apache-2.0 (GitHub API license key `apache-2.0`; npm `cline` license Apache-2.0; Open VSX Apache-2.0) [S2][S6][S7]
- open source? **partial.** EXT, CLI, SDK, KANBAN source is public under Apache-2.0 [S1][S2][S30]. JB: README states "Currently we are not open-sourcing JetBrains plugins" [S1]. DESKTOP: releases are published in the cline/cline repo (desktop-v0.0.15, 2026-08-21) but no `apps/desktop` directory was found in the repo tree — source location unverified (see section 6) [S5][S31]. CLOUD (app.cline.bot, api.cline.bot, ClinePass, Enterprise console) is a hosted service, not open (none found).
- first public release: EXT first published to VS Code Marketplace 2024-07-10 (as Claude Dev) [S3]; GitHub repo created 2024-07-06 [S2]; earliest GitHub release listed v1.0.4 2024-07-28 [S33]. CLI: first Cline publish under the npm name `cline` was 1.0.0-nightly.1 on 2025-10-13 (the npm name previously belonged to an unrelated 2013 package) [S6]; "Cline CLI 2.0" announced 2026-02-13 [S20]. SDK announced 2026-05-13 [S21]. KANBAN repo created 2026-03-09 [S30].
- latest release (as-of 2026-08-21): EXT v4.1.12 (GitHub release 2026-08-21T22:39Z; Open VSX 4.1.12; VS Code Marketplace showed 4.1.11, updated 2026-08-21T05:44Z at fetch time) [S4][S7][S3]; CLI cli-v3.0.56 (2026-08-21T05:03Z; npm latest 3.0.56, nightly tag also published) [S4][S6]; SDK sdk/sdk/v0.0.77 (2026-08-21) [S4]; DESKTOP desktop-v0.0.15 (2026-08-21) and v0.0.16-beta.1 prerelease same day [S4][S31]. Homebrew formula `cline` at 3.0.3 [S9].
- what it is:
  - Form factors: EXT for VS Code, Cursor, Windsurf, VSCodium, Antigravity (Open VSX) [S11]; JB plugin (closed source) [S1]; CLI with interactive TUI and headless/JSON mode [S12]; ACP server mode (`cline --acp`) for Zed, JetBrains AI Assistant, Neovim, Emacs and other ACP clients [S15]; KANBAN web task board running parallel agents in git worktrees (research preview) [S16]; DESKTOP macOS app (v0.0.x, "renamed from Cline Code") [S31]; SDK (TypeScript/Node 22+) exposing the same agent core [S17]; CLOUD: Cline account with credits, ClinePass subscription, OpenAI-compatible Cline API, Enterprise admin console [S13][S14][S18]; CLI connectors for Telegram, Slack, Discord, Google Chat, WhatsApp, Linear; scheduled (cron) agents; agent teams [S1][S12].
  - Models: BYO provider — Anthropic, OpenAI, Google, OpenRouter, Vercel AI Gateway, AWS Bedrock, Azure, GCP Vertex, Cerebras, Groq, Ollama, LM Studio, any OpenAI-compatible API [S1]; plus hosted "Cline (usage-billing)" credits across "100+ models" with rotating free models [S13][S29]; ClinePass $9.99/mo flat subscription for a curated set of open-weight models (GLM, Kimi, DeepSeek, MiMo, MiniMax, Qwen) [S14]; a Claude Pro/Max subscription can be used via the "Claude Code" provider (requires Claude CLI installed) and a ChatGPT subscription via `openai-codex` [S28][S12] (as-of 2026-08-21).
  - Pricing: software free/open source; inference pay-as-you-go via own keys or Cline credits; ClinePass $9.99/mo; Enterprise custom (contact sales) [S10][S14]. Enterprise launch post (2025-10-20): Teams tier free to end-2025, then free up to 10 users, then $20/user/month; Enterprise custom [S22].
  - Install: VS Code Marketplace / Open VSX / JetBrains Marketplace (plugin 28247); `npm install -g cline` (Node 20+, platform binaries via optional deps); `brew install cline`; `npx kanban` or `npm i -g kanban`; `npm install @cline/sdk` (Node 22+) [S1][S11][S9][S17].
  - Default autonomy: docs overview — every action requires explicit approval [S10]; per-category Auto Approve toggles (read/edit project files, safe/all commands, browser, MCP) and a "YOLO mode" that approves everything [S19]; CLI `--auto-approve true` / `-y` for unattended runs [S12][S20]; ACP: nothing auto-approved by default [S15]; `CLINE_COMMAND_PERMISSIONS` allow/deny shell policy and `CLINE_SANDBOX` env var (CLI) [S18]; Plan mode is read-only (see section 3).
  - Repo language: TypeScript [S2].

## 2. Adoption evidence

| metric / claim | value | as-of | source | type |
|---|---|---|---|---|
| GitHub stars (cline/cline) | 66,615 | 2026-08-21 | [S2] | independently observable |
| GitHub forks | 7,179 | 2026-08-21 | [S2] | independently observable |
| GitHub watchers (subscribers) | 282 | 2026-08-21 | [S2] | independently observable |
| GitHub open issues | 1,060 | 2026-08-21 | [S2] | independently observable |
| GitHub issues ever filed (search API) | 4,397 | 2026-08-21 | [S2] | independently observable |
| GitHub contributors (incl. anonymous) | 321 | 2026-08-21 | [S2] | independently observable |
| Commits, last 90 days (since 2026-05-23) | 1,113 | 2026-08-21 | [S2] | independently observable |
| GitHub releases (all surfaces, total) | 382; the 100 most recent span 2026-06-09 to 2026-08-21 (multiple per day across EXT/CLI/SDK/DESKTOP) | 2026-08-21 | [S2][S4] | independently observable |
| VS Code Marketplace installs (EXT) | 5,054,611 installs; 312 ratings, avg 4.06; updateCount 68,191,279 | 2026-08-21 | [S3] | independently observable |
| Open VSX downloads (EXT) | 6,068,974; 12 reviews, avg 3.67 | 2026-08-21 | [S7] | independently observable |
| JetBrains Marketplace downloads (JB, plugin 28247) | 683,776 | 2026-08-21 | [S8] | independently observable |
| npm weekly / monthly downloads, `cline` (CLI) | 74,481 (2026-08-14..20) / 507,713 (2026-07-22..08-20) | 2026-08-20 | [S6b] | independently observable |
| npm weekly / monthly, `@cline/sdk` | 73,381 / 462,990 | 2026-08-20 | [S6b] | independently observable |
| npm weekly / monthly, `@cline/core` | 78,574 / 503,152 | 2026-08-20 | [S6b] | independently observable |
| npm weekly / monthly, `kanban` | 1,131 / 6,197 | 2026-08-20 | [S6b] | independently observable |
| Homebrew formula `cline` installs 30d / 90d / 365d | 100 / 342 / 1,632 | 2026-08-21 | [S9] | independently observable |
| cline/kanban stars / forks | 1,269 / 300 (created 2026-03-09) | 2026-08-21 | [S30] | independently observable |
| "700,000 downloads" in VS Code | at MCP Marketplace launch | 2025-02-19 | [S23] | maker-claimed |
| "1,000,000 installs" | milestone post | 2025-03-22 | [S25] | maker-claimed |
| Installs / stars / X followers / Discord | 2.7M installs (VS Marketplace + Open VSX), 48k GitHub stars, 48k X followers, 20k Discord members | 2025-07-31 | [S26] | maker-claimed |
| Installs | "over 3.8 million" | 2025-11-04 | [S27] | maker-claimed |
| GitHub Octoverse 2025 ranking | "fastest growing AI-focused open source project", 4,704% YoY contributor growth, #2 fastest-growing project overall (maker citing GitHub's report) | 2025-11-04 | [S27] | third-party (GitHub), repeated by maker |
| Developers | "5+ million developers" | 2026-02-13 | [S20] | maker-claimed |
| Installs / stars (CoreWeave partnership release) | "over 5 million installations", 58,000 stars | 2026-03 (see section 6 on date) | [S36] | maker-claimed (joint press release) |
| Developers | "over 7 million developers" | 2026-05-13 | [S21] | maker-claimed |
| Installs / developers (homepage) | "8.0M+ installs across all platforms"; "Trusted by 8M+ developers"; 66.6k stars; 4.1/5 from 312 reviews | 2026-08-21 | [S32] | maker-claimed (stars/reviews independently observable) |
| Enterprise docs | "the coding agent millions of developers trust" | 2026-08-21 | [S18b] | maker-claimed |
| Public customers / logos | homepage: Samsung, Salesforce, Oracle, Amazon, LG, Globant, Microsoft, eBay, Visa, IBM; enterprise page adds Credit Karma, Lockheed Martin, Plaid, Reddit, Roche, Sony; enterprise launch post: Salesforce (Agentforce "built using Cline's architecture"), Samsung, SAP, Oracle "tens of thousands of developers"; funding post: SAP, Samsung, Fortune 100 | 2026-08-21 / 2025-10-20 / 2025-07-31 | [S32][S34][S22][S26] | maker-claimed |
| Funding | $32M total (Seed + Series A), Series A led by Emergence Capital, Pace Capital also named as lead; 1984 Ventures, Essence VC, Cox Exponential; angels incl. Jared Friedman (YC), Eric Simons (Bolt.new), Logan Kilpatrick, Addy Osmani, Theo Browne | 2025-07-31 | [S26][S24][S35] | maker-claimed / press |
| Valuation | $110M (Series A) — appears in VC-news aggregators only; not in maker post | 2025-07/08 | [S35] | press / unverified |
| Press | Forbes: "Cline Has Raised $27 Million" (2025-07-31); GlobeNewswire release (2025-07-31); VC News Daily (2025-08-04); CoreWeave/W&B Inference partnership release (2026-03) | 2026-08-21 | [S35][S24][S36] | press |
| Community: Discord | 20k members (maker, 2025-07-31); current count not obtainable without joining | 2026-08-21 | [S26] | null (current) |
| Community: r/cline | exists (linked from README); subscriber count not obtainable (reddit.com fetch blocked) | 2026-08-21 | [S1] | null |
| Community: GitHub Discussions | enabled (has_discussions true); feature-requests category linked from README; volume null | 2026-08-21 | [S2][S1] | null (volume) |
| Benchmark: Terminal-Bench | maker claims 74.2% with Claude Opus 4.7 via the SDK harness (2026-05-13); no "Cline" row on the public tbench.ai Terminal-Bench 2.1 leaderboard (17 rows) | 2026-08-21 | [S21][S37] | maker-claimed; absent from public board |
| Benchmark: SWE-bench | null (not researched; no maker claim found) | — | — | null |
| Evals | maker open-sourced evals for open-weight agents (blog 2026-08-18); `evals/` dir in repo | 2026-08-21 | [S39][S5] | maker-claimed |
| Third-party: podcast | Latent Space episode "Cline: The Open Source Code Agent" with Saoud Rizwan and Nik Pash | n/d | [S40] | third-party |

## 3. Plugin interface (PRI-2925)

- mcp_support: **client** — connects to stdio, Streamable HTTP and legacy SSE servers; config `~/.cline/mcp.json` (CLI) or extension MCP settings JSON; `cline mcp` wizard; per-tool `autoApprove`; enterprise MCP allowlists (`allowedMCPServers`) [S41][S4]. First-party **MCP Marketplace** with one-click install from the extension (launched 2025-02-19; page says applies to IDE, CLI, SDK) [S23][S42]. README: Cline can "create custom tools on the fly" (i.e., author MCP servers) [S1]. No first-party MCP-server mode for Cline itself found (researched, absent). Evidence: https://docs.cline.bot/mcp/mcp-overview ; https://cline.bot/mcp-marketplace (as-of 2026-08-21)
- plugin_support: **True**, several kinds:
  1. MCP Marketplace (see above) [S42].
  2. Skills — `SKILL.md` directories with YAML frontmatter, progressive loading, slash-command trigger; locations `.cline/skills/`, `.clinerules/skills/`, `.claude/skills/` (project) and `~/.cline/skills/` (global) [S43].
  3. Rules — `.clinerules/` (primary), `.cursorrules`, `.windsurfrules`, `AGENTS.md` / `~/.agents/AGENTS.md` auto-detected; `/newrule` [S44].
  4. Plugins (SDK/CLI/KANBAN) — `AgentPlugin` TypeScript/JS modules bundling tools, hooks, slash commands, rules, events; installed via `cline plugin install` from file URL, git, npm, local path; `package.json` `cline.plugins` manifest; stored in `~/.cline/plugins/` or `.cline/plugins/`; docs warn "not applicable on VSCode and JetBrains Extension for now" [S45][S46]. Desktop v0.0.15 notes "consolidates plugins into marketplace" [S31].
  5. Workflows — global workflows dir `~/.cline/data/workflows/`; CLI 2.0 post mentions custom workflow slash commands [S18][S20].
  Evidence: https://docs.cline.bot/customization/plugins ; https://docs.cline.bot/sdk/plugins ; https://docs.cline.bot/customization/skills
- claude_code_plugin: **partial** — reads `.claude/skills/` as a project skills location [S43] and `AGENTS.md` [S44]; can use a Claude Pro/Max subscription as a model provider via the "Claude Code" provider [S28]. No support found for Claude Code plugin manifests (`.claude-plugin/plugin.json`), plugin marketplaces, `CLAUDE.md`, `.claude/agents`, or Claude Code hooks format (researched in docs; absent). The cline/cline repo itself contains `.claude`, `.codex`, `.agents`, `.cline`, `.clinerules` dirs (dogfooding) [S5].
- subagents: **True** — (a) `use_subagents` tool: parallel, read-only research subagents with separate context windows; cannot edit files, use browser/MCP, or nest; enabled by default across VS Code, JetBrains, CLI; experimental [S47]. (b) Agent Teams: coordinator + specialist agents with persistent task board and mailbox (`cline --team-name`, `/team`); SDK/CLI/KANBAN only, not EXT/JB [S48]. (c) SDK "subagents with independent models/tools/prompts" [S21]. Evidence: https://docs.cline.bot/features/subagents ; https://docs.cline.bot/cli/agent-teams
- hooks: **True** — (a) SDK/CLI plugin lifecycle hooks `beforeRun`, `afterRun`, `beforeModel`, `afterModel`, `beforeTool`, `afterTool`, `onEvent`; stages incl. `session_start`, `run_start`, `tool_call_before`, `tool_call_after`, `run_end`, `error`; policies blocking/async, fail_open/fail_closed; `beforeTool` can block a call [S46][S49]. (b) CLI "approval hooks" that gate tool calls with custom scripts (cline.bot/cli) [S12b]; hooks dirs `~/.cline/hooks/`, `.cline/hooks/`, `~/Documents/Cline/Hooks/`, `CLINE_HOOKS_DIR` [S18]. (c) EXT: script hooks introduced v3.36 (2025-11-06): `PreToolUse`, `PostToolUse`, `UserPromptSubmit`, `TaskStart`, `TaskResume`, `TaskCancel` in `.clinerules/hooks/` or `~/Documents/Cline/Rules/Hooks/`, macOS/Linux only, JSON over stdin, can cancel or inject context [S50]; the current docs "Hooks" page now just points to SDK Plugins [S51]. Evidence: https://docs.cline.bot/sdk/plugins ; https://cline.bot/blog/cline-v3-36-hooks
- plan_mode: **True** — Plan & Act modes; in Plan mode Cline reads/searches/discusses but "cannot modify any files or execute commands"; separate models per mode; Tab toggles in CLI TUI; `cline -p` plan-first headless; `/deep-planning` command; mode switch exposed over ACP [S52][S20][S15]. Evidence: https://docs.cline.bot/core-workflows/plan-and-act
- plugin_docs_url: https://docs.cline.bot/customization/plugins (SDK API: https://docs.cline.bot/sdk/plugins ; skills: https://docs.cline.bot/customization/skills ; MCP marketplace: https://cline.bot/mcp-marketplace)
- config_docs_url: https://docs.cline.bot/getting-started/config (CLI: https://docs.cline.bot/cli/configuration ; auto-approve: https://docs.cline.bot/features/auto-approve)
- ACP support: **yes, first-party** — `cline --acp` (CLI acts as ACP agent over stdio) for Zed, JetBrains AI Assistant, Neovim (CodeCompanion `cline_cli` adapter, avante, agentic.nvim), Emacs agent-shell, other ACP clients; supports sign-in from client, Plan/Act, model/provider switching, permission prompts, session resume, images [S15] (as-of 2026-08-21). ACP added with CLI 2.0 (2026-02-13) [S20].
- SDK: **yes** — `@cline/sdk` (re-exports `@cline/core`, `@cline/agents`, `@cline/llms`, `@cline/shared`), TypeScript, Node 22+, Apache-2.0, "the same harness used in the Cline IDE extensions and CLI"; hub-spoke architecture (local daemon `cline-hub`, default 127.0.0.1:25463) [S17][S18][S5]. Also: OpenAI-compatible Cline API (api.cline.bot) [S13][S14]; Enterprise REST API [S18b]; `cline/sdk-skill` for coding agents [S17].

## 4. Claimed differentiation (raw material for PRI-2927)

- tagline (README, verbatim-short): "The open source coding agent in your IDE and terminal." — https://github.com/cline/cline [S1]
- tagline (homepage): "The Open Coding Agent" — https://cline.bot [S32]
- docs one-liner: "AI-powered coding agent for complex work" / "Read files, write code, run commands, all with your approval." — https://docs.cline.bot/cline-overview [S10]
- marketplace blurb: autonomous coding agent in your IDE "with your permission every step of the way" — https://marketplace.visualstudio.com/items?itemName=saoudrizwan.claude-dev [S3]
- maker claims (paraphrased):
  1. Open source (Apache 2.0), auditable; cited as GitHub Octoverse 2025's fastest-growing AI OSS project [S1][S27].
  2. Model-agnostic: "Works With Every Model", no provider lock-in; 100+ models via Cline credits; open-weight models via ClinePass [S1][S13][S14][S26].
  3. Human-in-the-loop by default: every edit/command needs approval; Plan/Act separation; checkpoints and one-click undo; opt-in auto-approve/YOLO [S1][S10][S19].
  4. Client-side and private: code stays in your environment, no indexing, no training on your data; bring your own inference at negotiated rates, "no markup" [S18b][S34].
  5. One engine, many surfaces: the SDK is the same harness behind CLI, Kanban, VS Code, JetBrains; sessions persist across surfaces [S17][S21].
  6. Orchestration: multi-agent teams, read-only subagents, scheduled (cron) agents, messaging connectors, headless CI/CD, Kanban parallel worktrees, ACP in any editor [S1][S12][S16][S15].
  7. Extensible: MCP (early adopter) + first-party MCP Marketplace, rules, skills, plugins and lifecycle hooks [S1][S23][S25][S49].
  8. Enterprise governance: SSO/SCIM, RBAC, model/tool controls, remote config, OpenTelemetry export; "Fortune 100" customers; Salesforce/Samsung/SAP/Oracle named [S34][S22][S26].
  9. Performance claim: "best-in-class agent harness", 74.2% Terminal-Bench with Opus 4.7, lower token cost vs previous CLI [S21].
- audience: individual developers (free tier, "Free for individual developers") [S10b]; "engineering teams" and enterprise "platform teams" needing central control [S18b][S34]; developers building their own agents/integrations (SDK) [S17]; ACP users of Zed/JetBrains/Neovim/Emacs [S15].

## 5. Company & contact targets (PRI-2929) — company-level only

- legal name: Cline Bot Inc. [S1][S8]
- HQ: San Francisco, CA per funding press coverage [S24]; JetBrains vendor record: 1007 N Orange St, Wilmington, DE (registered-agent style address) [S8]
- size: null (no public headcount found on company pages; careers page gives none) [S53]
- funding stage: Series A — $32M total seed + Series A announced 2025-07-31 [S26]
- publicly named leadership (only as named by the company itself):
  - Saoud Rizwan — Founder / CEO (byline and self-description in the funding post on cline.bot; quoted as Founder in GlobeNewswire/VC News Daily coverage) [S26][S24]
  - Nik Pash — referred to as "Head of AI" in search snippets and the Latent Space episode; the cline.bot author page (/blog/author/pash) returned "Author Not Found" on 2026-08-21, so the title is **not verified on a company page** [S40][S54]
  - Blog bylines on cline.bot (titles not shown on the pages fetched): Nick Baumann (2025-03, 2025-10, 2025-11 posts), Juan Pablo Flores (2025-11, 2026-02), Renee Huang (2026-05 SDK post), Etisha Garg (2026-06, 2026-08), Ara Khan (2026-08; also an npm maintainer of `cline`), Tony Loehr [S25][S22][S50][S27][S20][S21][S49][S39][S6]
  - CTO / head of product / DevRel lead / head of partnerships: none named on company pages found (researched, absent) [S53][S32]
- contact: enterprise sales via https://cline.bot/enterprise ("contact sales" on pricing page) [S10b][S34]; vendor support address shown on JetBrains Marketplace: support@cline.bot [S8]; community Discord https://discord.gg/cline [S1]

## 6. Open questions / conflicts

- Existing census `first_released: "2024-07-06"` — that is the repo creation date; first Marketplace publish was 2024-07-10 (as "Claude Dev") [S3][S2].
- Existing census `current_release: "2026-08-20"` — EXT v4.1.12 / CLI 3.0.56 / SDK 0.0.77 / Desktop 0.0.15 all released 2026-08-21 [S4].
- Existing census `stars: null` — 66,615 on 2026-08-21 [S2].
- Existing census `maker: "cline"` — company is Cline Bot Inc. [S1].
- Existing census `platforms: ["IDE","CLI"]` — also web (Kanban), desktop app (macOS), SDK, ACP-in-editor, messaging connectors, hosted API [S10][S16][S31][S15].
- Existing census `pricing: "Free / open source (BYOK to providers)"` — incomplete: also Cline credits (pay-as-you-go), ClinePass $9.99/mo, Enterprise custom; Teams $20/user/month after 10 users per 2025-10-20 post [S13][S14][S10b][S22].
- Existing census `install_method` lists `npm i -g kanban`; docs say `npx kanban` (README shows `npm i -g kanban`) — both valid; Homebrew formula `cline` also exists [S1][S11][S9].
- Existing census `plugin_docs_url` / `config_docs_url` / `claude_code_plugin`: null — filled above (claude_code_plugin = partial).
- Existing census `subagents: True` — true, but built-in subagents are read-only research agents; writing delegation is via Agent Teams, which are CLI/SDK/Kanban-only [S47][S48].
- Existing census `hooks: True` — true, but surface-dependent: SDK/CLI plugin hooks are current; EXT script hooks (v3.36) are macOS/Linux only and the docs page now redirects to SDK plugins [S50][S51].
- Existing census `source_available: True` / `license: Apache-2.0` — accurate for EXT/CLI/SDK/Kanban; JetBrains plugin is closed; Desktop app source location not found; suggest "partial" [S1][S5].
- Plugins surface conflict: docs say plugins are "not applicable on VSCode and JetBrains Extension for now" [S45], while the 2026-06-15 blog says a plugin "can be reused across the CLI, VS Code, JetBrains, and the SDK" [S49].
- JetBrains link conflict: docs overview links plugin id 27189, which the JetBrains API resolves to an unrelated "Private Test PHP Course" plugin; README and install docs link 28247 (the real Cline plugin, 683,776 downloads) [S10][S1][S8].
- "67k GitHub stars" appears in 2025-02 and 2025-03 blog posts; the repo had ~48k stars in 2025-07 per the funding post, so the 67k figure is the site-wide header badge rendered on old posts, not a dated statistic [S23][S25][S26].
- Homepage "8.0M+ installs across all platforms" vs observable marketplace counters (5.05M VS Code installs + 6.07M Open VSX downloads + 0.68M JetBrains downloads = 11.8M) — counting method unknown (Open VSX counts downloads, not installs); "8M+ developers" = "8M+ installs" on the same page [S32][S3][S7][S8].
- $110M valuation appears only in VC-news aggregators (vcnewsdaily/traded) — not in the maker's post [S35][S26].
- CoreWeave partnership press release: fetched page text read "March 17, 2025", but it cites 5M installs and 58k stars, which match 2026 figures (Cline had 48k stars in 2025-07); search summary dated it March 2026 — treat as 2026-03, date unverified [S36].
- Terminal-Bench 74.2% claim is maker-stated; no Cline entry on the public leaderboard [S21][S37].
- Unreachable: GlobeNewswire release (timeout), finsmes (403), reddit.com (blocked), cline.bot/blog/author/pash (404). Discord current member count not obtainable.
- Desktop app: releases exist in cline/cline ("renamed from Cline Code") but no `apps/desktop` dir found; whether source is public is unverified [S31][S5].
- Leadership titles beyond Founder/CEO are not stated on company pages; Nik Pash's "Head of AI" title is from third-party/search snippets only.

## 7. Sources

1. [S1] https://github.com/cline/cline (README via raw-cline/readme.md) — tagline, products, providers, license, JetBrains closed
2. [S2] https://api.github.com/repos/cline/cline (+ contributors, commits?since, search/issues Link headers) — stars, forks, dates, counts
3. [S3] https://marketplace.visualstudio.com/_apis/public/gallery/extensionquery (saoudrizwan.claude-dev, raw-cline/vscode.json) — installs, ratings, publish date
4. [S4] https://api.github.com/repos/cline/cline/releases (+ /tags/cli-v3.0.56, /tags/desktop-v0.0.15) — latest releases, cadence
5. [S5] https://api.github.com/repos/cline/cline/contents/ and /contents/apps — repo layout
6. [S6] https://registry.npmjs.org/cline (raw-cline/npm_cline.json) — versions, first Cline publish, license, maintainers; [S6b] https://api.npmjs.org/downloads/point/last-week|last-month/{cline,@cline/sdk,@cline/core,kanban} — downloads
7. [S7] https://open-vsx.org/api/saoudrizwan/claude-dev — downloads, version, license
8. [S8] https://plugins.jetbrains.com/api/plugins/28247 (and /27189) — JB downloads, vendor record
9. [S9] https://formulae.brew.sh/api/formula/cline.json — Homebrew installs, version
10. [S10] https://docs.cline.bot/cline-overview — what it is, surfaces, approval default; [S10b] https://cline.bot/pricing — Open Source free / Enterprise custom
11. [S11] https://docs.cline.bot/getting-started/installing-cline — install paths
12. [S12] https://docs.cline.bot/usage/cli-overview and apps/cli/README.md — CLI headless, auto-approve, providers; [S12b] https://cline.bot/cli — approval hooks, teams, scheduling, connectors
13. [S13] https://docs.cline.bot/getting-started/cline-provider — Cline credits, 100+ models, free models
14. [S14] https://docs.cline.bot/getting-started/clinepass — $9.99/mo, models, Cline API
15. [S15] https://docs.cline.bot/usage/acp — ACP mode, clients, defaults
16. [S16] https://docs.cline.bot/usage/kanban — Kanban preview, worktrees
17. [S17] https://docs.cline.bot/sdk/overview — SDK packages, "same harness", Node 22
18. [S18] https://docs.cline.bot/getting-started/config and https://docs.cline.bot/cli/configuration — config dirs, hooks/plugins dirs, env vars, sandbox, command permissions; [S18b] https://docs.cline.bot/enterprise-solutions/overview — enterprise claims, "millions of developers"
19. [S19] https://docs.cline.bot/features/auto-approve — auto-approve categories, YOLO
20. [S20] https://cline.bot/blog/introducing-cline-cli-2-0 — CLI 2.0 (2026-02-13), ACP, 5M+ developers
21. [S21] https://cline.bot/blog/introducing-cline-sdk-the-upgraded-agent-runtime — SDK (2026-05-13), 7M+ developers, Terminal-Bench claim
22. [S22] https://cline.bot/blog/introducing-cline-for-enterprise — Enterprise launch (2025-10-20), pricing, customers
23. [S23] https://cline.bot/blog/introducing-the-mcp-marketplace-clines-new-app-store — MCP Marketplace (2025-02-19), 700k downloads
24. [S24] https://www.vcnewsdaily.com/cline/venture-capital-funding/mfrldncjlg — HQ San Francisco, investors (2025-08-04)
25. [S25] https://cline.bot/blog/1-000-000-installs-and-our-all-in-bet-on-the-future-of-software-engineering — 1M installs (2025-03-22)
26. [S26] https://cline.bot/blog/cline-raises-32m-series-a-and-seed-funding-building-the-open-source-ai-coding-agent-that-enterprises-trust — $32M, investors, 2.7M installs, 48k stars, 20k Discord (2025-07-31)
27. [S27] https://cline.bot/blog/cline-the-fastest-growing-ai-open-source-project-on-github-in-2025-thanks-to-you — Octoverse claim, 3.8M installs (2025-11-04)
28. [S28] https://docs.cline.bot/provider-config/anthropic — Claude Code subscription provider
29. [S29] https://docs.cline.bot/getting-started/free-models — rotating free models
30. [S30] https://api.github.com/repos/cline/kanban — Kanban stars, created date
31. [S31] https://api.github.com/repos/cline/cline/releases/tags/desktop-v0.0.15 — Desktop app, rename, macOS
32. [S32] https://cline.bot — homepage claims, 8.0M+ installs, logos
33. [S33] https://api.github.com/repos/cline/cline/releases?per_page=1&page=382 — earliest release v1.0.4 (2024-07-28)
34. [S34] https://cline.bot/enterprise — enterprise claims, logos
35. [S35] web search results: Forbes ($27M), GlobeNewswire, traded.co/vcnewsdaily ($110M valuation) — funding press
36. [S36] https://www.barchart.com/story/news/794053/cline-selects-coreweave-to-power-high-performance-autonomous-engineering — CoreWeave release, 5M installs, 58k stars
37. [S37] https://www.tbench.ai/leaderboard/terminal-bench/2.1 — no Cline row
38. [S38] web search results on "Claude Dev" rename (Oct 2024) — rename date (third-party)
39. [S39] https://cline.bot/blog (index) — post list incl. evals post 2026-08-18
40. [S40] https://www.latent.space/p/cline (via search) — podcast with Saoud Rizwan and Nik Pash
41. [S41] https://docs.cline.bot/mcp/mcp-overview — MCP client details
42. [S42] https://cline.bot/mcp-marketplace — marketplace page
43. [S43] https://docs.cline.bot/customization/skills — skills format and locations incl. .claude/skills
44. [S44] https://docs.cline.bot/customization/cline-rules — rule formats incl. AGENTS.md, .cursorrules
45. [S45] https://docs.cline.bot/customization/plugins — plugin install, manifest, surface warning
46. [S46] https://docs.cline.bot/sdk/plugins — AgentPlugin, hooks, stages, policies
47. [S47] https://docs.cline.bot/features/subagents — read-only subagents
48. [S48] https://docs.cline.bot/cli/agent-teams — teams, surface warning
49. [S49] https://cline.bot/blog/extend-cline-with-plugins-and-hooks — plugins/hooks post (2026-06-15)
50. [S50] https://cline.bot/blog/cline-v3-36-hooks — EXT script hooks (2025-11-06)
51. [S51] https://docs.cline.bot/customization/hooks — redirects to SDK plugins
52. [S52] https://docs.cline.bot/core-workflows/plan-and-act — Plan/Act
53. [S53] https://cline.bot/join-us — careers page (no headcount/leadership)
54. [S54] https://cline.bot/blog/author/pash — 404 "Author Not Found"
55. https://docs.cline.bot/llms.txt — docs index; https://docs.cline.bot/core-workflows/using-commands — slash commands

## Inclusion check (Jesse's test)

**Yes** — Cline runs its own agentic loop (the `@cline/core` / `@cline/agents` harness: reads/edits files, runs commands, browser, MCP tools, iterates with approval) across its extension, CLI, SDK and Kanban surfaces; it is not a wrapper around another vendor's agent [S17][S10][S1].
