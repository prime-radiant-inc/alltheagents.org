#!/usr/bin/env python3
"""
Build the final coding-agent-harness table.
Loads: jqueryscript (enriched), merged candidates, GitHub cache enrichment, non-GitHub entries.
Classifies each as a genuine coding agent harness or not, then assembles the final table with:
  name, maker, license, url, source_code_url, what_makes_it_special, platforms,
  first_released, current_release, source_list, stars
"""
import os, re, csv, json

SRCDIR = os.path.dirname(os.path.abspath(__file__))

def clean(s):
    return re.sub(r"\s+", " ", s or "").strip()

# ---------- Classification ----------
# A coding agent harness: primary purpose is letting an LLM write/modify/debug/run code
# or build software/apps autonomously. Exclude pure skill packs, MCP servers, benchmarks,
# monitors, context layers, guardrails, tutorials, books, prompts, general chatbots.

EXCLUDE_KW = [
    "skill pack","skills for","agent skills","skill library","awesome-agent-skill",
    "system prompt","system-prompt","system prompts","prompts and models","prompt collection",
    "prompt-engineering","prompt engineering","awesome-prompt","promptbase","prompt holy grail",
    "mcp server","mcp-server","model context protocol server","mcp adapter","mcp tool",
    "mcp for","mcp bridge","mcp plugin","mcp toolkit",
    "benchmark","bench ","-bench","benchmarking tool","codabench","swe-bench pro",
    "evaluat","leaderboard","scoreboard",
    "monitor","observability","htop for","real-time monitor","status companion",
    "notch panel","dynamic island","activity readout","hud","live workspace state",
    "context layer","context window optimization","context budget","context-mode",
    "memory layer","memory lifecycle","project memory","session memory","persistent context across session",
    "guardrail","safety net","security gate","safety skill","cybersecurity skill",
    "linter for your agent","repo auditor","readiness","agent-ready",
    "book","tutorial","guide to","course","cheatsheet","cheat sheet","how to","how-claude","how-",
    "from scratch","learn coding","learn-claude","deep dive into","deep-dive",
    "marketing","seo","copywriting","growth engineering","investing","value investing","trading",
    "video production","video studio","slide","presentation","design.md","design system","design plugin",
    "codegraph","code knowledge","knowledge graph","code intelligence","code search mcp","search mcp",
    "telegram bot","discord bot","slack bot","chatbot framework","chatgpt clone","chat ui","chat client",
    "raspberry pi","arduino","home automation","robot learning","robotics",
    "calendar","weather","recipe","resume","hr chatbot","hr-",
    "docker","kubernetes","ansible","terraform","deployment platform","cloud cost","finops","infracost",
    "snippet manager","code snippet","snippet",
    "playlist","newsletter","blog","podcast","finllm","radiology","ethics",
    "awesome","best-practice","best practice","landscape","ranking","directory of",
    "claude-code-router","cc-switch","profile switcher","api proxy","switch between",
    "repomix","graph engineering","godot","unreal engine",
    "adapter framework for evaluating",
    "hotkey","shortcut","launcher","bookmark","scheduler","standalone app for",
    "code search","search engine for","code index","code search engine",
]
# Tokens that strongly indicate a coding agent harness
INCLUDE_KW = [
    "coding agent","code agent","coding harness","agent harness","agent runtime","agent os","agent platform",
    "pair programmer","pair programming","software engineer","software engineering","swe agent","swe-agent",
    "ai developer","ai engineer","autonomous software","autonomous coding","autonomous dev","autonomous engineer",
    "terminal agent","terminal coding","cli agent","cli coding","terminal coding agent","terminal-native ai coding",
    "ide agent","agentic ide","agent ide","code editor","coding assistant","ai coding","ai pair",
    "code generation","codegen","code generator","app builder","vibe coding","full-stack app","fullstack",
    "dev agent","developer agent","devagent","ai dev","autonomous agent that","autonomous pair",
    "codebase","repo agent","repository","multi-agent","agent framework","agentic coding","agentic framework",
    "fix github issue","fix issue","patch","pr ","pull request","code review",
    "open source coding agent","open-source coding agent","coding tool","coding workbench","coding workstation",
    "self-hosted ai coding","self-hosted coding","local-first coding","local coding agent",
    "nano claude","claude code–like","claude-code-like","coding loop","agent loop","code editor for the ai",
    "dev team of ai agents","whole dev team","ai coding assistant","ai assistant for","engineering platform",
    "codegen platform","code generation tool","autonomous program","program improvement",
    # broader terms that catch the missed ones
    "ai-driven development","ai driven development","beyond code suggestions","code suggestion",
    "extensible ai agent","ai agent that","agent that goes","power of gemini","agentic chat",
    "build application","build apps","natural language","development platform","development environment",
    "coding experience","development work","dev platform","development agent",
    "code edit","edit code","write code","modify code","run code","debug","test code",
    "code changes","file edit","edit file","file changes","codebase intelligence",
    "development tasks","software development","code completion","code suggest",
    "ai agent for","agent for developer","agent for coding","agent for software",
    "development platform","software platform","agent platform",
]

def is_coding_harness(name, desc, topics, category, url):
    # Exclude only on name + desc + category (NOT topics, since many agents support MCP etc.)
    excl_blob = clean((name or "")+" "+(desc or "")+" "+(category or "")).lower()
    n = (name or "").lower()
    # Exclude ancillary
    for ex in EXCLUDE_KW:
        if ex in excl_blob:
            return False
    # Include checks name + desc + category + topics + url
    incl_blob = clean((name or "")+" "+(desc or "")+" "+(category or "")+" "+" ".join(topics or [])+" "+(url or "")).lower()
    # Strong include
    for inc in INCLUDE_KW:
        if inc in incl_blob:
            return True
    # Name-based: name contains code/coding/dev/swe + has agent-ish or tool-ish desc
    if any(w in n for w in ["code","coding","devagent","swe","dev-agent","codegen","coder"]):
        if any(w in incl_blob for w in ["agent","tool","cli","terminal","ide","editor","llm","gpt","model","autonomous","pair","build","program","compile","prompt","harness","runtime","framework","workbench","workstation","assistant","developer","engineer"]):
            # but not if it's clearly a non-coding thing
            if not any(ex in excl_blob for ex in ["video","slide","design","marketing","game","robot","calendar","weather","recipe","resume","hr"]):
                return True
    # url-based github topic coding-agent / ai-coding-agent
    if "coding-agent" in incl_blob or "ai-coding-agent" in incl_blob or "code-agent" in incl_blob:
        return True
    return False

# ---------- Load sources ----------

def load_jqueryscript():
    """Parse jqueryscript.md entries (have license + platforms)."""
    out = {}
    text = open(os.path.join(SRCDIR,"jqueryscript.md"), encoding="utf-8").read()
    for line in text.splitlines():
        m = re.match(r"^- \[([^\]]+)\]\((https?://[^)]+)\) - \*\*([^*]+)stars?\*\* · (.+)$", line)
        if not m: continue
        name = clean(m.group(1)); url = clean(m.group(2))
        rest = clean(m.group(4))
        parts = rest.split(". ", 1)
        tags = parts[0]; desc = parts[1] if len(parts)>1 else ""
        license_=""; platforms=[]
        for tok in re.findall(r"`([^`]+)`", tags):
            if tok.lower() in ("mit","apache-2.0","agpl-3.0","closed source","source available","gpl","bsd","proprietary","free"):
                license_=tok
            else: platforms.append(tok)
        mr = re.match(r"https?://github\.com/([^/]+/[^/#?]+)", url)
        repo = mr.group(1) if mr else ""
        out[repo.lower() if repo else url.lower()] = {
            "name":name,"url":url,"license":license_,"platforms":";".join(platforms),
            "stars":clean(m.group(3)),"what_makes_it_special":desc,"source_list":"jqueryscript","github_repo":repo
        }
    return out

def load_cache():
    if os.path.exists(os.path.join(SRCDIR,"gh_cache.json")):
        return json.load(open(os.path.join(SRCDIR,"gh_cache.json")))
    return {}

def main():
    jq = load_jqueryscript()
    cache = load_cache()
    rows = list(csv.DictReader(open(os.path.join(SRCDIR,"merged.tsv")), delimiter="\t"))
    print(f"merged candidates: {len(rows)}; jqueryscript: {len(jq)}; cache: {len(cache)}")

    # Build entries: key by github_repo (lower) or url (lower)
    entries = {}
    def add(e):
        repo = e.get("github_repo","")
        key = repo.lower() if repo else e.get("url","").lower().rstrip("/").split("?")[0]
        if key in entries:
            # merge missing fields
            for f in ["license","platforms","stars","what_makes_it_special","category","web","source_list"]:
                if not entries[key].get(f) and e.get(f):
                    entries[key][f]=e[f]
            entries[key]["source_list"] = entries[key].get("source_list","")+","+e.get("source_list","")
        else:
            entries[key]=e

    # First add jqueryscript (richest)
    for k,e in jq.items():
        add(e)
    # Then merged (fills in the rest)
    for r in rows:
        e = {"name":r["name"],"url":r["url"],"github_repo":r.get("github_repo",""),
             "license":"","platforms":"","stars":"","what_makes_it_special":r.get("what_makes_it_special",""),
             "category":r.get("category",""),"web":r.get("web",""),"source_list":r.get("source_list","")}
        add(e)

    # Enrich from cache (GitHub metadata)
    for key,e in entries.items():
        repo = e.get("github_repo","")
        if repo and repo.lower() in cache:
            d = cache[repo.lower()]
            if d.get("error"): continue
            if not e.get("license") and d.get("license"):
                e["license"]=d["license"]
            if not e.get("stars") and d.get("stargazers_count"):
                e["stars"]=str(d["stargazers_count"])
            e["maker"]=d.get("owner","")
            e["first_released"]=d.get("created_at","")[:10] if d.get("created_at") else ""
            e["current_release"]=d.get("pushed_at","")[:10] if d.get("pushed_at") else ""
            e["gh_description"]=d.get("description","") or ""
            e["topics"]=d.get("topics",[])
            e["archived"]=d.get("archived",False)
            e["homepage"]=d.get("homepage","") or ""
            e["language"]=d.get("language","") or ""
        else:
            e["maker"]=e.get("maker","")
            e["first_released"]=""; e["current_release"]=""
            e["gh_description"]=""; e["topics"]=[]; e["archived"]=False
            e["homepage"]=""; e["language"]=""

    print(f"Total unique entries: {len(entries)}")

    # Classify
    keep = []
    drop = []
    for key,e in entries.items():
        name=e.get("name",""); desc=e.get("gh_description","") or e.get("what_makes_it_special","")
        topics=e.get("topics",[]); cat=e.get("category",""); url=e.get("url","")
        if is_coding_harness(name, desc, topics, cat, url):
            keep.append(e)
        else:
            drop.append(e)
    print(f"Classified keep: {len(keep)}; drop: {len(drop)}")

    # Build source_code_url: github url if available, else empty
    for e in keep:
        repo = e.get("github_repo","")
        if repo:
            e["source_code_url"]=f"https://github.com/{repo}"
            e["source_available"]="Yes" if e.get("license") and e["license"].upper() not in ("NONE","NOASSERTION","CLOSED SOURCE","") else ("Source available" if e.get("license") else "Check")
            # fix: if license is None/NOASSERTION but repo exists on github, source is visible
            if not e.get("license") or e["license"]=="NOASSERTION":
                # closed source repo (e.g. cursor, claude-code) - source visible but no OSS license
                e["source_available"]="Source-visible (no OSS license)" if repo else "No"
        else:
            e["source_code_url"]=""
            e["source_available"]="No (proprietary)"
        # platforms: prefer jq platforms, else infer from desc
        if not e.get("platforms"):
            p=[]
            b=(e.get("gh_description","")+e.get("what_makes_it_special","")).lower()
            if any(w in b for w in ["terminal","cli","command line"]): p.append("CLI")
            if any(w in b for w in ["ide","vs code","vscode","jetbrains","editor"]): p.append("IDE")
            if any(w in b for w in ["web","browser","cloud"]): p.append("Web")
            if any(w in b for w in ["desktop","desktop app","macos","windows","linux app"]): p.append("Desktop")
            if any(w in b for w in ["autonomous","daemon","background","headless"]): p.append("Autonomous")
            e["platforms"]=";".join(p) if p else ""

    # Write final table
    cols = ["name","maker","license","url","source_code_url","source_available",
            "what_makes_it_special","platforms","first_released","current_release","stars","language","homepage","source_list"]
    out = os.path.join(SRCDIR, "..", "coding_agent_harnesses.tsv")
    with open(out,"w") as f:
        f.write("\t".join(cols)+"\n")
        for e in keep:
            f.write("\t".join(str(e.get(c,"")).replace("\t"," ").replace("\n"," ") for c in cols)+"\n")
    print(f"Wrote {out} with {len(keep)} entries")

    # Also write dropped for review
    with open(os.path.join(SRCDIR,"dropped.tsv"),"w") as f:
        f.write("\t".join(cols)+"\n")
        for e in drop:
            f.write("\t".join(str(e.get(c,"")).replace("\t"," ").replace("\n"," ") for c in cols)+"\n")

    # show top keep by stars
    def st(e):
        try: return int(e.get("stars","0"))
        except: return 0
    keep.sort(key=st, reverse=True)
    print("\n=== Top 30 by stars ===")
    for e in keep[:30]:
        print(f"  {e.get('name','')[:28]:28} {str(e.get('stars',''))[:8]:8} {e.get('license','')[:14]:14} {e.get('first_released','')} {e.get('url','')[:40]}")

if __name__ == "__main__":
    main()
