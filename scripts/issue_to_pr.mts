// The mechanical steps of docs/issue-to-pr.md. Node 24+ runs this file directly.
//
//   node scripts/issue_to_pr.mts list                   issues waiting: "N<TAB>add|fix<TAB>title"
//   node scripts/issue_to_pr.mts fetch <N>              gh issue -> work/issue-<N>/issue.json
//   node scripts/issue_to_pr.mts write <verified.json>  new entry file + ledger row + maker record
//   node scripts/issue_to_pr.mts pr <N> [--base main]   branch, commit, push, open the PR
import { execFileSync } from "node:child_process";
import { existsSync, mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const TEMPLATES: Record<string, string> = { add: ".github/ISSUE_TEMPLATE/add-agent.yml", fix: ".github/ISSUE_TEMPLATE/update-agent.yml" };
// agents/_TEMPLATE.md order, with `stars` where the template says `github_stars`
// because every existing entry uses `stars`.
const FIELD_ORDER = [
  "name", "slug", "layout", "category", "maker", "license", "url", "source_code_url",
  "source_available", "homepage", "docs_url", "download_url", "install_method", "platforms",
  "autonomy_level", "specialization", "language", "first_released", "current_release",
  "maintained", "mcp_support", "plugin_support", "claude_code_plugin", "subagents", "hooks",
  "plan_mode", "plugin_docs_url", "config_docs_url", "model_providers", "pricing", "stars",
  "sources", "last_verified", "date_added", "what_makes_it_special",
];
const LIST_FIELDS = new Set(["platforms", "autonomy_level", "sources"]);
const DEFAULTS = { layout: "agent.njk", specialization: "general", platforms: [], autonomy_level: [], sources: ["github-issue"] };
const LEDGER = "CATEGORIZATION_LEDGER.md";
const LEDGER_HEADER = "| Slug | Name | Category | Rationale |";
const LEDGER_ROW = /^\| `([^`]+)` \| (.*?) \| (\S+) \| (.*) \|$/;
// The only files a run may change; `pr` refuses to commit anything else.
const ALLOWED = /^(agents\/[^/]+\.md|CATEGORIZATION_LEDGER\.md|_data\/makers\.json)$/;

type Json = any;
const fail = (msg: string): never => { console.error(msg); process.exit(1); };
const run = (cmd: string, args: string[]) =>
  execFileSync(cmd, args, { cwd: ROOT, encoding: "utf8", stdio: ["ignore", "pipe", "inherit"] });
const gh = (args: string[]): Json => JSON.parse(run("gh", args));
const read = (path: string) => readFileSync(resolve(ROOT, path), "utf8");
const readJson = (path: string): Json => JSON.parse(read(path));
const workDir = (n: string) => { const d = join(ROOT, "work", `issue-${n}`); mkdirSync(d, { recursive: true }); return d; };

// Which form an issue came from: the label, or the title prefix when the issue
// was filed with the gh CLI and carries no label.
function kindOf(labels: string[], title: string) {
  if (labels.includes("new-entry") || /^Add:/.test(title)) return "add";
  if (labels.includes("correction") || /^Fix:/.test(title)) return "fix";
  return null;
}

// [{id, label, type}] in form order, read from the template YAML so a label
// edit in the form never breaks parsing. Option labels start with "- " and so
// never match the field-label pattern.
function templateFields(path: string) {
  const fields: { id?: string; label?: string; type: string }[] = [];
  for (const raw of read(path).split("\n")) {
    const line = raw.trim();
    const type = line.match(/^-\s+type:\s*(\S+)/);
    if (type) { fields.push({ type: type[1] }); continue; }
    const field = fields.at(-1);
    if (!field) continue;
    const id = line.match(/^id:\s*(\S+)/);
    if (id && !field.id) field.id = id[1];
    const label = line.match(/^label:\s*(.+)$/);
    if (label && !field.label) field.label = label[1].trim().replace(/^"|"$/g, "");
  }
  return fields.filter((f) => f.id && f.id !== "confirm");
}

// GitHub renders a submitted form as one "### <Label>" heading per field.
function parseBody(body: string, fields: ReturnType<typeof templateFields>) {
  const out: Record<string, Json> = Object.fromEntries(fields.map((f) => [f.id, null]));
  const parts = body.replace(/\r\n/g, "\n").split(/^### (.+?)\s*$/m);
  for (let i = 1; i + 1 < parts.length; i += 2) {
    const field = fields.find((f) => f.label === parts[i].trim());
    const text = parts[i + 1].trim();
    if (!field) continue;
    if (field.type === "checkboxes") out[field.id!] = [...text.matchAll(/^- \[[xX]\] (.+?)\s*$/gm)].map((m) => m[1]);
    else out[field.id!] = ["", "_No response_", "None", "No change"].includes(text) ? null : text;
  }
  return out;
}

function cmdList() {
  const prs: Json[] = gh(["pr", "list", "--state", "open", "--limit", "500", "--json", "headRefName"]);
  const claimed = new Set(prs.map((p) => p.headRefName.match(/^issue-(\d+)-/)?.[1]));
  const issues: Json[] = gh(["issue", "list", "--state", "open", "--limit", "500", "--json", "number,title,labels"]);
  for (const issue of issues.sort((a, b) => a.number - b.number)) {
    const labels = issue.labels.map((l: Json) => l.name);
    const kind = kindOf(labels, issue.title);
    if (kind && !labels.includes("needs-info") && !claimed.has(String(issue.number)))
      console.log(`${issue.number}\t${kind}\t${issue.title}`);
  }
}

function cmdFetch(n: string) {
  const raw = gh(["issue", "view", n, "--json", "number,title,body,labels,author,url"]);
  const labels = raw.labels.map((l: Json) => l.name);
  const kind = kindOf(labels, raw.title) ?? fail(`cannot tell add from fix: labels=${labels} title=${JSON.stringify(raw.title)}`);
  const fields = parseBody(raw.body, templateFields(TEMPLATES[kind]));
  const issue: Json = { number: raw.number, kind, title: raw.title, author: raw.author?.login, url: raw.url, fields };
  if (kind === "add" && fields.category) fields.category = fields.category.split(":")[0].trim();
  if (kind === "fix") {
    issue.changes = []; issue.unparsed = [];
    for (const line of (fields.changes ?? "").split("\n")) {
      const m = line.match(/^\s*([A-Za-z_]+)\s*:\s*(.*?)\s*->\s*(.*?)\s*$/);
      if (m) issue.changes.push({ field: m[1], old: m[2] || null, new: m[3] || null });
      else if (line.trim()) issue.unparsed.push(line.trim());
    }
    issue.slug_hint = (fields.entry ?? "").match(/\/agents\/([A-Za-z0-9._-]+)/)?.[1] ?? null;
  }
  writeFileSync(join(workDir(n), "issue.json"), JSON.stringify(issue, null, 2) + "\n");
  console.log(`wrote work/issue-${n}/issue.json`);
}

const quote = (v: Json) => `"${String(v).replace(/"/g, '\\"')}"`;
function renderField(key: string, value: Json): string[] {
  if (LIST_FIELDS.has(key) || Array.isArray(value)) {
    const items: Json[] = value ?? [];
    return items.length ? [`${key}:`, ...items.map((v) => `  - ${quote(v)}`)] : [`${key}: []`];
  }
  if (value === null || value === undefined) return [`${key}: null`];
  if (typeof value === "boolean") return [`${key}: ${value ? '"True"' : '"False"'}`];
  return [`${key}: ${quote(value)}`];
}

const cell = (s: Json) => String(s).replace(/\|/g, "\\|").replace(/\s*\n\s*/g, " ").trim();
// The ledger file with the new row at its sorted position; everything else is
// kept byte for byte. No count lives in the file (the site computes counts at
// build time), so two entry PRs never edit the same line.
function ledgerWith(row: { slug: string; name: string; category: string; rationale: string }) {
  const text = read(LEDGER);
  const rows = text.split("\n").flatMap((line) => {
    const m = line.match(LEDGER_ROW);
    return m ? [{ slug: m[1], name: m[2], category: m[3], rationale: m[4] }] : [];
  });
  if (rows.some((r) => r.slug === row.slug)) fail(`${LEDGER} already has a row for ${row.slug}`);
  const at = rows.findIndex((r) => r.slug > row.slug);
  rows.splice(at < 0 ? rows.length : at, 0, row);
  const head = text.slice(0, text.indexOf(LEDGER_HEADER));
  const table = rows.map((r) => `| \`${r.slug}\` | ${r.name} | ${r.category} | ${r.rationale} |`);
  return head + [LEDGER_HEADER, "|------|------|----------|-----------|", ...table].join("\n") + "\n";
}

// makers.json with the record added, keys sorted so a new maker lands at its
// alphabetical position; arrays of scalars stay on one line as in the file.
function makersWith(key: string, record: Json) {
  const makers = readJson("_data/makers.json");
  if (makers[key]) return null;
  if (!record) fail(`maker "${key}" is not in _data/makers.json and verified.json has no maker_record`);
  makers[key] = record;
  const sorted = Object.fromEntries(Object.keys(makers).sort().map((k) => [k, makers[k]]));
  return JSON.stringify(sorted, null, 2).replace(/\[\s+([^\[\]{}]*?)\s+\]/g, (_, s) => `[${s.replace(/,\s+/g, ", ")}]`) + "\n";
}

function cmdWrite(file: string) {
  const v = readJson(file);
  const slug: string = v.slug;
  if (!/^[a-z0-9][a-z0-9._-]*$/.test(slug)) fail(`invalid slug: ${JSON.stringify(slug)}`);
  const path = `agents/${slug}.md`;
  if (existsSync(join(ROOT, path))) fail(`entry already exists: ${path}`);
  const entry: Json = { ...DEFAULTS, ...v.entry, slug, last_verified: new Date().toISOString().slice(0, 10) };
  if (entry.date_added == null) entry.date_added = entry.last_verified;
  const unknown = Object.keys(entry).filter((k) => !FIELD_ORDER.includes(k));
  if (unknown.length) fail(`unknown entry fields: ${unknown.join(", ")}`);
  for (const k of ["name", "category", "maker", "url"]) if (!entry[k]) fail(`entry.${k} is required`);
  if (!v.body?.trim()) fail("body (the narrative) is empty");
  if (!v.rationale?.trim()) fail("rationale is empty");
  const writes: Record<string, string> = {
    [path]: ["---", ...FIELD_ORDER.flatMap((k) => renderField(k, entry[k])), "---", "", v.body.trim(), ""].join("\n"),
    [LEDGER]: ledgerWith({ slug, name: cell(entry.name), category: entry.category, rationale: cell(v.rationale) }),
  };
  const makers = makersWith(entry.maker, v.maker_record);
  if (makers) writes["_data/makers.json"] = makers;
  for (const [p, text] of Object.entries(writes)) writeFileSync(join(ROOT, p), text);
  console.log(`wrote ${Object.keys(writes).join(", ")}`);
}

function cmdPr(n: string, base: string) {
  const d = workDir(n);
  const issue = readJson(join(d, "issue.json"));
  const v = readJson(join(d, "verified.json"));
  const bodyFile = join(d, "pr-body.md");
  if (!existsSync(bodyFile)) fail(`write the PR body to work/issue-${n}/pr-body.md first (template in docs/issue-to-pr.md)`);
  const changed = run("git", ["status", "--porcelain", "--untracked-files=all"]).split("\n").filter(Boolean).map((l) => l.slice(3));
  const stray = changed.filter((p) => !ALLOWED.test(p));
  if (stray.length) fail(`the working tree has changes outside the entry files; commit or stash them first: ${stray.join(", ")}`);
  if (!changed.length) fail("nothing to commit");
  const remotes = run("git", ["remote"]).split("\n").filter(Boolean);
  const remote = remotes.includes("origin") ? "origin" : remotes[0] ?? fail("no git remote");
  const branch = issue.kind === "add" ? `issue-${n}-${v.slug}` : `issue-${n}-fix-${v.slug}`;
  if (run("git", ["ls-remote", "--heads", remote, branch]).trim()) fail(`branch already exists on ${remote}: ${branch}`);
  const title = `${issue.kind === "add" ? "Add" : "Fix"} entry: ${v.entry?.name ?? v.slug} (#${n})`;
  const start = run("git", ["rev-parse", "--abbrev-ref", "HEAD"]).trim();
  run("git", ["checkout", "-q", "-b", branch, base]); // the uncommitted entry changes come along
  try {
    run("git", ["add", "--", ...changed]);
    run("git", ["commit", "-q", "-m", title]);
    run("git", ["push", "-q", "-u", remote, branch]);
    console.log(run("gh", ["pr", "create", "--base", base, "--head", branch, "--title", title, "--body-file", bodyFile]).trim());
  } finally {
    run("git", ["checkout", "-q", start]); // the next issue starts where this one did
  }
}

const [cmd, arg, flag, flagValue] = process.argv.slice(2);
try {
  if (cmd === "list") cmdList();
  else if (cmd === "fetch" && arg) cmdFetch(arg);
  else if (cmd === "write" && arg) cmdWrite(arg);
  else if (cmd === "pr" && arg) cmdPr(arg, flag === "--base" && flagValue ? flagValue : "main");
  else fail("usage: node scripts/issue_to_pr.mts list | fetch <N> | write <verified.json> | pr <N> [--base <branch>]");
} catch (err) {
  fail(err instanceof Error ? err.message : String(err));
}
