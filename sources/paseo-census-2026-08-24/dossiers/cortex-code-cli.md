# Dossier: Cortex Code / Snowflake CoCo (census_slug: cortex-code-cli)

Compiled 2026-08-21 (research run 2026-08-24 clock; treat as-of dates below as authoritative). Facts only. Null convention: "null = not researched"; "False/none = researched and absent". Sources [Sn] in section 7.

IMPORTANT framing: the census entry conflates two artifacts. (a) **Cortex Code CLI** (`cortex`, docs now call the product "Snowflake CoCo") — Snowflake's closed-binary coding agent, the harness Paseo drives via `cortex acp serve`. (b) **snowflake-ai-kit** — a small open-source *plugin/installer* repo that routes prompts from Claude Code/Codex INTO Cortex Code. This dossier is about (a); (b) is covered as its plugin ecosystem.

## 1. Identity

- name: Cortex Code (product marketing now "Snowflake CoCo"; CLI surface "CoCo CLI" / Cortex Code CLI) [S1][S8]
- maker: Snowflake Inc. (public company, NYSE: SNOW; HQ Menlo Park, CA, USA — relocated 2025, previously Bozeman, MT) [S13]
- product URL: https://www.snowflake.com/en/product/features/cortex-code/ [S8]; docs https://docs.snowflake.com/en/user-guide/cortex-code/cortex-code (overview) and .../cortex-code-cli (CLI) [S1][S2]
- repo URL: none for the CLI itself (closed binary; researched, absent). Companion repos: https://github.com/Snowflake-Labs/snowflake-ai-kit (plugin+installer, Apache-2.0 with skills under "Snowflake Skills License") [S3][S4]; https://github.com/Snowflake-Labs/subagent-cortex-code (predecessor router, last push 2026-05-05) [S5]
- license: CLI = proprietary Snowflake product (no public source or license file found; researched, absent). ai-kit repo = Apache-2.0 (code) + Snowflake Skills License (skills) [S3][S4]
- open source? **False** for the harness. source_available: **partial at best** — only the routing plugin/installer and skills are public; the `cortex` binary is distributed via Snowflake's install script [S1][S3]
- first public release: Cortex Code debuted in **private preview November 2025** (BUILD); CLI **GA 2026-02-03** (press release; earliest changelog entry v1.0.6, 2026-02-04) [S6][S9][S16]
- latest release: **v1.1.65, 2026-08-11** (docs changelog; ~weekly-biweekly cadence) [S9] (as-of 2026-08-21)
- what it is:
  - Form factors: CLI (macOS arm64/x64, Linux x64/arm64, Windows WSL + native); CoCo Desktop (macOS/Windows IDE, GA); CoCo in Snowsight (web, GA); VS Code via Snowflake extension (private preview per Apr 2026 PR); ACP mode for Zed/JetBrains/Neovim (preview); CoCo Agent SDK Python/TS (preview); Cloud Agents (private preview) [S1][S2][S7][S8]
  - Models: Snowflake-hosted multi-model via Cortex — Claude Opus 5, Claude Sonnet 5, Claude Opus 4.8/4.7/4.6, Claude Sonnet 4.6/4.5/4.0, OpenAI GPT 5.5 (preview)/5.4/5.2; `auto` picks "highest quality model available to your account"; cross-region inference. No BYO API keys documented (all inference billed through Snowflake) [S1][S8]
  - Pricing: individual self-serve subscription **$20 USD/month** after a 30-day trial with **$40 free inference credits** (signup.snowflake.com/cortex-code — Snowflake's "first standalone subscription", Feb 2026); enterprise customers pay-as-you-go token/credit consumption on their Snowflake account; per-user daily credit limits settable by admins [S8][S10][S11][S6b]
  - Install: `curl -LsS https://ai.snowflake.com/static/cc-scripts/install.sh | sh` (macOS/Linux/WSL, to ~/.local/bin) or `irm https://ai.snowflake.com/static/cc-scripts/install.ps1 | iex` (Windows native). No Homebrew formula/cask found (researched, absent) [S1][S12]. The ai-kit repo README also lists `bash install.sh` / `.\install.ps1` / `npx @snowflake-labs/ai-kit`, but the npm package `@snowflake-labs/ai-kit` returns "not found" on the npm registry (see section 6) [S3][S14]
  - Default autonomy: permission prompts with envelope-based permission policy (ai-kit ships "envelope" policies); plan mode asks confirmation before executing actions; hooks can block tools; requires a configured Snowflake connection (`~/.snowflake/connections.toml`) and CORTEX_USER/CORTEX_AGENT_USER role; admin "managed settings enforcement" added v1.1.65 [S1][S2][S3][S9]
  - Specialization: **data-engineering / Snowflake-native** — SQL, dbt, Airflow, dynamic tables, governance, lineage, cost intelligence, ML, Streamlit, notebooks (55+ bundled skills); Feb 2026 expansion targets "any data, anywhere" (dbt, Airflow GA; AWS Glue, Databricks, Postgres, Spark support announced Apr 2026) [S3][S6b][S7][S15]

## 2. Adoption evidence

| metric / claim | value | as-of | source | type |
|---|---|---|---|---|
| Cortex Code active use | "more than 50 percent of customers" since Nov 2025 launch (customer base "over 13,900") | 2026-04-21 | [S7] | maker-claimed |
| New users | "over 4,400 new users" since Nov 2025 launch | 2026-02-23 | [S6b] | maker-claimed |
| Snowflake AI products weekly customers | 9,100 customers weekly (all AI products, not CoCo alone) | 2026-04-21 | [S7] | maker-claimed |
| Claude Code plugin installs (snowflake-cortex-code) | 1,784 installs on claude.com marketplace | 2026-08-21 | [S14b] | independently observable |
| GitHub stars: Snowflake-Labs/snowflake-ai-kit | 35 stars, 12 forks, 5 contributors, 36 commits last 90 days; created 2026-03-10; last push 2026-08-13; 0 releases | 2026-08-21 | [S4] | independently observable |
| GitHub stars: Snowflake-Labs/subagent-cortex-code | 57 stars, 8 forks; created 2026-04-08, last push 2026-05-05 (appears superseded by ai-kit) | 2026-08-21 | [S5] | independently observable |
| npm downloads @snowflake-labs/ai-kit | package not found on registry (404) | 2026-08-21 | [S14] | independently observable (absent) |
| Homebrew | no formula/cask found | 2026-08-21 | [S12] | independently observable (absent) |
| Named customers (launch PR) | Braze, Decile, dentsu, FYUL, LendingTree, Shelter Mutual Insurance, TextNow, United Rentals, WHOOP | 2026-02-03 | [S6] | maker-claimed |
| Product-page logos | WHOOP, United Rentals, Shelter Mutual Insurance, Under Armour | 2026-08-21 | [S8] | maker-claimed |
| Customer outcomes | one customer: "over 500 hours in time saving — roughly $100,000" in first 20 days; TS Imagine: "5x more pull requests", 3-4 days → 2-3 hours | 2026-02-23 / 2026-03-26 | [S6b][S15] | maker-claimed |
| Accenture | "thousands of Accenture practitioners active on the platform", ~two dozen purpose-built skills | 2026-04-21 | [S7] | partner-claimed (quoted by maker) |
| Benchmark (maker-run) | 65% accuracy on dbt tasks vs 58% for Claude Code, "nearly 50% fewer total calls" | 2026-02-23 | [S6c] | maker-claimed |
| Funding/company | public company; FY2026 revenue $4.68B (FY ended 2026-01-31); 9,060 employees | 2026-01-31 | [S13] | independently observable (filings/Wikipedia) |
| Community | no Discord/subreddit found for Cortex Code specifically; third-party tutorials exist (DEV Community guide on skills/subagents/hooks/MCP; Flexera, Seemore Data, digitalapplied blog coverage) | 2026-08-21 | [S17] | independently observable |
| Press | BusinessWire carried both major releases; Constellation Research covered Apr 2026 expansion | 2026-08-21 | [S6][S7][S17] | press |

Note the tension between ">50% of ~13,900 customers" (Cortex Code across all surfaces, incl. free Snowsight usage) and "4,400+ new users" (Feb, likely CLI/standalone signups) — different denominators; treat the 50% figure as the marketing headline and the 4,400 as the concrete count.

## 3. Plugin interface (PRI-2925)

- mcp_support: **client** (preview) — `cortex mcp` CLI + `/mcp` slash command; central registry `~/.snowflake/cortex/mcp.json`; OAuth (tokens in `~/.snowflake/cortex/mcp_oauth/`), OAuth client secrets (v1.1.52), zero-config auth to MCP servers on Snowpark Container Services (v1.1.65). Not documented as an MCP *server* itself (Snowflake's managed MCP servers are a separate platform feature). Evidence: https://docs.snowflake.com/en/user-guide/cortex-code/cortex-code-mcp [S2][S9][S18]
- plugin_support: **True** (preview) — plugins = manifest at `.cortex-plugin/plugin.json` **or** `.claude-plugin/plugin.json` + `skills/`, `agents/`, `commands/`, `hooks/hooks.json`, `.mcp.json`; install via `cortex plugin install` from official CoCo marketplace, GitHub shorthand (`owner/repo@branch`), or git URLs. Separate skills system: SKILL.md + YAML frontmatter; sources BUNDLED (55+ ship with binary) / GLOBAL (`~/.snowflake/cortex/skills/`) / EXTERNAL (`cortex skill add <path|owner/repo>`) / PROJECT / session / remote-git; `/skill` manager; skill/plugin sharing via Snowflake stages (cortex-code-skill-plugin-sharing docs page). Evidence: https://docs.snowflake.com/en/user-guide/cortex-code/cortex-code-plugins and .../extensibility [S18][S19][S3]
- claude_code_plugin: **yes (bidirectional, partial)** — (1) CoCo *reads Claude Code formats*: `.claude-plugin/plugin.json` manifests, `.claude/skills/`, `.claude/agents/`, `.claude/settings.json` + settings.local.json for hooks; v1.1.53 "configuration reuse from existing Claude Code setups". CLAUDE.md/AGENTS.md support not documented (null). (2) Snowflake *ships a Claude Code plugin* (`snowflake-cortex-code@claude-plugins-official`, 1,784 installs) that routes Snowflake prompts from Claude Code into Cortex Code; Codex marketplace variant too; Cursor via "Third-party skills" [S19][S9][S3][S14b]
- subagents: **True** — built-in `general-purpose`, `explore` (3 thoroughness modes), `plan`, `feedback`, plus `data-discovery` (v1.1.65); custom agents as Markdown+frontmatter (name/description/tools/model) in `.cortex/agents/`, `.claude/agents/`, `~/.snowflake/cortex/agents/`, `~/.claude/agents/`; automatic delegation, explicit/parallel/background invocation, worktree isolation; max 50 concurrent background agents; `/agents` (Ctrl-B), kill/resume; "Agent Teams" multiagent orchestration announced 2026-03-26. Evidence: https://docs.snowflake.com/en/user-guide/cortex-code/extensibility [S19][S15][S9]
- hooks: **True** — events PreToolUse (blocking), PostToolUse, PermissionRequest (blocking), UserPromptSubmit, SessionStart, SessionEnd, PreCompact, Stop, SubagentStop; handler types: command (shell, 60s default timeout, JSON stdin/stdout with allow/block decision + updatedInput) and prompt (LLM-evaluated, 30s); tool matchers (`Bash`, `SQL*`, `Edit|Write`, `mcp__.*`); configured in `.cortex/` or `.claude/` settings.json files or `~/.snowflake/cortex/hooks.json`. Evidence: extensibility docs [S19]
- plan_mode: **True** — CLI docs list plan mode (asks confirmation before executing actions) and a built-in `plan` subagent; "Cloud Agents with Plan Mode" in private preview (Apr 2026) [S1][S19][S7]
- plugin_docs_url: https://docs.snowflake.com/en/user-guide/cortex-code/cortex-code-plugins (extensibility: https://docs.snowflake.com/en/user-guide/cortex-code/extensibility)
- config_docs_url: https://docs.snowflake.com/en/user-guide/cortex-code/cortex-code-cli (connections.toml; credit limits: https://docs.snowflake.com/en/user-guide/cortex-code/credit-usage-limit)
- ACP support: **yes, first-party (preview)** — `cortex acp serve -c <connection_name>`; documented editors Zed, JetBrains, Neovim (VS Code users directed to the Snowflake extension instead); streams messages/tool calls/file diffs over stdio; can call client-exposed tools; prompt cancellation; `unstable_listSessions`; no separate auth flow (uses pre-configured Snowflake connections); slash commands not exposed over ACP. Evidence: https://docs.snowflake.com/en/user-guide/cortex-code/cortex-code-acp [S20]. This is what Paseo drives.
- SDK: **yes (preview)** — CoCo Agent SDK, Python + TypeScript, "framework for building agentic applications"; announced 2026-04-21. Evidence: https://docs.snowflake.com/en/user-guide/cortex-code-agent-sdk/cortex-code-agent-sdk [S2][S7]

## 4. Claimed differentiation (raw material for PRI-2927)

- tagline (product page, verbatim): "Your data-native AI coding agent. Turn your complex data engineering, analytics and AI workflows into simple conversations." — https://www.snowflake.com/en/product/features/cortex-code/ [S8]
- launch PR headline claim: an AI coding agent "that drastically increases productivity by understanding your enterprise data context" [S6]
- maker claims (paraphrased):
  1. Enterprise-data context from the first prompt: knows the catalog, lineage, RBAC and pipeline dependencies; code is grounded in governance policies and permissions [S8][S6]
  2. Data-specialized built-in tooling: semantic catalog search, data diffing, sandboxed runtimes, 55+ bundled skills (SQL, governance, dynamic tables, ML, cost intelligence, dbt, notebooks, security investigation) [S8][S3]
  3. Secure by design: runs inside Snowflake's security/governance perimeter; RBAC-honoring; admin cost controls with per-user daily credit quotas [S6][S8][S11]
  4. Multi-model with auto-selection: Claude Opus/Sonnet families + OpenAI GPT, `auto` picks the best model available to the account [S1][S8]
  5. Works beyond Snowflake: dbt and Airflow GA; AWS Glue, Databricks, Postgres, Spark; "any data, anywhere"; standalone $20/mo subscription needs no Snowflake deployment [S6b][S6c][S7]
  6. Many surfaces, interoperable: Snowsight, Desktop, CLI, VS Code, "30+ editor integrations" (ACP), Agent SDK; ships as plugins for Claude Code and Codex, works in Cursor [S8][S20][S3]
  7. Performance vs. general agents: 65% vs Claude Code's 58% on dbt tasks with ~50% fewer calls (maker-run) [S6c]
  8. Multiagent orchestration: subagents/Agent Teams coordinating work across dbt, Airflow, Postgres, Spark, Glue [S8][S15]
- audience: enterprise data teams — data engineers, analytics engineers, BI professionals; expanded to individual developers via self-serve subscription [S8][S6b]

## 5. Company & contact targets (PRI-2929) — company-level only

- legal name: Snowflake Inc.; public (NYSE: SNOW), IPO Sept 2020 [S13]
- HQ: Menlo Park, CA (since 2025; formerly Bozeman, MT as principal executive office) [S13]
- size: 9,060 employees (as of 2026-01-31); FY2026 revenue $4.68B [S13]
- funding stage: public company [S13]
- publicly named leadership (snowflake.com leadership page + PR/blog bylines):
  - Sridhar Ramaswamy — CEO [S21][S13]
  - Christian Kleinerman — EVP Product (quoted in both Cortex Code press releases; the product-side contact tier) [S21][S6][S6b]
  - S. Muralidhar — CTO [S21]
  - Vivek Raghunathan — SVP Engineering [S21]
  - Baris Gultekin — VP of AI (quoted in Apr 2026 Cortex Code/Intelligence PR) [S7]
  - Umesh Unnikrishnan — Developer Experiences Lead (bylined the Feb 2026 CLI expansion blog; closest to a DevRel contact publicly named) [S6c]
  - Aria Attar — Senior Product Manager (same byline) [S6c]
  - Siddharth Dwivedi — AI Product Marketing (bylines Feb + Mar 2026 blogs) [S6c][S15]
  - Denise Persson — CMO; Brian Robins — CFO; Jon Beaulier — CRO [S21]
- head of partnerships/ecosystem: none found named on the leadership page (researched, absent at that page; Accenture relationship surfaced via PR quote) [S21][S7]

## 6. Open questions / conflicts

- Census `maker: null` → Snowflake Inc. [S13]
- Census `license: "Apache-2.0 (CLI); Snowflake Skills License (skills)"` → **wrong attribution**: Apache-2.0 covers the *snowflake-ai-kit plugin repo*, not the CLI. The `cortex` CLI is a closed proprietary binary with no public license file found [S3][S4].
- Census `source_available: "Yes"` → overstates. Only the routing plugin/installer + skills are open; the harness itself is closed. Suggest "partial (plugin/installer only)" [S3][S1].
- Census `source_code_url: null` + `download_url: github.com/Snowflake-Labs/snowflake-ai-kit` → that repo is the plugin, not the CLI download; official CLI install is the ai.snowflake.com script [S1].
- Census `install_method: "bash install.sh / ./install.ps1 / npx @snowflake-labs/ai-kit"` → those are the *ai-kit plugin* installers; and `@snowflake-labs/ai-kit` is **not on the npm registry** (404 on 2026-08-21) despite the README advertising `npx` [S3][S14]. The harness's own install is the curl/irm script [S1].
- Census `language: "Python"` → that is the ai-kit repo's GitHub language; the CLI binary's implementation language is not public (null) [S4].
- Census `first_released`/`current_release`/`mcp_support`/`subagents`/`hooks`/`plan_mode`/`model_providers`/`pricing`/`homepage`/`plugin_docs_url`/`config_docs_url`: null → filled above (Nov 2025 preview / CLI GA 2026-02-03; v1.1.65 2026-08-11; client; yes; yes; yes; Snowflake-hosted Claude+OpenAI; $20/mo or PAYG) [S1][S6][S9].
- Census `url: snowflake.com/en/product/cortex-code/` → live product page is /en/product/features/cortex-code/ (redirect not verified) [S8].
- Census `what_makes_it_special` is written from the ai-kit plugin README (55+ skills, ~50ms keyword filter) — accurate for the plugin, but the census entry should represent the harness; recommend re-anchoring on the CLI itself.
- Adoption-number tension: ">50% of customers actively leveraging" Cortex Code (Apr 2026) vs "4,400+ new users" (Feb 2026) — different denominators/surfaces; neither independently verifiable [S7][S6b].
- The dbt benchmark (65% vs 58% vs Claude Code) is maker-run with no published methodology found [S6c].
- Product renamed/rebranded to "Snowflake CoCo" in docs and product pages; press releases still say "Cortex Code"; exact rename date not established (null).
- CLI GA status vs sub-feature preview labels: CLI itself GA, but MCP/ACP/plugins/Agent SDK are marked Preview on the docs overview page [S2].
- pypistats/npm for any `cortex`/SDK packages: not researched (null) beyond ai-kit 404.

## 7. Sources

1. [S1] https://docs.snowflake.com/en/user-guide/cortex-code/cortex-code-cli — CLI install, models, plan mode, prerequisites, config
2. [S2] https://docs.snowflake.com/en/user-guide/cortex-code/cortex-code — overview, surfaces, GA/preview matrix, billing split, doc tree
3. [S3] https://raw.githubusercontent.com/Snowflake-Labs/snowflake-ai-kit/main/README.md — plugin routing, 55+ skills, installers, licenses
4. [S4] https://api.github.com/repos/Snowflake-Labs/snowflake-ai-kit — stars/forks/license/dates/contributors/commits
5. [S5] https://api.github.com/repos/Snowflake-Labs/subagent-cortex-code — predecessor router repo stats
6. [S6] https://www.snowflake.com/en/news/press-releases/snowflake-unveils-cortex-code-an-ai-coding-agent-that-drastically-increases-productivity-by-understanding-your-enterprise-data-context/ — 2026-02-03 GA PR, customers, Kleinerman quote
7. [S6b] https://www.snowflake.com/en/news/press-releases/snowflake-cortex-code-expands-towards-supporting-any-data-anywhere/ — 2026-02-23 PR: 4,400+ users, subscription, dbt/Airflow
8. [S6c] https://www.snowflake.com/en/blog/cortex-code-cli-expands-support/ — dbt benchmark vs Claude Code, bylines, $100k customer claim
9. [S7] https://www.snowflake.com/en/news/press-releases/snowflake-expands-snowflake-intelligence-and-cortex-code-to-power-the-control-plane-for-the-agentic-enterprise/ — 2026-04-21: >50% adoption, Agent SDK, ACP, Glue/Databricks/Postgres, Gultekin
10. [S8] https://www.snowflake.com/en/product/features/cortex-code/ — tagline, $20/mo + $40 credits, models, logos, differentiation
11. [S9] https://docs.snowflake.com/en/user-guide/cortex-code/changelog — v1.0.6 (2026-02-04) → v1.1.65 (2026-08-11), Claude Code config reuse, managed settings
12. [S10] web search results (seemoredata.io guide quoting signup terms) — $20/mo after 30 days, third-party corroboration
13. [S11] https://docs.snowflake.com/en/user-guide/cortex-code/credit-usage-limit — per-user daily credit limits
14. [S12] https://formulae.brew.sh/api/cask/cortex.json (+formula) — 404, no Homebrew
15. [S13] https://en.wikipedia.org/wiki/Snowflake_Inc. — legal name, HQ, employees, revenue, ticker, CEO
16. [S14] https://registry.npmjs.org/@snowflake-labs/ai-kit — package not found; [S14b] https://claude.com/plugins/snowflake-cortex-code — 1,784 installs
17. [S15] https://www.snowflake.com/en/blog/cortex-code-snowsight/ — 2026-03-26: Snowsight GA, Agent Teams, TS Imagine 5x PRs
18. [S16] web search (softwarereviews.com et al.) — Nov 2025 private preview debut
19. [S17] https://dev.to/tsubasa_tech/supercharge-cortex-code-cli-a-practical-guide-to-skills-subagents-hooks-and-mcp-lc8 (found via search) + Flexera/Seemore/digitalapplied posts — third-party coverage
20. [S18] https://docs.snowflake.com/en/user-guide/cortex-code/cortex-code-plugins — plugin manifest (.cortex-plugin/.claude-plugin), install sources
21. [S19] https://docs.snowflake.com/en/user-guide/cortex-code/extensibility — skills/subagents/hooks details, .claude/ compatibility
22. [S20] https://docs.snowflake.com/en/user-guide/cortex-code/cortex-code-acp — `cortex acp serve`, Zed/JetBrains/Neovim
23. [S21] https://www.snowflake.com/en/company/overview/leadership-and-board/ — executive names/titles

## Inclusion check (Jesse's test)

**Yes** — Cortex Code CLI is a first-party agent with its own agentic loop (orchestrates skills, subagents, MCP tools, file edits and command/SQL execution against local repos and Snowflake; exposes that loop over ACP via `cortex acp serve` and as the CoCo Agent SDK) [S1][S19][S20]. The *snowflake-ai-kit plugin* is NOT itself a harness (it routes other agents' prompts into Cortex Code) — the census entry should be understood as the CLI, not the plugin. Specialization: data-engineering/Snowflake-focused (general coding is possible but the product is positioned and skill-stacked for data workflows).
