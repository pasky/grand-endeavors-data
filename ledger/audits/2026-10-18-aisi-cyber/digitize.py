#!/usr/bin/env python3
# /// script
# dependencies = ["pillow", "numpy", "scipy"]
# ///
"""Read the per-model 80% cyber time horizons off UK AISI's figure (the post publishes no data).

  OPENBLAS_NUM_THREADS=1 uv run digitize.py [figure.png] [--write]   (default: downloads FIGURE;
      --write: models.csv; peak memory ~0.4 GB)

Markers: solid discs in the two provider colours (Anthropic 212,94,0; OpenAI 43,74,142), ~33 px;
the legend's smaller discs (29 px, far right) are skipped. The y axis is log10: the four gridlines
are 0.1 h (labelled 6m), 1 h, 10 h, 100 h (labelled 4d), found as full-width light rows. Models are
named by the order of their markers along x (release order; the figure's labels), see MODELS.
Checks: exactly 10 markers, 4 gridlines evenly spaced, and AISI's one value in its text (Claude
Sonnet 4.5: 16 min) read back within 3%.
"""
import io
import math
import sys
import urllib.request

import numpy as np
from PIL import Image
from scipy import ndimage

FIGURE = ("https://cdn.prod.website-files.com/663bd486c5e4c81588db7a48/"
          "6a049b1b50c15bf9b137ab42_aisi_ctf_time_horizon_with_mythos_preview_new%20(1).png")
# markers left to right, as labelled in the figure (provider colour checked)
MODELS = [("o1", "OpenAI"), ("Claude 3.7 Sonnet", "Anthropic"), ("Claude Opus 4", "Anthropic"),
          ("GPT-5", "OpenAI"), ("Claude Sonnet 4.5", "Anthropic"), ("Claude Opus 4.5", "Anthropic"),
          ("Claude Opus 4.6", "Anthropic"), ("GPT-5.3 Codex", "OpenAI"), ("Claude Mythos Preview", "Anthropic"),
          ("GPT-5.5", "OpenAI")]
COLOURS = {"Anthropic": (212, 94, 0), "OpenAI": (43, 74, 142)}

args = [a for a in sys.argv[1:] if a != "--write"]
raw = open(args[0], "rb").read() if args else urllib.request.urlopen(FIGURE, timeout=60).read()
im = np.asarray(Image.open(io.BytesIO(raw)).convert("RGB")).astype(np.int16)   # ~76 MB for 4778x2643
H, W, _ = im.shape
marks = []
for org, col in COLOURS.items():
    lab, n = ndimage.label(np.abs(im - np.array(col, dtype=np.int16)).sum(2) < 25)
    for i, sl in enumerate(ndimage.find_objects(lab), 1):
        h, w = sl[0].stop - sl[0].start, sl[1].stop - sl[1].start
        if 31 <= h <= 36 and 31 <= w <= 36:
            cy, cx = ndimage.center_of_mass(lab[sl] == i)
            marks.append((cx + sl[1].start, cy + sl[0].start, org))
marks.sort()
assert len(marks) == 10, marks
x0, x1 = int(.08 * W), int(.98 * W)
rows = [y for y in range(H) if (((im[y, x0:x1] > 225) & (im[y, x0:x1] < 250)).all(1).mean() > .8)]
grid = []
for y in rows:  # gridlines are 3 px bands: their centres
    if grid and y - grid[-1][-1] <= 1:
        grid[-1].append(y)
    else:
        grid.append([y])
grid = [sum(g) / len(g) for g in grid if len(g) >= 2]
grid = [g for g in grid if 0.15 * H < g < 0.85 * H]   # drop the frame lines
assert len(grid) == 4 and max(np.diff(grid)) - min(np.diff(grid)) < 3, grid
per_decade = (grid[-1] - grid[0]) / 3          # 6m (0.1 h) at the bottom line
hours = lambda y: 0.1 * 10 ** ((grid[-1] - y) / per_decade)
out = {}
for (x, y, org), (name, want) in zip(marks, MODELS):
    assert org == want, (name, org)
    out[name] = hours(y)
assert abs(out["Claude Sonnet 4.5"] * 60 / 16 - 1) < .03, out["Claude Sonnet 4.5"]
print(f"gridlines {[round(g, 1) for g in grid]} ({per_decade:.1f} px per decade); markers {len(marks)}")
print("model,aisi_cyber_h80_h,minutes")
for k, v in out.items():
    print(f"{k},{v:.4f},{v * 60:.1f}")
# models.csv: every marker with its release date and ECI score (Epoch's eci_scores.csv, 2026-10-18;
# Mythos Preview: no ECI score, release date from METR's TH1.1 file); the dashboard's ECI calibration
# chart overlays it (views/kpi_charts.py), the frontier steps are the ledger series
RELEASE_ECI = {"o1": ("2024-12-17", 141.84), "Claude 3.7 Sonnet": ("2025-02-24", 141.14),
               "Claude Opus 4": ("2025-05-22", 142.65), "GPT-5": ("2025-08-07", 150.00),
               "Claude Sonnet 4.5": ("2025-09-29", 146.83), "Claude Opus 4.5": ("2025-11-24", 150.17),
               "Claude Opus 4.6": ("2026-02-05", 155.27), "GPT-5.3 Codex": ("2026-02-05", 156.76),
               "Claude Mythos Preview": ("2026-04-07", None), "GPT-5.5": ("2026-04-23", 158.95)}
if "--write" in sys.argv:
    with open("models.csv", "w", encoding="utf-8") as f:
        f.write("model,release,eci,aisi_cyber_h80_h,published\n")
        for k, v in out.items():
            rel, e = RELEASE_ECI[k]
            f.write(f"{k},{rel},{'' if e is None else f'{e:.2f}'},{v:.4f},2026-05-13\n")
    print("wrote models.csv")
