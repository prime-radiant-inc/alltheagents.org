# Dossier: GLM Agent (proposed census_slug: glm-acp-agent)

Compiled 2026-08-21 (some sources report data through 2026-08-24 due to registry reporting windows). Facts only. Null convention: "null = not researched"; "False/none = researched and absent". NOT currently in the census — proposed new-entry frontmatter at the end. Small individual project — research kept proportionate.

## 1. Identity

- name: GLM Agent / glm-acp-agent (npm package and binary `glm-acp-agent`)
- maker: individual — **Stefan de Vogelaere** (GitHub **stefandevo**; npm author field with public email; GitHub profile: company "Devosoft", location Belgium, bio ".NET veteran, React developer") [S3][S4] (as-of 2026-08-21). Third-party project — no evidence of Zhipu/Z.AI affiliation (researched, absent) [S2].
- product URL: https://www.npmjs.com/package/glm-acp-agent (repo homepage field) | repo URL: https://github.com/stefandevo/glm-acp-agent [S1]
- license: Apache-2.0 (GitHub API and npm agree) [S1][S3]. open source? True; source_available: True [S1].
- first public: repo created 2026-04-27; first npm publish 1.0.0 on 2026-04-29 [S1][S3].
- latest release: 1.6.1, published 2026-08-24; repo last push 2026-08-24 — actively maintained, ~4 months old [S3][S1].
- what it is:
  - Form factor: an ACP agent server over stdio (newline-delimited JSON) for ACP-compatible editors — Zed recommended; Neovim/others possible; no standalone interactive CLI/TUI of its own [S2][S3].
  - Native agentic loop in TypeScript: own reasoning/tool-calling loop (default 20-turn cap), executes tools in-process, maps GLM function-calling results back into the loop, streams to the client [S2] (maker-described; architecture as documented).
  - Models: **locked to Zhipu/Z.AI GLM Coding Plan** — glm-5.3 (default, 1M context, thinking always on), glm-5-turbo (128K), glm-4.7 (200K), via https://api.z.ai/api/coding/paas/v4 only; uses the `openai` npm client against that endpoint [S2][S3].
  - Pricing: free, open source; requires a Z.AI Coding Plan subscription/API key (`Z_AI_API_KEY`) [S2].
  - Install: `npm install -g glm-acp-agent@latest`; Node.js 20+ [S2][S3].
  - Default autonomy: `default` mode prompts for writes and commands; `accept_edits` auto-approves writes; `bypass_permissions` fully silent [S2] (maker-described, not independently tested).
  - Language: TypeScript [S1].

## 2. Adoption evidence

| metric / claim | value | as-of | source | type |
|---|---|---|---|---|
| GitHub stars | 43 | 2026-08-21 | [S1] | independently observable |
| GitHub forks | 11 | 2026-08-21 | [S1] | independently observable |
| GitHub watchers (subscribers) | 0; open issues 0 | 2026-08-21 | [S1] | independently observable |
| npm downloads | 9,675/month (2026-07-25..08-23) | 2026-08-24 window | [S5] | independently observable (npm counts include CI/mirrors; still notable for a 4-month-old solo package) |
| Release cadence | 1.0.0 → 1.6.1 in ~4 months (2026-04-29 to 2026-08-24) | 2026-08-24 | [S3] | independently observable |
| Maker usage claims | none found | 2026-08-21 | [S2] | researched, absent |
| Funding / customers / community / press | none found | 2026-08-21 | [S2] | researched, absent |
| Ecosystem listing: Paseo | in Paseo's ACP catalog as a third-party ACP agent for Zhipu GLM models | 2026-08-21 | task brief | independently observable |
| Zhipu/Z.AI endorsement | none found — community project, not official | 2026-08-21 | [S2] | researched, absent |

## 3. Plugin interface (PRI-2925)

- mcp_support: **client (narrow, hardwired)** — spawns Zhipu's `@z_ai/mcp-server` over stdio for image analysis and uses the Coding Plan Web MCP for `web_search`/`web_reader`; no evidence of user-configurable arbitrary MCP servers (README documents only these built-ins) [S2] (as-of 2026-08-21). Evidence: https://github.com/stefandevo/glm-acp-agent
- plugin_support: **False (researched, absent)** — no skills, plugins, or extension system documented [S2].
- claude_code_plugin: **no** — no `.claude/`, CLAUDE.md, skills, or plugin-format support found [S2].
- subagents: **False** — "does not advertise skills, subagents, or hooks" [S2].
- hooks: **False** [S2].
- plan_mode: **False** — no plan mode; permission modes (`default`/`accept_edits`/`bypass_permissions`) are the only autonomy controls [S2].
- plugin_docs_url: none. config_docs_url: https://github.com/stefandevo/glm-acp-agent (README; env vars + Zed settings snippet).
- ACP support: **yes — ACP is the product's entire surface**: built on `@agentclientprotocol/sdk` ^0.20.0, claims "Full ACP compliance", session persistence, per-session model switching, streaming with chain-of-thought visibility [S2][S3].
- SDK: **False** — a binary/agent only, not published as a reusable library (bin entry `glm-acp-agent`) [S3].
- Built-in tools: read_file, write_file, list_files, run_command (local) + web_search, web_reader, image_analysis (via Z.AI MCP) — 7 total [S2].

## 4. Claimed differentiation (raw material for PRI-2927)

- tagline (repo description, verbatim): "ACP agent in TypeScript that uses the Z.AI / Zhipu AI GLM Coding Plan models (GLM-5.3, GLM-5 Turbo, GLM-4.7) as the reasoning core" [S1].
- maker claims (paraphrased):
  1. Brings GLM Coding Plan models into any ACP editor (Zed first) — the gap it fills [S2].
  2. "Full ACP compliance" with real-time streaming [S2].
  3. Thinking-mode integration: chain-of-thought/reasoning-token visibility in the editor [S2].
  4. Session persistence and per-session model switching among the three GLM models [S2].
  5. Graduated permission modes for writes and commands [S2].
  6. Native loop, not a wrapper: tools execute in the agent process [S2].
- audience: developers who subscribe to Z.AI's GLM Coding Plan and want to use it from an ACP-compatible editor [S2]. No other audience claims (researched, absent).

## 5. Company & contact targets (PRI-2929)

- Not a company product. Individual maintainer: **Stefan de Vogelaere** (GitHub stefandevo, Belgium; profile lists company "Devosoft" — appears to be his own consultancy; not researched further per individual-privacy instruction) [S4]. Public identities only.
- Contact paths the project offers: GitHub issues; npm author email is public in package metadata [S3].
- Funding stage: none/personal (researched, absent).
- Note for partnerships context: the relevant company behind the MODELS is Zhipu AI / Z.AI — but this project is not theirs.

## 6. Open questions / conflicts

- MCP configurability: whether users can attach arbitrary MCP servers (beyond the hardwired Z.AI vision/web MCP) is unverified — README documents only built-ins; the census field should say "client (built-in Z.AI MCP only)" unless source review shows a config path.
- Whether ACP-client-supplied MCP servers (a standard ACP feature) are honored: null (not researched).
- Edit granularity: README lists `write_file` but no `edit_file`/diff tool — whole-file writes vs surgical edits not verified from source.
- Dates: GitHub/npm snapshots reflect activity through 2026-08-24 (registry windows) though this dossier is dated 2026-08-21; the brief's "today" and live data diverge slightly — values recorded as returned.
- No Zhipu acknowledgment or listing of this agent found; whether Z.AI docs reference it: null (not searched).

## 7. Sources

1. [S1] https://api.github.com/repos/stefandevo/glm-acp-agent — stars, license, dates, description, topics
2. [S2] https://raw.githubusercontent.com/stefandevo/glm-acp-agent/main/README.md — architecture, tools, permission modes, models, claims
3. [S3] https://registry.npmjs.org/glm-acp-agent — versions, dates, author, deps, bin
4. [S4] https://api.github.com/users/stefandevo — maker public identity
5. [S5] https://api.npmjs.org/downloads/point/last-month/glm-acp-agent — npm downloads

## Inclusion check (Jesse's test)

**Yes** — glm-acp-agent implements its own agentic loop in TypeScript (own 20-turn reasoning/tool-calling loop, in-process file and shell tools, permission gating) around GLM models reached via an OpenAI-compatible client; it wraps a model API, not another vendor's agent [S2][S3]. It is single-vendor-locked (Z.AI Coding Plan only) and editor-bound (ACP server only, no standalone CLI), which the census entry should reflect.

## Proposed census frontmatter (per hc/agents/_TEMPLATE.md — do not write into hc/)

```yaml
name: "GLM Agent (glm-acp-agent)"
slug: "glm-acp-agent"
layout: "agent.njk"
category: "agent"
maker: "stefandevo"            # individual: Stefan de Vogelaere (Belgium); third-party, not Zhipu
license: "Apache-2.0"
url: "https://github.com/stefandevo/glm-acp-agent"
source_code_url: "https://github.com/stefandevo/glm-acp-agent"
source_available: true
homepage: "https://www.npmjs.com/package/glm-acp-agent"
docs_url: "https://github.com/stefandevo/glm-acp-agent"
download_url: "https://www.npmjs.com/package/glm-acp-agent"
install_method: "npm install -g glm-acp-agent (Node 20+); runs as ACP stdio server in Zed etc."
platforms: ["IDE"]             # ACP server for editors; no standalone CLI/TUI
autonomy_level: ["agentic"]
specialization: "general"
language: "TypeScript"
first_released: "2026-04-29"   # first npm publish (repo created 2026-04-27)
current_release: "2026-08-24"
maintained: "active"
mcp_support: "client (built-in Z.AI web/vision MCP only; arbitrary servers unverified)"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no (permission modes only)"
plugin_docs_url: null
config_docs_url: "https://github.com/stefandevo/glm-acp-agent"
model_providers: "locked — Zhipu/Z.AI GLM Coding Plan (glm-5.3, glm-5-turbo, glm-4.7)"
pricing: "BYOK"                # free agent; requires Z.AI Coding Plan key
github_stars: 43
sources: ["paseo-acp-catalog"]
last_verified: "2026-08-21"
what_makes_it_special: "The community bridge that puts Zhipu's GLM Coding Plan models into ACP editors like Zed: a native TypeScript tool-calling loop with thinking-mode visibility and graduated permissions, locked to Z.AI's coding endpoint."
```
