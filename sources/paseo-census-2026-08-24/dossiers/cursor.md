# Dossier: Cursor (census_slug: cursor)

Compiled 2026-08-21. Facts only. Null convention: "null = not researched"; "False/none = researched and absent". Each non-obvious fact carries a source [Sn] (see section 7) and an as-of date. Cursor is primarily an IDE; this dossier treats the product as a harness with three surfaces and tags facts by surface: **IDE** (desktop app agent), **CLI** (`agent` / legacy `cursor-agent`, the surface Paseo drives via `cursor-agent acp`), **Cloud** (cloud agents, formerly background agents; plus SDK/API). Note: docs.cursor.com/en/cli/overview (the roster URL) now 308-redirects to https://cursor.com/docs; CLI docs live at https://cursor.com/docs/cli/overview [S1] (as-of 2026-08-21).

## 1. Identity

- name: Cursor (product); CLI surface shipped as "Cursor CLI" / "Cursor Agent CLI"; binary `agent`, legacy symlink `cursor-agent` [S2][S3]
- maker: Anysphere, Inc. (company; d/b/a Cursor); since 2026-08-14 a wholly owned subsidiary of SpaceX under the "SpaceXAI" division [S20][S21][S22]; HQ San Francisco, CA, USA (ToS mailing address 2261 Market Street STE 86466, San Francisco; governing law Texas) [S23] (as-of 2026-08-21)
- product URL: https://cursor.com ; docs https://cursor.com/docs ; CLI docs https://cursor.com/docs/cli/overview [S1]
- repo URL: https://github.com/cursor/cursor (getcursor/cursor redirects here) — contains only README.md, SECURITY.md, .github (issue templates); no source code, no releases [S4] (as-of 2026-08-21)
- license: proprietary. GitHub API license: null [S4]; ToS grants "a limited right to access and use the Service", Anysphere retains all right, title and interest [S23] (ToS last updated 2026-08-13)
- open source? False. source_available: False (researched and absent) — neither IDE, CLI, nor cloud agent source is published; the CLI is a downloaded binary tarball (downloads.cursor.com/lab/<version>/…/agent-cli-package.tar.gz) [S4][S5][S3]. Exception: Cursor open-sourced an MoE training megakernel ("Mixture-of-Kittens", 2026-08-04) — research code, not the harness [S17].
- first public release:
  - IDE: March 2023 (GitHub repo cursor/cursor created 2023-03-12; third-party histories say "launched March 2023") [S4][S24] (repo date independently observable; month from press)
  - CLI: 2025-08-07, "Cursor CLI — Beta Available Now" forum announcement; install `curl https://cursor.com/install -fsS | bash`; binary then `cursor-agent` [S25]
  - Cloud agents: "Background Agents" preceded; Cloud Agents launch dated Feb 2026 in press on the revenue run-rate [S26] (press)
- latest release:
  - IDE: Homebrew cask `cursor` version 3.17.8 (as-of 2026-08-21) [S5]; last numbered changelog entry visible is 3.11 (2026-07-10); newest dated changelog entries are unnumbered (2026-08-19 "Cloud Agents and Cursor Harness Improvements") [S6][S7]
  - CLI: version 2026.08.11-e8db854 (install script and Homebrew cask `cursor-cli`) [S3][S5]; CLI changelog latest entry 2026-08-11 [S8] (as-of 2026-08-21)
- what it is:
  - Form factors: IDE (VS Code-fork desktop app, macOS/Windows/Linux); terminal CLI (`agent`, macOS/Linux/WSL/Windows) with interactive, print/headless and ACP-server modes; Cloud agents on Cursor-hosted VMs triggered from desktop, web (cursor.com/agents), iOS app, Android PWA, iPad app, Slack, GitHub/Bitbucket PR comments, Linear, API; SDK (TypeScript `@cursor/sdk`, Python `cursor-sdk`) with local and cloud runtimes; JetBrains via ACP ("AI Assistant" plugin); Bugbot (PR review), Security Agents, Automations; "Origin" code hosting (early beta 2026-08-17) [S1][S2][S9][S10][S11][S12][S6] (as-of 2026-08-21)
  - Models: multi-vendor via Cursor's hosted inference — first-party Cursor models (Grok 4.6/4.5 incl. Fast variants, Composer 2.5/2.5 Fast) plus OpenAI (GPT-5 … GPT-5.6 Luna/Sol/Terra, Codex variants), Anthropic (Claude 4–4.7 Opus, Sonnet 4–4.6, Sonnet 5, Fable 5, Haiku 4.5), Google (Gemini 2.5–3.7 Flash, 3/3.1 Pro), Moonshot (Kimi K2.7 Code, K3), Z.ai (GLM 5.2); "Auto" routed by Cursor Router (Cost/Balance/Intelligence) [S13][S14]; SDK inference "goes through Cursor's hosted models regardless of runtime" [S11]. BYO API keys: docs mention OpenAI/Anthropic/Google/Azure key compatibility [S13] — details null (not fully researched).
  - Pricing: Hobby free; Pro $20/mo ($20 of "other models" credit + generous first-party-model usage); Pro+ $60/mo; Ultra $200/mo; Start (India) ₹649/mo; Teams Standard $40/user/mo; Teams Premium $40/user/mo + 5x limits; Enterprise custom. Teams add $0.25/M-token "Cursor Token Rate" on third-party models. Cloud agents charged at model API pricing, paid plans only [S15][S14][S10] (as-of 2026-08-21)
  - Install: IDE download from cursor.com (Homebrew cask `cursor`); CLI `curl https://cursor.com/install -fsS | bash` (macOS/Linux/WSL), `irm 'https://cursor.com/install?win32=true' | iex` (Windows); installs to ~/.local/share/cursor-agent and symlinks ~/.local/bin/agent and ~/.local/bin/cursor-agent; Homebrew cask `cursor-cli` (community-maintained cask, binary `cursor-agent`); auto-updates, `agent update` [S2][S3][S5]
  - Default autonomy (CLI): interactive mode asks to approve (y/n) before running terminal commands; sandbox modes (`/sandbox`, `--sandbox`), three-mode approval system "Run Everything / Auto-Run / Ask" (Jan 2026); print mode proposes changes only unless `--force`/`--yolo` (auto-apply edits, headless trust) [S1][S16][S8]. IDE: agent "suggest edits to files and apply them automatically" and runs terminal commands; Agent Review surface; consent workflow details not stated on the overview page [S9]. Cloud: runs autonomously on isolated VMs, opens PRs [S10].

## 2. Adoption evidence

| metric / claim | value | as-of | source | type |
|---|---|---|---|---|
| GitHub stars, cursor/cursor (issue-tracker repo, no code) | 33,158 | 2026-08-21 | [S4] | independently observable |
| GitHub forks / watchers / open issues | 2,286 / 253 / 3 | 2026-08-21 | [S4] | independently observable |
| GitHub issues ever filed (search API) | 3,739 | 2026-08-21 | [S4] | independently observable |
| GitHub contributors (incl. anonymous) | 33 | 2026-08-21 | [S4] | independently observable |
| Commits, last 90 days (since 2026-05-23) | 0 (last push 2026-05-12) | 2026-08-21 | [S4] | independently observable |
| GitHub Discussions | not enabled | 2026-08-21 | [S4] | independently observable |
| Homebrew cask `cursor` installs 30d / 90d / 365d | 8,197 / 27,949 / 127,746 | 2026-08-21 | [S5] | independently observable |
| Homebrew cask `cursor-cli` installs 30d / 90d / 365d | 1,689 / 4,625 / 16,301 | 2026-08-21 | [S5] | independently observable |
| npm weekly downloads, @cursor/sdk (official SDK) | 492,537 (2026-08-14..20) | 2026-08-20 | [S27] | independently observable |
| PyPI downloads, cursor-sdk (official SDK) | 111,965 / week; 427,241 / month | 2026-08-21 | [S28] | independently observable |
| npm weekly downloads, `cursor-agent` (unofficial) / `cursor-agent-acp` (unofficial) | 147 / 75 | 2026-08-20 | [S27] | independently observable |
| Third-party ACP adapter repos (pre-date official `agent acp`) | blowmage/cursor-agent-acp-npm 125 stars; roshan-c/cursor-acp 15; konsumer/cursor-agent-acp 12 (created 2025-09-03) | 2026-08-21 | [S4] | independently observable |
| JetBrains marketplace: unofficial "Cursor CLI Terminal" plugin | 12,781 downloads; official JetBrains integration is via the JetBrains "AI Assistant" plugin (id 22282) using ACP — no Cursor-published plugin count | 2026-08-21 | [S29][S12] | independently observable |
| Annualized revenue | >$500M | 2025-06-06 | [S30] | maker-claimed |
| Annualized revenue | >$1B; "millions of developers"; team >300 | 2025-11-13 | [S31] | maker-claimed |
| Annualized revenue | $2B (Feb 2026) -> $3B (late Apr 2026) -> >$4B (early Jun 2026); ~75% enterprise | 2026-06 | [S26][S32] | press / aggregator (Bloomberg cited by Wikipedia for $3B; Dealroom for $4B); no Cursor post found stating these |
| Fortune 500 penetration | "over half" (2025-06-06); 64% (enterprise page); 70% (AIUC-1 post, 2026-08-13) | 2026-08-21 | [S30][S33][S34] | maker-claimed (figures differ by page/date) |
| Enterprises deployed | "50,000+" | 2026-08-21 | [S33] | maker-claimed |
| Lines of code written daily with Cursor | "100M+" | 2026-08-21 | [S33] | maker-claimed |
| Public customers / logos | Salesforce, Fox, PayPal, Stripe, NVIDIA (40,000 engineers), Coinbase (2,400+ devs; 75% of PRs by agents; 55% more PRs/engineer), Rippling (500+ engineers), JetBrains, Sentry, Vercel, Wayfair, Faire, Brex (>70% of engineers), monday.com, Mercado Libre, eBay, Decagon, OnePay, Optiver, Trimble (800+ engineers), Upwork, Activision, Datadog, Sierra, Uber, Adobe, OpenAI (testimonial), Y Combinator (>80% of batch), Eureka Labs, shadcn | 2026-08-21 | [S35][S33][S36][S37][S30] | maker-claimed |
| Funding | Seed $8M (2023-10, OpenAI Startup Fund); Series A $60M at $400M (2024); Series B (2025-01-16); Series C $900M at $9.9B (2025-06-06, Thrive/Accel/a16z/DST); Series D $2.3B at $29.3B post (2025-11-13, Accel/Coatue co-led; NVIDIA, Google new) | 2025-11-13 | [S30][S31][S24] | maker-claimed (C, D) / press (seed, A) |
| Acquisition (of Cursor) | SpaceX acquired Anysphere, all-stock, $60B; agreed 2026-06-16; closed 2026-08-14 (389,289,254 SpaceX Class A shares; SEC 8-K); Cursor now under SpaceXAI | 2026-08-14 | [S20][S21][S22][S24] | maker-claimed (close) + SEC/press |
| Acquisitions (by Cursor) | Supermaven (2024-11); Koala (2025-07); Graphite (2025-12, >$290M per press); Firetiger (2026-08-13) | 2026-08-21 | [S24][S17] | press / maker blog |
| Community: Discord | 38,612 members (search-result snippet of discord.com/invite/cursor) | 2026-08-21 | [S38] | independently observable (snippet; not verified in-app) |
| Community: forum.cursor.com | ~103K members (third-party index) | 2026-08-21 | [S38] | third-party |
| Community: r/cursor subscribers | null (reddit about.json blocked) | — | — | unreachable |
| Community program | 300+ ambassadors, 800+ events, 250+ cities, 80+ countries | 2026-08-21 | [S39] | maker-claimed |
| Marketplace | "100+" plugins (Vercel, Stripe, AWS, Google, Slack, Notion, GitHub, MongoDB, Shopify, Datadog, HubSpot, Salesforce, Azure, Twilio…); no install counts shown | 2026-08-21 | [S40] | maker-published |
| Benchmark: Terminal-Bench 2.1 | #4 Cursor CLI + Grok 4.5, 79.3% ± 1.5% (2026-07-09) | 2026-08-21 | [S41] | independently observable (third-party leaderboard) |
| Certification | AIUC-1 (Schellman), covers IDE agents and cloud agents; SOC 2 Type II | 2026-08-13 | [S34][S33] | maker-claimed |
| Press | Reuters/Bloomberg/TechCrunch on funding and SpaceX deal; Fortune profile of CEO | 2026-08 | [S24][S22][S42] | press |

## 3. Plugin interface (PRI-2925)

- mcp_support: **client** (IDE, CLI, Cloud, ACP mode). Transports stdio, SSE, streamable HTTP; config `.cursor/mcp.json` (project) and `~/.cursor/mcp.json` (user); supports tools, prompts, resources, roots, elicitation, MCP Apps UI; OAuth; one-click install from marketplace; team/enterprise MCP allowlists. CLI "automatically detect and respect your mcp.json". ACP mode supports project/user MCP servers but not dashboard-configured team MCP servers. No first-party MCP-server mode documented (researched, absent) [S42-MCP][S16][S43] (as-of 2026-08-21). Evidence: https://cursor.com/docs/mcp
- plugin_support: **True** — Cursor plugins bundle rules, skills, agents (subagents), commands, MCP servers, hooks; manifest `.cursor-plugin/plugin.json`; also accepts "Agent Plugins" open-standard layout (root `plugin.json`); official marketplace cursor.com/marketplace (manually reviewed, must be open source), community cursor.directory, team marketplaces (Teams/Enterprise) with Default Off / Default On / Required install modes; CLI got plugins Mar 2026 and marketplace sources by git URL May 2026 [S44][S8] (as-of 2026-08-21). Evidence: https://cursor.com/docs/plugins
- claude_code_plugin: **partial** — reads `CLAUDE.md` (CLI rules), `.claude/skills/` and `~/.claude/skills/` (legacy-compat skill dirs), `.claude/agents/` (subagent dir compat); no documented support for `.claude-plugin/plugin.json` or Claude Code `marketplace.json` (researched, absent) [S16][S45][S46][S44] (as-of 2026-08-21).
- subagents: **True** — markdown+YAML files in `.cursor/agents/` or `~/.cursor/agents/` (also `.claude/agents/`, `.codex/agents/`); built-ins Explore, Bash, Browser; foreground/background; parallel via concurrent Task calls; cloud subagents on dedicated VMs (`/in-cloud`); isolated git worktrees; child subagents allowed one level deep; fields name/description/model/readonly/is_background; available in editor, CLI, Cloud; CLI subagents shipped Mar 2026 [S46][S8]. Evidence: https://cursor.com/docs/subagents
- hooks: **True** — events sessionStart, sessionEnd, preToolUse, postToolUse, postToolUseFailure, subagentStart, subagentStop, beforeShellExecution, afterShellExecution, beforeMCPExecution, afterMCPExecution, beforeReadFile, afterFileEdit, beforeSubmitPrompt, preCompact, stop, afterAgentResponse, afterAgentThought, plus Tab hooks (beforeTabFileRead, afterTabFileEdit) and workspaceOpen; `.cursor/hooks.json` (project), `~/.cursor/hooks.json` (user), enterprise paths; precedence Enterprise > Team > Project > User; exit code 2 blocks; cloud agents run command-based hooks only (subset); CLI hooks shipped Jan 2026 [S47][S8]. Evidence: https://cursor.com/docs/hooks
- plan_mode: **True** — Plan mode (asks clarifying questions, researches, produces editable plan; no code until approved) and Ask mode (read-only); IDE Shift+Tab / mode picker; CLI `/plan`, `/ask`, `--mode=plan`, `--plan`, Shift+Tab; ACP exposes agent/plan/ask modes; CLI plan mode shipped Jan 2026 [S48][S1][S16][S43][S8]. Evidence: https://cursor.com/docs/agent/plan-mode
- plugin_docs_url: https://cursor.com/docs/plugins (marketplace https://cursor.com/marketplace; skills https://cursor.com/docs/skills; rules https://cursor.com/docs/rules)
- config_docs_url: https://cursor.com/docs/customize-cursor (MCP https://cursor.com/docs/mcp; hooks https://cursor.com/docs/hooks; CLI https://cursor.com/docs/cli/using)
- ACP support: **yes, first-party** — `agent acp` runs the CLI as an ACP server over stdio (JSON-RPC 2.0, newline-delimited JSON; protocolVersion 1); modes agent/plan/ask; permission requests allow-once/allow-always/reject-once; Cursor extension methods (e.g. `cursor/ask_question`, `cursor/create_plan`); named clients JetBrains AI Assistant, Zed, Neovim (avante.nvim) [S43][S12]. Paseo invokes the legacy alias `cursor-agent acp`; the installer symlinks both `agent` and `cursor-agent` to the same executable [S3].
- SDK: **yes** — `@cursor/sdk` (npm, Node 22.13+) and `cursor-sdk` (PyPI, Python 3.10+); wraps "the same agent that runs in the Cursor IDE, CLI, and web app"; local runtime (agent loop in-process) or cloud runtime (Cursor VM); requires CURSOR_API_KEY; GA per docs; cloud agents also have a REST API [S11][S49][S10] (as-of 2026-08-21).

## 4. Claimed differentiation (raw material for PRI-2927)

- tagline (homepage, verbatim-short): "Cursor is your coding agent for building ambitious software." — https://cursor.com [S35]
- GitHub/ToS/legacy descriptor: "The best way to code with AI" (page title) [S4][S23]
- CLI one-liner: interact with AI agents from the terminal to write, review, and modify code — https://cursor.com/docs/cli/overview [S1]
- maker claims (paraphrased):
  1. Agents turn ideas into code end-to-end (build, test, demo) while the developer focuses on decisions [S35].
  2. One agent across surfaces: desktop, CLI, web/mobile, Slack, GitHub, JetBrains (ACP), SDK — sessions hand off between local and cloud (`&` prefix, /in-cloud, Cursor 3 "unified workspace") [S35][S16][S50].
  3. Cloud agents run in parallel on isolated VMs for multi-day tasks; Builds cut start time (3x faster first token, 10x faster boot); always-on Automations, subscriptions to PRs/Slack threads, `/goal` long-lived objectives [S6][S10][S51].
  4. Model choice: frontier third-party models plus first-party Grok/Composer models priced more generously; Cursor Router picks the model per request [S13][S14][S52].
  5. Own models trained on SpaceX GPU fleet post-acquisition ("more capable models at reduced costs") [S20].
  6. Customization stack: rules (.mdc, AGENTS.md), skills (open Agent Skills standard), subagents, hooks, MCP, plugins + reviewed marketplace, team marketplaces [S44][S45][S46][S47].
  7. Enterprise trust: SOC 2 Type II, AIUC-1 certification (adversarially tested agents), privacy mode/zero retention, SSO/SCIM, repo and MCP allowlists, audit logs [S33][S34].
  8. Evidence offered: 64–70% of Fortune 500, 50,000+ enterprises, 100M+ lines/day, customer case studies (Coinbase, Wayfair 90% ML cost cut, Faire 2x PR throughput, Vercel) [S33][S37][S17].
- audience: professional developers and engineering teams/enterprises ("software development teams and enterprises", "individual builders"); pricing tiers for hobbyists, pros, teams, enterprise, and India "Start" plan [S35][S15].

## 5. Company & contact targets (PRI-2929) — company-level only

- legal name: Anysphere, Inc. (d/b/a Cursor); wholly owned subsidiary of SpaceX (SpaceXAI division) since 2026-08-14 [S23][S21][S22]
- HQ: San Francisco, CA (ToS mailing address; Wikipedia); European HQ London announced Jun 2026 (press) [S23][S24][S26]
- size: ">300" (maker, 2025-11-13) [S31]; later third-party estimates not verified (null)
- funding stage: acquired (SpaceX, $60B all-stock, closed 2026-08-14); prior Series D $2.3B at $29.3B (2025-11) [S21][S31]
- publicly named leadership (only as named on cursor.com or in company filings/press releases):
  - Michael Truell — co-founder; bylined "Cursor 3" launch post (2026-04-02) with no title on cursor.com [S50]; CEO per Wikipedia/Fortune [S24][S42]
  - Sualeh Asif — co-founder; co-bylined "Cursor 3" post, no title on cursor.com [S50]; Chief Product Officer per Wikipedia [S24]
  - Aman Sanger, Arvid Lunnemark — co-founders per Wikipedia (not found named on cursor.com in this research) [S24]
  - Jordan Topoleski — COO per Wikipedia (not found on cursor.com) [S24]
  - Kenneth Moras — bylined AIUC-1 certification post (2026-08-13), no title given [S34]
  - Dan Perks — posted the CLI beta announcement on forum.cursor.com (2025-08-07), staff role not titled [S25]
  - DevRel / partnerships lead: none named on cursor.com (careers page lists a "Strategic Partnerships & Growth Lead — DoW / Army" opening; community@cursor.com is the published community contact; Ambassadors program) [S53][S39] — researched, absent
- contact: enterprise sales via https://cursor.com/enterprise; community@cursor.com (community page) [S33][S39]

## 6. Open questions / conflicts

- Existing census `url` / `source_code_url: https://github.com/cursor/cursor` — repo holds only README/SECURITY/issue templates; it is an issue tracker, not source. `source_available: False` is correct [S4].
- Existing census `platforms: ["IDE","Desktop"]` — understates: CLI (terminal), Cloud/web (cursor.com/agents), iOS app, iPad app, Android PWA, Slack, GitHub/Bitbucket/Linear triggers, JetBrains via ACP, SDK [S1][S10][S12][S6].
- Existing census `install_method: "Download from https://cursor.com"` — CLI installs via `curl https://cursor.com/install -fsS | bash` / PowerShell; Homebrew casks `cursor` and `cursor-cli` exist [S2][S5].
- Existing census `hooks: null` — hooks exist (extensive event list; IDE, CLI, cloud subset) [S47].
- Existing census `claude_code_plugin: null` — partial: reads CLAUDE.md, .claude/skills, .claude/agents; no .claude-plugin/marketplace.json support found [S16][S45][S46].
- Existing census `model_providers` lists "SpaceXAI (Grok)" — docs list Grok 4.5/4.6 under Cursor's first-party models (trained with SpaceXAI/xAI compute per the joining-spacex post) [S13][S20]; also Moonshot and Z.ai models present [S13].
- Existing census `pricing` — "$20/month Individual (Pro/Pro+/Ultra)" is wrong: Pro $20, Pro+ $60, Ultra $200 (docs models-and-pricing) while the marketing pricing page phrases Pro+/Ultra as "$20 base + 3x/20x limits" [S14][S15]. Teams $40/user matches. Start (India ₹649) missing.
- Existing census `current_release: "2026-05-12"` — that is the GitHub repo's last push date, not a product release; IDE cask is 3.17.8 and the changelog has entries through 2026-08-19; CLI 2026.08.11 [S5][S6][S8].
- Existing census `maker: "cursor"` — legal maker is Anysphere, Inc., now a SpaceX subsidiary (2026-08-14) [S23][S21].
- Existing census `docs_url/plugin_docs_url/config_docs_url: null` — filled in section 3.
- Existing census prose ("fleets of parallel agents working for hours or days", "Plan Mission Control") — partially matches Cursor 3 / cloud-agent claims; "Mission Control" phrase appears in a Coinbase quote, not as a product name in docs consulted [S37].
- Roster URL https://docs.cursor.com/en/cli/overview redirects (308) to https://cursor.com/docs — roster should point to https://cursor.com/docs/cli/overview [S1].
- Binary naming: official docs use `agent`; Paseo uses `cursor-agent acp`; installer creates both symlinks ("primary: agent, legacy: cursor-agent") and Homebrew `cursor-cli` cask installs `cursor-agent` only — both work today; "legacy" label suggests risk of future removal [S3][S5].
- Fortune 500 share stated three ways: "over half" (Jun 2025), 64% (enterprise page), 70% (Aug 2026 post) [S30][S33][S34].
- Revenue after $1B (Nov 2025): $2B/$3B/$4B figures are press/aggregator (Bloomberg via Wikipedia; Dealroom returned 403 on direct fetch) — no Cursor-authored post found [S26][S32]. First public release month (Mar 2023) rests on press + repo creation date; no Cursor-authored launch post located.
- Leadership titles on cursor.com: bylines without titles; CEO/CPO/COO titles come from Wikipedia/press, not company pages [S50][S24].
- IDE default autonomy (auto-run commands vs ask) not stated on the agent overview page fetched; CLI defaults are documented [S9][S16].
- Unreachable/unverified: Dealroom note (403); cursor.com/about and cursor.com/company returned a bare title page; reddit subscriber count blocked; Discord count from search snippet only.

## 7. Sources

1. [S1] https://cursor.com/docs/cli/overview — CLI overview, install, modes, sandbox (docs.cursor.com/en/cli/overview 308-redirects to cursor.com/docs)
2. [S2] https://cursor.com/docs/cli/installation — install, binary `agent`, auto-update
3. [S3] https://cursor.com/install (script) — version 2026.08.11-e8db854, symlinks agent + cursor-agent
4. [S4] https://api.github.com/repos/cursor/cursor (+ contents, contributors, commits, search/issues; third-party ACP repos) — stars, dates, repo contents
5. [S5] https://formulae.brew.sh/api/cask/cursor.json and /cask/cursor-cli.json — versions, install analytics
6. [S6] https://cursor.com/changelog — Aug 2026 entries (cloud agents, Origin, Builds, iPad)
7. [S7] https://cursor.com/changelog/page/2 — 3.11 (Jul 10), 3.10, Router, Start
8. [S8] https://cursor.com/docs/cli/changelog — CLI feature timeline (hooks/plan Jan 2026, subagents/plugins Mar 2026, marketplace May 2026, latest 2026-08-11)
9. [S9] https://cursor.com/docs/agent/overview — agent tools
10. [S10] https://cursor.com/docs/cloud-agent — cloud agents, triggers, pricing
11. [S11] https://cursor.com/docs/sdk/typescript — @cursor/sdk, runtimes, GA
12. [S12] https://cursor.com/docs/integrations/jetbrains — ACP-based JetBrains integration, plugin 22282
13. [S13] https://cursor.com/docs/models — model list, Router
14. [S14] https://cursor.com/docs/models-and-pricing — plan credits, Teams token rate, Start plan
15. [S15] https://cursor.com/pricing — plan names and features
16. [S16] https://cursor.com/docs/cli/using — flags, approvals, rules/MCP/ACP in CLI, `&` cloud handoff
17. [S17] https://cursor.com/blog — post list (SpaceX, AIUC-1, Firetiger, Builds, Grok 4.6, Router, Mixture-of-Kittens, customer stories)
18. [S18] (reserved)
19. [S19] (reserved)
20. [S20] https://cursor.com/blog/joining-spacex — 2026-08-14 acquisition post
21. [S21] https://finance.yahoo.com/technology/ai/articles/spacex-completes-record-60-billion-131311785.html — close details, 8-K, SpaceXAI
22. [S22] web search results (Seeking Alpha, Crowdfund Insider, SatNews) — SpaceX close 2026-08-14, 389,289,254 shares
23. [S23] https://cursor.com/terms-of-service — Anysphere, Inc., license wording, address, updated 2026-08-13
24. [S24] https://en.wikipedia.org/wiki/Cursor_(code_editor) — founders, funding table, acquisitions, ARR cites (TechCrunch, Bloomberg, Reuters, SEC 8-K)
25. [S25] https://forum.cursor.com/t/cursor-cli-beta-available-now/126964 — CLI beta 2025-08-07, `cursor-agent`
26. [S26] web search results (Dealroom note, getlatka, axis-intelligence) — $2B/$3B/$4B run-rate timeline, enterprise share, London HQ
27. [S27] https://api.npmjs.org/downloads/point/last-week/@cursor/sdk (and cursor-agent, cursor-agent-acp) — npm weekly downloads
28. [S28] https://pypistats.org/api/packages/cursor-sdk/recent — PyPI downloads
29. [S29] https://plugins.jetbrains.com/api/searchPlugins?search=cursor — unofficial plugin downloads
30. [S30] https://cursor.com/blog/series-c — $900M at $9.9B, >$500M ARR, >half F500, NVIDIA/Uber/Adobe
31. [S31] https://cursor.com/blog/series-d — $2.3B at $29.3B, >$1B ARR, >300 staff, investors
32. [S32] web search results for "$4 billion" (Dealroom, tradingkey) — $4B ARR Jun 2026
33. [S33] https://cursor.com/enterprise — 64% F500, 50,000+ enterprises, 100M+ lines/day, logos, SOC 2, controls
34. [S34] https://cursor.com/blog/aiuc-1 — AIUC-1, Schellman, 70% F500, author byline
35. [S35] https://cursor.com — tagline, claims, testimonials, NVIDIA/YC numbers
36. [S36] https://cursor.com/customers — customer list and metrics
37. [S37] https://cursor.com/blog/coinbase — Coinbase metrics 2026-06-23
38. [S38] web search results (discord.com/invite/cursor snippet, thehiveindex) — Discord 38,612; forum ~103K
39. [S39] https://cursor.com/community — ambassadors/events numbers, contact
40. [S40] https://cursor.com/marketplace — 100+ plugins, publishers
41. [S41] https://www.tbench.ai/leaderboard/terminal-bench/2.1 — Cursor CLI + Grok 4.5 #4, 79.3%
42. [S42] https://fortune.com/article/who-is-michael-truell-cursor-ceo-spacex-acquisition/ (via search) — CEO press profile; [S42-MCP] https://cursor.com/docs/mcp — MCP client details
43. [S43] https://cursor.com/docs/cli/acp — `agent acp`, stdio JSON-RPC, modes, permissions, limits
44. [S44] https://cursor.com/docs/plugins — plugin format, marketplace rules, team marketplaces
45. [S45] https://cursor.com/docs/skills — SKILL.md, directories incl. .claude/skills
46. [S46] https://cursor.com/docs/subagents — subagent format, built-ins, .claude/agents compat
47. [S47] https://cursor.com/docs/hooks — hook events, config paths, cloud subset
48. [S48] https://cursor.com/docs/agent/plan-mode — plan mode behaviour
49. [S49] https://cursor.com/docs/sdk/python — cursor-sdk, Python 3.10+
50. [S50] https://cursor.com/blog/cursor-3 — Cursor 3 (2026-04-02), bylines Truell/Asif
51. [S51] https://cursor.com/blog/builds — Builds, 3x faster (via blog list/changelog)
52. [S52] https://cursor.com/blog/router — Cursor Router 2026-07-22 (via blog list/changelog)
53. [S53] https://cursor.com/careers/strategic-partnerships-growth-lead-dow-army (via search) — partnerships role listing
54. https://cursor.com/docs/cli/headless — --force/--yolo, output formats, CURSOR_API_KEY
55. https://cursor.com/docs/rules — .mdc rules, AGENTS.md, precedence
56. https://cursor.com/docs — docs navigation (CLI, SDK, Cloud, Customize sections)

## Inclusion check (Jesse's test)

**Yes** — Cursor ships its own agentic loop (the same agent runs in the IDE, CLI, cloud VMs and the SDK; it reads/edits files, runs shell, spawns subagents, iterates to completion) over multi-vendor and first-party models; `agent acp` exposes that native agent over ACP rather than wrapping a third-party agent [S11][S43][S16].
