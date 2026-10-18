#!/usr/bin/env python3
# /// script
# dependencies = ["pillow", "numpy", "scipy"]
# ///
"""Read the per-model 80% cyber time horizons off UK AISI's figure (the post publishes no data).

  uv run digitize.py [figure.png]     (default: downloads FIGURE)

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

raw = open(sys.argv[1], "rb").read() if len(sys.argv) > 1 else urllib.request.urlopen(FIGURE, timeout=60).read()
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
