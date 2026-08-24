# Dossier: GitHub Copilot CLI (census_slug: github-copilot-cli)

Researched 2026-08-21. Facts only. Null convention: "null" = not researched; "False/none" = researched and absent. Family-level (GitHub Copilot as a whole) numbers are labelled [FAMILY]; CLI-specific numbers are labelled [CLI]. "maker-claimed" vs "independently observable" marked per item.

## 1. Identity

- name: GitHub Copilot CLI (npm package `@github/copilot`; binary `copilot`)
- maker: GitHub, Inc. (wholly owned subsidiary of Microsoft since 2018-10-26; org form: company; HQ San Francisco, CA, USA). Source: https://en.wikipedia.org/wiki/GitHub (as of 2026-08-21)
- product URL: https://github.com/features/copilot/cli/
- repo URL: https://github.com/github/copilot-cli (repo contains only README.md, LICENSE.md, changelog.md, install.sh and .github/; no source code — checked via GitHub contents API 2026-08-21)
- license: proprietary "GitHub Copilot CLI License" (LICENSE.md). No right to modify or create derivatives; redistribution only unmodified as part of a larger app. GitHub API reports license as "Other/NOASSERTION". Source: https://raw.githubusercontent.com/github/copilot-cli/main/LICENSE.md (2026-08-21)
- open source: False. source_available: False — the public repo hosts the issue tracker, changelog and install script; the npm package `@github/copilot` ships only `npm-loader.js` plus per-platform optional binary packages (`@github/copilot-darwin-arm64` etc.). Source: https://unpkg.com/@github/copilot@1.0.80/package.json (2026-08-21). Related open components: `github/copilot-sdk` is MIT (https://github.com/github/copilot-sdk); plugin marketplaces `github/copilot-plugins` and `github/awesome-copilot` are MIT.
- first public release: public preview 2025-09-25 (changelog post https://github.blog/changelog/2025-09-25-github-copilot-cli-is-now-in-public-preview/ ; npm `@github/copilot` 0.0.1 published 2025-09-25 per https://registry.npmjs.org/@github/copilot ; oldest GitHub release tag v0.0.328 published 2025-09-26 per GitHub releases API). The repo itself was created 2023-01-06 (GitHub API `created_at`), when it hosted the earlier "GitHub Copilot for CLI" technical preview; that preview became the separate, now-archived `gh copilot` extension (https://github.com/github/gh-copilot, created 2023-10-26, archived, last push 2025-10-30).
- general availability: 2026-02-25 (https://github.blog/changelog/2026-02-25-github-copilot-cli-is-now-generally-available/ ; repo changelog entry 0.0.418 2026-02-25)
- latest release: stable 1.0.80 (2026-08-14, changelog.md); npm dist-tag latest 1.0.80, prerelease 1.0.81-7 published 2026-08-21 (registry.npmjs.org, GitHub releases API, 2026-08-21). 802 versions published on npm since 2025-09-25.
- what it is:
  - Form factor: terminal CLI coding agent (interactive TUI + programmatic `-p` mode); also runs as an ACP server (`copilot --acp`) for IDEs, and is the runtime bundled by the Copilot SDK. Available inside JetBrains IDEs as an agent option since 2026-06-02 (https://github.blog/changelog/2026-06-02-introducing-copilot-cli-and-agentic-capabilities-enhancements-in-jetbrains-ides/). Cloud-sandbox mode (`copilot --cloud`) runs the session in a GitHub-hosted ephemeral Linux environment (preview).
  - Models: multi-vendor via GitHub's model routing — Anthropic, OpenAI, Google models (changelog adds e.g. Claude Opus 5 1.0.75 2026-07-24, GPT-5.6 1.0.70, Gemini 3.6 Flash 1.0.74, grok-4.5 1.0.76, kimi-k3 1.0.79, Claude Fable 5); switch with `/model`. BYOK / custom providers supported via env vars: OpenAI-compatible, Azure OpenAI, Anthropic, local (Ollama). Sources: https://docs.github.com/en/copilot/concepts/agents/about-copilot-cli ; changelog.md (2026-08-21).
  - Pricing: included in every Copilot plan (Free, Student, Pro $10, Pro+ $39, Max $100, Business $19/seat, Enterprise $39/seat); each interaction consumes "AI credits" (1 credit = $0.01 USD) from the plan's monthly allowance, usage-based since 2026-06-01. Sources: https://docs.github.com/en/copilot/get-started/plans ; https://github.com/features/copilot/plans ; https://github.com/orgs/community/discussions/192963 (2026-08-21). Earlier (to 2026-05-31) billing was per "premium request".
  - Install: `curl -fsSL https://gh.io/copilot-install | bash`; `brew install copilot-cli`; `winget install GitHub.Copilot`; `npm install -g @github/copilot`; release binaries; included in Codespaces/dev containers. Source: README (2026-08-21).
  - Default autonomy: asks before tool use that modifies files/runs shell ("approve once / approve for session / reject"); "trusted directory" confirmation at start; flags `--allow-all-tools`, `--allow-tool`, `--deny-tool`; Autopilot mode (Shift+Tab or `--autopilot`) runs until done; local sandbox (`/sandbox enable`, preview) and cloud sandbox. Sources: https://docs.github.com/en/copilot/concepts/agents/about-copilot-cli ; https://docs.github.com/en/copilot/concepts/agents/copilot-cli/autopilot (2026-08-21).

## 2. Adoption evidence

| metric / claim | value | as-of | source | type |
|---|---|---|---|---|
| [CLI] GitHub stars github/copilot-cli | 11,108 | 2026-08-21 | https://api.github.com/repos/github/copilot-cli | independently observable |
| [CLI] forks | 1,904 | 2026-08-21 | same | independently observable |
| [CLI] watchers (subscribers) | 266 | 2026-08-21 | same | independently observable |
| [CLI] open issues (incl. PRs) | 2,169 open; 4,031 issues total (1,895 closed); 184 PRs; 120 discussions | 2026-08-21 | GitHub REST + GraphQL | independently observable |
| [CLI] contributors listed | 22 (repo holds only docs/changelog/install script, so contributor count is not a proxy for dev team size) | 2026-08-21 | GitHub contributors API | independently observable |
| [CLI] commits last 90 days (main) | 32 (each is a release/changelog bump) | 2026-05-23..2026-08-21 | GitHub commits API | independently observable |
| [CLI] release cadence | ~25 stable 1.0.x releases 2026-06-01..2026-08-14 plus near-daily prereleases; 398 tags; 802 npm versions | 2026-08-21 | changelog.md; registry.npmjs.org | independently observable |
| [CLI] npm weekly downloads `@github/copilot` | 1,463,245 | week 2026-08-13..2026-08-19 | https://api.npmjs.org/downloads/point/last-week/@github/copilot | independently observable (note: `@github/copilot-sdk` bundles the CLI as a dependency and itself had 908,823 weekly downloads, so part of CLI downloads are SDK-driven) |
| [CLI] npm monthly downloads | 7,192,248 | 2026-07-21..2026-08-19 | https://api.npmjs.org/downloads/point/last-month/@github/copilot | independently observable |
| [CLI] Homebrew cask `copilot-cli` installs | 19,085 (30d); 64,203 (90d, rank #17 of all casks, 0.93%); 214,733 (365d) | 2026-08-21 | https://formulae.brew.sh/api/cask/copilot-cli.json ; https://formulae.brew.sh/api/analytics/cask-install/90d.json | independently observable |
| [CLI] Copilot SDK repo (wraps CLI) stars | 10,428 stars, 1,412 forks, created 2026-01-14, MIT | 2026-08-21 | https://api.github.com/repos/github/copilot-sdk (via gh) | independently observable |
| [CLI] CLI usage "nearly doubling month over month" | qualitative | 2026-04-29 (MSFT FY26 Q3 call) | https://www.fool.com/earnings/call-transcripts/2026/04/29/microsoft-msft-q3-2026-earnings-transcript/ | maker-claimed (Microsoft) |
| [CLI] Microsoft-internal study: adopters of Claude Code + Copilot CLI merged ~24% more PRs; tens of thousands of Microsoft engineers; 4-month window early 2026 | ~24% | submitted 2026-07-01 | https://arxiv.org/abs/2607.01418 | maker-affiliated research (Microsoft authors) |
| [FAMILY] GitHub Copilot paid subscribers | 4.7 million, +75% YoY; Pro+ individual subs +77% QoQ | 2026-01-28 (FY26 Q2 call) | https://www.fool.com/earnings/call-transcripts/2026/01/28/microsoft-msft-q2-2026-earnings-call-transcript/ | maker-claimed (Microsoft) |
| [FAMILY] organizations using Copilot in Enterprise | nearly 140,000, nearly tripled YoY | 2026-04-29 (FY26 Q3 call) | fool.com Q3 transcript (above) | maker-claimed |
| [FAMILY] GitHub Copilot users | 50 million (of 225 million GitHub users); "1 in 3 pull requests on GitHub now involves an agent"; Copilot revenue "accelerated over 60% quarter over quarter" after June usage-based pricing | 2026-07-29 (FY26 Q4 call) | https://www.fool.com/earnings/call-transcripts/2026/08/07/microsoft-msft-q4-2026-earnings-call-transcript/ | maker-claimed (Microsoft) |
| [FAMILY] GitHub platform | 180M+ developers, 4M+ organizations, 90% of Fortune 100 | 2026-08-21 | https://github.com/about | maker-claimed |
| [FAMILY] customer logos on Copilot page | Duolingo, FedEx, American Airlines, Shopify, Stripe, Coca-Cola, Coyote Logistics, Mercado Libre, General Motors; case study Grupo Boticário "+94% productivity" | 2026-08-21 | https://github.com/features/copilot | maker-claimed |
| [FAMILY] Copilot page claims | "up to 55% more productive", "up to 75% higher job satisfaction", "millions of individual users and tens of thousands of business customers" | 2026-08-21 | https://github.com/features/copilot | maker-claimed |
| [FAMILY] JetBrains AI Pulse survey | Copilot 76% awareness, 29% adoption at work | 2026-04 | via search summary (secondary; primary not fetched) | third-party |
| funding / valuation | GitHub acquired by Microsoft for $7.5B (completed 2018-10-26); no separate funding | — | https://en.wikipedia.org/wiki/GitHub | independently observable |
| community | no dedicated Discord found (none researched beyond GitHub); GitHub Community "Copilot News and Announcements" discussions; repo discussions 120 | 2026-08-21 | https://github.com/orgs/community/discussions/categories/copilot-news-and-announcements | independently observable |
| third-party: ACP registry listing | Listed in Zed ACP agent registry (`npx @github/copilot@1.0.80 --acp`) | 2026-08-21 | https://zed.dev/acp/agent/github-copilot | independently observable |
| third-party: benchmarks | none found specific to Copilot CLI (SWE-bench etc.) — researched, absent in official materials and press found | 2026-08-21 | — | — |
| press | InfoQ 2026-04-12 (https://www.infoq.com/news/2026/04/github-copilot-cli-ga/); Visual Studio Magazine 2026-03-02 (https://visualstudiomagazine.com/articles/2026/03/02/github-copilot-cli-reaches-general-availability-bringing-agentic-coding-to-the-terminal.aspx — 403, not read); Microsoft Tech Community posts; numerous comparison blogs (devleader.ca 2026-07-31 etc.) | 2026-08-21 | — | third-party |

## 3. Plugin interface (six census fields)

- mcp_support: **client** (uses MCP servers; GitHub MCP server built in; stdio/HTTP/SSE transports; `copilot mcp add`, `/mcp add`, `~/.copilot/mcp-config.json`, repo `.mcp.json` or `.github/mcp.json`; enterprise registry/allowlist policy). No evidence it can act as an MCP server (researched: docs silent) — note it instead exposes an ACP server and JSON-RPC via the SDK. Evidence: https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-mcp-servers (2026-08-21)
- plugin_support: **True** — own plugin system with marketplaces. Plugins bundle custom agents (`agents/*.agent.md`), skills (`skills/*/SKILL.md`), hooks (`hooks.json`), MCP config, LSP config, commands; manifest `plugin.json` at plugin root; also supports Agent Plugins 1.0 / Open Plugin Spec v1 manifests (changelog 1.0.74 2026-07-23; GA 2026-08-12). Default marketplaces: `github/copilot-plugins` and `github/awesome-copilot`; `copilot plugin install NAME@MARKETPLACE`, `copilot plugin marketplace add OWNER/REPO` (GitHub, other Git hosts, local path). Enterprise-managed plugins via `.github-private/.github/copilot/settings.json` (preview 2026-05-06). Skills also standalone: `.github/skills`, `.claude/skills`, `.agents/skills`, `~/.copilot/skills`, `~/.agents/skills`. Evidence: https://docs.github.com/en/copilot/concepts/agents/copilot-cli/about-cli-plugins ; https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/plugins-finding-installing ; https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-skills ; https://github.blog/changelog/2026-08-12-agent-plugins-1-0-in-vs-code-copilot-cli-and-the-copilot-app/ ; https://github.blog/changelog/2026-05-06-enterprise-managed-plugins-in-github-copilot-cli-are-now-in-public-preview/
- claude_code_plugin: **partial / largely yes (officially evidenced in the maker's changelog, not in the docs pages)**. Repo changelog entries: reads `CLAUDE.md` and `.claude/CLAUDE.md` as instructions (docs: add-custom-instructions); `.claude/skills` is a documented skill location; `.claude/commands/` single-file commands supported (0.0.399, 2026-01-29); Claude-style `.mcp.json` without `mcpServers` wrapper (0.0.401, 2026-02-03); reads `extraKnownMarketplaces` from project `.claude/settings.json` "for Claude compatibility" (0.0.421, 2026-03-03); plugins using `.claude-plugin/plugin.json` discovered via `--plugin-dir` (1.0.6, 2026-03-16) and their MCP/LSP servers load (1.0.10, 2026-03-20); hook config files accept Claude Code's nested matcher/hooks structure and PascalCase event names (1.0.6); reads `.claude/settings.json` / `.claude/settings.local.json` as repo config (1.0.12, 2026-03-26); plugin hooks receive `CLAUDE_PLUGIN_ROOT`, `CLAUDE_PROJECT_DIR`, `CLAUDE_PLUGIN_DATA` (1.0.26 and 1.0.9-era); `.claude/agents` nested directories discovered (1.0.62, 2026-06-13); Claude-format plugin `preToolUse`/`permissionRequest` hooks fire with Claude tool names (1.0.62); `@`-imports in CLAUDE.md expanded (1.0.66). Limits: `~/.claude/` user-level agents/skills/commands are deliberately NOT loaded (1.0.35/1.0.36, 2026-04-23/24); hook event set is smaller than Claude Code's (third-party: https://cora7.com/blog/copilot-cli-plugin-portability/). No official docs page states "Claude Code plugin compatible" — evidence is changelog-only. Evidence: https://raw.githubusercontent.com/github/copilot-cli/main/changelog.md ; https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions (2026-08-21)
- subagents: **True** — built-in agents (Explore, Task, General-purpose, Code-review; also Plan, Research, Rubber duck, Critic per various posts) to which the main agent auto-delegates; custom agents (`.github/agents`, `~/.copilot/agents`, org/enterprise `.github-private`) usable as subagents; `/fleet` parallel orchestrator (all users since 0.0.411, 2026-02-17; blog 2026-04-01); `/subagents` picker for model/effort per agent; nesting depth default 4 (1.0.71); `/tasks` management; `/delegate` or `&` hands off to cloud Copilot coding agent. Evidence: https://docs.github.com/en/copilot/how-tos/copilot-cli/use-copilot-cli/invoke-custom-agents ; https://docs.github.com/en/copilot/concepts/agents/copilot-cli/fleet ; https://github.blog/ai-and-ml/github-copilot/run-multiple-agents-at-once-with-fleet-in-copilot-cli/ ; https://docs.github.com/en/copilot/how-tos/copilot-cli/use-copilot-cli/delegate-tasks-to-cca
- hooks: **True** — events `sessionStart`, `sessionEnd`, `userPromptSubmitted`, `preToolUse`, `postToolUse`, `errorOccurred`, `agentStop` (docs) plus `subagentStart`/`subagentStop`/`permissionRequest` per changelog; JSON files in `.github/hooks/` or `~/.copilot/hooks/`; preToolUse can deny (exit 2) and modify args; shell command handlers (bash / powershell keys). Evidence: https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/use-hooks ; changelog.md (2026-08-21)
- plan_mode: **True** — Shift+Tab toggles plan mode; since 1.0.71 (2026-07-16) plan mode hard-blocks built-in mutating tools; `/model plan` picks a plan-mode model (1.0.79); headless `--plan` + `--mode autopilot`. Plan mode first shipped 0.0.387 (2026-01-20). Evidence: https://docs.github.com/en/copilot/concepts/agents/about-copilot-cli ; changelog.md
- plugin_docs_url: https://docs.github.com/en/copilot/concepts/agents/copilot-cli/about-cli-plugins
- config_docs_url: https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/change-settings (settings in `~/.copilot/settings.json`; enterprise `managed-settings.json`)
- ACP support: **yes** — `copilot --acp` (stdio or `--port`), public preview since 2026-01-28; listed in Zed ACP registry. Evidence: https://github.blog/changelog/2026-01-28-acp-support-in-copilot-cli-is-now-in-public-preview/ ; https://docs.github.com/en/copilot/reference/copilot-cli-reference/acp-server
- SDK: **yes** — GitHub Copilot SDK (TypeScript, Python, Go, .NET, Java, Rust; MIT; JSON-RPC to the CLI process; CLI bundled for Node/Python/.NET), public preview 2026-04-02, GA 2026-06-02. Evidence: https://github.com/github/copilot-sdk ; https://github.blog/changelog/2026-06-02-copilot-sdk-is-now-generally-available/
- Other: LSP tool for code intelligence (experimental since 0.0.399); local sandbox (macOS Seatbelt, Linux bubblewrap, Windows Insiders) and cloud sandbox, both public preview; prompt scheduling `/every` `/after` (experimental); `/remote` control from other devices; voice input (GA 2026-06-02); `/rewind`; Copilot Memory across sessions.

## 4. Claimed differentiation (raw material)

- taglines: README: "The power of GitHub Copilot, now in your terminal." (https://github.com/github/copilot-cli). Product page: "Less // TODO: more done" (https://github.com/features/copilot/cli/). Repo description / npm: "brings the power of Copilot coding agent directly to your terminal".
- maker claims (paraphrased):
  1. GitHub-native agent: works directly with issues, PRs, branches via built-in GitHub MCP server; respects branch protections, required checks and org policies. (https://github.com/features/copilot/cli/)
  2. Same agentic runtime/harness as the Copilot coding agent and the Copilot SDK; "full agentic development environment" that plans, builds, reviews and remembers across sessions. (README; https://github.blog/changelog/2026-02-25-github-copilot-cli-is-now-generally-available/)
  3. Multi-model choice (Anthropic, OpenAI, Google) switchable mid-session with `/model`; BYOK providers. (product page; about-copilot-cli docs)
  4. Multi-agent: `/fleet` parallel subagents, custom agents, `/delegate` to cloud agent, `/remote` across devices. (product page; fleet blog)
  5. User control: every action previewed and approved; plan mode; sandboxing. (README; docs)
  6. Extensible via MCP, plugins (Agent Plugins 1.0 open standard), skills, hooks, custom agents. (GA post; Agent Plugins post)
  7. Included in all Copilot plans at no additional cost beyond AI credits. (product page; plans docs)
  8. Cross-platform (macOS, Linux, Windows) and many install paths; integrated with VS Code, JetBrains, Codespaces, Copilot app, GitHub Mobile notifications. (README; changelog posts)
- audience: "all Copilot plan subscribers (Free, Pro, Pro+, Max, Business, Enterprise)"; enterprise teams with admin enablement (https://github.com/features/copilot/cli/). README: developers working in the terminal; "still early in our journey" feedback invitation.

## 5. Company & contact targets (company-level only)

- legal name: GitHub, Inc.; HQ San Francisco, CA; subsidiary of Microsoft Corp. (acquired 2018, $7.5B); ~3,787 employees (Wikipedia figure, year unstated). Source: https://en.wikipedia.org/wiki/GitHub (2026-08-21)
- funding stage: n/a (Microsoft subsidiary). Since 2025-08 GitHub has no standalone CEO; reports into Microsoft CoreAI (Thomas Dohmke announced departure 2025-08-11 — Wikipedia; CoreAI reporting per press/secondary search results, not verified on a GitHub-owned page).
- publicly named leadership (https://github.com/about/leadership, 2026-08-21): Kyle Daigle — Chief Operating Officer (page says leads culture, developer outreach, operations, communications); Vladimir Fedorov — Chief Technology Officer; Mario Rodriguez — Chief Product Officer; Elizabeth Pemmerl — Chief Revenue Officer; Demetris Cheatham — Chief of Staff; Richard Paik — CFO; Shweta Vohra — Chief People Officer; Alexis Wales — CISO; Dave Green — Associate General Counsel.
- Copilot CLI bylines on GitHub blog: Matt Nigh — "Program Manager Director, I lead the AI for Everyone program at GitHub" (https://github.blog/author/mattnigh/) and Brian LaFlamme (title not stated; author page 404) — authors of the `/fleet` post (https://github.blog/ai-and-ml/github-copilot/run-multiple-agents-at-once-with-fleet-in-copilot-cli/, 2026-04-01); Jacklyn Carroll — author of custom-agents post 2026-06-09 (https://github.blog/ai-and-ml/github-copilot/from-one-off-prompts-to-workflows-how-to-use-custom-agents-in-github-copilot-cli/), title not stated on the page fetched.
- DevRel / partnerships lead: null (no GitHub-owned page naming a head of developer relations or partnerships was found in this pass).

## 6. Open questions / conflicts

- Existing census entry `first_released: "2023-01-06"` is the repo creation date (the 2023 "Copilot for CLI" technical preview, later the archived `gh copilot` extension). The current agentic Copilot CLI first shipped 2025-09-25 (public preview) and went GA 2026-02-25. Recommend first_released = 2025-09-25 with a note.
- Census `license: "Source Available"` / `source_available: True` looks wrong: the repo has no source code (README, LICENSE, changelog, install.sh only) and the npm package ships compiled per-platform binaries under a proprietary no-derivatives license. Recommend license = "Proprietary (GitHub Copilot CLI License)" and source_available = False.
- Census `model_providers: "Claude Sonnet 4.5, Claude Sonnet 4, GPT-5"` is stale (README at one time); current docs list Anthropic/OpenAI/Google models (Opus 5, Sonnet 5, GPT-5.6, Gemini 3.6 Flash, grok-4.5, kimi-k3, etc.) plus BYOK (OpenAI-compatible, Azure OpenAI, Anthropic, Ollama).
- Census `pricing: "...each prompt consumes one premium request"` is stale since 2026-06-01: billing is now token-based AI credits; CLI included in all plans including Free.
- Census `language: "Shell"` reflects only install.sh; the CLI binary's implementation language is not published.
- Census nulls to fill: stars 11,108; plugin_support True; claude_code_plugin partial; subagents True; hooks True; plan_mode True; plugin_docs_url/config_docs_url as in section 3; homepage https://github.com/features/copilot/cli/.
- Census `mcp_support: True` — correct but should be "client".
- Census `what_makes_it_special` mentions "LSP support" — LSP tool exists but is experimental-flag gated (changelog 0.0.399); minor.
- Conflict: GA changelog post (2026-02-25) said CLI is included with Pro/Pro+/Business/Enterprise, then an editor's note (2026-02-27) said all subscribers; current plans doc says all plans incl. Free include Copilot CLI.
- Conflict: InfoQ 2026-04-12 article describes "suggest"/"explain" features and a GitHub CLI dependency — those describe the old `gh copilot` extension, not the agentic CLI; treat that article as partly inaccurate.
- Unreachable: Visual Studio Magazine GA article (HTTP 403); mlq.ai earnings highlight (403); github.blog author page for Brian LaFlamme (404). Microsoft FY26 Q4 IR press release contains no GitHub-specific numbers; numbers come from the call transcript (fool.com).
- Microsoft has disclosed no CLI-specific user count; only "usage nearly doubling month over month" (2026-04-29). npm weekly downloads (1.46M) are inflated by SDK bundling and by CI installs; Homebrew 90d installs (64k) are the cleanest independent human-install proxy.
- Whether the CLI can act as an MCP *server*: docs silent; treat as no.
- Family-level "50 million users" (2026-07-29) vs "4.7 million paid subscribers" (2026-01-28): different metrics (total vs paid); no later paid-subscriber figure was disclosed in the Q3/Q4 calls found.

## 7. Sources

1. https://raw.githubusercontent.com/github/copilot-cli/main/README.md — tagline, install, features, models (stale)
2. https://raw.githubusercontent.com/github/copilot-cli/main/LICENSE.md — proprietary license terms
3. https://raw.githubusercontent.com/github/copilot-cli/main/changelog.md — version history, feature first-ship dates, Claude-compat entries
4. https://api.github.com/repos/github/copilot-cli — stars, forks, created_at, license
5. GitHub GraphQL/REST via gh — issues, PRs, discussions, contributors, commits, releases, copilot-sdk/gh-copilot/awesome-copilot/copilot-plugins repos
6. https://registry.npmjs.org/@github/copilot — versions, first publish date
7. https://api.npmjs.org/downloads/point/last-week/@github/copilot and last-month — downloads; also @github/copilot-sdk, @github/copilot-language-server
8. https://unpkg.com/@github/copilot@1.0.80/package.json — package contents (binary loader)
9. https://formulae.brew.sh/api/cask/copilot-cli.json and analytics/cask-install/90d.json — Homebrew installs
10. https://docs.github.com/en/copilot/concepts/agents/about-copilot-cli — overview, modes, billing, BYOK, ACP
11. https://docs.github.com/en/copilot/how-tos/use-copilot-agents/use-copilot-cli — section index, features
12. https://docs.github.com/en/copilot/concepts/agents/copilot-cli/about-cli-plugins — plugin system
13. https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/plugins-finding-installing — plugin commands
14. https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-skills — skills format/locations
15. https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/use-hooks — hook events/config
16. https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-mcp-servers — MCP client config
17. https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions — AGENTS.md/CLAUDE.md/GEMINI.md reading
18. https://docs.github.com/en/copilot/how-tos/copilot-cli/use-copilot-cli/invoke-custom-agents — built-in agents, agent locations, auto-delegation
19. https://docs.github.com/en/copilot/concepts/agents/copilot-cli/fleet — /fleet
20. https://docs.github.com/en/copilot/how-tos/copilot-cli/use-copilot-cli/delegate-tasks-to-cca — /delegate to cloud agent
21. https://docs.github.com/en/copilot/concepts/agents/copilot-cli/autopilot — autopilot mode
22. https://docs.github.com/en/copilot/concepts/about-cloud-and-local-sandboxes — sandboxing status
23. https://docs.github.com/en/copilot/reference/copilot-cli-reference/acp-server — ACP server reference
24. https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/change-settings — settings file
25. https://docs.github.com/en/copilot/get-started/plans — plan prices, credits, CLI inclusion
26. https://github.com/features/copilot/plans — plan page
27. https://github.com/features/copilot/cli/ — product page, tagline, claims
28. https://github.com/features/copilot — family-level claims, logos
29. https://github.com/about — platform numbers
30. https://github.com/about/leadership — leadership names/titles
31. https://github.blog/changelog/2025-09-25-github-copilot-cli-is-now-in-public-preview/ — preview launch
32. https://github.blog/changelog/2025-10-28-github-copilot-cli-use-custom-agents-and-delegate-to-copilot-coding-agent/ — custom agents, /delegate
33. https://github.blog/changelog/2026-01-14-github-copilot-cli-enhanced-agents-context-management-and-new-ways-to-install/ — built-in agents, installs
34. https://github.blog/changelog/2026-01-28-acp-support-in-copilot-cli-is-now-in-public-preview/ — ACP preview
35. https://github.blog/changelog/2026-02-25-github-copilot-cli-is-now-generally-available/ — GA
36. https://github.blog/changelog/2026-05-06-enterprise-managed-plugins-in-github-copilot-cli-are-now-in-public-preview/ — enterprise plugins
37. https://github.blog/changelog/2026-06-02-copilot-sdk-is-now-generally-available/ — SDK GA
38. https://github.blog/changelog/2026-06-02-introducing-copilot-cli-and-agentic-capabilities-enhancements-in-jetbrains-ides/ — CLI in JetBrains
39. https://github.blog/changelog/2026-06-02-copilot-cli-improved-ui-rubber-duck-prompt-scheduling-and-voice-input/ — Build 2026 features
40. https://github.blog/changelog/2026-06-23-copilot-cli-new-terminal-interface-is-generally-available/ — new TUI GA
41. https://github.blog/changelog/2026-08-12-agent-plugins-1-0-in-vs-code-copilot-cli-and-the-copilot-app/ — Agent Plugins 1.0
42. https://github.blog/changelog/2026-08-13-github-copilot-weekly-releases-august-10/ — latest weekly features
43. https://github.blog/ai-and-ml/github-copilot/run-multiple-agents-at-once-with-fleet-in-copilot-cli/ — /fleet blog, bylines
44. https://github.blog/ai-and-ml/github-copilot/from-one-off-prompts-to-workflows-how-to-use-custom-agents-in-github-copilot-cli/ — custom agents blog, byline
45. https://github.blog/author/mattnigh/ — author title
46. https://github.com/github/copilot-sdk/blob/main/README.md — SDK/CLI relationship
47. https://github.com/orgs/community/discussions/192963 — individual plan / AI-credit changes
48. https://www.fool.com/earnings/call-transcripts/2026/01/28/microsoft-msft-q2-2026-earnings-call-transcript/ — 4.7M paid subs
49. https://www.fool.com/earnings/call-transcripts/2026/04/29/microsoft-msft-q3-2026-earnings-transcript/ — 140k orgs, CLI usage doubling
50. https://www.fool.com/earnings/call-transcripts/2026/08/07/microsoft-msft-q4-2026-earnings-call-transcript/ — 50M users, 1-in-3 PRs
51. https://www.microsoft.com/en-us/investor/earnings/fy-2026-q4/press-release-webcast — no GitHub numbers
52. https://arxiv.org/abs/2607.01418 — Microsoft CLI-agent study
53. https://zed.dev/acp/agent/github-copilot — ACP registry listing
54. https://www.infoq.com/news/2026/04/github-copilot-cli-ga/ — press (partly inaccurate)
55. https://en.wikipedia.org/wiki/GitHub and https://en.wikipedia.org/wiki/GitHub_Copilot — company facts
56. https://cora7.com/blog/copilot-cli-plugin-portability/ — third-party Claude-plugin compatibility notes
57. Unreachable: https://visualstudiomagazine.com/articles/2026/03/02/github-copilot-cli-reaches-general-availability-bringing-agentic-coding-to-the-terminal.aspx (403); https://mlq.ai/earnings/highlight/MSFT-satya-nadella-highlights-booming-github-9591e9/ (403); https://github.blog/author/blaflamme/ (404)

## Inclusion check (Jesse's test)

Yes — Copilot CLI is a full coding agent with its own agentic loop: it plans, edits files, runs shell/tests, iterates until done (Autopilot), spawns subagents, and is the runtime the Copilot SDK and JetBrains agent wrap (README; GA post 2026-02-25; SDK README).
