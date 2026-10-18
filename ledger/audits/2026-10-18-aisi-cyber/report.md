# UK AISI's cyber time horizons: a series, and a check of the ECI conversion's slope (2026-10-18)

Owner question (2026-10-18): why is the AISI cyber horizon not tracked as a series, why is it "not
comparable", and could it be blended into the software (ECI) side of the KPI's calibration?

## Source

AISI, "How fast is autonomous AI cyber capability advancing?" (published 2026-05-13,
https://www.aisi.gov.uk/blog/how-fast-is-autonomous-ai-cyber-capability-advancing), Figure 1:
80%-reliability time horizon on AISI's narrow cyber (CTF) task suite, 2.5M-token budget per task,
a simple agent scaffold, reasoning models only. The post gives no data file and one value in its
text (Claude Sonnet 4.5: 16 minutes). Its doubling time: 4.7 months since late 2024 (February 2026
estimate; 8 months in its November 2025 estimate); Mythos Preview and GPT-5.5 lie above that trend.

## Why its level is not the KPI's (METR's) level

- The 2.5M-token cap and the simple scaffold lower success on purpose (AISI: uncapped, success is so
  high that horizons cannot be computed, and uncapped horizons "would be significantly higher").
- The tasks are narrow cyber skills, not METR's software suite; the longest is 12 h and only six
  are 8 h or longer, so the newest models saturate it (AISI: "highly uncertain").
- Measured against the ECI conversion (below) its level sits 0.77 doublings lower on average, with
  a 0.6-doubling scatter: an offset that belongs to the suite and budget, not to capability.

So it cannot be pooled into the ECI -> METR calibration (that would mix two scales of hours).

## Digitized values (digitize.py, reproducible; run with OPENBLAS_NUM_THREADS=1)

The figure as read is kept here (figure1.png, sha256 2c3ae170b20abeb222731c79fb0e89ead557461b695fe96fedb60a3762ac904e);
`digitize.py figure1.png --write` reproduces models.csv (every marker; the dashboard's ECI chart
overlays it). The Mythos marker is labelled "Mythos Preview (new)" in the figure: AISI's newer
checkpoint, not the early one METR measured.

Marker centroids on the 4778 x 2643 px figure; log axis from its four gridlines (0.1, 1, 10, 100 h;
479.7 px per decade), so the reading error is well under 1%. Check: Claude Sonnet 4.5 reads 16.0
min (AISI's text: 16 min).

| model | 80% cyber horizon | ECI (Epoch, 2026-10-18) |
|---|---|---|
| o1 | 5.6 min | 141.84 |
| Claude 3.7 Sonnet | 6.3 min | 141.14 |
| Claude Opus 4 | 8.5 min | 142.65 |
| GPT-5 | 9.9 min | 150.00 |
| Claude Sonnet 4.5 | 16.0 min | 146.83 |
| Claude Opus 4.5 | 24.1 min | 150.17 |
| Claude Opus 4.6 | 39.6 min | 155.27 |
| GPT-5.3 Codex | 41.5 min | 156.76 |
| Claude Mythos Preview | 4.84 h | (no ECI score) |
| GPT-5.5 | 2.48 h | 158.95 |

## The slope check (slope.py)

OLS of log2(AISI horizon) on ECI: **0.216 +- 0.032** (standard error) doublings per ECI point over
the 9 models with an ECI score, **0.178 +- 0.028** without GPT-5.5 (which AISI calls highly
uncertain; approximate 95% interval 0.11-0.25), against the frozen calibration's 0.2226 (METR's
software suite, 21 models, ECI <= 156.76). The errors are OLS standard errors only: AISI's own
per-model uncertainty (its bootstrap bands) is not propagated. Level offsets (AISI minus converted)
range from -1.84 (GPT-5) to +0.08 (GPT-5.5) doublings, mean -0.77.

Reading: **compatible with the conversion's slope, but too uncertain to validate its
extrapolation.** Without GPT-5.5 the central estimate is about 20% flatter, and no model beyond ECI
156.76 remains, so the frontier is not independently checked. The task-horizon driver (drivers.yaml)
already widens the software conversion error for the slope's form beyond METR's data (an assumed sd
of 0.043 doublings per point, i.e. about 0.18-0.27, folded into a fixed 0.70-doubling level error at
the anchor, not a sampled slope). If only the slope beyond 156.76 were the flatter 0.178, keeping the
fit below it, today's ~10-point extrapolation would overstate the software horizon by about
(0.223 - 0.178) x 10 = 0.45 doublings (1.4x), inside that 0.70-doubling error.

Use: a check on the *slope* of the conversion, not on its level. Owner decision pending: whether to
use it to inform the driver's slope allowance (not done here).

## Verification

- 2026-10-18, extraction: Claude Sonnet 4.5 reads 16.0 min against AISI's text (16 min); marker
  count, colours (provider legend) and evenly spaced gridlines asserted by digitize.py.
- 2026-10-18, independent check: a separate review agent fetched the post and the figure itself,
  inspected it, and reproduced all ten values (peak memory 374 MB under a 2 GiB limit).

## Series

Registered `aisi-cyber-h80-by-release` (h, irregular): the release-cohort frontier of the table above
(GPT-5.5 is below Mythos Preview, so not a frontier step), release dates from Epoch's ECI file (Mythos
Preview: 2026-04-07, METR's TH1.1 file). Published 2026-05-13 (the post), retrieved 2026-10-18.
Re-read the figure when AISI updates it (gather/sources/robots-software.yaml lists the post).
