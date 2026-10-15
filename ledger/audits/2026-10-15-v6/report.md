# Independent v6 ETA audit — 2026-10-15

**Result: 2 MAJOR findings affecting 2 milestones.** Neither is a shared-driver or anchor failure. One is a small but reproducible probability error; the other is a rule-7 justification failure.

**Scope correction:** the six specified runs contain **20 milestones**, not 18 (3 software, 5 hardware, 3 rockets, 2 fusion, 4 health, 3 climate). All 20 are covered below. Repository files were not edited; no staging or commits were performed.

## Per-milestone verdicts

Years are stored unconditional p10/p50/p90; “—” means null. Findings distinguish central numerical/rule violations from documentation improvements.

| Milestone | Verdict | Years | Reasons |
|---|---|---|---|
| robots-software/the-linux-kernel-patch | OK | 2028/2029/2031 | Canonical METR draws feed the model; previous result and current result reproduce; no reportable move; all failure scenarios below 10%; assumed policy gate is not a delay. |
| robots-software/the-nature-author | OK | 2028/2029/2035 | Same indexed METR draws; no central private refit; retained inputs reproduce; individually sub-10% failures. The p90 is fragile because success probability is close to .90, but this is disclosed. |
| robots-software/the-10m-solopreneur | OK | 2027/2029/2032 | Canonical coupled/floored 80% METR draws; revenue annualization is explicitly assumed rather than misreported as measured ARR; no reportable move. |
| robots-hardware/robotaxi-saturation | minor | 2027/2028/2031 | No registered shared driver applies; prior simulation reproduces unchanged. Context should separate Baidu's system-wide ride count from Wuhan's fleet count. |
| robots-hardware/the-blue-collar-shift | minor | 2027/2027/2030 | Dyna draws are used directly; mapping from rejects to interventions is assumed and tested. Some stated input intervals are not the actual percentiles of the symmetric-lognormal implementation. |
| robots-hardware/the-dark-line | minor | 2028/2031/— | All three Dyna columns are used; p10 2029→2028 is genuinely attributable to canonical sampling. Same input-interval notation issue as Blue Collar; no central arithmetic failure found. |
| robots-hardware/the-fukushima-test | minor | 2027/2027/2030 | Canonical Dyna odds draws; unknown round outcomes are not counted as failures. Prose uses .075 rather than .087 for odds of probability .08; code uses the correct formula. Label should distinguish unreported valve closure from demonstrated non-completion. |
| robots-hardware/the-wozniak-test | minor | 2027/2028/2032 | Canonical Dyna odds draws feed both trend and LEAP remapping. No new anchor-driven adjustment. LEAP spread .49 and the remapping deserve separate assumed-input sensitivities. |
| rockets/the-deluge | OK | 2033/2035/— | Canonical launch-mass draws, indexed without resampling; no central private fit. Model reproduces, including 5,001/10,000 successes by end-2035. Median sample fragility is disclosed. |
| rockets/the-export | minor | 2030/2035/— | No required driver; unchanged competing-path model reproduces. Inherited space-access failure .02 differs from .01 in the other rocket models without a distinct event definition; this is disclosed, not silently retuned. |
| rockets/the-homestead | minor | 2045/2075/— | No required driver; unchanged model reproduces. The .190 failure has a counted outcome class and an explicit explanation for the absence of a countable surface-base pursuit class. Historical station/program classifications need better citations. |
| fusion/the-first-watt | minor | 2028/2032/2060 | Canonical start draws plus .25 years; pre-anchor distribution precedes anchor analysis; .598 versus .3678 gap has a concrete Helion/Polaris crux. p90 move is attributable. Some successor sensitivity distributions are mislabeled as triangular after piecewise transformation; central result is unaffected. |
| fusion/grid-parity | minor | 2033/2046/— | Both required drivers sampled without central refit; output reproduces. The 20% branch has 1/6 counts and explicit calibration. CSP/CCGT classification sources and the approximate CPI value need tighter provenance. |
| health/precise-screening | minor | 2041/2057/2091 | No driver/anchor applies; unchanged model reproduces. Both year moves are genuine flooring corrections. Dirichlet concentration and class-rate spread lack complete separate sensitivities. |
| health/taming-cancer | **MAJOR** | 2055/2073/— | **M1:** the claimed solid-only survival correction is absent from the executable model. Applying the stated −.0008 changes stored p_achieved from .834 to .833, although all stored years stay unchanged. |
| health/the-long-middle-age | **MAJOR** | 2034/2042/— | **M2:** F1 .15→.18 and F2 .12→.11 are attributed to v6, but adding counts does not itself invalidate the prior disclosed judgments or mandate these exact replacements. The p10 flooring correction is valid; the separate probability recalibration needs a genuine rule-7 basis. |
| health/unbroken-mind | minor | 2052/2079/— | No driver/anchor applies; unchanged model reproduces. Corrected 1/10 or deduplicated 1/9 trend counts support a disclosed judgment, not an exact .15 derivation. Obsolete unresolved-definition prose and incomplete subsidiary sensitivities remain. |
| climate/the-bend | minor | 2031/2036/2050 | Canonical curvature draw i is used for draw i; TRACE reconciliation is an explicit inherited mapping, not a new private fit. No stored move. Reporting-date precision and isolated land-use-spread sensitivity need improvement. |
| climate/the-balance | minor | 2087/—/— | Canonical curvature and the attribution chain reproduce. The 10% removal-stall branch has 0/5 counts, caveats, and a 1/6 adverse alternative; member-level historical sources remain insufficiently traceable. |
| climate/the-ceiling | minor | 2082/—/— | Same driver draws and reproduced p10 attribution; ten-year hold is implemented. Same counted-class sourcing caveat as Balance; no new central arithmetic failure found. |

## MAJOR findings

### M1 — Taming Cancer: stated correction omitted from the actual calculation

**Records/files:** `data/ledger/assessments/health.jsonl`, record `2026-10-15-milestone-taming-cancer`, by `assess:20261015T110538Z`; `data/ledger/assessments/notes/health/20261015T110538Z.md`, milestone section beginning line 138, input register, and Appendix A class `Can`.

The modeled target is solid tumours, while the measured 69% anchor is all cancers. The notes and record's calc describe a solid-only adjustment of −0.08 percentage points, based on hematological cancers being 9.41% of cases with 69.8% survival. The implied solid-only center is `(0.69 − 0.0941 × 0.698)/(1 − 0.0941) = 0.689169`, approximately 0.6892.

But `Can.run` uses `S5=(.685,.695)` and interpolates directly within that interval. It never subtracts .0008. The current record therefore does not implement the numerical model it describes.

Independent common-draw rerun:

| Calculation | P(by 2100) | p10 | p50 | p90 |
|---|---:|---:|---:|---|
| Actual current code | .8343 | 2055.63 | 2073.78 | null |
| Apply the stated −.0008, `S5=(.6842,.6942)` | .8328 | 2055.71 | 2073.91 | null |

At the record's three-decimal probability precision, this is **.834→.833**. The difference is small, but the audit's severity definition makes a reproducible number-changing discrepancy MAJOR; it does not require a one-year ETA move or a .05 probability move. The previous working treated the difference as negligible, and the in-run review called it minor because years were unchanged; neither makes the current claim that the adjustment is included true.

**Repair:** implement the stated correction and attribute the small probability fix, or explicitly document and justify retaining the all-cancer anchor as an approximation, withdrawing the assertion that the correction enters the calculation. Do not describe the current output as already solid-adjusted.

Independent artifacts: `/tmp/ge-audit/work/health/extra.py`, `extra-output.txt`, and extracted `block0.py:88–115`.

### M2 — Long Middle Age: new reference-class documentation is not by itself a recalibration mandate

**Records/files:** `data/ledger/assessments/health.jsonl`, old `2026-10-14-milestone-the-long-middle-age`, by `assess:20261014T155116Z`, versus current `2026-10-15-milestone-the-long-middle-age`, by `assess:20261015T110538Z`; previous notes `data/ledger/assessments/notes/health/20261014T155116Z.md:264–286`; current notes `.../20261015T110538Z.md:256–302`, and current `basis.change_note`.

The old F1=.15 and F2=.12 are explicitly assumed probabilities, not arithmetic mistakes. The new record replaces them with .18 and .11 from Laplace-smoothed selected analogues, while attributing the changes to v6 and denying new evidence. V6 requires counted classes and a defensible transfer or a reason the relevant class cannot be counted. It does **not** require Laplace smoothing, exact adoption of an analogue's posterior mean, or abandoning a previously disclosed judgment that the counts do not contradict. Rule 7 protects input choices, not just changes exceeding the reporting thresholds.

The account identifies missing count documentation, but does not establish why the old .15/.12 values cease to be valid judgments. F1=.15 is between the cited raw 1/9=.111 and smoothed 2/11=.182; F2=.12 is essentially adjacent to the proposed 1/9=.111. Other milestones in these very runs correctly retain prior judgments when the newly supplied counts merely bracket them. F1 also changes its failure interpretation from clock/function improvement without disease benefit to failure of clocks to register disease-beneficial interventions; that is a new mapping choice, not just adding a denominator.

Independent reproduction isolates the changes:

| Inputs | P(by 2100) | p10 | p50 |
|---|---:|---:|---:|
| Previous F1=.15, F2=.12 | .7473 | 2034.89 | 2042.33 |
| F1=.18, F2=.12 | .7208 | 2034.96 | 2042.84 |
| F1=.18, F2=.11 | .7276 | 2034.94 | 2042.69 |

Thus the stored **.747→.728** is a substantive input change, not canonical-driver noise or flooring. Being below the .05 attribution threshold does not exempt it from rule 7's restriction on replacing sound assumed inputs. The valid separate encoding fix is **p10 2035→2034**.

**Repair:** retain .15/.12 while adding the counted context, unless the assessor can identify and explain a real newly learned evidential update or a previous mapping error. Newly consulted historical papers could support a rule-7(a) update, but that requires an honest new-evidence attribution and an explicit assumed transfer, rather than presenting .18/.11 as required by v6. This finding is about the justification as written, not a claim that .15/.12 are objectively superior probabilities.

**Count-quality caveat, independently checked:** Wang (`PMC5371228`) supports three positive intervention categories; Petkovich (`PMC5578459`) supports CR, GHR knockout and Snell dwarf categories. `PMC6224226` reuses published data and compares multiple clocks, three CR experiments and three dwarf experiments, with non-significant rapamycin results. The reported 8/9 is therefore an illustrative paper/category aggregation, not nine independent experiments measuring the probability that every human intervention fails by 2100. Its counting unit, dependence, and mouse-to-human/existential transfer must be disclosed. The retrieved source also does not match the notes' Meer/eLife identification. Saved fetched sources: `/tmp/ge-audit/sources/PMC5371228.md`, `PMC5578459.md`, `PMC6224226.md`.

## Driver and anchor checks

All **13 milestones listed in any `used_by`** consume the required canonical draws (14 driver–milestone links across six drivers). The other seven have no registered driver requirement. I regenerated the draws through `ledger.py driver-draws ... --as-of 2026-10-15`, inspected the consuming code, and reran every current model.

| Driver in `data/drivers.yaml` | Required consumers | Actual central use |
|---|---|---|
| metr-horizon | kernel, Nature, solopreneur | Same 10,000 indexed horizon/date/rate arrays; 80% uses the canonical floored rate. |
| dyna-failure-halving | Blue Collar, Dark Line, Fukushima, Wozniak | Same 10,000 halving/odds/throughput draws, converted from months to years. |
| launch-mass | Deluge | Canonical mass and slope arrays; independent milestone crossing/failure noise. |
| fusion-first-watt | First Watt, Grid Parity | Both use the same commercial-start array; First Watt adds .25 years. |
| irena-lcoe | Grid Parity | Canonical `r_offshore` array. |
| fossil-co2-deceleration | Bend, Balance, Ceiling | Canonical curvature array, with shared own component paths. Fixed level/rate are checked against the series; the explicitly disclosed TRACE mapping reconciles component rates. |

Private-fit code remains only for previous-model reproduction, attribution, or labeled sensitivities; I found **no private central refit**. No baseline silently switches to a favorable sensitivity.

First Watt's pre-anchor distribution appears at notes line 49, before the anchor analysis at line 138: p50 **2032**, p10 **2028**, p90 **2060**, P **.93**. The file asserts it was written before reading anchor observations; static committed files cannot independently prove execution chronology. The previous unanchored forecast already had p50 2032.

The regenerated anchor calculation gives **P(by end-2035)=.598**, not the approximate **.55** obtained by interpolating stored quantiles. Against `manifold-pr0qngelph-p=.3678`, the difference is **.2302**, exceeding .15. The current record's calc names the driver Helion weight **.50**, schedule multiplier **2**, absence of demonstrated net electricity, and verified Polaris output or a changed Orion/Microsoft schedule as the resolving observation. It also identifies the market's **11** forecasters and weak resolution match. This is a real, quantified crux, not an unexplained discount or an unattributed move toward the market. Sensitivity weight .25 gives .411 by end-2035; weight .10 gives .305. The second weaker bound holds: **.739≤.8710**, with **56** forecasters.

## Failure-scenario coverage

- Software: all individual failures <10%; no mandatory count is missing.
- Hardware: all individual failures <10%; Dark Line's own .10 mask represents separately named .08 economic and .02 disclosure scenarios, already present before v6, not a newly invented split to evade counts.
- Deluge/Export: all milestone-stopping scenarios <10%. Export's .50 failure of one route does not stop its competing route; notes additionally discuss a 0/1 route analogue.
- Homestead: the .190 resupply/no-pursuit/no-successor outcome has 0/5 station food-production outcomes, while the notes explicitly distinguish these from unobserved decisions by nonexistent surface-base programs. The missing pursuit denominator is genuinely argued; .35/.45 remain assumptions with sensitivities.
- First Watt: .03 physics and .04 funding failures are individually below threshold.
- Grid Parity: non-learning .20 has named membership, **1/6** raw versus **2/8=.25** smoothed. Nuclear cost literature and the three ledger renewable series make the broad classification plausible; CCGT/CSP criteria and source linkage remain weak, not absent counts.
- Screening: .0015 ceiling and .062 slow diffusion are below threshold.
- Middle Age: F1=.18 and F2=.11 have numerical counts, but the mapping and update problem is M2; the 0/7 platform class is a hand-selected set of approved platforms, not a demonstrated census of all resolved therapeutic-platform attempts.
- Cancer: plateau input .10 has 0 aggregate decade stalls over approximately 9.2 series-decades plus 4/25 site declines; permanence is explicitly uncountable and assumed. Slow failure .1048 has 0/2 long spans and 2/4 approximately twenty-year spans below ~1.03%/yr. Counts are traceable to the supplied historical endpoint series; these are small, dependent analogues, not measured permanent-failure frequencies.
- Dementia: stall .15 has **1/10** trend series or **1/9** deduplicated population units; the mixture of incidence, standardized and crude prevalence is disclosed. Slow/no-regime failure .200 has an explicit decomposition, **0/3** prevention-readout analogue and **1/3** slow prevalence series. This is a disclosed transfer, not a mechanically measured .15/.40.
- Balance/Ceiling: removal stall .10 has **0/5** named abatement-service classifications, giving .083–.143 under the stated smoothers. Unmeasured climate-only CCS is excluded and alternatively treated as a stall, **1/6→.214–.25**. The earlier 41-Mt subset/whole-sector error is withdrawn. The five historical classifications lack retrievable member-level sources and have revenue-boundary ambiguities; this remains minor because they are expressly assumed classifications with adverse alternatives, not claimed measurements. Decarbonization stall .05 is below threshold.

## Rule-7 moves

Actual previous/latest records confirm the requested moves and no additional calendar-year moves:

| Target | Stored move | Independent check |
|---|---|---|
| Dark Line | p10 2029→2028 | Previous actual script 2029.04; private comparison at 10,000 draws 2029.03; canonical result 2028.97. Valid v6 sampling attribution. |
| Precise Screening | p10 2042→2041; p50 2058→2057 | Same model gives 2041.54/2057.91 in both versions. Valid rounding-to-floor correction. |
| Long Middle Age | p10 2035→2034; P .747→.728 | Flooring is valid; separate F1/F2 recalibration is M2. |
| First Watt | p90 2061→2060 | Actual previous script 2061.13; canonical result 2060.88. Valid v6 sampling attribution. |
| Balance | p10 2088→2087 | Previous 50,000-draw result 2088.2; own first 10,000 still 2088.2; canonical curvature gives 2087.5. |
| Ceiling | p10 2083→2082 | Previous 2083.1; own first 10,000 2083.3; canonical curvature 2082.1. |

Climate's removal of the private .00105 spread on fixed `g_2020` is disclosed separately; its canonical-curvature substitution explains the stored p10 changes. No p_achieved move reaches .05. All other stored quantile years and nulls are unchanged.

## KEY CLAIMS — exact verification pointers

1. **M1 numerical mismatch:** `data/ledger/assessments/health.jsonl`, `2026-10-15-milestone-taming-cancer`, `basis.eta.calc` and `p_achieved=.834`; notes `health/20261015T110538Z.md`, class `Can`, `S5=(.685,.695)`. Scratch `health/extra-output.txt`: **.8343→.8328**, p50 **2073.78→2073.91** with stated **−.0008** applied.
2. **M2 attribution:** same ledger file, `2026-10-15-milestone-the-long-middle-age`, versus `2026-10-14-milestone-the-long-middle-age`. Current `change_note` attributes **.15→.18**, **.12→.11** to v6. Scratch `health/output.txt:15–18`: **.7473→.7208→.7276**, median **2042.33→2042.84→2042.69**. Old notes `20261014T155116Z.md:264` explicitly identify .15/.12 as assumptions.
3. **Anchor gap is explained:** `data/ledger/assessments/fusion.jsonl`, `2026-10-15-milestone-the-first-watt-3`, `basis.eta.calc`; notes `fusion/20261015T105338Z.md:49,138–166`. Series `manifold-pr0qngelph-p@2026-10-15=.3678` (11), `manifold-iubcricrjrizushzxq97-p@2026-10-15=.8710` (56). Scratch `fusion/anchors.txt`: **.598/.739**, Helion-weight .25 alternative **.411**.
4. **Software spot-checks:** `ledger.py series robots-software metr-50-horizon-by-release --as-of 2026-10-15` and the 80% counterpart: **1044.78/185.91 minutes on 2026-04-07**. `data/ledger/events/robots-software.jsonl`, `2025-01-01-pieter-levels-3m-arr-rv`: **$3M revenue**, with no stated period or ARR. Current solo notes correctly register annualization as assumed.
5. **Hardware spot-checks:** `data/ledger/events/robots-hardware.jsonl`, `2026-08-27-dyna-din-tai-fung-shift-throughput`: **75%→93%** quality pass over **14 months**, **480→1590** per shift; canonical medians **7.623/6.521/8.102 months** for fraction/odds/throughput. `2026-06-28-agibot-longcheer-whole-section-8-robots`: **8 robots, 55,107 operations, 99.987%, >54 hours**; line-hour interpretation is assumed, giving **.133** task failures/robot-shift. `2026-09-17-figure-helix-25-30-homes`: **56%** task success in **30** homes, not measured coffee success.
6. **Rockets spot-checks:** series `payload-mass-to-orbit`, **2021–2025 = 797.4/1046.4/1462.8/2625.9/3194.0**; event `2025-01-01-jsr-payload-mass-2025-rv2` confirms **3194.0/2625.9** and leaves metric-versus-short-ton ambiguity. `data/ledger/events/rockets.jsonl`, `2023-06-01-iss-98-percent-water-recovery-rv`: **98%** water recovery; `2023-09-06-moxie-completes-mission-rv`: **12 g/hour**, **16** runs, **98%+** purity. These are not food-closure achievements.
7. **Fusion spot-checks:** `data/ledger/events/fusion.jsonl`, `2025-04-07-nif-q-4-13-rv`: **8.6/2.08 MJ, Q=4.13**, not net electrical gain; `2025-01-01-helion-2028-microsoft-target-rv`: **2028** target. Series `lcoe-offshore-wind-irena`: **208/155/127/89/81/79** at **2010/2015/2018/2020/2022/2024**, supporting the driver's **.076107/year** full-history rate. `2023-01-01-lindley-fusion-foak-lcoe-rv`: estimate **>$150/MWh**, not an observed plant cost.
8. **Health spot-checks:** `data/ledger/events/health.jsonl`, `2025-01-01-acs-2025-five-year-survival-all-cancers-rv`: **69%**, **2014–2020** diagnoses; `2021-01-01-fitzgerald-diet-lifestyle-epigenetic-age-rv`: **3.23 years relative to controls**, not a within-group reduction; `2025-01-01-adams-us-dementia-prevalence-80-plus-rv`: **24.19%/37.36%**, estimates dated **2002**. Series `hale-median-country@2023=63.8`, context only.
9. **Climate spot-checks:** series `co2-emissions-fossil-gcb`: **23.26/29.19/34.71/38.1 Gt** for **1995/2005/2015/2025**; total series **2025=42.2**. `data/ledger/events/climate.jsonl`, `2026-09-24-climate-trace-jul-2026-ghg`: Jan–Jul **33.7 GtCO₂e, +.3%**; `2026-09-01-edgar-2026-ghg-2025`: **54.1 GtCO₂e, +.7%**; `2026-09-21-irena-tripling-tracker-693gw-2025`: **5.15 TW, +693 GW**, hence **ln(5.15/4.457)=.14452/year**. All match the inputs and their disclosed mappings.
10. **Canonical sampling and output:** `data/drivers.yaml` has **seed 20261015, n=10000**. Scratch `work/<section>/output.txt` contains independent full current reruns; `work/<section>/prev/` contains extracted actual previous scripts and reruns. Current fusion P **.9324/.7475**; climate **.9505/.2820/.1831**; software raw quantiles **2028.06/2029.13/2031.46**, **2028.68/2029.93/2035.87**, **2027.70/2029.24/2032.97** reproduce the records' calendar-year encodings.

## Execution and limits

Scripts were extracted under `/tmp/ge-audit/work/`, inspected before execution, then run with `ulimit -v 4000000`, single-threaded BLAS where applicable, and uv. Current climate arrays are bounded at **2000×751**; hardware grid batches are **1500×approximately 1466**; rocket vectors are at most **400,000**, with the propellant sensitivity only **10000×75**; health uses **40,000** small per-draw records. Existing script-specific tighter memory caps were retained. Actual previous scripts were also rerun, including climate's 50,000-draw predecessor and hardware's 200,000-draw baselines.

No current central output failed reproduction. `ledger.py check` for the six sections exits **0**; this does not detect the two substantive findings above. Local ledger/series checks are saved in `work/ledger-checks.txt` and `work/series/`. Primary-source research was limited to the three mouse-clock papers; other historical reference-class facts are assessed for plausibility and citation adequacy, not represented as independently exhaustively verified censuses.
