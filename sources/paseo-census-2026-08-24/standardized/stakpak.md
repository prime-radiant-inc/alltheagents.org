# Standardized differentiation extraction: Stakpak (census_slug: stakpak)

Run 2026-08-24 against official materials only (stakpak.dev homepage, repo README, gitbook docs intro + rulebooks page).

1. **One-sentence self-description:** An open-source DevOps agent that runs continuously on your own machines to keep applications operational — healing incidents, maintaining infrastructure, and optimizing cost — asking for a human only when needed.

2. **Claimed differentiators:**
   - Autonomous 24/7 operations ("Ship your code, on autopilot"; "lives on your machines 24/7 … only pings when it needs a human") (kind: capability/workflow). Source: https://stakpak.dev + https://github.com/stakpak/agent README.
   - Enterprise-grade security architecture: Warden sandbox with Cedar policy enforcement, secret substitution of 210+ secret types before LLM processing, mTLS, audit logs and session replay (kind: trust-safety). Source: https://stakpak.dev.
   - Runs on-premises as a single binary, no cloud lock-in (kind: openness/trust-safety). Source: https://stakpak.dev.
   - Rulebooks — markdown SOPs that make the agent follow your org's procedures "just like a teammate would" (kind: workflow). Source: https://stakpak.gitbook.io/docs/how-it-works/rulebooks.md.
   - Multi-provider models: BYO Anthropic/OpenAI/Gemini keys, hosted Stakpak API, or local OpenAI-compatible endpoints (kind: model/openness). Source: README.

3. **Stated audience:** development teams and DevOps professionals managing production applications who want autonomous incident response without giving up control or compliance. Source: https://stakpak.dev.

4. **Positioning against others:** alludes to cloud-hosted, lock-in tools as the category it is not ("no cloud lock-in", on-prem single binary); a "comparisons" docs section exists. No competitor named on the pages consulted.

5. **Evidence offered:** "5,000+ developers" figure and a customer logo wall (Paymob, Mistral AI, Writer, Breadfast, Overmind, Replicated, Daytona, Vectara, and others) on https://stakpak.dev; no benchmarks or case-study documents on the pages consulted.

6. **Notable silences:** no mention of Claude Code/CLAUDE.md/AGENTS.md compatibility, lifecycle hooks, a dedicated plan/read-only mode, a plugin marketplace, pricing tiers, or SWE-bench-style benchmarks; the Vercel acquisition's impact on the roadmap is not addressed in the docs.

7. **Confidence:** high — materials are substantial and consistent (marketing site, long README, real docs), and the security-first DevOps-autonomy positioning is uniform across all of them.

Sources: https://stakpak.dev/; https://github.com/stakpak/agent (README); https://stakpak.gitbook.io/; https://stakpak.gitbook.io/docs/how-it-works/rulebooks.md
