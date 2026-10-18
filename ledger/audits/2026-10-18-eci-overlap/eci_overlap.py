#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["eci @ git+https://github.com/epoch-research/eci-public@e937446cd8ac0e910ea578516b1cab2b00c06d25"]
# ///
"""Does ECI's own use of METR horizons and RLI bias the KPI? Refit ECI without them and redo the
ECI -> METR calibration (owner question 2026-10-18: "maybe ECI itself is a blend already?").

ECI is fitted (Epoch's eci-public code, pinned above) on Epoch's published fit input
epoch_capabilities_index/processed_data_for_eci.csv, which includes "METR Time Horizons" (the
very horizons the KPI's calibration regresses on) and "Remote Labor Index" (the KPI's other half).
Variants: the full input (must reproduce eci_scores.csv), and without METR, RLI, or both. For each:
the p80/p50 calibration refit on robots_software.CALIBRATION_PAIRS, the frontier horizon under it,
and the SWE-Marathon gap (measured / converted 80% horizon) over the current ECI frontier.

  OPENBLAS_NUM_THREADS=1 uv run data/ledger/audits/2026-10-18-eci-overlap/eci_overlap.py \
      [--zip benchmark_data.zip] [--write DIR]      (run from the repo root; fetches live otherwise)
"""
from __future__ import annotations

import argparse
import hashlib
import io
import math
import os
import sys
import urllib.request
import zipfile

import pandas as pd
from eci import fit_eci_model

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
sys.path[:0] = [os.path.join(ROOT, "gather", "collectors"), os.path.join(ROOT, "core")]
import common  # noqa: E402
import robots_software as rs  # noqa: E402
import swe_marathon as sm  # noqa: E402

METR, RLI = "METR Time Horizons", "Remote Labor Index"
VARIANTS = {"full": set(), "no-METR": {METR}, "no-RLI": {RLI}, "no-METR-no-RLI": {METR, RLI}}
MIN_BENCH = 4   # eci-public's prepare_benchmark_data default


def fit(proc: pd.DataFrame, drop: set[str]) -> tuple[pd.DataFrame, pd.DataFrame]:
    df = proc[~proc["benchmark"].isin(drop)]
    n = df.groupby("Model")["benchmark"].nunique()
    df = df[df["Model"].isin(n[n >= MIN_BENCH].index)]
    eci, edi, _ = fit_eci_model(df, bootstrap_samples=0)
    return eci, edi


def gap(eci: dict[str, float], cal: tuple[float, float], swe: dict[str, float]) -> tuple[float, list]:
    """Mean log2(SWE-Marathon h80 / converted h80) over SWE-Marathon models within rs.GAP_WINDOW ECI
    points of the variant's current top ECI (today's pool; the collector's monthly series uses
    release-dated pools)."""
    top = max(eci.values())
    pool = [(m, eci[m], h) for m, h in swe.items() if m in eci and eci[m] >= top - rs.GAP_WINDOW]
    a, b = cal
    g = [math.log2(h * 60 / 2 ** (a + b * e)) for _, e, h in pool]
    return sum(g) / len(g), sorted(pool, key=lambda p: -p[1])


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--zip", help="local copy of benchmark_data.zip (default: fetch live)")
    ap.add_argument("--write", metavar="DIR", help="write eci_variants.csv and calibration.csv there")
    a = ap.parse_args()
    data = open(a.zip, "rb").read() if a.zip else urllib.request.urlopen(rs.EPOCH_URL).read()
    print(f"benchmark_data.zip sha256 {hashlib.sha256(data).hexdigest()}")
    zf = zipfile.ZipFile(io.BytesIO(data))
    proc = pd.read_csv(zf.open("epoch_capabilities_index/processed_data_for_eci.csv"))
    pub = pd.read_csv(zf.open("epoch_capabilities_index/eci_scores.csv")).set_index("Model")["eci"]
    _, metr = rs.models(common.fetch(rs.URL))
    sw = sm.fetch(None)
    swe = {m: f["h80"] for m, f in sm.best_by_model(sm.configs(sw["trials"], sw["tasks"])).items()}

    ecis, cals, rows = {}, {}, []
    for name, drop in VARIANTS.items():
        e, edi = fit(proc, drop)
        ecis[name] = dict(zip(e["Model"], e["eci"]))
        if name == "full":
            d = (e.set_index("Model")["eci"] - pub).dropna().abs()
            print(f"reproduction: {len(d)} models, max |ECI - published| {d.max():.4f}")
            for bm in (METR, RLI):
                r = edi[edi["benchmark"] == bm].iloc[0]
                print(f"  {bm}: difficulty {r['edi']:.1f}, slope {r['discriminability_scaled']:.3f} per ECI point")
        ems = [{"id": m, "value": v} for m, v in ecis[name].items()]
        for q in ("p80", "p50"):
            c = rs.calibrate(metr, ems, q)
            cals[name, q] = (c["a"], c["b"])
            top_m = max(ecis[name], key=ecis[name].get)
            top = ecis[name][top_m]
            h = 2 ** (c["a"] + c["b"] * top) / 60
            hf = 2 ** (rs.ECI_CAL[q][0] + rs.ECI_CAL[q][1] * pub[top_m]) / 60
            row = {"variant": name, "q": q, "n": c["n"], "eci_per_doubling": c["eci_per_doubling"], "r2": c["r2"],
                   "resid_sd": c["resid_sd"], "top_pair_eci": c["top_eci"], "frontier_model": top_m,
                   "frontier_eci": top, "frontier_h": h, "frontier_h_kpi": hf,
                   "pred_se_frontier": c["pred_se"](top)}
            if q == "p80":
                g, pool = gap(ecis[name], cals[name, q], swe)
                row["swe_gap"], row["swe_pool"] = g, len(pool)
            rows.append(row)
    cal = pd.DataFrame(rows)
    pd.set_option("display.width", 200)
    print("\ncalibration per variant (frontier_h: the frontier model's horizon under the variant's own "
          "refit; frontier_h_kpi: the KPI's frozen line on the published ECI)")
    print(cal.drop(columns=["frontier_h_kpi"]).round(3).to_string(index=False))
    print(f"KPI now: {rows[0]['frontier_model']} {rows[0]['frontier_h_kpi']:.2f} h (p80)")

    pairs = [(mid, e) for mid, e in rs.CALIBRATION_PAIRS.items() if e in ecis["full"]]
    by = {m["id"]: m for m in metr}
    tab = pd.DataFrame([{"metr_id": mid, "model": e, "metr_p80_h": by[mid]["p80"]["estimate"] / 60,
                         **{f"eci_{v}": ecis[v].get(e) for v in VARIANTS}} for mid, e in pairs])
    for v in ("full", "no-METR-no-RLI"):
        av, bv = cals[v, "p80"]
        tab[f"resid_{v}"] = [math.log2(h * 60) - (av + bv * x) for h, x in zip(tab["metr_p80_h"], tab[f"eci_{v}"])]
    tab["shift"] = tab["eci_no-METR-no-RLI"] - tab["eci_full"]
    print("\ncalibration models: ECI without METR+RLI minus full, and p80 residuals (doublings)")
    print(tab[["model", "eci_full", "shift", "resid_full", "resid_no-METR-no-RLI"]].round(2).to_string(index=False))
    fr = sorted(ecis["full"], key=ecis["full"].get, reverse=True)[:10]
    print("\nfrontier (top 10 by full ECI): ECI shift without METR+RLI")
    print(", ".join(f"{m} {ecis['no-METR-no-RLI'][m] - ecis['full'][m]:+.2f}" for m in fr))
    if a.write:
        allm = sorted(set().union(*map(set, ecis.values())), key=lambda m: -ecis["full"].get(m, 0))
        pd.DataFrame([{"model": m, **{v: ecis[v].get(m) for v in VARIANTS}} for m in allm]).round(4).to_csv(
            os.path.join(a.write, "eci_variants.csv"), index=False)
        cal.round(4).to_csv(os.path.join(a.write, "calibration.csv"), index=False)
        print(f"wrote {a.write}/eci_variants.csv, calibration.csv")
    return 0


if __name__ == "__main__":
    sys.exit(main())
