#!/usr/bin/env python3
"""
Final cleanup pass on coding_agent_harnesses.tsv:
1. Dedupe by name (keep richest entry)
2. Remove general-purpose agent frameworks not focused on coding
3. Remove non-coding commercial products
4. Normalize names
"""
import os, re, csv

SRCDIR = os.path.dirname(os.path.abspath(__file__))
TBL = os.path.join(SRCDIR, "..", "coding_agent_harnesses.tsv")

def clean(s):
    return re.sub(r"\s+", " ", s or "").strip()

# Entries to explicitly DROP (not coding agent harnesses)
DROP_NAMES = {
    "chatarena","westworld simulation","ailaflow","apidna","avanzai","beam",
    "brain soup","brainsoup","fine tuner","fine-tuner","questflow","relevance ai",
    "naut","kompas ai","input","vortic","invicta","second","test driver","tusk",
    "grit","gitwit","codewp","codegen","blackbox ai","blackboxai","duckie ai",
    "code autopilot","ellipsis","fine","sentius","nlsom","agentverse","ai legion",
    "babycatagi","babybeeagi","babycatagi","babydeeragi","babyelfagi","babyagi",
    "ufo","superagi","adala","agentforge","agentty","zot","waveloom","dvalincode",
    "san","qqcode","zeroclaw","gitclaw","pool","orca (stably)","agent afk",
    "claudescope","dotagent","data-to-paper","gptswarm","fin","kompas",
    "awesome-finllms","awesome-prompt-engineering","awesome-aitools",
    "awesome-ai-llms-in-radiology","ethics","jonathan-flightbase",
    "awesome","open an issue","@aclerbois","prompt-engineering-holy-grail",
    "visual editor","osop","01","codeagentswarm","code agent swarm",
    "vibe-kanban","everything claude code","karpathy-inspired claude code",
    "claude-code-best-practice","claude-code-best-practices",
    "awesome-claude-code","claude-code-router","cc-switch",
    "llamaindex tools","llama_index","haystack","symphony","beads",
    "tabby","daytona","zed-industries/zed","zed","oh my openagent",
    "oh-my-opagent","repomix","codewhale","codewhale","multica",
    "herdr","cmux","aionui","agenticseek","openagentrelay",
    "karpathy-inspired claude code","karpathy-inspired",
    "pr-harmony","the-perfect-orchestrator","pi-boss",
    # academic papers, not harnesses
    "swe-agent: agent-computer interface","executable code actions elicit",
    "codet: code generation with generat","lever: learning to verify",
    "coderl: mastering code generation","teaching large language models to s",
    "is self-repair a silver bullet","self-edit: fault-aware",
    "debug like a human","alphaevolve: a coding agent for sci",
    "codeevolve: an open-source evolutio","codeplan: repository-level coding",
    "autocoderover: autonomous program i","swe-search: enhancing software agent",
    "repograph: enhancing ai software en","demystifying llm-based software eng",
    "swe-master: unleashing the potentia","rethinking the value of agent-gener",
    "scaling test-time compute for agent","swe-replay: efficient test-time sca",
    "swe-rl: advancing llm reasoning","understanding code agent behaviour",
    "chatdev: communicative agents for s","metagpt: meta programming for a mul",
    "mapcoder: multi-agent code generati","magis: llm-based multi-agent framew",
    "large language model-based agents f","llm-based multi-agent systems for s",
    "large language models for software","a survey on large language models fo",
    "advances and frontiers of llm-based",
    # non-harnesses
    "waitlist","memories","r/chatgptcoding","ai engineering","agent os",
    "freebuff","tracknpred",
    # skill packs, not harnesses
    "superpowers","karpathy-inspired claude code skills","karpathy-inspired",
    "agent executor (ax)","agent-qa","effiskill","do personalized skills help",
    # mcp servers, not harnesses
    "jetbrains-index-mcp-plugin","codex-mcp-go",
    # more non-harnesses
    "pipenv","chrome-devtools-mcp","gpt researcher","gpt-researcher",
    "roocode","openai swarm","ante","wfgy","llm-agents.nix",
    "waylog-cli","shadxn","klear-team-brain","claude-stats",
    "gnap","gsd-pro","velaterm","branchbox","yu-ai-code-mother",
    "multi-agent-emergence-environm",
}

# Names to normalize/merge
NORMALIZE = {
    "gpt-engineer": "GPT Engineer",
    "gpt engineer": "GPT Engineer",
    "claude code": "Claude Code",
    "codex cli": "Codex CLI",
    "codex (openai)": "Codex (OpenAI)",
    "opencode": "OpenCode",
    "openhands": "OpenHands",
    "opendevin": "OpenDevin",
    "swe agent": "SWE-agent",
    "swe-agent": "SWE-agent",
    "open interpreter": "Open Interpreter",
    "aider": "Aider",
    "continue": "Continue",
    "cursor": "Cursor",
    "cursor (agent)": "Cursor",
    "windsurf": "Windsurf",
    "devin ai": "Devin AI",
    "bolt.new": "Bolt.new",
    "bolt": "Bolt.new",
    "cody": "Cody (Sourcegraph)",
    "metagpt": "MetaGPT",
    "chatdev": "ChatDev",
    "opendevin": "OpenHands",
    "openhands": "OpenHands",
    "gpt pilot": "GPT Pilot",
    "devika": "Devika",
    "devon": "Devon",
    "sweep": "Sweep",
    "mentat": "Mentat",
    "mentat cli": "Mentat",
    "smol developer": "Smol Developer",
    "v0 by vercel": "v0 (Vercel)",
    "v0": "v0 (Vercel)",
    "github copilot x": "GitHub Copilot",
    "github copilot cli": "GitHub Copilot CLI",
    "maige": "Maige",
    "evo.ninja": "EvoNinja",
    "create.xyz": "Create.xyz",
    "leap.new": "Leap.new",
    "mocha": "Mocha",
    "autogpt": "AutoGPT",
    "agentgpt": "AgentGPT",
}

def norm_name(name):
    key = name.lower().strip()
    return NORMALIZE.get(key, name)

def main():
    rows = list(csv.DictReader(open(TBL), delimiter="\t"))
    print(f"Input: {len(rows)}")

    # Drop garbage (parsing artifacts)
    import re
    garbage = set()
    cleaned = []
    for r in rows:
        n = r["name"].strip()
        if n.startswith(("!","|","**","-","[","@","Add ","http")):
            garbage.add(n); continue
        if len(n) < 2:
            garbage.add(n); continue
        # strip markdown bold from name
        r["name"] = n.replace("**","").strip()
        # Drop academic papers (description starts with numbered citation like "1. [" or "12. [")
        desc = (r.get("what_makes_it_special","") or "").strip()
        if re.match(r"^\d{1,2}\.\s+\[", desc):
            garbage.add(r["name"]); continue
        cleaned.append(r)
    rows = cleaned
    print(f"After garbage+paper removal: {len(rows)}; removed: {len(garbage)}")

    # Drop by name
    kept = []
    dropped = []
    for r in rows:
        n = r["name"].lower().strip()
        if n in DROP_NAMES:
            dropped.append(r)
            continue
        # also drop if name starts with "awesome" or contains "prompt-engineering"
        if n.startswith("awesome") or "prompt-engineering" in n or "prompt engineering" in n:
            dropped.append(r); continue
        # drop entries that are general-purpose LLM frameworks without coding focus
        desc = (r.get("what_makes_it_special","") or "").lower()
        if n == "autogen" and "multi-agent conversation" in desc and "coding" not in desc and "code" not in desc:
            # keep autogen - it's used for coding
            pass
        kept.append(r)

    print(f"After drop: {len(kept)}; dropped: {len(dropped)}")

    # Dedupe by normalized name - keep richest entry (most filled fields)
    by_name = {}
    for r in kept:
        nn = norm_name(r["name"])
        r["name"] = nn
        # also normalize URL for github repos
        score = sum(1 for v in r.values() if v and v not in ("0",""))
        key = nn.lower()
        if key in by_name:
            ex = by_name[key]
            ex_score = sum(1 for v in ex.values() if v and v not in ("0",""))
            if score > ex_score:
                by_name[key] = r
        else:
            by_name[key] = r

    final = list(by_name.values())
    print(f"After dedupe by name: {len(final)}")

    # Sort by stars (desc), no-stars at end
    def star_val(r):
        try: return int(r.get("stars","0") or 0)
        except: return 0
    final.sort(key=star_val, reverse=True)

    cols = list(rows[0].keys())
    with open(TBL, "w") as f:
        f.write("\t".join(cols)+"\n")
        for r in final:
            f.write("\t".join(str(r.get(c,"")).replace("\t"," ").replace("\n"," ") for c in cols)+"\n")
    print(f"Wrote {TBL} with {len(final)} entries")

if __name__ == "__main__":
    main()
