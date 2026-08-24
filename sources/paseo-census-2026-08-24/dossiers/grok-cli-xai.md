# Dossier: Grok Build — xAI/SpaceXAI's coding agent (census mapping: grok-build)

Compiled 2026-08-24. Facts only. Null convention: "null = not researched"; "False/none = researched and absent". Sources [Sn] in section 7.

## Census mapping (read this first)

- Paseo's catalog entry "Grok" (command `grok agent stdio`, install link https://docs.x.ai/build/overview) is **Grok Build**, the official first-party coding agent from xAI/SpaceXAI — census entry **`grok-build`** (https://github.com/xai-org/grok-build). `grok agent stdio` is documented as "Run as an ACP agent over stdin/stdout" in the official CLI reference [S6][S7]; the repo contains a first-party ACP crate (`crates/codegen/xai-acp-lib`) [S10].
- The census entry **`grok-cli`** (superagent-ai/grok-cli) is a **different, third-party product**: an MIT-licensed TypeScript agent by Superagent AI that merely calls the xAI Grok API (npm `@vibe-kit/grok-cli`). It is NOT the subject of Paseo's "Grok" entry and should not be conflated with it [S11].
- Product naming: the maker calls the product "Grok Build"; the binary/CLI command is `grok`; the install page is x.ai/cli. "Grok CLI" is not the official name.

## 1. Identity

- name: **Grok Build** (CLI command `grok`)
- maker: **SpaceXAI LLC** (formerly X.AI Corp / xAI; company). xAI was acquired by SpaceX 2026-02-02 in an all-stock deal (xAI valued at $250B, combined $1.25T) and rebranded "SpaceXAI" in July 2026; it is a wholly owned subsidiary of SpaceX (SpaceX listed on Nasdaq as SPCX 2026-06-12). HQ: Stanford Research Park, Palo Alto, CA, USA [S14][S15]. The GitHub org remains `xai-org` and the docs/domains remain x.ai/docs.x.ai [S1][S2].
- product URL: https://x.ai/cli (403s to scripted fetchers; linked from README) [S3]; docs home https://docs.x.ai/build/overview [S2]
- repo URL: https://github.com/xai-org/grok-build [S1]
- license: **Apache-2.0** for first-party code; third-party components keep their own licenses [S1][S3] (as-of 2026-08-24)
- open source? **True** (since 2026-07-15). source_available: True — the full harness is published (~844,530 lines of Rust: agent loop, tools, TUI, extension system); code is synced one-way from the SpaceXAI monorepo by a bot and external contributions are not accepted per CONTRIBUTING.md [S3][S9][S13]. Some fetched-at-runtime pieces (models, service side) remain closed.
- first public release: **2026-05** — official launch post "Introducing Grok Build" dated 2026-05-25, early beta for SuperGrok and X Premium+ subscribers [S8]; press reported early testing for paying subscribers from mid-May 2026 [S12]. Open-sourced 2026-07-15 (repo created 2026-07-14T20:04Z; announcement "Grok Build is now open source" 2026-07-15) [S1][S9].
- latest release: **no tagged releases or versions on GitHub** (0 releases, 0 tags; continuous main-branch sync; last push 2026-08-23) [S1][S4]. Third-party coverage reports a "1.0 / leaves beta" milestone on 2026-08-07 [S16] — not verified against a first-party source (x.ai/build/changelog returns 403 [S17]). Census `current_release: 2026-08-19` appears to be a last-push date, not a version.
- what it is:
  - Form factors: terminal CLI with a fullscreen, mouse-interactive TUI; headless mode (`grok -p`, output formats plain/json/streaming-json) for scripts and CI; ACP agent mode (`grok agent stdio`, JSON-RPC over stdio) for IDE/tool embedding; `grok dashboard` (Agent Dashboard); related cloud product "Grok Bot" ("AI teammates on a cloud computer") is documented separately [S2][S6][S7].
  - Models: default is xAI's **grok-4.6** ("the same model that powers Grok Build", 500k context, $2-4/M input, $6-12/M output tiered); a **grok-build-0.1** coding model exists on the API (256k context, $1-2/M in, $2-4/M out); **BYO models supported** — any OpenAI-compatible endpoint via `[model.*]` blocks in `~/.grok/config.toml` (base_url + env_key), switchable with `/model` or `-m` [S2][S18].
  - Pricing: bundled with **SuperGrok** ($30/mo per Wikipedia-cited reporting) and **X Premium+** subscriptions (launch post: "available to SuperGrok and X Premium Plus subscribers"); alternatively API-key pay-as-you-go via the xAI API; no free tier indicated at launch [S8][S15]. Since open-sourcing, the harness itself can be compiled and pointed at your own inference [S9].
  - Install: `curl -fsSL https://x.ai/cli/install.sh | bash` (macOS/Linux), `irm https://x.ai/cli/install.ps1 | iex` (Windows), or build from source (Rust + DotSlash). No npm or Homebrew package found (researched, absent) [S2][S3][S19].
  - Default autonomy: **Ask** is the default permission mode ("Prompt for anything not already allowed"); other modes: Plan, Auto (classifier auto-approves safe tools), Always-approve; allow/deny rules in TOML; OS sandbox profiles are separate from permissions; dangerous patterns (`rm`, `git push`) still prompt under remembered grants [S5].
  - Language: Rust (GitHub API) [S1].

## 2. Adoption evidence

| metric / claim | value | as-of | source | type |
|---|---|---|---|---|
| GitHub stars | 25,990 | 2026-08-24 | [S1] | independently observable |
| GitHub forks | 4,880 | 2026-08-24 | [S1] | independently observable |
| GitHub watchers (subscribers) | 215 | 2026-08-24 | [S1] | independently observable |
| GitHub open issues | 0 (issues effectively not used; discussions disabled) | 2026-08-24 | [S1] | independently observable |
| Star velocity | 24,346 stars / 4,625 forks by 2026-08-07, ~3.5 weeks after code published | 2026-08-07 | [S16] | independently observable (third-party snapshot) |
| Commits, last 90 days | 36 (all since repo creation 2026-07-14; all by `grokkybara[bot]` monorepo sync — 1 contributor total) | 2026-08-24 | [S4] | independently observable |
| Commit cadence | last push 2026-08-23; sync commits continue ~weekly+ | 2026-08-24 | [S1][S4] | independently observable |
| Codebase size | ~844,530 lines of Rust (~3% vendored) | 2026-07-15 | [S13] | independently observable (Simon Willison) |
| GitHub releases / tags | 0 / 0 | 2026-08-24 | [S4] | independently observable |
| npm / Homebrew / crates.io packages | none found (binary installer only) | 2026-08-24 | [S19] | independently observable (absent) |
| Maker usage numbers (users, tokens, revenue for Grok Build) | none published in launch or open-source posts | 2026-08-24 | [S8][S9] | researched, absent |
| Grok (chatbot) user base | ~117M users, growth stalled (context, not Grok Build) | 2026-07 (late) | [S16] | third-party |
| xAI revenue | $3.2B revenue, -$6.4B operating income (2025) | 2025 FY | [S15] | press/Wikipedia-cited |
| Company events | SpaceX absorbed xAI at $1.25T combined (2026-02-02); SPCX IPO raised $75B (2026-06-12); Cursor (Anysphere) acquired for $60B in stock, closed 2026-08-14 | 2026-08-15 | [S14][S20] | press |
| Benchmark | grok-code-fast-1: 70.8% SWE-bench Verified, 256K context (model-level, cited in Grok Build coverage) | 2026-05-15 | [S12] | maker-claimed, relayed by press |
| Enterprise adoption signal | ETR survey: Claude/Gemini enterprise adoption climbing while "Grok usage has stalled in both consumer and enterprise segments" | 2026-05-15 | [S12] | third-party (ETR via DevOps.com) |
| Press coverage | DevOps.com launch analysis; Simon Willison on the open-sourced repo; AlternativeTo/Medium on the repo-upload backlash; Bloomberg/TechCrunch/CNBC/Engadget on Cursor deal | 2026-05..08 | [S12][S13][S21][S20] | press |
| Community: Discord/subreddit | none linked from README (researched, absent in README; not searched further) | 2026-08-24 | [S3] | absent/null |
| Notable incident driving attention | July 2026: Grok Build found uploading users' entire directories/repos (SSH keys, secrets) to xAI-controlled Google Cloud storage; xAI disabled the feature, switched default retention off (from 2026-07-12), said it deleted collected data, and open-sourced the harness | 2026-07-15 | [S13][S21] | independently observable (researcher reports) + maker response |

## 3. Plugin interface (six census fields)

- mcp_support: **client** — `grok mcp add|list|remove|doctor`; stdio and HTTP transports; OAuth handled automatically for remote servers (tokens in `~/.grok/mcp_credentials.json`); `${VAR}` expansion; project scope via `.grok/config.toml`; `/mcps` TUI tab. Also loads MCP configs from Claude Code's `~/.claude.json`/project `.mcp.json` and Cursor's `.cursor/mcp.json`. No MCP-server mode documented (researched, absent). Evidence: https://docs.x.ai/build/features/mcp-servers [S22]
- plugin_support: **True** — skills (`SKILL.md` with YAML frontmatter, in `./.grok/skills/`, `~/.grok/skills/`, plugin `skills/` dirs), plugins (`./.grok/plugins/`, `~/.grok/plugins/`, `--plugin-dir`), marketplaces (TUI Marketplace tab, `[[marketplace.sources]]`, `grok plugin marketplace add`), managed via a single extensions modal (`/plugins`, `/hooks`, `/skills`, `/mcps`). Evidence: https://docs.x.ai/build/features/skills-plugins-marketplaces [S23]
- claude_code_plugin: **yes** — docs: "Grok is fully compatible with Claude Code with zero configuration needed"; it "automatically reads Claude Code marketplaces, plugins, skills, MCPs, agents, hooks, and instruction files (`CLAUDE.md`, ..., `.claude/rules/`)"; also reads the AGENTS.md family and `~/.agents/skills|commands`; reads Claude `.claude/settings.json` hooks, `managed-settings.json` policy subset, and accepts Claude Code CLI flag aliases (`--allowedTools`, `--dangerously-skip-permissions`, etc.) [S23][S24][S25][S6]
- subagents: **True** — built-in `general-purpose`, `explore` (read-only), `plan`; custom types under `.grok/agents/` or `~/.grok/agents/`; personas as behavioral overlays; enabled by default; workflows "orchestrate a bounded set of subagents in the background"; sessions get git-worktree isolation (`grok worktree` command; `xai-fast-worktree` crate); press reports up to 8 parallel subagents (not confirmed in docs). Evidence: https://docs.x.ai/build/features/subagents [S26][S6][S12]
- hooks: **True** — events: SessionStart/End, UserPromptSubmit, PreToolUse (blocking), PostToolUse, PostToolUseFailure, PermissionDenied, Stop, StopFailure, Notification, SubagentStart/Stop, PreCompact/PostCompact; handlers: command (shell) and HTTP POST; JSON files in `~/.grok/hooks/` and `.grok/hooks/`; project hooks require `/hooks-trust`; also reads Claude Code and Cursor hook files. Evidence: https://docs.x.ai/build/features/hooks [S24]
- plan_mode: **True** — dedicated Plan mode: "only the session plan file can be edited until you approve"; plan preview UI with approve/request-changes/line comments; not skipped even under auto/always-approve; agent can enter plan mode on its own. Evidence: https://docs.x.ai/build/features/plan-mode [S5]
- plugin_docs_url: https://docs.x.ai/build/features/skills-plugins-marketplaces
- config_docs_url: https://docs.x.ai/build/settings (reference: https://docs.x.ai/build/settings/reference; enterprise layering: https://docs.x.ai/build/enterprise)
- ACP support: **yes, first-party** — `grok agent stdio` runs Grok as an ACP agent over JSON-RPC on stdin/stdout; documented with a Node.js client example; first-party `xai-acp-lib` crate in the repo [S7][S6][S10]
- SDK: no dedicated agent SDK found (researched, absent). Programmatic use = headless `-p` with json/streaming-json output, or ACP; the xAI API SDK (`xai_sdk`) exposes the underlying models, and the whole harness is Apache-2.0 source [S7][S2][S9]

## 4. Claimed differentiation (raw material for PRI-2927)

- tagline (docs, verbatim): "Grok Build is a powerful and extensible coding agent." — https://docs.x.ai/build/overview [S2]
- tagline (README): "terminal-based AI coding agent" that "understands your codebase, edits files, executes shell commands, searches the web, and manages long-running tasks" — https://github.com/xai-org/grok-build [S3]
- launch post: "a powerful new coding agent for professional software engineering and complex coding work" — https://x.ai/news/grok-build-cli [S8]
- maker claims (paraphrased):
  1. Plan-first workflow for complex tasks: start in plan mode, approve/comment/rewrite the plan before execution [S8][S5].
  2. Extensibility: skills, plugins, marketplaces, hooks, MCP servers, subagents managed from one extensions modal [S8][S23].
  3. Drop-in Claude Code compatibility: reads Claude Code plugins, marketplaces, skills, agents, hooks, MCP configs, CLAUDE.md, managed settings, and flag aliases with "zero configuration" [S23][S25].
  4. Three surfaces from one binary: interactive TUI (fullscreen, mouse), headless scripting/CI, ACP for IDE embedding [S2][S7].
  5. Open source as trust move: "Publishing the code is the most direct way to build toward a robust and reliable harness"; run it against your own inference [S9].
  6. Parallel background work: workflows fan out subagents; background tasks, `/loop`, `/deep-research`, git-worktree session isolation, Agent Dashboard [S6][S26].
  7. Best-model claim: grok-4.6 is "the most intelligent and fastest model we've built", recommended for code, same model powering Grok Build [S18][S2].
  8. Enterprise manageability: five-layer TOML config with fail-closed `requirements.toml` pinning, enterprise OIDC (Entra/Okta/Auth0), ZDR at team level, sandbox profile pinning [S25].
- audience: "professional software engineering and complex coding work" (launch post); SuperGrok / X Premium+ subscribers; enterprises via the enterprise deployment docs [S8][S25].

## 5. Company & contact targets (company-level only)

- legal name: SpaceXAI LLC (formerly X.AI Corp, 2023-2026); wholly owned subsidiary of SpaceX (Nasdaq: SPCX since 2026-06-12) [S15][S14]
- HQ: Stanford Research Park, Palo Alto, California, USA [S15]
- size: 1,200+ employees (2025, pre-merger xAI figure) [S15]
- funding stage: subsidiary of a public company; xAI valued at $250B in the 2026-02-02 SpaceX all-stock acquisition; SpaceX IPO raised $75B (2026-06-12); Cursor (Anysphere) acquired for $60B in stock, closed 2026-08-14 [S14][S15][S20]
- publicly named leadership:
  - Elon Musk — founder of xAI/SpaceXAI; CEO of SpaceX (named across company materials and press) [S15][S14]
  - Michael Nicolls — President, SpaceXAI (appointed 2026-04-10; previously VP of Starlink at SpaceX) [S15]
  - No named head of product / DevRel / partnerships for Grok Build found on x.ai (launch and open-source posts carry no bylines) — researched, absent [S8][S9]
- contact: enterprise path is the docs' enterprise deployment page; no partnerships contact page found (not researched further)

## 6. Open questions / conflicts

- **Census `grok-cli` conflation risk**: Paseo's "Grok" (`grok agent stdio`) is grok-build, not superagent-ai/grok-cli. The two entries describe unrelated products by different makers; grok-cli (3,432 stars, last push 2026-07-06, npm @vibe-kit/grok-cli at 1,235 weekly downloads as-of 2026-08-23) looks dormant and its census `maintained: "active"` is doubtful [S11][S19].
- Census `grok-build.first_released: "2026-07-14"` — that is the open-sourcing/repo-creation date. The product's public beta launch was announced 2026-05-25 (press: paid early access from ~2026-05-14) [S8][S12].
- Census `grok-build.current_release: "2026-08-19"` — repo has no releases/tags; value looks like a push date. Third-party "1.0 on 2026-08-07" is unverified (official changelog at x.ai/build/changelog returns 403) [S4][S16][S17].
- Census `stars: null` → 25,990; `homepage: null` → https://x.ai/cli; `plan_mode/subagents/claude_code_plugin: null` → all True/yes; `pricing: null` → SuperGrok / X Premium+ subscription or API key; `plugin_docs_url`/`config_docs_url: null` → filled in section 3 [S1][S5][S23][S8].
- Census `model_providers: "xAI/Grok models (implied)"` — imprecise: default grok-4.6, but custom/BYO OpenAI-compatible models are a documented first-class feature [S2].
- Census description says "SpaceXAI's..." — correct post-July-2026 rebrand, but confusing without context; maker field "xai-org" is the GitHub org, company is SpaceXAI LLC (SpaceX subsidiary) [S15].
- Underlying model confusion in press: DevOps.com (May 2026) says Grok Build runs grok-code-fast-1 at $0.20/M input; current docs say default grok-4.6 with grok-build-0.1 also on the API at $1-2/M input. Model lineup evidently changed between beta and now; the $0.20 figure does not match current pricing [S12][S18].
- DevOps.com also claims "standard npm installation with optional web UI" and "Arena Mode" — not corroborated by official docs (no npm package exists); treat as inaccurate or beta-era [S12][S19].
- Wikipedia's Grok article summary asserted Grok Build was "co-developed with Cursor" — plausible only after the 2026-08-14 Cursor closing and not corroborated elsewhere; treat as unverified [S15].
- July 2026 privacy incident: researcher reports of full-directory uploads (one figure circulating: "27,800x more data than necessary", via Wikipedia citation) preceded the open-sourcing; official open-source post does not mention the incident — the causal framing is press/community, the retention changes (default off from 2026-07-12, data deletion) are reported second-hand [S13][S21][S15][S9].
- Unreachable sources: https://x.ai/cli (Cloudflare 403 to fetchers), https://x.ai/build/changelog (403), https://docs.x.ai/build/features/mcp (404 — correct path is /build/features/mcp-servers).
- Parallel-subagent count ("up to 8") appears only in press, not in official docs [S12][S16].

## 7. Sources

1. [S1] https://api.github.com/repos/xai-org/grok-build — stars, forks, dates, license, language
2. [S2] https://docs.x.ai/build/overview — product definition, install, models, BYO config
3. [S3] https://raw.githubusercontent.com/xai-org/grok-build/main/README.md — tagline, install, license note, monorepo sync, no-contributions policy
4. [S4] https://api.github.com/repos/xai-org/grok-build/{releases,tags,commits,contributors} — 0 releases/tags, 36 commits, 1 bot contributor
5. [S5] https://docs.x.ai/build/features/permissions and /build/features/plan-mode (via docs.x.ai/llms.txt dump) — Ask default, mode table, plan mode details
6. [S6] https://docs.x.ai/build/cli/reference (via llms.txt) — `grok agent stdio`, `grok mcp/plugin/worktree/dashboard`, Claude flag aliases
7. [S7] https://docs.x.ai/build/cli/headless-scripting — `-p`, output formats, ACP section with Node example
8. [S8] https://x.ai/news/grok-build-cli — official launch post, 2026-05-25, availability, plan-mode quote
9. [S9] https://x.ai/news/grok-build-open-source — official open-sourcing post, 2026-07-15
10. [S10] Cargo.toml at raw.githubusercontent.com/xai-org/grok-build/main/Cargo.toml — Rust workspace incl. xai-acp-lib, xai-fast-worktree
11. [S11] https://api.github.com/repos/superagent-ai/grok-cli — third-party grok-cli stats
12. [S12] https://devops.com/xai-enters-the-coding-agent-race-with-grok-build/ — 2026-05-15 press: pricing, grok-code-fast-1, competitors, ETR data, analyst quote
13. [S13] https://simonwillison.net/2026/Jul/15/grok-build/ — codebase size 844,530 LoC, incident context, technical notes
14. [S14] Web search results: Motley Fool / Yahoo Finance / TechCrunch / CNBC / Bloomberg — SpaceX-xAI merger, SPCX IPO, Cursor acquisition dates and values
15. [S15] https://en.wikipedia.org/wiki/SpaceXAI and /wiki/Grok_(chatbot) — legal name, HQ, leadership, revenue, SuperGrok pricing, incident citation
16. [S16] https://pasqualepillitteri.it/en/news/10006/grok-build-1-0-xai-leaves-beta (via search snippet) — "1.0" 2026-08-07 claim, star snapshot, 117M users
17. [S17] https://x.ai/build/changelog — 403, unreachable
18. [S18] https://docs.x.ai/developers/models — grok-4.6 and grok-build-0.1 pricing/context
19. [S19] registry.npmjs.org (grok-build: 404; @vibe-kit/grok-cli downloads), formulae.brew.sh (grok/grok-build: 404) — package absence
20. [S20] https://techcrunch.com/2026/08/15/spacex-officially-closes-its-cursor-acquisition/ (via search) — Cursor closing
21. [S21] https://alternativeto.net/news/2026/7/xai-has-open-sourced-grok-build-after-backlash-over-secretly-uploading-users-repositories/ (via search) — incident and retention changes
22. [S22] https://docs.x.ai/build/features/mcp-servers (via llms.txt) — MCP client details, Claude/Cursor MCP compat
23. [S23] https://docs.x.ai/build/features/skills-plugins-marketplaces — skills/plugins/marketplaces, Claude Code compatibility quote
24. [S24] https://docs.x.ai/build/features/hooks — hook events, handlers, trust model, Claude/Cursor hook compat
25. [S25] https://docs.x.ai/build/enterprise — config layers, OIDC, ZDR, managed-settings.json compat
26. [S26] https://docs.x.ai/build/features/subagents and /build/modes-and-commands — subagent types, personas, workflows, slash commands

## Inclusion check (Jesse's test)

**Yes** — Grok Build is a first-party coding agent with its own agentic loop (the open-sourced Rust runtime implements context assembly, tool dispatch, edits, shell execution, and subagent orchestration); it is not a wrapper around another vendor's agent [S9][S13]. (Conversely, Paseo's use of it via `grok agent stdio` is just this same agent over ACP.)
