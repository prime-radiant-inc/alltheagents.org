# Harness Census

Comprehensive census of coding agent harnesses — systems that let an LLM autonomously write, modify, debug, or run code.

**1101 harnesses catalogued.** Browse the live site at [harness-census](https://prime-radiant-inc.github.io/harness-census/).

## Contents

- `coding_agent_harnesses.tsv` — tab-separated data (1101 entries)
- `coding_agent_harnesses.csv` — comma-separated data (1101 entries)
- `coding_agent_harnesses.md` — markdown table with summary
- `agents/` — individual entry pages (Markdown with YAML frontmatter)
- `_data/agents.json` — JSON data for client-side search
- `_layouts/`, `*.njk` — Eleventy templates
- `css/style.css` — dark theme stylesheet
- `scripts/generate_pages.py` — TSV-to-markdown page generator
- `sources/` — raw source data, scripts, and intermediate files

## Website

The site is built with [Eleventy](https://www.11ty.dev/) and deployed to GitHub Pages via GitHub Actions.

### Local development

```bash
npm install
npx @11ty/eleventy --serve
```

This starts a local dev server at `http://localhost:8080`.

### Build

```bash
npm install
npx @11ty/eleventy
```

Output goes to `_site/`.

## Columns

| Field | Description |
|-------|-------------|
| name | Name of the harness |
| category | Entry bucket: harness, multiplexer, tool, or something-else |
| maker | Company or individual that makes it |
| license | License (MIT, Apache-2.0, Proprietary, etc.) |
| url | Primary URL |
| source_code_url | URL to source code if available |
| source_available | Whether source code is available |
| what_makes_it_special | 1-2 sentence description |
| platforms | CLI, IDE, Web, Desktop, Autonomous |
| first_released | First release date (YYYY-MM-DD) |
| current_release | Most recent release/update date |
| stars | GitHub stars |
| language | Primary programming language |
| homepage | Homepage URL |
| source_list | Which source list(s) it was found in |

## Methodology

Built from 15 "awesome" aggregation lists, 5 rounds of GitHub topic/keyword searches, GitHub API enrichment of 1,516 repos, and manual research of 25 commercial products.
