# Stratified sample of physical O*NET tasks for the general-purpose (GP) robot coverage prototype.
# Weights: time_share x OEWS May 2024 employment (split equally across O*NET codes in one SOC).
# Stratum A: tasks where Anthropic's ratings cite any GP-looking source (PPS sample).
# Stratum B: other tasks rated E1+ (PPS sample with replacement). Stratum C: E0 tasks (PPS).
import pandas as pd, numpy as np, json, re
rng = np.random.default_rng(20261017)
t = pd.read_csv("rx_tasks.csv")
oes = pd.read_excel("oesm24nat/national_M2024_dl.xlsx", usecols=["OCC_CODE","O_GROUP","TOT_EMP"])
oes = oes[oes.O_GROUP=="detailed"]; oes["TOT_EMP"]=pd.to_numeric(oes.TOT_EMP, errors="coerce")
emp = dict(zip(oes.OCC_CODE, oes.TOT_EMP))
t["soc"]=t.onetsoc_code.str[:7]
nper=t.drop_duplicates("onetsoc_code").groupby("soc").size()
t["w"]=t.time_share*(t.soc.map(emp)/t.soc.map(nper)).fillna(0)
p=t[(t.physical=="Yes")&(t.w>0)].copy()
W=p.w.sum(); p["share"]=p.w/W
GPDEV = re.compile(r"figure ai|physical intelligence|1x tech|agility robotics|apptronik|ubtech|unitree|agibot|zhiyuan|galbot|sanctuary|dyna robotics|sunday robotics|skild|fourier|xpeng|robotera|spirit ai|galaxea|hello robot|everyday robots|reflex robotics|persona ai|toyota research|x-humanoid|beijing humanoid|leju|engineai|mentee|1x\b", re.I)
GPSYS = re.compile(r"optimus|atlas \(electric\)|atlas humanoid|electric atlas|gemini robotics|mobile aloha|helix|humanoid", re.I)
BAD = re.compile(r"avidbots|ripcord|atlas copco|steris|uveye|leica|zünd|kepler intubation|lectra", re.I)
def anygp(srcs):
    if not isinstance(srcs,str): return False
    for s in json.loads(srcs):
        d=s.get("developer") or ""; y=s.get("system") or ""
        if not BAD.search(d+y) and (GPDEV.search(d) or GPSYS.search(y)): return True
    return False
p["gp_lead"]=p.sources.apply(anygp)
A=p[p.gp_lead]; B=p[~p.gp_lead & p.exposure_tier.isin(["E1","E2","E3"])]; C=p[~p.gp_lead & (p.exposure_tier=="E0")]
def pps(df,n):
    idx=rng.choice(len(df), size=n, replace=True, p=(df.w/df.w.sum()).values)
    return df.iloc[idx]
sA=pps(A,80); sB=pps(B,60); sC=pps(C,30)
strata={"A":(A,sA),"B":(B,sB),"C":(C,sC)}
meta={k:{"stratum_share":float(v[0].w.sum()/W),"n_pop":int(len(v[0])),"n_sample":int(len(v[1])),"n_unique":int(v[1].drop_duplicates(['onetsoc_code','task_id']).shape[0])} for k,v in strata.items()}
print(json.dumps(meta,indent=1))
items=[]; draws=[]
for k,(pop,s) in strata.items():
    for _,r in s.iterrows():
        key=f"{r.onetsoc_code}_{r.task_id}"
        draws.append({"stratum":k,"key":key})
    for _,r in s.drop_duplicates(["onetsoc_code","task_id"]).iterrows():
        key=f"{r.onetsoc_code}_{r.task_id}"
        insts=[{"instance":i["instance"],"weight_pct":i["weight_pct"],"description":i["description"],"anthropic_tier":i["tier"]} for i in json.loads(r.instances)] if isinstance(r.instances,str) else []
        leads=[{k2:s2.get(k2) for k2 in ("system","developer","date","maturity","autonomy_status","url")} for s2 in json.loads(r.sources)] if isinstance(r.sources,str) else []
        items.append({"key":key,"stratum":k,"occupation":r.occupation_title,"task":r.task_statement,"share_of_physical_work":round(float(r.share),6),
                      "anthropic_task_tier":r.exposure_tier,"instances":insts,"anthropic_leads":leads})
json.dump({"W":float(W),"meta":meta,"draws":draws},open("sample_meta.json","w"),indent=1)
items.sort(key=lambda x:(x["stratum"],x["key"]))
json.dump(items,open("items.json","w"),indent=1)
print("unique items", len(items))
