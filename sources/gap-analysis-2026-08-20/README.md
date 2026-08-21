# Gap analysis round 1 — 2026-08-20

Discovery sweep of channels the census had not covered (commercial/closed-source,
VS Code Marketplace + Open VSX, JetBrains Marketplace), diffed against
coding_agent_harnesses.tsv, sources/dropped.tsv, and cleanup.py DROP_NAMES.

- candidates_*.txt — raw candidates per channel (pipe-delimited: name|maker|url|extra|description|source)
- gap_diff.py — the matcher: python3 gap_diff.py <census.tsv> <dropped.tsv> candidates_*.txt
- gap_report_clean.tsv — ~410 candidates never seen by the census (151 commercial, 148 JetBrains, 111 VS Code/Open VSX)
- harness_gap_candidates_2026-08-20.csv — same, sorted by channel for sharing
- previously_dropped.tsv — candidates that matched prior deliberate drops
- match_log.tsv — candidates matched to existing entries, with the match reason

NOT yet verified or filtered by the inclusion test ("own agentic loop"); many marketplace
rows are wrapper/bridge plugins that will fail it. Tracking: Linear PRI-2939.
