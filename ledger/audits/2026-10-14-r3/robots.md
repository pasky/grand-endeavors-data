# Round-3 robotics ETA verification

Scope: seven r2-correction records, software `assess:20261014T164549Z` and hardware `assess:20261014T165450Z`, versus r1 runs `20261014T143724Z` / `20261014T145110Z`. Read rubric v5 fully, the round-2 reports, current working and predecessor comparisons; checked effective events and METR series.

**2 MAJOR findings under the specified categorical bar: one residual labelling error and one new sensitivity implementation error. Neither changes the base ETAs.**

## Findings

1. **Nature — MAJOR, incomplete closure of r2 #5.** In `data/ledger/assessments/notes/robots-software/20261014T164549Z.md:402`, the input register still labels 2.53/3.45/5.97 months measured and describes them as fitted values. The 2.53-month value is not a measured fit: it is the judgmental geometric combination of the fast confidence bound and half-window fit. The next row, shared discussion and assessment calc correctly label the forecast distribution assumed, so this is a contradictory leftover, not a concealed model change. Replace the measured row with the actual OLS/CI/half-window/long-run estimates, as already done for kernel and solo. The requested assumption-versus-measurement correction is not completely implemented.

2. **Dark Line — MAJOR, new wrong-input sensitivity.** Hardware notes `20261014T165450Z.md:53,180` advertise changing shared stall S0 from 0.02 to 0.08, but line 788 leaves S0 unchanged and raises own failure from 0.10 to 0.16. These are not equivalent independent risks: intended survival is 0.92×0.90 = 0.828; implemented survival is 0.98×0.84 = 0.8232. Re-running with the same 50k draws and only the shared threshold changed gives p_achieved **0.828**, p50 **2031.48**, rather than **0.824 / 2031.50**. Fix the override and propagated table values. Numerically small, but this computes a different sensitivity, not merely an incomplete one.

## Round-2 closure

- **#1 Fukushima:** fixed. Unreported rounds remain unknown; Beta(2,8) is explicitly assumed, sensitivity-tested, and the earlier attribution is corrected. Retaining its value is justified.
- **#2 Solopreneur:** fixed. Levels/Base44 no longer enter qualifying-gap or ramp arithmetic; HeadshotPro is explicitly legacy/unverified. The retained assumed lag is tested against a separate legacy-anchored ramp.
- **#3 Dark Line:** fixed. Throughput now gates success; charging consumes spares; upkeep and changeover are separately accounted for. Throughput is explicitly nonbinding at base, with a slower alternative.
- **#4 Wozniak:** fixed. Three-home sensitivity uses p³; median reproduces at 2029.93 versus previous 2029.70.
- **#5:** software/taxi forecast spreads are otherwise correctly separated from empirical estimates and sensitivity-tested.

## Reproduction and stability

Executed both software scripts, all current hardware script sections and predecessor base models in memory under a **1.5-GiB limit**, with chunked hardware grids. Printed outputs reproduce exactly; the wrong-input sensitivity above also reproduces mechanically. Medians: solo 2029.21, kernel 2029.12, Nature 2029.94; taxi 2028.62, Dark Line 2031.28, Fukushima 2027.78, Wozniak 2028.03.

All stored quantiles/probabilities remain unchanged versus r1. Dark Line’s decimal +0.07-year move is correctly attributed to charging spares. Current stored quantiles and labels use calendar-year flooring; nulls agree with achievement probabilities. Selected evidence IDs are effective. Owner-pending definitions are not findings.
