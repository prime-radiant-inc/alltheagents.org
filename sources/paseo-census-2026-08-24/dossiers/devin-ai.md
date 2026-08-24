# Dossier: Devin (census_slug: devin-ai)

Compiled 2026-08-21. Facts only. Null convention: "null = not researched"; "False/none = researched and absent". Each non-obvious fact carries a source [Sn] (see section 7) and an as-of date. Devin is a product family; each fact states the surface it applies to: **cloud** (Devin / Devin Cloud, the autonomous VM agent), **CLI** (Devin CLI, a.k.a. "Devin for Terminal"; Paseo drives it via `devin acp`), **Desktop** (Devin Desktop, the rebranded Windsurf IDE, whose local agent "Devin Local" shares the CLI harness), **Windsurf** (pre-June-2026 IDE/plugins), **company** (Cognition).

## 1. Identity

- name: Devin (product family). Surfaces named by the maker on 2026-06-02: Devin Desktop, Devin Cloud, Devin CLI, Devin Review [S14]. Roster row is "Devin CLI" (cli.devin.ai/docs); census slug devin-ai.
- maker: Cognition AI, Inc. (company; earlier styled "Cognition Labs"; terms of service name "Cognition AI, Inc."; legacy Windsurf contracts may be with Exafunction, Inc.) — HQ San Francisco, CA, USA; offices London (opened 2026-01-28) and Singapore APAC HQ (2026-04-30) [S25][S26][S27][S28] (as-of 2026-08-21)
- product URL: https://devin.ai (web app https://app.devin.ai); CLI docs https://docs.devin.ai/cli (https://cli.devin.ai/docs 301-redirects there) [S1][S2]; docs home https://docs.devin.ai [S3]
- repo URL: https://github.com/CognitionAI/devin-cli — release/issue-tracking repo only (contents: README.md pointing to docs, `.github/`, `scripts/`); 1 star, 0 forks, 11 GitHub releases, created 2026-06-10, license field null [S4] (as-of 2026-08-21)
- license: proprietary (ACP registry entry for Devin lists `"license": "proprietary"`) [S5]; no license in repo [S4]. open source? **False**. source_available: **False** for the agent (CLI ships as binaries from static.devin.ai; cloud agent is hosted). Adjacent open repos under github.com/CognitionAI: blockdiff (257 stars), devin-swebench-results (124), deepwiki (87), metabase-mcp-server (57), devin-outpost-k8s, terraform-provider-devin, plugin-template, team-marketplace-template [S4] (as-of 2026-08-21). Third-party "Devin Handoff" plugin (club-cog/devin-handoff) is described by the docs as open-source [S6].
- first public release:
  - cloud: announced 2024-03-12 (early access / waitlist; "first AI software engineer"; byline Scott Wu) [S7]; general availability 2024-12-10 ($500/mo team plan, unlimited seats) [S8][S9]
  - CLI: earliest entry in the stable changelog is v2026.3.9-0 dated 2026-03-09 [S10]; launch blog "Devin CLI: Start Local, Hand Off to the Cloud" dated 2026-04-27 [S11]; company X post describing "Devin for Terminal" 2026-04-29 [S12]
  - Desktop: Windsurf rebranded to Devin Desktop 2026-06-02 (over-the-air update; Cascade agent retired 2026-07-01 in favour of Devin Local) [S14]
- latest release: CLI v3000.4.25 (changelog 2026-08-13; GitHub release published 2026-08-14; Homebrew cask version 3000.4.25) [S10][S4][S13]; Devin Desktop v3.7.25 (2026-08-13) [S15]; cloud release notes most recent entry 2026-08-21 [S16] (as-of 2026-08-21)
- what it is:
  - Form factors: **cloud** background-autonomous agent in its own VM (shell, IDE, browser, and since Devin 2.2 a Linux desktop) driven from web app, Slack, Microsoft Teams, Linear/Jira, GitHub, REST API, Automations (event/schedule/webhook triggers); **CLI** terminal agent for macOS/Linux/WSL/Windows with `/handoff` to cloud; **Desktop** IDE (VS Code-compatible fork of Windsurf) with Devin Local agent and an "Agent Command Center" that also hosts third-party ACP agents; ACP integrations for JetBrains, Zed, Xcode; Windsurf plugins for JetBrains/VS Code/Visual Studio/Vim/Neovim/Jupyter/Eclipse; Devin Review (devinreview.com); DeepWiki; Devin Outposts (self-hosted workers); VPC deployment for enterprise [S3][S17][S18][S14][S19][S20] (as-of 2026-08-21)
  - Models: multi-vendor — docs say CLI supports latest models from Anthropic, OpenAI, Google and Cognition (SWE-1.x family, e.g. SWE-1.6, SWE-1.7) plus open-source DeepSeek, Kimi, GLM; "Adaptive" router is the default recommendation; short names `opus`, `sonnet`, `swe`, `codex`, `gemini`; Devin Fusion hybrid-model system (cloud, 2026-06-29) [S21][S22][S23]. BYO API keys: none found in CLI docs (usage billed through plan quota/credits) — researched, not found.
  - Pricing (all surfaces share quota): Free $0; Pro $20/mo; Max $200/mo; Teams $80/mo minimum + $40/mo per full seat (flex seats free, unlimited members); Enterprise billed in Agent Compute Units (ACUs) per order form, contact sales; usage beyond quota at "API pricing" via on-demand credits [S24][S25b] (as-of 2026-08-21). History: $500/mo team plan at GA 2024-12-10 [S8]; Core plan $20 pay-as-you-go 2025-04-03 [S29]; legacy Core users migrated to Free [S24].
  - Install (CLI): `curl -fsSL https://cli.devin.ai/install.sh | bash` (macOS/Linux/WSL); `brew install --cask devin-cli`; Windows installers or `irm https://static.devin.ai/cli/setup.ps1 | iex`; bundled with Devin Desktop on enterprise plans [S2]. Cloud: sign up at app.devin.ai [S3]. Desktop: download from devin.ai [S14].
  - Default autonomy (CLI): default "Normal" mode — read-only tools auto-run; file edits, shell and fetches prompt; other modes Accept Edits, Smart (fast-model judge), Bypass, Autonomous (only with `--sandbox`, OS-level isolation via bubblewrap/Seatbelt, fail-closed); agent modes Normal / Plan / Ask; org-level deny/ask rules override user modes [S30][S31]. Cloud: runs autonomously in its own VM; admins constrain via Security Profiles (network, MCP, git, gh access) [S32].
  - Implementation language: maker says the CLI uses a "custom terminal rendering library in Rust" and Devin Local was "rewritten from scratch in Rust" [S11][S14]; GitHub reports the release repo's language as Python (scripts only) [S4].

## 2. Adoption evidence

| metric / claim | value | as-of | source | type |
|---|---|---|---|---|
| Homebrew cask installs, devin-cli (30d / 90d / 365d) | 980 / 2,348 / 2,348 (rank #327 of 12,349 casks in 30d; 0.04%) | 2026-08-21 | [S13] | independently observable |
| Homebrew cask installs, devin-desktop (30d / 90d / 365d) | 490 / 1,723 / 1,723; devin-desktop@next 41 / 123 / 123 | 2026-08-21 | [S13] | independently observable |
| Homebrew cask installs, windsurf (30d / 90d / 365d) | 33 / 565 / 10,453 | 2026-08-21 | [S13] | independently observable |
| GitHub CognitionAI/devin-cli | 1 star, 0 forks, 1 open issue, 11 releases (3000.4.25 on 2026-08-14), created 2026-06-10 | 2026-08-21 | [S4] | independently observable (repo is release-only) |
| GitHub org repos (stars) | blockdiff 257; devin-swebench-results 124; deepwiki 87; metabase-mcp-server 57; qa-devin 40 | 2026-08-21 | [S4] | independently observable |
| npm / PyPI | no official package. npm `devin-cli` is a 0.0.1 placeholder (2025-06-02); PyPI `devin-cli` is an "Unofficial CLI" by a third party (2,846 downloads/30d) | 2026-08-21 | [S33] | independently observable (not maker's) |
| VS Code Marketplace, cognition.devin "Devin [Beta]" | 7,007 installs; released 2024-11-19, last updated 2025-04-21 | 2026-08-21 | [S34] | independently observable |
| VS Code Marketplace, Codeium "Windsurf Plugin" | 3,977,221 installs; 1,472 ratings avg 4.73; codeium-enterprise-updater 250,921 installs | 2026-08-21 | [S34] | independently observable |
| JetBrains Marketplace, Windsurf Plugin (id 20540) | 9,974,029 downloads; "Windsurf (Remote Development)" 490,713 | 2026-08-21 | [S35] | independently observable |
| ACP registry | Devin listed (1 of 39 agents), version 3000.4.25, binary distribution from static.devin.ai, launched as `devin acp` | 2026-08-21 | [S5] | independently observable |
| Annualized run-rate revenue (company) | $492M | 2026-05-27 | [S36][S37] | maker-claimed (confirmed to TechCrunch by CEO) |
| ARR history | $1M (Sept 2024) -> $73M (June 2025) [S38]; $37M (May 2025) per TechCrunch [S37] | 2025-09-08 / 2026-05-27 | [S38][S37] | maker-claimed / press |
| Windsurf at acquisition | $82M ARR, 350+ enterprise customers, "hundreds of thousands" DAU; enterprise ARR doubling QoQ; acquisition "more than doubled our ARR" | 2025-07-14 / 2025-09-08 | [S39][S38] | maker-claimed |
| Growth | enterprise usage ">10x since the start of this year"; "50% month-over-month for six months" (to TechCrunch) | 2026-05-27 | [S36][S37] | maker-claimed |
| Internal dogfooding | 89% of code committed at Cognition is committed by Devin | 2026-05-27 | [S36] | maker-claimed |
| PRs / outcomes | "hundreds of thousands of PRs merged"; 67% PR merge rate (vs 34% prior year); "thousands of companies"; DeepWiki over 400,000 repos | 2025-11-14 | [S40] | maker-claimed |
| Users | "Millions of engineers use Windsurf and Devin" | 2026-06-02 | [S14] | maker-claimed |
| Customer metrics (site) | EBANX 92% of merged PRs; Gumroad 1,500+ merged PRs (#1 contributor); Hamming 25% of code volume; Mercedes-Benz COBOL migration 8 months -> 8 days; FE fundinfo 1,800 repos; Itaú fixes 70% of security vulns automatically; Litera regression cycles -90% | 2026-08-21 | [S41][S36] | maker-claimed |
| Public customers / logos | Series D post: Citi, Mercedes-Benz, Goldman Sachs, Elevance, Dell, Santander, U.S. Army, U.S. Navy, Infosys, Cognizant, Itaú; startups Exa, Modal, Eight Sleep, OpenRouter [S36]. Sept 2025: Goldman Sachs, Citi, Dell, Cisco, Ramp, Palantir, Nubank, Mercado Libre [S38]. devin.ai/customers: Compiled Health, EBANX, GE Aerospace, Hippo, AHEAD, AngelList, Evinova, Mercedes-Benz, RV Tech, Cognizant, FE fundinfo, Infosys, Itaú, The Citation Group, Litera, Hamming, Bilt, Gumroad, Linktree, Crossmint, Ramp, Nubank [S41]. Devin Desktop launch quotes: Ramp, Harvey, NVIDIA, Modal, Intact Financial [S14]. cognition.com logos: Mercedes-Benz, Goldman Sachs, RV Tech, Infosys, Anduril, Itaú, Cognizant, Nubank [S42]. Partnerships: Infosys (2026-01-07), Cognizant (2026-01-28), Mercedes-Benz (2026-04-27), OCBC (Singapore post), LTM (260+ clients, 2026-07-28), U.S. DOE Genesis Mission MOU (2026-07-22); NASA named by TechCrunch | 2026-08-21 | [S36][S38][S41][S14][S42][S43][S28][S37] | maker-claimed (press for NASA) |
| Funding / valuation | Series A $21M at $350M (Mar 2024, Founders Fund); $175M at ~$2B (Apr 2024); round led by 8VC at ~$4B (Mar 2025); >$400M at $10.2B post (2025-09-08, Founders Fund); Series D >$1B at $26B post / $25B pre (2026-05-27; Lux, General Catalyst, 8VC co-leads; Founders Fund, Ribbit, Atreides, Layer Global et al.); reported talks at $40B+ (Bloomberg via TechCrunch, 2026-08-12) | 2026-08-21 | [S7][S26][S38][S36][S37][S44] | maker-claimed (rounds) / press |
| Acquisition | Cognition acquired Windsurf (IP, product, trademark, brand, business, employees) — definitive agreement 2025-07-14; price undisclosed; after Google hired Windsurf's founders | 2025-07-14 | [S39][S45] | maker-claimed / press |
| Benchmark: SWE-bench (launch) | 13.86% resolved end-to-end on a 25% random subset, vs 1.96% prior SOTA (maker-run) | 2024-03-12 | [S7] | maker-claimed |
| Benchmark: SWE-1.7 model (not the harness) | Terminal-Bench 2.1 81.5%; SWE-Bench Multilingual 77.8%; FrontierCode 1.1 Main 42.3%; served at ~1000 tok/s via Cerebras | 2026-07-08 | [S23] | maker-claimed |
| Benchmark: tbench.ai Terminal-Bench 2.1 agent leaderboard | no rows for Devin / SWE-1 / Cognition / Windsurf | 2026-08-21 | [S46] | independently observable (absent) |
| Community: Discord / Reddit / GitHub Discussions | none found on official materials (support routed to support@cognition.ai and in-app); member counts null | 2026-08-21 | [S3] | null (not obtainable) |
| Employees | 200 (Wikipedia, 2026); 286 (Contrary, 2026-02-26); 305-471 (third-party trackers, Mar-Jun 2026) | 2026-08-21 | [S26][S25][S47] | third-party estimates |
| Press | CNBC on Windsurf deal and $10.2B round (2025); TechCrunch/Bloomberg on Series D and $40B talks (2026); Fortune on Japan usage (2026-07-03) | 2026-08-21 | [S45][S37][S44][S48] | press |

## 3. Plugin interface (PRI-2925)

- mcp_support: **both**. Client: CLI connects to MCP servers over stdio, HTTP and SSE (`.devin/` config, `devin mcp login` with OAuth discovery), and cloud Devin has an MCP marketplace (Settings > Connections) plus custom servers over stdio/SSE/HTTP with org/personal access scopes [S49][S50]. Server: Cognition hosts the authenticated Devin MCP server at https://mcp.devin.ai/ (sessions, playbooks, knowledge, scheduling, repo search) and the DeepWiki MCP server [S51][S52]. (as-of 2026-08-21) Evidence: https://docs.devin.ai/cli/extensibility/mcp/overview ; https://docs.devin.ai/work-with-devin/devin-mcp
- plugin_support: **True** — own system: rules/AGENTS.md, skills (`SKILL.md`, `/skill` invocation, can run as subagents), custom subagents, MCP servers, hooks, and **plugins** (closed beta, request via support) = bundles with `.devin-plugin/plugin.json`, `AGENTS.md`, `rules/`, `agents/`, `hooks.json`, `.mcp.json`, `skills/`; installed from GitHub `owner/repo`, git URL, `git-subdir`, or local path (`devin plugins install`); managed org/enterprise marketplace in the web app (Settings > Resources > Plugins) with `requiredPlugins` / `optionalPlugins` / `forbiddenPlugins` manifests, an official catalog, and zip upload; plugins work across cloud sessions, CLI and Desktop with surface-specific limits [S53][S54][S55][S56] (as-of 2026-08-21). Evidence: https://docs.devin.ai/cli/extensibility/plugins/overview
- claude_code_plugin: **yes (partial)** — Devin loads Claude-format plugins directly: falls back to `.claude-plugin/plugin.json` when no `.devin-plugin/plugin.json`, honours root `.mcp.json` and manifest `mcpServers`, expands `${CLAUDE_PLUGIN_ROOT}`; also loads Agent Plugins 1.0.0-spec plugins [S53]. Config import reads `CLAUDE.md`, `~/.claude/CLAUDE.md`, `.claude/skills/**/SKILL.md`, `.claude/commands/**/*.md` (as skills), and MCP servers from `.mcp.json` / `.claude/settings*.json` / `~/.claude.json` [S57]. Claude Code `marketplace.json` marketplaces are not mentioned (researched, absent) [S53][S56].
- subagents: **True** — CLI/Desktop: parent spawns `subagent_explore` (default cheap model, SWE-1.6) or `subagent_general` (parent's model) or custom profiles (`agents/<name>.md` / `agents/<name>/AGENT.md`, with model/tools/prompt), foreground or background, nestable; admins set default subagent model or disable [S58][S59]. Cloud: Devin can orchestrate managed sessions in parallel ("team of Devins"), Security Swarm multi-agent [S60][S41][S61]. Evidence: https://docs.devin.ai/cli/subagents
- hooks: **True** — events PreToolUse, PostToolUse, PermissionRequest, UserPromptSubmit, Stop, PostCompaction, SessionStart, SessionEnd; `command` (shell, JSON stdin, can block/inject context) and `prompt` (LLM) hook types; regex matcher on tool_name; `.devin/hooks.v1.json`; plugin `hooks.json`; cloud sessions run command hooks except SessionStart/End; `devin migrate hooks` converts Windsurf hooks; Desktop legacy Cascade hooks [S62][S63][S53] (as-of 2026-08-21). Evidence: https://docs.devin.ai/cli/extensibility/hooks/overview
- plan_mode: **True** — CLI `/plan` switches to Plan agent mode with read-only tools (grep, glob, read, todo, ask_user_question, exit_plan_mode); `/ask` for Q&A; Plan remains available in sandbox sessions; Devin Local in Desktop has plan mode; cloud Devin has Interactive Planning (Devin 2.0) [S31][S64][S65][S29]. Evidence: https://docs.devin.ai/cli/reference/commands
- plugin_docs_url: https://docs.devin.ai/cli/extensibility/plugins/overview (cloud admin side: https://docs.devin.ai/product-guides/plugins ; skills: https://docs.devin.ai/cli/extensibility/skills/overview)
- config_docs_url: https://docs.devin.ai/cli/reference/configuration/config-file (overview https://docs.devin.ai/cli/extensibility/configuration ; permissions https://docs.devin.ai/cli/reference/permissions)
- ACP support: **yes, first-party** — `devin acp` runs Devin CLI as an ACP server over stdio (JSON-RPC), advertises slash commands to hosts, `--model` flag; documented for Zed (ACP registry install), JetBrains AI Chat, Xcode; Devin Desktop is also an ACP **host** (runs Codex, Claude Agent, OpenCode, Junie, Gemini CLI, custom agents) [S66][S67][S68][S19][S14]; registry entry launches `./bin/devin acp` [S5] (as-of 2026-08-21).
- SDK: no language SDK found. Programmatic surfaces: REST API v3 (`https://api.devin.ai/v3/organizations/*`, `/v3/enterprise/*`, service users with RBAC) [S69]; Devin MCP server [S51]; CLI non-interactive `devin -p/--print`, `--export`, `--format json` [S64]; Terraform provider and Outposts/fleet API [S4][S70]; Devin Desktop has an ACP custom-agent guide [S71].

## 4. Claimed differentiation (raw material for PRI-2927)

- tagline (devin.ai hero): "Devin, the AI software engineer" — https://devin.ai [S1]
- tagline (docs intro): "the AI software engineer, built to help ambitious engineering teams crush their backlogs" — https://docs.devin.ai/get-started/devin-intro [S17]
- tagline (company): "Cognition operates Devin, the first autonomous software engineer" — https://cognition.com [S42]
- tagline (CLI docs): "a local command-line coding agent with deep Devin Cloud integration" — https://docs.devin.ai/cli [S2]
- tagline (CLI launch): "Start Local, Hand Off to the Cloud" — https://cognition.com/blog/devin-for-terminal [S11]; X: "the first CLI agent with its own dedicated virtual machine" [S12]
- maker claims (paraphrased):
  1. Autonomy rule of thumb: if a human can do it in three hours, Devin can most likely do it; handles tickets, features, bug repro/fix, migrations end-to-end in its own VM with shell, IDE, browser and (2.2) Linux desktop for end-to-end testing; self-reviews via Devin Review Autofix [S17][S61].
  2. Parallelism/fleet: spin up many Devins / "a fleet of agents" for multi-repo migrations, scheduled chores, incident triage; gets better by reading past session trajectories [S1][S29].
  3. Start local, hand off to cloud: CLI (and Claude Code/Codex/Cursor via the open-source Devin Handoff plugin) can hand a session, branch and uncommitted diff to a cloud Devin with its own computer that keeps working after the laptop closes [S11][S6][S72].
  4. Any frontier model plus own models: Anthropic/OpenAI/Google, Cognition's SWE-1.x (SWE-1.7 "frontier-level intelligence at a much lower cost", ~1000 tok/s), open-source models; Adaptive router; Devin Fusion "35% lower cost" [S21][S23][S22]; pricing page: "First class support for every major model provider" [S24].
  5. Works where the team works: Slack/Teams tagging, Linear/Jira tickets, GitHub PR loop with CI/review feedback, API and Automations; "hundreds of tools" via MCP [S1][S50].
  6. Learns the codebase/org: Knowledge, Playbooks, DeepWiki auto-docs, Ask Devin; "Learns your codebase & picks up tribal knowledge" [S1][S3].
  7. One Devin, every surface: same agent/context across Desktop (IDE with Agent Command Center and Kanban, Spaces), Cloud, CLI, Review; Desktop is an open ACP host for third-party agents [S14].
  8. Performance/safety engineering: CLI with custom Rust terminal rendering; OS-level sandbox that fails closed; Smart mode; enterprise controls (team settings, MDM system.json, security profiles, SSO/RBAC, VPC); subagents "improve overall coding performance and reduce cost"; Devin Local "up to 30% more token efficient" than Cascade [S11][S30][S31][S58][S14].
  9. Evidence offered: $492M run-rate, 89% internal code by Devin, customer outcomes (Mercedes 8 months -> 8 days; Itaú 70% of vulns), hundreds of thousands of merged PRs, 67% merge rate [S36][S40][S41].
- audience: "engineering teams with complex, multi-repo projects" (homepage) [S1]; "ambitious engineering teams" (docs) [S17]; enterprise (Citi, Goldman, Mercedes, government: "Cognition for Government") [S36][S42]; individual developers via Free/Pro/Max; CLI positioned for "quick fixes, code exploration, and interactive coding" with handoff for longer tasks [S17][S24].

## 5. Company & contact targets (PRI-2929) — company-level only

- legal name: Cognition AI, Inc. (terms of service, privacy policy; acceptable-use policy covers "Devin and Windsurf"); Windsurf legacy licences may be held by Exafunction, Inc. [S25] (as-of 2026-08-21)
- HQ: San Francisco, CA [S26]; London office (2026-01-28) [S27]; Singapore APAC HQ (2026-04-30) [S28]
- size: estimates range 200 (Wikipedia 2026) / 286 (Contrary 2026-02-26) / 305-471 (trackers Mar-Jun 2026) [S26][S25][S47]
- funding stage: late private; Series D >$1B at $26B post (2026-05-27); press reports talks at $40B+ (2026-08-12) [S36][S44]
- publicly named leadership (only where the company itself names them):
  - Scott Wu — CEO and co-founder (bylines on cognition.com posts: Introducing Devin 2024-03-12, Windsurf acquisition 2025-07-14, funding post 2025-09-08; CEO per TechCrunch) [S7][S39][S38][S37]
  - Russell Kaplan — President (Cognition X account announcement 2024-08-05; Fortune 2026-07-03) [S73][S48]
  - Richard Spence — Vice President and General Manager, APAC (cognition.com/blog/singapore, 2026-04-30) [S28]
  - Steven Hao — CTO and co-founder; Walden Yan — CPO and co-founder (titles per Wikipedia / Contrary Research / Forbes; not found on a cognition.com page during this research) [S26][S25][S47]
  - swyx (Shawn Wang), Christian Lawless, Emily Cohen — named as joining full-time in the 2025-09-08 funding post (roles at Cognition not stated) [S38]
  - SWE-1.7 research bylines (2026-07-08): Ben Pan, Carlo Baronio, Rohan Choudhury, Eric Lu, Ryan Kim, Deniz Birlikci, TC Qin, Sam Lee, Fermi Ma, Allen Liu, Yang Liu, Sampriti Panda, Jacob Teo, Ray Wang, Gary Chang, Steven Cao, Silas Alberti [S23]
  - Head of product / DevRel lead / head of partnerships: none found named on cognition.com or devin.ai — researched, absent.
- contact: sales/partnerships via https://cognition.com/contact and devin.ai "Contact sales"; product support support@cognition.ai (listed in docs) [S42][S1][S53]

## 6. Open questions / conflicts

- Existing census `maker: null` — Cognition AI, Inc. [S25][S42].
- Existing census `license: null`, `source_available: False` — license is proprietary (ACP registry) [S5]; source_available False is correct.
- Existing census `platforms: ["Autonomous"]` — also CLI (macOS/Linux/Windows), Desktop IDE, and ACP inside JetBrains/Zed/Xcode [S2][S14][S66][S67][S68].
- Existing census `first_released: null` — cloud announced 2024-03-12, GA 2024-12-10; CLI first changelog entry 2026-03-09, launch post 2026-04-27 [S7][S8][S10][S11].
- Existing census `current_release: null` — CLI v3000.4.25 (2026-08-13/14); Desktop v3.7.25 (2026-08-13) [S10][S4][S15].
- Existing census `stars: null` — only a 1-star release repo exists; stars are not a meaningful signal [S4].
- Existing census `language: null` — maker says Rust for CLI/Devin Local; GitHub labels the release repo Python (scripts) [S11][S14][S4].
- Existing census `mcp_support: True` — more precisely "both" (client in CLI/cloud; Cognition hosts Devin and DeepWiki MCP servers) [S49][S51][S52].
- Existing census `claude_code_plugin: False` — looks wrong: Devin loads `.claude-plugin/plugin.json` plugins and imports CLAUDE.md, `.claude/skills`, `.claude/commands` and Claude MCP configs [S53][S57]. Suggest "partial/yes".
- Existing census `subagents: null`, `hooks: null`, `plan_mode: null` — all True with docs [S58][S62][S31].
- Existing census `pricing: "Individual and Teams plans"` — Free / Pro $20 / Max $200 / Teams $80 min + $40 per full seat / Enterprise ACUs [S24].
- Existing census `install_method: null`, `plugin_docs_url: null`, `config_docs_url: null` — filled above.
- Existing census `name: "Devin AI"` — maker uses "Devin"; roster row says "Devin CLI". Whether the census entry is the family or the CLI should be decided.
- Existing census `what_makes_it_special` says "features MCP and Plugin marketplaces" — plugins are in closed beta (managed marketplace exists for orgs) [S53][S56].
- CLI launch date conflict: stable changelog starts 2026-03-09; launch blog 2026-04-27; Terminal Trove (unreachable, 403) reportedly lists 2026-04-09 via search snippet [S10][S11][S74].
- ARR conflict: TechCrunch cites $37M (May 2025); Cognition's own post cites $73M (June 2025) and $1M (Sept 2024) — different months, both pre-Windsurf [S37][S38].
- Employee count varies 200-471 across sources [S26][S25][S47].
- Legal-name styling: "Cognition AI, Inc." (terms) vs "Cognition Labs" (Wikipedia alias, Contrary) [S25][S26].
- Unreachable: devin.ai pages returned HTTP 429 / Vercel security checkpoint to WebFetch and curl; homepage, pricing, customers and the Devin Desktop post were read through the Claude browser pane instead [S1][S24][S41][S14]. github.com/CognitionAI/devin-cli and terminaltrove.com returned 403 to WebFetch (GitHub data taken via `gh api`) [S4][S74]. Discord/Reddit sizes not found.
- Terminal-Bench/SWE-bench figures for SWE-1.7 are model scores published by the maker, not independent harness placements; tbench.ai shows no Devin rows [S23][S46].
- Leadership titles for Hao/Yan rest on third-party sources; not located on cognition.com during this pass.

## 7. Sources

1. [S1] https://devin.ai/ (read via browser pane) — hero tagline, use cases, audience, integrations
2. [S2] https://docs.devin.ai/cli (cli.devin.ai/docs redirects here; .md via docs.devin.ai/cli/index.md) — CLI quickstart, install, CLI vs cloud
3. [S3] https://docs.devin.ai/ and https://docs.devin.ai/llms.txt — docs index, surfaces, feature list
4. [S4] https://api.github.com/repos/CognitionAI/devin-cli (+ releases, contents, org search via `gh api`) — repo facts, org repos
5. [S5] https://cdn.agentclientprotocol.com/registry/v1/latest/registry.json — Devin ACP registry entry, license proprietary, `devin acp`
6. [S6] https://docs.devin.ai/cli/handoff — /handoff, open-source Devin Handoff plugin
7. [S7] https://cognition.com/blog/introducing-devin — 2024-03-12 launch, SWE-bench 13.86%, $21M Series A, Scott Wu byline
8. [S8] https://docs.devin.ai/release-notes/2024 — GA note, $500/mo, unlimited seats
9. [S9] https://cognition.com/blog/devin-generally-available — GA 2024-12-10 details
10. [S10] https://docs.devin.ai/cli/changelog/stable — CLI versions/dates (v2026.3.9-0 .. v3000.4.25)
11. [S11] https://cognition.com/blog/devin-for-terminal — CLI launch 2026-04-27, Rust rendering, models, handoff
12. [S12] https://x.com/cognition/status/2049602227610751180 (via search; date from snowflake ID) — "Devin for Terminal" claim, 2026-04-29
13. [S13] https://formulae.brew.sh/api/cask/devin-cli.json and /api/analytics/cask-install/{30d,90d,365d}.json — Homebrew installs
14. [S14] https://devin.ai/blog/windsurf-is-now-devin-desktop (read via browser pane) — rebrand 2026-06-02, ACP host, Devin Local, "millions of engineers", surfaces list
15. [S15] https://docs.devin.ai/desktop/changelog — Desktop v3.7.25 (2026-08-13)
16. [S16] https://docs.devin.ai/release-notes/overview — cloud release notes (latest 2026-08-21)
17. [S17] https://docs.devin.ai/get-started/devin-intro — docs tagline, 3-hour rule, strengths, workflows
18. [S18] https://docs.devin.ai/desktop/getting-started — Devin Desktop IDE
19. [S19] https://docs.devin.ai/desktop/acp — Desktop as ACP host, example agents
20. [S20] https://docs.devin.ai/cloud/outposts/quickstart (via llms.txt summary) — Outposts self-hosted workers
21. [S21] https://docs.devin.ai/cli/models — model vendors, Adaptive, short names
22. [S22] https://cognition.com/blog/devin-fusion (via blog index) — Devin Fusion 35% lower cost, 2026-06-29
23. [S23] https://cognition.com/blog/swe-1-7 — SWE-1.7 benchmarks, bylines, 2026-07-08
24. [S24] https://devin.ai/pricing (read via browser pane) — plan prices and features
25. [S25] https://cognition.ai/terms-of-service, https://cognition.ai/acceptable-use-policy (via search) — "Cognition AI, Inc.", Exafunction note; [S25b] https://docs.devin.ai/admin/billing/self-serve — plan mechanics, seats, credits, legacy Core migration
26. [S26] https://en.wikipedia.org/wiki/Cognition_AI — founders, HQ, funding history, employees
27. [S27] https://cognition.com/blog/cognition-london (via blog index) — London office 2026-01-28
28. [S28] https://cognition.com/blog/singapore — APAC HQ, Richard Spence title, OCBC
29. [S29] https://cognition.com/blog/devin-2 — Devin 2.0, Core $20, parallel Devins, Interactive Planning (2025-04-03)
30. [S30] https://docs.devin.ai/cli/reference/permissions — modes, defaults, Smart, Autonomous
31. [S31] https://docs.devin.ai/cli/essential-commands — 5 permission modes, 3 agent modes, /plan
32. [S32] https://docs.devin.ai/product-guides/security-profiles (via llms.txt summary) — cloud security profiles
33. [S33] https://registry.npmjs.org/devin-cli ; https://pypi.org/pypi/devin-cli/json ; https://pypistats.org/api/packages/devin-cli/recent — unofficial packages
34. [S34] https://marketplace.visualstudio.com/_apis/public/gallery/extensionquery — Devin [Beta] and Windsurf plugin installs
35. [S35] https://plugins.jetbrains.com/api/plugins/20540 ; /api/searchPlugins?search=devin — JetBrains downloads
36. [S36] https://cognition.com/blog/series-d — $1B at $26B, $492M ARR, customers, 89% internal, 2026-05-27
37. [S37] https://techcrunch.com/2026/05/27/ai-coding-startup-cognition-raises-1b-at-25b-pre-money-valuation/ — press on Series D, $37M May 2025, NASA, 50% MoM
38. [S38] https://cognition.com/blog/funding-growth-and-the-next-frontier-of-ai-coding-agents — $400M at $10.2B, ARR history, customers, hires (2025-09-08)
39. [S39] https://cognition.com/blog/windsurf — acquisition terms, $82M ARR, 350+ enterprises (2025-07-14)
40. [S40] https://cognition.com/blog/devin-annual-performance-review-2025 — PRs, merge rate, 400k repos (2025-11-14)
41. [S41] https://devin.ai/customers (read via browser pane) — customer list and metrics
42. [S42] https://cognition.com/ — company tagline, logos, products, contact link
43. [S43] https://cognition.com/blog (index) — post list/dates: LTM, DOE, Infosys, Cognizant, Mercedes, Security Swarm, Devin 2.2, SWE-1.5, Windows VM
44. [S44] https://techcrunch.com/2026/08/12/ai-coding-startup-cognition-reportedly-already-in-talks-to-raise-at-40b-valuation/ — $40B talks (Bloomberg)
45. [S45] https://www.cnbc.com/2025/07/14/cognition-to-buy-ai-startup-windsurf-days-after-google-poached-ceo.html (via search) — acquisition press
46. [S46] https://www.tbench.ai/leaderboard/terminal-bench/2.1 — no Devin rows
47. [S47] https://research.contrary.com/company/cognition ; web search results (Revelio, jobsbyculture, Forbes) — employees, exec titles
48. [S48] https://fortune.com/2026/07/03/devin-kun-cognition-ai-japan-russell-kaplan/ (via search) — Kaplan title, Japan usage
49. [S49] https://docs.devin.ai/cli/extensibility/mcp/overview — CLI MCP client
50. [S50] https://docs.devin.ai/work-with-devin/mcp — cloud MCP marketplace, transports
51. [S51] https://docs.devin.ai/work-with-devin/devin-mcp — Devin MCP server (mcp.devin.ai)
52. [S52] https://docs.devin.ai/work-with-devin/deepwiki-mcp (via llms.txt) — DeepWiki MCP server
53. [S53] https://docs.devin.ai/cli/extensibility/plugins/overview — plugin format, Claude/Agent-Plugins compatibility, closed beta
54. [S54] https://docs.devin.ai/cli/extensibility/skills/overview — skills
55. [S55] https://docs.devin.ai/cli/extensibility/index — extensibility overview, .devin/ layout
56. [S56] https://docs.devin.ai/product-guides/plugins — managed plugin marketplace/manifests
57. [S57] https://docs.devin.ai/cli/reference/configuration/read-config-from — import from Claude Code, Cursor, Windsurf, Copilot, OpenCode, Zed
58. [S58] https://docs.devin.ai/cli/subagents — subagent profiles, models, controls
59. [S59] https://docs.devin.ai/desktop/devin-local — Devin Local agent, subagents, sandbox, token efficiency
60. [S60] https://docs.devin.ai/work-with-devin/advanced-capabilities (via llms.txt) — parallel managed sessions
61. [S61] https://cognition.com/blog/introducing-devin-2-2 — computer use, Review Autofix (2026-02-24); Security Swarm post via [S43]
62. [S62] https://docs.devin.ai/cli/extensibility/hooks/overview — hook types
63. [S63] https://docs.devin.ai/cli/extensibility/hooks/lifecycle-hooks — hook events
64. [S64] https://docs.devin.ai/cli/reference/commands — `devin acp`, `-p`, modes, /plan, profiles
65. [S65] https://docs.devin.ai/cli/enterprise/controls — CLI vs Cascade parity, plan mode in Devin Local
66. [S66] https://docs.devin.ai/cli/acp/zed — Zed ACP setup
67. [S67] https://docs.devin.ai/cli/acp/jetbrains (via llms.txt) — JetBrains ACP
68. [S68] https://docs.devin.ai/cli/acp/xcode (via llms.txt) — Xcode ACP
69. [S69] https://docs.devin.ai/api-reference/overview — REST API v3
70. [S70] https://docs.devin.ai/cloud/outposts/reference (via llms.txt) — Outposts API/CLI
71. [S71] https://docs.devin.ai/desktop/acp-custom (via llms.txt) — custom ACP agent in Desktop
72. [S72] https://docs.devin.ai/work-with-devin/devin-handoff — handoff from other agents
73. [S73] https://x.com/cognition_labs/status/1820461604586283089 (via search; date from snowflake ID) — Russell Kaplan named President, 2024-08-05
74. [S74] https://terminaltrove.com/ai-coding-agents/devin-for-terminal/ — 403 to WebFetch; search snippet only
75. https://docs.devin.ai/cli/sandbox — sandbox mechanics, fail-closed, Windows unsupported
76. https://docs.devin.ai/admin/billing/enterprise — ACU billing
77. https://docs.devin.ai/desktop/accounts/usage — Desktop plans still reference windsurf.com
78. https://docs.devin.ai/work-with-devin/devin-cli — cloud-docs description of the CLI

## Inclusion check (Jesse's test)

**Yes** — both the cloud Devin (autonomous VM agent that writes, runs and tests code end-to-end) and Devin CLI (a first-party local agent loop with tools, permissions, subagents and hooks, exposed over ACP via `devin acp`) create and modify software with their own agentic loop; neither is a wrapper around another vendor's agent [S17][S64][S58].
