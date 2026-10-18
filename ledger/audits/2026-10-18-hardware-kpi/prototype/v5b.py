#!/usr/bin/env python3
"""Re-judge v5's borderline pairs (any yes vote) one pair per call, so samples are independent,
with two models. Usage: v5b.py run|score"""
import json, os, sys, collections
import v5

N = {"openai-codex/gpt-6-luna:high": 7, "anthropic/claude-opus-5-5:high": 7}

def borderline():
    tiers = v5.setting_tiers(); out = []
    for k in v5.KEYS:
        pairs = v5.pairs_for(k, tiers)
        J = [{x["pair"]: x["covers"] for x in json.load(open(f"{v5.OUT}/judge_{k}_{j}.json"))["judgments"]} for j in range(6)]
        for n, p in enumerate(pairs):
            ys = sum(J[j].get(n) == "yes" for j in range(6))
            if ys: out.append((k, n, p, ys))
    return out

def one(arg):
    k, n, p, model, s = arg
    v5.MODEL = model   # module global used by v5.llm
    tag = model.split("/")[1].split(":")[0]
    it = v5.items[k]; dec = v5.decompose(k)
    desc = {i["instance"]: i["description"] for i in it["instances"]}
    step = {(i["instance"], x["id"]): x["step"] for i in dec["instances"] for x in i["substeps"]}
    txt = f"pair 0:\n  instance: {desc[p['instance']]}\n  sub-step: {step[(p['instance'], p['sid'])]}\n  entry: {v5.entry_text(p['entry'])}"
    return v5.llm(v5.JUDGE.format(occ=it["occupation"], task=it["task"], pairs=txt), f"{v5.OUT}/single_{k}_{n}_{tag}_{s}.json")

if __name__ == "__main__":
    B = borderline()
    if sys.argv[1] == "run":
        # one model per pmap so the module-global MODEL is not raced
        for model, n in N.items():
            v5.pmap(lambda a: one(a), [(k, i, p, model, s) for k, i, p, _ in B for s in range(n)])
    else:
        for k, i, p, ys in B:
            row = []
            for model, n in N.items():
                tag = model.split("/")[1].split(":")[0]
                y = sum(json.load(open(f"{v5.OUT}/single_{k}_{i}_{tag}_{s}.json"))["judgments"][0]["covers"] == "yes" for s in range(n))
                row.append(f"{tag} {y}/{n}")
            dec = v5.decompose(k)
            st = {(d["instance"], x["id"]): x["step"] for d in dec["instances"] for x in d["substeps"]}
            print(f"batched {ys}/6 | {' | '.join(row)} | {st[(p['instance'], p['sid'])][:60]} <- {v5.catd[p['entry']]['system'][:22]}")
