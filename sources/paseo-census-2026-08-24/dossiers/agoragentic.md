# Dossier: Agoragentic (census_slug: agoragentic)

Compiled 2026-08-24 (task-dated 2026-08-21). Facts only. Null convention: "null = not researched"; "False/none = researched and absent". NOT in the census. THE HEADLINE: this is not a coding agent — it FAILS Jesse's inclusion test (see Inclusion check). It is an agent-services marketplace/relay reached over MCP, with an `--acp` flag that merely re-exposes the same marketplace tools over ACP.

## 1. Identity

- name: Agoragentic (npm package `agoragentic-mcp`; platform runtime branded "Triptych OS (Agent OS)")
- maker: individual — npm maintainer and GitHub user **rhein1** (profile name "Rhein1 / Agoragentic", bio "Agoragentic founder building Triptych OS (Agent OS), execute-first agent routing", blog agoragentic.com, 7 followers, account since 2023-07-26; no real name or location published — pseudonymous) [S5] (as-of 2026-08-24). npm author field: "Agoragentic <support@agoragentic.com>" [S2]. No registered-company evidence found (researched, absent). Org form: individual.
- product URL: https://agoragentic.com | repo URL: https://github.com/rhein1/agoragentic-integrations (the npm package lives in its `mcp/` directory) [S2][S3]
- license: MIT (npm package and integrations repo) [S2][S3]. The hosted Router/Marketplace backend is closed — the package is a "stdio relay … for Agoragentic's hosted Triptych OS … Router / Marketplace" [S2]. source_available: partial — relay/adapters open, platform closed.
- first public release: npm `agoragentic-mcp` created 2026-03-02; integrations repo created 2026-02-27 [S2][S3]
- latest release: npm 1.3.6, last modified 2026-07-23 (12 versions); repo pushed 2026-08-24 [S2][S3] (as-of 2026-08-24)
- what it is:
  - Site self-description: "Control and proof layer for autonomous agents" — mandates, permission scoping, budgets, approval gates, execution recording; tagline "Control and Proof for Autonomous Agents" (verbatim) [S1].
  - Marketplace: listings of agent services (e.g. "Text Summarizer" $0.01 USDC, "Web Scraper" $0.01 USDC, free devtools/creative listings), paid execution settled in USDC via x402 (HTTP 402) micropayments on Base [S1][S4].
  - The npm package: a stdio MCP relay/fallback server exposing marketplace tools — `agoragentic_register`, `agoragentic_search`, `agoragentic_preview_x402`, `agoragentic_match`, `agoragentic_execute`, `agoragentic_execute_status` — against the hosted router [S4].
  - `--acp` mode: "ACP-compatible clients can launch the same relay through stdio" with baseline session flow plus tools/list and tools/call forwarding — i.e., the SAME marketplace tools over ACP, no LLM loop [S4].
  - No LLM anywhere in the package: no Anthropic/OpenAI/any provider keys; only `AGORAGENTIC_API_KEY` for its own service; zero runtime dependencies in the npm package [S4][S2].
  - Pricing: per-call USDC micropayments for paid listings; note the site currently states "Purchasing is temporarily unavailable while the platform custody policy is frozen" [S1] (as-of 2026-08-24).
  - Install: `npx agoragentic-mcp` (bin `agoragentic-mcp`) [S2].

## 2. Adoption evidence

| metric / claim | value | as-of | source | type |
|---|---|---|---|---|
| npm downloads `agoragentic-mcp` | 1,000/week; 3,238/month | 2026-08-24 | [S2] | independently observable (relay packages attract CI/bot noise; treat as ceiling) |
| GitHub stars (integrations repo) | 29; forks 5 | 2026-08-24 | [S3] | independently observable |
| Marketplace size | "84 approved active listings"; "1,164 successful public listing calls" (site) | 2026-08-24 | [S1] | maker-claimed |
| "174+ AI capabilities" (claim in Paseo catalog framing) | NOT found on the current site — site says 84 approved active listings; conflict noted in section 6 | 2026-08-24 | [S1] | unverified/conflicting |
| Maker's other repos | ~39 public repos, nearly all 0-2 stars (harness-core, ecf-core, micro-ecf, premortem CLI, etc.) | 2026-08-24 | [S5] | independently observable |
| Funding / customers / press / community / benchmarks | none found | 2026-08-24 | [S1][S5] | researched, absent |

## 3. Plugin interface (PRI-2925)

These fields presume a coding agent; recorded for completeness:

- mcp_support: **server** — the package IS an MCP server/relay (that is its entire function); it is not an MCP client hosting tools for its own loop (it has no loop) [S4][S2].
- plugin_support: False — n/a; the "marketplace" is of remote paid services, not local agent plugins [S1][S4].
- claude_code_plugin: False (researched, absent). subagents: False. hooks: False (approval gates/budgets exist platform-side as governance, not agent lifecycle hooks) [S1]. plan_mode: False.
- plugin_docs_url: https://agoragentic.com/developers/ ; config_docs_url: https://agoragentic.com/docs.html (+ /openapi.yaml) [S1].
- ACP support: **yes, but hollow** — `--acp` serves the same marketplace tool relay over ACP stdio ("baseline session flow plus tools/list and tools/call forwarding"); there is no agent behind it [S4].
- SDK: the integrations repo advertises adapters for agent frameworks (MCP/A2A/x402, LangChain/CrewAI keywords) [S3][S2] — SDK-for-the-marketplace, not an agent SDK.

## 4. Claimed differentiation (raw material for PRI-2927)

- tagline (verbatim): "Control and Proof for Autonomous Agents" [S1]
- maker claims (paraphrased):
  1. Governance/"proof" layer: mandates, scoped permissions, budgets, approval gates, recorded execution — "autonomy without accountability is not a product" (site, verbatim fragment) [S1].
  2. Agent commerce: paid agent services with USDC/x402 micropayment settlement on Base, receipt-backed status [S1][S4].
  3. "Execute-first routing" with governed handoffs and receipts (integrations repo description) [S3].
  4. Broad protocol surface: MCP, A2A, x402, ACP keywords; adapters for LangChain/CrewAI [S2][S3].
- audience: builders/operators of autonomous agents wanting oversight + monetization; agent-framework users wiring in paid capabilities [S1][S3].

## 5. Company & contact targets (PRI-2929)

- No company entity found; the project presents as a pseudonymous individual founder ("Rhein1"). Public contact: support@agoragentic.com [S5][S2]. No team page, no named leadership (researched, absent). Funding: none found.

## 6. Open questions / conflicts

- **"174+ AI capabilities" vs "84 approved active listings"**: the figure quoted in the Paseo/census framing does not appear on the current site; either stale, inflated, or counting unapproved listings. Use 84 (maker-claimed) with date.
- Purchasing is currently frozen ("platform custody policy is frozen") — the paid-marketplace core is not operational as-of 2026-08-24 [S1].
- npm 1,000/week vs 29 stars and 1,164 lifetime listing calls: the download number is almost certainly dominated by automation; the site's own call counter is the more honest scale signal.
- Whether any legal entity exists behind "Agoragentic" — unknown (null). Founder is pseudonymous.
- The hosted Triptych OS router's internals (and whether any LLM is used server-side for "match") — unknown; irrelevant to inclusion since the product neither edits code nor runs a coding loop.
- Paseo listing it among ACP "agents" is technically true at the protocol level (`--acp` speaks ACP) but categorically misleading — it is a tool relay, not an agent.

## 7. Sources

1. [S1] https://agoragentic.com — tagline, self-description, marketplace stats (84 listings, 1,164 calls), USDC, custody freeze, docs links
2. [S2] https://registry.npmjs.org/agoragentic-mcp + api.npmjs.org downloads — package description, MIT, bin, versions, dates, author, maintainer rhein1, keywords, zero deps, 1,000/wk
3. [S3] https://api.github.com/repos/rhein1/agoragentic-integrations — stars, MIT, dates, description ("adapters and discovery catalog")
4. [S4] https://raw.githubusercontent.com/rhein1/agoragentic-integrations/main/mcp/README.md — tool list, --acp = relay over ACP, no LLM keys, x402 payment flow
5. [S5] https://api.github.com/users/rhein1 + repo list — founder identity (pseudonymous), other near-zero-star repos

## Inclusion check (Jesse's test)

**NO — fails.** Agoragentic cannot "create and modify software using an LLM with its own agentic loop": the shipped package is a stdio MCP relay to a hosted services marketplace (register/search/quote/execute/status tools), it calls no LLM (no provider keys, zero dependencies), edits no files, and its `--acp` mode is explicitly "the same relay" forwarding tools/list and tools/call over ACP — protocol compliance without an agent behind it [S4][S2]. Recommend EXCLUDING it from the coding-agent census (or listing it only in a non-agent "ecosystem/marketplace" annex); the frontmatter below is provided only in case an entry is still wanted, and neither census category (agent/multiplexer) genuinely fits.

## Proposed census entry (conditional — recommend exclusion; per hc/agents/_TEMPLATE.md)

```yaml
---
name: "Agoragentic"
slug: "agoragentic"
layout: "agent.njk"
category: "multiplexer"      # least-bad fit: it routes to OTHER agents/services and does not code; a true fit would need a new category (e.g. "marketplace")
maker: "rhein1"              # new makers.json record: maker_type individual (pseudonymous "Rhein1"), country null, makes_models false, revenue_model []  # per-call USDC fees fit neither tokens nor subscriptions
license: "MIT (relay/adapters); hosted platform closed"
url: "https://agoragentic.com"
source_code_url: "https://github.com/rhein1/agoragentic-integrations"
source_available: "partial"
homepage: "https://agoragentic.com"
docs_url: "https://agoragentic.com/docs.html"
download_url: "https://www.npmjs.com/package/agoragentic-mcp"
install_method: "npx agoragentic-mcp"
platforms: ["CLI"]
autonomy_level: []           # none — no agentic loop of its own
specialization: "general"    # n/a — not a coding agent; agent-services marketplace + governance layer
language: "JavaScript"
first_released: "2026-03-02"
current_release: "2026-07-23"   # npm 1.3.6
maintained: "active"
mcp_support: "server (stdio relay to hosted marketplace)"
plugin_support: false
claude_code_plugin: false
subagents: false
hooks: false
plan_mode: false
plugin_docs_url: "https://agoragentic.com/developers/"
config_docs_url: "https://agoragentic.com/docs.html"
model_providers: "none — calls no LLM itself"
pricing: "usage (per-call USDC/x402 micropayments; purchasing currently frozen)"
github_stars: "29"
sources: ["paseo-acp-catalog"]
last_verified: "2026-08-24"
what_makes_it_special: "Not a coding agent: an MCP/ACP relay into a USDC-micropayment marketplace of hosted agent services with governance ('control and proof') framing — fails the census inclusion test."
---
```
