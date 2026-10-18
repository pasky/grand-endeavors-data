#!/usr/bin/env python3
"""Doubling times of the robots-software KPI (the blended 80% horizon), its two components and
METR's own measurements; where METR's pace broke; how much the remote side's pace rests on the
assumed slope of METR's success-vs-length curve (owner question 2026-10-18: the KPI was judged
against METR's ~7-month long-run doubling time, but the blend is not on METR's scale).

  uv run data/ledger/audits/2026-10-18-horizon-pace/pace.py      (run from the repo root)

Series: `core/ledger.py series robots-software <metric> --as-of 2026-10-18`, dated rows only,
kept as a running maximum (the frontier). Doubling time = 1 / OLS slope of log2(value) on months
(30.44 days), with a t-based 95% interval (rows of a frontier are not independent, so these
intervals are too narrow; they are for comparing windows, not for inference).
"""
from __future__ import annotations

import datetime as dt
import json
import math
import os
import subprocess
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
AS_OF = "2026-10-18"
T975 = {1: 12.71, 2: 4.30, 3: 3.18, 4: 2.78, 5: 2.57, 6: 2.45, 7: 2.36, 8: 2.31, 9: 2.26, 10: 2.23,
        11: 2.20, 12: 2.18, 13: 2.16, 14: 2.14, 15: 2.13, 16: 2.12, 17: 2.11, 18: 2.10, 19: 2.09, 20: 2.09}
D = dt.date.fromisoformat


def series(metric: str) -> list[tuple[dt.date, float]]:
    out = subprocess.run(["uv", "run", "core/ledger.py", "series", "robots-software", metric, "--as-of", AS_OF],
                         cwd=ROOT, capture_output=True, text=True, check=True).stdout
    rows = sorted((D(l.split(",")[0]), float(l.split(",")[1])) for l in out.splitlines()
                  if len(l.split(",")[0]) == 10)
    front, top = [], 0.0
    for d, v in rows:
        if v > top:
            front.append((d, v))
            top = v
    return front


def months(d: dt.date, d0: dt.date) -> float:
    return (d - d0).days / 30.44


def ols(pts: list[tuple[float, float]]) -> tuple[float, float]:
    n = len(pts)
    mx, my = sum(x for x, _ in pts) / n, sum(y for _, y in pts) / n
    sxx = sum((x - mx) ** 2 for x, _ in pts)
    b = sum((x - mx) * (y - my) for x, y in pts) / sxx
    sd = math.sqrt(sum((y - my - b * (x - mx)) ** 2 for x, y in pts) / (n - 2)) if n > 2 else 0.0
    return b, sd / math.sqrt(sxx)


def doubling(s, a: str, b: str = "9999-12-31") -> str:
    """'3.60 mo [3.3-3.9], n=13' over the rows dated a..b (the frontier in force at a included)."""
    lo, hi = D(a), D(b)
    pts = [(d, v) for d, v in s if lo <= d <= hi]
    prior = [(d, v) for d, v in s if d < lo]
    if prior and (not pts or pts[0][0] > lo):
        pts = [(lo, prior[-1][1])] + pts
    if len(pts) < 3:
        return "n<3"
    xy = [(months(d, pts[0][0]), math.log2(v)) for d, v in pts]
    k, se = ols(xy)
    t = T975.get(len(xy) - 2, 2.0)
    ci = f"[{1 / (k + t * se):.2f}-{1 / (k - t * se):.2f}]" if k > t * se else "[open]"
    return f"{1 / k:5.2f} mo {ci:13s} n={len(pts)}"


def breakpoint(s) -> list[tuple[float, dt.date, float, float]]:
    """Two joined straight lines in log2 space, break dates on the 1st of every other month
    2021-2025: (SSE, break, doubling before, doubling after), best first."""
    d0 = s[0][0]
    xs, ys = [months(d, d0) for d, _ in s], [math.log2(v) for _, v in s]
    out = []
    for y in range(2021, 2026):
        for m in range(1, 13, 2):
            bd = dt.date(y, m, 1)
            b = months(bd, d0)
            X = [(1.0, x, max(0.0, x - b)) for x in xs]
            # normal equations, 3x3
            A = [[sum(r[i] * r[j] for r in X) for j in range(3)] for i in range(3)]
            v = [sum(r[i] * yy for r, yy in zip(X, ys)) for i in range(3)]
            c = solve3(A, v)
            sse = sum((c[0] + c[1] * r[1] + c[2] * r[2] - yy) ** 2 for r, yy in zip(X, ys))
            out.append((sse, bd, 1 / c[1], 1 / (c[1] + c[2])))
    return sorted(out)


def solve3(A, v):
    M = [row[:] + [vv] for row, vv in zip(A, v)]
    for i in range(3):
        p = max(range(i, 3), key=lambda r: abs(M[r][i]))
        M[i], M[p] = M[p], M[i]
        for r in range(3):
            if r != i:
                f = M[r][i] / M[i][i]
                M[r] = [a - f * b for a, b in zip(M[r], M[i])]
    return [M[i][3] / M[i][i] for i in range(3)]


def main() -> None:
    S = {m: series(m) for m in ("horizon-80-blended", "horizon-80-software-eci", "horizon-80-remote-rli",
                                "eci-frontier-by-release", "rli-automation-by-release",
                                "metr-80-horizon-by-release", "metr-50-horizon-by-release")}
    blend0 = str(S["horizon-80-blended"][0][0])
    last = str(S["horizon-80-blended"][-1][0])
    split = D(blend0) + (D(last) - D(blend0)) / 2
    print(f"== 1. The KPI and its parts, over the KPI's window {blend0}..{last} (halves split {split})")
    for m in ("horizon-80-blended", "horizon-80-software-eci", "horizon-80-remote-rli", "rli-automation-by-release"):
        s = S[m]
        print(f"  {m:28s} all {doubling(s, blend0)}  first half {doubling(s, blend0, str(split))}"
              f"  second half {doubling(s, str(split))}")
    e = [(d, v) for d, v in S["eci-frontier-by-release"] if d >= D(blend0)]
    k, _ = ols([(months(d, e[0][0]), v) for d, v in e])
    print(f"  eci-frontier-by-release      {k:.2f} ECI points per month (linear OLS, from {e[0][0]})")
    sw, rw = S["horizon-80-software-eci"], S["horizon-80-remote-rli"]
    print(f"  software horizon since 2024: {doubling(sw, '2024-01-01')}; since its start: {doubling(sw, '2023-01-01')}")

    print("\n== 2. METR's own measurements (frontier by release date)")
    for m in ("metr-50-horizon-by-release", "metr-80-horizon-by-release"):
        s = S[m]
        print(f"  {m}")
        for a, b, lab in (("2019-01-01", "2025-03-31", "2019..2025-03 (METR's original paper span)"),
                          ("2019-01-01", "9999-12-31", "all (2019..2026-04)"),
                          ("2023-01-01", "9999-12-31", "from 2023"),
                          ("2024-05-01", "9999-12-31", "from the fitted break (2024-05-01)"),
                          ("2025-06-05", "9999-12-31", f"over the KPI's window, from {blend0}")):
            print(f"    {lab:45s} {doubling(s, a, b)}")
        for sse, bd, before, after in breakpoint(s)[:3]:
            print(f"    break {bd}: SSE {sse:.2f}, doubling {before:.1f} mo before, {after:.2f} mo after")
    print("  METR's own file (benchmark_results_1_1.yaml, p50): all-time 187.8 days = 6.2 mo,"
          " from 2023 128.7 days = 4.2 mo [3.4-5.2]")

    print("\n== 3. The remote side's pace vs the assumed slope (BETA) of METR's success-vs-length curve")
    sys.path[:0] = [os.path.join(ROOT, "core"), os.path.join(ROOT, "views")]
    import kpi_charts  # noqa: E402  the chart module's re-implementation of the RLI conversion
    with open(kpi_charts.CALIBRATION_JSON, encoding="utf-8") as f:
        cal = json.load(f)
    rli = S["rli-automation-by-release"]
    for beta in (0.4, 0.5, 0.6, 0.7, 0.8, 1.0):
        c = json.loads(json.dumps(cal))
        c["rli"]["beta"] = beta
        k80 = 2 ** (-math.log(4) / beta)
        h = [(d, kpi_charts.rli_h50(v, c) * k80) for d, v in rli]
        mark = "  (used)" if beta == cal["rli"]["beta"] else ""
        print(f"  BETA {beta:.1f} (odds x{math.exp(beta):.2f} per doubling): latest 80% horizon"
              f" {kpi_charts.hours(h[-1][1]):>7s}, doubling {doubling(h, blend0)}{mark}")


if __name__ == "__main__":
    main()
