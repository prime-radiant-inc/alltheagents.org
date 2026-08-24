# Dossier: Factory Droid (census_slug: droid; paseo_id: factory-droid)

Compiled 2026-08-21. Facts only. Null convention: "null = not researched"; "False/none = researched and absent". Each non-obvious fact carries a source [Sn] (see section 7) and an as-of date. Surface labels: **CLI** = Droid CLI (`droid`, `droid exec`), **App** = Factory App (desktop) / web (app.factory.ai), **Platform** = Factory cloud features (Missions, Droid Computers, Software Factory, Slack/Linear/Jira, GitHub/GitLab review), **Company** = Factory AI as a whole.

## 1. Identity

- name: Factory Droid. The agent is "Droid"; the terminal product is "Droid CLI" (binary `droid`); the company/platform is "Factory" [S1][S2]. Company copyright line: "Factory AI" [S1].
- maker: Factory (company; legal entity name not verified — README says "Factory AI", press releases say "Factory"); HQ San Francisco, CA, USA [S16][S19]; founded 2023 by Matan Grinberg and Eno Reyes [S19] (as-of 2026-08-21).
- product URL: https://factory.ai/product/cli (CLI); https://factory.ai (company/platform); docs https://docs.factory.ai [S1][S2][S12]
- repo URL: https://github.com/Factory-AI/factory — created 2026-07-29; contents are `.github/`, `README.md`, `docs/` only (no agent source) [S3][S4] (as-of 2026-08-21). Older public repos in the org: factory-plugins (2026-01-12), droid-action (2025-11-15), droid-code-review (2025-10-16), droid-sdk-typescript/-python (2026-03), factory-zed-extension (2026-01-13) [S5].
- license: proprietary. GitHub API license: null; README: "Copyright (c) 2025-2026 Factory AI. All rights reserved." [S1][S4]; npm `droid` license field: "UNLICENSED" [S6] (as-of 2026-08-21).
- open source? False. source_available: False for the agent — the `droid` npm package is a launcher whose optionalDependencies are per-platform binaries (`@factory/cli-darwin-arm64`, `-linux-x64`, `-win32-x64`, etc.); the GitHub repo holds README/docs/issues only [S3][S6]. Open-source satellites: eslint-plugin (Apache-2.0), droid-sdk-python (Apache-2.0), legacy-bench (Apache-2.0), factory-zed-extension (Apache-2.0) [S5].
- first public release: **CLI** — Droid CLI publicly available by 2025-09-25 ("Factory Unleashes the Droids" Series B post: available "in any interface: CLI, IDE, Slack, Linear, Browser") [S13][S14]; VS Code extension first published 2025-09-10 [S9]; oldest release-notes entry v0.19.8 dated "September 30 - October 13" (2025) [S7]; first Factory-published npm version 0.57.5 on 2026-02-05 (the `droid` npm name carries an unrelated 0.0.1 from 2013-09-30) [S6]. **Platform** — company founded 2023; enterprise platform "globally rolled out" at named customers by Sept 2025 [S13][S19]. No single dated "v1.0 launch" found.
- latest release: **CLI** v0.202.0 per Homebrew cask (2026-08-21) [S10]; npm latest 0.200.0 published 2026-08-20T02:46Z [S6]; docs release notes latest entry v0.199.0 dated 2026-08-18 [S7]. npm publishes: 185 Factory versions between 2026-02-05 and 2026-08-20 (14-34 per month) [S6]. GitHub releases: none on the repo [S4].
- what it is:
  - Form factors: **CLI** (`droid` interactive TUI; `droid exec` headless one-shot for CI/scripts; `droid daemon`); **App** (Factory App desktop for macOS Apple Silicon/Intel, Windows x64/ARM64; web app.factory.ai; mobile referenced in README/docs); IDE: VS Code extension (also Cursor/Windsurf), JetBrains plugin and Zed via ACP; Slack, Linear, Jira integrations; GitHub Action (droid-action) and GitHub/GitLab automated PR review; **Platform**: Missions (multi-agent orchestration), Droid Computers (managed cloud or bring-your-own machines), Software Factory (24/7 SDLC automations, private preview), Factory Router (model routing), Agent Readiness/Agent Effectiveness analytics [S1][S2][S12][S21][S22][S23][S24][S25] (as-of 2026-08-21).
  - Models: multi-vendor, Factory-brokered: Anthropic (Claude Fable 5, Opus 5/4.8/4.7/4.6/4.5, Sonnet 5/4.6/4.5, Haiku 4.5), OpenAI (GPT-5.6 Sol/Terra/Luna, 5.5, 5.4, 5.3-Codex, 5.2), Google (Gemini 3.6/3.5/3 Flash, 3.1 Pro), xAI (Grok 4.5), "Droid Core" open-weight pool (GLM-5.2/5.1, Nemotron 3 Ultra, Kimi K2.7/K2.6/K2.5, DeepSeek V4 Pro, MiniMax M3/M2.7/M2.5), each with a usage multiplier; BYOK custom models (OpenAI/Anthropic keys, any OpenAI-compatible endpoint, local models) are CLI-only [S26][S27] (as-of 2026-08-21). Enterprise: LLM gateways, hierarchical model allow/deny, airgapped deployment [S28].
  - Pricing: Pro $20/mo, Plus $100/mo (~5x usage, Droid Computers), Max $200/mo (~10x, early access), Business (up to 150 seats, SSO/SAML/SCIM, ZDR, audit), Enterprise (unlimited seats, dedicated compute, on-prem, CMEK, data residency); no free tier; rolling 5-hour/weekly/monthly rate limits; "Droid Core" open-weight overflow at no extra cost; prepaid "Extra Usage" credits, $10 minimum; BYOK allowance on individual plans [S29][S30] (as-of 2026-08-21).
  - Install: `curl -fsSL https://app.factory.ai/cli | sh` (macOS/Linux), `irm https://app.factory.ai/cli/windows | iex` (Windows), `npm install -g droid` (Node >=20); Homebrew cask `droid` exists (not listed in docs install block); desktop app downloads from app.factory.ai [S1][S2][S6][S10][S21].
  - Default autonomy: two interaction modes, Auto and Spec (Shift+Tab); four Autonomy Levels Off/Low/Medium/High (Ctrl+L) gating file edits (Low+) and commands/MCP tools by risk tier; Off = manual approval of everything beyond read tools/allowlisted commands; built-in denylist and an unbypassable blocklist; `droid exec` is read-only unless `--auto low|medium|high` or `--skip-permissions-unsafe`; subagents inherit the parent level; Missions require High; org settings can set default and maximum levels; OS-level sandbox (seatbelt/bubblewrap) in Beta, opt-in [S31][S32][S33][S34]. The out-of-the-box starting Autonomy Level for a fresh install is not stated explicitly in the docs snapshot (see section 6).
  - Repo language per GitHub API: null (docs-only repo); npm package ships native binaries [S4][S6].

## 2. Adoption evidence

| metric / claim | value | as-of | source | type |
|---|---|---|---|---|
| GitHub stars, Factory-AI/factory | 5 | 2026-08-21 | [S4] | independently observable |
| GitHub forks / watchers / open issues (= total issues) | 0 / 0 / 13 | 2026-08-21 | [S4] | independently observable |
| GitHub contributors (incl. anonymous) | 47 | 2026-08-21 | [S4] | independently observable |
| Commits since repo creation 2026-07-29 | >=100 (API page cap) | 2026-08-21 | [S4] | independently observable |
| GitHub Discussions | enabled on repo (has_discussions true) | 2026-08-21 | [S4] | independently observable |
| Org repos stars: factory-plugins / eslint-plugin / cursed-plugins / droid-action / droid-code-review / droid-sdk-typescript / droid-sdk-python / legacy-bench | 103 (13 forks) / 209 / 104 / 52 / 51 / 38 / 5 / 19 | 2026-08-21 | [S5] | independently observable |
| npm weekly downloads, `droid` | 11,186 (2026-08-14..20) | 2026-08-20 | [S8] | independently observable |
| npm monthly downloads, `droid` | 42,939 (2026-07-22..08-20) | 2026-08-20 | [S8] | independently observable |
| npm weekly downloads, `@factory/droid-sdk` (TS SDK, v0.7.0) | 2,467 | 2026-08-20 | [S8] | independently observable |
| PyPI downloads, `droid-sdk` (Python SDK, v0.3.0) | 629 last week / 3,240 last month | 2026-08-21 | [S11] | independently observable |
| Homebrew cask `droid` installs 30d / 90d / 365d | 260 / 824 / 4,093 (cask rank #795 of 30d list) | 2026-08-21 | [S10] | independently observable |
| VS Code Marketplace, Factory.factory-vscode-extension ("Droid - Factory's AI Coding Agent") | 38,121 installs; 10 ratings, avg 3.9; published 2025-09-10, last updated 2026-05-07 | 2026-08-21 | [S9] | independently observable |
| JetBrains Marketplace plugin 28649 "Factory Droid" | 3,655 downloads | 2026-08-21 | [S9] | independently observable |
| Zed extension "factory-droid" downloads | null (Zed extensions API returned no data) | 2026-08-21 | [S5] | unreachable |
| Discord "Droid" server | 1,556 members, 187 online | 2026-08-21 | [S15] | independently observable |
| Developers using Droids | "hundreds of thousands of developers" daily | 2026-04-16 | [S17] | maker-claimed |
| Revenue growth | "doubled revenue month-over-month for past six months"; no absolute figure | 2026-04-16 | [S17] | maker-claimed |
| Outcome claims | 31x faster feature delivery; 96.1% shorter migrations; 95.8% shorter on-call resolution (Series B); enterprise page: 7x faster feature delivery, 40% incident-response reduction at Empower | 2025-09-25 / 2026-08-21 | [S13][S20] | maker-claimed |
| Public customers (named by maker) | Series B: MongoDB, EY, Bayer, Zapier, Clari; Series C: Nvidia, Adobe, EY, Palo Alto Networks, Adyen; CRO release: Revolut; Factory 2.0 post: Blackstone, Wipro, Comarch; homepage logos: Blackstone, Adyen, Wipro, Comarch, Groq, Chainguard, You.com, Podium; enterprise page: Nav, Tilt, Comarch, You.com, Chainguard, Groq, Empower; case studies: You.com (2026-06-16), Comarch (2026-07-29) | 2026-08-21 | [S12][S13][S16][S17][S18][S19][S20] | maker-claimed |
| Funding: Series B | $50M at $300M valuation; NEA, Sequoia, J.P. Morgan, Nvidia; angels Slootman, Arora, Levie | 2025-09-25 | [S13][S14] | maker-claimed (round) / press |
| Funding: Series C | $150M at $1.5B post; led by Khosla Ventures; Sequoia, Blackstone, Insight, Evantic, 20VC, NEA, Mantis | 2026-04-16 | [S17] | maker-claimed |
| Total raised | ~$220M (aggregate per press/search) | 2026-04 | [S35] | press |
| Partner program commitment | $100M "Factory Partner Network" | 2026-08-19 | [S24] | maker-claimed |
| Community program | "Factory Guild" launched; no member count | 2026-08-14 | [S36] | maker-claimed |
| Benchmark: Terminal-Bench (v1) | Droid + Opus 4.1 58.8% "#1", GPT-5 52.5%, Sonnet 4 50.5%; vs Claude Code 43.2%, Codex CLI 42.8% | 2025-09-25 | [S37] | maker-claimed (press repeated it) |
| Benchmark: Terminal-Bench 2.0 (tbench.ai) | Droid best row rank #10, GPT-5.3-Codex 77.3% (2026-02-24); also #23 Opus 4.6 69.9%, #31 GPT-5.2 64.9%, #34 Opus 4.5 63.1%, #42 Gemini 3 Pro 61.1%; #1 overall NexAU-AHE 84.7% | 2026-08-21 | [S38] | independently observable |
| Benchmark: Terminal-Bench 2.1 (tbench.ai) | no Droid/Factory entries among 17 rows | 2026-08-21 | [S39] | independently observable |
| Benchmark page on docs | shows "Factory Droid #1 63.1%, Dec 2025" on TB 2.0 (stale vs live leaderboard) | 2026-08-21 | [S40] | maker-claimed |
| Other maker benchmark pages | Agent Arena, Legacy-Bench (Factory-authored, repo Apache-2.0), Next.js evals, Review Benchmark | 2026-08-21 | [S41][S5] | maker-claimed |
| Press | SiliconANGLE (2025-09-25, Series B); BusinessWire PR (2025-09-25, timed out on fetch); Fast Company profile; aggregator coverage of Series C (KuCoin, EnterpriseDNA, etc.) | 2026-08-21 | [S14][S35] | press |

## 3. Plugin interface (PRI-2925)

- mcp_support: **client** — `droid mcp add <name> <url> --type http|sse|stdio`, OAuth for HTTP servers, `/mcp` manager, built-in registry of 40+ servers (Figma, Linear, Sentry, Notion, Stripe, Vercel, Playwright, ...), org-managed MCP policy (`mcpAutonomyUrlOverrides`); MCP servers can ship inside plugins (`mcp.json`). No documented mode in which Droid itself serves MCP [S42][S43] (as-of 2026-08-21). Evidence: https://docs.factory.ai/cli/configuration/mcp
- plugin_support: **True** — plugins are directories with `.factory-plugin/plugin.json` plus `commands/`, `skills/`, `droids/`, `hooks/hooks.json`, `mcp.json`; distributed via marketplaces (GitHub/Git URL/local path/npm registry incl. private registries), `droid plugin install <plugin@marketplace>`, `/plugins` UI, user/project/org scopes, git-commit versioning with ref/sha pinning, team auto-install via `extraKnownMarketplaces`/`enabledPlugins`, Enterprise Plugin Registry; official marketplace https://github.com/Factory-AI/factory-plugins (103 stars); separately: Skills (`.factory/skills/<name>/SKILL.md`, merged with custom slash commands), custom droids, AGENTS.md [S43][S44][S45][S46] (as-of 2026-08-21).
- claude_code_plugin: **yes** — docs: "Droid is compatible with plugins built for Claude Code ... the plugin format is interoperable"; both `.factory-plugin/plugin.json` + `droids/` + `mcp.json` and `.claude-plugin/plugin.json` + `agents/` + `.mcp.json` layouts accepted, Claude layouts translated into the plugin cache; `${CLAUDE_PLUGIN_ROOT}` aliased to `${DROID_PLUGIN_ROOT}`; docs example plugin id `security-guidance@claude-plugins-official` [S43][S44] (as-of 2026-08-21). Reads AGENTS.md; CLAUDE.md reading not found in docs snapshot (null).
- subagents: **True** — Task tool with built-in `worker` and `explorer`; custom droids as Markdown files in `.factory/droids/` or `~/.factory/droids/` with own prompt/tools/model/autonomy; foreground or `run_in_background` with `TaskOutput`/`TaskStop`, `resume`, `complexity` routing; subagents cannot nest or ask the user; Missions add an orchestrator-plus-workers multi-agent mode (`/missions`, `droid exec --mission`) [S47][S22] (as-of 2026-08-21). Evidence: https://docs.factory.ai/cli/configuration/custom-droids
- hooks: **True** — events PreToolUse (can block), PostToolUse, UserPromptSubmit, Notification, Stop, SubagentStop, PreCompact, SessionStart, SessionEnd; `type: command` shell hooks with matchers, JSON stdin, exit-code or JSON output; user/project/org-managed/plugin hook locations [S48][S49] (as-of 2026-08-21). Evidence: https://docs.factory.ai/cli/configuration/hooks-guide, https://docs.factory.ai/reference/hooks-reference
- plan_mode: **True** — "Specification Mode" (Shift+Tab): read-only analysis, generates spec + implementation plan, no edits until approval; `droid exec` defaults to read-only spec mode; `--spec-model` for a separate planning model [S32][S33][S50]. Evidence: https://docs.factory.ai/cli/user-guides/specification-mode
- plugin_docs_url: https://docs.factory.ai/cli/configuration/plugins (building: https://docs.factory.ai/guides/building/building-plugins; marketplace repo: https://github.com/Factory-AI/factory-plugins)
- config_docs_url: https://docs.factory.ai/cli/configuration/settings
- ACP support: **yes, first-party** — README: "ACP support for JetBrains IDEs and Zed"; JetBrains installs "Factory Droid" from the ACP registry; Zed extension `factory-droid` (repo Factory-AI/factory-zed-extension, Apache-2.0); release notes: ACP streaming (v0.49.0, 2026-01-13), "ACP daemon mode" (release notes call it "Agent Control Protocol") [S1][S51][S52][S7][S5] (as-of 2026-08-21).
- SDK: **yes** — `@factory/droid-sdk` (TypeScript, v0.7.0; runs the `droid` CLI subprocess or connects to a `droid daemon`; sessions, streaming, tools, skills, MCP, hooks) and `droid-sdk` (Python asyncio, v0.3.0); plus `droid exec` (text/json/stream-json, `--input-format stream-jsonrpc`) and GitHub Action `Factory-AI/droid-action` [S53][S54][S11][S33][S5] (as-of 2026-08-21).

## 4. Claimed differentiation (raw material for PRI-2927)

- tagline (README): "The agent-native development platform. Works across CLI, Web, Slack/Teams, Linear/Jira and Mobile." — https://github.com/Factory-AI/factory [S1]
- tagline (homepage, verbatim short): "The autonomy stack for enterprise teams" / "The industrial revolution for software development" — https://factory.ai [S12]
- tagline (CLI docs): "the power of Factory in your terminal" — https://docs.factory.ai/cli/getting-started/overview [S2]
- maker claims (paraphrased):
  1. Top terminal-benchmark performance: README "top performing in terminal benchmarks"; Series C "#1 across the leading software development agent benchmarks"; Sept 2025 Terminal-Bench #1 attributed to harness design (three-tier prompting, model-specific adaptations, minimal tool set) [S1][S17][S37].
  2. Model independence: "not locked into a single AI provider"; route tasks to the best model; Factory Router; BYOK; Droid Core open-weight pool [S2][S23][S26][S27].
  3. One agent across surfaces with shared memory/config: CLI, desktop, web, IDE (VS Code/JetBrains/Zed), Slack, Linear/Jira, mobile; skills/plugins sync across surfaces [S1][S12-CLI][S21].
  4. Enterprise-first security/governance: SOC 2, ISO 27001/42001, GDPR/CCPA, on-prem, airgapped, LLM gateways, hierarchical org settings capping autonomy, Droid Shield secret scanning, OS sandbox [S2][S20][S28][S55].
  5. Controlled autonomy: Spec Mode before edits, tiered autonomy levels with risk classification, denylist/blocklist, read-only `droid exec` by default [S31][S32][S33].
  6. Delegation over autocomplete; persistent sessions/missions; "Missions" multi-agent orchestration; Droid Computers for long-running remote work [S12-CLI][S22][S25].
  7. "Software Factory" vision: 24/7 agent automations across triage, codegen, validate, release, document, monitor ("Factory 2.0") [S16][S56].
  8. Open plugin ecosystem interoperable with Claude Code plugins; official marketplace [S43][S44].
- audience: "enterprise teams", global systems integrators and AI labs (homepage); "highest-security customers — systemically important banks, governments, healthcare, national security" (enterprise docs); individuals via Pro/Plus/Max plans; engineering leaders (Agent Effectiveness) [S12][S28][S29][S57].

## 5. Company & contact targets (PRI-2929) — company-level only

- legal name: not verified (README copyright "Factory AI"; press releases "Factory") [S1][S19]
- HQ: San Francisco, CA [S16][S19]
- size: null (no public headcount found on company materials; not researched beyond that)
- funding stage: Series C ($150M at $1.5B post, 2026-04-16) [S17]
- publicly named leadership (only as named by the company):
  - Matan Grinberg — Co-founder and CEO (https://factory.ai/news/marcello-gallo-cro, 2026-06-08; also bylines Series C and Factory 2.0 posts) [S19][S17][S56]
  - Eno Reyes — Co-founder (company: "Founded in 2023 by Matan Grinberg and Eno Reyes"; co-byline on Series C/Factory 2.0 posts). "CTO" title appears in press/third-party profiles (Fast Company, The Org), not located on factory.ai [S19][S17][S35]
  - Marcello Gallo — Chief Revenue Officer (appointed 2026-06-08) [S19]
  - Mark Kobe — author of the Factory Partner Network announcement (no title on page); partner inquiries: partners@factory.ai [S24]
  - Terminal-Bench post authors (no titles): Abhay Singhal, Leo Tchourakov, Daniel Flaherty, Stepan Bedratiuk [S37]
  - DevRel / developer relations lead: none found named (researched, absent). Head of Product / CTO page: none found on factory.ai [S16].
- contact: https://factory.ai/contact (sales); partners@factory.ai (partner network); Discord https://discord.gg/zuudFXxg69 [S1][S24][S29]

## 6. Open questions / conflicts

- **Census `droid.md` vs `factory.md`: should be ONE entry.** Both describe the same product line (Droid is Factory's agent; Factory App/web/Slack/Missions are surfaces of the same agent and subscription). Recommend merging into `droid` (maker "Factory AI"), platforms CLI + IDE + Desktop + Web + Autonomous, and redirecting `factory`.
- Census `droid.md` `maker: "Factory-AI"` — that is the GitHub org slug; company name is Factory / Factory AI [S1][S19].
- Census `droid.md` `license: null` / `source_available: True` — proprietary ("All rights reserved"; npm UNLICENSED); repo is docs-only and the CLI is a closed binary: source_available should be False [S1][S3][S6].
- Census `droid.md` `first_released: "2026-07-29"` — that is the GitHub repo creation date; the CLI was public by 2025-09-25 (VS Code extension 2025-09-10; release notes from v0.19.8, Sept/Oct 2025) [S4][S9][S7][S13].
- Census `droid.md` `current_release: "2026-08-17"` — repo push date; CLI is v0.202.0 (Homebrew, 2026-08-21) / npm 0.200.0 (2026-08-20) [S10][S6].
- Census `droid.md` `language: "TypeScript"` — GitHub reports null; product is a native binary (org has a `bun-pty` fork, suggesting Bun, not verified) [S4][S5].
- Census `droid.md` `mcp_support/subagents/hooks/plan_mode/model_providers/pricing/config_docs_url: null` — all filled above (client / True / True / True / multi-vendor / $20-$200 + Business/Enterprise / settings URL).
- Census `droid.md` `plugin_docs_url` points to the GitHub marketplace repo; docs page is https://docs.factory.ai/cli/configuration/plugins.
- Census `droid.md` `claude_code_plugin: False` — docs say Claude Code plugins install directly and are translated: should be **yes** [S43][S44].
- Census `droid.md` prose "Top-performing 'Droid' agent in terminal benchmarks" is a maker claim; independently, Droid's best Terminal-Bench 2.0 row is rank #10 and it has no TB 2.1 entry as of 2026-08-21 [S38][S39].
- Census `factory.md` `platforms: ["Web"]`, `install_method: "Droid CLI via Homebrew (macOS/Linux) or npm (Windows)"` — docs list curl/irm/npm; Homebrew cask exists but is not the documented path [S2][S10]. `first_released: "2024"` not verified from company materials (founded 2023; enterprise rollout stated Sept 2025) [S19][S13].
- Terminal-Bench conflict: docs benchmark page shows "Factory Droid #1 63.1% (Dec 2025)" on TB 2.0, but tbench.ai TB 2.0 now lists that 63.1% row at rank 34 and Droid's best at rank 10 (77.3%, GPT-5.3-Codex) [S40][S38].
- Live docs release-notes page paginates (oldest visible entry June 3 2026, v0.140.0) while the raw snapshot in raw-droid/ goes back to v0.19.8 (Sept/Oct 2025); labels carry no year [S7].
- npm `droid` package name was created 2013-09-30 (unrelated 0.0.1); Factory's first publish is 0.57.5 on 2026-02-05 — npm-based age/download history before Feb 2026 is not attributable to Factory [S6].
- Starting Autonomy Level for a fresh install is not explicit in the docs snapshot (docs describe Off/Low/Medium/High and say Off keeps manual approvals) [S31][S34].
- Unreachable: businesswire.com Series B release (timeout), openai.com/index/factory (403), Zed extension download count (API empty). Discord count is a live invite snapshot.
- "Revenue doubled month-over-month for six months" and "hundreds of thousands of developers" have no absolute base figure; no independent revenue figure found [S17].
- Employee headcount and legal entity name: not found on company materials.

## 7. Sources

1. [S1] https://github.com/Factory-AI/factory (README via raw) — tagline, install, ACP, SDKs, Discord, copyright
2. [S2] https://docs.factory.ai/cli/getting-started/overview — CLI install, capabilities, "why teams choose Factory"
3. [S3] https://api.github.com/repos/Factory-AI/factory/contents/ — repo tree (README, docs, .github)
4. [S4] https://api.github.com/repos/Factory-AI/factory (+contributors, commits, search/issues, releases) — stars, dates, license null
5. [S5] https://api.github.com/orgs/Factory-AI/repos (raw-droid/org-repos.json) + per-repo API — satellite repos, stars, licenses
6. [S6] https://registry.npmjs.org/droid — versions, publish dates, UNLICENSED, binary optionalDependencies
7. [S7] https://docs.factory.ai/changelog/release-notes (live + raw snapshot) — version history, feature first-mentions
8. [S8] https://api.npmjs.org/downloads/point/last-week|last-month/droid and @factory/droid-sdk — npm downloads
9. [S9] https://marketplace.visualstudio.com/_apis/public/gallery/extensionquery (Factory.factory-vscode-extension); https://plugins.jetbrains.com/api/searchPlugins?search=Factory%20Droid — installs/downloads
10. [S10] https://formulae.brew.sh/api/cask/droid.json and /api/analytics/cask-install/{30d,90d,365d}.json — cask version 0.202.0, installs
11. [S11] https://pypistats.org/api/packages/droid-sdk/recent; https://pypi.org/pypi/droid-sdk/json — Python SDK downloads, version
12. [S12] https://factory.ai — taglines, logos, audience; [S12-CLI] https://factory.ai/product/cli — CLI claims, quotes
13. [S13] https://factory.ai/news/series-b — $50M/$300M, customers, outcome claims, Terminal-Bench #1
14. [S14] https://siliconangle.com/2025/09/25/factory-unleashes-droids-software-agents-50m-fresh-funding/ — press on Series B, CEO title
15. [S15] https://discord.com/api/v9/invites/zuudFXxg69?with_counts=true — Discord member count
16. [S16] https://factory.ai/company — mission, HQ, investors, advisors
17. [S17] https://factory.ai/news/series-c — $150M/$1.5B, investors, usage/revenue claims, customers, bylines
18. [S18] https://factory.ai/news — post index, case studies
19. [S19] https://factory.ai/news/marcello-gallo-cro — CRO, CEO title, founded 2023, HQ, customers incl. Revolut
20. [S20] https://factory.ai/enterprise — compliance list, logos, outcome numbers, CTO quotes
21. [S21] https://docs.factory.ai/web/getting-started/overview — Factory App downloads/platforms
22. [S22] https://docs.factory.ai/features/missions/overview — Missions
23. [S23] https://factory.ai/news/software-factory — Factory 2.0, Router, Missions, Droid Computers, customers
24. [S24] https://factory.ai/news/factory-partner-network — $100M partner network, contact
25. [S25] https://docs.factory.ai/cli/features/droid-computers — Droid Computers (managed/BYOM)
26. [S26] https://docs.factory.ai/models — model list and multipliers
27. [S27] https://docs.factory.ai/cli/byok/overview — BYOK (CLI only)
28. [S28] https://docs.factory.ai/enterprise — enterprise deployment, audience, compliance
29. [S29] https://docs.factory.ai/pricing — plans, rate limits, Droid Core, Extra Usage
30. [S30] https://factory.ai/pricing — public plan prices, "no free tier", model statement
31. [S31] https://docs.factory.ai/cli/user-guides/auto-run — autonomy levels, lists, defaults
32. [S32] https://docs.factory.ai/cli/user-guides/specification-mode — Spec Mode
33. [S33] https://docs.factory.ai/cli/droid-exec/overview — headless mode, read-only default, flags
34. [S34] https://docs.factory.ai/cli/configuration/settings — sessionDefaultSettings, command lists; https://docs.factory.ai/cli/configuration/sandbox — OS sandbox beta
35. [S35] web search results (KuCoin, EnterpriseDNA, theaiworld, Fast Company, The Org, Crunchbase) — total raised, CTO title (press only)
36. [S36] https://factory.ai/news/factory-guild — community program
37. [S37] https://factory.ai/news/terminal-bench — Sept 2025 Terminal-Bench claims, harness design, authors
38. [S38] https://www.tbench.ai/leaderboard/terminal-bench/2.0 — Droid rows and ranks
39. [S39] https://www.tbench.ai/leaderboard/terminal-bench/2.1 — no Droid rows
40. [S40] https://docs.factory.ai/benchmarks/terminal-bench — maker benchmark page
41. [S41] https://docs.factory.ai/benchmarks/* (agent-arena, legacy-bench, nextjs-eval, review-benchmark) — other benchmark pages
42. [S42] https://docs.factory.ai/cli/configuration/mcp — MCP client details
43. [S43] https://docs.factory.ai/cli/configuration/plugins — plugin format, marketplaces, Claude Code compatibility
44. [S44] https://docs.factory.ai/guides/building/building-plugins — layouts, npm registries, CLAUDE_PLUGIN_ROOT alias
45. [S45] https://docs.factory.ai/cli/configuration/skills — skills format
46. [S46] https://docs.factory.ai/enterprise/enterprise-plugin-registry — enterprise registry
47. [S47] https://docs.factory.ai/cli/configuration/custom-droids — subagents
48. [S48] https://docs.factory.ai/cli/configuration/hooks-guide — hook events
49. [S49] https://docs.factory.ai/reference/hooks-reference — hook reference
50. [S50] https://docs.factory.ai/reference/cli-reference — commands, flags, `droid daemon`
51. [S51] https://docs.factory.ai/integrations/jetbrains — ACP install
52. [S52] https://docs.factory.ai/integrations/zed — Zed ACP extension
53. [S53] https://github.com/Factory-AI/droid-sdk-typescript (README via raw) — TS SDK capabilities
54. [S54] https://registry.npmjs.org/@factory/droid-sdk — SDK version/dates
55. [S55] https://docs.factory.ai/cli/account/droid-shield — Droid Shield
56. [S56] https://factory.ai/news/software-factory — bylines (Grinberg, Reyes)
57. [S57] https://factory.ai/news/agent-effectiveness — analytics feature, audience
58. https://docs.factory.ai/integrations/ide-integrations — VS Code/JetBrains features
59. https://docs.factory.ai/web/software-factory — Software Factory private preview
60. https://factory.ai/news/nvidia-dgx-spark — Nemotron/DGX Spark airgapped announcement (2026-08-11)

## Inclusion check (Jesse's test)

**Yes** — Droid is Factory's own agent with its own agentic loop (Read/Edit/Execute/Task tools, autonomy-tiered approvals, subagents, Missions), shipped as a closed binary and exposed via CLI, `droid exec`, SDKs and ACP; the Sept 2025 Terminal-Bench post describes Factory's own harness design [S37][S33][S47].
