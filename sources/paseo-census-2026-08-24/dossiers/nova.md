# Dossier: Nova / Compass AI (census_slug: nova-compass)

Compiled 2026-08-24. Facts only. Null convention: "null = not researched"; "False/none = researched and absent". Closed-development commercial product with thin public footprint — several claims are maker-only. NOT currently in the census; proposed new-entry frontmatter at end. Slug proposed as `nova-compass` ("nova" alone is collision-prone).

## 1. Identity

- name: **Nova** — "the flagship Compass AI agent" [S5]. npm `@compass-ai/nova`; installs two equivalent bins, `nova` and `compass`; internal codename **Kore-CLI** (npm repository field and update/release-notes URLs point to `dev.azure.com/oakpeak-devops/Kore/_git/Kore-CLI`; the bundle logs "Kore-CLI OAuth credentials") [S3][S6].
- maker: **Compass Agentic Platform** ("Compass AI"), maker of an enterprise agent suite (Nova for developers; Gilford/Alfred/Barnaby/Marlowe for Excel/Outlook/PowerPoint/Word; Compass Partner desktop) [S4]. Org form/HQ: not public (researched, absent). Public contact is a gmail address: get.compass.ap@gmail.com [S4]. GitHub org Compass-Agentic-Platform created 2026-01-30, 2 followers [S8]. npm maintainers (public handles): dherbe, compass-ap [S3]. Euro-denominated pricing suggests Europe (observation, not maker-stated) [S4].
- product URL: https://www.compassap.ai/portfolio/nova.html (company: https://www.compassap.ai)
- repo URL: development is private (Azure DevOps `oakpeak-devops/Kore`, redirects to login) [S3][S7]; public GitHub https://github.com/Compass-Agentic-Platform/nova is a **shell repo** — README, CHANGELOG, LICENSE, assets only, no source, last pushed 2026-03-06 [S8].
- license: **MIT** (npm metadata; LICENSE in the GitHub shell repo) [S3][S8] — but see §6: MIT-labeled with no public source.
- open source? **False.** source_available: False — npm ships a minified ~11 MB `dist/cli.js` bundle plus vendored node_modules; no source repository is public [S6][S8].
- first public release: npm 1.0.0 on 2026-01-06 [S3].
- latest release: 1.1.37, 2026-08-22; 130 npm versions in ~7.5 months [S3].
- what it is:
  - Form factor: terminal CLI/TUI (Ink/React) with interactive sessions, `--print` one-shot mode, session archive/resume, local observability dashboard (`nova dashboard`), `nova doctor` health checks; **ACP server** (`nova acp`, with `--unleash` unguarded mode); **A2A server** (`nova a2a`, tunnel via bundled cloudflared); internal JSON-RPC stdio tools server (`nova tools-rpc`) for automation clients [S5][S6].
  - Models: Compass-managed models via the maker's proxy (api.compassap.ai, **plan-gated**: "Haiku and Ollama models are available. Upgrade for full access"), Anthropic-compatible providers via API key, OpenAI chat/responses incl. ChatGPT sign-in, custom endpoints via `nova models`, Ollama [S5][S6][S9].
  - Pricing: subscription seats platform-wide — Teams €40, Pro €80, Max €200, Enterprise €500 per seat/month, 7-day trial [S4]; BYOK usable alongside [S5].
  - Install: `npm install -g @compass-ai/nova` then `nova setup` (auth, consent, provider config); Node >= 22.12 [S5].
  - Default autonomy: "guarded execution" — file/shell/git/database/external actions pass explicit safety rules; destructive or externally visible actions require confirmation; risk-tiered approval policy (`maxRiskWithoutApproval` in bundle); managed git-worktree isolation for dirty repos; GDPR-style export/delete via `nova data` [S5][S6] (maker-described, not independently tested).
  - Implementation: TypeScript, bundled/minified; deps include @anthropic-ai/sdk, @modelcontextprotocol/sdk, Ink/React, simple-git, cloudflared, pptxgenjs/exceljs/pdfjs (document skills) [S3][S6].

## 2. Adoption evidence

| metric / claim | value | as-of | source | type |
|---|---|---|---|---|
| npm downloads `@compass-ai/nova` | 1,316/week; 4,360/month | 2026-08-24 | [S10] | independently observable |
| npm release cadence | 130 versions 2026-01-06 → 2026-08-22 | 2026-08-24 | [S3] | independently observable |
| GitHub stars (shell repo) | 13; 1 fork; repo has no code and is stale since 2026-03-06 | 2026-08-24 | [S8] | independently observable (weak proxy) |
| "500+ enterprise teams" | stated on compassap.ai (platform-wide, not Nova-specific) | 2026-08-24 | [S4] | maker-claimed, unverifiable |
| SOC 2 Type II, ISO 27001, GDPR, 99.9% uptime SLA | stated on compassap.ai | 2026-08-24 | [S4] | maker-claimed; no auditor/cert registry evidence found |
| Ecosystem listing | Zed/JetBrains ACP setup (`npx @compass-ai/nova@latest acp`) documented; subject of this census because it appears in Paseo's ACP catalog | 2026-08-24 | [S9] | independently observable |
| Press, community server, case studies, funding, benchmarks | none found (no Discord/Slack, no named customers, no benchmark entries, no coverage) | 2026-08-24 | [S9] | researched, absent |

## 3. Plugin interface (PRI-2925)

- mcp_support: **client** — `nova mcp` / `/mcp`, MCP server management with auth (API tokens and OAuth to remote servers; Figma/Notion examples; handles OAuth-restricted remote servers), `@modelcontextprotocol/sdk` dependency. No MCP server mode found [S5][S6][S3]. Evidence: npm README "MCP and custom workflows".
- plugin_support: **True** — several layers: Skills (`SKILL.md` packages in `.compass/skills/` and `~/.compass/skills/`; bundled skills for frontend design, PowerPoint generation, Azure/CloudFoundry ops), custom slash commands (`.compass/commands` and `~/.compass/commands`, markdown with frontmatter, `allowed-tools`, argument hints, inline `` !`cmd` `` output interpolation), custom agents, scheduled tasks [S5][S6]. No marketplace of its own.
- claude_code_plugin: **partial** — consumes the Agent Skills `SKILL.md` format; its own embedded docs tell users to install skills with `npx skills add <skill> -a claude-code` (into `.claude/skills/`) and then **move** the folder to `.compass/skills/` — i.e., format-compatible but it does not read `.claude/` paths itself. Its slash-command format (frontmatter + `!` command interpolation) mirrors Claude Code's, and internal prompt templates are written for "Claude Code subagents" verbatim [S6]. Not the Claude Code plugin/marketplace format.
- subagents: **True** — "specialized agents for exploration, verification, planning, and implementation"; `/agents` to switch/inspect; README example "Spawn a verification agent to check the fix without editing files"; bundle contains a subagent-generation flow [S5][S6].
- hooks: **True** — "add hooks that run on lifecycle events" (README); no public hook reference doc found (depth/matchers unverified) [S5].
- plan_mode: **True (as planning workflow)** — `/plan` creates and manages implementation plans; plan→build→verify framing. A distinct enforced read-only mode was not documented (unverified) [S5].
- plugin_docs_url: none public — documentation ships inside the CLI/bundle; the GitHub shell README is the closest public doc [S8] (researched, absent).
- config_docs_url: none public — config precedence documented only in the npm README (`~/.compass/config.json`, `./.compass/config.json`, env, flags) [S5].
- ACP support: **yes, first-party** — `nova acp` (options: `--cwd`, `--debug`, `--unleash` unguarded mode); documented for Zed and JetBrains via `npx @compass-ai/nova@latest acp`; ACP sessions map to a distinct runtime surface in the bundle [S6][S9]. Also **A2A** server mode with cloudflared tunnel, and an "agui" command surface [S6].
- SDK: **False** — no published SDK; `nova tools-rpc` JSON-RPC stdio server is offered for scripted automation instead (an internal "sdk" runtime surface exists in the bundle but nothing is published) [S5][S6].

## 4. Claimed differentiation (raw material for PRI-2927)

- tagline: portfolio page pitches Nova as "a fully-fledged software engineer at your command" (per census brief); page copy: "A powerful command-line interface that seamlessly integrates with your IDE and guides you through every step of building code." [S2]. README: "planning, editing, verifying, and shipping software from your terminal" [S5]. Company: "AI That Works Where You Work" [S4].
- maker claims (paraphrased):
  1. Built for production repos, not demos: long-running sessions, dirty worktrees, "teams that need more than a chat box pasted beside an editor" [S5].
  2. Guarded execution as a design pillar — explicit safety rules over file/shell/git/db/external actions; risk-gated approvals [S5].
  3. Verification-first delivery: treats passing tests/lint/type checks as completion criteria, "not vibes" [S5].
  4. Git-native: managed worktree isolation for dirty repos, conventional commits, PR-ready summaries, `/undo` [S5].
  5. Model flexibility: Compass-managed models, Anthropic-compatible, OpenAI incl. ChatGPT OAuth, custom endpoints, Ollama [S5].
  6. Part of an enterprise agent suite spanning Office apps and Microsoft 365, one platform login [S4].
  7. Privacy/compliance posture: local data under `~/.compass`, encrypted credentials, GDPR export/delete flows, SOC 2 / ISO 27001 (platform claims) [S5][S4].
  8. Observability: local live dashboard, JSONL event logs, token/cost inspection [S5].
- audience: developers/power users ("elite of developers" on the portfolio page) inside enterprises; platform pricing is per-seat teams→enterprise [S2][S4].

## 5. Company & contact targets (PRI-2929)

- Company name as self-presented: "Compass Agentic Platform" [S4]. Legal entity, HQ, size: not found (researched, absent). Azure DevOps org name "oakpeak-devops" is the only other organizational trace [S3].
- Leadership: none named anywhere public that was found — no team page, no press releases, no bylines (researched, absent) [S4][S9].
- Contact paths: get.compass.ap@gmail.com (site) [S4]; npm maintainer emails are public on the registry [S3]; GitHub org issues.
- Funding: none found (researched, absent).

## 6. Open questions / conflicts

- **Enterprise claims vs. footprint**: "500+ enterprise teams", SOC 2 Type II, ISO 27001, 99.9% SLA — asserted on a site whose only contact is a gmail address, with no named customers, auditors, team, or legal entity found. All §2 compliance/traction lines are maker-claimed and unverified [S4][S9].
- **MIT with no source**: the package and shell repo say MIT, but no source is public and development is on a private Azure DevOps. "MIT" here licenses the distributed bundle; it is not open source in practice [S3][S8][S6].
- **Embedded third-party OAuth client**: the bundle ships OpenAI's Codex CLI OAuth client id (`app_EMoamEEZ73f0CkXaXp7hrann`, originator `codex_cli_rs`) and drives ChatGPT/Codex backend usage endpoints through it — i.e., Nova authenticates to OpenAI as if it were Codex CLI. Independently observable in the bundle; whether OpenAI sanctions this is unknown. No equivalent Anthropic OAuth impersonation found (Anthropic path is plain API key) [S6].
- **Name sprawl**: Nova (product) = `compass` (alias bin) = Kore-CLI (internal) = oakpeak-devops (Azure org) = Compass Agentic Platform / "Compass AI" (company). The census entry should record the aliases [S3][S6][S4].
- GitHub shell repo (13 stars, stale since March) vs npm (active through 2026-08-22): GitHub metrics do not reflect the project's activity [S8][S3].
- The portfolio page's marketing ("elite of developers", "SOC 2") could not be fully parsed (fetched via summarizing proxy); the "fully-fledged software engineer" tagline comes from the census brief and the page summary, not a raw-quote capture [S2].
- Compass-managed model plan-gating ("Haiku and Ollama … Upgrade for full access") appears only in bundle strings; the public pricing page does not describe Nova-specific model tiers [S6][S4].
- Whether `/plan` is an enforced read-only mode (vs. a planning workflow) is unverified [S5].

## 7. Sources

1. [S1] — (reserved; not used)
2. [S2] https://www.compassap.ai/portfolio/nova.html (WebFetch summary) — Nova positioning, IDE integration, audience, SOC 2 mention
3. [S3] https://registry.npmjs.org/@compass-ai/nova — versions/dates, MIT, bins nova+compass, Azure DevOps repo field, maintainers, deps
4. [S4] https://www.compassap.ai (WebFetch summary) — company suite, pricing €40-€500/seat, "500+ enterprise teams", certifications, gmail contact
5. [S5] npm package README.md (in tarball, dated 2026-06-24) — capabilities, commands, skills/commands/hooks, config, privacy, guarded execution
6. [S6] nova-1.1.37.tgz `dist/cli.js` bundle inspection — Kore-CLI strings, api.compassap.ai proxy + plan gating, Codex OAuth client id, ACP/A2A/tools-rpc surfaces, autonomy policy, Claude Code subagent prompt templates, skills-install-via-claude-code instructions
7. [S7] https://dev.azure.com/oakpeak-devops/Kore — 302 redirect (private; UNREACHABLE without login)
8. [S8] https://api.github.com/repos/Compass-Agentic-Platform/nova + /orgs/Compass-Agentic-Platform — shell repo (no source), 13 stars, MIT LICENSE, org created 2026-01-30
9. [S9] Web search results 2026-08-24 — GitHub org discovery, Zed/JetBrains ACP setup snippet, absence of press/community
10. [S10] https://api.npmjs.org/downloads/point/last-week|last-month/@compass-ai/nova — download counts

## Inclusion check (Jesse's test)

**Yes** — Nova owns its own agentic loop: the bundle implements its own tool engine (file/shell/git/db/MCP), risk-tiered autonomy policy, subagents, session/worktree management, and a multi-provider model layer (own proxy + Anthropic + OpenAI + custom); it does not spawn or wrap another vendor's agent. Caveat for the record: it borrows Claude Code's ecosystem conventions (SKILL.md, slash-command format, literal "Claude Code subagent" prompt templates) and OpenAI Codex's OAuth client identity, but the loop itself is its own [S5][S6].

## Proposed census entry (per hc/agents/_TEMPLATE.md — new file agents/nova-compass.md)

```yaml
---
name: "Nova"
slug: "nova-compass"          # "nova" alone is collision-prone; register override if needed
layout: "agent.njk"
category: "agent"
maker: "compass-agentic-platform"   # new maker record: maker_type company (entity unverified), country null (EUR pricing; HQ not public), makes_models false, revenue_model ["subscriptions"]
license: "MIT"                # MIT-labeled distribution; no public source (see body)
url: "https://www.compassap.ai/portfolio/nova.html"
source_code_url: null          # private Azure DevOps (oakpeak-devops/Kore); GitHub repo is a docs shell
source_available: False
homepage: "https://www.compassap.ai"
docs_url: "https://github.com/Compass-Agentic-Platform/nova"   # public README shell; real docs ship in-CLI
download_url: "https://www.npmjs.com/package/@compass-ai/nova"
install_method: "npm install -g @compass-ai/nova; nova setup"
platforms: ["CLI", "IDE"]      # IDE via ACP (Zed, JetBrains)
autonomy_level: ["agentic"]
specialization: "general"
language: null                 # closed source (TypeScript per bundle, unverifiable further)
first_released: "2026-01-06"
current_release: "2026-08-22"
maintained: "active"
mcp_support: "yes (client; API-token and OAuth auth to remote servers)"
plugin_support: "yes (SKILL.md skills, custom slash commands, custom agents, scheduled tasks)"
claude_code_plugin: "partial (SKILL.md-format compatible — docs route installs through claude-code then relocate to .compass/; command format mirrors Claude Code)"
subagents: "yes (exploration/verification/planning/implementation agents; /agents)"
hooks: "yes (lifecycle-event hooks; depth undocumented publicly)"
plan_mode: "yes (/plan implementation-plan workflow; enforced read-only unverified)"
plugin_docs_url: null
config_docs_url: null
model_providers: "Compass-managed proxy, Anthropic (API key), OpenAI (incl. ChatGPT OAuth), Ollama, custom endpoints"
pricing: "subscription"        # €40-€500/seat/month platform plans; BYOK usable
github_stars: 13               # docs-shell repo only; npm ~4.4k downloads/month is the better signal
sources: ["paseo-acp-catalog"]
last_verified: "2026-08-24"
what_makes_it_special: "The developer-facing flagship of an enterprise agent suite (Office add-ins included), pitching guarded execution, worktree isolation, and verification-first delivery — developed in private, sold per-seat, with heavy borrowing of Claude Code's skills and command conventions."
---
Nova is the coding-agent arm of Compass Agentic Platform, a closed-development
suite whose other agents live inside Excel, Outlook, PowerPoint, and Word.
Internally codenamed Kore-CLI, it targets enterprise developers who want an
agent with brakes: risk-gated approvals, managed git worktrees for dirty repos,
GDPR export flows, and a local observability dashboard. It runs on Compass's
own plan-gated model proxy or bring-your-own Anthropic/OpenAI/Ollama
credentials, and reaches editors through a first-party ACP server. Its public
traction is modest (~4.4k npm downloads a month) against large maker claims
("500+ enterprise teams") that nothing public corroborates.
```
