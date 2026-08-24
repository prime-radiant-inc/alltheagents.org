# Paseo harness census — dossier spec (v1, 2026-08-21)

One dossier per harness, written to dossiers/<census_slug>.md. Facts only, every
non-obvious fact carries a source URL and an as-of date. Do NOT write prose
opinions; the narrative and the subjective take are written later from this file.
Null convention: "null = not researched", "False/none = researched and absent" —
say which one you mean.

## 1. Identity
- name (canonical product name) | maker (company or individual; org form:
  company / individual / community; HQ country if public) | product URL | repo URL |
  license | open source? (source_available: True/False/partial — say what is open)
- first public release (date + source) | latest release (version + date + source)
- what it is, in 3-5 factual bullets: form factor(s) (CLI / IDE / web / desktop /
  background-autonomous), models it runs on (locked to one vendor or BYO / which),
  pricing model, how it is installed, default autonomy (does it ask before edits /
  shell / etc.).

## 2. Adoption evidence (the core of PRI-2924)
Each item = metric or claim | value | as-of date | source URL. Collect whatever exists:
- GitHub stars, forks, contributors, commit cadence (last 90 days)
- package downloads: npm weekly, PyPI monthly, Homebrew, crates.io, marketplace installs
- usage numbers stated by the maker (users, paying customers, tokens, PRs merged)
- public customers, case studies, logos on the site (list names)
- funding, valuation, acquisition (with source)
- community size: Discord members, subreddit, GitHub discussions volume
- third-party signals: benchmark placements (SWE-bench etc.), press coverage, notable
  public users/endorsements
Mark each item "maker-claimed" vs "independently observable".

## 3. Plugin interface (PRI-2925) — fill the six census fields, each with evidence URL
- mcp_support: can it act as an MCP client (use MCP servers)? client/server/both/none
- plugin_support: does it have its own plugin/extension/skills system? what kind
  (marketplace? skills dirs? extensions API?) + docs link
- claude_code_plugin: is it compatible with the Claude Code plugin format / marketplace?
  (yes / no / partial — e.g. reads .claude/skills or CLAUDE.md but not plugins)
- subagents: can it spawn sub-agents? how
- hooks: lifecycle hooks (pre/post tool, on-stop, etc.)?
- plan_mode: a read-only / planning mode?
- plugin_docs_url, config_docs_url
Also note: ACP support (Agent Client Protocol) yes/no, SDK availability.

## 4. Claimed differentiation (raw material for the standardized prompt, PRI-2927)
- tagline (verbatim, short) + URL
- the maker's own "why us / what makes X different" claims, paraphrased, up to 8
  bullets, each with URL (README, homepage, docs intro, launch post, changelog)
- who they say it is for (audience) + URL
- keep quotes to a few words; paraphrase everything else

## 5. Company & contact targets (PRI-2929) — company-level only
- company legal name, HQ, approx size (public sources), funding stage
- publicly named leadership relevant to partnerships: CEO, CTO, head of product,
  DevRel / developer relations lead, head of partnerships/ecosystem — ONLY people
  the company itself names publicly (team page, press releases, launch blog bylines).
  Name + title + the public URL where named. No LinkedIn scraping, no private
  individuals, no personal contact details.

## 6. Open questions / conflicts
- anything the sources disagree on, anything you could not verify, anything where
  the existing census entry looks wrong (quote the field and what you found)

## 7. Sources
- numbered list of every URL consulted with a 3-6 word note on what it provided

## Inclusion check (Jesse's test)
State in one line whether this tool "can create and modify software using an LLM,
with its own agentic loop" — yes / no / unsure, with one sentence of evidence. (A thin
ACP wrapper around someone else's agent = no for the wrapper, yes for the wrapped agent.)
