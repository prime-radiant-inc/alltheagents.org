# Dossier: Qwen Code (census_slug: qwen-code)

Compiled 2026-08-21 (some API fetches executed 2026-08-22 UTC). Facts only. Null convention: "null = not researched"; "False/none = researched and absent". Each non-obvious fact carries a source [Sn] (see section 7) and an as-of date.

Fork lineage (recorded precisely): the launch blog (2025-07-22) says "Forked from Gemini Code, Qwen Code has been adapted with customized prompts and function calling protocols" ("Gemini Code" = Google's Gemini CLI, Apache-2.0) [S10][S26]. The current README states: "This project was originally based on Google Gemini CLI v0.8.2 … Starting from Qwen Code v0.1, we stopped syncing with upstream and began independent development as a multi-protocol, multi-platform agent framework" [S1] (as-of 2026-08-21). So: hard fork of Gemini CLI at v0.8.2, upstream sync ended at Qwen Code v0.1; not a thin wrapper.

## 1. Identity

- name: Qwen Code
- maker: Qwen team, Alibaba Group (company; GitHub org "QwenLM"; Alibaba Cloud describes itself as "the digital technology and intelligence backbone of Alibaba Group"). Alibaba Group HQ Hangzhou, China [S11][S25] (as-of 2026-08-21).
- product URL: https://qwenlm.github.io/qwen-code-docs/en/users/overview (GitHub `homepage` field) [S2]; repo URL: https://github.com/QwenLM/qwen-code [S2]
- license: Apache-2.0 (GitHub API spdx; LICENSE file in repo; Homebrew formula) [S2][S3][S7] (as-of 2026-08-21). npm registry `license` field is unset [S4].
- open source? True. source_available: True — full monorepo source (TypeScript): 18 packages incl. cli, core, desktop, desktop-shell, web-shell, webui, vscode-ide-companion, zed-extension, acp-bridge, channels, chrome-extension, cua-driver, mobile-mcp, sdk-typescript, sdk-python, sdk-java [S2][S9] (as-of 2026-08-21).
- first public release: 2025-07-22 — announced in the Qwen3-Coder launch blog [S10]; first npm version 0.0.1 published 2025-07-22T14:36Z [S4]. GitHub repo created 2025-06-26 [S2]. Alibaba Cloud press release on the launch dated 2025-07-23 [S26].
- latest release: v0.21.15, 2026-08-20 (GitHub release 2026-08-20T17:38Z; npm latest 0.21.15 published 2026-08-20T17:36Z) [S5][S4]. 600 npm versions; dist-tags include `preview` and daily `nightly` builds [S4]. Desktop app "Qwen Code Desktop v0.1.0" declared officially launched in the 2026-08-06 weekly update [S22] (see section 6 for a version-tag conflict).
- what it is:
  - Form factors: terminal CLI (interactive TUI; headless `--prompt/-p` mode with structured/JSON output and session resume) [S1][S20]; VS Code companion extension, JetBrains plugin, Zed via ACP (`qwen --acp`) [S1][S16]; GitHub Actions [S13]; desktop app (native installers, macOS/Windows/Linux) [S22]; daemon `qwen serve` — local HTTP+SSE server, multiple clients share one agent session, spawns `qwen --acp` children [S15]; IM-bot channels (`qwen channel`): Telegram, WeChat, DingTalk, Feishu, WeCom, plus GitHub/GitLab channels [S1][S12]; web shell; SDKs (TypeScript, Python, Java); Computer Use desktop automation [S1][S12][S18].
  - Models: multi-protocol, not locked to Qwen — "Supports OpenAI, Anthropic, Gemini, and Qwen APIs. Any third-party provider or local model (Ollama / vLLM). Switch at runtime" [S1]. Auth options: Alibaba Cloud Model Studio Coding Plan (default models incl. qwen3-coder-plus, qwen3.7-plus, glm-5, kimi-k2.5, MiniMax-M2.5), API keys (OpenAI-compatible incl. OpenRouter/ModelScope/Azure, `ANTHROPIC_API_KEY`, `GEMINI_API_KEY`, Vertex AI) [S14] (as-of 2026-08-21).
  - Pricing: the tool itself is free, Apache-2.0 [S2]. Model access is paid or BYO: the free Qwen OAuth tier (originally 2,000 requests/day at launch per third-party guides, later 1,000/day) was cut to 100 requests/day on 2026-04-13 and discontinued entirely 2026-04-15 [S17][S14][S31]. Alibaba Cloud Model Studio "Coding Plan": Pro US$50/month international (¥200/month China), quotas up to 6,000 requests per 5 hours / 45,000 per week / 90,000 per month; Lite plan (~US$10/mo) closed to new subscriptions 2026-03-20 and to renewals 2026-04-13 [S19][S32]. ModelScope offers 2,000 free OpenAI-compatible API calls/day usable from Qwen Code (Alibaba's model-hosting platform) [S33] (as-of 2026-08-21).
  - Install: standalone install scripts — `curl … install-qwen-standalone.sh | bash` (Linux/macOS) and PowerShell `irm … install-qwen-standalone.ps1 | iex` (Windows), hosted on an Alibaba OSS bucket; `npm install -g @qwen-code/qwen-code@latest` (Node.js >= 22); `brew install qwen-code` [S1][S4][S7].
  - Default autonomy: five approval modes — Plan (read-only), "Ask Permissions" (default: manual approval for all edits and commands), Auto-Edit, Auto (LLM classifier auto-approves safe shell/network/out-of-workspace actions, blocks risky ones), YOLO; cycled with Shift+Tab; optional sandboxing; setting `tools.approvalMode` [S21] (as-of 2026-08-21).
  - Repo language per GitHub API: TypeScript [S2].

## 2. Adoption evidence

| metric / claim | value | as-of | source | type |
|---|---|---|---|---|
| GitHub stars | 27,279 | 2026-08-21 | [S2] | independently observable |
| GitHub forks | 2,908 | 2026-08-21 | [S2] | independently observable |
| GitHub watchers (subscribers) | 135 | 2026-08-21 | [S2] | independently observable |
| GitHub open issues+PRs | 1,176 | 2026-08-21 | [S2] | independently observable |
| GitHub issues ever filed (search API) | 3,900 | 2026-08-21 | [S6] | independently observable |
| GitHub merged PRs ever (search API) | 4,224 | 2026-08-21 | [S6] | independently observable |
| GitHub contributors (incl. anonymous) | 528 | 2026-08-21 | [S6] | independently observable |
| Commits, last 90 days (since 2026-05-23, default branch) | 2,787 (note: includes heavy automated/nightly and self-agent commit traffic; README: Qwen Code "us[es] its own agent … to file issues, submit PRs, review code") | 2026-08-21 | [S6][S1] | independently observable |
| Release cadence | daily nightlies + roughly weekly stable (v0.21.14 2026-08-19, v0.21.15 2026-08-20); 100 releases on first API page alone | 2026-08-21 | [S5] | independently observable |
| npm weekly downloads, @qwen-code/qwen-code | 64,525 (2026-08-14..20) | 2026-08-20 | [S8] | independently observable |
| npm monthly downloads, @qwen-code/qwen-code | 285,215 (2026-07-22..08-20) | 2026-08-20 | [S8] | independently observable |
| npm cumulative downloads since launch | ~3.91M (sum of npm range API 2025-07-01..2026-08-21); peak month 504,355 (Apr 2026) | 2026-08-21 | [S8] | independently observable |
| npm weekly, @qwen-code/sdk (TS SDK) | 5,321 | 2026-08-20 | [S8] | independently observable |
| PyPI monthly, qwen-code-sdk | 16,714 | 2026-08-21 | [S8] | independently observable |
| Homebrew installs (formula qwen-code) | 6,087 (30d) / 16,686 (90d) / 67,798 (365d) | 2026-08-21 | [S7] | independently observable |
| VS Code Marketplace, "Qwen Code Companion" (qwenlm.qwen-code-vscode-ide-companion) | 333,403 installs | 2026-08-21 | [S24] | independently observable |
| GitHub Discussions | active; categories Announcements/General/Ideas/Polls/Q&A/Show-and-tell; 6+ pages; newest 2026-08-20 | 2026-08-21 | [S23] | independently observable |
| "300+ merged pull requests" in one week (v0.21.2–v0.21.6) | weekly update 2026-08-06 | 2026-08-06 | [S22] | maker-claimed |
| Qwen model family >3B downloads; >460 models; 300k+ derivative models | Alibaba claim, widely reported ~2026-08-15 — NOTE: this is the model family, NOT Qwen Code the CLI | 2026-08 | [S27] | maker-claimed (press-relayed) |
| Qwen consumer app 203M MAU | press-reported, family-level context only | 2026-08 | [S27] | maker-claimed (press-relayed) |
| Qwen3-Coder launch HN reception | 765 points / 366 comments | 2025-07 | [S28] | independently observable |
| Press coverage | Simon Willison (2025-07-22, notes the Gemini CLI fork); VentureBeat covers Qwen3-Coder/-Next models (Qwen Code mentioned as companion CLI); Alibaba Cloud press room | 2025-2026 | [S10][S26][S28] | independently observable |
| Listed in Zed ACP agent registry ("An open-source AI agent for the terminal, optimized for Qwen3-Coder") | yes | 2026-08-21 | [S16] | independently observable |
| Funding/valuation | none separate — Alibaba Group subsidiary product (NYSE: BABA); no Qwen-Code-specific revenue disclosed | 2026-08-21 | [S25] | n/a |
| Maker-published Qwen-Code-specific usage numbers (users/downloads) | none found — weekly updates and blog contain no CLI adoption figures | 2026-08-21 | [S22][S30] | researched and absent |

## 3. Plugin interface (six census fields)

- mcp_support: **client** (no server mode documented). Transports stdio / HTTP (recommended) / SSE (deprecated); config in `settings.json` `mcpServers` or `qwen mcp add/remove`; OAuth 2.0 with token refresh; `/mcp` management dialog; MCP prompts become slash commands; resources injectable via `@server:uri`; background/progressive server discovery. Evidence: https://qwenlm.github.io/qwen-code-docs/en/users/features/mcp/ [S34] (as-of 2026-08-21).
- plugin_support: **True — extensions + skills, with multi-marketplace ingestion.** Extensions are installable units (`qwen-extension.json` manifest) bundling commands, skills, MCP servers, subagents, context file (default QWEN.md), settings, and channel adapters; install from GitHub URL/`owner/repo`, local path, .zip/.tar.gz, archive URL, npm scoped package, or marketplace sources (`qwen extensions install|list|update|uninstall|enable|disable|sources`; `/extensions` hot-reload UI with a Discover/browse tab) [S35]. Skills: `SKILL.md` packages in `~/.qwen/skills/`, `.qwen/skills/`, or extension `skills/` dirs; model- or user-invoked; auto-generated "Auto-Skills" (`/learn`, `/curator`, staleness/archival lifecycle) [S36] (as-of 2026-08-21).
- claude_code_plugin: **partial-yes.** Docs: "Extensions and plugins from Gemini CLI Extensions Gallery, Claude Code Marketplace, Qoder, and the portable Agent Plugins v1 format can be directly installed into Qwen Code"; `qwen extensions install <marketplace-name>:<plugin-name>`; "Claude plugins are automatically converted to Qwen Code format during installation: `claude-plugin.json` is converted to `qwen-extension.json`" [S35]. Subagent definitions accept "Claude Code 2.1.168 frontmatter fields" (permissionMode→approvalMode mapping; some fields like `effort`, `memory` not yet implemented) [S37]. Context: reads `AGENTS.md` if present, but primary file is `QWEN.md`; no documented reading of `CLAUDE.md` or `.claude/skills` [S38][S36]. So: Claude Code marketplace plugins install via automatic conversion (not native execution of the .claude-plugin format).
- subagents: **True.** Markdown+YAML agents in `.qwen/agents/` (project), `~/.qwen/agents/` (user), or extensions; invoked automatically, by name, or via Task tool; "fork subagents" run detached in parallel with inherited context and shared prompt-cache prefix (claimed 80%+ token saving); nested sub-agents; per-task permission profiles (`.qwen/fork-profiles/`); background agents resumable via `list_agents`/`send_message`. Also "Agent Team" runtime (`/coordinate`, up to three workstreams, one writer in a git worktree) and "Arena" (competing models on the same task) [S37][S39][S22] (as-of 2026-08-21).
- hooks: **True.** 19 events: PreToolUse, PostToolUse, PostToolUseFailure, UserPromptSubmit, SessionStart, SessionEnd, SessionDelete, MessageDisplay, Stop, StopFailure, SubagentStart, SubagentStop, PreCompact, PostCompact, Notification, PermissionRequest, PermissionDenied, TodoCreated, TodoCompleted; executor types command / http / prompt (/ internal function); configured in `.qwen/settings.json` `hooks` [S40] (as-of 2026-08-21).
- plan_mode: **True.** Plan Mode is one of the five approval modes — read-only analysis, no edits/shell; entered via `/plan`, Shift+Tab cycling, or `"approvalMode": "plan"` [S21] (as-of 2026-08-21).
- plugin_docs_url: https://qwenlm.github.io/qwen-code-docs/en/users/extension/introduction/ [S35]
- config_docs_url: https://qwenlm.github.io/qwen-code-docs/en/users/configuration/settings/ [S14]
- ACP support: **yes** — `qwen --acp` (JSON-RPC/stdio) used by Zed (ACP Registry entry; manual custom-agent config also documented) and by the `qwen serve` daemon internally; listed on agentclientprotocol.com agents list; community "Qwen Code Claw / acpx" lets other agents delegate to Qwen Code over ACP [S16][S15][S41][S1] (as-of 2026-08-21).
- SDK: **yes** — TypeScript `@qwen-code/sdk` (npm), Python `qwen-code-sdk` (PyPI, alpha), Java (alpha); `query()` API with streaming, tools, MCP, permission modes; labeled experimental; requires local Qwen Code >= 0.4.0, Node >= 22 [S18][S1] (as-of 2026-08-21).

## 4. Claimed differentiation

- tagline: "The open-source AI coding agent that lives in your terminal." — README [S1]; docs overview: "Qwen's agentic coding tool that lives in your terminal and helps you turn ideas into code faster than ever before" [S12].
- Maker claims (paraphrased, each with source):
  - Agentic out of the box: Auto-Memory, Auto-Skills, SubAgents, Agent Teams, MCP — "Dynamic workflows, zero setup" [S1].
  - Open source "inside and out": both the framework and the Qwen models are open source and "evolve together. No vendor lock-in" [S1].
  - Multi-protocol: OpenAI, Anthropic, Gemini, Qwen APIs, any third-party or local model, switchable at runtime — README presents this as a ✓ vs Claude Code "—" [S1].
  - Beyond the terminal: IDE plugins, desktop app, daemon mode, SDKs, IM bots (Telegram/DingTalk/WeChat/Feishu) — also positioned as a differentiator vs Claude Code [S1].
  - Explicit Claude Code parity positioning: "If you know Claude Code, you already know Qwen Code — and then some", linking a third-party/collaborator parity report; a feature-comparison table vs Claude Code sits in the README [S1]. Developer roadmap states the goal to "Catch up with Claude Code's product functionality" [S42].
  - Self-developing: "Qwen Code is actively iterating on itself — using its own agent and models to file issues, submit PRs, review code, and run tests" [S1].
  - Computer Use (cross-platform desktop automation) and Git-worktree isolated parallel sessions as headline features [S1][S30].
- Audience: developers using the terminal; docs list use cases (build features from descriptions, debug, navigate codebases, automate chores) [S12]; Alibaba Cloud press release: "enables developers to delegate engineering tasks to AI using natural language" [S26]. No team-size/stack segmentation claimed.

## 5. Company & contact targets (company-level)

- Company: Alibaba Group Holding Limited (NYSE: BABA / HKEX: 9988), HQ Hangzhou, China [S26][S25]. Product sits with the Qwen team / Alibaba Cloud ("digital technology and intelligence backbone of Alibaba Group", founded 2009) [S26]. Alibaba Cloud international operations HQ'd in Singapore per Wikipedia [S25]. Size: Alibaba Group is a public mega-cap; no Qwen-Code-team headcount published (none found).
- Funding stage: n/a (wholly-owned business of a listed company) [S25].
- Publicly named leadership (company-named sources only):
  - Eddie Wu (Wu Yongming) — Chief Executive Officer, Alibaba Group (since Sept 2023); named on Alibaba's own leadership page https://www.alibabagroup.com/en-US/about-alibaba-leadership-1637927598568767488 (page is JS-rendered; title corroborated by Alibaba SEC filing exhibit) [S43] (as-of 2026-08-21).
  - No named product/DevRel/partnerships lead for Qwen Code appears in official Qwen materials (README, docs, weekly updates carry no bylines) — researched and absent [S1][S22][S30].
  - Press-reported (NOT company-page-verified, include with caution): April 2026 Alibaba AI reorg — CEO-led tech committee; Zhou Jingren moved from Alibaba Cloud CTO to "Chief AI Architect" leading Tongyi Lab; Li Feifei appointed cloud CTO (Caixin/SCMP/Benzinga, 2026-04-08) [S44].

## 6. Open questions / conflicts

- Census entry `first_released: "2025-06-26"` is the GitHub repo creation date, not a public release; public launch was 2025-07-22 (blog + first npm publish) [S2][S4][S10].
- Census entry `stars: null` → 27,279 as of 2026-08-21 [S2]. `claude_code_plugin: null` → partial-yes (marketplace plugins auto-converted) [S35]. `plugin_docs_url`/`config_docs_url: null` → both exist (section 3).
- Census `pricing: "Free / open source"` is incomplete: the CLI is free, but the free hosted-model tier (Qwen OAuth) was discontinued 2026-04-15; hosted usage now requires a Coding Plan (US$50/mo Pro), API keys, or free ModelScope quota [S17][S19][S33].
- Census `maker: "QwenLM"` is the GitHub org name; the maker is the Qwen team at Alibaba (Alibaba Cloud) [S26].
- Census `sources` list (jqueryscript/brad/ishandutta/tiennm) are third-party blogs, not official materials.
- Desktop-app version conflict: weekly update 2026-08-06 announces "Qwen Code Desktop v0.1.0 … officially released"; the `desktop-latest` GitHub tag points at desktop-v0.0.5 (auto-update feed) and `packages/desktop/package.json` reads name "openwork", version 0.0.5; press mentions v0.2.1 mid-Aug — versioning across channels is inconsistent [S22][S45][S9].
- Free-tier history is messy: launch-era third-party guides say 2,000 requests/day via Qwen OAuth; the maintainer's shutdown notice (#3203) describes 1,000/day cut to 100/day on 2026-04-13, then full closure 2026-04-15. The 2,000/day figure could not be confirmed in an official doc (docs page now just says discontinued) [S31][S17][S14].
- Benchmarks: no official SWE-bench/Terminal-Bench score is published for Qwen Code as a harness; Qwen model cards report scores (e.g., Qwen3.6: 73.4 SWE-bench Verified; Qwen3.8-Max: 86.6 Terminal-Bench 2.1) using internal/various scaffolds — model claims, not harness claims [S29]. Repo release tags include internal eval runs ("DSW EAS SWE 500 + Terminal-Bench 89 full") with no published numbers [S5].
- The 3B-downloads figure often quoted near Qwen Code is the Qwen model family, not the CLI; no maker-published Qwen-Code-specific user/download number exists (npm ~3.91M cumulative is the best observable proxy) [S27][S8].
- Leadership churn (press only, unverified by company pages): 36kr/geopolitechs report the head of Qwen Code ("Huibin") left for Meta in Jan 2026 and Qwen tech lead Junyang Lin departed 2026-03-04 after a team-reorg dispute [S46]. Treat as unconfirmed.
- Unreachable/failed sources: https://www.alibabagroup.com/en-US/about-alibaba-leadership renders no content via fetch (JS-only); the Eddie Wu bio page and the Caixin 2026-04-08 reorg article could not be fetched before a session limit (titles taken from search snippets); X/Twitter posts (@Alibaba_Qwen Coding Plan launch, ~2026-02-21, "from ~$10/mo (Lite) or ~$50/mo (Pro)") not directly fetchable — relied on search snippets [S32][S43][S44].

## 7. Sources

1. [S1] https://raw.githubusercontent.com/QwenLM/qwen-code/main/README.md — tagline, claims, fork statement, install, surfaces
2. [S2] https://api.github.com/repos/QwenLM/qwen-code — stars/forks/dates/license/language
3. [S3] https://raw.githubusercontent.com/QwenLM/qwen-code/main/LICENSE — Apache-2.0 text
4. [S4] https://registry.npmjs.org/@qwen-code/qwen-code — versions, publish dates, engines, bin
5. [S5] https://api.github.com/repos/QwenLM/qwen-code/releases — release cadence, eval tags
6. [S6] GitHub search/contributors/commits APIs (link-header counts) — contributors 528, commits 2,787/90d, issues 3,900, merged PRs 4,224
7. [S7] https://formulae.brew.sh/api/formula/qwen-code.json — brew installs, license
8. [S8] https://api.npmjs.org/downloads/... (@qwen-code/qwen-code, @qwen-code/sdk) + https://pypistats.org/api/packages/qwen-code-sdk/recent — download counts
9. [S9] https://github.com/QwenLM/qwen-code/tree/main/packages — 18 packages
10. [S10] https://qwenlm.github.io/blog/qwen3-coder/ — 2025-07-22 launch, "Forked from Gemini Code"
11. [S11] https://qwenlm.github.io/qwen-code-docs/en/users/overview — self-description, docs nav
12. [S12] https://qwenlm.github.io/qwen-code-docs/en/users/overview (channels/features nav) — IM channels, capabilities
13. [S13] docs nav: integration-github-action — GitHub Actions surface
14. [S14] https://qwenlm.github.io/qwen-code-docs/en/users/configuration/auth/ — auth options, OAuth discontinued, Coding Plan models
15. [S15] https://qwenlm.github.io/qwen-code-docs/en/users/qwen-serve/ — daemon, HTTP+SSE, `qwen --acp` children
16. [S16] https://qwenlm.github.io/qwen-code-docs/en/users/integration-zed/ + https://zed.dev/acp/agent/qwen-code — ACP integration, registry entry
17. [S17] https://github.com/QwenLM/qwen-code/issues/3203 — OAuth free tier 1,000→100/day 2026-04-13, closed 2026-04-15
18. [S18] https://qwenlm.github.io/qwen-code-docs/en/developers/sdk-typescript/ — SDK packages/status
19. [S19] https://help.aliyun.com/en/model-studio/coding-plan + https://www.alibabacloud.com/help/en/model-studio/coding-plan — ¥200 / $50 Pro, quotas, tool list, Lite dates
20. [S20] https://raw.githubusercontent.com/QwenLM/qwen-code/main/docs/users/features/headless.md — headless flags, sessions, /goal
21. [S21] https://qwenlm.github.io/qwen-code-docs/en/users/features/approval-mode/ — five modes, default, plan mode
22. [S22] https://qwenlm.github.io/qwen-code-docs/en/blog/updates/weekly-update-2026-08-06/ — desktop v0.1.0 launch, 300+ PRs/week
23. [S23] https://github.com/QwenLM/qwen-code/discussions — categories, activity
24. [S24] VS Code Marketplace extensionquery API (qwenlm.qwen-code-vscode-ide-companion) — 333,403 installs
25. [S25] https://en.wikipedia.org/wiki/Alibaba_Cloud — founding, parent, HQs
26. [S26] https://www.alibabacloud.com/en/press-room/alibaba-unveils-cutting-edge-ai-coding-model-qwen3 — 2025-07-23 press release, open-sourcing Qwen Code, boilerplate
27. [S27] https://fortune.com/2026/08/15/alibaba-qwen-open-ai-models-3-billion-downloads-meta-google/ (+ EqualOcean, windowsforum) — 3B model-family downloads claim
28. [S28] https://simonwillison.net/2025/Jul/22/qwen3-coder/ + https://locoroo.net/reports/2026-april/alibaba — press/analyst coverage, HN 765 points
29. [S29] search results: nxcode.io / kingy.ai / emergent.sh Qwen3.6-3.8 benchmark write-ups; arxiv 2603.00729 (Qwen3-Coder-Next TR) — model benchmark context
30. [S30] https://qwenlm.github.io/qwen-code-docs/en/blog/updates/ — weekly update index (Feb 2026 onward), no adoption metrics
31. [S31] https://aiengineerguide.com/til/qwen-code-cli-free-tier/ (+ blog.balakumar.dev) — launch-era 2,000 req/day free-tier reports (third-party)
32. [S32] https://x.com/Alibaba_Qwen/status/2024136381308805564 (via search snippet) + https://xueqiu.com/9216592857/376560484 — Coding Plan launch ~2026-02-21, Lite ~$10 / Pro ~$50
33. [S33] https://blog.balakumar.dev/2025/08/26/get-2000-free-qwen3-coder-api-requests-daily-use-with-claude-code-roo-cline-more/ + freellm.net/providers/modelscope — ModelScope 2,000 free calls/day
34. [S34] https://qwenlm.github.io/qwen-code-docs/en/users/features/mcp/ — MCP client details
35. [S35] https://qwenlm.github.io/qwen-code-docs/en/users/extension/introduction/ (+ raw docs/users/extension/introduction.md) — extensions, Claude/Gemini/Qoder marketplace ingestion, conversion
36. [S36] https://qwenlm.github.io/qwen-code-docs/en/users/features/skills/ — SKILL.md, dirs, auto-skills, /learn
37. [S37] https://qwenlm.github.io/qwen-code-docs/en/users/features/sub-agents/ (+ raw sub-agents.md) — subagents, fork agents, Claude Code 2.1.168 frontmatter compat
38. [S38] https://qwenlm.github.io/qwen-code-docs/en/users/features/memory/ — QWEN.md, AGENTS.md fallback, auto-memory
39. [S39] https://qwenlm.github.io/qwen-code-docs/en/users/features/multi-agent-coordination/ — Agent Team, Arena
40. [S40] https://qwenlm.github.io/qwen-code-docs/en/users/features/hooks/ — 19 hook events, executors
41. [S41] https://agentclientprotocol.com/get-started/agents (via search) + https://github.com/openclaw/acpx — ACP listings
42. [S42] https://qwenlm.github.io/qwen-code-docs/en/developers/roadmap/ — "Catch up with Claude Code" goal
43. [S43] https://www.alibabagroup.com/en-US/about-alibaba-leadership-1637927598568767488 (+ SEC exhibit via search) — Eddie Wu, CEO (fetch blocked; search-snippet sourced)
44. [S44] https://www.caixinglobal.com/2026-04-08/alibaba-revamps-ai-structure-with-new-tech-committee-102431852.html (+ SCMP, Benzinga, startupintros) — Apr 2026 reorg (press; fetch blocked)
45. [S45] https://github.com/QwenLM/qwen-code/releases/tag/desktop-latest + packages/desktop/package.json — desktop tag/version conflict
46. [S46] https://eu.36kr.com/en/p/3807382930251523 + https://www.geopolitechs.org/p/inside-the-stepping-down-of-qwens + https://mlq.ai/news/... — leadership departures (press, unconfirmed)
47. https://github.com/wenshao/codeagents/blob/main/docs/comparison/qwen-code-improvement-report.md — parity report linked from README (280+ items, ~60% implemented; 2026-06-20)
48. https://qwenlm.github.io/qwen-code-docs/en/blog/updates/weekly-update-2026-08-13/ — Agent Plugins v1, Qoder plugins, QR takeover

## Inclusion check (Jesse's test)

**Yes** — Qwen Code is a full coding agent with its own agentic loop (reads/edits files, runs shell, plans, iterates; loop also exposed headless, via SDKs, and as an ACP server). It is a hard fork of Gemini CLI (v0.8.2 base, independent since v0.1), not a thin wrapper around someone else's agent [S1][S10].
