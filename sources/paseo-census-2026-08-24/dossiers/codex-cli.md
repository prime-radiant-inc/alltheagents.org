# Dossier: Codex CLI (OpenAI)

census_slug: codex-cli | paseo_id: codex | tier 1 | researched 2026-08-21

Scope note: "Codex" is OpenAI's umbrella name for a coding-agent product family. The dossier
anchor is **Codex CLI** (the open-source terminal agent in github.com/openai/codex). Where a fact
applies to another surface (IDE extension, Codex cloud, ChatGPT desktop app, ChatGPT web/mobile)
it is labelled. Null convention: "null = not researched", "none = researched and absent".

Access note: every openai.com page (launch posts, openai.com/codex, chatgpt.com/codex,
help.openai.com) returned HTTP 403 to this environment on 2026-08-21. Maker numbers from those
posts are therefore relayed through secondary sources and labelled as such (section 6).

## 1. Identity

- name: Codex CLI (product family: Codex)
- maker: OpenAI (company; San Francisco, CA, USA; OpenAI Group PBC — see section 5)
- product URL: https://developers.openai.com/codex (308-redirects to https://learn.chatgpt.com/docs as of 2026-08-21)
- repo URL: https://github.com/openai/codex (repo description: "Lightweight coding agent that runs in your terminal")
- license: Apache-2.0 (GitHub API license field + npm `license`, 2026-08-21)
- open source? source_available: True for the CLI/core (codex-rs workspace, TUI, app-server, SDK glue, plugin/skills loaders). Not open: the Codex cloud service, the IDE extension binary distribution, the ChatGPT desktop app, and the models. Language mix (GitHub languages API via gh, 2026-08-21): Rust 96.3%, Python 2.9%, Starlark 0.2%, TypeScript 0.2%.
- first public release: 2025-04-16 — first npm publish of `@openai/codex` 0.1.2504161551 at 2025-04-16T22:53Z (https://registry.npmjs.org/@openai/codex); repo created 2025-04-13T05:37Z (https://api.github.com/repos/openai/codex); launch date 2025-04-16 per https://en.wikipedia.org/wiki/OpenAI_Codex_(AI_agent) (OpenAI launch post https://openai.com/index/introducing-codex/ unreachable, 403).
- latest release: rust-v0.149.0, published 2026-08-20T21:04Z (https://github.com/openai/codex/releases/latest, 2026-08-21); npm dist-tag latest 0.149.0, alpha 0.150.0-alpha.5 (2026-08-21); Homebrew cask codex 0.149.0 (https://formulae.brew.sh/api/cask/codex.json, 2026-08-21).
- what it is:
  - Form factors: CLI/TUI (`codex`, plus `codex exec` non-interactive); IDE extension for VS Code, Cursor, Windsurf, Xcode, JetBrains (https://learn.chatgpt.com/docs/codex/ide); Codex cloud (sandboxed cloud tasks, GitHub and GitLab-beta integration, https://learn.chatgpt.com/docs/changelog 2026-08-19 entry); desktop: the standalone Codex app (launched Feb 2026) was merged into the ChatGPT desktop app for macOS/Windows on 2026-07-09 (https://www.techtimes.com/articles/320087/20260710/chatgpt-work-free-every-plan-what-openais-codex-merger-changes-you.htm; https://en.wikipedia.org/wiki/OpenAI_Codex_(AI_agent)); ChatGPT web and iOS ("Codex Remote", changelog 2026-08-18); app-server (JSON-RPC) and SDKs for embedding (https://learn.chatgpt.com/docs/app-server, https://learn.chatgpt.com/docs/codex-sdk).
  - Models: default provider `openai` (config reference: `model_provider` default `openai`, model example `gpt-5.5`); pricing page lists GPT-5.6 Sol / Luna allowances (https://learn.chatgpt.com/docs/pricing). Not locked: built-in providers `azure`, `bedrock` (Amazon Bedrock Runtime built-in as of CLI 0.148.0, 2026-08-18, changelog; AWS announcement 2026-06-01 https://aws.amazon.com/blogs/aws/get-started-with-openai-gpt-5-5-gpt-5-4-models-and-codex-on-amazon-bedrock/), `ollama`/`oss` local open-weight models via `codex --oss` (https://ollama.com/blog/codex, 2026-01-15), and custom `[model_providers.<id>]` with `base_url` + `wire_api` (https://learn.chatgpt.com/docs/config-file/config-reference).
  - Pricing: included in all ChatGPT tiers — Free $0, Go $8/mo, Plus $20/mo, Pro from $100/mo ($100 = 5x, $200 = 20x limits), Business $20/user/mo (annual, 2+ users), Enterprise/Edu custom; rolling 5-hour message windows; credits purchasable on Pro/Business; or API key pay-per-token (https://learn.chatgpt.com/docs/pricing, 2026-08-21). README (2026-08-21) lists Plus/Pro/Business/Edu/Enterprise only — see section 6.
  - Install: `curl -fsSL https://chatgpt.com/codex/install.sh | sh` (macOS/Linux); PowerShell `irm https://chatgpt.com/codex/install.ps1 | iex` (Windows); `npm install -g @openai/codex`; `brew install --cask codex`; GitHub Releases binaries (README, 2026-08-21). Platforms: macOS arm64/x86_64, Linux x86_64/arm64, Windows.
  - Default autonomy: new sessions in a version-controlled folder default to "Auto" = sandbox `workspace-write` + `on-request` approvals; non-VCS folders default to `read-only`; network access off by default; full-access `--yolo`/`danger-full-access` labelled "not recommended". OS sandbox: macOS Seatbelt (`sandbox-exec`), Linux bwrap + seccomp, Windows native sandbox or WSL2 (https://learn.chatgpt.com/docs/agent-approvals-security, 2026-08-21).

## 2. Adoption evidence

Independently observable (all as of 2026-08-21 unless noted):
- GitHub stars | 111,208 | 2026-08-21 | https://api.github.com/repos/openai/codex
- GitHub forks | 17,050 | 2026-08-21 | same
- GitHub watchers (subscribers) | 569 | 2026-08-21 | same
- Open issues / open PRs | 13,208 issues, 176 PRs | 2026-08-21 | GitHub GraphQL via gh (repo issues/pullRequests OPEN totalCount)
- Contributors | 471 | 2026-08-21 | Link header of https://api.github.com/repos/openai/codex/contributors?per_page=1
- Commits, last 90 days (since 2026-05-23) | 2,802 | 2026-08-21 | https://api.github.com/repos/openai/codex/commits?since=2026-05-23T00:00:00Z (28 pages x 100 + 2)
- Releases, last 90 days | 28 stable + 181 prerelease = 209 | 2026-08-21 | https://api.github.com/repos/openai/codex/releases (stable: 0.144.x .. 0.149.0; most recent stable 0.146.1 2026-08-05, 0.147.0 2026-08-07, 0.148.0 2026-08-18, 0.149.0 2026-08-20)
- GitHub Discussions | 732 total, six categories, multiple new threads on 2026-08-21 | 2026-08-21 | https://github.com/openai/codex/discussions
- npm `@openai/codex` weekly downloads | 13,530,406 (2026-08-13..08-19) | https://api.npmjs.org/downloads/point/last-week/@openai/codex
- npm `@openai/codex` monthly downloads | 66,821,031 (2026-07-21..08-19) | https://api.npmjs.org/downloads/point/last-month/@openai/codex
- npm `@openai/codex` versions published | 3,966 (first 2025-04-16) | 2026-08-21 | https://registry.npmjs.org/@openai/codex
- npm `@openai/codex-sdk` weekly downloads | 1,022,230 (2026-08-13..08-19) | https://api.npmjs.org/downloads/point/last-week/@openai/codex-sdk
- npm `@agentclientprotocol/codex-acp` (third-party ACP adapter) weekly downloads | 1,130,010 (2026-08-13..08-19) | https://api.npmjs.org/downloads/point/last-week/@agentclientprotocol/codex-acp
- Homebrew cask `codex` installs | 30d 114,832 (rank #1 of all casks, 5.01%), 90d 263,516, 365d 709,591 | 2026-08-21 | https://formulae.brew.sh/api/cask/codex.json ; https://formulae.brew.sh/api/analytics/cask-install/30d.json
- VS Code Marketplace extension `openai.chatgpt` ("Codex – OpenAI's coding agent") | 13,348,301 installs; avg rating 3.07 (530 ratings); version 26.5818.32112 last updated 2026-08-21 | Marketplace extensionquery API + https://marketplace.visualstudio.com/items?itemName=openai.chatgpt (surface: IDE extension)
- PyPI `openai-codex` (Python SDK) | version 0.147.0 | 2026-08-21 | https://pypi.org/pypi/openai-codex/json (download counts: pypistats rate-limited, null)
- Curated skills repo openai/skills | 25,097 stars, created 2025-11-25 | 2026-08-21 | https://api.github.com/repos/openai/skills
- Benchmark (independent) | GPT-5.6 Sol (max) "in Codex" scores 80 on Artificial Analysis Coding Agent Index (leads all three sub-evals: DeepSWE, Terminal-Bench v2, SWE-Atlas-QnA); Intelligence Index 59 | 2026-07-09 | https://artificialanalysis.ai/articles/gpt-5-6-has-landed (note: AA states it supported OpenAI with pre-release evaluation)
- Benchmark (aggregator) | SWE-bench Pro: GPT-5.6 Sol 64.6%, Terra 63.4%, Luna 62.7%; Terminal-Bench 2.1 Sol 89.5% | Aug 2026 | https://www.morphllm.com/swe-bench-pro (third-party aggregate; model-level, not harness-level)
- Press coverage with numbers | Fortune 2026-03-04: 1.6M weekly active users, >1M desktop-app downloads since early Feb 2026, token usage up 5x | https://www.fortune.com/2026/03/04/openai-codex-growth-enterprise-ai-agents

Maker-claimed (OpenAI statements relayed via secondary sources because openai.com returned 403):
- ~600K weekly users at start of 2026 | Jan 2026 | aggregator citing OpenAI disclosures, https://www.digitalapplied.com/blog/openai-codex-4m-weekly-developers-growth-data
- >1M weekly active users | 2026-02-02 (Codex desktop app launch) | Reuters via digitalapplied (above)
- 1.6M weekly active users, "more than tripled" since GPT-5.3-Codex | 2026-03-04 | Fortune (above), OpenAI figures
- >2M weekly active users | 2026-03-19 | Reuters via Wikipedia https://en.wikipedia.org/wiki/OpenAI_Codex_(AI_agent)
- 3M weekly developers | 2026-04-08 | Sam Altman announcement via digitalapplied; 3M also in https://thenextweb.com/news/openai-codex-enterprise-partners-cognizant-cgi (2026-04-21)
- ">4 million developers ... every week" | 2026-04-21 | OpenAI post https://openai.com/index/scaling-codex-to-enterprises-worldwide/ (403 here); same sentence quoted in AWS blog 2026-06-01 https://aws.amazon.com/blogs/aws/get-started-with-openai-gpt-5-5-gpt-5-4-models-and-codex-on-amazon-bedrock/
- >5M weekly active users; >6x since desktop app launch; ~20% knowledge workers growing 3x faster than developers | 2026-06-02 | OpenAI post https://openai.com/index/codex-for-knowledge-work/ (403 here); relayed by https://www.unite.ai/openai-says-codex-and-chatgpt-work-hit-10-million-users/ and https://tech-insider.org/ie/openai-codex-5-million-users-2026/
- 10M people using Codex + ChatGPT Work combined (not broken out; metric definition unclear) | 2026-07-21 | Tibo Sottiaux on X / OpenAI to Bloomberg, relayed by unite.ai (above)
- "grown 20x since August [2025]", "trillions of tokens weekly" | Dec 2025/Jan 2026 | Alexander Embiricos on Lenny's Podcast https://www.lennysnewsletter.com/p/why-humans-are-ais-biggest-bottleneck (maker employee statement on third-party podcast)
- Cisco: PR review time reduced up to 50%; Instacart: Codex SDK integrated into its "Olive" background-agent platform | 2025-10 GA post https://openai.com/index/codex-now-generally-available/ (403 here) via search snippets
- Gartner: OpenAI named a Leader in enterprise coding agents | 2026 | https://openai.com/index/gartner-2026-agentic-coding-leader/ (403 here; title only, from search)

Public customers / logos (maker-named; all via openai.com posts relayed by press): Cisco, Temporal, Superhuman, Duolingo, Vanta, Rakuten, Instacart (May/Oct 2025 posts); Cisco, Nvidia, Ramp, Rakuten, Harvey (Fortune 2026-03-04); Notion, Ramp, Braintrust, GitHub, Nextdoor, Wonderful, Cisco, Nvidia, Virgin Atlantic (2026-04-21 enterprise post via TNW); GSI partners Cognizant and CGI (2026-04-21, https://news.cognizant.com/2026-04-21-Cognizant-and-OpenAI-Partner-to-Reshape-Enterprise-Software-Engineering-with-Codex); Dell partnership (2026-05-18, via digitalapplied).

Funding / valuation (company-level, independently reported): OpenAI raised $122B at $852B post-money, closed 2026-03-31 (https://www.cnbc.com/2026/03/31/openai-funding-round-ipo.html; https://www.forbes.com/sites/antoniopequenoiv/2026/03/31/openai-valuation-reaches-852-billion-after-massive-funding-round/). Codex-specific revenue: none published.

Community size: GitHub Discussions 732 (above). Codex Discord announced by @OpenAIDevs Jan 2026 (https://x.com/OpenAIDevs/status/2014050636506255407); member count null (not accessible). r/codex subscriber count: null (reddit returned 403). OpenAI Developer Community forum has a Codex CLI category (https://community.openai.com/t/adjusting-codex-plan-mode/1378499); volume null.

## 3. Plugin interface (census fields)

- mcp_support: **both** (CLI). Client: connects to STDIO and streamable-HTTP MCP servers with bearer/OAuth (CIMD + DCR) auth, configured in `~/.codex/config.toml` or project `.codex/config.toml` under `[mcp_servers.<name>]`; `/mcp` in the TUI; surfaces: CLI, IDE extension, ChatGPT desktop app, ChatGPT web for plugin-provided remote MCP (https://learn.chatgpt.com/docs/extend/mcp?surface=cli, 2026-08-21). Server: the CLI exposes a `codex mcp-server` subcommand (`McpServer(McpServerCommand)` in https://github.com/openai/codex/blob/main/codex-rs/cli/src/main.rs, 2026-08-21); the SDK page also describes orchestrating Codex from the Agents SDK via MCP server configuration (https://learn.chatgpt.com/docs/codex-sdk).
- plugin_support: **True** — two layers. (a) Plugins: bundles of skills, connectors/MCP servers, apps, hooks, browser-extension capabilities and scheduled-task templates; manifest `.codex-plugin/plugin.json` (fields incl. `skills`, `hooks`, `mcpServers`, `apps`, `interface` — https://github.com/openai/codex/blob/main/codex-rs/skills/src/assets/samples/plugin-creator/references/plugin-json-spec.md); distributed via marketplaces (`~/.agents/plugins/marketplace.json` personal marketplace; `codex plugin add <name>@<marketplace>`, `codex plugin marketplace add/list`, `codex plugin list`) and a universal "Plugins Directory" shared with ChatGPT (tabs: OpenAI / workspace / Personal / Installed); CLI `/plugins`; not supported in the IDE extension (https://learn.chatgpt.com/docs/plugins, 2026-08-21). (b) Skills: `SKILL.md` folders following the open Agent Skills standard (agentskills.io), discovered in `.agents/skills` (cwd, parents, repo root), `$HOME/.agents/skills`, `/etc/codex/skills`, plus OpenAI-bundled; invoked with `$name` in CLI/IDE or auto-selected; curated catalog https://github.com/openai/skills (https://learn.chatgpt.com/docs/build-skills, 2026-08-21).
- claude_code_plugin: **partial** (researched). Official docs are silent on Claude Code. Source code and release notes show: plugin loader treats `.claude-plugin/plugin.json` as an alternate manifest path next to `.codex-plugin/plugin.json` (https://github.com/openai/codex/blob/main/codex-rs/core-plugins/src/manifest.rs, https://github.com/openai/codex/blob/main/codex-rs/utils/plugins/src/plugin_namespace.rs); marketplace loader accepts `.agents/plugins/marketplace.json`, `.agents/plugins/api_marketplace.json`, `.claude-plugin/marketplace.json`, `.cursor-plugin/marketplace.json` (https://github.com/openai/codex/blob/main/codex-rs/core-plugins/src/marketplace.rs); release 0.146.0 (2026-07-29): "additional plugin marketplaces for Amazon Bedrock and Claude Code" (#34979 "Infer the bundled Claude Code plugin marketplace"); release 0.145.0 (2026-07-21): `/import` "migrate Cursor and Claude Code settings, MCP servers, plugins, sessions, commands, and project-scoped memories" (#31672 etc.); release 0.147.0 (2026-08-07): sync imported Claude and Cursor conversations (https://github.com/openai/codex/releases). Instruction files: reads AGENTS.md / AGENTS.override.md only; CLAUDE.md is not read unless listed in `project_doc_fallback_filenames` (https://learn.chatgpt.com/docs/agent-configuration/agents-md). Skills: reads `.agents/skills`, not `.claude/skills` (build-skills page).
- subagents: **True** — built-in multi-agent: Codex spawns specialised subagents for independent tasks and consolidates results; `[agents]` config (`agents.enabled` default true, `max_concurrent_threads_per_session`, `default_subagent_model`, `default_subagent_reasoning_effort`); custom agents as TOML under `~/.codex/agents/` or `.codex/agents/` (name, description, developer_instructions); built-ins `default`, `worker`, `explorer`; `/agent` command; Subagents panel; CLI 0.149.0 added an interactive `codex agents` dashboard (https://learn.chatgpt.com/docs/agent-configuration/subagents; https://github.com/openai/codex/releases/tag/rust-v0.149.0, 2026-08-20).
- hooks: **True** — events SessionStart, SessionEnd, PreToolUse, PermissionRequest, PostToolUse, UserPromptSubmit, Stop, PreCompact, PostCompact, SubagentStart, SubagentStop; configured in `~/.codex/hooks.json` or `config.toml`, project `.codex/hooks.json`, or plugin `hooks/hooks.json`; feature key `features.hooks` (alias `codex_hooks`); only `type: "command"` handlers execute (prompt/agent parsed but skipped); admins can enforce via `requirements.toml`; `/hooks` command (https://learn.chatgpt.com/docs/hooks, 2026-08-21).
- plan_mode: **True** — `/plan [description]` or Shift+Tab cycles collaboration modes (Default, Plan, Pair, Execute); Plan mode is read-only exploration producing a reviewable plan; config key `plan_mode_reasoning_effort` (https://learn.chatgpt.com/docs/codex/cli; https://learn.chatgpt.com/docs/developer-commands?surface=cli; config reference).
- plugin_docs_url: https://learn.chatgpt.com/docs/plugins (developers.openai.com/codex/plugins redirects there); skills: https://learn.chatgpt.com/docs/build-skills
- config_docs_url: https://learn.chatgpt.com/docs/config-file/config-reference (developers.openai.com/codex/config-file redirects to https://learn.chatgpt.com/docs/config-file which returned 404 on 2026-08-21)
- ACP support: **no first-party**. OpenAI docs (app-server, SDK) do not mention Agent Client Protocol. Third-party adapters wrap the app-server: zed-industries/codex-acp (created 2025-09-16, archived, 879 stars) succeeded by agentclientprotocol/codex-acp (created 2025-12-03, 288 stars, npm `@agentclientprotocol/codex-acp`, Apache-2.0; "starts the Codex App Server, translates ACP requests") — https://github.com/agentclientprotocol/codex-acp, https://zed.dev/acp/agent/codex-cli. Codex issue #9085 "ACP Agent Client Protocol Support" (2026-01-12) closed as not planned (https://github.com/openai/codex/issues/9085).
- SDK availability: TypeScript `@openai/codex-sdk` (Node 18+; start/continue/resume threads, sandbox presets); Python `openai-codex` (3.10+; controls app-server over JSON-RPC, `AsyncCodex`); GitHub Action; app-server JSON-RPC 2.0 over stdio (default), WebSocket (experimental), Unix socket (https://learn.chatgpt.com/docs/codex-sdk; https://learn.chatgpt.com/docs/app-server).

## 4. Claimed differentiation (raw material)

- tagline (README first line): "Codex CLI is a coding agent from OpenAI that runs locally on your computer." — https://github.com/openai/codex ; repo description "Lightweight coding agent that runs in your terminal" — https://api.github.com/repos/openai/codex ; docs CLI page: "Inspect, edit, and run code from your terminal" — https://learn.chatgpt.com/docs/codex/cli ; docs landing: "Start with a goal, idea, or task. ChatGPT can gather context, take action, and produce something useful." — https://learn.chatgpt.com/docs
- maker claims (paraphrased):
  1. Runs locally, open source (Apache-2.0), one install line; same agent available as CLI, IDE extension, cloud, desktop app — README; https://learn.chatgpt.com/docs/quickstart
  2. Sign in with an existing ChatGPT plan (all tiers incl. Free) rather than paying per token; API key as alternative — README; https://learn.chatgpt.com/docs/pricing
  3. Safety-first defaults: OS-level sandboxing (Seatbelt / bwrap+seccomp / Windows sandbox), network off by default, graduated approval policies and permission profiles — https://learn.chatgpt.com/docs/agent-approvals-security
  4. Extensible via skills (open Agent Skills standard), plugins shared with ChatGPT's universal plugin directory, MCP, hooks — https://learn.chatgpt.com/docs/build-skills ; https://learn.chatgpt.com/docs/plugins
  5. Built-in multi-agent (subagents, `codex agents` dashboard, message queueing to sessions) — https://learn.chatgpt.com/docs/agent-configuration/subagents ; release 0.149.0
  6. Embeddable: app-server JSON-RPC, TS/Python SDKs, GitHub Action — https://learn.chatgpt.com/docs/codex-sdk
  7. Enterprise controls: `requirements.toml` managed config, managed-hooks-only mode, Guardian auto-review, Codex Security — https://github.com/openai/codex/blob/main/docs/config.md ; changelog
  8. Positioned beyond coding: "quickly becoming an indispensable tool for everyone who does work on a computer" — OpenAI Forum event 2026-05-13 https://forum.openai.com/public/events/codex-is-for-everyone-why-codex-matters-beyond-code-fa40puy7wi
- audience: developers/engineers needing "codebase context and developer tools" (Codex mode of the quickstart) — https://learn.chatgpt.com/docs/quickstart ; README "included in ChatGPT Plus, Pro, Business, Edu, and Enterprise plans"; enterprise engineering orgs via GSIs (Cognizant PR 2026-04-21); knowledge workers, leaders, researchers, educators, small-business owners (OpenAI Forum event page).

## 5. Company & contact targets (company-level)

- legal name / form: OpenAI Group PBC (public benefit corp) under the OpenAI Foundation (structure per openai.com/our-structure — 403 from this environment; not re-verified here). HQ: San Francisco, California, USA.
- size: not researched (null). Funding stage: private; $122B round at $852B post-money valuation closed 2026-03-31 (CNBC, Forbes — section 2); IPO preparation reported by CNBC.
- publicly named leadership relevant to Codex/partnerships (only where OpenAI itself names them):
  - Thibault "Tibo" Sottiaux — "GM, Codex @ OpenAI" on the OpenAI Forum event page (2026-05-13) https://forum.openai.com/public/events/codex-is-for-everyone-why-codex-matters-beyond-code-fa40puy7wi ; described as "Head of Codex Product" by Fortune 2026-03-04; press reports a 2026 expansion of his GM role across core products (third-party; unverified on openai.com).
  - Alexander Embiricos — named by Sottiaux at the OpenAI Forum event as lead product manager on Codex (event replay https://forum.openai.com/public/videos/event-replay-codex-is-for-everyone-why-codex-matters-beyond-code-2026-05-13); "OpenAI Codex Product Lead" in third-party podcast listings (https://www.lennysnewsletter.com/p/why-humans-are-ais-biggest-bottleneck).
  - Denise Dresser — Chief Revenue Officer, quoted in the Cognizant-OpenAI partner release 2026-04-21 https://news.cognizant.com/2026-04-21-Cognizant-and-OpenAI-Partner-to-Reshape-Enterprise-Software-Engineering-with-Codex (relevant to partnerships).
  - Sam Altman — CEO (openai.com leadership/structure pages 403 from this environment; named as announcing the 3M-developer milestone 2026-04-08 via digitalapplied).
  - Head of DevRel / head of ecosystem for Codex: none found publicly named by OpenAI in the materials reached (null).
- No personal contact details collected.

## 6. Open questions / conflicts

- openai.com, chatgpt.com/codex and help.openai.com all returned HTTP 403 to WebFetch and curl on 2026-08-21; every maker-claimed user figure above is relayed through press/aggregators and should be re-verified against the primary posts (introducing-codex, introducing-the-codex-app, codex-now-generally-available, scaling-codex-to-enterprises-worldwide, codex-for-knowledge-work, gartner-2026-agentic-coding-leader).
- "10M users" (2026-07-21) covers Codex + ChatGPT Work combined and the metric window (daily vs weekly) is not defined (unite.ai). Do not treat as a Codex-only WAU figure.
- Pricing conflict: README (2026-08-21) says Codex is included in Plus/Pro/Business/Edu/Enterprise; the docs pricing page lists Free ($0) and Go ($8) as also including Codex (Free/Go cannot buy Codex credits per help-center search snippet). Existing census `pricing` field omits Free/Go.
- Docs domain moved: developers.openai.com/codex/* now 308-redirects to learn.chatgpt.com/docs/*; some redirect targets 404 (e.g. /docs/config-file; /docs/codex/skills-and-plugins). The census `docs_url`, `plugin_docs_url`, `config_docs_url` still point at developers.openai.com (they resolve via redirect, but the config-file target is currently broken).
- Config reference documents `wire_api` value "responses" only; older docs/ community material reference "chat" for OpenAI-compatible providers — not re-verified.
- Existing census entry fields that look wrong or stale:
  - `first_released: "2025-04-13"` — that is the repo-creation date; public launch / first npm publish is 2025-04-16.
  - `current_release: "2026-08-19"` — no stable release on that date; latest stable is 0.149.0 on 2026-08-20 (0.148.0 on 2026-08-18). Field should probably carry a version string.
  - `platforms: ["CLI"]` — product family also ships IDE extension (VS Code, Cursor, Windsurf, Xcode, JetBrains), Codex cloud, ChatGPT desktop app, web, iOS. If the entry is CLI-only by design, fine, but `what_makes_it_special` already mentions IDEs.
  - `stars: null` — 111,208 on 2026-08-21.
  - `homepage: null` — https://developers.openai.com/codex (redirects to learn.chatgpt.com/docs).
  - `model_providers: "OpenAI, Amazon Bedrock"` — also Azure, Ollama/OSS local, and any OpenAI-compatible endpoint via `model_providers`.
  - `claude_code_plugin: null` — researched: partial (reads `.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json`; `/import` migrates Claude Code settings/plugins; does not read CLAUDE.md or `.claude/skills`).
  - `language: "Rust, TypeScript"` — TypeScript is 0.2% of the repo; Rust 96.3%, Python 2.9%.
  - `mcp_support: True` — more precisely both client and server.
- Not verified: Discord member count; r/codex size; PyPI download counts (pypistats 429); exact date plan mode / hooks / plugins first shipped (changelog page only rendered August 2026 entries).

## 7. Sources

1. https://github.com/openai/codex — README (tagline, install, plans, IDEs, license)
2. https://api.github.com/repos/openai/codex — stars, forks, watchers, created_at, license, language
3. https://api.github.com/repos/openai/codex/contributors?per_page=1 — contributor count (Link header)
4. https://api.github.com/repos/openai/codex/commits?since=2026-05-23T00:00:00Z — 90-day commit count
5. https://api.github.com/repos/openai/codex/releases — release cadence, latest release, release notes (Claude Code marketplace, /import, Bedrock)
6. https://github.com/openai/codex/releases/latest — 0.149.0 notes (agents dashboard, queue, doctor)
7. GitHub GraphQL (gh api graphql) — discussions 732, open issues/PRs
8. https://github.com/openai/codex/discussions — categories, recency
9. GitHub languages API (gh) — Rust 96.3%
10. https://registry.npmjs.org/@openai/codex — first publish date, version count, dist-tags
11. https://api.npmjs.org/downloads/point/last-week/@openai/codex — weekly downloads
12. https://api.npmjs.org/downloads/point/last-month/@openai/codex — monthly downloads
13. https://api.npmjs.org/downloads/point/last-week/@openai/codex-sdk — SDK weekly downloads
14. https://api.npmjs.org/downloads/point/last-week/@agentclientprotocol/codex-acp — ACP adapter downloads
15. https://formulae.brew.sh/api/cask/codex.json and /api/analytics/cask-install/30d.json — Homebrew installs, #1 cask
16. VS Code Marketplace extensionquery API + https://marketplace.visualstudio.com/items?itemName=openai.chatgpt — 13.35M installs
17. https://pypi.org/pypi/openai-codex/json — Python SDK version
18. https://api.github.com/repos/openai/skills — skills catalog stars
19. https://learn.chatgpt.com/docs — docs landing (redirect target), sections
20. https://learn.chatgpt.com/docs/codex/cli — CLI features, plan mode, slash commands
21. https://learn.chatgpt.com/docs/developer-commands?surface=cli — slash command list
22. https://learn.chatgpt.com/docs/extend/mcp?surface=cli — MCP client details
23. https://learn.chatgpt.com/docs/plugins — plugins, directory, surfaces
24. https://learn.chatgpt.com/docs/build-skills — skills standard, directories
25. https://learn.chatgpt.com/docs/hooks — hook events, config, flags
26. https://learn.chatgpt.com/docs/agent-configuration/subagents — subagents
27. https://learn.chatgpt.com/docs/agent-configuration/agents-md — AGENTS.md discovery, no CLAUDE.md
28. https://learn.chatgpt.com/docs/agent-approvals-security — sandbox, approvals, defaults
29. https://learn.chatgpt.com/docs/config-file/config-reference — providers, features, plan_mode_reasoning_effort
30. https://learn.chatgpt.com/docs/codex-sdk — TS/Python SDKs
31. https://learn.chatgpt.com/docs/app-server — JSON-RPC app server
32. https://learn.chatgpt.com/docs/pricing — plan tiers incl. Free/Go
33. https://learn.chatgpt.com/docs/changelog — Aug 2026 entries, Bedrock, GitLab beta
34. https://learn.chatgpt.com/docs/codex/ide — IDE extension editors
35. https://learn.chatgpt.com/docs/quickstart — surfaces, audience wording
36. https://github.com/openai/codex/blob/main/codex-rs/core-plugins/src/marketplace.rs — marketplace manifest paths incl. .claude-plugin
37. https://github.com/openai/codex/blob/main/codex-rs/core-plugins/src/manifest.rs — alternate .claude-plugin/plugin.json
38. https://github.com/openai/codex/blob/main/codex-rs/external-agent-migration/src/source/cla.rs — Claude Code import source
39. https://github.com/openai/codex/blob/main/codex-rs/skills/src/assets/samples/plugin-creator/references/plugin-json-spec.md — plugin.json spec
40. https://github.com/openai/codex/blob/main/codex-rs/cli/src/main.rs — `codex mcp-server` subcommand
41. https://github.com/openai/codex/blob/main/docs/config.md — managed hooks note
42. https://github.com/agentclientprotocol/codex-acp — third-party ACP adapter
43. https://zed.dev/acp/agent/codex-cli — Zed ACP integration
44. https://github.com/openai/codex/issues/9085 — ACP request closed not planned
45. https://forum.openai.com/public/events/codex-is-for-everyone-why-codex-matters-beyond-code-fa40puy7wi — Sottiaux title, audience claim
46. https://forum.openai.com/public/videos/event-replay-codex-is-for-everyone-why-codex-matters-beyond-code-2026-05-13 — Embiricos named
47. https://www.fortune.com/2026/03/04/openai-codex-growth-enterprise-ai-agents — 1.6M WAU, customers
48. https://www.unite.ai/openai-says-codex-and-chatgpt-work-hit-10-million-users/ — 10M combined, 5M June
49. https://www.digitalapplied.com/blog/openai-codex-4m-weekly-developers-growth-data — milestone table
50. https://thenextweb.com/news/openai-codex-enterprise-partners-cognizant-cgi — enterprise customers, CRO quote
51. https://news.cognizant.com/2026-04-21-Cognizant-and-OpenAI-Partner-to-Reshape-Enterprise-Software-Engineering-with-Codex — partner PR
52. https://aws.amazon.com/blogs/aws/get-started-with-openai-gpt-5-5-gpt-5-4-models-and-codex-on-amazon-bedrock/ — Bedrock support, 4M quote
53. https://ollama.com/blog/codex — codex --oss
54. https://artificialanalysis.ai/articles/gpt-5-6-has-landed — independent benchmark
55. https://www.morphllm.com/swe-bench-pro — aggregator scores
56. https://en.wikipedia.org/wiki/OpenAI_Codex_(AI_agent) — timeline
57. https://www.techtimes.com/articles/320087/20260710/chatgpt-work-free-every-plan-what-openais-codex-merger-changes-you.htm — July 9 merger
58. https://www.cnbc.com/2026/03/31/openai-funding-round-ipo.html — funding
59. https://www.forbes.com/sites/antoniopequenoiv/2026/03/31/openai-valuation-reaches-852-billion-after-massive-funding-round/ — valuation
60. https://www.lennysnewsletter.com/p/why-humans-are-ais-biggest-bottleneck — Embiricos claims
61. https://x.com/OpenAIDevs/status/2014050636506255407 — Discord announcement
62. Unreachable (403): https://openai.com/index/introducing-codex/ ; https://openai.com/index/introducing-the-codex-app/ ; https://openai.com/index/codex-now-generally-available/ ; https://openai.com/index/scaling-codex-to-enterprises-worldwide/ ; https://openai.com/index/codex-for-knowledge-work/ ; https://openai.com/codex/ ; https://chatgpt.com/codex ; https://help.openai.com/en/articles/11369540-using-codex-with-your-chatgpt-plan

## Inclusion check (Jesse's test)

**Yes** — Codex CLI runs its own agentic loop (Rust core with tool calls for shell/edit/MCP, sandboxing, approvals, subagents) against OpenAI or configurable models and creates/modifies software locally; it is the agent itself, not a wrapper (third-party ACP adapters wrap it).
