# Standardized differentiation-extraction prompt (PRI-2927, v1, 2026-08-21)

Run the SAME prompt for every harness. Inputs are the harness's own materials only
(README, homepage, docs landing/intro, official launch post, pricing page). Output
goes to standardized/<census_slug>.md using exactly the schema below so answers are
apples-to-apples across harnesses.

---
You are analyzing the official materials of a coding-agent harness named {NAME}.
Use ONLY the supplied official materials (listed under Sources). Do not use outside
knowledge or other tools' materials. Where the materials are silent, write "not claimed".

Answer in exactly this schema:

1. One-sentence self-description: how the maker describes the product in one sentence,
   paraphrased (no marketing adjectives kept unless they are the claim).
2. Claimed differentiators: up to 5 bullets. For each: the claim in plain words, the
   kind of claim (capability / model / workflow / price / openness / performance /
   integration / trust-safety / audience), and the source URL. Order by how prominently
   the maker makes the claim.
3. Stated audience: who the maker says it is for (role, team size, language/stack),
   with URL; or "not claimed".
4. Positioning against others: does the maker name or clearly allude to competitors
   or a category it is NOT? Quote at most a few words, with URL; or "not claimed".
5. Evidence the maker offers for its claims: benchmarks, numbers, customer names,
   demos — listed with URLs; or "none offered".
6. Notable silences: common coding-agent capabilities the materials do not mention
   (e.g. MCP, plan mode, multi-model, sandboxing, enterprise controls, open source).
7. Confidence: high / medium / low that sections 1-5 reflect the maker's actual
   positioning, and one sentence on why (e.g. sparse materials, docs-only, no launch post).

Sources: {LIST OF URLS CONSULTED}
---
