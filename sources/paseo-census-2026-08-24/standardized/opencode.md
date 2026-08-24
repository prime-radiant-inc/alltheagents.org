# Standardized differentiation extraction: OpenCode (census_slug: opencode)

Prompt: STANDARD_PROMPT.md v1 (PRI-2927). Inputs: the maker's own materials only (listed under
Sources). Run 2026-08-21.

1. One-sentence self-description:
   An open-source AI coding agent that works in the terminal, IDE, or desktop, with free
   models included or any model from any provider connected by the user.
   (https://opencode.ai/, README)

2. Claimed differentiators (ordered by prominence in the materials):
   - Open source, MIT-licensed, the whole agent is the public repo and the desktop/IDE/web
     surfaces are included — kind: openness — https://opencode.ai/, README
   - Provider-agnostic: "75+ LLM providers" via Models.dev, local models, and login with
     existing Claude Pro/Max, ChatGPT Plus/Pro or GitHub Copilot subscriptions; free models
     included so no separate subscription is required to start — kind: model —
     https://opencode.ai/, https://opencode.ai/docs/providers/
   - Privacy: the agent does not store code or context data; runs locally or via direct
     provider calls; enterprise deployment with SSO, central config and internal AI gateway —
     kind: trust-safety — https://opencode.ai/, https://opencode.ai/docs/enterprise/
   - Architecture/workflow: LSP auto-loaded for the model; client/server design with
     multi-session, shareable session links, headless server with OpenAPI, local web UI,
     ACP for editors, SDK, GitHub Action — kind: capability/integration —
     https://opencode.ai/, https://opencode.ai/docs/server/, https://opencode.ai/docs/acp/
   - Curated paid model access: Zen = tested/benchmarked models for coding agents at
     pay-as-you-go with "zero markups"; Go = $10/month (first month $5) open-weight model
     subscription with "generous limits" — kind: price/model — https://opencode.ai/zen,
     https://opencode.ai/docs/zen/, https://opencode.ai/go, https://opencode.ai/docs/go/

3. Stated audience:
   Developers writing code in terminal/IDE/desktop (https://opencode.ai/); Go is aimed at
   "programmers around the world" wanting affordable model access (https://opencode.ai/go);
   Enterprise is aimed at organizations that need code and data to stay inside their own
   environment with SSO and internal gateways (https://opencode.ai/docs/enterprise/).
   No team size, language or stack named.

4. Positioning against others:
   No competitor harness is named as a competitor. The materials reference Claude, GPT,
   Gemini, ChatGPT Plus/Pro and GitHub Copilot only as models/subscriptions OpenCode can use
   (https://opencode.ai/). Docs mention Claude Code only as a compatibility target (reads
   CLAUDE.md and .claude/skills; `OPENCODE_DISABLE_CLAUDE_CODE`) (https://opencode.ai/docs/rules/,
   https://opencode.ai/docs/skills/). Category disclaimer: Zen is described as "completely
   optional" and not required to use OpenCode (https://opencode.ai/docs/zen/). Otherwise
   not claimed.

5. Evidence the maker offers:
   - Homepage counters: "over 195,000 GitHub stars, 950 contributors, and over 13,000 commits"
     and "over 16M developers every month" (https://opencode.ai/)
   - Go page repeats "195K GitHub stars" (https://opencode.ai/go)
   - Zen: states models were tested and benchmarked with model teams/providers, but no
     benchmark numbers are published (https://opencode.ai/docs/zen/)
   - Demo video on the homepage (https://opencode.ai/)
   - No customer names or logos; no benchmark scores.

6. Notable silences:
   - No SWE-bench / Terminal-bench or any quantitative benchmark result for the harness.
   - No sandboxing / container isolation claim for tool execution (permissions are
     allow/ask/deny; `.env` blocked; no sandbox described).
   - No plugin marketplace or registry (plugins are npm packages or local files).
   - No native lifecycle "hooks" config (only plugin-API events).
   - No hosted/cloud background-agent offering (GitHub Action runs in the user's runners).
   - No pricing/ETA for "Black"; enrollment "temporarily paused".
   - No team/about page, no funding or company-size statements on opencode.ai or anoma.ly.
   - Multi-model and MCP are documented but not headlined as differentiators beyond
     "75+ providers".

7. Confidence: **high** that sections 1-5 reflect the maker's positioning — the homepage,
   README, docs intro, Zen/Go/Enterprise pages all repeat the same three themes (open source,
   any model/provider, privacy); the only gap is the absence of an official launch blog post
   (opencode.ai/blog returns 404), so positioning is taken from site and docs rather than a
   launch narrative.

Sources (official materials only, fetched 2026-08-21):
- https://opencode.ai/ (homepage, FAQ headings, counters)
- https://raw.githubusercontent.com/anomalyco/opencode/dev/README.md
- https://opencode.ai/docs/ (intro)
- https://opencode.ai/docs/providers/
- https://opencode.ai/docs/zen/ and https://opencode.ai/zen
- https://opencode.ai/docs/go/ and https://opencode.ai/go
- https://opencode.ai/black
- https://opencode.ai/docs/enterprise/ and https://opencode.ai/enterprise
- https://opencode.ai/docs/server/, https://opencode.ai/docs/sdk/, https://opencode.ai/docs/acp/,
  https://opencode.ai/docs/github/, https://opencode.ai/docs/web/, https://opencode.ai/docs/ide/
- https://opencode.ai/docs/agents/, https://opencode.ai/docs/permissions/,
  https://opencode.ai/docs/plugins/, https://opencode.ai/docs/mcp-servers/,
  https://opencode.ai/docs/rules/, https://opencode.ai/docs/skills/
- https://opencode.ai/changelog
- https://anoma.ly/
