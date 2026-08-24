# Dossier: TRAE CLI / Trae Agent (census_slug: trae-agent)

Compiled 2026-08-24 (task dated 2026-08-21). Facts only. Null convention: "null = not researched"; "False/none = researched and absent". Sources [Sn] in section 7.

## 0. One product or two? (the question this dossier was asked to settle)

**Two different products sharing the TRAE brand.** Recommendation: **two census entries.**

1. **trae-agent** (github.com/bytedance/trae-agent) — an open-source (MIT) **Python research agent** by ByteDance's "Trae Research Team". Invoked as `trae-cli` (installed via `git clone` + `uv sync`), BYO API keys, YAML config `trae_config.yaml`. Built for "studying AI agent architectures, conducting ablation studies" [S1]. No ACP support anywhere in the repo docs (researched, absent) [S1]. Development has stalled: last commit 2026-02-05, zero GitHub releases or tags ever [S2].
2. **TRAE CLI**, product name in docs "**TraeCode CLI**" (docs.trae.cn/cli_*) — a **closed-source commercial CLI** shipped as a native binary `traecli`, installed via `curl https://trae.cn/trae-cli/install.sh`, login with **enterprise credentials**; available only to TRAE Enterprise Edition flagship-tier (旗舰版) customers [S3][S4]. Has ACP (`traecli acp serve`), MCP client, skills, custom agents, permission modes, worktrees — none of which match the OSS repo [S5]-[S9]. Docs reference "TraeCode CLI 1.0" [S9].

Divergence evidence: different binary names (`trae-cli` vs `traecli`), different config files (`trae_config.yaml` vs `trae_cli.yaml`), different install channels (git clone vs trae.cn installer), different licensing (MIT vs proprietary/enterprise login), different feature sets (no ACP/skills/permission-modes in OSS; no BYO-provider flags documented for the product), different activity (OSS dormant since 2026-02-05; product docs describe a 1.0 actively documented in 2026) [S1][S2][S3][S5][S9]. They are related — same company, and the arXiv paper behind trae-agent is by the "Trae Research Team" [S10] — but the product is not the repo.

**Paseo mapping:** Paseo's `traecli` provider runs `traecli acp serve` and links docs.trae.cn/cli_get-started-with-trae-cli as the install link [S11] — i.e., Paseo drives **TRAE CLI (the commercial product), not trae-agent**. The roster line mapping paseo_id `traecli` → census_slug `trae-agent` is therefore a mis-mapping; the existing census entry describes the OSS repo.

Suggested fix: keep `trae-agent` for the OSS research agent (mark maintenance stalled), add a new entry (e.g. `trae-cli` or `trae`) for the commercial TRAE coding product (IDE + SOLO/TraeWork + plugin + CLI), and point Paseo's `traecli` at the new entry.

## 1. Identity

### 1a. TRAE (the commercial product family, incl. TRAE CLI)
- name: TRAE ("The Real AI Engineer" per third-party coverage [S20]); China docs now brand the coding products "TraeCode" (TraeCode IDE, TraeCode Plugin, TraeCode CLI) and the SOLO app "TraeWork" [S4][S12]; international docs landing likewise announces "TraeWork is available" and titles SOLO docs "What is TraeWork?" [S13] (as-of 2026-08-24).
- maker: ByteDance (company; HQ Beijing/PRC group; international TRAE operated from Singapore — the 2025-09-23 launch press release is issued by "TRAE (Singapore)" [S14]; JetBrains marketplace vendor for the TRAE plugin is "MarsCode", Singapore, verified organization [S15]). TRAE evolved from ByteDance's earlier MarsCode product [S15][S16].
- product URLs: international https://www.trae.ai (docs https://docs.trae.ai); China https://www.trae.cn (docs https://docs.trae.cn). CLI docs exist only on the China docs site (`docs.trae.cn/cli_*`); no CLI section found on docs.trae.ai (researched via site search, absent) [S17].
- repo URL: none for the product (closed source). source_available: False for IDE/CLI/SOLO. The IDE is a fork of Code OSS (VS Code's open base) [S18][S19].
- license: proprietary; CLI additionally gated behind TRAE Enterprise flagship-tier login [S3].
- first public release: TRAE IDE launched ~2025-01-19/20 (press coverage 2025-01-27; Baidu Baike gives 2025-01-19) [S16][S20]; China version (trae.cn) with Doubao/DeepSeek models followed ~March 2025 [S16]. SOLO mode announced 2025-07-21 [S21]; global SOLO/"TRAE 2.0" launch press release 2025-09-23 [S14]. TRAE 企业版 (Enterprise Edition, China) announced 2025-12-18 [S22]. TRAE CLI: no public launch date found; docs reference "TraeCode CLI 1.0"; a TRAE staffer confirmed CLI is enterprise-only with "no plans" for individual availability on 2026-03-10 [S9][S3].
- latest release: null for CLI version beyond "1.0" (docs.trae.cn/cli_release-notes 404s [S23]); IDE changelog exists at docs.trae.ai/ide/changelog (not itemized here).
- what it is (CLI surface): a terminal Code Agent ("Your dedicated Code Agent" — 专属的 Code Agent) that takes natural-language instructions for coding, testing and Git tasks; multiple built-in LLMs "plus OpenAI/Claude support" (no BYO-key docs found); defaults to "Max mode" with a usage-consumption caution; asks before non-read-only tool calls in `default` permission mode [S4][S8]. Installed by shell installer on Windows 10+/macOS 14.7.8+/Ubuntu 20.04+/Debian 10+, x86_64+ARM64; auto-updates on startup, `traecli update` manual [S3].
- what it is (IDE surface): VS Code-fork AI IDE with Builder/agent chat, SOLO end-to-end autonomous mode (PRD→code→deploy), custom agents, MCP, rules, skills; free tier plus paid plans; models incl. Claude/GPT/DeepSeek/Doubao depending on region [S16][S14][S21][S24].

### 1b. trae-agent (OSS)
- name: Trae Agent | maker: ByteDance (company) | repo https://github.com/bytedance/trae-agent | license MIT | source_available: True (fully open) [S1][S2].
- first public: repo created 2025-06-13, initial commit 2025-06-14 [S2]. Latest activity: last commit 2026-02-05 ("fix(openai): persist tool outputs...") ; **no releases, no tags ever published**; not on PyPI (install is git clone + uv) [S2][S1]. Only 3 commits since 2025-09-08; 0 commits in the 90 days before 2026-08-21 [S2].
- what it is: Python 3.12+ CLI agent (`trae-cli run|interactive|show-config`); multi-LLM (OpenAI, Anthropic, Doubao, Azure, OpenRouter, Ollama, Google Gemini; custom base_url); tools: bash, str_replace edit, sequential thinking, task_done; Lakeview step summaries; trajectory recording to JSON; Docker execution mode (`--docker-image`, `--dockerfile-path`, container attach); MCP servers via `mcp_servers:` config; max_steps config (example 200) [S1]. Free / BYO API keys [S1].
- research pedigree: arXiv 2507.23370 "Trae Agent: An LLM-based Agent for Software Engineering with Test-time Scaling" (submitted 2025-07-31, Trae Research Team, 15 listed authors): agent-based ensemble (generation/pruning/selection), claims **first place on SWE-bench Verified with 75.20% Pass@1** [S10].

## 2. Adoption evidence

| metric / claim | value | as-of | source | type |
|---|---|---|---|---|
| trae-agent GitHub stars | 12,046 | 2026-08-21 | [S2] | independently observable |
| trae-agent GitHub forks | 1,341 | 2026-08-21 | [S2] | independently observable |
| trae-agent watchers / open issues | 66 / 158 | 2026-08-21 | [S2] | independently observable |
| trae-agent contributors (incl. anon) | 52 | 2026-08-21 | [S2] | independently observable |
| trae-agent issues ever / PRs ever | 163 / 268 | 2026-08-21 | [S2] | independently observable |
| trae-agent commits, last 90 days | 0 (last commit 2026-02-05) | 2026-08-21 | [S2] | independently observable |
| trae-agent releases/tags | 0 | 2026-08-21 | [S2] | independently observable |
| TRAE registered users | 6M+, ~200 countries | 2025-12-29 ("2025 Product Report") | [S24][S25] | maker-claimed |
| TRAE monthly active users | 1.6M+ | 2025-12-29 (same report) | [S24][S25] | maker-claimed |
| TRAE MAU | 1M+ | 2025-06-11/12 (Volcano Engine announcement) | [S26] | maker-claimed |
| TRAE "users" | "12M" (2026-06-01) | 2026-06 | [S27] | third-party blog, **no primary source found — treat as unverified** |
| Annual usage (2025 report) | ~60M sessions, 500M queries, ~100B lines of code generated in 2025; token consumption +700% in 6 months | 2025-12-29 | [S24][S25] | maker-claimed |
| Mode adoption | Builder used by 80% of users; SOLO ~40% (30% China / 44% intl per GeekPark); 365k custom agents created; 11,000+ MCP tools/servers integrated | 2025-12-29 | [S24][S25] | maker-claimed |
| Internal ByteDance use | 92% of ByteDance engineers use TRAE; AI code = 43% of contributions in a Douyin team | 2025-12-29 | [S25][S22] | maker-claimed |
| JetBrains "TRAE AI: Coding Assistant" plugin downloads | 3,645,423 (vendor MarsCode, SG; latest 1.7.0.4) | 2026-08-24 | [S15] | independently observable |
| VS Code Marketplace | no official TRAE-published coding-agent extension found under "Trae" search (only third-party themes/utilities; "Trae AI Helper" 1,786 installs) — the TraeCode Plugin for VS Code is distributed via docs/marscode.com | 2026-08-24 | [S28][S12] | independently observable (absence) |
| SWE-bench Verified | 75.20% Pass@1, claimed #1 at submission | 2025-07-31 | [S10] | maker-claimed (paper) |
| Discord (trae-agent README badge, server 1320998163615846420) | member count unobtainable (widget disabled) | 2026-08-24 | [S1][S29] | null (not obtainable) |
| TRAE CLI adoption | none public (enterprise flagship-tier only; staff: no plans for individuals, 2026-03-10) | 2026-08-24 | [S3] | researched, absent |
| Press/third-party signals | The Register: telemetry sent despite opt-out, ~500 calls/26MB in ~7 min (2025-07-28, Unit 221B research; ByteDance responded) [S18]; InfoQ on free Claude 3.7/DeepSeek R1 (2025-03) [S16]; Reuters-carried global launch PR (2025-09-23) [S14]; GeekPark year-review (2025-12-29) [S25] | 2026-08-24 | — | press |
| Pricing-tier evidence of monetization | Pro plan $10/mo with 600 fast requests announced on X 2025-05-27; five tiers Free/$3 Lite/$10 Pro/$30 Pro+/$100 Ultra with token credits from ~2026-06-26 | 2026-06 | [S30][S31] | maker-claimed (X) / third-party (tier table) |

## 3. Plugin interface (six census fields)

### TRAE CLI (TraeCode CLI — the thing Paseo drives)
- mcp_support: **client** — stdio, SSE (OAuth w/ RFC 8414/7591 discovery), Streamable HTTP; configured in global `trae_cli.yaml` via `traecli config edit`; `/mcp` status/auth command; also reads TraeCode IDE project-level `.trae/mcp.json`. No MCP-server mode documented. Evidence: https://docs.trae.cn/cli_model-context-protocol [S6] (as-of 2026-08-24)
- plugin_support: **partial** — a `/plugin` (`/plugins`) management command exists (contents undocumented on the pages read); skills system: `SKILL.md` + YAML frontmatter in `.traecli/skills/` (project) and `~/.traecli/skills/` (global), on-demand loading, progressive disclosure; also reads legacy IDE dirs `.trae/skills/` and `~/.trae-cn/skills`; custom slash commands as Markdown in `.traecli/commands/` with `$1`/`$ARGUMENTS` substitution. No marketplace documented. Evidence: https://docs.trae.cn/cli_skills ; https://docs.trae.cn/cli_slash-commands [S7][S9]
- claude_code_plugin: **no** — docs use own `.traecli/` tree; no mention of CLAUDE.md, `.claude/`, or Claude Code plugin format anywhere in the CLI docs read (researched, absent). AGENTS.md is used for project instructions (`/init` generates one) [S9].
- subagents: **yes** — custom agents as Markdown+frontmatter (`name`, `description`, `tools` incl. `mcp__server__tool`, `model`) in `.traecli/agents/`; auto task decomposition/delegation to matching agents, or explicit `@{agent_name}`; created via `/agent-new`. Evidence: https://docs.trae.cn/cli_agent [S5]
- hooks: **none found** — no hooks page or hook mention in the CLI docs read (researched, absent within the pages accessible; docs.trae.cn/cli_hooks returns 400) [S23].
- plan_mode: **yes** — `permission_mode: plan` ("AI analyzes requirements and generates a plan for user confirmation before execution"); other modes `default` (ask before non-read-only tools) and `bypass_permissions` (狂飙 "wild" mode); plus `-y/--yolo` flag. Evidence: https://docs.trae.cn/cli_permission-mode [S8][S9]
- ACP: **yes, first-party** — `traecli acp serve`; Zed integration documented; clients normally spawn it as a subprocess. Evidence: https://docs.trae.cn/cli_acp [S5-ACP]. Paseo runs exactly this command and notes traecli publishes slash commands and skills asynchronously over ACP [S11].
- SDK: none documented for the CLI (researched, absent). Headless: `-p/--print` (+ `--json`), `--allowed-tool`, `--disallowed-tools`, `-w/--worktree` isolated git worktrees, timeouts — CI-ready [S9].
- plugin_docs_url: https://docs.trae.cn/cli_skills (closest); config_docs_url: https://docs.trae.cn/cli_permission-mode + `traecli config edit` (`trae_cli.yaml`).

### TRAE IDE (context)
- MCP client with marketplace ("11,000+ MCP" maker claim [S24]); custom agents with MCP tools (docs.trae.ai/ide/agent, /use-mcp-servers-in-agents [S32]); rules (docs.trae.ai/ide/rules-for-ai); skills rolled out in SOLO first, IDE in progress; skills dirs: convention `.agents/skills/` auto-discovered, `.trae/skills/` takes precedence on name clash [S33]. Hooks: none found in IDE docs (researched lightly, absent).

### trae-agent (OSS)
- mcp_support: **client** (`mcp_servers:` YAML, stdio commands e.g. Playwright) [S1]; plugin_support: **False** (no plugin/skill system); claude_code_plugin: **no**; subagents: **False** as a user feature (multi-agent ensemble exists as research method in the paper [S10]); hooks: **False**; plan_mode: **False** (none documented); ACP: **False**; SDK: on the roadmap only (headless interface "planned") [S34].

## 4. Claimed differentiation

- TRAE tagline (trae.ai): "Collaborate with Intelligence"; products "TraeWork — Professional AI Work Assistant" and "TraeCode — 10x AI Coding Engineer" [S12] (as-of 2026-08-24).
- TRAE CLI tagline (docs.trae.cn): your dedicated Code Agent, so you can "focus on higher-value creative work" (paraphrase from 专属 Code Agent framing) [S4].
- TRAE CLI claims (paraphrased): ready to use with minimal configuration; automates coding, testing (lint/unit tests), and Git workflows; extensible via MCP; multiple built-in LLMs plus OpenAI/Claude models; defaults to Max mode [S4].
- SOLO claims: "context engineer" positioning — AI at the start of the project, covering PRD → front/back-end development → deployment end-to-end (launch coverage, 2025-07-21) [S21]; press release: unified environment with complementary IDE Mode and SOLO Mode, SOLO "a breakthrough in end-to-end automation" [S14].
- trae-agent README claims (verbatim-short): "transparent, modular architecture", "research-friendly design" for "studying AI agent architectures, conducting ablation studies"; features Lakeview summaries, multi-LLM support, trajectory recording [S1].
- Audience: TRAE CLI — enterprise flagship-tier developers [S4][S3]; TRAE IDE/SOLO — professional developers and, for SOLO, non-developers turning natural language into software [S14][S33]; trae-agent — researchers and the academic/open-source community [S1].

## 5. Company & contact targets (company-level only)

- ByteDance Ltd. — privately held; founded 2012; HQ Beijing (international corporate structure via Cayman/Singapore entities); TRAE's international launch PR is issued from Singapore [S14]; JetBrains vendor record: "MarsCode", 77 Robinson Road, Singapore [S15].
- TRAE sits in the Volcano Engine (火山引擎) orbit of ByteDance's developer/cloud products; Volcano Engine president **Tan Dai (谭待)** publicly represents the Agent product line (Trae, Coze, HiAgent) in press interviews (2026) [S35]. The 1M-MAU milestone was announced via Volcano Engine [S26].
- No TRAE-specific product leads are named on trae.ai/trae.cn or in the launch PR (researched, absent; PR contact is "TRAE Team", feedback@mail.trae.ai) [S14]. A Trae representative named in press: Zhen Qi (responding to The Register on telemetry, 2025-07-28) [S18]. trae-agent paper corresponding group: "Trae Research Team" (first-listed author Pengfei Gao) [S10].
- Enterprise contact: BytePlus ("Contact us via BytePlus"), ussupport@mail.traeai.us (from trae.ai pricing/FAQ page) [S31-FAQ].

## 6. Open questions / conflicts (incl. existing census-entry errors)

- **Census mis-mapping (the big one):** roster maps paseo_id `traecli` → `trae-agent`, but Paseo's catalog command `traecli acp serve` belongs to the commercial TraeCode CLI; trae-agent has no ACP. Two entries needed (see section 0) [S11][S1][S5-ACP].
- Census `stars: null` → 12,046 (2026-08-21) [S2].
- Census `current_release: "2026-02-05"` — that is the **last commit date**; the repo has zero releases/tags. Field misleading as a "release" [S2].
- Census `maintained: "active"` → stale: 0 commits in last 90 days; 3 commits since 2025-09-08 [S2].
- Census `first_released: "2025-06-13"` = repo creation; fine (initial commit 2025-06-14).
- Census `homepage: "https://www.trae.ai/"` — that is the GitHub repo's homepage field, but it points at the commercial product, reinforcing the conflation; trae.ai does not document trae-agent [S2][S12].
- Census `platforms: ["CLI","Autonomous"]` — "Autonomous" overstates; it is a CLI agent with optional Docker sandbox runs [S1].
- Census nulls fillable: plugin_support → False (OSS), subagents → False (user-facing), hooks → False, plan_mode → False, docs_url → repo `docs/` (roadmap.md, tools.md, TRAJECTORY_RECORDING.md) [S1][S34].
- Census `what_makes_it_special` (research-friendly, Lakeview, trajectories, Docker) is accurate for the OSS repo [S1].
- China/international split: CLI is documented only on docs.trae.cn and gated to China Enterprise Edition flagship tier; international docs.trae.ai has IDE/SOLO(TraeWork)/Plugin but no CLI section found [S3][S17]. Unverified whether any international enterprise offering includes the CLI.
- Naming flux: "TRAE" → China docs now say "TraeCode"/"TraeWork"; international site uses TraeCode/TraeWork too, while most press still says "Trae". No formal rebrand announcement located [S12][S13][S4].
- "12M users" (June 2026) appears only in a third-party Chinese blog without attribution; last maker-sourced figures are 6M registered / 1.6M MAU (Dec 2025) [S27][S24].
- The X (Trae_ai) Pro-plan post and the five-tier token pricing come from X + a third-party comparison; the official pricing/billing pages (trae.ai/pricing, docs.trae.ai/ide/new-plans-and-billing) could not be read (client-rendered SPA; WebFetch returned truncated/empty content) — pricing details should be re-verified [S30][S31].
- Unreachable/failed sources: docs.trae.ai page bodies (ide/agent, ide/skills, ide/model-context-protocol, ide/rules-for-ai, ide/new-plans-and-billing, ide/solo-mode — SPA, no SSR text); trae.cn homepage (HTTP 403); docs.trae.cn sitemap and cli_hooks/cli_release-notes/etc. (400/404); trae.ai/terms-of-service (body not served); Discord member count (widget disabled); PyPI (trae-agent not published); GitHub unauthenticated API (rate-limited; gh CLI used instead).
- TRAE CLI model lineup ("built-in models + OpenAI/Claude") is vague in docs; whether BYO keys exist for the CLI is unverified [S4].

## 7. Sources

1. [S1] https://raw.githubusercontent.com/bytedance/trae-agent/main/README.md — OSS features, install, config, MIT, Discord badge, citation
2. [S2] GitHub API repos/bytedance/trae-agent (+ releases, tags, commits, contributors, search) — stars 12,046, created 2025-06-13, last commit 2026-02-05, 0 releases, 52 contributors
3. [S3] https://docs.trae.cn/cli_get-started-with-trae-cli — install, OS support, enterprise login, update; and https://forum.trae.cn/t/topic/684 — staff "no plans" for individual users (2026-03-10)
4. [S4] https://docs.trae.cn/cli_what-is-trae-cli — TraeCode CLI definition, enterprise flagship-tier only, features, Max-mode default
5. [S5] https://docs.trae.cn/cli_agent — custom agents; [S5-ACP] https://docs.trae.cn/cli_acp — `traecli acp serve`, Zed config
6. [S6] https://docs.trae.cn/cli_model-context-protocol — MCP client, transports, trae_cli.yaml, .trae/mcp.json compat
7. [S7] https://docs.trae.cn/cli_skills — SKILL.md format, .traecli/skills, legacy dirs
8. [S8] https://docs.trae.cn/cli_permission-mode — default/plan/bypass_permissions modes
9. [S9] https://docs.trae.cn/cli_slash-commands and https://docs.trae.cn/cli_use-cases — slash commands, custom commands, headless -p/--json, --allowed-tool, --worktree, YOLO, "TraeCode CLI 1.0", AGENTS.md via /init
10. [S10] https://arxiv.org/abs/2507.23370 — Trae Agent paper, 75.20% SWE-bench Verified, authors
11. [S11] getpaseo/paseo repo (acp-provider-catalog.ts, trae-acp-agent.ts via raw.githubusercontent) — command ["traecli","acp","serve"], install link to docs.trae.cn
12. [S12] https://www.trae.ai/ — "Collaborate with Intelligence", TraeWork + TraeCode product split
13. [S13] https://docs.trae.ai/ landing title "Important Updates: TraeWork is available"; https://docs.trae.ai/solo/what-is-trae-solo page title "What is TraeWork? - TRAE SOLO"
14. [S14] Reuters-carried press release 2025-09-23 "TRAE Unleashes the Next Era of AI Coding" (via tradingview mirror) — TRAE (Singapore), IDE Mode + SOLO Mode global launch
15. [S15] https://plugins.jetbrains.com/api/plugins/24326 — TRAE AI plugin, 3,645,423 downloads, vendor MarsCode (Singapore), v1.7.0.4
16. [S16] https://www.infoq.com/news/2025/03/trae-bytedance-claude-37-free/ — free Claude 3.7/DeepSeek R1, VS Code fork, China-version models
17. [S17] WebSearch site:docs.trae.ai for CLI/traecli — no CLI docs section internationally
18. [S18] https://www.theregister.com/2025/07/28/bytedance_trae_telemetry/ — telemetry findings, Unit 221B, ByteDance response, Code OSS fork, Zhen Qi
19. [S19] https://visualstudiomagazine.com/articles/2025/01/27/ai-powered-trae-ide-ships.aspx (via search) — Jan 2025 ship, fork observation
20. [S20] https://baike.baidu.com/en/item/Trae/1481007 (via search) — released 2025-01-19; thamizhelango.medium.com — "The Real AI Engineer" backronym (third-party)
21. [S21] https://news.aibase.com/news/19848 + traesolo blog (via search) — SOLO mode launch 2025-07-21, "context engineer" positioning
22. [S22] https://news.aibase.com/news/23822 — TRAE CN Enterprise Edition, 2025-12-18, 100k files/150M LOC, encryption, zero-storage
23. [S23] https://docs.trae.cn/cli_release-notes (404) and probes of cli_hooks/cli_rules/cli_plugins etc. (400) — pages absent
24. [S24] https://news.aibase.com/news/24099 — Trae "2025 Product Report": 6M registered, 1.6M MAU, ~200 countries, ~100B lines, 60M sessions, 500M queries, +700% tokens, Builder 80%/SOLO 40%, 11,000+ MCP
25. [S25] https://www.geekpark.net/news/358722 (+ qq mirror) — same report; 92% ByteDance engineers, Douyin 43% AI code, 365k custom agents, latency/crash metrics, SOLO 30% CN / 44% intl
26. [S26] https://www.aibase.com/news/18830 — MAU >1M (2025-06-11/12, via Volcano Engine)
27. [S27] https://www.aitoollab.cn/articles/trae-2-0-solo-agent-deep-review-202606/ — "12M users" claim, no primary source
28. [S28] VS Code Marketplace extensionquery API, search "Trae" — no official coding-agent extension; third-party themes only
29. [S29] https://img.shields.io/discord/1320998163615846420.json — "widget disabled"
30. [S30] https://x.com/Trae_ai/status/1927334494748524900 (via search) — Pro plan, 600 fast requests, zero rate limits (2025-05-27)
31. [S31] https://aiidelist.com/blog/trae-ai-ide-pricing-2026 — Free/Lite $3/Pro $10/Pro+ $30/Ultra $100 token-credit tiers (2026-06-26); [S31-FAQ] https://www.trae.ai/pricing FAQ page — BytePlus contact, ussupport@mail.traeai.us
32. [S32] https://docs.trae.ai/ide/agent, /custom-agents-ready-for-one-click-import, /use-mcp-servers-in-agents (titles + search snippets; bodies unrenderable)
33. [S33] https://docs.trae.ai/ide/skills (search snippet: .agents/skills convention, .trae/skills precedence; skills launched in SOLO first) and https://www.trae.ai/blog/trae_tutorial_0115 (unfetched)
34. [S34] https://raw.githubusercontent.com/bytedance/trae-agent/main/docs/roadmap.md — SDK/headless, sandbox, MLOps trajectory plans, MCP expansion
35. [S35] Chinese press interviews with Volcano Engine president Tan Dai (jiemian.com/article/14631587.html; news.qq.com 2026-06-23) — Trae in Volcano Engine agent portfolio; positioning as China's Cursor-like integrated coding agent

## Inclusion check (Jesse's test)

- **trae-agent (OSS): yes** — its own LLM agentic loop (max_steps-bounded tool loop with bash + file-edit tools) that creates and modifies software [S1].
- **TRAE CLI (product): yes** — its own closed-source agentic loop (permission-gated tool calls, subagent delegation, MCP tools) that writes/modifies code; it is a real agent exposing ACP, not a thin ACP wrapper around someone else's agent [S4][S5][S8].
