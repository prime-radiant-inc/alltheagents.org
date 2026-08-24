# Dossier: CodeBuddy Code (proposed census_slug: codebuddy-code)

Compiled 2026-08-24 (task dated 2026-08-21). Facts only. Null convention: "null = not researched"; "False/none = researched and absent". Sources [Sn] in section 7.

NOT currently in the census. The existing census slug `codebuddy` is an unrelated archived open-source project by olasunkanmi-SE (GitHub) and must not be conflated with this product; hence the proposed slug `codebuddy-code`.

Family context: "CodeBuddy" is a Tencent Cloud product family with three form factors — IDE plugin (VS Code/JetBrains, formerly "Tencent Cloud AI Code Assistant"), a standalone CodeBuddy IDE, and the CLI agent **CodeBuddy Code** [S9][S12]. This dossier's subject is the CLI, with family context where numbers are family-level. There is a China site (codebuddy.cn / copilot.tencent.com, Hunyuan/DeepSeek models, CNY pricing) and an international site (codebuddy.ai / tencentcloud.com, GPT/Gemini and at times Claude) [S6][S12][S13].

## 1. Identity

- name: CodeBuddy Code
- maker: Tencent Cloud (Tencent Holdings Ltd., public company; HQ Shenzhen, China) [S9][S12]
- product URL: https://www.codebuddy.cn/cli/ (CN) and https://www.codebuddy.ai (international); intl product page https://www.tencentcloud.com/products/acc [S1][S9]
- repo URL: https://cnb.cool/codebuddy/codebuddy-code (Tencent's CNB code-hosting platform; this is the issues/docs repo — README states MIT, but the npm package license field says "SEE LICENSE IN README.md" and the shipped CLI is not published as source) [S2][S3]
- license: ambiguous — cnb.cool repo README shows MIT; npm license field "SEE LICENSE IN README.md" [S2][S3] (as-of 2026-08-24). Treat product as proprietary with a source-hosting repo; see section 6.
- open source? source_available: partial at most — repo exists on cnb.cool (123 stars, 75 forks, 1,029 commits, 4 contributors, 781 open issues) but npm tarball is the distribution; core agent source availability unverified [S2] (as-of 2026-08-24).
- first public release: CLI — first npm publish 0.0.1-beta.0 on 2025-08-05 [S3]; official public launch 2025-09-09 ("first in China to support plugin + IDE + CLI forms") [S8][S12]. Family — original assistant opened to public 2024-05-22; Craft agent Apr 2025; MCP support May 2025 (claimed first Chinese code assistant with MCP); CodeBuddy IDE public beta 2025-08-21 (CN) / 2025-09-09 (open beta) [S12].
- latest release: npm 2.138.0, published 2026-08-24T15:27Z; 1,205 versions on npm; near-daily dev builds [S3]. CodeBuddy Code 2.0 (Jan 2026) added Skills, Plan Mode, ACP protocol, open SDK, sandboxed execution [S12][S17].
- what it is:
  - Form factor: terminal CLI agent (`codebuddy` / `cbc` binaries; npm `@tencent-ai/codebuddy-code`, Node.js 18+); headless mode and HTTP API (beta); Unix-pipeline composable [S3][S4][S16]. Family also ships IDE plugins and a standalone IDE [S9].
  - Models: CN version runs Tencent Hunyuan (incl. Hy3) and DeepSeek; international version has offered Claude/GPT/Gemini — Baike records the intl IDE removing Claude and moving to GPT-5/Gemini-2.5-Pro on 2025-10-01 [S12][S13]. `--model` flag exists (docs example "sonnet") [S2]. Not BYO-open per docs read; endpoint-config env work visible in npm dist-tags [S3].
  - Pricing (CN, family-level): free experience tier; personal plans re-tiered 2026-07-01 into Standard/Premium/Flagship, Standard from ~¥99/mo (~¥70 on monthly promo); enterprise SaaS ¥198/seat/mo and private-cloud ¥316/seat/mo since 2026-05-15; limited-time free Hy3 calls through 2026-08-31 [S12][S14]. International pricing page unreadable (JS-only) — null [S15].
  - Install: `npm install -g @tencent-ai/codebuddy-code` [S2][S3].
  - Default autonomy: docs overview does not state ask-before-edit default; permission system exists (PermissionRequest/PermissionDenied hook events, permission modes incl. plan and "plan + bypass" combinations, sandboxed execution since 2.0) [S4][S5][S17]. null on exact default.
  - Deep design similarity to Claude Code: CODEBUDDY.md memory file, `.codebuddy/settings.json`, plugins/skills/agents/hooks layouts, and explicit Claude Code plugin-format compatibility [S5][S7].

## 2. Adoption evidence

| metric / claim | value | as-of | source | type |
|---|---|---|---|---|
| npm weekly downloads, @tencent-ai/codebuddy-code | 80,047 (2026-08-17..23) | 2026-08-23 | [S3b] | independently observable |
| npm monthly downloads, same | 479,033 (2026-07-25..08-23) | 2026-08-23 | [S3b] | independently observable |
| npm versions published / cadence | 1,205 versions since 2025-08-05; multiple dev builds daily, 2.138.0 on 2026-08-24 | 2026-08-24 | [S3] | independently observable |
| VS Code Marketplace installs (Tencent-Cloud.coding-copilot — family IDE plugin, not CLI) | 598,258 installs; 119 ratings avg 4.12; updated 2026-08-20 | 2026-08-24 | [S10] | independently observable |
| JetBrains Marketplace downloads (plugin 24379 "Tencent Cloud CodeBuddy" — family) | 507,188 | 2026-08-24 | [S11] | independently observable |
| cnb.cool repo | 123 stars, 75 forks, 781 open issues, 1,029 commits, 4 contributors | 2026-08-24 | [S2] | independently observable (Tencent-owned platform) |
| Tencent internal engineers using CodeBuddy family | ">95% of Tencent's engineers"; overall coding time -40% | 2026-06-05 | [S9b] | maker-claimed |
| Tencent internal R&D on CodeBuddy (earlier figure) | ">50% of Tencent's internal R&D personnel" | page live 2026-08-24 (undated claim) | [S9] | maker-claimed |
| CodeBuddy Code (CLI) internal adoption | 12,000 engineers within Tencent; also >10,000 non-technical Tencent employees using CodeBuddy | 2026-01 | [S12] | maker-claimed (via Baidu Baike citing Tencent) |
| External enterprise customers | "over 50 well-known external enterprises" | 2026-01 | [S12] | maker-claimed |
| AI-written share of code | 30% of Tencent code (Apr 2024, family); "90% of new CodeBuddy Code code written by itself" (Jan 2026) | 2026-01 | [S12] | maker-claimed |
| Third-party integrations | ACP client ecosystem: Zed config documented; Vibe-Kanban added Tencent CodeBuddy CLI (PR #1791); listed in vscode-acp / Codeg supported agents; Paseo drives it via `codebuddy --acp` | 2026-08-24 | [S6][S18] | independently observable |
| Funding/valuation | n/a — Tencent Holdings (0700.HK) business unit, not a startup | — | — | n/a |
| Community size (Discord/subreddit) | none found for the CLI; support via codebuddy@tencent.com and CN docs contact page | 2026-08-24 | [S4] | researched, none found |
| Benchmarks (SWE-bench, Terminal-Bench) | none found for CodeBuddy Code | 2026-08-24 | — | researched, none found |

## 3. Plugin interface (PRI-2925)

- mcp_support: **client** — stdio/SSE/streamable-HTTP transports; user/project/local scopes; `codebuddy mcp add|add-json|list|remove`; OAuth flow for remote servers; no server mode documented [S5b]. Evidence: https://www.codebuddy.ai/docs/cli/mcp
- plugin_support: **True** — plugins with `.codebuddy-plugin/plugin.json`, `skills/name/SKILL.md`, `commands/` (legacy), `agents/*.md`, `hooks/hooks.json`, `.mcp.json`, `.lsp.json`, `bin/`; marketplaces from local dirs, GitHub repos, git URLs, HTTP; `codebuddy plugin install|enable|update|marketplace add ...`; plugin deps with semver constraints [S7]. Evidence: https://www.codebuddy.ai/docs/cli/plugins-reference
- claude_code_plugin: **yes** — docs state the plugin system "is designed to be compatible with the Claude Code plugin specification"; accepts `.claude-plugin/` (its own `.codebuddy-plugin/` takes priority) and recognizes `${CLAUDE_PLUGIN_ROOT}`/`${CLAUDE_PLUGIN_DATA}`; no migration required [S7]. (Whether CLAUDE.md is read as memory: null — CODEBUDDY.md is the documented file.)
- subagents: **True** — built-in Plan sub-agent; custom agents as Markdown+frontmatter (`model`, `effort`, `maxTurns`, `tools`, `disallowedTools`, `isolation: "worktree"`); subagents inherit MCP tools; Agent Teams multi-agent collaboration (with ACP status streaming) [S5c][S6][S7]. Evidence: https://www.codebuddy.ai/docs/cli/sub-agents and /docs/cli/agent-teams
- hooks: **True** — 27+ events (PreToolUse, PostToolUse, PostToolUseFailure, UserPromptSubmit, Stop, StopFailure, SubagentStart/Stop, SessionStart/End, Setup, PreCompact/PostCompact, PermissionRequest/Denied, Elicitation, TaskCreated/Completed, TeammateIdle, FileChanged, WorktreeCreate/Remove, etc.); command/prompt/agent/http handler types; can block tool calls (exit 2 / `continue: false`); configured in `~/.codebuddy/settings.json`, project `.codebuddy/settings.json(.local)`, or agent/skill frontmatter [S5]. Evidence: https://www.codebuddy.ai/docs/cli/hooks
- plan_mode: **True** — read-only planning mode ("plan first, then execute"; introduced in 2.0, Jan 2026); plan mode preserves prior permission settings ("plan + bypass" combos); SDK exposes plan permission mode [S5d][S12][S17]. Evidence: https://www.codebuddy.ai/docs/cli/common-workflows (plan mode section) and /docs/ide/Features/Plan-Mode
- plugin_docs_url: https://www.codebuddy.ai/docs/cli/plugins (reference: https://www.codebuddy.ai/docs/cli/plugins-reference; marketplaces: https://www.codebuddy.ai/docs/cli/plugin-marketplaces)
- config_docs_url: https://www.codebuddy.ai/docs/cli/settings
- ACP support: **yes, first-party** — `codebuddy --acp` starts an ACP server; documented Zed integration; extends ACP via `_meta` on session_info_update for Agent Teams status; filters slash-command list for ACP clients [S6]. Evidence: https://www.codebuddy.ai/docs/cli/acp
- SDK: **yes** — CodeBuddy Agent SDK (TypeScript documented; demo projects repo); clean-runtime default (no filesystem config loaded unless `settingSources` set); headless mode (`-p`) and HTTP API beta [S5e][S16]. Evidence: https://www.codebuddy.ai/docs/cli/sdk

## 4. Claimed differentiation (raw material for PRI-2927)

- tagline (CN site, verbatim): "AI 时代的智能编程伙伴" ("intelligent programming partner for the AI era") — https://www.codebuddy.cn/cli/ [S1]
- tagline (intl product page): "seamless development experience across plugins, IDEs, and CLIs" — https://www.tencentcloud.com/products/acc [S9]
- npm description: "Use CodeBuddy, Tencent's AI assistant, right from your terminal... understand your codebase, edit files, run terminal commands, and handle entire workflows" [S3]
- maker claims (paraphrased):
  1. Full-form-factor coverage: first in China to offer plugin + IDE + CLI AI programming tools as one family (launch claim, 2025-09-09) [S8][S12].
  2. Terminal-native lifecycle automation: natural-language control of file edits, Git, tests, deploys; Unix-pipeline compatible; headless/CI use [S4].
  3. Deep Tencent Cloud integration and Tencent-scale dogfooding (>95% of Tencent engineers; 40% coding-time reduction) [S9][S9b].
  4. Extensibility parity with the leading US harness: plugins/skills/hooks/subagents/MCP, plus explicit Claude Code plugin-format compatibility [S7].
  5. Open protocols: first-party ACP server mode, open SDK, MCP client [S5b][S6].
  6. Model flexibility by region: Hunyuan/DeepSeek domestically; GPT/Gemini (and at times Claude) internationally [S12][S13].
  7. Enterprise editions incl. private-cloud deployment (¥316/seat/mo) [S12][S14].
  8. Millisecond code completion adapted to private code style (family claim) [S9].
- audience: CLI aimed at "DevOps engineers and senior developers" / professional engineers; IDE aimed at product managers, designers, full-stack devs, beginners (family page) [S9][S12].

## 5. Company & contact targets (PRI-2929) — company-level only

- company: Tencent Holdings Ltd. (0700.HK, public); product owned by Tencent Cloud within the Cloud and Smart Industries Group (CSIG); HQ Shenzhen, China [S9][S12]
- size: Tencent ~100k+ employees (public company; not re-verified — null); funding stage: n/a (public company)
- publicly named leadership relevant to partnerships:
  - Tang Daosheng (Dowson Tong) — Senior Executive Vice President; CEO, Cloud and Smart Industries Group — named in Tencent's 2026-06-05 announcement [S9b]
  - Yao Shunyu — Tencent Chief AI Scientist — same announcement [S9b]
  - Liu Yi (刘毅) — Vice President of Tencent Cloud; head of CodeBuddy & WorkBuddy product line — named in launch-event press (Sina Tech, 2026-06-06) [S19]
- contact: codebuddy@tencent.com (docs support address) [S4]; CN contact page https://cloud.tencent.com/document/product/1749/104249

## 6. Open questions / conflicts

- License conflict: cnb.cool README reportedly MIT, but npm says "SEE LICENSE IN README.md" and the product is a Tencent commercial service; whether the shipped CLI source is genuinely MIT-licensed and complete on cnb.cool is unverified [S2][S3].
- First-release date: npm first publish 2025-08-05 vs official launch 2025-09-09 (Baike; aibase article dated 2025-09-09) — treat 2025-09-09 as public launch, 2025-08-05 as first artifact [S3][S8][S12].
- Internal-adoption figures vary by date and scope: ">50% of R&D" (undated, intl product page), ">95% of engineers" (2026-06-05, family), "12,000 engineers" (Jan 2026, CLI specifically) — different denominators, all maker-claimed [S9][S9b][S12].
- Baike (secondary source) supplies several load-bearing numbers (12,000 engineers, >50 enterprises, 90% self-written code, model lineups, CN pricing history); primary Tencent URLs for these were not all located [S12].
- International model lineup churn: Claude offered, then removed 2025-10-01 in favor of GPT-5/Gemini-2.5-Pro (per Baike, for the IDE); current intl CLI model list not directly readable (codebuddy.ai pricing/homepage render via JS only) [S12][S13][S15].
- Census conflict: existing census entry `codebuddy` = olasunkanmi-SE's archived GitHub project — unrelated. New slug `codebuddy-code` required; do not merge histories.
- Default permission behavior (ask-before-edit?) not stated in docs overview — null.
- WorkBuddy claim "1200万 DAU / 3 months" (Zhihu) is about WorkBuddy, not CodeBuddy — excluded.

## 7. Sources

1. [S1] https://www.codebuddy.cn/cli/ — CN product page, tagline (page is JS-heavy; only title extracted)
2. [S2] https://cnb.cool/codebuddy/codebuddy-code — repo README, MIT notice, stars/forks/issues
3. [S3] https://registry.npmjs.org/@tencent-ai/codebuddy-code — versions, dates, license field, bins; [S3b] https://api.npmjs.org/downloads/point/last-week|last-month/@tencent-ai/codebuddy-code — download counts
4. [S4] https://www.codebuddy.ai/docs/cli/overview — what it is, install, family, support email
5. [S5] https://www.codebuddy.ai/docs/cli/hooks — hook events/types; [S5b] /docs/cli/mcp — MCP client; [S5c] /docs/cli/sub-agents — subagents; [S5d] /docs/cli/common-workflows + /docs/ide/Features/Plan-Mode — plan mode; [S5e] /docs/cli/sdk (+ /docs/cli/sdk-typescript, /docs/cli/sdk-demos, /docs/cli/headless) — SDK/headless
6. [S6] https://www.codebuddy.ai/docs/cli/acp — `codebuddy --acp`, Zed config, Agent Teams over ACP
7. [S7] https://www.codebuddy.ai/docs/cli/plugins-reference (+ /docs/cli/plugins, /docs/cli/plugin-marketplaces) — plugin format, Claude Code compatibility
8. [S8] https://www.aibase.com/news/21148 — 2025-09-09 CLI launch, "first in China" claim
9. [S9] https://www.tencentcloud.com/products/acc — intl family page, >50% R&D claim, audiences; [S9b] http://www.tencent.com/zh-cn/tencent-cloud-debuts-productivity-agent-suite-creating-a-new-gateway-to-ai-for-users-and-enterprises/ — 2026-06-05, >95% engineers, -40% coding time, Tang Daosheng, Yao Shunyu
10. [S10] https://marketplace.visualstudio.com/_apis/public/gallery/extensionquery (Tencent-Cloud.coding-copilot) — VS Code installs/ratings
11. [S11] https://plugins.jetbrains.com/api/plugins/24379 — JetBrains downloads
12. [S12] https://baike.baidu.com/en/item/CodeBuddy/1432154 — family timeline, adoption numbers, models, CN pricing (secondary source)
13. [S13] https://baike.baidu.com/en/item/CodeBuddy%20IDE/1937675 (via search summary) — intl IDE model changes 2025-10-01
14. [S14] https://cloud.tencent.com/announce/detail/2270 and https://cloud.tencent.com/document/product/1749/126593 (via search summaries) — 2026 pricing changes, tiers
15. [S15] https://www.codebuddy.ai/pricing and https://www.codebuddy.ai/cli — fetched empty (client-side rendered); unreachable for extraction
16. [S16] https://www.codebuddy.ai/docs/cli/http-api — HTTP API beta (title via search)
17. [S17] https://www.codebuddy.ai/docs/cli/release-notes/v2.48.0 (via search) + Baike — 2.0 feature set (Skills, Plan Mode, ACP, SDK, sandbox)
18. [S18] https://github.com/BloopAI/vibe-kanban/pull/1791 — third-party CLI integration; https://github.com/formulahendry/vscode-acp and https://docs.codeg.app/guide/supported-agents — ACP client listings
19. [S19] https://finance.sina.com.cn/tech/roll/2026-06-06/doc-iniancxn1917457.shtml — Liu Yi, VP Tencent Cloud, CodeBuddy/WorkBuddy head

## Inclusion check (Jesse's test)

**Yes** — CodeBuddy Code is a first-party CLI agent with its own agentic loop (edits files, runs commands, spawns subagents/agent teams, exposes that loop via its own SDK and a first-party ACP server), not a wrapper around someone else's agent [S4][S5][S6].

## Proposed new-entry frontmatter (census _TEMPLATE.md values)

```yaml
name: "CodeBuddy Code"
slug: "codebuddy-code"          # census `codebuddy` is an unrelated archived project — keep separate
layout: "agent.njk"
category: "agent"
maker: "tencent-cloud"          # new makers.json record: company, CN, makes_models: true (Hunyuan),
                                # revenue_model: [subscriptions]
license: "Proprietary"          # repo README claims MIT; npm says SEE LICENSE — unresolved, see dossier §6
url: "https://www.codebuddy.cn/cli/"
source_code_url: "https://cnb.cool/codebuddy/codebuddy-code"
source_available: null          # partial/unverified — repo exists on cnb.cool, completeness unconfirmed
homepage: "https://www.codebuddy.ai"
docs_url: "https://www.codebuddy.ai/docs/cli/overview"
download_url: "https://www.npmjs.com/package/@tencent-ai/codebuddy-code"
install_method: "npm install -g @tencent-ai/codebuddy-code"
platforms: ["CLI"]
autonomy_level: ["agentic"]
specialization: "general"
language: null
first_released: "2025-09-09"    # official launch; first npm publish 2025-08-05
current_release: "2026-08-24"   # npm 2.138.0
maintained: "active"
mcp_support: True               # client
plugin_support: True
claude_code_plugin: True        # explicit compatibility with Claude Code plugin spec
subagents: True
hooks: True
plan_mode: True
plugin_docs_url: "https://www.codebuddy.ai/docs/cli/plugins"
config_docs_url: "https://www.codebuddy.ai/docs/cli/settings"
model_providers: "Tencent Hunyuan, DeepSeek (CN); OpenAI, Google (intl; Claude at times)"
pricing: "freemium"             # free tier + CNY subscriptions; enterprise seats
github_stars: null              # not on GitHub; cnb.cool repo has 123 stars
sources: ["paseo-acp-list"]
last_verified: "2026-08-24"
what_makes_it_special: "Tencent's terminal coding agent — a Claude Code-compatible harness (plugins, hooks, subagents, CODEBUDDY.md) with first-party ACP server mode, dogfooded across most of Tencent's engineering org, split into China (Hunyuan/DeepSeek) and international (GPT/Gemini) editions."
```

Suggested body narrative (draft): CodeBuddy Code is the CLI member of Tencent Cloud's CodeBuddy family, launched September 2025 as China's first big-tech terminal coding agent alongside the family's IDE plugin and standalone IDE. It deliberately tracks the Claude Code interface — CODEBUDDY.md memory, the same plugin/skills/hooks/subagent layout, and declared compatibility with the Claude Code plugin spec — while adding first-party ACP server mode (`codebuddy --acp`) that editors like Zed and multiplexers like Paseo drive. Its users split along its two editions: Chinese developers on Hunyuan/DeepSeek with CNY pricing, international users on GPT/Gemini, plus Tencent's own engineers, most of whom the company says now use the family internally.
