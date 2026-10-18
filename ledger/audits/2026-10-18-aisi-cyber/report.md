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

OLS of log2(AISI horizon) on ECI: **0.216 +- 0.032** doublings per ECI point over the 9 models with
an ECI score, **0.178 +- 0.028** without GPT-5.5 (which AISI calls highly uncertain), against the
frozen calibration's 0.2226 (METR's software suite, 21 models, ECI <= 156.76). The task-horizon
driver (drivers.yaml) already allows a frontier slope of about 0.18-0.27 (an assumed sd of 0.043 per
point); AISI's slope sits in the lower half of that range. If the flatter value held beyond ECI
156.76, the ~10-point extrapolation to today's frontier would overstate the software horizon by about
(0.223 - 0.178) x 10 = 0.45 doublings: inside the driver's 0.70-doubling software conversion error.

Use: an independent check on the *slope*, the part of the conversion the frontier extrapolation rests
on (GPT-5.5 at ECI 158.95 is beyond METR's calibration range), not on the level. Owner decision
pending: whether to narrow the driver's slope allowance with it (not done here).

## Series

Registered `aisi-cyber-h80-by-release` (h, irregular): the release-cohort frontier of the table above
(GPT-5.5 is below Mythos Preview, so not a frontier step), release dates from Epoch's ECI file (Mythos
Preview: 2026-04-07, METR's TH1.1 file). Published 2026-05-13 (the post), retrieved 2026-10-18.
Re-read the figure when AISI updates it (gather/sources/robots-software.yaml lists the post).
