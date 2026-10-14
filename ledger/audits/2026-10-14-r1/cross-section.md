# Cross-section ETA consistency audit

Checked 20 latest milestones (2026-10-13), notes, framework, RUBRIC §4.1, `drivers`, selected series.

## Shared-driver inventory

Codes give observation dates, not assessment dates:

- **M50/M80:** METR 1,044.78/185.91 minutes, 2026-04-07. Software's 2024-10-13+ window doubles every 3.45/4.09 months; hardware's 2025+ M80: 4.43; health's 2023+ M50: 4.097. Long-run fits agree: 5.97/6.36 months.
- **D:** Dyna quality failures 25%→7%, June 2025–August 2026; halving 7.6 months.
- **C:** IRENA PV/onshore/offshore LCOE, $/MWh, 2020/2022/2024: 55/51/43; 39/33/34; 89/81/79. Fusion log-declines: .06153/.03430/.02980 yearly. Climate: identical PV/onshore histories, no rate.
- **P:** EU/US wholesale $/MWh: 95/50 (2025), 105/52 (H1 2026); no rate.
- **L:** orbital payload 3,194 tonnes, 2025; 2021–25 growth 44.7%/year.
- **G:** fossil CO₂ 23.26/29.19/34.71/38.1 Gt, 1995/2005/2015/2025; growth deceleration .00080015/year².
- **R:** removals proxy .0012 Gt/year, September 2026; renewables 5.15 TW/0.693 TW additions (2025): 15.55%/year, doubling 4.796 years.

| Milestone | Shared input and use |
|---|---|
| Linux Kernel Patch | M50:3.45mo central |
| Nature Author | M50:3.45mo central |
| $10M Solopreneur | M80:4.09mo central |
| Robotaxi Saturation | Own Waymo rides, December 2025, 2.41×/year |
| Wozniak Test | D; M80:4.43mo cross-check |
| Fukushima Test | D; M80:4.43mo cross-check |
| Blue Collar Shift | D; M80:4.43mo cross-check |
| Dark Line | D; M80:4.43mo cross-check |
| Deluge | L central |
| Homestead | L nonbinding context |
| Export | L context, no sale-odds mapping |
| First Watt | No foreign driver; Grid Parity's timing parent |
| Grid Parity | C offshore central; PV/onshore sensitivity; not P |
| Taming Cancer | M50:4.097mo context |
| Precise Screening | M50:4.097mo context |
| Unbroken Mind | M50:4.097mo context |
| Long Middle Age | M50:4.097mo context |
| Bend | G central; C/P context |
| Balance | G/R central; C/P context |
| Ceiling | G/R central; C/P context |

**MILESTONE, minor — METR fit drift.** Endpoints/as-of agree; window choices lack justification. Hardware projects October ~335 minutes from a fitted intercept; software ~530 from the endpoint. Hardware/health medians are unaffected. Fix: versioned fit/anchor; justified exceptions.

Cost/price values agree. Balance/Ceiling share removals; differing all-GHG/CO₂ anchors are explained.

## Elicited-parameter inventory

Percentages are **judgments, not measured failure frequencies**. Basis means motivation, not calibration. Lags: central years.

| Milestone | Failure/branch; lag | Basis | P2100 / median |
|---|---|---|---|
| Kernel | 5%; review .5 | merge-window practice | .95 / 2028 |
| Nature | 8%; review .75 | unsourced typical review | .92 / 2029 |
| Solopreneur | 7%; ramp/disclosure .75 | OpenView, solo-firm examples | .93 / 2028 |
| Robotaxi | 7%; publication .4 | Cruise; uncalibrated lag | .93 / 2028 |
| Wozniak | 3%; demo .3; LEAP 25% | safety/publications/survey | .97 / 2028 |
| Fukushima | 5%; venues .7/.4 | competitions; unsourced weights | .95 / 2028 |
| Blue Collar | 8%; disclosure .75 + run .12 | missing logs; literal run floor | .92 / 2028 |
| Dark Line | 12%; integration 1 | automation/collisions, not durations | .88 / 2030 |
| Deluge | 12% plateau | historical launch plateau | .87 / 2035 |
| Homestead | US/China abandonment 30/25%; common 10%; base 9 + operation 1 | cancellations, space-station timelines | .87 / 2041 |
| Export | pharma success 50%; common failure 7%; materials hazard 6%/year; start .8 + programme 4 | reformulations, ~40-year materials history | .92 / 2033 |
| First Watt | failure 7%; paths 50/35/8% | programme schedules, fission analogy | .93 / 2034 |
| Grid Parity | additional nonlearning 20%; no extra lag | fission-cost analogy | .72 / 2061 |
| Cancer | 15%; follow-up 10 + publication 2 | literal endpoint; publication assumed | .697 / 2077 |
| Screening | 12%; no extra lag | generic screening diffusion, no fitted rollout | .824 / 2061 |
| Mind | accelerated regime 40%, starts 2035–50 | prevention narrative, not measured frequency | .306 / null |
| Middle Age | 25%; development 8 + validation 6 | clinical analogy, four-year BP trial | .749 / 2042 |
| Bend | 5%; ≥3 declines, ≥1% decline, reporting 1 | false plateaus; threshold heuristic | .95 / 2036 |
| Balance | 15%; no extra lag | permanence/non-CO₂ narrative | .23 / null |
| Ceiling | 15%; no extra lag | deployment/non-CO₂ narrative | .12 / null |

**RUBRIC-WIDE, MAJOR — incomparable priors.** Dark Line's 12%, First Watt's 7%, Cancer's 15% lack shared calibration. Narratives alone cannot justify relative magnitudes. Fix: require event definition, reference-class denominator or explicit elicitation, shared-risk treatment, sensitivity. Removing Grid Parity's nonlearning branch shifts 2061→2055.

**RUBRIC-WIDE, MAJOR — inconsistent evidence bar.** Software excludes unmeasured transfer penalties from medians; health uses elicited rates; hardware adds uncalibrated disclosure/integration durations. Naming barriers does not measure duration. Fix: distinguish literal floors, measured lags and elicited priors; require zero-lag/alternative-prior sensitivities.

**RUBRIC-WIDE, minor — discounts.** Hardware/Export/climate generally use 1.5–3×; climate discounts today's remaining duration, fusion the 2025 programme state (median 2×). Homestead's US 1.8×/China 1.15× reliability distinction lacks dated comparisons. Middle Age discounts only trial initiation; independent LEAP is not discounted. Others lack applicable dates. Fix: standardize discount clocks; source programme-specific deviations.

## Probability sanity

All 20 pass quantile ordering, 2100 ceiling and probability/null checks. Robotics generally exceeds distant health/climate probabilities; <50% correctly means null median. First Watt .93 versus Dark Line .88 is not contradictory: failure mechanisms differ. Calibration, not probability/median ordering, needs repair.
