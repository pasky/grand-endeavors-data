# ECI already contains METR horizons and RLI: does that bias the KPI? (2026-10-18)

Owner question (2026-10-18): the KPI treats ECI as the software side and RLI as general remote
work, "but maybe ECI itself is a blend already?"

## What ECI contains

ECI is Epoch's IRT index over ~60 benchmarks (performance = sigmoid(slope x (capability -
difficulty)), one capability per model; code github.com/epoch-research/eci-public). The 12 top
models' inputs (processed_data_for_eci.csv, vintage of 2026-10-18) are maths (OTIS AIME,
FrontierMath tiers 1-3 and 4, ProofBench), knowledge and science (GPQA, SimpleQA, HLE), puzzles and
games (chess, mystery games, ARC-AGI 1 and 2, furniture assembly, SpireClimb, Balrog), software
(FrontierCode, FrontierSWE, MirrorCode, DeepSWE, GSO, WeirdML, PostTrainBench), professional and
computer-use work (APEX-Agents, OSWorld 2.0) and others (DTBench, LMCA, EBR-bench, Surface Evolver
Bench). So ECI is a general capability index; the KPI's "software" label comes from the
conversion target (METR's software/ML/cyber suite), not from ECI's content.

Two inputs overlap the KPI itself:
- **METR Time Horizons** (34 models, all 21 calibration pairs): the horizons the ECI -> METR
  calibration regresses on, so the calibration is in principle circular.
- **Remote Labor Index** (15 models, incl. Claude Opus 5.5 and GPT-6 Astra): the KPI's other half,
  so the blend's two halves are not fully independent.

## Test (eci_overlap.py, reproducible)

Refit ECI with Epoch's own code (eci-public @ e937446) on Epoch's published fit input, with and
without METR and RLI, and redo the p80/p50 calibration on CALIBRATION_PAIRS for each variant.
Input: benchmark_data.zip retrieved 2026-10-18, sha256
0555162213a0a0495fdfbadab08bd909b4042110161b68f691c81f52abfabc82. The full refit reproduces the
published eci_scores.csv to 0.005 ECI points (all 277 models). Output: output.txt,
calibration.csv, eci_variants.csv (every model under every variant).

Note: fitting from the raw CSVs via eci-public's loader does not reproduce the published scores
(frontier +0.6 points; the loader's input differs from processed_data_for_eci.csv in about 100 model x
benchmark rows, mostly Chess Puzzles and models it drops), so the published fit input is used instead.

## Results

| variant | p80 ECI per doubling | R² | resid sd | Opus 5.5 h80 (own refit) | SWE-Marathon gap |
|---|---|---|---|---|---|
| full (= KPI's line) | 4.492 | 0.966 | 0.49 | 7.93 h | +0.01 |
| no RLI | 4.492 | 0.966 | 0.49 | 7.94 h | +0.02 |
| no METR | 4.380 | 0.970 | 0.46 | 9.07 h | -0.17 |
| no METR, no RLI | 4.380 | 0.970 | 0.46 | 9.09 h | -0.16 |

- **The ECI scores barely depend on METR or RLI.** The fit gives METR a shallow curve (slope 0.063
  per ECI point; RLI 0.148), so dropping both moves calibration models by at most 0.22 ECI points
  (Claude 3 Opus +0.20, GPT-4 -0.22, the rest within 0.1) and frontier models by at most 0.03.
  So the circularity does not flatter the fit (R² 0.966 with METR, 0.970 without),
  and RLI's double counting has no measurable effect.
- **The one material change is a single pair, not circularity.** GPT-5.3 Codex has only 4 ECI
  benchmarks (WeirdML, METR, SWE-bench Verified, Terminal-Bench); without METR it falls below
  Epoch's 4-benchmark minimum and loses its ECI. It is the highest calibration pair (156.76) and
  the second-lowest residual (-0.88 doublings). Dropping that pair alone from the published ECI gives the same line as
  the no-METR refit (4.376 ECI per doubling, Opus 5.5 at 9.08 h): the whole difference is that
  one thinly measured model. Its effect, +0.19 doublings (+14%) at the frontier, is well within
  the frontier prediction error (0.55 doublings) and the SWE-Marathon gap stays near zero
  (+0.01 vs -0.16).

## Conclusion

No change to the KPI's metrics: the overlap is real but its effect is negligible, and the frozen
calibration stays (a refit would be new metric ids for a within-noise change). What does change
is the description: ECI is a general capability index expressed in METR software-hours, not a
software benchmark, and it contains METR and RLI (checked here: no measurable effect). The
calibration's sensitivity to GPT-5.3 Codex (a 4-benchmark ECI) is the larger caveat, and it
belongs with the extrapolation caveats already on the dashboard.
