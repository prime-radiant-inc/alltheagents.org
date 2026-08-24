# Dossier: Qoder / Qoder CLI (census slugs: qoder, qoder-cli)

Compiled 2026-08-24 (task brief dated 2026-08-21). Facts only. Null convention: "null = not researched"; "False/none = researched and absent". Sources [Sn] in section 7. Covers both surfaces — the Qoder platform/IDE and Qoder CLI — with the CLI as anchor (Paseo drives it via `npx @qoder-ai/qodercli --acp`).

## 1. Identity

- name: **Qoder** (platform: IDE + CLI + JetBrains plugin + Cloud Agents + QoderWork + QoderWake); the CLI product is **Qoder CLI** (npm `@qoder-ai/qodercli`, binary `qoder`/`qodercli`) [S1][S2][S8]
- maker: **Qoder**; legal entity **Bright Zenith Private Limited**, Singapore (51 Bras Basah Road, #03-01 Lazada One, Singapore 189554; UEN 202416120Z, incorporated 2024-04-23) [S5][S6][S7] (as-of 2026-08-24)
- **Alibaba relationship (establish precisely):**
  - The launch press release (ACCESS Newswire, 2025-08-21, issued by "Qoder") is headlined "Alibaba Launches Qoder: An Agentic Coding Platform for Real Software" [S4]. Later Qoder-issued releases are also headlined "Alibaba Launches..." and press describes Qoder as "Alibaba's agentic coding platform" [S15].
  - The China-market counterpart **Qoder CN** is Alibaba Cloud's product: Alibaba Cloud's **Tongyi Lingma (通义灵码)** was rebranded to Qoder CN on **2026-05-20** (Alibaba Cloud developer articles) [S16]; the JetBrains plugin "Qoder CN (Formerly Lingma)" is published by verified vendor **Alibaba Cloud** (xmlId `com.alibabacloud.intellij.cosy`) [S12]. There is a separate China CLI npm package `@qodercn-ai/qoderclicn` [S10]. Qoder is sold on the Alibaba Cloud Marketplace ("Qoder for Enterprise") [S7].
  - IDC's 2025 China AI-coding market report (as reported 2026-07-16) attributes Qoder to Alibaba: Alibaba leads with 47.6% share "driven by its core AI programming product Qoder" [S15].
  - Circumstantial: Qoder's registered office is in "Lazada One" (HQ building of Alibaba subsidiary Lazada); qoder.com assets are served from Alibaba's CDN (img.alicdn.com); the international model Qwen3-Coder is Alibaba's [S5][S4].
  - **Not found:** any public filing or statement specifying the equity relationship (e.g., "wholly-owned subsidiary of Alibaba Group"). The precise, defensible formulation: *Qoder is Alibaba's coding-agent brand; the international product is operated through Singapore-incorporated Bright Zenith Private Limited, while the China edition (Qoder CN, ex-Tongyi Lingma) is operated directly by Alibaba Cloud.* The company's own site does not mention Alibaba [S5].
- product URL: https://qoder.com (CLI: https://qoder.com/cli — npm homepage field [S8]); China site: https://qoder.com.cn [S1]
- docs: https://docs.qoder.com/ (CLI docs at /cli/*) [S2]
- repo URL: **none for the product** (researched, absent). Official GitHub org is **QoderAI** (31 public repos: changelogs, action, samples, better-harness) [S11]. `github.com/qoder-cli/qoder-cli` (in existing census) **does not exist** — GitHub API 404 [S11].
- license: **proprietary**; npm package has no license field [S8]. source_available: **False** for IDE and CLI (CLI ships as a JS bundle on npm; no source repo). Ancillary OSS: QoderAI/better-harness (MIT), qoder-action (MIT), qoder-agent-sdk-samples (MIT), qoder-acp-demos (Apache-2.0) [S11].
- first public release: platform/IDE **2025-08-21** as a free public preview (launch PR) [S4]; Chinese sources date it 2025-08-22 China time [S16]. CLI: first npm publish **2025-09-24** (v0.0.9-preview) [S8]; first release-notes entry v0.1.0, 2025-10-24 [S13].
- latest release (CLI): **v1.1.29, 2026-08-24** (npm; 204 versions to date; near-daily cadence) [S8]; release-notes latest documented v1.1.28, 2026-08-21 [S13].
- what it is:
  - Form factors: desktop **IDE** (download qoder.com/download) with Editor + **Quest** (autonomous agent-first workspace: Agent mode, Experts multi-agent mode, Goal-driven, Spec-driven/SDD, scheduled tasks, sandboxed terminal); **CLI** (terminal, headless/CI, ACP server, SDK engine); **JetBrains plugin**; **Cloud Agents** (managed agent API for enterprises); **QoderWork** (desktop/document/browser agent) and **QoderWake** ("AI employees"/Wakers); mobile & web monitoring of IDE/CLI tasks [S1][S2][S3][S9].
  - Models: multi-model with automatic routing — Alibaba's Qwen3-Coder plus "Claude, Gemini, and GPT" frontier models, "automatic model selection based on cost-effectiveness" [S4]; own agentic model **Qwen-Coder-Qoder** "trained inside" the Qoder platform, announced 2026-02-03, maker-claimed 60.51% task-resolution rate [S14]; proprietary Next-Edit-Suggestion (NES) model [S4]; CLI added multi-model support + **BYOK** in v0.2.0 (2026-04-26) [S13]. Not locked to one vendor.
  - Pricing: Free plan (basic models, limited messages, BYOK, one-time 2-week Pro trial with 300 credits); **Pro $20/mo (2,000 credits)**, **Pro+ $60/mo (6,000)**, **Ultra $200/mo (20,000)**; credit packs $20 per 1,500 (expire in 1 month); Teams/Enterprise plans exist [S17] (as-of 2026-08-24).
  - Install (CLI): `npm install -g @qoder-ai/qodercli@latest` (Node >= 20) or `curl -fsSL https://qoder.com/install | bash` / `irm https://qoder.com/install.ps1 | iex`; macOS/Linux/Windows, arm64+amd64 (Windows arm64 unsupported); auto-upgrade on by default [S18]. IDE from qoder.com/download; JetBrains via marketplace [S1][S12].
  - Default autonomy: permission-based — "confirmations before critical operations" (file writes, command execution); `--yolo` bypass flag; auto-permission classifier mode added v0.2.14 (2026-05-14); working modes: Interactive, Plan, Goal, Scheduled Task, /loop, Headless [S2][S13][S19].

## 2. Adoption evidence

| metric / claim | value | as-of | source | type |
|---|---|---|---|---|
| npm weekly downloads, @qoder-ai/qodercli | 11,313 (2026-08-17..23) | 2026-08-24 | [S10] | independently observable |
| npm monthly downloads, @qoder-ai/qodercli | 95,638 (2026-07-25..08-23) | 2026-08-24 | [S10] | independently observable |
| npm weekly, @qodercn-ai/qoderclicn (China CLI) | 2,411 | 2026-08-24 | [S10] | independently observable |
| npm weekly, @qoder-ai/qoder-agent-sdk (TS SDK) | 4,392 | 2026-08-24 | [S10] | independently observable |
| npm weekly, @qoder-ai/better-harness | 516 | 2026-08-24 | [S10] | independently observable |
| npm release cadence | 204 versions since 2025-09-24; v1.1.25-29 on Aug 18/19/20/21/24 2026 (near-daily) | 2026-08-24 | [S8] | independently observable |
| JetBrains Marketplace, "Qoder - Agentic AI Coding Platform" (com.qoder, vendor "Qoder", verified) | 2,893,479 downloads; rating 3.09 | 2026-08-24 | [S12] | independently observable |
| JetBrains Marketplace, "Qoder CN (Formerly Lingma)" (vendor Alibaba Cloud, verified) | 38,626,010 downloads; rating 2.44 (lineage: Lingma-era downloads included) | 2026-08-24 | [S12] | independently observable |
| GitHub: QoderAI org | 31 public repos; top repo better-harness 1,957 stars / 163 forks (created 2026-07-21); qoder-action 51 stars | 2026-08-24 | [S11] | independently observable |
| Homepage counters | "1,000,000+ global users"; "400k+ codebase wikis generated"; Product Hunt Product of the Day | 2026-08-24 | [S1] | maker-claimed |
| Users worldwide | "over 5 million users" | 2026-07-16 | [S15] | maker-claimed (via IDC-report press) |
| Enterprise users in China | "over 500,000", named: FAW, CITIC Securities, AsiaInfo | 2026-07-16 | [S15] | maker-claimed (via IDC-report press) |
| IDC: 2025 China AI-coding market share | Alibaba 47.6% "driven by ... Qoder", > sum of ranks 2-5; market RMB 399M (2025) -> RMB 1.173B proj. 2026 | 2026-07-16 | [S15] | third-party (IDC, via press) |
| Product Hunt launch | Product of the Day, 652 upvotes | 2025-08 | [S3] | independently observable (via press) |
| Benchmark: Qwen-Coder-Qoder | 60.51% "task resolution rate", "approaching frontier models" at lower cost | 2026-02-03 | [S14] | maker-claimed |
| Funding / valuation | none separate found — Alibaba-funded brand; Bright Zenith incorporated 2024-04-23, SG | 2026-08-24 | [S6][S7] | researched, absent |
| Community | Discord/subreddit sizes not researched (null); QoderAI/qoder-community repo 67 stars | 2026-08-24 | [S11] | independently observable |
| Demand-side gray signal | trial-reset/account-farming tools on GitHub (qoder-free 398 stars, qoder-creator 173, qoder-reset 91, qoder2api 78) | 2026-08-24 | [S11] | independently observable (indicates paywall pressure/demand, esp. CN) |
| Technical scale claims | up to 100k files analyzed; up to 26h agent execution | 2026-08-24 | [S1] | maker-claimed |

## 3. Plugin interface (PRI-2925) — six census fields

- **mcp_support: client** — CLI consumes MCP servers over stdio / sse / http / ws; scopes user (`~/.qoder/settings.json`), local (`.qoder/settings.local.json`), project (`.mcp.json`); `qoder mcp add`; MCP OAuth since v0.1.4 (2025-10-29); tools gated by permissions. No documented MCP-server mode. IDE also an MCP client [S20][S13][S2]. Evidence: https://docs.qoder.com/cli/mcp-servers.md
- **plugin_support: True** — CLI plugins: `.qoder-plugin/plugin.json` manifest (only `name` required) + conventional dirs `commands/`, `agents/`, `skills/`, `hooks/`, `output-styles/`, `workflows/`, `bin/`, `.mcp.json`; marketplaces via `marketplace.json` (`name`, `owner`, `plugins`); `qoder plugins install|enable|disable|update|validate`, `/plugins`; plugin marketplace shipped v1.0.35 (2026-07-01); official repo QoderAI/qoder-plugins-official. IDE has a separate curated in-IDE marketplace (7 categories) [S21][S22][S13][S11]. Evidence: https://docs.qoder.com/cli/plugins-reference.md
- **claude_code_plugin: no (documented) / de-facto near-clone** — no mention of Claude Code, `.claude/` dirs, or third-party format compat anywhere in plugin/skills/subagent docs [S21][S23][S24]; however the format mirrors Claude Code's field-for-field (`.qoder-plugin/plugin.json` vs `.claude-plugin/plugin.json`; same `commands/agents/skills/hooks/mcp.json` layout; `marketplace.json` with same required fields; `SKILL.md` with name/description frontmatter identical to Anthropic's Agent Skills spec) — porting is mechanical renaming, but unmodified Claude Code plugins are not read. Recommend census value: **no** (with "format-parallel" note).
- **subagents: True** — Markdown + YAML frontmatter in `.qoder/agents/` (project) and `~/.qoder/agents/` (user); built-ins `general-purpose`, `Explore`, `Plan` (+ conditional `qoder-guide`, `statusline-setup`); explicit (`@name`, "use the X subagent"), implicit (description matching), or `qoder --agent name`; concurrent dispatch and background execution; **Agent Teams** multi-agent collaboration since v1.1.15 (2026-08-05); IDE Quest "Experts Mode" runs multiple agents in parallel [S23][S13][S9]. Evidence: https://docs.qoder.com/cli/subagent.md
- **hooks: True** — ~23 events (SessionStart/End, UserPromptSubmit, PreToolUse, PostToolUse, PostToolUseFailure, PermissionRequest/Denied, Stop, StopFailure, SubagentStart/Stop, PreCompact/PostCompact, Notification, InstructionsLoaded, ConfigChange, CwdChanged, FileChanged, WorktreeCreate/Remove, Elicitation, ElicitationResult); handler types **command / http / prompt / agent**; blocking via exit 2, input rewrite (`updatedInput`), output rewrite (`updatedToolOutput`), matchers with regex and `if` glob filters, async hooks; configured in the three settings.json layers. Hook system since v0.1.8 (2025-11-08) [S25][S13]. Evidence: https://docs.qoder.com/cli/hooks.md
- **plan_mode: True** — `/plan` command and Plan working mode (read-only planning before edits) since v0.2.0 (2026-04-26); Plan built-in subagent; IDE Quest generates execution plans for review before autonomous execution [S26][S13][S19][S4]. Evidence: https://docs.qoder.com/cli/plan-mode.md
- plugin_docs_url: https://docs.qoder.com/cli/plugins-reference.md (IDE: https://docs.qoder.com/extensions/plugins.md)
- config_docs_url: https://docs.qoder.com/cli/cli-reference.md (settings layers documented in hooks/MCP pages; `~/.qoder/settings.json`)
- **ACP: yes** — `qoder --acp` starts an Agent Client Protocol server (stdio), since v0.1.17 (2025-12-17); docs reference agentclientprotocol.com; Zed is the documented client; exposes built-in tools, subagents, MCP, permissions, images; default vs bypass-permissions (`--yolo`-equivalent) modes; auth via CLI login or `QODER_PERSONAL_ACCESS_TOKEN`. Matches Paseo's `npx @qoder-ai/qodercli --acp` invocation. Note: docs index mislabels ACP as "Agent Collaboration Protocol" [S27][S13][S2]. Evidence: https://docs.qoder.com/cli/acp.md
- **SDK: yes** — Qoder Agent SDK, TypeScript (`@qoder-ai/qoder-agent-sdk`, 1.0.25) and Python (`qoder-agent-sdk` on PyPI, 1.0.13); docs at /cli/sdk/*; samples repo QoderAI/qoder-agent-sdk-samples; homepage pitches the CLI as "an agent engine you can build on" [S10][S28][S11][S1].

## 4. Claimed differentiation (raw material for PRI-2927)

- tagline (homepage, verbatim): "Think deeper, build better" / "Agentic Platform for Real Work" — https://qoder.com [S1]
- CLI tagline (homepage, verbatim): "A terminal-native AI coding partner—and an agent engine you can build on" [S1]; docs: "An AI Coding Assistant for terminal developers" [S2]
- IDE tagline: "The autonomous development IDE for real-world software" [S1]
- maker claims (paraphrased):
  1. Quest mode: delegate whole features — "Define the goal. Review the result."; autonomous end-to-end execution delivering tested, production-ready code (vs conversational Agent mode) [S9][S4].
  2. Multi-agent "Experts Mode": parallel expert agents for full-stack work, research, debugging [S9][S1].
  3. Spec-driven development (SDD): specification-first workflow as the innovation over prompt-driven coding [S2][S4].
  4. Context engineering at repo scale: "Wikilize" your codebase (Repo Wiki architecture discovery), up to 100k files analyzed [S1].
  5. Long-horizon autonomy: up to 26h agent execution; scheduled tasks; 7×24 "AI employees" (QoderWake) [S1].
  6. Memory & rules: "learns from you and works in your way"; auto-memory with promotion suggestions [S1][S29].
  7. Model-agnostic routing: Qwen3-Coder + Claude/Gemini/GPT with automatic cost-effectiveness-based selection; own in-platform-trained model (Qwen-Coder-Qoder) [S4][S14].
  8. Full product suite one subscription: IDE, CLI, JetBrains, Cloud Agents, QoderWork, QoderWake, mobile/web monitoring [S3][S1].
- audience: individual developers through enterprises ("Empower Every Individual. Elevate Every Organization"); terminal developers (CLI); enterprises via Cloud Agents/Enterprise plan and Alibaba Cloud Marketplace [S1][S2][S7].

## 5. Company & contact targets (PRI-2929) — company-level only

- legal name: Bright Zenith Private Limited (Singapore, UEN 202416120Z, inc. 2024-04-23) [S5][S6]; brand: Qoder; parent-brand: Alibaba (see section 1 for exact relationship; China edition operated by Alibaba Cloud) [S4][S12][S16]
- HQ: 51 Bras Basah Road, #03-01 Lazada One, Singapore 189554 [S5]
- size: not published; "a team based right here in Singapore" (about-us); no headcount found [S5] — researched, absent
- funding stage: no independent funding; Alibaba-backed brand [S4][S15]
- publicly named leadership: **Yu Ding — Head of Qoder** (quoted in the 2025-08-21 launch press release) [S4]. No other individuals named on qoder.com/about-us (checked) [S5]. Alibaba Cloud executives not attributed to Qoder in sources reviewed — null (not researched further).
- contact: contact@qoder.com (published on about-us page — company-level) [S5]

## 6. Open questions / conflicts

- **Census qoder-cli.md errors:** `url`/`source_code_url` = github.com/qoder-cli/qoder-cli — repo does not exist (GitHub API 404) [S11]; `license: MIT` — wrong, npm package has no license and the product is proprietary [S8]; `source_available: True` — wrong, False; "based on Qwen programming large model" — misleading: multi-model routing incl. Claude/Gemini/GPT + BYOK (Qwen3-Coder is one of the models) [S4][S13]. Entry may have been contaminated by an unrelated/squatted project.
- **Census qoder.md errors:** `platforms: ["Web"]` — wrong: desktop IDE, CLI, JetBrains plugin, cloud, mobile/web monitoring [S1][S3]; `mcp_support: null` → client; `hooks: null` → True; `claude_code_plugin: null` → no (format-parallel); `plugin_docs_url`/`config_docs_url` null → filled above; `first_released: 2025` → 2025-08-21 precise [S4].
- Equity relationship Alibaba ↔ Bright Zenith not documented in any public filing found; qoder.com never mentions Alibaba while Alibaba/press/IDC treat Qoder as Alibaba's product. See section 1 formulation.
- User counts conflict: homepage "1,000,000+" [S1] vs "over 5 million worldwide" (2026-07 press around IDC report) [S15]. Homepage counter likely stale; both maker-claimed; no independent verification.
- JetBrains "Qoder CN" 38.6M downloads includes the Tongyi Lingma era (plugin renamed); do not attribute wholly to Qoder-branded period [S12].
- Qwen-Coder-Qoder's "60.51% task resolution rate" — benchmark not named in the press item retrieved (likely SWE-bench Verified; unconfirmed) [S14].
- npm package keywords include "gemini" and it ships a JS bundle (`bundle/qodercli.js`) [S8] — possible Gemini-CLI-derived lineage; **unverified observation**, no source states this.
- Docs index calls ACP "Agent Collaboration Protocol"; the doc body links agentclientprotocol.com (Agent Client Protocol) [S2][S27]. Naming sloppiness, not a different protocol.
- Whether the IDE is a VS Code fork is not stated in docs (widely assumed in reviews); left unresearched-precise — null.
- Unreachable: accessnewswire.com returned HTTP 403 (content recovered via Yahoo Finance syndication) [S14]; pypistats.org rate-limited (429) so Python SDK download counts are null [S10].

## 7. Sources

1. [S1] https://qoder.com — homepage: taglines, product suite, 1M+ users, 400k wikis, 100k files/26h, entity name, qoder.com.cn
2. [S2] https://docs.qoder.com/llms.txt + https://docs.qoder.com/cli/overview.md — docs index, CLI description, working modes, permissions
3. [S3] https://docs.qoder.com/product-series/what-is-qoder.md — product family definitions
4. [S4] https://finance.yahoo.com/news/alibaba-launches-qoder-agentic-coding-133000732.html — launch PR 2025-08-21 (ACCESS Newswire): "Alibaba Launches Qoder", Yu Ding quote, models, NES, free preview
5. [S5] https://qoder.com/about-us — Bright Zenith Private Limited, Singapore address, contact@qoder.com, no Alibaba mention
6. [S6] https://www.sgpbusiness.com/company/Bright-Zenith-Private-Limited (via search) — UEN 202416120Z, incorporated 2024-04-23
7. [S7] https://www.alibabacloud.com/en/marketplace/qoder — Qoder for Enterprise on Alibaba Cloud Marketplace (via search)
8. [S8] https://registry.npmjs.org/@qoder-ai/qodercli — versions (204), dates, no license, bin, homepage qoder.com/cli, node>=20, keywords
9. [S9] https://docs.qoder.com/user-guide/quest/overview.md — Quest, Agent/Experts modes, autonomy
10. [S10] https://api.npmjs.org/downloads/point/... (qodercli, qoderclicn, qoder-agent-sdk, better-harness) + npm search + https://pypi.org/pypi/qoder-agent-sdk/json + pypistats (429) — download counts, package roster
11. [S11] https://api.github.com/orgs/QoderAI/repos + /search/repositories?q=qoder + /repos/qoder-cli/qoder-cli (404) — org repos, stars, ecosystem/reset tools, nonexistent census repo
12. [S12] https://plugins.jetbrains.com/api/searchPlugins?search=qoder — Qoder plugin 2,893,479 dl (vendor Qoder); Qoder CN ex-Lingma 38,626,010 dl (vendor Alibaba Cloud)
13. [S13] https://docs.qoder.com/release-notes/qoder-cli.md — version history: 0.1.0 (2025-10-24) ... 1.1.28 (2026-08-21); ACP v0.1.17, hooks v0.1.8, skills v0.1.20, plan/multi-model v0.2.0, auto-permissions v0.2.14, 1.0.0 cloud (2026-05-19), marketplace v1.0.35, Agent Teams v1.1.15
14. [S14] https://finance.yahoo.com/news/alibaba-launches-large-model-trained-120000343.html — Qwen-Coder-Qoder, 2026-02-03, 60.51%; accessnewswire original 403
15. [S15] https://www.kucoin.com/news/flash/idc-report-alibaba-leads-2025-china-ai-coding-market-with-47-6-share — IDC 47.6%, RMB 399M/1.173B, 5M users, 500k CN enterprise users, FAW/CITIC/AsiaInfo (2026-07-16)
16. [S16] https://developer.aliyun.com/article/1743163 (+1742464, via search) — Tongyi Lingma renamed Qoder CN 2026-05-20; Alibaba released global Qoder 2025-08-22
17. [S17] https://docs.qoder.com/account/pricing.md — Free/Pro $20/Pro+ $60/Ultra $200, credits, trial, packs
18. [S18] https://docs.qoder.com/cli/installation.md — install methods, platforms, node>=20, auto-upgrade
19. [S19] https://docs.qoder.com/cli/slash-reference.md — /plan /agents /skills /plugins /mcp /init /memory
20. [S20] https://docs.qoder.com/cli/mcp-servers.md — transports, scopes, no server mode
21. [S21] https://docs.qoder.com/cli/plugins-reference.md — .qoder-plugin/plugin.json, dirs, marketplace.json, commands
22. [S22] https://docs.qoder.com/extensions/plugins.md — IDE curated marketplace, no Claude mention
23. [S23] https://docs.qoder.com/cli/subagent.md — subagent format, built-ins, parallelism
24. [S24] https://docs.qoder.com/cli/Skills.md — SKILL.md format, ~/.qoder/skills, triggers
25. [S25] https://docs.qoder.com/cli/hooks.md — events, handler types, blocking/rewrite
26. [S26] https://docs.qoder.com/cli/plan-mode.md — plan mode page (listed; not fetched in detail)
27. [S27] https://docs.qoder.com/cli/acp.md — --acp, Zed, capabilities, modes, PAT auth
28. [S28] https://docs.qoder.com/cli/sdk/overview.md — SDK docs (listed in index)
29. [S29] https://docs.qoder.com/cli/slash-reference.md (/memory auto-memory notes) — memory management

## Inclusion check (Jesse's test)

**Yes** — Qoder CLI is a first-party agent with its own agentic loop (autonomously reads files, invokes tools, executes commands, iterates; exposed as an SDK and over ACP), running Qoder's own multi-model backend — not a wrapper around someone else's agent [S2][S27][S28]. The IDE's Quest mode is the same claim at IDE scale [S9].

## Entry-structure recommendation

Keep **two entries**, re-scoped:
1. **`qoder`** — the platform/company entry (maker page): Qoder by Bright Zenith Private Limited / Alibaba; surfaces = IDE (desktop), JetBrains plugin, Cloud Agents, QoderWork, QoderWake. Fix `platforms` (not "Web"), fill mcp/hooks/plugin fields from section 3, add Alibaba-relationship note.
2. **`qoder-cli`** — the harness entry Paseo actually drives (this is the directory-relevant agent): proprietary, npm `@qoder-ai/qodercli`, url https://qoder.com/cli, docs https://docs.qoder.com/cli/overview.md, ACP `--acp`, multi-model (Qwen3-Coder/Claude/Gemini/GPT + BYOK). **Delete** the bogus github.com/qoder-cli/qoder-cli URL, MIT license, source_available True, and the "based on Qwen model" one-liner.
Cross-link the two (qoder-cli.maker → qoder). Optionally a third slug later for Qoder CN if the census tracks China-market variants separately (distinct npm package, billing, and operator).
