# Standardized differentiation extraction: Agoragentic (census_slug: agoragentic)

Run 2026-08-24 against official materials only (agoragentic.com, npm package metadata, mcp/README in rhein1/agoragentic-integrations). NOTE: subject fails the census inclusion test (not a coding agent); this extraction records how the maker positions it regardless.

1. **One-sentence self-description:** A "control and proof layer for autonomous agents" — a governed runtime (Triptych OS) plus a marketplace where agent services are discovered, invoked, and paid per call in USDC, with mandates, budgets, approval gates, and receipts.

2. **Claimed differentiators:**
   - Governance and accountability: mandates, permission scoping, budgets, approval gates, recorded execution — "autonomy without accountability is not a product" (kind: trust-safety). Source: https://agoragentic.com.
   - Agent commerce with receipts: paid execution settled via x402 (HTTP 402) USDC micropayments on Base, "receipt-backed status" (kind: capability/integration). Source: https://agoragentic.com + mcp/README.
   - "Execute-first routing" with governed handoffs across agents/services (kind: workflow). Source: https://github.com/rhein1/agoragentic-integrations description.
   - Broad protocol/framework surface: MCP relay, ACP mode, A2A/x402 adapters, LangChain/CrewAI integrations (kind: integration/openness). Source: npm package keywords + integrations repo.
   - Verified marketplace listings ("84 approved active listings") (kind: trust-safety). Source: https://agoragentic.com.

3. **Stated audience:** builders and operators of autonomous agents who need oversight, and developers wiring paid agent capabilities into frameworks; not stated by role/team size. Source: https://agoragentic.com, /developers/.

4. **Positioning against others:** implicitly against ungoverned autonomy ("autonomy without accountability is not a product"); the site states it is NOT a coding agent itself — it is infrastructure. No competitor named.

5. **Evidence offered for claims:** marketplace counters on the site — "84 approved active listings", "1,164 successful public listing calls"; no benchmarks or customer names.

6. **Notable silences:** no LLM/model story at all (the relay calls no LLM), no code-editing capability, no plan mode/hooks/subagents, no company or team identity, no pricing tiers beyond per-call fees — and purchasing is currently disclosed as frozen ("platform custody policy is frozen").

7. **Confidence:** medium — the materials are consistent and first-hand (site + package + README), but the platform is young, partly non-operational (purchasing frozen), and run by a pseudonymous founder, so positioning may shift quickly.

Sources: https://agoragentic.com; https://registry.npmjs.org/agoragentic-mcp; https://github.com/rhein1/agoragentic-integrations (mcp/README.md)
