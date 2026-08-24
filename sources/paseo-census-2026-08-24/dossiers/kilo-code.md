# Dossier: Kilo Code (census_slug: kilo-code)

Compiled 2026-08-24 (research window 2026-08-21..24; API counts pulled 2026-08-24 unless noted). Facts only. Null convention: "null = not researched"; "False/none = researched and absent". Sources [Sn] in section 7.

## 1. Identity

- name: Kilo Code (company/platform increasingly branded just "Kilo"; the IDE extension and CLI are "Kilo Code") [S1][S5]
- maker: Kilo (Kilo Code) — venture-backed company; co-founded by Scott Breitenother (CEO, founder of Brooklyn Data) and Sid Sijbrandij (co-founder & executive chair; GitLab co-founder) [S20][S21][S22]. Org form: company. HQ: not confirmed in reachable sources (CNBC 403, Businesswire timeout — see section 6). Legal name not confirmed (task brief says "Kilocode Inc."; no primary source located).
- product URL: https://kilo.ai (app: https://app.kilo.ai; docs: https://kilo.ai/docs; blog: https://blog.kilo.ai) [S1][S5]
- repo URL: https://github.com/Kilo-Org/kilocode [S2]
- license: MIT. LICENSE reads "Copyright (c) 2026 Kilo Code / Copyright (c) 2025 opencode" [S3] (as-of 2026-08-21)
- open source? source_available: **partial-by-surface** — the clients (VS Code extension, JetBrains plugin, CLI/TUI, agent runtime) are fully MIT open source in the monorepo; the hosted services (Kilo Gateway, Cloud Agents, Code Reviews, KiloClaw hosting, Gas Town hosting, Teams/Enterprise dashboard) are proprietary services (KiloClaw wraps open-source OpenClaw) [S2][S3][S13][S14][S15]
- **Lineage (precise)**:
  - Kilo Code launched March 2025 as a fork of **Roo Code**: "We started Kilo as a Roo fork in 2025. The two codebases share real git history" (official migration guide, 2026-04-22) [S17]. Roo Code in turn "originated" from **Cline** (Roo Code's own README) [S18].
  - The **Kilo CLI** (first npm publish 2025-10-13) is a fork of **OpenCode**: "Kilo CLI is a fork of OpenCode, enhanced to work within the Kilo agentic engineering platform" (README FAQ); CLI docs: "The Kilo CLI is a fork of OpenCode and supports the same configuration options" [S1][S6]. The monorepo tracks upstream at `packages/opencode` (`.opencode-version`: v1.18.13 as-of 2026-08-21) [S2].
  - In 2026 the whole platform pivoted onto the OpenCode-based runtime: the current VS Code extension is "built on the Kilo CLI" (`packages/kilo-vscode`, shipped as the Marketplace "pre-release" channel) [S9][S10]; the original Roo-lineage extension/plugin moved to **Kilo-Org/kilocode-legacy** (created 2026-02-22, archived) and reached **end of life 2026-07-31** [S4].
- first public release: VS Code Marketplace listing kilocode.Kilo-Code released 2025-03-07 [S7]; GitHub repo created 2025-03-10 [S2]; earliest README offered "$20 of free Claude 3.7 Sonnet tokens" and a Product Hunt launch [S4]. CLI: first npm publish 2025-10-13 (0.0.1-alpha.0); CLI 1.0.0 on 2026-01-29; CLI renumbered from 1.0.x to 7.0.x on 2026-02-23 to match the extension version line [S8][S2].
- latest release: v7.4.23, 2026-08-20 (GitHub release + npm latest + Marketplace all agree); JetBrains plugin releases tagged separately (jetbrains/v7.1.0-rc.2 on 2026-08-18) [S2][S7][S8] (as-of 2026-08-21)
- what it is:
  - Form factors: VS Code extension; JetBrains plugin; CLI (interactive TUI, headless `kilo run` [--auto], local server `kilo serve`, `kilo acp`); Cloud Agents (browser, GitHub/GitLab repos, ephemeral containers, also driven via `kilo cloud`); Slack integration; mobile apps; automated PR Code Reviews (GitHub App / GitLab); KiloClaw (hosted always-on OpenClaw agent, 24/7, chat via Kilo Chat/Telegram/Discord/Slack); Gas Town (hosted multi-agent orchestration: Mayor/Polecats/Refinery working in parallel worktrees, built on the open Gastown protocol); Kilo Gateway (OpenAI-compatible model API); App Builder; Kilo Deploy [S1][S5][S9][S12][S13][S14][S15][S16]
  - Models: BYO across "500+ models across 60+ providers" via the Kilo Gateway (no API key needed to start), or BYOK direct to Anthropic/OpenAI/Google/Bedrock/Vertex/OpenRouter/etc., or local (Ollama, LM Studio); mid-task model switching; per-agent "Sticky Models" [S1][S5][S11][S17]
  - Pricing model: clients free & open source; inference pay-as-you-go at "the model provider's rate with zero markup" (5% credit-purchase processing fee); Kilo Pass $19/mo starter with up-to-50% bonus credits; free-model tier ($0, Auto Free/BYOK/Local); Teams $15/user/mo (analytics, centralized billing — no credits included); Enterprise custom (SSO/OIDC/SCIM, audit logs, model/provider allow-listing, SLA); cloud compute billed per second (Gas Town $1.20/hr, Code Review $0.33/hr, Cloud Agent Standard $1.20/hr; Cloud Agents & Code Reviews compute free during beta) [S5][S12][S13][S19]
  - Install: VS Code Marketplace (current product ships on the "pre-release" channel), Open VSX, JetBrains Marketplace, `npm install -g @kilocode/cli`, `curl -fsSL https://kilo.ai/cli/install | bash`, pnpm, bun, `brew install Kilo-Org/tap/kilo`, AUR `kilo-bin`, GitHub Release binaries (incl. musl and x64-baseline builds) [S1][S9]
  - Default autonomy: interactive sessions "request approval for operations which have not been auto-approved"; per-tool/per-glob `allow`/`ask`/`deny` permission rules (bash patterns, file paths, `task` delegation targets); built-in sensitive-file prompts for `.env*` that broad allows do not bypass; `kilo run --auto` disables all prompts (CI/CD); read-only built-in agents (Ask, explore) [S1][S6][S23][S24]
  - Repo language: TypeScript; runtime built on Bun; CLI ships as compiled binaries [S2][S25]

## 2. Adoption evidence

| metric / claim | value | as-of | source | type |
|---|---|---|---|---|
| GitHub stars (Kilo-Org/kilocode) | 26,973 | 2026-08-21 | [S2] | independently observable |
| GitHub forks / watchers / open issues | 3,074 / 109 / 596 | 2026-08-21 | [S2] | independently observable |
| GitHub contributors | 397 (non-anonymous); 1,217 incl. anonymous — history includes upstream OpenCode commits (29,489 total commits) | 2026-08-21 | [S2] | independently observable (caveat: fork history inflates) |
| Legacy repo (kilocode-legacy) contributors / stars | 369 / 44; archived, EOL 2026-07-31 | 2026-08-21 | [S4] | independently observable |
| Commits since 2026-05-23 (90d) | 7,675 (incl. upstream merges) | 2026-08-21 | [S2] | independently observable |
| GitHub releases (current repo) | 185; roughly weekly stable releases (v7.4.21/22/23 on Aug 11/13/20) | 2026-08-21 | [S2] | independently observable |
| Issues ever filed / PRs ever | 4,537 / 7,642 | 2026-08-21 | [S2] | independently observable |
| VS Code Marketplace installs (kilocode.Kilo-Code) | 1,446,345 installs; 205 ratings, avg 3.85 | 2026-08-21 | [S7] | independently observable |
| Open VSX downloads (kilocode/Kilo-Code) | 3,514,033; 3.38 avg over 21 reviews | 2026-08-21 | [S26] | independently observable |
| JetBrains Marketplace downloads (plugin 28350 "Kilo Code") | 357,704 | 2026-08-21 | [S27] | independently observable |
| npm weekly downloads @kilocode/cli | 19,897 (2026-08-14..20); monthly 195,032; 218 versions since 2025-10-13 | 2026-08-20 | [S8] | independently observable |
| npm weekly downloads `kilocode` (community wrapper?) | 87 | 2026-08-20 | [S8] | independently observable |
| Discord members ("Kilo" guild) | 15,329 (1,569 online) | 2026-08-21 | [S28] | independently observable (invite API) |
| Blog (Substack) subscribers | "Over 27,000" | 2026-08-21 | [S29] | maker-claimed (Substack-displayed) |
| Registered users | "3M+ Kilo Coders" | 2026-08-21 (homepage) | [S5] | maker-claimed |
| Tokens processed | "40T+ tokens processed" (cumulative) | 2026-08-21 (homepage) | [S5] | maker-claimed |
| Earlier milestones | "1.5M+ Kilo Coders. 25T+ tokens processed. #1 on OpenRouter" (archived repo description, frozen ~2026-02-24) | 2026-02-24 | [S30] | maker-claimed |
| At seed announcement | 750,000+ downloads; #1 on OpenRouter; ~6.1T tokens/month | 2025-12-10 | [S20][S21][S22] | maker-claimed (repeated by press) |
| Funding | $8M seed led by Cota Capital; Breakers, General Catalyst, Quiet Capital, Tokyo Black | 2025-12-10 | [S20][S21][S22] | maker-claimed / press (CNBC headline confirms) |
| Customer logos on homepage | Meta, Amazon, Airbnb, PayPal, Square, Red Hat ("developers at" framing) | 2026-08-21 | [S5] | maker-claimed |
| "#1 Open Source Product of the Month" badge | displayed on homepage (platform unspecified on page) | 2026-08-21 | [S5] | maker-claimed |
| Press | CNBC "Former GitLab CEO raises money for Kilo…" (2025-12-10, paywalled/403 to fetch); Businesswire release (timeout); techstartups.com recap | 2025-12-10 | [S21][S22][S31] | press |
| Benchmarks (SWE-bench, Terminal-Bench) | none found for the Kilo harness (Kilo runs its own model leaderboard at kilo.ai/leaderboard; docs list "Benchmarking" as a feature proposal) | 2026-08-24 | [S13][S32] | researched, absent |
| Reddit r/kilocode | exists (linked from README); member count | null (not researched) | [S1] | null |

## 3. Plugin interface (PRI-2925)

- mcp_support: **client** — connects to MCP servers over STDIO and SSE transports; per-tool `allow`/`ask`/`deny` auto-approval; curated servers installable from the Kilo Marketplace (community repo Kilo-Org/kilo-marketplace); no MCP-server mode documented (researched, absent). Evidence: https://kilo.ai/docs/automate/mcp/overview [S33] (as-of 2026-08-24)
- plugin_support: **True** — (1) TypeScript/JavaScript **plugins** loaded at startup in both CLI and VS Code extension: add custom tools, intercept/block tool calls, subscribe to events, register auth/model providers, mutate LLM params; loaded from npm (install scripts disabled), config `plugin` array, or `.kilo/plugin/` dirs; `kilo plugin <module>`; `KILO_PURE=1` disables; behavior documented as identical to upstream OpenCode plugins [S34]. (2) **Skills** — implements the open Agent Skills format (SKILL.md), from `~/.kilo/skills/`, `.kilo/skills/`, extra paths and remote URL manifests [S35]. (3) **Custom modes/agents** (markdown + frontmatter) and **workflows/slash commands** (`.kilo/commands/*.md`) [S36][S37]. (4) **Kilo Marketplace** for MCP servers and modes [S38]
- claude_code_plugin: **partial** — loads `.claude/skills/` "when Claude Code Compatibility is enabled" plus `.agents/skills/` (open agent standard) by default; reads `~/.claude/CLAUDE.md` and `CLAUDE.md` as instruction sources alongside AGENTS.md; imports Claude Code session transcripts from `~/.claude/projects/` (and Codex CLI rollouts); no support for the Claude Code plugin/marketplace format itself (researched, absent) [S35][S39] (as-of 2026-08-24)
- subagents: **True** — built-in subagents `general` (full tools) and `explore` (read-only); custom subagents via `kilo.jsonc` `agent` map, markdown files in `~/.config/kilo/agents/` / `.kilo/agents/`, or `kilo agent create`; agent `mode: primary|subagent|all`; invoked by the Task tool or `@agent-name`; isolated sessions, per-agent model/temperature/permissions; `task` permission controls which subagents an agent may spawn; subagents run in parallel; legacy Orchestrator mode deprecated in favor of native subagents; Code Reviews shards up to 6 read-only subagents; Gas Town orchestrates whole agent teams (Mayor/Polecats/Refinery) [S23][S36][S14][S15]. Evidence: https://kilo.ai/docs/customize/custom-subagents
- hooks: **True (via the plugin system, not a standalone hooks config)** — plugin hook surface includes tool-call interception before/after execution (mutate args, rewrite output, block), event subscriptions (sessions, messages, permission requests, LSP diagnostics, file changes), chat-parameter/header mutation, compaction customization, shell env injection; hooks from multiple plugins run sequentially in load order [S34]. No shell-command lifecycle hooks file like Claude Code's `hooks.json` (researched, absent).
- plan_mode: **True** — built-in **Plan** agent: read-only tools plus editing restricted to `.kilo/plans/` (replaces legacy Architect mode); **Ask** agent is fully read-only with a restricted bash whitelist [S23]. Evidence: https://kilo.ai/docs/code-with-ai/agents/using-agents
- plugin_docs_url: https://kilo.ai/docs/automate/extending/plugins (skills: https://kilo.ai/docs/customize/skills; marketplace: https://kilo.ai/docs/customize/marketplace)
- config_docs_url: https://kilo.ai/docs/code-with-ai/platforms/cli#configuration (settings UI: https://kilo.ai/docs/getting-started/settings; permissions: https://kilo.ai/docs/customize/agent-permissions). Config: `~/.config/kilo/kilo.json[c]`, project `kilo.json[c]` / `.kilo/`, legacy `opencode.json[c]` / `.kilocode/` still read; schema at https://app.kilo.ai/config.json [S6][S34]
- ACP support: **yes, first-party** — `kilo acp` starts an "ACP (Agent Client Protocol) server" (CLI command reference) [S6] (as-of 2026-08-24)
- SDK: **partial/available** — JS SDK generated from the CLI server API lives in the monorepo (`packages/sdk/js`, plus `@kilocode/plugin` types); `kilo serve` exposes a local HTTP+SSE API; the documented "SDKs & Frameworks" page covers the Kilo **Gateway** (model API), not an agent SDK product [S25][S34][S16]

## 4. Claimed differentiation (raw material for PRI-2927)

- tagline (homepage, verbatim): "Code with AI without breaking the bank" — https://kilo.ai [S5]
- README one-liner (verbatim): "The open source coding agent for building with AI in VS Code, JetBrains, or the CLI." — https://github.com/Kilo-Org/kilocode [S1]
- GitHub description: "Kilo is the all-in-one agentic engineering platform… the most popular open source coding agent" [S2]
- maker claims (paraphrased):
  1. Open pricing / no markup: pay the model provider's exact rate, zero inference markup, no lock-in; 5% credit processing fee is the disclosed cost; "all roads lead to metered pricing" essays [S1][S5][S19]
  2. Model freedom: 500+ models across 60+ providers, mid-task switching, no silent model switching, BYOK and local models, per-agent sticky models [S1][S5][S17]
  3. Open source: MIT-licensed clients you can fork/modify/self-host [S1][S5]
  4. One platform, many surfaces: one portal controlling agents across IDEs, CLI and cloud (Cloud Agents, Code Reviews, KiloClaw, Gas Town, Slack, mobile) [S5][S9]
  5. Parallel/orchestrated agents: parallel tool execution, parallel subagents, isolated git worktrees, Gas Town multi-agent teams that write, review and merge with minimal intervention [S17][S14][S23]
  6. Transparency/control: prompt and context visibility, explicit allow/ask/deny permissions, sensitive-file guards [S5][S24]
  7. Self-checking agent, terminal & browser control, inline autocomplete, MCP marketplace [S1]
  8. Speed framing: "Kilo Speed", eliminating "AI drag" (seed post) [S20]
- audience: individual developers (free, open source), "developers at" large companies (logo wall), teams (Teams plan, AI Adoption Score) and enterprises (SSO, audit logs, model controls) [S5][S12][S19]
- named competitors: comparison pages vs Cursor, GitHub Copilot, Roo Code, Windsurf, Claude Code (homepage footer); migration guides from Cursor/Windsurf and Roo Code [S5][S17][S40]

## 5. Company & contact targets (PRI-2929) — company-level only

- company: Kilo (Kilo Code); legal name not confirmed in reachable primary sources (brief says Kilocode Inc.) — see section 6
- HQ: not confirmed (Businesswire dateline unreachable; CNBC 403) — null
- size: not stated publicly in consulted sources — null
- funding stage: seed — $8M (announced 2025-12-10), led by Cota Capital, with Breakers, General Catalyst, Quiet Capital, Tokyo Black [S20][S21][S22]
- publicly named leadership:
  - Scott Breitenother — Co-founder & CEO (seed announcement byline; press) — https://blog.kilo.ai/p/kilo-raised-8-million-seed-round [S20][S22]
  - Sid Sijbrandij — Co-founder & Executive Chair (GitLab co-founder) — same sources [S20][S21][S22]
  - DevRel / partnerships leads: none found named on kilo.ai (researched, absent)
- contact: enterprise sales via https://kilo.ai/contact-sales [S12]

## 6. Open questions / conflicts

- **Census `maker: "Kilo-Org"`** — that is the GitHub org name; the maker is the company Kilo (Kilo Code), co-founded by Breitenother/Sijbrandij, $8M seed [S20]. Legal entity name ("Kilocode Inc.") not verified against a primary source (Businesswire timed out, CNBC 403, Crunchbase not consulted directly).
- **Census records no lineage** — significant: Kilo Code began as a Roo Code fork (Roo Code originated from Cline) [S17][S18]; the CLI and the current VS Code/JetBrains products are built on a fork of OpenCode [S1][S6]; the Roo-lineage codebase is EOL (2026-07-31) and archived [S4]. Any lineage field should say "Roo Code/Cline lineage (legacy, EOL); OpenCode fork (current)".
- **Census `first_released: "2025-03-10"`** — repo creation date; the Marketplace listing went live 2025-03-07 [S7]. Close enough but the earlier date is observable.
- **Census `current_release: "2026-08-20"`** — matches v7.4.23 [S2]; still true as of 2026-08-21.
- **Census `stars: null`** — 26,973 (2026-08-21) [S2].
- **Census `hooks: null`** — True via the plugin hook system [S34].
- **Census `claude_code_plugin: null`** — partial (`.claude/skills` + CLAUDE.md + transcript import; not the plugin format) [S35][S39].
- **Census `plugin_docs_url`/`config_docs_url`: null** — filled in section 3.
- **Census `what_makes_it_special` lists a "Review" specialized agent** — docs state Review "is not included in the VSCode extension or CLI"; automated review is the separate cloud Code Reviews product [S23][S14]. Also "specialized agents (Code, Plan, Ask, Debug, Review)" should note Orchestrator is deprecated.
- **Census `install_method` mentions "curl script"** — correct (https://kilo.ai/cli/install); Homebrew is via the Kilo tap (`Kilo-Org/tap/kilo`), not homebrew-core (no formula found in core) [S1].
- **Census `platforms: ["IDE","CLI"]`** — misses web/cloud (Cloud Agents, Gas Town, KiloClaw, Code Reviews), Slack, mobile [S5][S9].
- "3M+ Kilo Coders" (homepage) vs 1.45M VS Code installs + 3.5M Open VSX downloads: the "Kilo Coders" definition (registered accounts? installs?) is not stated; treat as maker-claimed [S5][S7][S26].
- "#1 on OpenRouter" is a Dec-2025 maker/press claim; current OpenRouter app ranking not re-verified (rankings page not fetched) [S20][S22].
- GitHub contributor/commit counts are inflated by inherited OpenCode history after the 2026 repo pivot; legacy-repo contributor count (369) better reflects the pre-pivot extension community [S2][S4].
- Unreachable sources: https://www.cnbc.com/2025/12/10/former-gitlab-ceo-raises-8-million-for-kilo-to-compete-in-vibe-coding.html (HTTP 403); https://www.businesswire.com/news/home/20251210195261/en/ (timeout). HQ/legal-name facts they may contain are therefore unfilled.

## 7. Sources

1. [S1] https://raw.githubusercontent.com/Kilo-Org/kilocode/main/README.md — tagline, installs, surfaces, agents, --auto, OpenCode-fork FAQ (2026-08-21)
2. [S2] https://api.github.com/repos/Kilo-Org/kilocode (+ /releases, /contributors, /commits, /contents, search API via gh) — stars/forks/dates/releases/tree/.opencode-version
3. [S3] https://raw.githubusercontent.com/Kilo-Org/kilocode/main/LICENSE — MIT, Kilo Code + opencode copyright
4. [S4] https://github.com/Kilo-Org/kilocode-legacy (README + API) — legacy Roo-lineage codebase, EOL 2026-07-31, Roo migration link, early README
5. [S5] https://kilo.ai/ — tagline, 3M+ Kilo Coders, 40T+ tokens, logos, why-Kilo claims, comparison pages
6. [S6] https://kilo.ai/docs/code-with-ai/platforms/cli — OpenCode fork statement, commands (incl. `kilo acp`), config paths, permissions
7. [S7] https://marketplace.visualstudio.com/_apis/public/gallery/extensionquery (kilocode.Kilo-Code) — installs, ratings, releaseDate 2025-03-07, v7.4.23
8. [S8] https://registry.npmjs.org/@kilocode/cli + https://api.npmjs.org/downloads/point/... — versions, first publish, weekly/monthly downloads
9. [S9] https://kilo.ai/docs/getting-started/installing — pre-release channel note, Open VSX, VSIX, Slack tab
10. [S10] https://kilo.ai/docs (landing) — "rebuilt on the Kilo CLI" framing
11. [S11] https://kilo.ai/docs (AI Providers section index in llms.txt) — provider list incl. Ollama/LM Studio/Bedrock/Vertex
12. [S12] https://kilo.ai/docs/collaborate/teams/about-plans — Teams $15/user/mo, Enterprise features, contact-sales
13. [S13] https://kilo.ai/docs/code-with-ai/platforms/cloud-agent — cloud agents, `kilo cloud`, beta compute free
14. [S14] https://kilo.ai/docs/automate/code-reviews/overview — PR reviews, REVIEW.md, sub-agent tiers, $ credits
15. [S15] https://kilo.ai/docs/kiloclaw/overview + https://kilo.ai/docs/code-with-ai/gastown — hosted OpenClaw; Gas Town orchestration (Mayor/Polecats/Refinery)
16. [S16] https://kilo.ai/docs/gateway (section index) — Kilo Gateway API, SDKs & Frameworks
17. [S17] https://kilo.ai/articles/roo-to-kilo-migration-guide — "started Kilo as a Roo fork in 2025", permission model change, parallel subagents, sticky models (2026-04-22)
18. [S18] https://github.com/RooCodeInc/Roo-Code (README) — "Cline (from where Roo Code originated)"
19. [S19] https://kilo.ai/pricing — Kilo Pass $19/mo, 5% processing fee, compute rates, zero-markup, 60+ providers
20. [S20] https://blog.kilo.ai/p/kilo-raised-8-million-seed-round — $8M seed, investors, founders, 750k downloads, #1 OpenRouter, 6T tokens/mo (2025-12-10)
21. [S21] https://www.cnbc.com/2025/12/10/former-gitlab-ceo-raises-8-million-for-kilo-to-compete-in-vibe-coding.html — press headline (page 403 on fetch; headline via search)
22. [S22] https://techstartups.com/2025/12/10/kilo-code-raises-8m-in-seed-funding-as-its-open-source-ai-coding-agent-hits-1-on-openrouter/ — press recap: founders, investors, 6.1T tokens/mo
23. [S23] https://kilo.ai/docs/code-with-ai/agents/using-agents + https://kilo.ai/docs/customize/custom-subagents — built-in agents, Plan read-only, Orchestrator deprecated, subagent mechanics
24. [S24] https://kilo.ai/docs/customize/agent-permissions — allow/ask/deny globs, .env guards, task permission
25. [S25] https://kilo.ai/docs/contributing/architecture (+ cli-runtime/vscode-extension pages via llms.txt) — packages/opencode runtime, Bun-compiled CLI, packages/sdk regeneration
26. [S26] https://open-vsx.org/api/kilocode/Kilo-Code — downloads/rating
27. [S27] https://plugins.jetbrains.com/api/searchPlugins?search=kilo%20code — plugin 28350 downloads
28. [S28] https://discord.com/api/v9/invites/Ja6BkfyTzJ?with_counts=true — member counts
29. [S29] https://blog.kilo.ai/ — Substack subscriber count, 3M+/40T+ banner
30. [S30] https://api.github.com/repos/Kilo-Org/kilo (archived 2026-02-24) — description: "#1 on OpenRouter. 1.5M+ Kilo Coders. 25T+ tokens processed"
31. [S31] https://www.businesswire.com/news/home/20251210195261/en/ — official release (unreachable: timeout)
32. [S32] https://kilo.ai/docs/contributing/features (Benchmarking proposal) + kilo.ai/leaderboard — no external harness benchmark found
33. [S33] https://kilo.ai/docs/automate/mcp/overview — MCP client, STDIO/SSE, marketplace, tool permissions
34. [S34] https://kilo.ai/docs/automate/extending/plugins — plugin/hook system, load order, KILO_PURE, OpenCode-identical behavior
35. [S35] https://kilo.ai/docs/customize/skills — Agent Skills format, .claude/skills & .agents/skills compatibility, remote skill URLs
36. [S36] https://kilo.ai/docs/customize/custom-modes — custom modes/agents, org-managed modes
37. [S37] https://kilo.ai/docs/customize/workflows — slash commands in .kilo/commands/
38. [S38] https://kilo.ai/docs/customize/marketplace + https://github.com/Kilo-Org/kilo-marketplace — MCP/modes marketplace
39. [S39] llms.txt corpus (https://kilo.ai/docs/llms.txt) — CLAUDE.md support, Claude Code transcript import, AGENTS.md handling
40. [S40] https://kilo.ai/docs/getting-started/migrating — "Migrating from Cursor/Windsurf"

## Inclusion check (Jesse's test)

**Yes** — Kilo Code creates and modifies software with its own agentic loop: the MIT-licensed runtime in `packages/opencode` (an actively maintained OpenCode fork, not a thin wrapper) executes tools (read/edit/bash/browser), enforces permissions, and drives subagents across CLI, IDE and cloud surfaces [S1][S6][S25].
