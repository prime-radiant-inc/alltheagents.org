# Dossier: Kiro (census_slug: kiro)

Compiled 2026-08-21. Facts only. Null convention: "null = not researched"; "False/none = researched and absent". Each non-obvious fact carries a source [Sn] (see section 7) and an as-of date. Kiro has two coding-agent surfaces in scope for the census: the **Kiro IDE** (desktop app, Code OSS fork) and **Kiro CLI** (`kiro-cli`, successor to Amazon Q Developer CLI). Web, iOS and "Kiro Crew" surfaces exist and are noted where relevant. Every fact states which surface it applies to.

## 1. Identity

- name: Kiro (surfaces: Kiro IDE; Kiro CLI (`kiro-cli`); Kiro Web; Kiro for iOS; Kiro Crew) [S1][S4][S5] (as-of 2026-08-21)
- maker: Amazon Web Services / Amazon.com, Inc. (company; README footer "(c)2026 Amazon.com, Inc. or its affiliates"); HQ Seattle, WA, USA [S2][S44] (as-of 2026-08-21)
- product URL: https://kiro.dev ; CLI docs https://kiro.dev/docs/cli/ ; ACP docs https://kiro.dev/docs/cli/acp/ [S1][S7][S8]
- repo URL: https://github.com/kirodotdev/Kiro — README states the repo is for bug reports, feature requests and feedback; no product source [S2][S3]. Related public repos: kirodotdev/KiroCrew (Apache-2.0, Python), kirodotdev/powers (registry), aws/amazon-q-developer-cli (Apache-2.0, predecessor CLI, "no longer actively maintained") [S3][S21] (as-of 2026-08-21)
- license: proprietary for IDE and CLI. GitHub API reports license null for kirodotdev/Kiro [S3]; aws/amazon-q-developer-cli README calls Kiro CLI "a closed-source product" [S21]; IDE is based on Code OSS (MIT) per FAQ [S9]. Kiro Crew is Apache-2.0 [S3][S18].
- open source? False for IDE and CLI. source_available: partial — only Kiro Crew (agent workspace) and the powers registry are open; the IDE and CLI binaries are closed [S3][S18][S21] (as-of 2026-08-21)
- first public release: IDE public preview 2025-07-14 (launch post "Introducing Kiro"; "free during preview, with some limits") [S10]; GitHub repo created 2025-06-17 [S3]. Waitlist period Oct 2025 (AWS roundup "Kiro waitlist" 2025-10-20) [S26]. General availability of IDE, CLI and team plans 2025-11-17 [S11][S12]. Kiro CLI: announced at GA 2025-11-17 as "a new Kiro CLI bringing agents to your terminal" [S12]; predecessor Amazon Q Developer CLI repo (created 2024-09-23) now redirects users to Kiro CLI [S21]. CLI 2.0 2026-04-13 (headless mode, API keys, Windows) [S15]. CLI 3.0 "early release" via `kiro-cli --v3` (docs page updated 2026-08-04) [S16]. IDE 1.x: first 1.0.x changelog entry 1.0.52 on 2026-07-02 [S17].
- latest release: IDE 1.0.337 (2026-08-18); CLI 2.19.1 (2026-08-21; Homebrew cask kiro-cli 2.19.1); Kiro Crew v0.3.0 (2026-08-21) [S6][S17][S3][S22] (as-of 2026-08-21)
- what it is:
  - Form factors: desktop IDE (macOS Intel/Apple Silicon, Windows 10/11, Linux; Code OSS fork with VS Code settings/extension import) [S19][S2]; terminal CLI `kiro-cli` (macOS, Linux glibc 2.34+/musl, Windows 11 PowerShell; interactive TUI, headless `--no-interactive` mode, ACP server mode, voice mode) [S7][S14][S19]; web app (app.kiro.dev) and iOS app (TestFlight early access) running built-in agents; Kiro Crew (open-source persistent/scheduled agent with Slack/Discord/Telegram/Teams channels) [S18][S19][S9]. Since 2026-08-03 all surfaces share one "agent harness" — a standalone server process speaking ACP to the clients [S20].
  - Models: maker-hosted only; no BYO-key or BYO-model documented (researched, absent) [S23][S9]. Catalogue (2026-08-21): "Auto" router; OpenAI GPT-5.6 Sol/Terra/Luna (routed via US regions); Anthropic Claude Opus 5, Sonnet 5, Opus/Sonnet 4.x, Haiku 4.5; open-weight DeepSeek 3.2, MiniMax M2.5, GLM-5, Qwen3; served via cross-region inference across AWS Regions (US or EU by profile) [S23][S9][S1]. Free tier: open-weight models + Claude Sonnet 4.5 [S24]. Credit multipliers relative to Auto=1.0x (e.g. Opus 2.2x, Qwen3 0.05x) [S23].
  - Pricing (credit-based, same credits across IDE/CLI/web): Free $0 (50 credits/mo); Pro $20/user/mo (1,000 credits); Pro+ $40 (2,000); Pro Max $100 (5,000); Power $200 (10,000); add-on credits $0.04/credit; enterprise via AWS account with IAM Identity Center, centralized billing, optional overages; GovCloud ~20% higher, no free tier; $20 sign-up credit promotion [S24] (as-of 2026-08-21). Startup program: one year of Pro+ for startups up to Series B (GA post) [S11].
  - Install: IDE — download installer from kiro.dev/downloads (auto-updates); Homebrew cask `kiro` exists [S19][S6]. CLI — `curl -fsSL https://cli.kiro.dev/install | bash` (macOS/Linux/Windows per docs); Homebrew cask `kiro-cli` [S7][S6]. Auth: Google, GitHub, AWS Builder ID, or organization IdP via IAM Identity Center (Okta, Entra ID); API keys (`KIRO_API_KEY`) for headless CLI on paid tiers [S19][S14][S25].
  - Default autonomy: capability-based permissions with effects deny/ask/allow (`~/.kiro/settings/permissions.yaml`, per-workspace files). By default Kiro reads workspace files and runs read-only git/system commands without asking; writes, other shell commands and anything not allowed require approval; writes to `.git/**`, `.kiro/` and `.kiroignore` always ask. IDE has "Autopilot" (executes permitted operations without prompting) vs "Supervised" (approval before actions) modes. CLI headless supports `--trust-all-tools` / `--trust-tools=<categories>` [S25][S14] (as-of 2026-08-21). Sandbox: only a "Sandbox" network-restriction feature in Web preview is mentioned; no OS-level sandbox documented for IDE/CLI (researched, absent) [S25].
  - Repo language per GitHub API: TypeScript (kirodotdev/Kiro; issues-only repo) [S3]. Predecessor Q CLI was Rust [S21].

## 2. Adoption evidence

| metric / claim | value | as-of | source | type |
|---|---|---|---|---|
| GitHub stars, kirodotdev/Kiro (issues/feedback repo) | 4,214 | 2026-08-21 | [S3] | independently observable |
| GitHub forks / watchers / open issues, kirodotdev/Kiro | 305 / 40 / 1,554 | 2026-08-21 | [S3] | independently observable |
| GitHub issues ever filed, kirodotdev/Kiro | 10,708 | 2026-08-21 | [S3] | independently observable |
| Commits last 90 days, kirodotdev/Kiro | 3 (repo holds docs/assets only; last push 2026-06-22) | 2026-08-21 | [S3] | independently observable |
| GitHub stars, kirodotdev/KiroCrew (created 2026-07-16, Apache-2.0) | 3,158 stars, 342 forks, 100+ commits in 90d, latest v0.3.0 2026-08-21 | 2026-08-21 | [S3] | independently observable |
| GitHub stars, kirodotdev/powers (registry) | 360 stars, 197 forks, 99+ commits in 90d | 2026-08-21 | [S3] | independently observable |
| GitHub stars, aws/amazon-q-developer-cli (predecessor, Apache-2.0) | 1,985 stars, 434 forks; last push 2026-08-17 | 2026-08-21 | [S3][S21] | independently observable |
| Homebrew cask installs `kiro-cli` 30d / 90d / 365d | 1,648 / 5,446 / 18,843 | 2026-08-21 | [S6] | independently observable |
| Homebrew cask installs `kiro` (IDE) 30d / 90d / 365d | 903 / 3,017 / 13,277 | 2026-08-21 | [S6] | independently observable |
| npm | no official package; `kiro-cli` on npm is a third-party "placeholder" (177 weekly downloads) | 2026-08-21 | [S27] | independently observable (not Kiro's) |
| VS Code / JetBrains marketplace installs | not applicable — Kiro IDE is a standalone Code OSS fork; no marketplace extension found | 2026-08-21 | [S2][S19] | researched, absent |
| Discord members (discord.gg/kirodotdev, via invite API) | 24,084 members; ~2,060 online | 2026-08-21 | [S28] | independently observable |
| Powers marketplace (kiro.dev/powers) | 76 listed powers (Verified partner + Community badges; partners incl. AWS, Stripe, Supabase, Datadog, Figma, Postman, GitHub, Snyk, Terraform, Zapier) | 2026-08-21 | [S29] | independently observable |
| Developers in preview | 100,000+ tried Kiro IDE in first 5 days (Jul 2025); "more than doubled" by Oct 2025 | 2026-07-14 | [S13] | maker-claimed |
| Developers at GA | "over 250,000 developers since its preview release" | 2025-11-24 | [S12] | maker-claimed |
| Developer growth | developers using Kiro "more than doubled" QoQ; enterprise customer usage "nearly tenfold" (Amazon Q1 2026 earnings highlights) | 2026-04-29 | [S30] | maker-claimed |
| Usage growth | Kiro "tripled in usage quarter-over-quarter"; "up to 50% more cost-effective than alternatives"; launched on iOS (Amazon Q2 2026 earnings) | 2026-07-30 | [S31] | maker-claimed |
| Community powers | 15,000+ unique community-created powers; 100+ curated partner powers; 1,000+ Kiro Ambassadors; Discord grew "by over one-third" | 2026-07-14 | [S13] | maker-claimed |
| Requests during preview | "over 300 million requests", "trillions of tokens" (reported in press recaps of GA; not found on kiro.dev GA post) | 2025-11 | [S32] | maker-claimed via press, not verified on kiro.dev |
| Public customers / case studies | Loyola Marymount University, Siemens, SmugMug, Flickr, Appian, Analytics Fox Softwares, Festly, ALO Tech Solutions, Trailflow Systems (one-year post); homepage testimonials are individual practitioners; Snyk partnership post | 2026-07-14 | [S13][S1][S33] | maker-claimed |
| Amazon Q Developer migration | Q Developer IDE plugins + paid subscriptions end of support 2027-04-30; new signups stopped 2026-05-15; latest models exclusive to Kiro from 2026-05-29 | 2026-04-30 | [S34] | maker-claimed (AWS blog) |
| Funding / valuation / acquisition | n/a — internal AWS product; no separate funding (researched, absent) | 2026-08-21 | — | — |
| Benchmarks (SWE-bench, Terminal-Bench) | none found for Kiro as a harness | 2026-08-21 | [S35] | researched, absent |
| Press | Forbes (2025-07-15), The New Stack ("AWS's specs-centric answer to Windsurf and Cursor"), Constellation Research (2025-12-02, re:Invent autonomous agents), The Register/CNBC on Amazon earnings mentions | 2026-08-21 | [S35][S36] | press |
| GitHub Discussions | not enabled (API has_discussions false) | 2026-08-21 | [S3] | independently observable |

## 3. Plugin interface (PRI-2925)

- mcp_support: **client** (IDE + CLI). Transports: local stdio (IDE, CLI, Web, Mobile with limits) and remote HTTP/SSE (IDE, CLI only); OAuth for remote servers (CLI 2.12+ / v3); workspace `.kiro/settings/mcp.json` and user-level config; docs state Kiro does not act as an MCP server [S37][S16] (as-of 2026-08-21). Evidence: https://kiro.dev/docs/mcp/
- plugin_support: **True** — "Powers": directory packages following the open Agent Plugins spec (`plugin.json` manifest, `skills/` with SKILL.md, optional `mcp.json`, optional `dev.kiro/` steering); one-click install from the kiro.dev/powers marketplace (76 listed) or any GitHub URL; legacy `POWER.md` format still works; IDE full support, CLI "v3+", Web/Mobile limited [S38][S39][S29]. Plus Agent Skills (`.kiro/skills/`, `~/.kiro/skills/`, agentskills.io standard; all surfaces) [S40]; Steering files (`.kiro/steering/`, AGENTS.md incl. nested, always/fileMatch/manual/auto modes) [S41]; custom agents (`.kiro/agents/`, JSON or Markdown) [S42]. Evidence: https://kiro.dev/docs/powers/
- claude_code_plugin: **partial** — Kiro does not read `.claude/` plugins, CLAUDE.md, `.claude/skills` or Claude Code marketplaces (researched, absent in docs) [S40][S41]. It installs Agent Plugins-format packages (root `plugin.json` + `skills/` + `mcp.json`; spec governed by Amazon, Cursor, Microsoft, OpenAI, Vercel), and SKILL.md skills per the agentskills.io standard, which overlap with Claude Code's skills/plugin content but are not the `.claude-plugin/plugin.json` format [S38][S39][S43] (as-of 2026-08-21).
- subagents: **True** (IDE + CLI; Web/Mobile built-in only) — `subagent` tool in the orchestrator agent's `tools`; explicit or automatic delegation to custom agents from `.kiro/agents/`; isolated context/tools/permissions; run in parallel; DAG task dependencies and review loops (1-10 iterations); `toolsSettings.subagent.availableAgents/trustedAgents`; CLI added subagents in 1.23 and "Introspect subagent" in 2.13 [S42][S17] (as-of 2026-08-21). Evidence: https://kiro.dev/docs/custom-agents/subagents/
- hooks: **True** (IDE + CLI; not Web/Mobile) — triggers PostFileSave, PostFileCreate, PostFileDelete (agent-made changes only), PreToolUse (can block), PostToolUse, UserPromptSubmit (can block), SessionStart, Stop; actions: shell command (context via STDIN) or agent prompt; stored as JSON files in `.kiro/hooks/`; global hooks (CLI 2.13, IDE 1.0.182) [S44][S17]. Evidence: https://kiro.dev/docs/hooks/
- plan_mode: **True** — built-in read-only Plan agent: `/plan` or Shift+Tab toggles plan vs execution; explores codebase, cannot modify files; produces implementation plan then hands off (CLI since 1.23; CLI v3 and IDE workflow picker "Plan") [S45][S16][S46]. Specs (requirements/design/tasks, quick spec, bugfix spec) are a separate planning artifact workflow on IDE/CLI/Web [S47]. Evidence: https://kiro.dev/docs/cli/chat/planning-agent/
- plugin_docs_url: https://kiro.dev/docs/powers/ (skills: https://kiro.dev/docs/skills/ ; custom agents: https://kiro.dev/docs/custom-agents/)
- config_docs_url: https://kiro.dev/docs/permissions/ (steering: https://kiro.dev/docs/steering/ ; CLI configuration/reference: https://kiro.dev/docs/cli/ ; MCP: https://kiro.dev/docs/mcp/)
- ACP support: **yes, first-party (CLI)** — `kiro-cli acp` runs Kiro CLI as an ACP agent (JSON-RPC over stdio); implements initialize, session/new, session/load, session/prompt, session/cancel, session/set_mode, session/set_model; `_kiro.dev/` extension methods for slash commands, MCP servers, compaction; documented clients JetBrains (`~/.jetbrains/acp.json`) and Zed; announced 2026-02-05 (CLI 1.25); the internal harness-to-client protocol is also ACP with 20+ Kiro extension methods [S8][S48][S20] (as-of 2026-08-21).
- SDK: **none** (researched, absent) — no Kiro SDK documented; programmatic use is via headless CLI (`kiro-cli chat --no-interactive`, `KIRO_API_KEY`, `--trust-tools`) or ACP [S14][S8].

## 4. Claimed differentiation (raw material for PRI-2927)

- tagline (homepage): "Move beyond AI coding to agentic engineering" — https://kiro.dev/ [S1]
- README one-liner: agentic IDE and CLI "from prototype to production with spec-driven development, agent hooks, powers" — https://github.com/kirodotdev/Kiro [S2]
- GitHub description: "an agentic IDE that works alongside you from prototype to production" [S3]
- maker claims (paraphrased):
  1. Spec-driven development: turns prompts into structured, executable specs (requirements/design/tasks, EARS-style acceptance criteria) instead of "vibe coding"; "first to bring spec-driven development" to AI coding tools [S10][S13][S47].
  2. Correctness beyond tests: property-based testing measures whether code matches the spec; "Analyze Requirements" uses automated reasoning to find contradictions/gaps [S1][S11][S47].
  3. Structure for the agent: steering files, hooks ("like an experienced developer catching things you miss"), custom agents, capability-based permissions [S10][S25][S44].
  4. Powers: on-demand context/tools that avoid "MCP context overload"; open Agent Plugins format; marketplace of partner powers [S3][S38][S39].
  5. One agent, every surface: the same harness and `.kiro` config across IDE, CLI, web, iOS, cloud sessions; headless CLI in CI/CD; ACP into other editors [S20][S1][S48].
  6. Multi-model with Auto routing and credit-based pricing "with no daily or weekly rate limits"; "up to 50% more cost-effective than alternatives" [S1][S24][S31].
  7. Enterprise/AWS: IAM Identity Center/SSO, centralized billing, GovCloud, US/EU regions, paid-tier content not used for training [S24][S9][S49].
  8. Open-source Crew: persistent, self-improving agent workspace released Apache-2.0 [S18][S3].
- audience: developers and teams ("helps developers and teams do their best work"); startups (startup credits, "Built for startups"); enterprises ("Enterprise-ready"); learners/students (one-year students post) [S1][S11][S13].

## 5. Company & contact targets (PRI-2929) — company-level only

- legal name: Amazon.com, Inc. (README copyright); product is built by Amazon Web Services (AWS) [S2][S34]
- HQ: Seattle, WA, USA (Amazon/AWS) [S44]
- size: Amazon.com, Inc. ~1.5M employees; AWS 2025 revenue US$128.7B (Wikipedia) [S44] (as-of 2026-08-21)
- funding stage: public company (NASDAQ: AMZN); Kiro is an internal product line [S30]
- publicly named leadership (only as bylined/named on kiro.dev, aws.amazon.com or aboutamazon.com):
  - Matt Garman — CEO, AWS (quoted on Kiro at re:Invent 2025) [S36][S44]
  - Deepak Singh — VP, DevEx & Agents, AWS (launch post byline 2025-07-14; one-year post 2026-07-14) [S10][S13]
  - Nikhil Swaminathan — Product Lead, Kiro (launch post and GA post bylines) [S10][S11]
  - Doug Clauson — Product Lead (CLI 2.0 post byline, 2026-04-13) [S15]
  - Clare Liguori — Engineering Lead (harness post 2026-08-03; Agent Plugins post 2026-08-07) [S20][S39]
  - Brian Beach — Tech Lead (ACP post 2026-02-05; cloud sessions post) [S48]
  - Dragos Ilinca, Krishna Dalal — Product Marketing (GA post; CLI 2.0 post) [S11][S15]
  - Ranjith Ramakrishnan — pricing/plans posts (Pro Max, overage caps) [S50]
  - Vipin Mohan — model availability posts (GPT-5.6, Opus 5, Sonnet 5) [S50]
  - Nicole Shum — community/builders posts (students, founders) [S50]
  - Helen Hasbun — community posts (birthday week, merch store) [S50]
  - DevRel / partnerships lead: none explicitly titled on kiro.dev (researched, absent); powers partner submissions via kiro.dev/powers [S29]
- contact: Discord https://discord.gg/kirodotdev ; issues https://github.com/kirodotdev/Kiro/issues ; billing via AWS Billing Support; security via AWS vulnerability reporting [S2]

## 6. Open questions / conflicts

- Existing census `maker: "kirodotdev"` — maker is Amazon / AWS (README copyright Amazon.com, Inc.; AWS blogs) [S2][S34]. `kirodotdev` is only the GitHub org.
- Existing census `platforms: ["IDE"]` — Kiro also ships a CLI (`kiro-cli`, GA 2025-11-17, 2.x current, 3.0 early release), web, iOS and Crew [S7][S11][S16][S18]. Roster row is "Kiro CLI"; dossier covers both IDE and CLI.
- Existing census `plugin_support: "no"` and `plugin_docs_url: null` — Kiro has Powers (Agent Plugins format, marketplace of 76), Agent Skills and custom agents [S38][S40][S29]. Should be "yes".
- Existing census `subagents: "no"` — docs describe sub-agents with parallel execution on IDE and CLI [S42]. Should be "yes".
- Existing census `claude_code_plugin: "no"` — "partial" is more accurate: Agent Plugins-format plugins and SKILL.md skills install, `.claude/` plugins and CLAUDE.md do not [S38][S39][S40].
- Existing census `license: null` / `source_available: False` — product is closed; Crew is Apache-2.0. "False" is right for IDE/CLI; note Crew [S3][S21].
- Existing census `current_release: "2026-06-22"` — that is the last push date of the issues repo; actual releases are IDE 1.0.337 (2026-08-18) and CLI 2.19.1 (2026-08-21) [S17][S6].
- Existing census `stars: "4201"` — 4,214 on 2026-08-21; note stars are on an issues-only repo [S3].
- Existing census `language: "TypeScript"` — repo language of an issues/docs repo; product binaries' language not published. Predecessor Q CLI was Rust [S21].
- Existing census `model_providers: null`, `pricing: null`, `config_docs_url: null` — filled in sections 1 and 3.
- Existing census `mcp_support: "yes"` — more precisely "client" [S37].
- Existing census `install_method: "binary"` — IDE installer download; CLI curl installer; both also Homebrew casks [S19][S6][S7].
- Existing census `first_released: "2025-06-17"` — that is the repo creation date; public preview was 2025-07-14 [S10][S3].
- Powers docs say CLI support is "version 3+" while the current CLI release line is 2.19.x with 3.0 opt-in (`kiro-cli --v3`); whether 2.x CLI loads powers is unclear from docs [S38][S16].
- IDE "What's new in 1.0" page fetch showed a date of 2026-08-21 (likely last-updated), while the IDE changelog's first 1.0.x entry is 1.0.52 on 2026-07-02 [S46][S17].
- "300 million requests / trillions of tokens" during preview appears in press/community recaps of the GA; not located on kiro.dev's GA post or the AWS roundup [S32][S11][S12].
- The exact date the Amazon Q Developer CLI binary was rebranded to Kiro CLI is not stated in official sources fetched (community posts say mid-Nov to Dec 2025); official: CLI announced at GA 2025-11-17 and the Q CLI repo README points to Kiro CLI [S12][S21].
- No absolute user count has been published since the 250,000 figure (Nov 2025); 2026 figures are growth multiples only [S30][S31].
- Unreachable/absent: no Kiro-level funding, no benchmark placements, no official npm/PyPI packages; the kiro.dev/docs/cli/installation/ and /docs/enterprise/ URLs redirect (to /docs/getting-started/installation/ and /docs/enterprise/concepts/) [S19][S49].

## 7. Sources

1. [S1] https://kiro.dev/ — tagline, features, models, audience, testimonials
2. [S2] https://github.com/kirodotdev/Kiro (README, via raw-kiro/kiro_readme.md) — capabilities, interfaces, copyright, support channels
3. [S3] https://api.github.com/repos/kirodotdev/Kiro (+ /orgs/kirodotdev/repos, search/issues, commits, KiroCrew releases) — stars, forks, dates, license
4. [S4] https://kiro.dev/docs/ — docs landing, surfaces, feature list
5. [S5] https://kiro.dev/faq/ — surfaces, models, pricing, enterprise, privacy
6. [S6] https://formulae.brew.sh/api/cask/kiro.json and /cask/kiro-cli.json — versions, install analytics
7. [S7] https://kiro.dev/docs/cli/ — CLI description, install command, features
8. [S8] https://kiro.dev/docs/cli/acp/ — ACP methods, client configs, extensions
9. [S9] https://kiro.dev/faq/ — Code OSS base, models, data use, regions (same as S5)
10. [S10] https://kiro.dev/blog/introducing-kiro/ — 2025-07-14 launch, bylines, preview pricing
11. [S11] https://kiro.dev/blog/general-availability/ — 2025-11-17 GA, CLI, team plans, startup offer
12. [S12] https://aws.amazon.com/blogs/aws/aws-weekly-roundup-how-to-join-aws-reinvent-2025-plus-kiro-ga-and-lots-of-launches-nov-24-2025 — 250,000 developers, GA features
13. [S13] https://kiro.dev/blog/one-year/ — 2026-07-14 anniversary numbers, customers, milestones
14. [S14] https://kiro.dev/docs/cli/headless/ — headless mode, API keys, trust flags
15. [S15] https://kiro.dev/blog/cli-2-0/ — 2026-04-13 CLI 2.0, bylines
16. [S16] https://kiro.dev/docs/cli/v3/ — CLI 3.0 early release features
17. [S17] https://kiro.dev/changelog/ , https://kiro.dev/changelog/cli/ , https://kiro.dev/changelog/ide/ — release versions/dates
18. [S18] https://kiro.dev/docs/crew/ — Kiro Crew description, install
19. [S19] https://kiro.dev/docs/getting-started/installation/ — OS support, auth methods
20. [S20] https://kiro.dev/blog/one-agent/ — 2026-08-03 unified harness, ACP internals, bylines
21. [S21] https://github.com/aws/amazon-q-developer-cli (README + API) — predecessor, closed-source note, Rust
22. [S22] https://api.github.com/repos/kirodotdev/KiroCrew/releases/latest — Crew v0.3.0
23. [S23] https://kiro.dev/docs/models/ — model catalogue, multipliers, regions
24. [S24] https://kiro.dev/pricing/ — tiers, credits, GovCloud, enterprise
25. [S25] https://kiro.dev/docs/permissions/ — autonomy modes, defaults, permission files
26. [S26] https://aws.amazon.com/blogs/aws/aws-weekly-roundup-kiro-waitlist-ebs-volume-clones-ec2-capacity-manager-and-more-october-20-2025 — waitlist period (via search)
27. [S27] https://registry.npmjs.org/kiro-cli and https://api.npmjs.org/downloads/point/last-week/kiro-cli — third-party placeholder package
28. [S28] https://discord.com/api/v9/invites/kirodotdev?with_counts=true — Discord member count
29. [S29] https://kiro.dev/powers/ — marketplace count, partners, badges
30. [S30] https://www.aboutamazon.com/news/company-news/amazon-earnings-q1-2026-report — developers doubled QoQ, enterprise 10x
31. [S31] https://www.aboutamazon.com/news/company-news/amazon-earnings-q2-2026-report — usage tripled QoQ, 50% cost claim, iOS
32. [S32] web search results (constellationr.com, caylent.com, aiwiki.ai) — "300M requests / trillions of tokens" recaps
33. [S33] https://kiro.dev/blog/ — post list, bylines (Snyk post, model posts)
34. [S34] https://aws.amazon.com/blogs/devops/amazon-q-developer-end-of-support-announcement/ — Q Developer EoS dates
35. [S35] web search (Forbes 2025-07-15, The New Stack, comparison sites) — press; no benchmark placements found
36. [S36] https://www.constellationr.com/insights/news/aws-kiro-launches-autonomous-agents-individual-developers — 2025-12-02, Garman/Swaminathan titles
37. [S37] https://kiro.dev/docs/mcp/ — MCP transports, client-only
38. [S38] https://kiro.dev/docs/powers/ — Powers structure, install, surfaces
39. [S39] https://kiro.dev/blog/powers-supports-plugins/ — 2026-08-07 Agent Plugins, TSC members
40. [S40] https://kiro.dev/docs/skills/ — Agent Skills locations/standard
41. [S41] https://kiro.dev/docs/steering/ — steering modes, AGENTS.md
42. [S42] https://kiro.dev/docs/custom-agents/ and https://kiro.dev/docs/custom-agents/subagents/ — agents, sub-agents
43. [S43] https://agent-plugins.org/ — spec manifest, maintainers
44. [S44] https://en.wikipedia.org/wiki/Amazon_Web_Services — AWS CEO, revenue; HQ Seattle
45. [S45] https://kiro.dev/docs/cli/chat/planning-agent/ (via search) and https://kiro.dev/changelog/cli/1-23/ — Plan agent, read-only
46. [S46] https://kiro.dev/docs/ide/whats-new-v1/ — IDE 1.0 changes
47. [S47] https://kiro.dev/docs/specs/ — specs workflow, PBT, surfaces
48. [S48] https://kiro.dev/blog/kiro-adopts-acp/ — 2026-02-05 ACP announcement, editors
49. [S49] https://kiro.dev/docs/enterprise/concepts/ — IAM Identity Center, regions, billing
50. [S50] https://kiro.dev/blog/ — bylines for pricing/model/community posts
51. [S51] https://kiro.dev/docs/how-kiro-works/ — six-step agent loop description
52. https://kiro.dev/docs/ide/whats-new-v1/ — see S46

## Inclusion check (Jesse's test)

**Yes** — Kiro IDE and Kiro CLI run AWS's own agent harness (context assembly, model call, permission check, tool execution, feedback loop until done, compaction) that reads/edits files and runs shell commands; the CLI's ACP mode exposes that same first-party loop rather than wrapping another vendor's agent [S20][S51][S8].
