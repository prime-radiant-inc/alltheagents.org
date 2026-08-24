# Dossier: MiniMax Code (census_slug: minimax-code — NEW ENTRY, not in census)

Compiled 2026-08-21 (some API reads reflect 2026-08-22 UTC). Facts only. Null convention: "null = not researched"; "False/none = researched and absent". Sources [Sn] in section 7.

## 1. Identity

- name: MiniMax Code (CLI binary/brand: `mcode`, "MCode")
- maker: MiniMax Group Inc. (company; HQ Shanghai, China; PRC operating entity Shanghai Xiyu Jizhi Technology Co., Ltd.; publicly listed on HKEX main board, stock code 0100.HK, since 2026-01-09) [S14][S15][S16] (as-of 2026-08-21)
- product URL: https://agent.minimax.io (code.minimax.io 302-redirects there [S9]); docs home https://agent.minimax.io/docs/code/welcome [S8]; download https://agent.minimax.io/download [S5]
- repo URL: https://github.com/MiniMax-AI/minimax-code — **issue-tracker only** for the desktop app ("This repository collects issue reports for the MiniMax Code desktop app"); no product source code [S5] (as-of 2026-08-21). npm package: https://www.npmjs.com/package/@minimax-ai/code [S1].
- license: npm CLI package declares **MIT** [S1][S2]; desktop app proprietary ("(c) 2026 MiniMax. All rights reserved." in repo README) [S5]. Third-party notice: portions of the TUI "derived from Pi TUI", MIT, (c) 2025 Mario Zechner [S2].
- open source? **False** for practical purposes; source_available: **False** — the npm tarball ships a bundled `cli.js` (MIT-labeled) but no source repository is published; the GitHub repo has no code [S1][S2][S5].
- first public release:
  - Desktop: earliest entry in the official MiniMax Code changelog is v3.0.20, 2026-05-01; the 3.x line and branding grew out of the MiniMax Agent desktop app (a "Web" changelog tab goes back to 2026-02-11); the issues repo for "MiniMax Code" was created 2026-06-01, the same day MiniMax launched the M3 model [S10][S4][S18] (as-of 2026-08-21).
  - CLI: `@minimax-ai/code` 0.1.0 published to npm 2026-08-14 (0.1.2 — the version Paseo pins — published 2026-08-15) [S1].
- latest release: CLI 0.2.3, published 2026-08-22T11:25Z UTC (11 versions in 8 days) [S1]; desktop v3.0.66, 2026-08-19 [S10].
- what it is:
  - Form factors: (1) desktop AI-agent app for macOS (Apple silicon + Intel) and Windows — chat, project workspace, files/changes/terminal panels, built-in browser, scheduled tasks, phone Remote Control, Telegram/WeChat/Lark/Feishu messaging integrations [S8][S10]; (2) terminal CLI/TUI `mcode` with headless `mcode exec` (JSON / stream-JSON output) and an ACP stdio server (`mcode acp`) [S2][S11]. The browser product at agent.minimax.io keeps the "MiniMax Agent" name.
  - Models: MiniMax-hosted M-series by default (Token Plan covers "the full MiniMax lineup (M3 / M2.7 / image / speech)"); BYOK: MiniMax API key or custom providers with base URL + API key (OpenAI/Anthropic-compatible), managed via `mcode provider` or desktop settings [S12][S2][S8-BYOK].
  - Pricing: limited free usage; Token Plan subscriptions Plus **$20/mo**, Max **$50/mo**, Ultra **$120/mo** (5-hour rolling + weekly quota windows; "Agent usage 3-4 / 4-5 / 6-7 agents"); prepaid Credits 1,000 = $1, valid 365 days; CLI itself free to install [S12] (as-of 2026-08-21).
  - Install: `npm install -g @minimax-ai/code` (Node 22.19+/24–26; Node 23 unsupported), or `curl -fsSL https://filecdn.minimax.chat/public/install.sh | bash` (macOS/Linux/WSL; installs a self-contained Node runtime if needed, no sudo; musl/Alpine unsupported), `irm https://filecdn.minimax.chat/public/install.ps1 | iex` (Windows); desktop via .dmg/.exe from agent.minimax.io/download [S11][S2][S10].
  - Default autonomy: permission modes **Ask / Auto / Full access** (`Alt+M`, `/permission`), independent of Plan Mode; approval cards for commands/files with allow-once vs allow-for-session; desktop "asks for confirmation before sensitive actions" (reads outside workspace, edits/deletes, commands, external side effects) [S2][S11][S13].
  - Implementation: distributed as bundled JavaScript on Node; TUI derived from Pi TUI (Mario Zechner, MIT) [S1][S2].

## 2. Adoption evidence

| metric / claim | value | as-of | source | type |
|---|---|---|---|---|
| npm weekly downloads, @minimax-ai/code | 3,082 (2026-08-17..23) | 2026-08-23 | [S3] | independently observable |
| npm downloads since launch (2026-08-15..21, all-time — package created 2026-08-14) | 2,819 | 2026-08-21 | [S3] | independently observable |
| npm versions published | 11 in 8 days (0.1.0 2026-08-14 → 0.2.3 2026-08-22) | 2026-08-22 | [S1] | independently observable |
| GitHub MiniMax-AI/minimax-code (desktop issue tracker) | 70 stars, 6 forks, 67 open issues; created 2026-06-01 | 2026-08-21 | [S4] | independently observable |
| GitHub MiniMax-AI/MiniMax-Code-Plugins (community plugin registry) | 6 stars; created 2026-08-17 | 2026-08-21 | [S4] | independently observable |
| GitHub MiniMax-AI/skills (skills ecosystem repo) | 13,434 stars; created 2026-03-17 | 2026-08-21 | [S4] | independently observable (adjacent ecosystem, not the harness) |
| Model repos: MiniMax-M2 / M2.1 / M2.5 / M3 / MSA | 2,605 / 544 / 587 / 467 / 417 stars | 2026-08-21 | [S4] | independently observable (models, not harness) |
| Desktop app installs / users | null — no public counter found (direct .dmg/.exe distribution, no store listing located) | 2026-08-21 | — | null |
| Discord community | exists (QR code in docs); member count not obtainable without joining | 2026-08-21 | [S8] | null (not obtainable) |
| Company MAU (all MiniMax products) | 27.6M MAU (Sep 2025), up from 3.1M (2023); >200M cumulative users, 200+ countries | 2026-01 | [S15][S16] | maker-claimed (IPO prospectus, via press) |
| Company paying users | 1.77M paying users, 9M2025; ARPPU $6 (2023) → $15 | 2026-01 | [S16] | maker-claimed (prospectus, via press) |
| Company revenue | ~$53M 9M2025 (up ~130% vs FY2024 ~$30M); >70% overseas; AI-native products 71.1% of revenue | 2026-01 | [S16] | maker-claimed (prospectus, via press) |
| IPO | listed HKEX 2026-01-09, stock code 0100.HK; priced HK$165 (top of range); raised ~HK$4.8B (~$618M) per Forbes / ~$538-540M per earlier reports (offer size upsized 25.39M → 29.2M shares — see §6); shares roughly doubled on debut; market value >$11.5B | 2026-01-09 | [S14][S15][S17] | press / independently observable |
| M3 model benchmark (powers MiniMax Code by default) | SWE-Bench Pro 59.0%, 1M-token context, open-weight, native multimodality (launched 2026-06-01) | 2026-06-01 | [S18][S19] | maker-claimed |
| M2.5 launch (2026-02-12) | "free for a limited time"; shipped into Cline, Ollama, etc. | 2026-02-12 | [S20] | maker-claimed / third-party integrations |
| Public customers / case studies for MiniMax Code | none found (plugin partners named: Hundsun, Qichacha, EverMe, PKUlaw, WPS, WeCom) | 2026-08-21 | [S13-PL] | researched, absent (partners ≠ customers) |
| Benchmark placements for the harness itself (Terminal-Bench etc.) | none found | 2026-08-21 | — | researched, absent |
| Press on the harness | DataCamp tutorial (MiniMax Code web/desktop, M3); coverage otherwise centers on models and IPO | 2026-08-21 | [S21] | third-party |

## 3. Plugin interface (PRI-2925)

- mcp_support: **client** — desktop has a dedicated MCP Servers configuration page (added v3.0.66, 2026-08-19); plugins can bundle MCP servers over `stdio`, `streamable-http`, and legacy `sse` (max 8 per plugin); CLI feature table lists "Skills, MCP, plugins". No MCP-server mode found. Evidence: https://agent.minimax.io/docs/code/agents/mcp [S8][S10][S6].
- plugin_support: **True** — "Agent Plugins 1.0" format: `plugin.json` (schema `https://agent-plugins.org/schemas/1.0.0/plugin.schema.json`) + `skills/<name>/SKILL.md` + optional `mcp.json`; package root `.minimax-plugin/plugin.json`; built-in Plugin Marketplace in the desktop app (added v3.0.63, 2026-08-12) with regional catalogs (CN/US) and surface targeting (MiniMax Code desktop / MiniMax Agent cloud); CLI: `mcode plugin list/add/enable/disable`; submissions via ZIP or public GitHub repo (Feishu form); community registry repo MiniMax-AI/MiniMax-Code-Plugins (Apache-2.0, "one folder, one pull request") [S6][S7][S13-PL][S2].
- claude_code_plugin: **partial** — the format visibly mirrors Claude Code's (plugin.json manifest, skills directories with SKILL.md + name/description frontmatter, bundled MCP), and the harness reads/generates `AGENTS.md` (not CLAUDE.md) via `mcode init`; but the manifest schema/location differ (`agent-plugins.org` schema, `.minimax-plugin/` dir vs `.claude-plugin/`), and the portable subset explicitly excludes hooks, custom agents/commands, LSP, apps/UI extensions, OAuth. A Claude Code plugin's skills would port with light re-packaging; the plugin as a whole would not load as-is [S6][S2][S11].
- subagents: **True** — "Agent Team": describe a goal once, MiniMax Code "coordinates decomposition, execution, progress tracking, and final synthesis"; desktop also supports Custom Agents (own role, instructions, skills, workspace, channels); tagline leads with "builds Agent teams"; Token Plan tiers are sized in "agents" (3-4 / 4-5 / 6-7); engineering blog on Agent Team design. Evidence: https://agent.minimax.io/docs/code/agents/team [S8][S5][S12][S22].
- hooks: **False** (researched, absent) — no hooks documentation anywhere in the docs index; the plugin contract explicitly lists "Hooks and lifecycle scripts" as "not currently public MCode Plugin capabilities" [S6][S8-IDX].
- plan_mode: **True** — CLI: Plan Mode reviews a plan before implementation, toggled with `Shift+Tab` or `/plan`, independent of permission modes; desktop added "a Plan mode that reviews before editing" in v3.0.66 (2026-08-19). Evidence: https://agent.minimax.io/docs/cli/features [S11][S10].
- plugin_docs_url: https://agent.minimax.io/docs/code/agents/plugins (contract: https://github.com/MiniMax-AI/MiniMax-Code-Plugins/blob/main/docs/plugin-compatibility.md)
- config_docs_url: https://agent.minimax.io/docs/cli/features (BYOK: https://agent.minimax.io/docs/code/account/byok)
- ACP support: **yes, first-party** — `mcode acp` starts an Agent Client Protocol server over stdio for ACP-capable editors/clients; supports listing, loading, resuming, and closing persisted sessions across client restarts [S2][S11]. (Paseo invokes `npx @minimax-ai/code --acp`; the official docs document the `mcode acp` subcommand — see §6.)
- SDK: **none found** (researched, absent) — automation path is headless `mcode exec` with JSON/stream-JSON + JSON Schema output, a JSONL side-channel/automation status protocol (0.2.3), and ACP; no language SDK published [S2][S11].

## 4. Claimed differentiation (raw material for PRI-2927)

- tagline (repo README, verbatim): "Remembers your habits, builds Agent teams, automates the repetitive work." — https://github.com/MiniMax-AI/minimax-code [S5]
- docs one-liner: "a desktop AI Agent app for software development, everyday workflows, automation, and remote collaboration" — https://agent.minimax.io/docs/code/welcome [S8]
- maker claims (paraphrased):
  1. One local workspace unifying chat, project context, file ops, terminal, browser previews, skills, memory, and automation [S8].
  2. Agent Team for complex work: decomposition, delegation, verification, synthesis; plus user-defined Custom Agents [S8][S22].
  3. Beyond-coding scope: separate Coding and Work modes (research, documents, everyday workflows), Office/multimodal tasks [S8].
  4. Long-horizon autonomy: "Goal" runs until a verifiable outcome is achieved or blocked; scheduled/recurring tasks [S8][S10].
  5. Remote collaboration: control the desktop agent from a phone (Remote Control) or via Telegram/WeChat/Lark/Feishu, including approving permissions remotely [S8].
  6. Memory: retains preferences, project conventions, long-term working patterns [S8][S5].
  7. Plugin Marketplace with domain plugins (financial data, company lookup, legal search, knowledge, Office) [S13-PL].
  8. CLI positioning: complements the desktop app — "stays close to code repositories, terminals, scripts, CI, and editors"; TUI + headless + ACP [S11].
- audience: developers (CLI/Coding mode) and general knowledge workers (Work mode: "research, documents, and everyday workflows") [S8][S11]; plugin partners skew to Chinese-market professional data (Hundsun, Qichacha, PKUlaw, WPS, WeCom) [S13-PL].

## 5. Company & contact targets (PRI-2929) — company-level only

- legal name: MiniMax Group Inc. (Cayman-incorporated listco; PRC entity Shanghai Xiyu Jizhi Technology Co., Ltd.) [S14][S16]
- HQ: Shanghai, China [S15][S16]
- size: 200+ employees (2025, press/Wikipedia-sourced; likely understated post-IPO) [S16]
- funding stage: public company — HKEX main board, 0100.HK, listed 2026-01-09; raised ~US$540-618M (see §6); sponsors CICC and UBS; backers pre-IPO included MiHoYo, Tencent, Alibaba (press) [S14][S15][S17]
- publicly named leadership (per company IR page, ir.minimax.io):
  - Dr. Yan Junjie — Founder, Chairman, CEO and CTO [S23]
  - Ms. Yun Yeyi — Executive Director and COO [S23]
  - Mr. Zhao Pengyu — Executive Director and Large Language Model Research Leader [S23]
  - Mr. Zhou Yucong — Executive Director and Visual Model Research Leader [S23]
  - Head of product for MiniMax Code / DevRel / partnerships lead: none found publicly named (researched, absent). Plugin submissions route through a Feishu form, not a named contact [S13-PL].

## 6. Open questions / conflicts

- **Paseo invocation vs docs**: Paseo runs `npx @minimax-ai/code --acp` (pinning 0.1.2); official docs document the subcommand form `mcode acp` [S2][S11]. Both presumably reach the same ACP stdio server; the `--acp` flag form is not in the public README — unverified.
- **Naming boundary**: "MiniMax Code" (desktop + CLI) vs "MiniMax Agent" (browser product at agent.minimax.io) share a domain, docs site ("MiniMax Agent Docs"), and plugin catalog; press sometimes uses the names interchangeably. The census entry should cover MiniMax Code (desktop + CLI); the web agent is a sibling surface [S8-IDX][S21].
- **First-release date is genuinely fuzzy**: desktop changelog starts at v3.0.20 (2026-05-01) with no 1.x/2.x history shown; the version line appears inherited from the MiniMax Agent desktop app, with the "MiniMax Code" branding traceable to ~2026-06-01 (issues repo creation, M3 launch). CLI is unambiguous: 2026-08-14 [S10][S4][S1].
- **IPO proceeds conflict**: pre-listing reports said 25.39M shares, ~US$538-540M [S14]; Forbes post-listing says 29.2M shares, HK$4.8B (~US$618M) — consistent with an upsized offer, but not confirmed from the prospectus directly [S17]. Stock code appears as "0100"/"00100.HK" in filings/press; one aggregator (Minichart) wrote "2610" — treat 0100.HK as correct (HKEX filing header) [S14].
- **npm downloads timing**: totals straddle the 2026-08-21 compile date; the "last-week" figure (3,082) covers 2026-08-17..23. All figures tiny/launch-week — expect rapid change [S3].
- **License is split**: MIT on the npm CLI package vs all-rights-reserved desktop; a single census `license` field will oversimplify (suggest "Proprietary (desktop); MIT (CLI package, bundled)") [S1][S5].
- **CLI 0.2.3 changelog mentions "Ludus"** (an eval tmux environment) and a machine-readable status protocol aimed at automation/evals — suggests MiniMax runs the CLI in internal agent evals; nothing public found [S2].
- Desktop install counts, Discord size, and any harness-level usage claims: not obtainable; MiniMax has published no MiniMax Code adoption numbers found in this research.
- MiniMax-AI/minimax-code repo shows 67 open issues in ~11 weeks — a weak but real signal of desktop-app usage [S4].

## 7. Sources

1. [S1] https://registry.npmjs.org/@minimax-ai/code — versions, dates, MIT license, bin `mcode`, engines
2. [S2] npm tarball 0.2.3 (README.md zh, CHANGELOG.md, THIRD_PARTY_NOTICES.md, package.json) — CLI features, ACP, providers, plugins, Pi TUI derivation
3. [S3] https://api.npmjs.org/downloads/... (@minimax-ai/code, point/last-week + range) — download counts
4. [S4] https://api.github.com/orgs/MiniMax-AI/repos + /repos/MiniMax-AI/minimax-code — repo stats and creation dates
5. [S5] https://raw.githubusercontent.com/MiniMax-AI/minimax-code/main/README.md — tagline, issues-only repo, download links, copyright
6. [S6] https://raw.githubusercontent.com/MiniMax-AI/MiniMax-Code-Plugins/main/docs/plugin-compatibility.md — Agent Plugins 1.0 contract, limits, unsupported capabilities
7. [S7] https://raw.githubusercontent.com/MiniMax-AI/MiniMax-Code-Plugins/main/README.md — community registry workflow
8. [S8] https://agent.minimax.io/docs/code/welcome.md — desktop overview, Discord; [S8-IDX] https://code.minimax.io/docs/llms.txt — full docs index; [S8-BYOK] https://agent.minimax.io/docs/code/account/byok.md (via index) — BYOK
9. [S9] https://code.minimax.io — 302 → agent.minimax.io
10. [S10] https://agent.minimax.io/docs/changelog.md — desktop v3.0.20 (2026-05-01) … v3.0.66 (2026-08-19), CLI tab, feature dates
11. [S11] https://agent.minimax.io/docs/cli/quick-start.md + /docs/cli/features.md — install scripts, TUI/headless/ACP, plan mode, permission modes
12. [S12] https://platform.minimax.io/docs/guides/pricing-token-plan.md — Plus/Max/Ultra pricing, credits, model coverage
13. [S13] https://agent.minimax.io/docs/code/workflows/permissions.md — approval behavior; [S13-PL] https://agent.minimax.io/docs/code/agents/plugins.md — marketplace, initial plugins, submission
14. [S14] https://www1.hkexnews.hk/listedco/listconews/sehk/2025/1231/2025123100025.pdf (Global Offering, via search) + aibase/minichart pre-listing reports — stock code 0100, offer terms
15. [S15] https://technode.com/2026/01/09/... + https://www.cnbc.com/2026/01/09/minimax-hong-kong-ipo-ai-tigers-zhipu.html (via search) — debut, market value, MAU
16. [S16] ChinaTalk / Futu / eWeek prospectus analyses (via search) — revenue, paying users, MAU history, Shanghai entity
17. [S17] https://www.forbes.com/sites/ywang/2026/01/09/founder-of-chinese-ai-model-developer-minimax-becomes-a-billionaire-as-shares-surge-on-listing/ (via search) — HK$4.8B raise, Yan Junjie
18. [S18] https://www.marktechpost.com/2026/06/01/minimax-releases-minimax-m3-... (via search) — M3 launch date, MSA, 1M context
19. [S19] https://www.minimax.io/models/text/m3 (via search) — M3 SWE-Bench Pro 59.0% claim
20. [S20] https://cline.bot/blog/minimax-m2-5 (via search) — M2.5 2026-02-12, free-for-limited-time
21. [S21] https://www.datacamp.com/tutorial/minimax-code-minimax-m3 (via search) — MiniMax Code web/desktop naming
22. [S22] https://agent.minimax.io/docs/techblog/agent-team.md (via index) — Agent Team design blog
23. [S23] https://ir.minimax.io/corporate-information/management — named executives
24. https://www.minimax.io/news — product/model index, code.minimax.io link
25. https://platform.minimax.io/docs/llms.txt — Token Plan docs index (Claude Code/Cursor/Codex integrations)

## Inclusion check (Jesse's test)

**Yes** — MiniMax Code has its own first-party agentic loop (reads project context, edits files, runs commands/tests, verifies results, spawns Agent Teams) in both desktop and CLI forms; it is MiniMax's own harness for its M-series models, not a wrapper around another agent [S2][S8][S11].

## Proposed new census entry (per hc/agents/_TEMPLATE.md)

```yaml
name: "MiniMax Code"
slug: "minimax-code"
layout: "agent.njk"
category: "agent"
maker: "minimax"            # new makers.json record: company, CN, makes_models: true,
                            # revenue_model: [tokens, subscriptions]
license: "Proprietary (desktop); MIT (CLI npm package, bundled)"
url: "https://agent.minimax.io"
source_code_url: "https://github.com/MiniMax-AI/minimax-code"   # issue tracker only
source_available: False
homepage: "https://agent.minimax.io"
docs_url: "https://agent.minimax.io/docs/code/welcome"
download_url: "https://agent.minimax.io/download"
install_method: "npm install -g @minimax-ai/code | curl install.sh (filecdn.minimax.chat) | desktop .dmg/.exe"
platforms: ["CLI", "Desktop"]
autonomy_level: ["agentic", "autonomous-background"]   # Goal + scheduled tasks
specialization: "general"
language: null              # closed source (ships bundled JS on Node)
first_released: "2026-06-01"   # desktop under the MiniMax Code name (M3 launch; changelog line from 2026-05-01); CLI 2026-08-14
current_release: "2026-08-22"  # CLI 0.2.3; desktop v3.0.66 2026-08-19
maintained: "active"
mcp_support: True           # client
plugin_support: True
claude_code_plugin: "partial"   # skills/SKILL.md-compatible spirit, different manifest; no hooks/commands/agents
subagents: True             # Agent Team + Custom Agents
hooks: False
plan_mode: True
plugin_docs_url: "https://agent.minimax.io/docs/code/agents/plugins"
config_docs_url: "https://agent.minimax.io/docs/cli/features"
model_providers: "MiniMax (default); BYOK custom providers (OpenAI/Anthropic-compatible)"
pricing: "freemium"         # free tier; Token Plan $20/$50/$120/mo; credits
github_stars: 70            # issues-only repo; weak proxy
sources: ["paseo"]
last_verified: "2026-08-21"
what_makes_it_special: "MiniMax's own harness for its open-weight M-series models: a desktop agent app plus a brand-new mcode CLI (first-party ACP server), leading with Agent Teams, long-horizon Goals, memory, and phone/IM remote control rather than terminal-only coding."
```

Body suggestion: MiniMax Code is model-maker MiniMax's harness for its M-series coding models, grown out of the MiniMax Agent desktop app around the M3 launch (June 2026) and extended to the terminal with the `mcode` CLI in August 2026. The desktop app aims wider than coding — Work mode, Office plugins, scheduled tasks, and remote control from a phone or Telegram/WeChat/Lark/Feishu — while the CLI covers TUI, headless CI, and ACP editor integration; its TUI is derived from Mario Zechner's Pi TUI. Users are primarily Token Plan subscribers running MiniMax's M3/M2.7 models, with BYOK as an escape hatch.
