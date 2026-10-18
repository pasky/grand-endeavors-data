#!/usr/bin/env python3
"""AISI's cyber 80% horizons (digitize.py output) against Epoch's ECI: the slope in doublings per
ECI point vs the frozen ECI -> METR calibration (0.222614), and the level offset.
  uv run slope.py      (ECI values: Epoch's eci_scores.csv as of 2026-10-18)"""
import math
AISI_H = {"o1": 0.0926, "Claude 3.7 Sonnet": 0.1054, "Claude Opus 4": 0.1420, "GPT-5": 0.1655,
          "Claude Sonnet 4.5": 0.2663, "Claude Opus 4.5": 0.4023, "Claude Opus 4.6": 0.6597,
          "GPT-5.3 Codex": 0.6921, "Claude Mythos Preview": 4.8362, "GPT-5.5": 2.4815}
ECI = {"o1": 141.84, "Claude 3.7 Sonnet": 141.14, "Claude Opus 4": 142.65, "GPT-5": 150.00,
       "Claude Sonnet 4.5": 146.83, "Claude Opus 4.5": 150.17, "Claude Opus 4.6": 155.27,
       "GPT-5.3 Codex": 156.76, "GPT-5.5": 158.95}   # Mythos Preview has no ECI score
A, B = -28.242299, 0.222614


def ols(pts):
    n = len(pts); mx = sum(x for x, _ in pts) / n; my = sum(y for _, y in pts) / n
    sxx = sum((x - mx) ** 2 for x, _ in pts); b = sum((x - mx) * (y - my) for x, y in pts) / sxx
    res = [y - (my + b * (x - mx)) for x, y in pts]; sd = math.sqrt(sum(r * r for r in res) / (n - 2))
    return b, sd / math.sqrt(sxx), sd


for label, keys in (("all 9 with ECI", list(ECI)), ("without GPT-5.5", [k for k in ECI if k != "GPT-5.5"])):
    b, se, sd = ols([(ECI[k], math.log2(AISI_H[k])) for k in keys])
    print(f"{label}: slope {b:.3f} +- {se:.3f} doublings per ECI point (calibration {B}), residual sd {sd:.2f}")
off = [math.log2(AISI_H[k] * 60 / 2 ** (A + B * ECI[k])) for k in ECI]
print("level: AISI minus ECI-converted (doublings):", ", ".join(f"{k} {o:+.2f}" for k, o in zip(ECI, off)),
      f"; mean {sum(off) / len(off):+.2f}")
