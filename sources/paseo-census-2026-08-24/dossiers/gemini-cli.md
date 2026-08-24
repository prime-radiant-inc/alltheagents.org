# Dossier: Gemini CLI (census_slug: gemini-cli)

Compiled 2026-08-21. Facts only. Null convention: "null = not researched"; "False/none = researched and absent". Each non-obvious fact carries a source [Sn] (see section 7) and an as-of date.

Status note (fact, not opinion): on 2026-05-19 Google announced Gemini CLI is being succeeded by "Antigravity CLI"; from 2026-06-18 Gemini CLI stopped serving free-tier, Google AI Pro/Ultra and free Gemini Code Assist accounts; Standard/Enterprise Code Assist licences and paid API keys keep working; the Apache-2.0 repo stays up and continues to receive model/bug/security updates "for our enterprise customers" [S15][S16][S17] (as-of 2026-08-21). Releases continued after that date (v0.56.0 on 2026-08-19) [S3].

## 1. Identity

- name: Gemini CLI
- maker: Google LLC (company; wholly owned subsidiary of Alphabet Inc., NASDAQ GOOG/GOOGL); HQ Mountain View, CA, USA [S29] (as-of 2026-08-21). GitHub org: google-gemini.
- product URL: https://geminicli.com (GitHub `homepage` field) [S2]; docs https://geminicli.com/docs/ [S6]
- repo URL: https://github.com/google-gemini/gemini-cli [S2]
- license: Apache-2.0 (GitHub API spdx_id; npm `license` field) [S2][S4] (as-of 2026-08-21)
- open source? True. source_available: True — full CLI source (TypeScript, monorepo with `@google/gemini-cli` and `@google/gemini-cli-core` packages) is in the repo [S2][S4]. The announced successor, Antigravity CLI (repo google-antigravity/antigravity-cli, created 2026-05-13, license: none per GitHub API), publishes only README/changelog, not source [S17][S33] (as-of 2026-08-21).
- first public release: 2025-06-25 — launch blog post [S13]; first npm version 0.1.0 published 2025-06-25T13:03Z [S4]. GitHub repo created 2025-04-17 [S2].
- latest release: v0.56.0 (stable), 2026-08-19T19:29Z; v0.57.0-preview.0 same day; nightlies daily (v0.56.0-nightly.20260822 published 2026-08-22T01:10Z) [S3]. npm dist-tags: latest 0.56.0, preview 0.57.0-preview.0, nightly [S4]. 594 GitHub releases; 716 npm versions [S4][S30] (as-of 2026-08-21). Docs changelog page lags (lists v0.55.1, 2026-08-11, as latest stable) [S24].
- what it is:
  - Form factors: terminal CLI (interactive TUI and headless `-p` mode with json / stream-json output); ACP server mode (`gemini --acp`, JSON-RPC over stdio) for Zed, JetBrains and other ACP clients; VS Code "Gemini CLI Companion" extension (Marketplace / Open VSX); GitHub Action `google-github-actions/run-gemini-cli` (PR review, issue triage) [S1][S18][S19][S26][S31] (as-of 2026-08-21).
  - Models: Google Gemini only (Gemini 3 / 3.1 Pro and Flash family; docs have "Gemini 3 Support", model selection and model-routing pages). Access via Google sign-in (Gemini Code Assist licence), Gemini API key (AI Studio), or Vertex AI / Google Cloud credentials [S1][S6][S12][S34]. No BYO non-Google models in official docs (none found).
  - Pricing: per docs quota page (updated 2026-06-18): Google account free tier 1,000 model requests/user/day; unpaid Gemini API key 250 req/day (Flash only); Google AI Pro 1,500/day, Ultra 2,000/day; Code Assist Standard 1,500/day, Enterprise 2,000/day, Workspace AI Ultra 2,000/day; Vertex AI Express free 90 days then pay-as-you-go; paid API key per-token [S12]. README still states 60 req/min and 1,000 req/day free with a personal Google account, and "1000 requests/day with Gemini 3" for API key [S1]. Since 2026-06-18 the free / AI Pro / Ultra / free-Code-Assist tiers are served by Antigravity CLI, not Gemini CLI (homepage banner and transition post) [S15][S23] — see section 6. Gemini Code Assist Standard/Enterprise list prices reported by third parties as roughly $19-22.80 and $45-54 per user/month depending on billing term; Google's pricing page could not be parsed by the fetch tool [S42] (unverified).
  - Install: `npx @google/gemini-cli`; `npm install -g @google/gemini-cli` (Node >= 20); `brew install gemini-cli`; `sudo port install gemini-cli`; conda + npm for restricted environments [S1][S43].
  - Default autonomy: approval modes `default` (prompts before write tools and shell), `auto_edit` (auto-approves edit tools), `plan` (read-only), `yolo` (auto-approve all; CLI flag only: `--yolo` / `--approval-mode=yolo`); setting `general.defaultApprovalMode` defaults to `"default"`; TOML policy engine (user `~/.gemini/policies`, admin `/etc/gemini-cli/policies`) with allow/deny/ask_user rules; optional sandboxing (Docker/Podman, macOS Seatbelt); trusted-folders gate [S10][S21][S35][S6] (as-of 2026-08-21).
  - Repo language per GitHub API: TypeScript [S2].

## 2. Adoption evidence

| metric / claim | value | as-of | source | type |
|---|---|---|---|---|
| GitHub stars | 106,608 | 2026-08-21 | [S2] | independently observable |
| GitHub forks | 14,459 | 2026-08-21 | [S2] | independently observable |
| GitHub watchers (subscribers) | 576 | 2026-08-21 | [S2] | independently observable |
| GitHub open issues+PRs (`open_issues_count`) | 789 | 2026-08-21 | [S2] | independently observable |
| GitHub issues ever filed (search API) | 14,043 | 2026-08-21 | [S30] | independently observable |
| GitHub PRs ever (search API) / merged | 12,598 / 6,662 | 2026-08-21 | [S30] | independently observable |
| Merged PRs created since 2026-05-23 (90 days) | 172 | 2026-08-21 | [S30] | independently observable |
| Commits, last 90 days (since 2026-05-23, default branch) | 162 | 2026-08-21 | [S30] | independently observable |
| Commits, last 52 weeks (stats/participation) | 4,448 | 2026-08-21 | [S30] | independently observable |
| GitHub contributors (incl. anonymous) | 692 | 2026-08-21 | [S30] | independently observable |
| GitHub Discussions (total) | 661 | 2026-08-21 | [S30] | independently observable |
| GitHub releases (total) | 594; cadence: nightly daily, stable+preview weekly (v0.56.0 + v0.57.0-preview.0 on 2026-08-19) | 2026-08-21 | [S3][S30] | independently observable |
| npm weekly downloads, @google/gemini-cli | 311,095 (2026-08-14..20) | 2026-08-20 | [S4] | independently observable |
| npm monthly downloads, @google/gemini-cli | 1,734,417 (2026-07-22..08-20) | 2026-08-20 | [S4] | independently observable |
| npm weekly downloads, @google/gemini-cli-core | 45,783 | 2026-08-20 | [S4] | independently observable |
| npm versions published | 716 (first 0.1.0 on 2025-06-25) | 2026-08-21 | [S4] | independently observable |
| Homebrew installs, formula `gemini-cli` | 30d 9,789; 90d 89,032 (rank 189 of all formulae, 0.14%); 365d 840,296 (rank 68, 0.30%) | 2026-08-21 | [S5] | independently observable |
| GitHub Action repo google-github-actions/run-gemini-cli | 2,056 stars, 279 forks (created 2025-07-11) | 2026-08-21 | [S31] | independently observable |
| Extensions: repos in GitHub org `gemini-cli-extensions` | 66 | 2026-08-21 | [S32] | independently observable |
| Extensions gallery (geminicli.com/extensions) | count not obtained (page > 10 MB, fetch failed) | 2026-08-21 | [S7] | null |
| "more than one million developers are building with Gemini CLI" within three months of launch | >1,000,000 developers | 2025-10-08 | [S14] | maker-claimed |
| "100,000+ GitHub stars", "6,000 merged pull requests", "hundreds of contributors" | as stated | 2026-05-19 | [S15] | maker-claimed (stars/PRs match observable counts above) |
| "13 million developers" building with Google's generative models (platform-wide, not CLI-specific) | 13M | 2026-05 (I/O 2026) | [S39] | maker-claimed via press |
| Extensions launch partners | Dynatrace, Elastic, Figma, Harness, Postman, Shopify, Snyk, Stripe | 2025-10-08 | [S14] | maker-claimed |
| Public customers / case studies / logos on site | none found on geminicli.com homepage, plans page or README (researched, absent) | 2026-08-21 | [S1][S23][S34] | — |
| Funding / valuation / acquisition | n/a — Google LLC is a subsidiary of public company Alphabet Inc. | 2026-08-21 | [S29] | independently observable |
| Community: Discord | no Gemini-CLI-specific server found; Google runs a general "Google Gemini" Discord (discord.com/invite/gemini); member count not obtained | 2026-08-21 | [S40] | null (count) |
| Community reaction to transition announcement (Discussion #27274) | 298 thumbs-down vs 6 thumbs-up | 2026-08-21 | [S16] | independently observable |
| Benchmark: Terminal-Bench 2.1 leaderboard, agent "Gemini CLI" | 65.8% +/- 1.4 (Gemini 3 Pro, 2026-05-01); 65.8% +/- 1.7 (Gemini 3.1 Pro, 2026-05-05) | 2026-08-21 | [S28] | independently observable (leaderboard-hosted) |
| SWE-bench | no Gemini-CLI-as-agent entry located (model-level scores circulate in third-party blogs; not verified) | 2026-08-21 | — | null |
| Third-party: Zed ACP | Gemini CLI was the "initial reference implementation" of the Agent Client Protocol (Zed blog) | 2025-08-27 | [S27] | independently observable |
| Third-party: DeepLearning.AI short course "Gemini CLI: Code and Create with an Open-Source Agent" | exists (linked from README) | 2026-08-21 | [S1][S41] | independently observable |
| Press coverage of transition | The Register 2026-05-20; TechTimes 2026-05-23 (403, not fetched); Forbes I/O 2026 | 2026-05 | [S17][S38][S39] | independently observable |

## 3. Plugin interface (PRI-2925)

- mcp_support: **client** — connects to MCP servers over stdio, SSE and streamable HTTP; OAuth 2.0 for remote servers (dynamic client registration, tokens in `~/.gemini/mcp-oauth-tokens.json`), service-account impersonation; MCP prompts exposed as slash commands, MCP resources via `@server://path`; `gemini mcp add/list/remove/enable/disable`; config under `mcpServers` in `~/.gemini/settings.json` / `.gemini/settings.json`. Docs do not describe Gemini CLI acting as an MCP server [S11] (as-of 2026-08-21). Evidence: https://geminicli.com/docs/tools/mcp-server/
- plugin_support: **True** — "Extensions": a directory/GitHub repo with `gemini-extension.json` (name, version, `mcpServers`, `contextFileName`, `excludeTools`) bundling prompts/context files, MCP servers, custom commands (TOML), themes, hooks, sub-agents and Agent Skills; `gemini extensions install <github-url|path>`, `/extensions list`; public gallery at https://geminicli.com/extensions/ ranked by GitHub stars; launch partners listed in section 2 [S7][S14][S37]. Also "Agent Skills" (agentskills.io SKILL.md standard) in `~/.gemini/skills/` or `~/.agents/skills/`, `.gemini/skills/` or `.agents/skills/`, extensions and built-ins; `gemini skills install <git|path> [--scope]` [S20]. Custom slash commands as TOML files [S1]. (as-of 2026-08-21)
- claude_code_plugin: **no** (interop caveat) — no support for `.claude-plugin/plugin.json`, Claude Code marketplaces, `.claude/` directories or CLAUDE.md is documented (researched, absent) [S7][S20][S36]. Interop points: Gemini CLI reads SKILL.md skills from the cross-tool `.agents/skills/` alias ("interoperable path" per docs) using the same Agent Skills open standard; the context file name is configurable (`context.fileName`, e.g. `["AGENTS.md","CONTEXT.md","GEMINI.md"]`), so a CLAUDE.md can be read only if configured [S20][S36] (as-of 2026-08-21).
- subagents: **True** — Markdown + YAML-frontmatter agents in `.gemini/agents/*.md` (project) or `~/.gemini/agents/*.md` (user); built-ins `codebase_investigator`, `cli_help`, `generalist`, `browser_agent` (off by default, Chrome 144+); automatic delegation or explicit `@agent-name`; per-agent model, temperature, max_turns (30), tools allow-list, timeout (10 min); enabled by default via `experimental.enableAgents`; "remote subagents" (`kind: remote`) call external agents over the Agent-to-Agent (A2A) protocol with API key / bearer / ADC / OAuth-PKCE auth [S9][S22] (as-of 2026-08-21). Evidence: https://geminicli.com/docs/core/subagents/
- hooks: **True** — events SessionStart, SessionEnd, BeforeAgent, AfterAgent, BeforeModel, AfterModel, BeforeToolSelection, BeforeTool, AfterTool, PreCompress, Notification; configured in project/user/system `settings.json` or shipped by extensions; command hooks return JSON, exit 2 blocks; can rewrite arguments, swap models, filter tools, inject context; project hooks fingerprinted with change warnings [S8] (as-of 2026-08-21). Evidence: https://geminicli.com/docs/hooks/
- plan_mode: **True** — `plan` approval mode: read-only tools, web search/fetch, research subagents, writes only to plan files; entered via Shift+Tab cycle, `/plan [goal]`, `gemini --approval-mode=plan`, or default in settings; "Plan Mode with model steering" marked experimental [S10] (as-of 2026-08-21). Evidence: https://geminicli.com/docs/cli/plan-mode/
- plugin_docs_url: https://geminicli.com/docs/extensions/ (reference: https://geminicli.com/docs/extensions/reference/ ; writing: https://geminicli.com/docs/extensions/writing-extensions/ ; skills: https://geminicli.com/docs/cli/skills/)
- config_docs_url: https://geminicli.com/docs/cli/settings/ (also https://geminicli.com/docs/reference/configuration/ ; policy engine: https://geminicli.com/docs/reference/policy-engine/)
- ACP support: **yes, first-party** — `gemini --acp` runs Gemini CLI as an ACP server (JSON-RPC 2.0 over stdio); listed in the ACP Agent Registry; used by Zed (reference implementation, 2025-08-27) and JetBrains IDEs [S18][S26][S27] (as-of 2026-08-21).
- SDK: **none documented** — official docs offer headless mode (`-p`, `--output-format json|stream-json`, exit codes 0/1/42/53) for programmatic use; no SDK/library page; `@google/gemini-cli-core` is published on npm (45,783 weekly downloads) but not documented as a public SDK [S4][S19] (as-of 2026-08-21). Google announced an "Antigravity SDK" for the successor platform at I/O 2026 [S25].

## 4. Claimed differentiation (raw material for PRI-2927)

- tagline (README / GitHub description, verbatim-short): "An open-source AI agent that brings the power of Gemini directly into your terminal." — https://github.com/google-gemini/gemini-cli [S1][S2]
- tagline (homepage hero): "Build, debug & deploy with AI" — https://geminicli.com/ [S23]
- docs one-liner: brings Gemini models into the terminal to understand code, automate tasks and build workflows with local project context — https://geminicli.com/docs/ [S6]
- maker claims (paraphrased):
  1. Free, generous tier: 60 req/min and 1,000 req/day with a personal Google account, described at launch as the industry's largest free allowance (README; launch post) [S1][S13].
  2. Gemini 3 models with 1M-token context window (README; launch post said Gemini 2.5 Pro, 1M context) [S1][S13].
  3. Built-in tools: Google Search grounding, file operations, shell commands, web fetch; multimodal input (images, PDFs, sketches) [S1][S13].
  4. Open source, Apache 2.0; community can inspect and contribute [S1][S13].
  5. Extensible: MCP support, custom commands, GEMINI.md context, extensions with a "playbook" that teaches the model how to use bundled tools; open ecosystem with partner and community extensions [S1][S14].
  6. Terminal-first design for developers who live in the terminal; automation via headless/scripts and the GitHub Action (PR reviews, issue triage) [S1][S13].
  7. Shares technology with Gemini Code Assist (agent mode in VS Code), so CLI and IDE use the same engine and licence [S13].
  8. Transition framing (2026-05-19): workflows have "outgrown" the early CLI; successor Antigravity CLI promises faster Go implementation, asynchronous background agents and unified architecture with Antigravity 2.0 [S15].
- audience: individual developers (free tier, students, hobbyists) and professional teams preferring terminal workflows; README adds teams needing Code Assist licences, enterprise users (Vertex AI), GitHub-workflow users [S1][S13].

## 5. Company & contact targets (PRI-2929) — company-level only

- legal name: Google LLC (subsidiary of Alphabet Inc.) [S29]
- HQ: Mountain View, California, USA (1600 Amphitheatre Parkway) [S29]
- size: 190,820 employees (Alphabet, 2025-12-31, Form 10-K) [S29]
- funding stage: public company (Alphabet Inc., NASDAQ GOOG/GOOGL) [S29]
- publicly named leadership (only as named in Google's own posts/filings):
  - Sundar Pichai — Chief Executive Officer, Alphabet and Google (Form 10-K executive officers) [S29]
  - Ryan J. Salva — Senior Director, Product Management (co-byline, Gemini CLI launch post, 2025-06-25) [S13]
  - Taylor Mullen — Senior Staff Software Engineer (launch post 2025-06-25; extensions post 2025-10-08), titled Principal Engineer in the 2026-05-19 transition post [S13][S14][S15]
  - Dmitry Lyalin — Group Product Manager (co-byline, transition post 2026-05-19; posted Discussion #27274) [S15][S16]
  - DevRel lead / head of partnerships for Gemini CLI: none named in consulted sources (researched, absent).
- contact: GitHub issues/discussions (repo); enterprise path via Gemini Code Assist / Google Cloud sales (docs enterprise guide) [S1][S6]

## 6. Open questions / conflicts

- Product status: Google's 2026-05-19 post and the homepage banner say free / Google One (AI Pro/Ultra) users are moved to Antigravity CLI from 2026-06-18, yet the docs quota page (updated 2026-06-18) and README still advertise free Google-account quotas. Which tiers can still sign in to Gemini CLI today is stated only in the transition post and Discussion #27274 (Standard/Enterprise Code Assist, paid API keys, Vertex) [S1][S12][S15][S16][S23].
- Free API-key quota: README says "1000 requests/day with Gemini 3" for an API key; quota page says unpaid API key = 250 req/day, Flash only [S1][S12].
- Existing census `first_released: "2025-04-17"` — that is the repo creation date; public launch and first npm publish were 2025-06-25 [S2][S4][S13].
- Existing census `stars: null`; prose says "107k stars, 6,381 commits" — GitHub API shows 106,608 stars (2026-08-21); commit total not re-verified (4,448 commits in last 52 weeks; 162 in last 90 days) [S2][S30].
- Existing census prose "MCP client and server support" — official MCP docs describe client features only; no server mode found [S11]. Field `mcp_support: True` should read "client".
- Existing census `subagents/hooks/plan_mode: null` — all three exist and are documented (section 3) [S8][S9][S10].
- Existing census `plugin_docs_url/config_docs_url: null` — filled in section 3.
- Existing census `pricing` ("Free tier: 60 req/min, 1,000 req/day...") — accurate to README but superseded for free/Pro/Ultra tiers by the 2026-06-18 transition [S15][S23].
- Existing census `platforms: ["CLI"]` — ACP (Zed/JetBrains), VS Code companion and GitHub Action are official surfaces; fine as "CLI" if IDE use is via ACP/companion [S18][S26][S31].
- Existing census `maintained: "active"` — releases continue (v0.56.0, 2026-08-19), but Google states ongoing work targets enterprise customers [S3][S16].
- "learned from millions of users" appears in a search snippet attributed to a Google developers blog post dated 2026-06-18; that post was not fetched directly — unverified.
- Gemini Code Assist Standard/Enterprise prices: Google's pricing pages (codeassist.google, cloud.google.com/products/gemini/pricing) could not be parsed by the fetch tool; third-party figures only [S42].
- Extensions gallery count: page exceeded fetch size; the `gemini-cli-extensions` GitHub org holds 66 repos, which is a lower bound on Google-published extensions [S7][S32].
- TechTimes article (6,000 contributions / enterprise-only) returned HTTP 403; facts taken from the Google post and The Register instead [S15][S17][S38].
- Homebrew formula JSON lists stable 0.46.0 while npm latest is 0.56.0 — Homebrew formula lag or cached API [S5].
- Discord member counts not obtainable (no CLI-specific server found) [S40].

## 7. Sources

- [S1] https://raw.githubusercontent.com/google-gemini/gemini-cli/main/README.md — tagline, why-bullets, install, auth, features, doc links (2026-08-21)
- [S2] https://api.github.com/repos/google-gemini/gemini-cli — stars, forks, created_at, license, language, homepage (2026-08-21)
- [S3] https://api.github.com/repos/google-gemini/gemini-cli/releases — latest v0.56.0, preview, nightlies (2026-08-21)
- [S4] https://registry.npmjs.org/@google/gemini-cli ; https://api.npmjs.org/downloads/point/last-week/@google/gemini-cli ; .../last-month/... ; .../last-week/@google/gemini-cli-core — versions, first publish, downloads (2026-08-21)
- [S5] https://formulae.brew.sh/api/formula/gemini-cli.json ; https://formulae.brew.sh/api/analytics/install/90d.json ; .../365d.json — Homebrew installs (2026-08-21)
- [S6] https://geminicli.com/docs/ — docs index, intro sentence, feature pages (2026-08-21)
- [S7] https://geminicli.com/docs/extensions/ ; https://geminicli.com/extensions/ (fetch failed, >10 MB) — extension system, gallery (2026-08-21)
- [S8] https://geminicli.com/docs/hooks/ — hook events and config (2026-08-21)
- [S9] https://geminicli.com/docs/core/subagents/ — subagents (2026-08-21)
- [S10] https://geminicli.com/docs/cli/plan-mode/ — plan mode, approval modes (2026-08-21)
- [S11] https://geminicli.com/docs/tools/mcp-server/ — MCP client features (2026-08-21)
- [S12] https://geminicli.com/docs/resources/quota-and-pricing/ — quota table, updated 2026-06-18 (2026-08-21)
- [S13] https://blog.google/technology/developers/introducing-gemini-cli-open-source-ai-agent/ — launch post 2025-06-25, bylines, claims
- [S14] https://blog.google/technology/developers/gemini-cli-extensions/ — extensions launch 2025-10-08, 1M developers, partners
- [S15] https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/ — transition post 2026-05-19, dates, tiers, metrics
- [S16] https://github.com/google-gemini/gemini-cli/discussions/27274 — Google statement on repo future, reactions (2026-08-21)
- [S17] https://www.theregister.com/ai-ml/2026/05/20/bye-bye-gemini-cli-google-nudges-devs-toward-antigravity/5243605 — press, closed-source successor
- [S18] https://geminicli.com/docs/cli/acp-mode/ — ACP mode (2026-08-21)
- [S19] https://geminicli.com/docs/cli/headless/ — headless flags, output formats (2026-08-21)
- [S20] https://geminicli.com/docs/cli/skills/ ; https://raw.githubusercontent.com/google-gemini/gemini-cli/main/docs/cli/skills.md — Agent Skills, .agents/skills alias (2026-08-21)
- [S21] https://geminicli.com/docs/reference/policy-engine/ — approval modes, TOML policies (2026-08-21)
- [S22] https://geminicli.com/docs/core/remote-agents/ — remote subagents via A2A (2026-08-21)
- [S23] https://geminicli.com/ — hero tagline, Antigravity banner (2026-08-21)
- [S24] https://geminicli.com/docs/changelogs/latest/ — changelog page (v0.55.1 listed) (2026-08-21)
- [S25] https://developers.googleblog.com/all-the-news-from-the-google-io-2026-developer-keynote/ — Antigravity 2.0 / CLI / SDK (2026-05-19)
- [S26] https://geminicli.com/docs/ide-integration/ — VS Code companion, JetBrains/Zed via ACP (2026-08-21)
- [S27] https://zed.dev/blog/bring-your-own-agent-to-zed — ACP reference implementation (2025-08-27)
- [S28] https://www.tbench.ai/leaderboard/terminal-bench/2.1 — Gemini CLI entries 65.8% (2026-05)
- [S29] https://www.sec.gov/Archives/edgar/data/1652044/000165204426000018/goog-20251231.htm — Alphabet 10-K FY2025, employees, HQ, officers
- [S30] GitHub search API (issues/PRs/merged counts), commits?since= and contributors?anon=true Link headers, stats/participation, GraphQL discussions/releases totalCount (2026-08-21)
- [S31] https://api.github.com/repos/google-github-actions/run-gemini-cli — GitHub Action repo stars (2026-08-21)
- [S32] https://api.github.com/orgs/gemini-cli-extensions/repos — 66 repos (2026-08-21)
- [S33] https://api.github.com/search/repositories?q=antigravity-cli+in:name — google-antigravity/antigravity-cli, no license (2026-08-21)
- [S34] https://geminicli.com/plans/ — plan tiers (2026-08-21)
- [S35] https://raw.githubusercontent.com/google-gemini/gemini-cli/main/docs/cli/settings.md — defaultApprovalMode, yolo flag-only (2026-08-21)
- [S36] https://raw.githubusercontent.com/google-gemini/gemini-cli/main/docs/cli/gemini-md.md — context.fileName config (2026-08-21)
- [S37] https://raw.githubusercontent.com/google-gemini/gemini-cli/main/docs/extensions/reference.md — gemini-extension.json fields (2026-08-21)
- [S38] https://www.techtimes.com/articles/317056/20260523/google-accepted-6000-gemini-cli-contributions-then-closed-tool-enterprise-only.htm — HTTP 403, not read
- [S39] https://www.forbes.com/sites/janakirammsv/2026/05/21/google-io-2026-turned-gemini-into-an-agent-platform/ — I/O 2026 press (via search summary; 13M developers)
- [S40] https://discord.com/invite/gemini — general Google Gemini Discord (via search)
- [S41] https://learn.deeplearning.ai/courses/gemini-cli-code-and-create-with-an-open-source-agent/information — DeepLearning.AI course
- [S42] https://aiproductivity.ai/pricing/gemini-code-assist/ and similar third-party pages (via search) — Code Assist prices, unverified
- [S43] https://raw.githubusercontent.com/google-gemini/gemini-cli/main/package.json — engines node >= 20 (2026-08-21)

## Inclusion check (Jesse's test)

**Yes** — Gemini CLI runs its own agentic loop (Gemini model + built-in file-edit, shell, web and MCP tools, approval modes, subagents) to create and modify software, with full Apache-2.0 source in the repo [S1][S2][S9][S21].
