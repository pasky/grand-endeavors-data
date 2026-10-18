#!/usr/bin/env python3
"""v5 GP-robot coverage rating: fixed decomposition, shared shortlist, atomic pair judgments.

Stages (each LLM call cached as a JSON file under v5/, so reruns resume):
  decompose  one call per task: instance -> sub-steps with time shares (fixed panel definition)
  shortlist  two independent calls per task: candidate catalogue entries per sub-step (union);
             candidates whose environment is easier than the instance setting are dropped
             (evidence transfers only from harder to easier environments)
  judge      N independent calls per task: yes/no per (sub-step, entry) pair
  score      majority per pair within each judge panel; coverage = time share of covered sub-steps
Usage: v5.py decompose|shortlist|judge|score
"""
import json, os, sys, subprocess, re, statistics, random
from concurrent.futures import ThreadPoolExecutor
import pandas as pd

P = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(P, "v5")
MODEL = "openai-codex/gpt-6-luna:high"
JUDGES = 6            # panel 1 = judges 0-2, panel 2 = judges 3-5
TV = {"E1": 1, "E2": 2, "E3": 3}

items = {x["key"]: x for x in json.load(open(os.path.join(P, "items.json")))}
sel = json.load(open(os.path.join(P, "v2_selection.json")))
KEYS = sel["A"] + sel["B"]
cat = json.load(open(os.path.join(P, "catalog_v1_compact.json")))
catd = {e["id"]: e for e in cat}

def setting_tiers():
    t = pd.read_csv(os.path.join(P, "rx_tasks.csv"), usecols=["onetsoc_code", "task_id", "instances"])
    t["key"] = t.onetsoc_code + "_" + t.task_id.astype(str)
    out = {}
    for r in t[t.key.isin(KEYS)].itertuples():
        for i in json.loads(r.instances):
            out[(r.key, i["instance"])] = i.get("setting_tier")
    return out

def llm(prompt, path):
    if os.path.exists(path):
        return json.load(open(path))
    os.makedirs(f"{OUT}/prompts", exist_ok=True)
    pfile = f"{OUT}/prompts/{os.path.basename(path)[:-5]}.txt"   # kept for audit; passed as @file (argv size limit)
    open(pfile, "w").write(prompt)
    for attempt in range(3):
        r = subprocess.run(["pi", "-p", "--no-tools", "--no-session", "--no-extensions", "--no-skills",
                            "--no-context-files", "--no-prompt-templates", "--model", MODEL,
                            "--system-prompt", "You are a careful analyst. Reply with one JSON object only, no prose, no code fences.",
                            "@" + pfile, "Follow the instructions in the attached file."],
                           capture_output=True, text=True, timeout=900, stdin=subprocess.DEVNULL)
        txt = r.stdout.strip()
        m = re.search(r"\{.*\}", txt, re.S)
        if r.returncode == 0 and m:
            try:
                obj = json.loads(m.group(0))
                json.dump(obj, open(path, "w"), indent=1)
                return obj
            except json.JSONDecodeError:
                pass
        sys.stderr.write(f"retry {path}: rc={r.returncode} {r.stderr[-300:]}\n")
    raise RuntimeError(f"LLM call failed: {path}")

def pmap(fn, args, n=12):
    with ThreadPoolExecutor(n) as ex:
        return list(ex.map(fn, args))

# ---------------------------------------------------------------- decompose
DECOMP = """Split each instance of this US job task into its main sub-steps and estimate how the
instance's working time divides among them.

Occupation: {occ}
Task: {task}
Instances (concrete ways the task is done; weights are shares of occurrences):
{insts}

For every instance give 2-6 sub-steps. Each sub-step is one concrete activity (verb + objects +
where), small enough that one could ask "has a robot done exactly this?". Include non-physical
parts (talking to people, paperwork, deciding) as their own sub-steps. `share` = fraction of the
instance's working time; shares sum to 1 per instance.
Reply: {{"instances": [{{"instance": 0, "substeps": [{{"id": "s1", "step": "...", "share": 0.4}}]}}]}}"""

def decompose(key):
    it = items[key]
    insts = "\n".join(f"- instance {i['instance']} (weight {i['weight_pct']}%): {i['description']}" for i in it["instances"])
    return llm(DECOMP.format(occ=it["occupation"], task=it["task"], insts=insts), f"{OUT}/decomp_{key}.json")

# ---------------------------------------------------------------- shortlist
SHORT = """Below is a catalogue of activities that general-purpose robots (humanoids, mobile
manipulators, generalist robot arms) have done autonomously, and the sub-steps of a US job task.
For every sub-step, list ALL catalogue entries that might plausibly show a robot doing that
sub-step or something very close to it. Favour recall: include an entry if in doubt; a later
judge will decide. Leave the list empty only when no entry is remotely related.

Catalogue:
{catalog}

Job task: {occ}: {task}
Sub-steps:
{subs}

Reply: {{"candidates": [{{"instance": 0, "id": "s1", "entries": ["C012", "C047"]}}]}}"""

def catalog_text():
    return "\n".join(f"{e['id']} | {e['system']} | {e['form']} | {e['env']} | {e['maturity']} | {e['activity']} | objects: {e.get('objects')} | setting: {e.get('setting')}" for e in cat)

def substeps_text(key, dec):
    it = items[key]; desc = {i["instance"]: i["description"] for i in it["instances"]}
    lines = []
    for ins in dec["instances"]:
        lines.append(f"instance {ins['instance']}: {desc.get(ins['instance'], '')}")
        for s in ins["substeps"]:
            lines.append(f"  {s['id']}: {s['step']}")
    return "\n".join(lines)

def shortlist(arg):
    key, rep = arg
    dec = decompose(key)
    it = items[key]
    return llm(SHORT.format(catalog=catalog_text(), occ=it["occupation"], task=it["task"], subs=substeps_text(key, dec)),
               f"{OUT}/short_{key}_{rep}.json")

def pairs_for(key, tiers):
    dec = decompose(key)
    cands = {}
    for rep in (0, 1):
        for c in shortlist((key, rep))["candidates"]:
            cands.setdefault((c["instance"], c["id"]), set()).update(e for e in c["entries"] if e in catd)
    out = []
    for ins in dec["instances"]:
        st = TV.get(tiers.get((key, ins["instance"])), 1)
        for s in ins["substeps"]:
            for e in sorted(cands.get((ins["instance"], s["id"]), ())):
                if TV.get(catd[e]["env"], 1) >= st:      # evidence transfers only to easier environments
                    out.append({"instance": ins["instance"], "sid": s["id"], "entry": e})
    return out

# ---------------------------------------------------------------- judge
JUDGE = """Decide, for each pair below, whether the catalogue entry shows that a general-purpose
robot can do the job sub-step.

Answer "yes" only if the entry shows the robot autonomously doing this sub-step itself: the same
kind of action on the same kind of objects, covering the whole sub-step, in a setting at least as
demanding as the one described, and well enough (speed, reliability) that it could do the
sub-step as it is done in this job. A related but different activity, only part of the
sub-step, or an easier version of it is "no".
Also say whether the entry's robot did it in the same kind of workplace as this instance
(e.g. a warehouse for a warehouse job, a home for a home job).

Job task: {occ}: {task}

Pairs:
{pairs}

Reply: {{"judgments": [{{"pair": 0, "covers": "yes|no", "same_workplace": "yes|no", "why": "<max 20 words>"}}]}}"""

def entry_text(e):
    e = catd[e]
    return (f"{e['id']} {e['system']} ({e['developer']}, {e['form']}): {e['activity']} | objects: {e.get('objects')} | "
            f"setting: {e.get('setting')} ({e['env']}) | maturity: {e['maturity']} | speed vs human: {e.get('speed_vs_human')} | "
            f"reliability: {e.get('reliability')} | caveats: {e.get('caveats')}")

def judge(arg):
    key, j, pairs = arg
    if not pairs:
        return {"judgments": []}
    it = items[key]; dec = decompose(key)
    desc = {i["instance"]: i["description"] for i in it["instances"]}
    step = {(ins["instance"], s["id"]): s["step"] for ins in dec["instances"] for s in ins["substeps"]}
    txt = "\n\n".join(f"pair {n}:\n  instance: {desc[p['instance']]}\n  sub-step: {step[(p['instance'], p['sid'])]}\n  entry: {entry_text(p['entry'])}"
                      for n, p in enumerate(pairs))
    return llm(JUDGE.format(occ=it["occupation"], task=it["task"], pairs=txt), f"{OUT}/judge_{key}_{j}.json")

# ---------------------------------------------------------------- score
MAT = {"demo": 1, "pilot": 2, "deployed": 3}

def coverage(key, pairs, votes, judges):
    """votes[j] = list of judgments aligned with pairs. Returns task coverage (instance-weighted)."""
    dec = decompose(key); w = {i["instance"]: i["weight_pct"] for i in items[key]["instances"]}
    yes = {}
    for n, p in enumerate(pairs):
        ys = sum(1 for j in judges if votes[j][n]["covers"] == "yes")
        if ys * 2 > len(judges):
            yes[(p["instance"], p["sid"])] = True
    tot = 0
    for ins in dec["instances"]:
        f = sum(s["share"] for s in ins["substeps"] if yes.get((ins["instance"], s["id"])))
        tot += w.get(ins["instance"], 0) * min(f, 1)
    return tot / 100

def main(stage):
    os.makedirs(OUT, exist_ok=True)
    if stage == "decompose":
        pmap(decompose, KEYS); return
    if stage == "shortlist":
        pmap(shortlist, [(k, r) for k in KEYS for r in (0, 1)]); return
    tiers = setting_tiers()
    P_ = {k: pairs_for(k, tiers) for k in KEYS}
    if stage == "judge":
        print("pairs:", sum(len(v) for v in P_.values()))
        pmap(judge, [(k, j, P_[k]) for k in KEYS for j in range(JUDGES)]); return
    if stage == "score":
        V = {}
        for k in KEYS:
            V[k] = {}
            for j in range(JUDGES):
                js = judge((k, j, P_[k]))["judgments"]
                byn = {x["pair"]: x for x in js}
                V[k][j] = [byn.get(n, {"covers": "no", "same_workplace": "no"}) for n in range(len(P_[k]))]
        share = {"A": 0.2016, "B": 0.6123}
        def report(name, ja, jb):
            a = {k: coverage(k, P_[k], V[k], ja) for k in KEYS}
            b = {k: coverage(k, P_[k], V[k], jb) for k in KEYS}
            xa = [a[k] for k in KEYS]; xb = [b[k] for k in KEYS]
            agree = sum((x > 0) == (y > 0) for x, y in zip(xa, xb))
            close = sum(abs(x - y) <= 0.02 for x, y in zip(xa, xb))
            est = lambda d: 100 * sum(share[s] * statistics.mean(d[k] for k in sel[s]) for s in share)
            print(f"{name}: zero/nonzero agree {agree}/{len(KEYS)}, |diff|<=2pp {close}/{len(KEYS)}, "
                  f"pearson {statistics.correlation(xa, xb):.2f}, share {est(a):.2f}% vs {est(b):.2f}%")
            return a, b
        npairs = sum(len(v) for v in P_.values())
        pa = sum(1 for k in KEYS for n in range(len(P_[k])) if V[k][0][n]["covers"] == V[k][3][n]["covers"])
        print(f"pairs {npairs}; single judge vs single judge pair agreement {pa}/{npairs}")
        report("single judge (0 vs 3)", [0], [3])
        a, b = report("panel of 3 (0-2 vs 3-5)", [0, 1, 2], [3, 4, 5])
        allj = {k: coverage(k, P_[k], V[k], list(range(JUDGES))) for k in KEYS}
        est = 100 * sum(share[s] * statistics.mean(allj[k] for k in sel[s]) for s in share)
        random.seed(1); boots = []
        for _ in range(5000):
            boots.append(100 * sum(share[s] * statistics.mean(allj[random.choice(sel[s])] for _ in sel[s]) for s in share))
        boots.sort()
        print(f"all 6 judges: GP share of US physical work {est:.2f}% (sampling 90% CI {boots[250]:.2f}-{boots[4750]:.2f}%)")
        for k in KEYS:
            if a[k] or b[k]:
                print(f"  {a[k]:.3f} {b[k]:.3f}  {items[k]['task'][:80]}")

if __name__ == "__main__":
    main(sys.argv[1])
