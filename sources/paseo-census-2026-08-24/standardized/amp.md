# Standardized differentiation extraction: Amp (census_slug: amp)

Run 2026-08-21 against the maker's own materials only (listed under Sources).

1. One-sentence self-description: Amp calls itself "the frontier agent" — a multi-model coding agent that runs on the web, in the terminal, on your phone, and on remote machines ("orbs") that keep working unattended, built by an independent agent research lab for people who want the most out of an agent rather than keeping their old ways. (homepage; manual "Why Amp?"; press kit)

2. Claimed differentiators (by prominence):
   - Frontier-first and opinionated: Amp moves where the models go, deletes old workflows, legacy features and stale assumptions ("no backcompat"), and keeps only features the team itself uses and loves. Kind: workflow / trust-safety (of product direction). https://ampcode.com ; https://ampcode.com/manual
   - Orbs and agents anywhere: threads run on remote machines that keep working after the laptop closes, can be started from web, terminal, Slack or phone, picked up from any device, wake on schedules and react to outside events. Kind: capability / workflow. https://ampcode.com ; https://ampcode.com/manual/orbs ; https://ampcode.com/news/subscriptions
   - Multi-model by design: GPT-5.6, Claude Fable 5, GLM-5.2, Gemini and others are routed per task ("Dial" modes low/medium/high/ultra) and per subagent, with the claim that the individual model matters less than task difficulty, context and review. Kind: model. https://ampcode.com/manual ; https://ampcode.com/models ; https://ampcode.com/news/who-cares-about-the-model
   - No approval prompts; policy via plugins: Amp runs tools without asking by default, replacing step-by-step approvals with a TypeScript plugin API that hooks events, adds tools, bundles skills and standardizes policy, shareable across a workspace ("inspired by Pi"). Kind: capability / workflow. https://ampcode.com/manual ; https://ampcode.com/news/neo ; https://ampcode.com
   - Subscriptions with generous included usage: $20 and $200 monthly plans include orb hours and agent usage, pay-as-you-go at provider API rates with zero markup for individuals, and linked ChatGPT or X subscriptions add usage at no per-token fee. Kind: price. https://ampcode.com/pricing ; https://ampcode.com/news/subscriptions

3. Stated audience: "people who want the most out of an agent, rather than keeping their old ways" (homepage); developers and teams who want to be a year ahead (Sourcegraph/Amp split post); those willing to "travel light" beyond editor integration (coding-agent-is-dead post); enterprises via SSO, managed settings and minimal data retention (manual Enterprise section); traditional-economy companies via Amp Labs. https://ampcode.com ; https://sourcegraph.com/blog/why-sourcegraph-and-amp-are-becoming-independent-companies ; https://ampcode.com/news/the-coding-agent-is-dead ; https://ampcode.com/manual ; https://ampcode.com/news/amp-labs

4. Positioning against others: alludes to the category of tools that require step-by-step approvals and to "coding agents" as an obsolete category ("The Coding Agent Is Dead", killing its own editor extension); homepage testimonials name Claude Code, Codex and Cursor Agent as tools users left; plugin system credited as "Inspired by Pi". https://ampcode.com/news/subscriptions ; https://ampcode.com/news/the-coding-agent-is-dead ; https://ampcode.com

5. Evidence the maker offers:
   - 500,000 messages in roughly the first week after public launch (2025-05-20). https://ampcode.com/news/500k
   - "Amp is profitable" at spinout (2025-12-02); no revenue figure. https://ampcode.com/news/amp-inc
   - Mode-share data after swapping the default model: medium carried two-thirds of new threads within a week, Dial modes 93%, 69% of users never changed the default (2026-07-29). https://ampcode.com/news/who-cares-about-the-model
   - Rebuild performance: 79% less CPU, 70% less idle memory (2026-05-06). https://ampcode.com/news/neo
   - Customer/partner: Westpac via Amp Labs (2026-07-29). https://ampcode.com/news/amp-labs-westpac
   - Homepage testimonials from five named X users; a live "which modes are people using" chart without absolute numbers; "Model Cards" with evals and caveats. https://ampcode.com ; https://ampcode.com/models
   - No public benchmark scores (SWE-bench, Terminal-Bench) on the homepage, manual or models page.

6. Notable silences: no plan/read-only mode; no Agent Client Protocol mention; no open-source or source-availability claim (proprietary, no repo); no absolute user, revenue or token counts; no benchmark placements; no sandboxing of local tool execution (orbs are the isolation story; manual warns about untrusted inputs); no on-prem/self-hosted control plane; no CLAUDE.md/Claude Code plugin compatibility claim beyond reading .claude/skills and a Claude-Code-shaped stream JSON.

7. Confidence: high — materials are extensive and consistent (homepage, manual, models, pricing, dated news posts and a spinout announcement), and the positioning is stated explicitly and repeatedly; the main ambiguity is that several claims are framed rhetorically ("the coding agent is dead") rather than as measurable differentiators, and no user or revenue figures are offered.

Sources:
- https://ampcode.com (homepage)
- https://ampcode.com/manual (Owner's Manual)
- https://ampcode.com/manual/orbs
- https://ampcode.com/manual/sdk
- https://ampcode.com/manual/appendix
- https://ampcode.com/models
- https://ampcode.com/pricing
- https://ampcode.com/press-kit
- https://ampcode.com/security
- https://ampcode.com/news (index)
- https://ampcode.com/news/amp-inc
- https://ampcode.com/news/the-coding-agent-is-dead
- https://ampcode.com/news/neo
- https://ampcode.com/news/drop-the-neo
- https://ampcode.com/news/subscriptions
- https://ampcode.com/news/who-cares-about-the-model
- https://ampcode.com/news/amp-labs
- https://ampcode.com/news/amp-labs-westpac
- https://ampcode.com/news/amp-free
- https://ampcode.com/news/amp-free-is-full-for-now
- https://ampcode.com/news/npm-package-changes
- https://ampcode.com/news/500k
- https://ampcode.com/notes/how-i-use-amp
- https://sourcegraph.com/blog/why-sourcegraph-and-amp-are-becoming-independent-companies (maker's former parent, co-authored by Amp's CEO)
