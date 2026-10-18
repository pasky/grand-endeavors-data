# Sources for measuring task horizons at the frontier: what was checked, and why each fails (2026-10-18)

Owner question (2026-10-18): instead of extrapolating the ECI -> METR line, could we measure time
horizons directly, e.g. from the per-task results of ECI's benchmarks? Read this before scouting
again; re-check an entry only if its "would change if" condition has happened.

## What a source needs

METR's method fits success against log human task length per model. A usable source needs:
1. **pass/fail per task and model** (ideally per trial), public and machine-readable;
2. **human hours per task**, measured (or at least per-task estimates), not only a histogram;
3. **hours that predict failure** (METR logistic slope >= 0.25 for most configurations, the test
   in gather/collectors/swe_marathon.py `fit()`);
4. **tasks spanning the frontier**: today's 80% horizon is ~8-16 h and the 50% one ~45 h, so tasks
   from ~1 h to weeks;
5. current frontier models, updated as they ship.

A weaker fallback ("score-only", as robots_software.py does for RLI) needs only an overall score
plus the task-length distribution, but assumes METR's logistic shape, i.e. short tasks are nearly
always solved.

## Verdicts

Facts from four research passes (2026-10-18) plus the owner-session checks marked (checked).

| Source | Hours per task | Per-task results | Fails on | Would change if |
|---|---|---|---|---|
| ECI's benchmarks in general (Epoch benchmark_data.zip) | none for most | aggregates only, except Epoch's own runs (Inspect logs) | 2, 4: mostly minute-scale Q&A, many saturated | - |
| SWE-bench Verified (Epoch logs) | OpenAI buckets: 196 <15 min, 261 15 min-1 h, 43 >1 h | yes (Epoch .eval logs, per sample) | 4: too short; top score ~83% | - |
| Cybench | human first-solve times, 2 min-25 h | no | 1, 4: 93% solved | - |
| APEX-Agents (Mercor) | expert estimates, mean 1.8 h | no | 1, 4: Epoch top 87% | - |
| GDPval (OpenAI) | expert self-reports, gold-set mean ~7 h | no; pairwise win rate vs humans | 1, and not pass/fail; last model GPT-5.2 | per-task results released |
| OSWorld 2.0 (checked: HF task data, paper arXiv 2606.29537 App. G.2) | two annotators' range guesses (midpoints), max 6 h; public only as 5 bins | monitor osworld-v2-monitor.xlang.ai down (HTTP 530) | 2, 3: success <= 24% even on <45-min tasks (Table 21), so length is not what limits agents; score-only conversion would mislead for the same reason | - |
| FrontierSWE (checked: github.com/Proximal-Labs/frontier-swe, 17 v1 task.toml) | none (task.toml has difficulty, tags, timeouts only) | yes, plus traces | 2; mostly continuous scores (1) | task.toml gains expert-hour fields |
| DeepSWE (Datacurve) | none | trial browser; HF tasks gated | 2 | - |
| MirrorCode (Epoch) | informal estimates for a few targets only (gotree 1.5-17 weeks) | yes (GitHub data repo) | 2 | - |
| FrontierCode (Cognition) | none ("40 h per task" is authoring effort) | aggregates | 1, 2 | - |
| GSO-Bench, AlgoTune, ALE-Bench, PostTrainBench, ExploitBench, The Agent Company | none | mostly aggregates | 2 (and 1) | - |
| PaperBench, MLE-bench, SWE-Lancer, Horizon-SWE | none (time budgets / payouts, not hours) | aggregates | 2; mostly stale (2024-early 2026) | - |
| METR TH1.1 (HCAST, RE-Bench, SWAA) | measured | yes (YAML) | 5: discontinued 2026-09 (last model 2026-04-07); METR calls >16 h unreliable | METR resumes |
| SWE-Marathon (collected) | expert estimates, 4-380 h | yes | 4 in effect: 6 of 20 tasks nearly always solved, 7 nearly never, so h80 ~10 h for every frontier model (data drivers.yaml task-horizon) | suite v2 with more mid-range tasks |
| Terminal-Bench 4.0 (collected as a rate) | expert estimates, 0.75-60 h | yes | 3: hours do not predict failures (terminal_bench.py docstring) | - |
| UK AISI cyber horizons (collected) | AISI's | chart only | 1; level not comparable (2.5M-token cap) (audit 2026-10-18-aisi-cyber) | data file published |
| RLI (KPI input, score-only) | histogram from the paper's figure | aggregate only | 1 (hence score-only) | per-project results released |
| BRIDGE (McGill-NLP, method) | predicted from IRT difficulty, anchored on METR's tasks (R² 0.81) | n/a | its hours scale ends with METR's tasks (~16 h), so it extrapolates like the ECI line it would check; data ends late 2025 | - |

Related: ECI itself contains METR's horizons and RLI; refitting without them barely matters
(audit 2026-10-18-eci-overlap).

## Conclusion

No existing source measures horizons at the frontier, and the task-horizon tripwire (two gap
series) cannot fire. The fix is our own time-tagged benchmark (TODO.md: "Nothing measures task
horizons at the frontier").
