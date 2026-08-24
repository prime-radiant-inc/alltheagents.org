# Dossier: Amp (census_slug: amp)

Compiled 2026-08-21 (some API pulls timestamped 2026-08-22 UTC). Facts only. Null convention: "null = not researched"; "False/none = researched and absent". Each non-obvious fact carries a source [Sn] (see section 7) and an as-of date. Raw captures of ampcode.com pages (home, manual, manual/orbs, manual/appendix, models, pricing, security, news index) sit in raw/amp/ and were taken 2026-08-21 (news index ends with the 2026-08-21 "Explain Usage" post).

## 1. Identity

- name: Amp (product name; site tagline "Amp is the frontier agent") [S1][S2]
- maker: Amp Frontier Corporation (company). Spun out of Sourcegraph, Inc. on 2025-12-02; the ampcode.com post uses "Amp Frontier Corporation", the Sourcegraph blog and X posts use "Amp Inc." [S10][S11][S12]. Founded in San Francisco in 2025 per the Westpac media release [S14]. HQ country: USA. Current corporate home is ampcode.com; https://sourcegraph.com/amp now 301-redirects to https://ampcode.com (checked 2026-08-22) [S18].
- product URL: https://ampcode.com [S1]; docs ("Owner's Manual") https://ampcode.com/manual [S2]
- repo URL: none for the product — Amp is closed-source. Public GitHub org https://github.com/ampcode holds ancillary repos only (amp.nvim, amp-contrib, amp-examples-and-guides, homebrew-tap, cra-github, amp-sdk-demo) [S19] (as-of 2026-08-22).
- license: proprietary; npm package license field "SEE LICENSE IN LICENSE.md" [S16]. Ancillary repos (amp.nvim) Apache-2.0 [S19].
- open source? False. source_available: False for the agent/CLI (ships as a Bun-compiled single-file executable since 2026-05-14) [S17]; partial for SDKs/plugins/contrib repos.
- first public release: research preview started roughly early March 2025 (Thorsten Ball's 2025-05-15 post says the preview ran ~10 weeks before public availability; first "Raising an Agent" episode 2025-03-06; VS Code Marketplace release date 2025-04-02; first npm publish of @sourcegraph/amp 2025-04-11) [S20][S3][S21][S16]. Public availability without waitlist: 2025-05-15 [S20]. Full rebuild ("Amp Neo") rolled out 2026-05-06 and became "Amp" on 2026-05-27 [S22][S23].
- latest release: rolling builds; npm @ampcode/cli latest 0.0.1787371742-geb2e5c published 2026-08-22T04:16Z; three versions published 2026-08-21/22; 796 versions on @ampcode/cli since 2026-05-12, 4,035 on the old @sourcegraph/amp name since 2025-04-11 [S16] (as-of 2026-08-22). Latest news post 2026-08-21 "Explain Usage" [S3].
- what it is:
  - Form factors: terminal CLI/TUI (primary, `amp`); web app at ampcode.com (threads, remote control, settings); mobile/PWA; Slack (`@Amp`, since 2026-07-20); "orbs" = remote machines (e2b-hosted) running agents unattended; "runners" (`amp --no-tui`) on any machine; CLI connects to VS Code (incl. Cursor/Windsurf), Neovim (amp.nvim), Zed; JetBrains plugin deprecated; the standalone VS Code/Cursor editor extension was killed 2026-02-19 (self-destruct 2026-03-05) [S2][S3][S24][S25] (as-of 2026-08-21).
  - Models: multi-vendor, Amp-routed by "Dial" mode (low/medium/high/ultra) and role: main agent GLM-5.2 (low), GPT-5.6 Sol (medium/high), Claude Fable 5 (ultra); Oracle GPT-5.6 Sol / Fable 5; subagents on GPT-5.5, GPT-5.6 Terra/Sol/Luna, GLM-5.2, Gemini 3.7 Flash (media), GPT Realtime 2.1 (voice), GPT Image 2; optional "Agent Mode Plugins" for Kimi K3, Grok 4.6, Inkling (Thinking Machines), Fable 5, GLM 5.2 [S4] (as-of 2026-08-21). BYOK: removed 2025-05-08, re-introduced — manual documents own Anthropic key for Fable 5 and "bring your own keys" on the Unconstrained plan; also "link your ChatGPT subscription" or X Premium+/SuperGrok subscription for included GPT-5.6/Grok usage [S2][S5][S3].
  - Pricing: Megawatt $20/mo (750 orb hours, $20 included agent usage, low/medium modes, high with linked ChatGPT sub); Gigawatt $200/mo (1,000 hours of xxlarge orbs, $200 included usage, all modes incl. ultra); Education $10/mo; Unconstrained pay-as-you-go at provider API rates with zero markup for individuals/non-enterprise; Enterprise +50% with SSO, minimal data retention, managed settings, entered via one-time $1,000 purchase [S5][S2] (as-of 2026-08-21). Amp Free (ad-supported, $10/day) launched 2025-10-15, closed to new users 2026-02-10 [S26][S27].
  - Install: `curl -fsSL https://ampcode.com/install.sh | bash`; Windows `irm https://ampcode.com/install.ps1 | iex`; `brew install ampcode/tap/ampcode`; npm `@ampcode/cli` ("not recommended"; old name @sourcegraph/amp is an alias that was slated for removal 2026-06-15 but still receives publishes); web with no install [S2][S17][S16].
  - Default autonomy: "By default, Amp does not ask for approval before running tools" — permission prompts were removed in the 2026-05 rebuild; policy is implemented via plugins (tool.call event can reject), with a legacy-permissions internal plugin activated if `amp.permissions` settings exist [S2][S22] (as-of 2026-08-21).
  - Supported platforms: macOS, Linux, Windows via WSL [S2].

## 2. Adoption evidence

| metric / claim | value | as-of | source | type |
|---|---|---|---|---|
| npm weekly downloads, @ampcode/cli (current name) | 21,132 (2026-08-14..20) | 2026-08-20 | [S15] | independently observable |
| npm weekly downloads, @sourcegraph/amp (legacy alias, still published) | 16,923 (2026-08-14..20) | 2026-08-20 | [S15] | independently observable |
| npm monthly downloads, @ampcode/cli / @sourcegraph/amp | 89,942 / 110,532 (2026-07-22..08-20) | 2026-08-20 | [S15] | independently observable |
| npm weekly downloads, @ampcode/sdk / @sourcegraph/amp-sdk | 3,197 / 1,316 | 2026-08-20 | [S15] | independently observable |
| npm: caveat | npm is "not recommended"; primary install is curl/brew binary, so npm undercounts [S2][S17] | 2026-08-21 | [S2] | context |
| VS Code Marketplace installs, sourcegraph.amp ("Amp (Research Preview)") | 108,457 installs; 34 ratings avg 4.21; last updated 2026-05-25; extension product discontinued 2026-02-19 | 2026-08-22 | [S21][S25] | independently observable (legacy surface) |
| GitHub: product repo | none (closed source) | 2026-08-22 | [S19] | independently observable |
| GitHub stars, ampcode/amp.nvim | 200 stars, 14 forks (created 2025-09-11, pushed 2026-08-03) | 2026-08-22 | [S19] | independently observable |
| GitHub stars, ampcode/amp-contrib / amp-examples-and-guides | 72 / 54 | 2026-08-22 | [S19] | independently observable |
| GitHub stars, tao12345666333/amp-acp (third-party ACP wrapper) | 86 stars, 16 forks; created 2025-10-19; last push 2026-07-31; Apache-2.0; npm `amp-acp` 182 weekly / 613 monthly downloads | 2026-08-22 | [S28][S15] | independently observable |
| Homebrew | own tap ampcode/homebrew-tap (not in homebrew-core; no public analytics) | 2026-08-22 | [S19] | independently observable (no count) |
| Messages sent | 500,000 messages in ~first week after public launch | 2025-05-20 | [S29] | maker-claimed |
| Profitability | "Amp is profitable" at spinout; no revenue figure | 2025-12-02 | [S10][S11] | maker-claimed |
| Funding / valuation (Amp) | none disclosed; board investors Craft, Redpoint, Sequoia, Goldcrest, a16z sit on both Sourcegraph and Amp boards; Sourcegraph had raised ~$223M at $2.625B (2021) | 2025-12-02 | [S11][S12][S30] | maker-claimed (boards) / press |
| Mode adoption after default swap | medium mode carried two-thirds of new threads within a week; Dial modes 93% of new threads; 69% of users never changed the default | 2026-07-29 | [S31] | maker-claimed (relative shares only) |
| Public customers / partners | Westpac (Amp Labs Australia, announced 2026-07-29 / Westpac release 2026-08-07); no customer logos on homepage; homepage shows five user testimonials from X | 2026-08-21 | [S13][S14][S1] | maker-claimed + customer press release |
| Amp Labs | consulting-style "small teams" unit, paid in warrants, one customer per sector | 2026-05-21 | [S32] | maker-claimed |
| Community | "Amp Insiders" community (ampcode.com/insiders; size not public); X @AmpCode; YouTube; Discord referenced in 2025-05 post, not on current site | 2026-08-21 | [S1][S2][S29] | null (counts not obtainable) |
| Hacker News | spinout post 90 points / 37 comments | 2025-12 | [S33] | independently observable |
| Benchmark: Terminal-Bench 2.1 | no Amp entry on leaderboard | 2026-08-21 | [S34] | independently observable (absent) |
| Benchmark: SWE-bench | none found; Amp publishes own "model cards" (evals/caveats) instead | 2026-08-21 | [S4] | researched, absent |
| Press | Tessl (2025-12-03), HackerNoon, Finextra, Mirage News, Technology Decisions (Westpac deal, 2026-08) | 2026-08-21 | [S12][S35] | press |
| Users / paying customers / tokens / PRs | none disclosed by maker | 2026-08-21 | [S3] | researched, absent |

## 3. Plugin interface (PRI-2925)

- mcp_support: **client** — `amp mcp add <name> -- <cmd>` or `amp mcp add <name> <url>`; `amp.mcpServers` config with command/args/env or url/headers; OAuth for remote servers; MCP bundled in skills via mcp.json (lazy-loaded); `amp.mcpPermissions` rules; enterprise MCP registry allowlist; MCP servers connectable to orbs and Puck (2026-08-19). No MCP-server mode documented [S2][S6][S3]. Evidence: https://ampcode.com/manual#mcp
- plugin_support: **True** — TypeScript/JavaScript plugins (single file or directory) using `amp.on(...)` events, `amp.registerTool`, `amp.registerCommand`, `amp.registerSkill`, `ctx.ui.*`, `amp.ai.ask`; can define custom agent modes and custom subagents; loaded from personal/workspace git-backed "global plugin repositories", project `.amp/plugins/`, or `amp plugins add <url>`; shareable by URL; Agent Mode Plugins published as `@amp/...`. Skills: `SKILL.md` directories under `.agents/skills/`, `~/.config/agents/skills/`, personal/workspace skill repositories, `amp skill add <source>`; custom slash commands removed 2026-01-29 in favour of skills [S2][S4][S3] (as-of 2026-08-21). Evidence: https://ampcode.com/manual#plugins , https://ampcode.com/manual#agent-skills
- claude_code_plugin: **partial** — reads `.claude/skills/`, `~/.claude/skills/` and `~/.claude/plugins/cache/` as skill sources (toggle `amp.skills.disableClaudeCodeSkills`); stream-JSON output "tries to be compatible" with Claude Code's format; uses AGENTS.md (not CLAUDE.md); no support for Claude Code plugin manifests, hooks, commands or marketplaces documented [S2][S7] (as-of 2026-08-21).
- subagents: **True** — built-in subagents (Search, Oracle, Librarian, Review, Read Thread, GitHub, Painter) with their own models and context windows, spawned automatically ("mostly in medium mode"); plugins can define custom subagents and custom agents; agents can spawn other agents, message them and exchange files across threads (2026-07-17); Puck meta-agent [S2][S4][S3]. Evidence: https://ampcode.com/manual#subagents
- hooks: **True** — plugin events `session.start`, `tool.call` (approve/reject), `tool.result` (observe/modify), `agent.start`, `agent.end` (can continue the turn); no shell-script hook config, only plugin code [S2] (as-of 2026-08-21). Evidence: https://ampcode.com/manual#plugins
- plan_mode: **False** — no read-only/plan mode; modes are low/medium/high/ultra capability presets; prior "deep"/"smart"/"rush" modes retired; planning is done via prompts ("Plan how to ..., but don't write code yet") or the Oracle subagent [S2][S4][S8] (researched, absent).
- plugin_docs_url: https://ampcode.com/manual#plugins
- config_docs_url: https://ampcode.com/manual#configuration (settings, enterprise managed settings)
- ACP support: **no first-party**. The manual and SDK page do not mention the Agent Client Protocol [S2][S9]. Third-party adapter `tao12345666333/amp-acp` (npm `amp-acp`, Apache-2.0, by an individual GitHub user, not Amp) wraps the Amp CLI for Zed/Toad and claims a Zed ACP Registry listing; this is the wrapper Paseo uses [S28]. Amp's own Zed integration is its CLI-IDE bridge, not ACP [S2].
- SDK: **yes** — TypeScript `@ampcode/sdk` (renamed from @sourcegraph/amp-sdk 2026-05-14; launched 2025-10-01) and Python SDK (2025-12-10); streaming JSON (`--stream-json`, `--stream-json-input`) and `amp -x` execute mode for scripting; `AMP_API_KEY` for CI [S9][S3][S7][S17].
- Other: AGENTS.md hierarchy (project, ~/.config/amp, /etc/ampcode) [S2]; schedules (agents wake themselves) [S2]; orbs with OIDC, webhooks, portals [S8]; enterprise managed settings, entitlements, thread visibility [S7].

## 4. Claimed differentiation (raw material for PRI-2927)

- tagline (homepage, verbatim-short): "Amp is the frontier agent" — https://ampcode.com [S1]; manual "Why Amp?": Multi-Model / Opinionated / On the Frontier / Threads [S2]
- maker claims (paraphrased):
  1. Frontier-first: follows the models, deletes old workflows and legacy features; "no backcompat" [S1][S2].
  2. Opinionated curation: only features the team uses and loves; features are removed when they stop pulling weight (e.g., killed Tab completion, TODOs, Fork, editor extension) [S1][S3][S25].
  3. Multi-model routing per task and per subagent (GPT-5.6, Fable 5, GLM-5.2, Gemini, etc.); "Who cares about the model" — default swapped overnight with no complaints [S2][S4][S31].
  4. Orbs: remote machines that keep working after the laptop closes; threads resumable from web/terminal/phone; event-driven, scheduled, multiplayer orbs [S1][S8][S3].
  5. No approval prompts by default; policy via plugins instead of step-by-step approvals [S2][S22][S36].
  6. Extensible via TypeScript plugins "inspired by Pi" and shareable skills/plugins across a workspace [S1][S2].
  7. Subscriptions with generous included usage; zero markup on provider API pricing; link ChatGPT / X subscriptions for extra usage [S5][S36].
  8. Fast/responsive on very large threads; rebuild cut CPU 79% and idle memory 70% [S1][S22].
- audience: "people who want the most out of an agent, rather than keeping their old ways" [S1]; developers and teams who want to be "a year ahead" (Sourcegraph split post) [S11]; those willing to "travel light" (coding-agent-is-dead post) [S25]; enterprises (SSO, managed settings) and, via Amp Labs, traditional-economy companies such as banks [S2][S32].

## 5. Company & contact targets (PRI-2929) — company-level only

- legal name: Amp Frontier Corporation (ampcode.com, Westpac release); also referred to as "Amp Inc." (Sourcegraph blog, X) [S10][S11][S14]
- HQ: San Francisco, CA, USA (Westpac release: "Founded in San Francisco in 2025") [S14]; Amp Labs Australia entity in Sydney [S13][S14]
- size: 20 co-founders named at spinout; total headcount not published [S10]
- funding stage: spun out of Sourcegraph 2025-12-02; no standalone round disclosed; profitable per maker; board investors Craft, Redpoint, Sequoia, Goldcrest, a16z [S10][S11]
- publicly named leadership (only as named by the company / its partner's release):
  - Quinn Slack — co-founder and CEO, Amp Frontier Corporation (Westpac media release quote; Sourcegraph blog names him Amp founder) [S14][S11]
  - Beyang Liu — co-founder (Sourcegraph blog: "co-founders Quinn Slack and Beyang Liu launch Amp Inc."; no Amp title given) [S11][S10]
  - Thorsten Ball — co-founder (listed in the 20; bylines ampcode.com notes and podcast) [S10][S20]
  - Remaining 17 co-founders are listed by name at [S10] without titles; not reproduced here.
  - CTO / head of product / DevRel lead / partnerships lead: none named on ampcode.com (press kit names no people) [S37] — researched, absent.
- contact (company-level): press kit and support both point to amp-devs@ampcode.com (company mailbox); Enterprise purchasing via the same address; Trust Portal for SOC 2 reports [S37][S2][S38]
- Related entity: Sourcegraph, Inc. (Dan Adler CEO since 2025-12-02) — separate company [S11]

## 6. Open questions / conflicts

- Existing census `maker: null` — maker is Amp Frontier Corporation (spun out of Sourcegraph 2025-12-02) [S10][S11].
- Existing census `url: "https://sourcegraph.com/amp"` — that URL now 301-redirects to https://ampcode.com; product URL should be ampcode.com [S18].
- Existing census `platforms: ["CLI"]` — official surfaces also include web, mobile, Slack, orbs/runners, and CLI-IDE bridges for VS Code/Neovim/Zed; the standalone editor extension was discontinued 2026-02-19 [S2][S25].
- Existing census `first_released: null` / `current_release: null` — research preview ~2025-03; public 2025-05-15; rolling builds, latest 2026-08-22 [S20][S16].
- Existing census `claude_code_plugin: null` — partial (reads .claude/skills and ~/.claude/plugins/cache; no plugin/marketplace format) [S2].
- Existing census `plan_mode: null` — researched: no plan mode exists [S2][S4].
- Existing census `plugin_docs_url` / `config_docs_url: null` — https://ampcode.com/manual#plugins and https://ampcode.com/manual#configuration.
- Existing census `install_method` — also npm @ampcode/cli (not recommended) and Windows PowerShell installer [S2][S17].
- Existing census `model_providers` — lists Z.ai "GLM-5.2" (site writes "GLM-5.2"/"GLM 5.2"), and omits that the main-agent default is GPT-5.6 Sol; Gemini 3.7 Flash is used only for media; GPT Realtime/GPT Image also used [S4]. Minor.
- Existing census `pricing` — matches the pricing page; add "Unconstrained = API pricing, zero markup for individuals; Enterprise +50%, $1,000 entry" [S5][S2].
- Existing census `mcp_support: "yes (MCP in Orbs ...)"` — more precisely: MCP client in CLI/web since 2025 (streamable HTTP 2025-07-08); orbs/Puck support added 2026-08-19 [S3][S6].
- Existing census `hooks: "yes (plugins hook into events)"` — correct but note there is no separate hooks config; events are session.start/tool.call/tool.result/agent.start/agent.end [S2].
- Existing census `what_makes_it_special` mentions "bring-your-own-subscription 'Dial'" — the Dial is the low/medium/high/ultra mode selector; linking a ChatGPT/X subscription is a separate feature that changes routing ("A Dial for You", 2026-08-10) [S3][S4].
- Legal name inconsistency: "Amp Frontier Corporation" (ampcode.com, Westpac) vs "Amp Inc." (Sourcegraph blog, HN title) — likely the same entity; not verified against a corporate registry [S10][S11].
- npm alias: the 2026-05-14 post said @sourcegraph/amp would be removed 2026-06-15, but it is still being published daily and out-downloads the new name monthly [S17][S15][S16].
- The amp-acp README claims Amp is installable from Zed's ACP Registry; the registry repo could not be checked (GitHub API rate limit) [S28].
- Unreachable: hackernoon.com (403), finextra.com (403), ampcode.com/news/pave-the-road (404 under that slug), VS Code Marketplace HTML page (404 via fetch; API used instead), Amp Insiders member count, Discord size, Tracxn profile (not attempted, paywalled).
- No revenue, user, or token numbers have been published by Amp since the 500k-messages post (2025-05-20); "profitable" (2025-12-02) is the only financial claim [S29][S10].

## 7. Sources

1. [S1] https://ampcode.com — homepage tagline, claims, install, testimonials (raw/amp/home.txt, 2026-08-21)
2. [S2] https://ampcode.com/manual — Owner's Manual: Why Amp, install, modes, tools/permissions, skills, subagents, MCP, plugins/events, CLI, SDK, enterprise, pricing notes (raw/amp/manual.txt, 2026-08-21)
3. [S3] https://ampcode.com/news — news index with dated posts 2025-03-06..2026-08-21 (raw/amp/newslist.txt)
4. [S4] https://ampcode.com/models — Modes & Models routing table, subagent/system models, Agent Mode Plugins (raw/amp/models.txt)
5. [S5] https://ampcode.com/pricing — Megawatt/Gigawatt/Unconstrained/Education/Enterprise (raw/amp/pricing.txt)
6. [S6] https://ampcode.com/news/mcp-in-orbs — MCP in orbs/Puck 2026-08-19 (title/blurb from index)
7. [S7] https://ampcode.com/manual/appendix — stream JSON, Claude Code compatibility, entitlements, MCP registry allowlist (raw/amp/appendix.txt)
8. [S8] https://ampcode.com/manual/orbs — orbs sizes/prices, OIDC, webhooks, portals; LLM-facing principles (raw/amp/orbs.txt)
9. [S9] https://ampcode.com/manual/sdk — @ampcode/sdk, Python SDK, streaming, no ACP
10. [S10] https://ampcode.com/news/amp-inc (also reachable as /news/amp-frontier-corporation) — spinout, 20 co-founders, "profitable", 2025-12-02
11. [S11] https://sourcegraph.com/blog/why-sourcegraph-and-amp-are-becoming-independent-companies — Amp Inc., Dan Adler CEO Sourcegraph, boards, "less than 9 months" (via fetch + search)
12. [S12] https://tessl.io/blog/sourcegraph-spins-out-ai-coding-agent-amp-as-a-standalone-company — press recap 2025-12-03, Quinn Slack CEO, May 2025 launch
13. [S13] https://ampcode.com/news/amp-labs-westpac — Amp Labs x Westpac 2026-07-29
14. [S14] https://www.westpac.com.au/about-westpac/media/media-releases/2026/7-august/ — Westpac release 2026-08-07: Amp Frontier Corporation, founded SF 2025, Quinn Slack co-founder & CEO
15. [S15] https://api.npmjs.org/downloads/point/last-week|last-month/@ampcode/cli, @sourcegraph/amp, @ampcode/sdk, @sourcegraph/amp-sdk, amp-acp — download counts (2026-08-14..20 / 07-22..08-20)
16. [S16] https://registry.npmjs.org/@ampcode/cli and /@sourcegraph/amp — created/modified dates, version counts, license field, rename note
17. [S17] https://ampcode.com/news/npm-package-changes — 2026-05-14 rename to @ampcode/cli, Bun single-file executable (raw/amp/npmchanges.txt)
18. [S18] curl -I https://sourcegraph.com/amp — 301 to ampcode.com (2026-08-22)
19. [S19] https://api.github.com/orgs/ampcode/repos ; /repos/ampcode/amp.nvim ; /repos/ampcode/homebrew-tap — ancillary repos, stars, dates
20. [S20] https://ampcode.com/notes/how-i-use-amp — 2025-05-15, Thorsten Ball, waitlist gone, ~10-week preview
21. [S21] https://marketplace.visualstudio.com/_apis/public/gallery/extensionquery (sourcegraph.amp) — 108,457 installs, releaseDate 2025-04-02, lastUpdated 2026-05-25
22. [S22] https://ampcode.com/news/neo — "Amp, Rebuilt" 2026-05-06: plugins, no pre-approval, remote control, CPU/memory figures
23. [S23] https://ampcode.com/news/drop-the-neo — 2026-05-27 Neo becomes Amp
24. [S24] https://ampcode.com/news index entries: "Amp Is Now In Slack" 2026-07-20, "Agents, Everywhere" 2026-06-04, "Agents in Orbs" 2026-06-30 (raw/amp/newslist.txt)
25. [S25] https://ampcode.com/news/the-coding-agent-is-dead — 2026-02-19 editor extension removal, CLI focus, "travel light"
26. [S26] https://ampcode.com/news/amp-free — 2025-10-15 ad-supported free tier; https://ampcode.com/news/amp-free-frontier — 2026-01-08 $10/day
27. [S27] https://ampcode.com/news/amp-free-is-full-for-now — 2026-02-10 free tier closed to new users
28. [S28] https://api.github.com/repos/tao12345666333/amp-acp and its README (raw.githubusercontent.com) — third-party ACP adapter facts
29. [S29] https://ampcode.com/news/500k — 2025-05-20, 500,000 messages in ~a week
30. [S30] https://en.wikipedia.org/wiki/Sourcegraph — Sourcegraph funding history, founders, Amp spin-off mention
31. [S31] https://ampcode.com/news/who-cares-about-the-model — 2026-07-29 default swap, mode share percentages
32. [S32] https://ampcode.com/news/amp-labs — 2026-05-21 Amp Labs model
33. [S33] https://news.ycombinator.com/item?id=46124649 — HN thread points/comments
34. [S34] https://www.tbench.ai/leaderboard/terminal-bench/2.1 — no Amp row
35. [S35] web search results (Mirage News, Technology Decisions, Finextra, MarketScreener) — Westpac deal press; Finextra/HackerNoon 403 on fetch
36. [S36] https://ampcode.com/news/subscriptions — 2026-07-18 subscription launch, positioning vs approval workflows
37. [S37] https://ampcode.com/press-kit — boilerplate "independent agent research lab", no names, press mailbox
38. [S38] https://ampcode.com/security — SOC 2 Type II, provider list (Anthropic, OpenAI, SpaceXAI, Meta, GCP, Bedrock, Baseten, Fireworks, e2b, ...) (raw/amp/security.txt)
39. https://x.com/sqs/status/1995923843391574436 (via search snippet) — "Amp Inc., an independent research lab"
40. https://www.producthunt.com/products/amp-free ; https://medium.com/@jonathanaraney/the-future-of-coding-is-here-f1cbb2c3c77d (search snippets) — May 2025 research-preview framing, not relied on

## Inclusion check (Jesse's test)

**Yes** — Amp is a first-party agent with its own agentic loop (runs tools and shell without approval, spawns its own subagents, routes across multiple vendors' models, runs unattended in orbs); the ACP adapter Paseo uses (tao12345666333/amp-acp) is a thin third-party wrapper around the Amp CLI and would itself be a "no" [S2][S28].
