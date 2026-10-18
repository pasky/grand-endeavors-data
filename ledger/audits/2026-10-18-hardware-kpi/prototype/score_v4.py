# Score v4 (catalogue-mapping) ratings; optionally enforce T3 (entry env must be >= instance setting tier)
import json, glob, statistics, sys, pandas as pd
items={x["key"]:x for x in json.load(open("items.json"))}
cat={e["id"]:e for e in json.load(open("catalog_v1_compact.json"))}
TV={"E1":1,"E2":2,"E3":3}
t=pd.read_csv("rx_tasks.csv", usecols=["onetsoc_code","task_id","instances"])
t["key"]=t.onetsoc_code+"_"+t.task_id.astype(str)
t=t[t.key.isin(items)]
setting={(r.key,i["instance"]):TV.get(i.get("setting_tier"),1) for r in t.itertools() for i in json.loads(r.instances)} if False else {}
for r in t.itertuples():
    for i in json.loads(r.instances): setting[(r.key,i["instance"])]=TV.get(i.get("setting_tier"),1)
def snap(x):
    g=[0,0.05,0.1,0.25,0.5,0.75,1]; return min(g,key=lambda v:abs(v-x))
def score(f, enforce):
    r={}; dropped=0
    for tk in json.load(open(f)):
        w={i["instance"]:i["weight_pct"] for i in items[tk["key"]]["instances"]}
        tot=0
        for i in tk["instances"]:
            st=setting.get((tk["key"],i["instance"]),1)
            if enforce:
                fr=0
                for s in i.get("substeps",[]):
                    ok=[c for c in s.get("covered_by",[]) if c in cat and TV.get(cat[c]["env"],1)>=st]
                    if s.get("covered_by") and not ok: dropped+=1
                    if ok: fr+=float(s.get("share") or 0)
                fr=snap(min(fr,1))
            else: fr=float(i.get("fraction") or 0)
            tot+=w.get(i["instance"],0)*fr
        r[tk["key"]]=tot/100
    return r,dropped
sel=json.load(open("v2_selection.json")); share={"A":0.2016,"B":0.6123}
for enforce in (False,True):
    R={}; D=0
    for rr in ("r1","r2"):
        R[rr]={}
        for g in range(10):
            x,d=score(f"out/v4_{g}_{rr}.json",enforce); R[rr].update(x); D+=d
    ks=list(R["r1"]); a=[R["r1"][k] for k in ks]; b=[R["r2"][k] for k in ks]
    print("T3 enforced" if enforce else "as rated", "| substeps dropped",D,
          "| agree zero/nonzero",sum((x>0)==(y>0) for x,y in zip(a,b)),"/",len(ks),
          "| pearson %.2f"%statistics.correlation(a,b),
          "| implied share r1 %.2f%% r2 %.2f%%"%tuple(100*sum(share[s]*sum(R[rr][k] for k in sel[s])/len(sel[s]) for s in share) for rr in ("r1","r2")))

# sampling uncertainty (T3 enforced, mean of the two raters), PPS-with-replacement draws
import random
R={rr:{} for rr in ("r1","r2")}
for rr in R:
    for g in range(10): R[rr].update(score(f"out/v4_{g}_{rr}.json",True)[0])
avg={k:(R["r1"][k]+R["r2"][k])/2 for k in R["r1"]}
random.seed(1); boots=[]
for _ in range(5000):
    boots.append(sum(share[s]*statistics.mean(random.choice(sel[s]) and avg[random.choice(sel[s])] for _ in sel[s]) for s in share))
boots.sort(); est=sum(share[s]*statistics.mean(avg[k] for k in sel[s]) for s in share)
print("rater-avg estimate %.2f%%, bootstrap 90%% CI %.2f-%.2f%%"%(est*100, boots[250]*100, boots[4750]*100))
