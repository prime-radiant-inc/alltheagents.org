# Paseo harness census — Part A research artifacts (2026-08-21..24)

Research pass over "paseo's list": the 43 coding agents the Paseo multiplexer
(getpaseo/paseo) can drive — 6 built-in providers (packages/protocol/src/provider-manifest.ts)
plus 37 ACP-catalog agents (packages/app/src/data/acp-provider-catalog.ts).
Tracking: Linear PRI-2924 (dossiers/adoption), PRI-2925 (plugin fields),
PRI-2926/2927 (special sauce), PRI-2928 (open-source flags), PRI-2929 (contacts).

- roster.tsv — the 43, with tiers and census-slug mapping (16 are new to the census)
- DOSSIER_SPEC.md / STANDARD_PROMPT.md — the research spec and the fixed
  differentiation-extraction prompt (PRI-2927)
- dossiers/<slug>.md — one factual dossier per harness: identity, adoption evidence
  (observable vs maker-claimed, dated, sourced), the six census plugin fields with
  evidence, claimed differentiation, company + publicly named leadership, open
  questions, sources, inclusion check
- standardized/<slug>.md — the standardized "what the maker claims is special"
  extraction, own-materials only, fixed 7-part schema
- master.tsv — one row per harness, 13 columns incl. census_fixes (what the census
  entry gets wrong) and eden_take (to be filled by Eden)
- TIER*_BRIEF.md — the per-wave briefs Eden reacts to for the subjective takes
- OPEN_SOURCE_FLAGS.md — the flagged open-source subset for Jesse's deep-dive tool
- CONTACT_TARGETS.md — company-level contact targets (public names only)

Inclusion result: 42 of 43 pass the "own agentic loop" test; Agoragentic fails
(MCP relay to a hosted marketplace, no LLM loop). Census corrections are per-row in
master.tsv census_fixes and per-dossier in section 6 — to be applied via PR batches
(PRI-2940 pipeline work first, so the generator does not clobber them).
