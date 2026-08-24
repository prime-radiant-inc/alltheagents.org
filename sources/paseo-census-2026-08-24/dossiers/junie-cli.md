# Dossier: Junie (census_slug: junie-cli)

Compiled 2026-08-21/22 (GitHub/marketplace API pulls dated 2026-08-22 UTC). Facts only. Null convention: "null = not researched"; "False/none = researched and absent". Junie ships on two surfaces — the Junie CLI and the Junie plugin inside JetBrains IDEs — sharing one agent engine; each fact below states which surface it applies to.

## 1. Identity

- name: Junie ("Junie CLI" for the terminal surface; "Junie, the AI coding agent by JetBrains" is the IDE plugin's marketplace name) [S1][S12]
- maker: JetBrains s.r.o. (company; privately held; founded Prague 2000; corporate overview lists HQ Amsterdam, Netherlands — see section 5/6) [S2][S22]
- product URL: https://junie.jetbrains.com (CLI-centric product site) and https://www.jetbrains.com/junie/ (IDE-centric page; JS-rendered) [S1][S14]
- repo URL: https://github.com/JetBrains/junie — distribution repo only: install scripts, per-channel registries/update manifests, templates, issue tracker; no agent source [S3][S4] (as-of 2026-08-22)
- license: proprietary. LICENSE.md: "© JetBrains s.r.o. All rights reserved", use subject to JetBrains AI Service Terms of Service [S5]. GitHub API license = Other/NOASSERTION [S4]. npm license field "SEE LICENSE IN LICENSE.md" [S7].
- open source? False. source_available: partial-scaffolding only — repo holds installers/registries/tests/templates; CLI binaries ship as ~420 MB platform zips via GitHub Releases [S3][S6].
- first public release: IDE agent Early Access Program announced 2025-01-23 ("Meet Junie, Your Coding Agent by JetBrains"; TechCrunch same day) [S16][S17]; IDE public launch 2025-04-16 ("JetBrains IDEs Go AI") [S18]; Junie CLI Beta 2026-03 (blog "Junie CLI, the LLM-agnostic coding agent, is now in Beta"; npm package @jetbrains/junie first published 2026-03-02) [S19][S7]; whole product GA / out of Beta 2026-06-17 [S15]. GitHub repo created 2025-04-07 [S4].
- latest release (CLI): stable "Junie Release 26.8.17" (build 2777.8), published 2026-08-19; nightly builds continue daily (2986.1 on 2026-08-22) [S4][S6]. npm latest 2777.8.0 (2026-08-19); 49 npm versions since 2026-03-02 [S7]. 59 stable versions in the stable update manifest (starting at build 888.12) [S6].
- what it is:
  - Form factors: terminal CLI (interactive TUI; also headless `-p`/one-shot for CI/CD); IDE agent inside JetBrains IDEs (via AI Chat or the Junie plugin tool window) and Android Studio; GitHub Action and GitLab CI/CD entry points; "Remote mode" streams a running CLI session to a web UI at junie.jetbrains.com/remote for monitoring/steering from another device; ACP server mode (`junie --acp true`) for ACP-capable editors [S8][S9][S10][S11][S15].
  - Models: LLM-agnostic. Auth/model routes: JetBrains Account (AI subscription credits), Junie API key (usage-based), BYOK direct to OpenAI, Anthropic, Google, xAI, OpenRouter, GitHub Copilot (OAuth), and custom/self-hosted endpoints (LiteLLM, Ollama, LM Studio) [S8][S20][S21]. Site lists Claude Opus 4.8 / Sonnet 5 / Fable 5, Gemini 3.1 Pro / 3.7 Flash, GPT-5.6, Grok 4.5; default model is Gemini 3.7 Flash since 2026-08-17 (promo: 40% off base pricing "for a limited time") [S1][S13].
  - Pricing: Free tier — 5 AI credits included, "No card or subscription required"; BYOK "Provider-rate pricing, zero markup"; AI Pro $8.33/user/mo (annual billing) with 10 AI credits per 30 days; AI Ultimate $25.00/user/mo with 35 AI credits per 30 days ("Recommended for Junie"); top-ups available; 30-day AI Pro trial; JetBrains AI Enterprise exists (Remote mode unavailable under it) [S1][S12][S10] (as-of 2026-08-21).
  - Install (CLI): `curl -fsSL https://junie.jetbrains.com/install.sh | bash` (macOS/Linux), PowerShell one-liner (Windows), Homebrew tap `jetbrains-junie/junie`, `npm install -g @jetbrains/junie`; four update channels (stable, EAP, nightly, experimental) switchable per-launch (`junie --eap` etc.) [S3]. IDE plugin from JetBrains Marketplace (or auto-download via AI Chat) [S12][S23].
  - Default autonomy: asks approval for "potentially sensitive actions" (most terminal commands, edits outside the project, MCP tools); "Always allow" builds a persistent Action Allowlist (`~/.junie/allowlist.json`); Brave mode levels Off / Auto (safety-classifier auto-approval) / On (no approval), cycled via `/brave` or Ctrl+B [S8]. IDE plugin: Code mode (agentic) / Ask mode (read-only) / Auto picker, plus Brave Mode toggle [S23]. Project-trust gate before loading project-scoped MCP/skills/commands (added release 26.8.3, 2026-08-03) [S25].
  - Repo language per GitHub API: Shell (install scripts) [S4].

## 2. Adoption evidence

| metric / claim | value | as-of | source | type |
|---|---|---|---|---|
| JetBrains Marketplace downloads, IDE plugin 26104 "Junie, the AI coding agent by JetBrains" | 31,571,710 | 2026-08-22 | [S24] | independently observable (marketplace counter; includes IDE auto-updates) |
| Marketplace plugin rating | 2.93 (search API; plugin API returns null) | 2026-08-22 | [S24] | independently observable |
| Second marketplace listing "Junie" (id 30252, xmlId fleet.ai.agent.junie) | 639 downloads | 2026-08-22 | [S24] | independently observable |
| GitHub release asset downloads (CLI zips), 1,200 most recent releases (2026-05-06..08-22; API pagination floor) | 960,732 total; 866,301 on stable-channel releases; top single release 77,022 (26.5.18) | 2026-08-22 | [S4] | independently observable (proxy for CLI installs+updates since May 2026) |
| GitHub stars / forks / watchers (JetBrains/junie) | 395 / 28 / 6 | 2026-08-22 | [S4] | independently observable |
| GitHub issues ever filed / open | 71 / 60 | 2026-08-22 | [S4] | independently observable |
| Contributors (incl. anonymous) | 9 | 2026-08-22 | [S4] | independently observable |
| Commit cadence | 100+ commits in last 90 days (API page cap); release automation commits daily; 1,200+ GitHub releases since 2026-05-06 | 2026-08-22 | [S4] | independently observable |
| npm weekly / monthly downloads, @jetbrains/junie | 1,267 (2026-08-14..20) / 5,220 (2026-07-22..08-20) | 2026-08-20 | [S7] | independently observable (npm is a minor install path) |
| Homebrew | own tap JetBrains/homebrew-junie (created 2025-07-11); not in homebrew/core, no public analytics | 2026-08-22 | [S4] | independently observable (no count available) |
| Junie users | "343K Junie users" (counting began 2025-03-26); "1M+ AI-assisted actions completed" | 2026 annual report (covering 2025-2026) | [S26] | maker-claimed |
| Paid AI users (AI Assistant + Junie) | 240% YoY growth Q4 2024 -> Q4 2025; quarterly index Q1'25=100 -> Q4'25=269 | 2026 | [S26] | maker-claimed |
| Developer Ecosystem Survey 2026 (15,000+ devs, May-Jul 2026) | 9% of developers worldwide use JetBrains AI in IDEs and/or Junie at work (vs Claude Code 39%, Copilot 21%, Codex 16%, Cursor 12%) | 2026-08 | [S27] | maker-run survey of external devs |
| Company context | 12.5M+ recurring active users of JetBrains products; 88 of Fortune Global Top 100 are customers; 25.69% YoY revenue growth | 2026 annual report | [S26] | maker-claimed |
| Benchmark: SWE-Rebench (Nebius, independent) | "number-one coding agent" on the latest run at GA: 61.6% resolved, 72.7% pass@5 (quote attributed to Alexander Golubev, Research Lead at Nebius) | 2026-06-17 | [S15] | third-party benchmark, cited by maker (not re-verified on swe-rebench site) |
| Benchmark: SWE-bench Verified (IDE launch claim) | 53.6% single-run | 2025-04-16 | [S18][S28] | maker-claimed |
| Funding / valuation | none found — JetBrains is privately held, historically bootstrapped; no Junie-specific funding events | 2026-08-22 | [S2][S22] | researched, absent |
| Community: Discord | official Junie Discord (jb.gg/junie-discord) linked from README/marketplace; member count not obtainable without joining | 2026-08-22 | [S3][S24] | null (count not obtainable) |
| GitHub Discussions | not enabled on repo | 2026-08-22 | [S4] | independently observable |
| Press | TechCrunch (2025-01-23 EAP launch); SiliconANGLE, Verdict, developer-tech (2025-04 IDE launch); DevOps.com (2026-03, Air + Junie CLI launch); assorted 2026 reviews | 2026-08-22 | [S17][S29] | press |
| Public customers / case studies | none found Junie-specific (company-level: 88 Fortune 100 logos claim) | 2026-08-22 | [S26] | researched, absent for Junie specifically |

## 3. Plugin interface (PRI-2925)

- mcp_support: **client** (both surfaces). CLI: MCP servers via `.junie/mcp/mcp.json` (project) / `~/.junie/mcp/mcp.json` (user); `/mcp` command with an AI "MCP Installation Assistant" (registry of pre-configured servers, searches the official MCP registry, verifies startup); local (npx/Docker/binary) and remote (HTTP/HTTPS) servers; OAuth for remote servers; `--mcp-location`/`--mcp-default-locations` flags; ACP clients can pass MCP servers at session init. Same JSON config shared with the IDE plugin. Not an MCP server itself (none found). Evidence: https://www.jetbrains.com/help/junie/junie-cli-mcp-configuration.html [S30] (as-of 2026-08-21)
- plugin_support: **True** — "extensions" (aliases /plugin, /plugins): reusable bundles packaging any combination of agent skills, MCP servers, subagents, custom slash commands, guidelines, and hooks; distributed via marketplaces (git repo, local dir, or direct marketplace.json URL); built-in official marketplace https://github.com/JetBrains/junie-extensions (Java, Kotlin, Android, Spring Boot, SQL, Redis...); project scope `.junie/extensions.json` / user scope `~/.junie/extensions/`. Also standalone Agent Skills (`.junie/skills/<name>/SKILL.md`, "open Agent Skills format", auto-invoked, also exposed as `/<skill-name>` and `$<skill-name>`) and custom slash commands (`.junie/commands/*.md`, `~/.junie/commands/`). Evidence: https://www.jetbrains.com/help/junie/junie-cli-extensions.html ; https://www.jetbrains.com/help/junie/agent-skills.html [S31][S32] (as-of 2026-08-21)
- claude_code_plugin: **partial (marketplace-compatible)** — extensions marketplaces accept "the Claude plugin format at .claude-plugin/marketplace.json", so "you can connect any Claude-compatible plugin marketplace to Junie CLI" (docs example even points at anthropics/knowledge-work-plugins); separately, Junie detects `.claude/skills/`, `.claude/agents/` (and .cursor/, .codex/ equivalents) and offers to import them into `.junie/`; guidelines import from other agents' memory files on first open; also reads cross-agent `.agents/skills/` and `AGENTS.md`. Not verified: direct execution of a full Claude Code plugin (hooks/commands) without import [S31][S32][S33][S34].
- subagents: **True** (CLI) — auto-delegation only (not manually invocable): Markdown+YAML files in `.junie/agents/`, `.agents/`, `~/.junie/agents/`, `~/.agents/`; frontmatter: name, description (required), tools/disallowedTools (groups: Read, Bash, Glob, Grep, Write, Edit, WebSearch, AskUserQuestion), mcpServers allowlist, model, permissionMode (default/acceptEdits/dontAsk/bypassPermissions/plan), reasoningLevel/effort, maxTurns, skills, allowPromptArgument; model policy setting SameModelOnly vs Auto (default; may pick cheaper tiers) — policy setting in EAP. Evidence: https://www.jetbrains.com/help/junie/junie-cli-subagents.html [S33] (as-of 2026-08-21)
- hooks: **True (EAP)** (CLI) — shell-command hooks in `~/.junie/config.json` (project-local hook files ignored by default for safety); events: SessionStart (startup/resume/clear/compact), UserPromptSubmit, PreToolUse (decision allow/ask/block, updatedInput, additionalContext; exit code 2 blocks), PermissionRequest (auto-approve/deny, skips dialog), Stop (block-with-retry, blockOnError), StopFailure (observability-only; 9 error kinds), SessionEnd; async hooks supported; PostToolUseFailure named as future. Evidence: https://www.jetbrains.com/help/junie/junie-cli-hooks.html [S35] (as-of 2026-08-21)
- plan_mode: **True** — CLI Plan mode: read-only exploration produces a structured design document (Requirements / Technical design / Testing / Delivery steps tabs), reviewed and iterated before implementation; Shift+Tab cycle, `/plan`, `--plan` flag; plans saved as Markdown ("lives in .junie/plans", committable, per GA post); GA post frames "plan on a strong model; implement on a cheap one". IDE plugin: Ask mode is the read-only mode. Also Debug mode (CLI+IDE: drives the real IDE debugger — breakpoints, stack frames, expression evaluation) and Goal mode `/goal` (β, orchestrated step-by-step for very large projects). Evidence: https://www.jetbrains.com/help/junie/junie-cli-plan-mode.html [S36][S15][S25] (as-of 2026-08-21)
- plugin_docs_url: https://www.jetbrains.com/help/junie/junie-cli-extensions.html (skills: https://www.jetbrains.com/help/junie/agent-skills.html)
- config_docs_url: https://www.jetbrains.com/help/junie/junie-cli-configuration.html (parameters: https://www.jetbrains.com/help/junie/parameters.html ; guidelines: https://www.jetbrains.com/help/junie/guidelines-and-memory.html)
- ACP support: **yes, first-party agent (server)** — `junie --acp true` serves ACP clients (JSON-RPC over stdio locally; HTTP/WebSocket remote "evolving in the ecosystem"); the GA IDE integration itself was rebuilt on ACP ("One engine, many surfaces" — AI chat, Junie tool window, and CLI share one engine); docs expand ACP as "Agent Client Protocol" while the GA blog post says "Agent Communication Protocol" (discrepancy noted). Evidence: https://www.jetbrains.com/help/junie/junie-cli-acp.html [S9][S15] (as-of 2026-08-21)
- SDK: **none found** — no public programmatic SDK; automation path is headless CLI (`junie --auth="$JUNIE_API_KEY" "<prompt>"`), GitHub Action (`/install-github-action`), GitLab CI/CD [S11][S3]. Researched, absent.
- Other config: guidelines from `.junie/AGENTS.md`, root `AGENTS.md` (+ `.junie/playbook.md`, `.junie/rules/*.md`), legacy `.junie/guidelines.md`; global `~/.junie/AGENTS.md`; project takes precedence [S34]. Custom model profiles `.junie/models/*.json` and `$JUNIE_HOME/models/` [S21]. Parallel sessions + git worktrees (`/new`, Task history) [S8].

## 4. Claimed differentiation (raw material for PRI-2927)

- tagline (repo, verbatim): "An LLM-agnostic coding agent built for real-world development — by JetBrains." — https://github.com/JetBrains/junie [S3]
- tagline (site hero): "Stop switching tools. Start shipping. The coding agent that works with any model you choose." — https://junie.jetbrains.com [S1]
- GitHub description: "ships code from your terminal, IDE, or CI/CD pipeline - powered by any LLM you choose" [S4]
- maker claims (paraphrased):
  1. LLM-agnostic / no lock-in: any top model via subscription or BYOK at provider rates with zero markup, plus local runtimes (Ollama, LM Studio, LiteLLM) — "delegating work to an agent should be something you can afford to do often" [S1][S15][S19].
  2. Powered by the IDE: "IntelliJ IDEA Engine"; uses the IDE's semantic index, build configs, test runners, databases (DataGrip), and the real debugger rather than approximations ("Junie opens the debugger", not println) [S1][S15].
  3. Plans before it codes: Advanced Plan Mode makes the plan a first-class, committable artifact (.junie/plans) and asks clarifying questions; "Plan on Opus, implement on Flash" cost strategy [S1][S15].
  4. Benchmark proof: "Top performer on SWE-Rebench" (site badge); #1 coding agent at GA with 61.6% resolved / 72.7% pass@5 [S1][S15].
  5. Live Prompting / real-time follow-ups: steer the agent mid-task without restarting ("Exclusive feature" label on site) [S1][S8].
  6. Human in the loop by default: approval prompts, dynamic Action Allowlist, graded Brave mode [S1][S8].
  7. Async + anywhere: Remote Control — start on laptop, monitor from phone via web app; GitHub/GitLab CI entry points [S1][S15].
  8. Frictionless migration: "Switch from other AI coding agents in seconds"; auto-imports skills/agents/guidelines from .claude/.cursor/.codex and Claude-format marketplaces [S1][S31][S33].
  9. One engine, many surfaces (ACP): same agent behind AI chat, IDE tool window, and CLI; "Improvements ship once and show up everywhere" [S15].
  10. Compliance: SOC 2 certification cited on site [S1].
- audience: professional developers, JetBrains IDE users first (IDE plugin "recommended way"); CLI aimed at terminal/CI users "inside any IDE"; teams (shared .junie config in VCS); orgs via AI Enterprise; individuals via Free/Pro/Ultimate tiers [S1][S12][S23].

## 5. Company & contact targets (PRI-2929) — company-level only

- legal name: JetBrains s.r.o. (Czech entity named in license/copyright); corporate overview 2026 lists HQ Amsterdam, Netherlands; founded 2000 in Prague [S5][S2][S22]
- size: "2600+ employees across 13 offices" (2026 annual highlights) [S26]; press/aggregators ~2,800 [S22]
- funding stage: privately held; no external funding rounds found (researched, absent) [S2][S22]
- publicly named leadership (public sources only):
  - Kirill Skrygan — CEO (appointed February 2024; named in press/company materials) [S22]
  - Junie team byline: Anastasia Krivosheeva — author of the Junie CLI Beta launch post on blog.jetbrains.com [S19]
  - No Junie-specific head of product / DevRel / partnerships lead found named publicly (researched, absent; JetBrains routes contact via jetbrains.com contact form and sales) [S1]
- contact: Contact Form + Support Guide linked from junie.jetbrains.com footer [S1]

## 6. Open questions / conflicts

- **One census entry or two?** hc/agents has both `junie.md` and `junie-cli.md`. They describe the same product: `junie.md`'s repo/install/docs fields are all the CLI's, and JetBrains positions Junie as one agent with two surfaces sharing one engine over ACP [S15]. Recommend **one entry** (slug junie-cli, name "Junie"), with the IDE plugin noted as a surface (its 31.6M marketplace downloads are the biggest adoption number and belong in the same entry).
- hc/agents/junie.md errors: `url` points at the GitHub repo instead of a product site; `first_released: 2025-04-07` is the repo creation date, not a product date (EAP 2025-01-23, IDE launch 2025-04-16, CLI beta 2026-03); `stars: 397` now 395; `mcp_support/plugin_support/subagents/hooks/plan_mode: null` → all researched above (client / yes / yes / yes-EAP / yes); `claude_code_plugin: False` → partial (Claude-format marketplaces + .claude/skills/.claude/agents import); `pricing: null` → filled; `model_providers` omits JetBrains Account/Junie API key/custom endpoints routes.
- hc/agents/junie-cli.md errors/gaps: `maker: null` → JetBrains s.r.o.; `source_code_url: null` → https://github.com/JetBrains/junie; `first_released/current_release/stars/language: null` → filled above; `mcp_support/claude_code_plugin/subagents/hooks: null` → filled; `url: junie.jetbrains.com` fine. Its what_makes_it_special mirrors site claims accurately, but "top performer on SWE-Rebench" should be labeled maker-cited (benchmark run by Nebius; not re-verified here).
- HQ conflict: license/copyright say JetBrains s.r.o. (Czech); 2026 corporate overview lists Amsterdam HQ; Wikipedia has described Prague as HQ historically. Not resolved here [S2][S22].
- ACP expansion conflict: docs say "Agent Client Protocol"; GA blog says "Agent Communication Protocol" [S9][S15].
- "343K Junie users" (annual report) has no as-of date beyond the report period and no MAU/WAU definition; the counting start (2025-03-26) predates the IDE public launch [S26].
- Marketplace 31.6M downloads counts plugin downloads including auto-updates across ~500K+ IDE installs (JetBrains does not publish unique-install counts); do not read as users.
- GitHub release-asset total (960,732) is a floor: the releases API pagination returned only the 1,200 most recent releases (back to 2026-05-06); stable builds before May 2026 (from 888.12) not counted. Also each install downloads one ~420 MB zip per update, so this measures install/update events.
- SWE-Rebench placement quoted from JetBrains' GA post; the live swe-rebench.com leaderboard was not fetched (results "move from run to run" per the post itself) [S15].
- Discord member count not obtainable without joining. www.jetbrains.com/junie/ and /ai-ides/buy/ are JS-rendered; their content was cross-covered via junie.jetbrains.com and docs instead.
- Hooks and the subagent model-policy setting are EAP-only today; census "hooks: yes" should carry that qualifier [S35][S33].
- npm downloads are tiny (~1.3K/wk) vs GitHub-release installs — npm is a shim; don't use npm counts as the adoption proxy.

## 7. Sources

1. [S1] https://junie.jetbrains.com/ — hero, features, models list, pricing tiers, SOC 2, footer contacts
2. [S2] https://en.wikipedia.org/wiki/JetBrains (via search snippets) — founding, private company
3. [S3] https://raw.githubusercontent.com/JetBrains/junie/main/README.md — tagline, install, channels, auth, GitHub Action, Discord
4. [S4] GitHub API repos/JetBrains/junie (+releases ×12 pages, contributors, commits, search/issues, contents; repos junie-extensions, junie-guidelines, homebrew-junie) — stars/dates/downloads
5. [S5] https://raw.githubusercontent.com/JetBrains/junie/main/LICENSE.md — all rights reserved, AI Service ToS
6. [S6] https://raw.githubusercontent.com/JetBrains/junie/main/update-info.jsonl — stable version history, zip sizes
7. [S7] https://registry.npmjs.org/@jetbrains/junie + api.npmjs.org downloads — first publish 2026-03-02, latest, weekly/monthly counts
8. [S8] https://www.jetbrains.com/help/junie/junie-cli.html — quickstart, approval/allowlist, Brave mode, modes, /review, /remote, /model, headless pointer
9. [S9] https://www.jetbrains.com/help/junie/junie-cli-acp.html — ACP mode, --acp flag, transports
10. [S10] https://www.jetbrains.com/help/junie/junie-cli-remote-mode.html — Remote mode mechanics, subscription requirement
11. [S11] https://www.jetbrains.com/help/junie/junie-headless.html — headless/CI usage, project trust
12. [S12] https://plugins.jetbrains.com/api/plugins/26104 (+searchPlugins) — IDE plugin name, downloads, vendor, description
13. [S13] https://junie.jetbrains.com/blog/junie-gemini-3-7-flash — default model change 2026-08-17, 40% off, private benchmark claim
14. [S14] https://www.jetbrains.com/junie/ — title only (JS-rendered)
15. [S15] https://junie.jetbrains.com/blog/junie-coding-agent-out-of-beta — GA 2026-06-17, SWE-Rebench #1 (61.6%/72.7%), Plan mode, debugger, ACP rebuild, review, remote control
16. [S16] https://blog.jetbrains.com/junie/2025/01/meet-junie-your-coding-agent-by-jetbrains/ — EAP announcement (via search)
17. [S17] https://techcrunch.com/2025/01/23/jetbrains-launches-junie-a-new-ai-coding-agent-for-its-ides/ — EAP launch date press
18. [S18] https://blog.jetbrains.com/blog/2025/04/16/jetbrains-ides-go-ai/ — IDE public launch, free tier, SWE-bench 53.6% (via search)
19. [S19] https://blog.jetbrains.com/junie/2026/03/junie-cli-the-llm-agnostic-coding-agent-is-now-in-beta/ — CLI Beta launch, BYOK, author byline
20. [S20] https://www.jetbrains.com/help/junie/byok.html — BYOK providers table, billing priority
21. [S21] https://www.jetbrains.com/help/junie/custom-llm-models.html — custom model JSON profiles, Ollama/LiteLLM/LM Studio
22. [S22] web search results (resources.jetbrains.com corporate overview PDF, Glassdoor, trueup, Fast Company profile) — HQ Amsterdam, ~2,800 employees, CEO Kirill Skrygan (Feb 2024)
23. [S23] https://www.jetbrains.com/help/junie/junie-ide-plugin.html — IDE plugin install, AI Chat, licensing/trial, Code/Ask/Brave modes
24. [S24] https://plugins.jetbrains.com/api/searchPlugins?search=junie + /api/plugins/30252 — download counts, rating 2.93, second listing
25. [S25] https://junie.jetbrains.com/whats-new — release notes (26.8.17 TUI//voice//stats; 26.8.3 project trust; Goal mode β)
26. [S26] https://www.jetbrains.com/lp/annualreport-2026/ — 343K Junie users, 240% paid-AI growth, 2600+ employees, 12.5M+ RAU, 88 Fortune 100
27. [S27] https://blog.jetbrains.com/research/2026/08/ai-coding-agent-adoption-2026/ — Dev Ecosystem Survey 2026 adoption percentages
28. [S28] https://siliconangle.com/2025/04/16/jetbrains-launches-junie-ai-coding-agent-developers/ — IDE launch press (via search)
29. [S29] https://devops.com/jetbrains-launches-air-and-junie-cli-to-blend-traditional-ide-with-ai-agents/ — Air + Junie CLI launch press (via search)
30. [S30] https://www.jetbrains.com/help/junie/junie-cli-mcp-configuration.html — MCP client config, Installation Assistant
31. [S31] https://www.jetbrains.com/help/junie/junie-cli-extensions.html — extensions, marketplaces, Claude plugin-format compat
32. [S32] https://www.jetbrains.com/help/junie/agent-skills.html — Agent Skills format, locations, import from .claude/.cursor/.codex
33. [S33] https://www.jetbrains.com/help/junie/junie-cli-subagents.html — subagent format, tool groups, import of other tools' agents
34. [S34] https://www.jetbrains.com/help/junie/guidelines-and-memory.html — AGENTS.md discovery order, global guidelines, import
35. [S35] https://www.jetbrains.com/help/junie/junie-cli-hooks.html — hook events, decisions, EAP status
36. [S36] https://www.jetbrains.com/help/junie/junie-cli-plan-mode.html — plan mode mechanics, plan view tabs
37. https://www.jetbrains.com/help/junie/junie-cli-jetbrains-ide-integration.html — /ide, supported IDEs, passive discovery
38. https://www.jetbrains.com/help/junie/custom-slash-commands.html — command file format, arguments

## Inclusion check (Jesse's test)

**Yes** — Junie is a first-party coding agent with its own agentic loop (plans, edits files, runs shell commands, drives tests/debugger, iterates to completion) on both CLI and IDE surfaces; the ACP mode exposes Junie's own agent, it is not a wrapper around someone else's [S8][S15][S9].
