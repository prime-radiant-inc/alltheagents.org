# Dossier: OpenCode (census_slug: opencode)

Researched 2026-08-21. Facts only; every non-obvious fact carries a source URL and as-of date.
Null convention: "null = not researched"; "False/none = researched and absent".
Name collision: the unrelated Charm "opencode" (now Crush) is excluded; see section 6.

## 1. Identity

- name: OpenCode
- maker: Anomaly (GitHub org `anomalyco`, display name "Anomaly"; company referred to in
  third-party registries as "Anomaly Innovations"); org form: company; HQ country: Canada
  (Toronto) per the company's Y Combinator profile (https://www.ycombinator.com/companies/opencode,
  as of 2026-08-21). The team was publicly known as "SST" until a 2026-01-02 rebrand under the
  Anomaly name (https://x.com/thdxr/status/2007199285251842478, tweet ID date 2026-01-02;
  confirmed by GitHub org redirect sst/opencode -> anomalyco/opencode, as of 2026-08-21).
- product URL: https://opencode.ai
- repo URL: https://github.com/anomalyco/opencode (older URL https://github.com/sst/opencode
  now redirects; GitHub API returns "Moved Permanently" for sst/opencode, 2026-08-21)
- license: MIT (GitHub API `license.spdx_id` = MIT, 2026-08-21)
- open source?: source_available: True — the full client (TUI, desktop, web UI, server, SDK,
  plugin API, GitHub action) is in the MIT repo. The hosted paid offerings (Zen gateway, Go
  subscription, Black, Enterprise) are services, not code in the repo
  (https://opencode.ai/docs/zen/, https://opencode.ai/docs/go/, 2026-08-21).
- first public release: repo created 2025-04-30 (GitHub API `created_at`); earliest GitHub
  release tag 0.0.45 published 2025-05-14 (https://github.com/anomalyco/opencode/releases/tag/0.0.45);
  first npm publish of `opencode-ai` 2025-05-31 (https://registry.npmjs.org/opencode-ai `time.created`);
  maker/press-stated public launch date 2025-06-19 (TFN interview with the CEO,
  https://techfundingnews.com/opencode-the-background-story-on-the-most-popular-open-source-coding-agent-in-the-world/,
  2026-01-13). Existing census value 2025-04-30 is the repo-creation date.
- latest release: v1.18.21, published 2026-08-21T14:51Z
  (https://github.com/anomalyco/opencode/releases/tag/v1.18.21; changelog
  https://opencode.ai/changelog, 2026-08-21). npm `latest` dist-tag = 1.18.21 (2026-08-21).
- what it is:
  - Form factors: terminal UI (default `opencode`), non-interactive CLI (`opencode run`),
    headless HTTP server (`opencode serve`, OpenAPI 3.1 at /doc), local web UI
    (`opencode web`), desktop app for macOS/Windows/Linux (marked BETA), IDE extension
    (VS Code/Cursor/Windsurf/VSCodium; launches TUI in split terminal), ACP subprocess
    (`opencode acp`) for Zed/JetBrains/Neovim, and a GitHub App + Actions workflow triggered by
    `/opencode` or `/oc` comments (https://opencode.ai/docs/cli/, /docs/server/, /docs/web/,
    /docs/ide/, /docs/acp/, /docs/github/, README, all 2026-08-21).
  - Models: BYO / any provider — "75+ LLM providers" via the Vercel AI SDK + Models.dev,
    including local models (Ollama, LM Studio, llama.cpp); OAuth login with existing
    Claude Pro/Max, ChatGPT Plus/Pro, GitHub Copilot subscriptions; plus maker-run paid
    gateway "Zen" and "Go" subscription (https://opencode.ai/docs/providers/, 2026-08-21).
  - Pricing model: software is free/MIT. Optional paid: Zen = pay-as-you-go per token,
    credits auto-reload $20 when below $5, up to $30/M input tokens for the top model
    (https://opencode.ai/docs/zen/); Go = $5 first month then $10/month for 23+ open-weight
    models with $12/5h, $30/week, $60/month usage caps (https://opencode.ai/docs/go/);
    Black = "enrollment temporarily paused" (https://opencode.ai/black); Enterprise =
    per-seat licensing, quote via sales (https://opencode.ai/docs/enterprise/). All 2026-08-21.
  - Install: `curl -fsSL https://opencode.ai/install | bash`; npm/bun/pnpm/yarn `-g opencode-ai`;
    Homebrew `opencode` formula and cask for desktop; Scoop, Chocolatey, pacman/AUR, mise, Nix,
    Docker; desktop DMG/EXE/deb/rpm/AppImage (README + https://opencode.ai/docs/, 2026-08-21).
  - Default autonomy: in the default "build" agent most permissions default to "allow"
    (read, edit, bash, glob, grep, skill, lsp, websearch); only `doom_loop` and
    `external_directory` default to "ask"; `.env` files are blocked; `--auto` approves anything
    not explicitly denied. The "plan" agent sets edit and bash to "ask"
    (https://opencode.ai/docs/permissions/, https://opencode.ai/docs/agents/, 2026-08-21).
    Note: README says the plan agent "denies file edits by default"; docs/agents says "ask" —
    see section 6.

## 2. Adoption evidence

Legend: [IO] independently observable; [MC] maker-claimed; [3P] third-party reported.

GitHub (https://api.github.com/repos/anomalyco/opencode, 2026-08-21) [IO]:
- stars | 199,960 | 2026-08-21
- forks | 25,823 | 2026-08-21
- open issues+PRs (`open_issues_count`) | 5,307 | 2026-08-21
- watchers (`subscribers_count`) | 771 | 2026-08-21
- contributors | 456 GitHub-account contributors; 1,001+ incl. anonymous (API Link-header
  page counts); 981 "mentionable users" (GraphQL) | 2026-08-21
- total commits (default branch `dev`) | ~15,510 (API pagination count) | 2026-08-21
- commits in last 90 days (since 2026-05-23) | ~2,181 | 2026-08-21
- total PRs 18,981; merged PRs 7,501; total issues 24,348 (GraphQL + search API) | 2026-08-21
- GitHub releases | ~863 (8 full pages of 100 + 63) | 2026-08-21
- GitHub Discussions | 0 (feature not used) | 2026-08-21
- Third-party star comparison: 193,678 stars, listed as the most-starred open-source
  coding agent ahead of Claude Code, Gemini CLI, Codex
  (https://www.morphllm.com/ai-coding-agent, as of page crawl 2026-08) [3P]

Package downloads [IO]:
- npm `opencode-ai` weekly | 1,728,914 | 2026-08-13..19 | https://api.npmjs.org/downloads/point/last-week/opencode-ai
- npm `opencode-ai` 30-day | 9,254,863 | 2026-07-21..08-19 | https://api.npmjs.org/downloads/point/last-month/opencode-ai
- npm `opencode-ai` monthly history (range API): 2025-06 42.5k; 2025-09 126.6k; 2025-12 433k;
  2026-01 1.24M; 2026-03 2.50M; 2026-04 4.99M; 2026-05 5.92M; 2026-06 9.01M; 2026-07 8.56M;
  2026-08 (1-19) 5.82M | https://api.npmjs.org/downloads/range/2025-06-01:2026-08-19/opencode-ai
- npm `@opencode-ai/sdk` weekly 10,629,975; `@opencode-ai/plugin` weekly 9,662,635
  (2026-08-13..19) — these are library packages also pulled as dependencies, so they
  overstate end-user installs
- Homebrew formula `opencode` installs | 30d 36,122; 90d 113,774; 365d 344,056 | 2026-08-21 |
  https://formulae.brew.sh/api/formula/opencode.json
- VS Code Marketplace `sst-dev.opencode` | 1,015,447 installs, avg rating 3.69 (16 ratings),
  v0.0.13 last updated 2025-12-28 | 2026-08-21 | https://marketplace.visualstudio.com/items?itemName=sst-dev.opencode
- VS Code Marketplace `sst-dev.opencode-v2` ("OpenCode Beta") | 46,242 installs | 2026-08-21
- Open VSX `sst-dev/opencode` | 494,690 downloads | 2026-08-21 | https://open-vsx.org/api/sst-dev/opencode

Maker-stated usage [MC]:
- "over 16M developers every month"; "over 195,000 GitHub stars, 950 contributors, and
  over 13,000 commits" | https://opencode.ai/ | 2026-08-21
- 650,000 monthly active users, 50,000 stars, 500 contributors "in five months since
  launch"; "several million dollars in annualized revenue" via Zen (CEO interview) |
  https://techfundingnews.com/opencode-the-background-story-on-the-most-popular-open-source-coding-agent-in-the-world/ | 2026-01-13
- ~8M MAU and 162k+ stars by May 2026; 7.5M MAU, 160k+ stars, 900 contributors by June 2026
  (secondary write-ups citing the maker; not independently verifiable) |
  https://ai.sulat.com/how-opencode-went-from-zero-to-titan-in-eight-months-dcdcd8ff5572 (403 on direct fetch; figures via search snippet) [3P/MC]

Public customers / case studies:
- Cloudflare: CEO interview names Cloudflare as an enterprise user (TFN, 2026-01-13) [MC];
  Cloudflare's own engineering blog (2026-04-20) lists OpenCode among its internal engineer
  coding tools and reports 27.08M OpenCode messages in 30 days, 688,460 requests/day and
  10.57B tokens/day through its AI Gateway, across 3,683 internal users of AI coding tools
  (https://blog.cloudflare.com/internal-ai-engineering-stack/) [IO]. Cloudflare also
  publishes an official OpenCode setup guide (https://developers.cloudflare.com/agent-setup/opencode/) [IO].
- No customer logos on opencode.ai homepage or /enterprise page (2026-08-21) [IO].

Funding / company:
- Y Combinator W21 (as SST/Serverless Stack); YC company page for "OpenCode" lists
  team size 24, Toronto, founded 2010 (https://www.ycombinator.com/companies/opencode, 2026-08-21) [IO]
- Backers named on the company's own SST about page: Reid Hoffman, Max Levchin, Steve Chen,
  Russ Simmons, SV Angel, Y Combinator (https://sst.dev/about/, 2026-08-21) [MC]
- Tracxn (via search snippet): Anomaly Innovations raised $1.63M over 3 rounds, latest a
  $1M seed on 2021-07-23; OpenCode entity "has not raised any funding" [3P]
- CEO interview: "raised an undisclosed funding round within months of launching" OpenCode
  (TFN, 2026-01-13) [MC] — amount/investors not public
- The widely indexed "Anomaly raises $17M (Sound Ventures, May 2026)" is a DIFFERENT company
  (Anomaly Insights, healthcare payer intelligence; https://www.businesswire.com/news/home/20260513966755/en/) — not OpenCode.
- Valuation / acquisition: none found.

Community:
- Discord "OpenCode" server | 77,273 members, 9,443 online | 2026-08-21 |
  https://discord.com/api/v10/invites/opencode?with_counts=true (invite https://opencode.ai/discord) [IO]
- Subreddit r/opencode: not reachable from this environment (Reddit API blocked) — null
- GitHub issues 24,348 total; Discussions disabled (2026-08-21) [IO]

Third-party signals:
- Benchmarks: no OpenCode-specific SWE-bench/Terminal-bench placement; third-party trackers
  note scores are model-dependent and none published for the harness
  (https://www.morphllm.com/ai-coding-agent; https://github.com/TheLime1/harness-bench) [3P]
- Press: Tech Funding News CEO profile 2026-01-13 (above); Cloudflare engineering blog
  2026-04-20 (above). No TechCrunch/Verge/Bloomberg coverage found for OpenCode specifically
  (WebSearch 2026-08-21).
- Ecosystem: third-party Claude-Code-compat layers (e.g. oh-my-opencode), multi-harness
  plugin marketplaces listing OpenCode as a target (https://github.com/wshobson/agents) [3P]

## 3. Plugin interface (census fields)

- mcp_support: **client** (not server). Local (stdio command) and remote (HTTP URL) MCP
  servers configured under `mcp` in opencode.json; OAuth with dynamic client registration
  handled automatically; `opencode mcp auth <name>`; no documented mode in which OpenCode
  itself serves MCP. https://opencode.ai/docs/mcp-servers/ (2026-08-21)
- plugin_support: **True** — JS/TS plugin modules loaded from `~/.config/opencode/plugins/`,
  `.opencode/plugins/`, or npm packages listed under `"plugin"` in config (installed via Bun);
  plugins receive `{project, directory, worktree, client, $}` and return event hooks; can
  register custom tools (Zod schemas; plugin tools override built-ins of same name).
  No official marketplace/registry. https://opencode.ai/docs/plugins/ (2026-08-21).
  Also: skills (SKILL.md) from `.opencode/skills/`, `~/.config/opencode/skills/`,
  `.claude/skills/`, `~/.claude/skills/`, `.agents/skills/` (https://opencode.ai/docs/skills/);
  custom slash commands as markdown in `.opencode/commands/` (https://opencode.ai/docs/commands/);
  custom agents as markdown in `.opencode/agents/` (https://opencode.ai/docs/agents/).
- claude_code_plugin: **partial** — reads `CLAUDE.md` (project, fallback after AGENTS.md) and
  `~/.claude/CLAUDE.md`, and Claude-format skills from `.claude/skills/` and `~/.claude/skills/`;
  opt-out via `OPENCODE_DISABLE_CLAUDE_CODE=1` (+ `_PROMPT`, `_SKILLS` variants).
  Official docs do NOT document reading `.claude/commands/`, `.claude/agents/`, Claude hooks,
  or the `.claude-plugin` marketplace format (third-party plugins such as oh-my-opencode add
  that). https://opencode.ai/docs/rules/, https://opencode.ai/docs/skills/ (2026-08-21)
- subagents: **True** — built-in subagents `general`, `explore`, `scout`; invoked by
  `@name` mention or automatically via the Task tool; custom agents definable in JSON or
  markdown with per-agent model/prompt/permissions; `subagent_depth` config key; changelog
  v1.18.20 mentions resumable subagent failures with `task_id`.
  https://opencode.ai/docs/agents/, https://opencode.ai/docs/config/ (2026-08-21)
- hooks: **via plugin API only** (no user-level shell-command hook config). Plugin events
  include `tool.execute.before`, `tool.execute.after`, `session.created/idle/compacted/error`,
  `permission.asked/replied`, `file.edited`, `command.executed`, `message.updated`,
  `shell.env`, `tui.*`. A native shell-hooks feature is an open feature request
  (https://github.com/anomalyco/opencode/issues/14863) and is served by third-party plugins
  (e.g. https://github.com/KristjanPikhof/OpenCode-Hooks). https://opencode.ai/docs/plugins/ (2026-08-21)
- plan_mode: **True** — built-in primary agent `plan` (edit and bash set to "ask"); switch
  with Tab. https://opencode.ai/docs/agents/ (2026-08-21)
- plugin_docs_url: https://opencode.ai/docs/plugins/
- config_docs_url: https://opencode.ai/docs/config/
- ACP support: **yes** — `opencode acp` (JSON-RPC over stdio); documented for Zed, JetBrains,
  Avante.nvim, CodeCompanion.nvim; `/undo` `/redo` unsupported over ACP. https://opencode.ai/docs/acp/ (2026-08-21)
- SDK: **yes** — `@opencode-ai/sdk` (JS/TS) over the HTTP server (`createOpencode()` /
  `createOpencodeClient()`, default http://localhost:4096); server exposes OpenAPI 3.1 at
  `/doc` and SSE `/event`. https://opencode.ai/docs/sdk/, https://opencode.ai/docs/server/ (2026-08-21)

## 4. Claimed differentiation

- tagline: "The open source AI coding agent" — https://opencode.ai/ and README (2026-08-21);
  GitHub description "The open source coding agent."
- maker claims (paraphrased):
  1. Open source (MIT), usable from terminal, IDE, or desktop — https://opencode.ai/
  2. Provider-agnostic: "75+ LLM providers" via Models.dev, including local models; free
     models included; log in with existing Claude/ChatGPT/Copilot subscriptions —
     https://opencode.ai/, https://opencode.ai/docs/providers/
  3. Privacy: "does not store any of your code or context data"; suitable for privacy-sensitive
     and on-prem environments — https://opencode.ai/, https://opencode.ai/docs/enterprise/
  4. LSP-enabled: automatically loads the right language servers for the model — https://opencode.ai/
  5. Client/server architecture: TUI is a client of a headless server; multi-session,
     shareable session links, remote attach, web UI — https://opencode.ai/, https://opencode.ai/docs/server/
  6. Zen: a "handpicked", tested and benchmarked set of models for coding agents, "zero
     markups" pay-as-you-go — https://opencode.ai/zen, https://opencode.ai/docs/zen/
  7. Go: low-cost open-model subscription ($10/month) with "generous limits" — https://opencode.ai/go
  8. Built-in build/plan agents and subagents; plan agent for exploring unfamiliar codebases —
     README
  - CEO framing (interview, not official materials): "not an AI product" but a product
    designed to use any AI; zero-friction onboarding without sign-up — TFN 2026-01-13
- audience: developers generally ("helps you write code in your terminal, IDE, or desktop");
  Go: "programmers around the world" needing affordable models (https://opencode.ai/go);
  Enterprise: organizations needing code/data to stay on-prem with SSO and internal AI
  gateways (https://opencode.ai/docs/enterprise/). All 2026-08-21.

## 5. Company & contact targets (company-level only)

- company legal/operating name: Anomaly (GitHub org `anomalyco`, "© 2026 Anomaly" site
  footer, https://anoma.ly); third-party registries and the YC page reference "Anomaly
  Innovations"; previously traded publicly as SST / Serverless Stack
- HQ: Toronto, Canada (https://www.ycombinator.com/companies/opencode, 2026-08-21)
- approx size: team size 24 (YC page, 2026-08-21)
- funding stage: YC W21 + angel/seed (see section 2); undisclosed later round claimed by CEO
- publicly named leadership (only as named by the company or in its own interviews/pages):
  - Jay V — CEO / Founder (https://www.ycombinator.com/companies/opencode "Founder at Anomaly";
    CEO per https://techfundingnews.com/opencode-the-background-story-on-the-most-popular-open-source-coding-agent-in-the-world/)
  - Frank Wang — CTO / Founder (same two URLs)
  - Dax Raad — co-founder (TFN interview; announced the Anomaly rebrand at
    https://x.com/thdxr/status/2007199285251842478)
  - Adam Elmore — co-founder (TFN interview)
  - Head of product / DevRel / partnerships: none publicly named (anoma.ly has no team page;
    opencode.ai has no team page) — researched and absent
- company contact surfaces: enterprise contact form at https://opencode.ai/enterprise;
  partnership "Talk to our team" link on https://anoma.ly (2026-08-21). No personal contacts collected.

## 6. Open questions / conflicts

- Name collision: the Charm-authored Go "opencode" (repo opencode-ai/opencode, 13.7k stars)
  was archived 2025-09-18 and continues as charmbracelet/crush (27.6k stars). It is unrelated
  to Anomaly's TypeScript OpenCode and must not be merged into this entry
  (https://github.com/opencode-ai/opencode, https://github.com/charmbracelet/crush, 2026-08-21).
- Funding: the "$17M Anomaly / Sound Ventures" (May 2026) and Tracxn "$34M total" results
  belong to Anomaly Insights (healthcare), not to this company. The CEO says OpenCode raised an
  undisclosed round after launch; amount/investors unverified.
- Plan-agent behavior: README says plan "denies file edits by default"; docs/agents says edit
  and bash are "ask". Treat as "plan = no edits without confirmation".
- Contributors: GitHub API gives 456 account contributors (1,001+ incl. anonymous) vs the
  homepage's "950 contributors" and the census text "15k+ commits" vs homepage "13,000+".
- "16M developers every month" is maker-claimed and not verifiable; npm weekly installs
  (1.73M) and Homebrew/VS Code installs are the observable proxies.
- Unreachable sources: techfundingnews.com and finsmes.com and crunchbase.com return 403 to
  WebFetch (TFN was read via curl); ai.sulat.com 403; Reddit API blocked; opencode.ai/blog
  does not exist (404) — no official launch blog post found; the launch date 2025-06-19 comes
  from the CEO interview and secondary write-ups.
- Existing census entry (scratchpad/hc/agents/opencode.md) vs findings:
  - `first_released: 2025-04-30` = repo creation date; first release tag 2025-05-14; public
    launch 2025-06-19.
  - `current_release: 2026-08-20` — latest is v1.18.21 on 2026-08-21.
  - `stars: null` — 199,960 on 2026-08-21.
  - `platforms: [CLI]` — also desktop app, IDE extension, web UI, ACP, GitHub Action.
  - `hooks: null` — plugin-API event hooks exist; no native shell hooks.
  - `claude_code_plugin: False` — partial (CLAUDE.md and .claude/skills are read).
  - `plugin_docs_url: null` -> https://opencode.ai/docs/plugins/; `config_docs_url: null` ->
    https://opencode.ai/docs/config/.
  - `pricing: "Free / open-source (MIT)"` — omits paid Zen (PAYG), Go ($10/mo), Enterprise
    (per seat).
  - `what_makes_it_special`: "the plan agent is read-only, denies file edits" — docs say
    "ask"; "Major project (199k stars, 15k+ commits)" matches API counts but not the homepage.
  - `maker: anomalyco` is the GitHub handle; company name is Anomaly.

## 7. Sources

1. https://api.github.com/repos/anomalyco/opencode — stars, forks, license, dates (2026-08-21)
2. https://api.github.com/repos/anomalyco/opencode/releases — release count, first/latest tags
3. https://api.github.com/repos/anomalyco/opencode/contributors / commits — contributor and commit counts via pagination
4. GitHub GraphQL (anomalyco/opencode) — PR/issue/discussion totals
5. https://api.github.com/search/issues?q=repo:anomalyco/opencode+is:pr+is:merged — merged PRs
6. https://api.github.com/repos/sst/opencode — redirect confirmation
7. https://api.github.com/orgs/anomalyco — org name "Anomaly", blog anoma.ly
8. https://api.npmjs.org/downloads/point/last-week/opencode-ai — weekly npm
9. https://api.npmjs.org/downloads/point/last-month/opencode-ai — monthly npm
10. https://api.npmjs.org/downloads/range/2025-06-01:2026-08-19/opencode-ai — monthly history
11. https://registry.npmjs.org/opencode-ai — first publish date, dist-tags
12. https://api.npmjs.org/downloads/point/last-week/@opencode-ai/sdk and /@opencode-ai/plugin — library downloads
13. https://formulae.brew.sh/api/formula/opencode.json — Homebrew installs
14. VS Code Marketplace gallery API (sst-dev.opencode, sst-dev.opencode-v2) — installs
15. https://open-vsx.org/api/sst-dev/opencode — Open VSX downloads
16. https://discord.com/api/v10/invites/opencode?with_counts=true — Discord member count
17. https://raw.githubusercontent.com/anomalyco/opencode/dev/README.md — tagline, install, agents
18. https://opencode.ai/ — tagline, features, maker-claimed numbers, FAQ headings
19. https://opencode.ai/docs/ — intro, install, features
20. https://opencode.ai/docs/mcp-servers/ — MCP client details
21. https://opencode.ai/docs/plugins/ — plugin model, hook events, custom tools
22. https://opencode.ai/docs/agents/ — build/plan/subagents, custom agents
23. https://opencode.ai/docs/config/ — config locations and keys
24. https://opencode.ai/docs/permissions/ — default permissions, --auto
25. https://opencode.ai/docs/skills/ — skills dirs incl. .claude/skills
26. https://opencode.ai/docs/rules/ — AGENTS.md/CLAUDE.md, disable env vars
27. https://opencode.ai/docs/commands/ — custom slash commands
28. https://opencode.ai/docs/acp/ — ACP support
29. https://opencode.ai/docs/sdk/ — @opencode-ai/sdk
30. https://opencode.ai/docs/server/ — opencode serve, OpenAPI
31. https://opencode.ai/docs/web/ — web UI
32. https://opencode.ai/docs/ide/ — IDE extension
33. https://opencode.ai/docs/cli/ — subcommands and flags
34. https://opencode.ai/docs/github/ — GitHub App/Action
35. https://opencode.ai/docs/providers/ — 75+ providers, subscription logins
36. https://opencode.ai/docs/zen/ and https://opencode.ai/zen — Zen pricing/positioning
37. https://opencode.ai/docs/go/ and https://opencode.ai/go — Go pricing/limits
38. https://opencode.ai/black — Black status
39. https://opencode.ai/docs/enterprise/ and https://opencode.ai/enterprise — enterprise offer
40. https://opencode.ai/changelog — latest release notes
41. https://anoma.ly/ — company site (no team page)
42. https://sst.dev/about/ — investors named by the company
43. https://www.ycombinator.com/companies/opencode — founders, HQ, team size
44. https://techfundingnews.com/opencode-the-background-story-on-the-most-popular-open-source-coding-agent-in-the-world/ — CEO interview, MAU/revenue/funding claims (2026-01-13)
45. https://x.com/thdxr/status/2007199285251842478 — Anomaly rebrand note (via search snippet)
46. https://blog.cloudflare.com/internal-ai-engineering-stack/ — Cloudflare internal usage numbers (2026-04-20)
47. https://developers.cloudflare.com/agent-setup/opencode/ — Cloudflare official setup guide
48. https://www.morphllm.com/ai-coding-agent — third-party star ranking, no benchmark scores
49. https://github.com/anomalyco/opencode/issues/14863 — native hooks feature request
50. https://github.com/opencode-ai/opencode and https://github.com/charmbracelet/crush — Charm collision
51. https://www.businesswire.com/news/home/20260513966755/en/ — confirms $17M round is Anomaly Insights (healthcare), not this company
52. https://ai.sulat.com/how-opencode-went-from-zero-to-titan-in-eight-months-dcdcd8ff5572 — secondary MAU figures (403 direct; via snippets)
53. Tracxn / Crunchbase search snippets — Anomaly Innovations historical funding (pages 403 / partial)

## Inclusion check (Jesse's test)

**Yes** — OpenCode runs its own agentic loop (its own tool set: read/edit/bash/glob/grep/
webfetch/task, permission system, session compaction, subagents) against any LLM provider,
and is the wrapped agent behind its own ACP, SDK, GitHub Action and IDE surfaces
(https://opencode.ai/docs/agents/, https://opencode.ai/docs/permissions/, https://opencode.ai/docs/acp/, 2026-08-21).
