# Dossier: DimCode / DimAgent (census_slug: dimcode)

Compiled 2026-08-24. Facts only. Null convention: "null = not researched"; "False/none = researched and absent". Small closed-source project — research kept proportionate. NOT currently in the census; proposed new-entry frontmatter at end.

## 1. Identity

- name: **DimCode** (npm package/CLI); the product site brands the umbrella product **DimAgent** — "one agent, everywhere" with CLI (DimCode), Desktop, and ACP entry points [S4][S5]. CLI commands: `dim` and `dimcode` (equivalent) [S3].
- maker: GitHub org **arcships** (org created 2026-04-01, location listed "Singapore", 19 followers, 11 public repos; repo was previously at `archships/dimcode` — renamed) [S6][S7]. npm maintainers (public handles only): zerob13, zjywill, simon_he [S1]. Site footer/X: @DimAgentai; "© 2026 DimAgent" [S4]. Site is Chinese-first with 11 UI languages; canonical domain in page metadata is dimagent.com, with mirrors dimagent.cn and dim.qwenkimi.com [S4][S9].
- product URL: https://dimcode.dev (docs at /docs/; ACP page at /docs/acp.html) [S4][S5]
- repo URL: https://github.com/arcships/dimcode — **issues-only tracker**, README says "This is the public issue tracker for DimCode"; sole file is README.md [S6][S8]
- license: none published. npm metadata has no license field; npm README says "See the repository root LICENSE file" but the repo contains no LICENSE [S1][S3][S8] (as-of 2026-08-24). Treat as **proprietary**.
- open source? **False.** source_available: False — distribution is compiled per-platform binaries (`dimcode-darwin-arm64` etc., ~175 MB unpacked, 2 files); the GitHub repo holds no source [S2][S6][S8].
- first public release: npm package created 2026-01-21 (first version 0.0.4-beta.38 same day) [S1].
- latest release: 0.3.19, 2026-08-24; 365 npm versions in ~7 months — near-daily cadence; description says "beta channel" is the recommended install [S1][S3].
- what it is:
  - Form factors: terminal CLI/TUI (`dim`) + headless `dim exec` (JSON output for pipes/CI); a native **desktop app** (Electron; chat workbench, browser preview with on-page annotation, Git integration); **ACP server** (`dim acp`) for editors (Zed shown); a VS Code extension exists on the Marketplace (`dimagent.dimagent-vscode-plugin`, launches the CLI in the integrated terminal) [S3][S4][S5][S9].
  - Models: BYO, multi-provider — site lists "30+ providers" incl. OpenAI, Anthropic, Google, DeepSeek, Qwen, Kimi, xAI, Mistral, Groq, OpenRouter, and local Ollama / LM Studio, plus custom endpoints; many China-market providers (StepFun, GLM, MiniMax, Doubao, Hunyuan, SiliconFlow, PPIO, Z.AI, AIHubMix) [S4].
  - Pricing: free download; BYOK. `dim auth login` exists "for cloud features"; a "Coding Plan" (team collaboration, central permissions, usage dashboards) is on the roadmap as "coming soon" [S3][S4].
  - Install: `npm i -g dimcode@beta` (also bun/pnpm); npm launcher script selects/downloads the platform binary; desktop app downloaded from site [S2][S3].
  - Default autonomy: interactive tool approval (Y/N prompts for commands/file access), `/approvals` settings, "programmable per-tool permissions", decisions remembered across sessions; plan mode is enforced read-only ("two-layer protection, not just a prompt hint" — maker-claimed); local-first storage in `~/.dimcode` (SQLite), credentials in OS keychain, "no forced cloud dependency" [S3][S4] (maker-described, not independently tested).
  - Implementation: closed; launcher references an "opentui binary"; site credits Bun, Electron, Vercel AI SDK, and Vue as community/partner tech — consistent with a Bun-compiled TypeScript runtime [S2][S4][S9]. Language: unknown (closed source).

## 2. Adoption evidence

| metric / claim | value | as-of | source | type |
|---|---|---|---|---|
| npm downloads `dimcode` | 3,752/week; 11,256/month | 2026-08-24 | [S10] | independently observable |
| GitHub stars (issues-only repo) | 22; 0 forks; 0 watchers; 12 open issues | 2026-08-24 | [S6] | independently observable |
| npm release cadence | 365 versions since 2026-01-21; latest published 2026-08-24 | 2026-08-24 | [S1] | independently observable |
| VS Code Marketplace | extension `dimagent.dimagent-vscode-plugin` exists; install count not collected | 2026-08-24 | [S9] | independently observable |
| KV-cache claim | "DeepSeek V4 measured 98% KV-cache reuse", others "90%+" | 2026-08-24 | [S4] | maker-claimed |
| Long-run claim | "20+ hours continuous running" without babysitting | 2026-08-24 | [S4] | maker-claimed |
| Users / customers / funding / community server | none found (no Discord/Slack link; no user numbers; no funding news) | 2026-08-24 | [S4][S9] | researched, absent |
| Benchmarks / press | none found | 2026-08-24 | [S9] | researched, absent |

## 3. Plugin interface (PRI-2925)

- mcp_support: **client** — stdio and HTTP transports, `/mcp` command + `dim mcp list`, config in `~/.dimcode/v2/mcp.json`; no server mode found [S3][S4][S5]. Evidence: https://dimcode.dev (EXTENSIBLE section), npm README.
- plugin_support: **True** — "manifest-driven, error-isolated plugin system"; declarative manifest registers tools / hooks / prompts; single-plugin crash does not take down the runtime; `/plugins` command. A "Plugin SDK" is roadmap "coming soon" [S3][S4]. Evidence: https://dimcode.dev
- claude_code_plugin: **partial** — Skills use "SKILL.md discovery and remote install" (the open Agent Skills format Claude Code also consumes); `@` opens a skill picker. No evidence it reads `.claude/` dirs or the Claude Code plugin/marketplace format [S3][S4] (maker-described; paths not documented publicly).
- subagents: **True** — async multi-agent orchestration; each subagent can use a different model ("let GPT generate, Claude review, DeepSeek refactor"); sandbox isolation via same workspace, git worktree, or container; results auto-aggregated [S4].
- hooks: **True** — "15 extension points" "from run to tool to subagent" [S4]. No public hook reference doc found.
- plan_mode: **True** — Tab toggles agent/plan mode in the TUI; plan mode claimed enforced read-only at two layers [S3][S4].
- plugin_docs_url: none found (docs site has guides for CLI/config/ACP only; no plugin reference page located) — researched, absent [S5].
- config_docs_url: https://dimcode.dev/docs/config.html (linked from docs nav; not fetched) [S5].
- ACP support: **yes, first-party** — `dim acp` starts a JSON-RPC 2.0 ACP server on stdio; shares TUI config (`~/.dimcode/v2/`); documented Zed `agent_servers` integration; `ACP_STICKY_SESSION=true` for stable cross-editor sessions [S5]. Evidence: https://dimcode.dev/docs/acp.html
- SDK: **maker-claimed** — a mirror-site description calls it a "TypeScript SDK for coding agents"; Plugin SDK is explicitly roadmap "coming soon". No published SDK package located [S9][S4].

## 4. Claimed differentiation (raw material for PRI-2927)

- tagline (site, translated from zh): "One agent, everywhere." / "ONE AGENT · EVERYWHERE"; npm README: "An AI coding agent for your terminal." [S4][S3]
- maker claims (paraphrased):
  1. One agent runtime, three entry points — desktop, terminal/scripts, editor (ACP); state lives in the runtime, the frontend is just interaction [S4][S5].
  2. Any model: 30+ providers, cloud and local treated identically, uniform behavior; BYOK [S4].
  3. Cache-friendly context management: stable system prompt / fixed tool definitions / fixed history prefix → claimed 98% KV-cache reuse on DeepSeek V4, 90%+ on other majors, making iteration cheap [S4].
  4. Reliable long-running agent runtime: layered error recovery, automatic context compaction, blob offload of long outputs, "20+ hours continuous running" [S4].
  5. Multi-agent orchestration with per-subagent model choice and sandbox isolation [S4].
  6. Desktop browser preview with on-page element annotation that feeds the agent ("see it change the page") [S4].
  7. Local-first + private: SQLite in `~/.dimcode`, OS keychain for credentials, no forced backend, offline with local models [S4].
  8. Extensible: plugins, MCP, Skills, hooks (15 extension points), subagents; full observability via structured JSONL traces with step-by-step replay, stored locally [S4].
- audience: repo description says "for terminal-first teams" [S6]; roadmap "Coding Plan" targets teams (collaboration, central permission management) [S4]. Chinese-first site + China-market provider list suggests a China-centric audience (observation, not maker-stated).

## 5. Company & contact targets (PRI-2929)

- No legal company name found (researched, absent). Public identity: GitHub org arcships (Singapore); X @DimAgentai; site "© 2026 DimAgent" [S6][S4].
- No team page, no named leadership, no press releases found. npm maintainer handles (zerob13, zjywill, simon_he) are the only public individual identities; per instruction, nothing beyond the public handles recorded [S1].
- Funding: none found (researched, absent).
- Contact paths: GitHub issues on arcships/dimcode; X account [S8][S4].

## 6. Open questions / conflicts

- License is unresolved: npm README points to "the repository root LICENSE file", but the public repo has no LICENSE and npm metadata carries none. Recorded as proprietary-by-default; flag for follow-up [S3][S8].
- Naming split: npm/CLI = DimCode, site/brand = DimAgent, org = arcships (formerly archships), and the docs live on dimcode.dev while metadata canonicalizes dimagent.com — at least four names/domains for one product [S4][S6][S9].
- dimcode.dev returns HTTP 403 to plain fetchers (bot blocking); pages retrieved with a browser user-agent. WebFetch of both target URLs failed [S4][S5].
- The GitHub repo pushed_at is 2026-04-24 while npm ships near-daily — the repo is a dead-drop for issues, so GitHub activity metrics say nothing about development pace here [S6][S1].
- "opentui binary" in the launcher and Vue in the marketplace description: the TUI stack (OpenTUI vs Vue-based) is unclear and unverifiable without source [S2][S9].
- Site stats counters (providers/languages/platforms/KV-cache %) render as "0" in static HTML (JS-animated) — numbers taken from body text instead [S4].
- Not in the existing census; new-entry frontmatter proposed below.

## 7. Sources

1. [S1] https://registry.npmjs.org/dimcode — versions, dates, maintainers, bin, no license/repo fields
2. [S2] dimcode-0.3.19.tgz (npm tarball) + https://registry.npmjs.org/dimcode-darwin-arm64 — launcher script, platform binary packages, 175 MB binary
3. [S3] npm package README.md / README.zh.md (in tarball) — commands, TUI, config, approvals, FAQ, license pointer
4. [S4] https://dimcode.dev/ (fetched 2026-08-24 with browser UA; zh-CN) — DimAgent brand, features, providers, claims, roadmap, partners, GitHub/X links
5. [S5] https://dimcode.dev/docs/acp.html — `dim acp`, Zed integration, shared config paths
6. [S6] https://api.github.com/repositories/1198070361 (arcships/dimcode) — stars 22, created 2026-04-01, no license/language
7. [S7] https://api.github.com/orgs/arcships — org profile, Singapore, created 2026-04-01
8. [S8] https://raw.githubusercontent.com/arcships/dimcode/main/README.md + repo contents API — issues-only repo, single file
9. [S9] Web search results 2026-08-24 — VS Code Marketplace listing (dimagent.dimagent-vscode-plugin), mirror sites dimagent.cn / dim.qwenkimi.com ("multi-model CLI, desktop app, and TypeScript SDK"), dimcode.dev/en/docs/
10. [S10] https://api.npmjs.org/downloads/point/last-week|last-month/dimcode — download counts

## Inclusion check (Jesse's test)

**Yes** — DimCode/DimAgent is its own agent with its own agentic loop: a closed-source compiled runtime with its own provider layer (30+ providers), its own tool set (read/write/edit/exec), approvals, subagent orchestration, and context management; the npm package is a thin launcher for *their own* binary, not a wrapper around another vendor's agent, and `dim acp` exposes that native loop [S2][S3][S4][S5].

## Proposed census entry (per hc/agents/_TEMPLATE.md — new file agents/dimcode.md)

```yaml
---
name: "DimCode"
slug: "dimcode"
layout: "agent.njk"
category: "agent"
maker: "arcships"            # new maker record: maker_type company (org form unverified), country SG (self-listed), makes_models false, revenue_model [] (Coding Plan subscriptions "coming soon")
license: "Proprietary"       # no license published; npm README's LICENSE pointer dangles
url: "https://dimcode.dev"
source_code_url: null         # issues-only tracker: https://github.com/arcships/dimcode
source_available: False
homepage: "https://dimcode.dev"
docs_url: "https://dimcode.dev/docs/"
download_url: "https://www.npmjs.com/package/dimcode"
install_method: "npm i -g dimcode@beta (also bun/pnpm); desktop app download"
platforms: ["CLI", "Desktop", "IDE"]        # IDE via ACP (Zed) + VS Code extension
autonomy_level: ["agentic"]
specialization: "general"
language: null                # closed source
first_released: "2026-01-21"
current_release: "2026-08-24"
maintained: "active"
mcp_support: "yes (client; stdio + HTTP)"
plugin_support: "yes (manifest-driven plugins: tools/hooks/prompts; Plugin SDK on roadmap)"
claude_code_plugin: "partial (SKILL.md Agent Skills format; not the plugin/marketplace format)"
subagents: "yes (async multi-agent, per-subagent model, worktree/container sandbox)"
hooks: "yes (15 extension points, run/tool/subagent)"
plan_mode: "yes (Tab toggle; claimed enforced read-only)"
plugin_docs_url: null
config_docs_url: "https://dimcode.dev/docs/config.html"
model_providers: "30+ (OpenAI, Anthropic, Google, DeepSeek, Qwen, Kimi, xAI, Ollama, LM Studio, custom)"
pricing: "BYOK"
github_stars: 22              # issues-only repo; weak proxy — npm 11.3k downloads/month is the better signal
sources: ["paseo-acp-catalog"]
last_verified: "2026-08-24"
what_makes_it_special: "A closed-source, local-first 'one agent runtime' from a Singapore/China-market org that fronts the same loop through a TUI, a desktop app with in-browser page annotation, and ACP — with cache-friendly context management as its headline cost claim."
---
DimCode (branded DimAgent on its site) appeared on npm in January 2026 as a
multi-model terminal coding agent and grew an Electron desktop workbench and an
ACP server around the same runtime. It courts the BYOK crowd — 30+ cloud and
local providers, China-market ones prominently included — and pitches
reliability engineering (error recovery, context compaction, 20-hour runs) over
model exclusivity. Development happens in private; the GitHub org exists only
to collect issues, and adoption so far is visible mainly as ~11k npm downloads
a month.
```
