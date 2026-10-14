# Round-2 cross-section ETA audit

Checked round-1 report, v5 rubric, 20 records, six notes, `drivers`, latest-v4 comparisons. **0 MAJOR findings.** Round-1 majors substantially repaired: mappings/lags and reasoned scenarios have sensitivities; calibration remains weak.

## Shared drivers

- **METR:** software/hardware share 2024-10-14+ fits, April 7 2026 observed anchors (M50/M80 1,044.78/185.91 minutes), doubling 3.45/4.09 months; long-run 5.97/6.36. Hardware drops its 4.43-month/fitted-intercept variant. Health retains 2023+ M50, 4.10 months, explicitly contrasting software; context-only, no clinical mapping. Hardware uses METR only as sensitivity.
- **IRENA:** fusion/climate agree: 2020/22/24 PV 55/51/43, onshore 39/33/34, offshore 89/81/79 $/MWh. Fusion transfers six-point 2010–24 offshore decline .076107/year after First Watt, arguing life-stage matching; recent .029797 remains sensitivity. Climate uses context only, no emissions mapping.
- **Wholesale:** identical EU/US 95/50 (2025), 105/52 (H1 2026); context-only.
- **Dyna:** four humanoid forecasts share June 2025→August 2026 failures 25%→7%; fraction halving 7.62 months, odds 6.52 (corrected). Explicit milestone anchors: deployment June 2026, navigation April, coffee 2026.7. Assumed transfer has slower/faster alternatives, shared draws.
- Climate harmonises curvature, TRACE anchoring, removals and stalls.

## Assumptions and failure scenarios

Weights are **judgments**, not frequencies; P=achievement probability; delays in years.

| Target | Named failure/branch; core assumptions | Basis; sensitivity example | P |
|---|---|---|---|
| Kernel | halt 2%, plateau 2%; transfer ×2, review .5 | technology persistence/kernel cycles; zero review −.66y | .96 |
| Nature | halt 2%, plateau 3%, novelty 4%, venue .5%; review .75 | AI novelty/journal longevity; doubled failures P=.822 | .91 |
| Solopreneur | halt 2%, plateau 1%, unverifiable 2%, duties 1%; ramp 1 | disclosure/delegability; ramp 3 → +1.77y | .94 |
| Robotaxi | regulation/economics/unreported 2/2/1%; lag .4 | Cruise/multiple markets; failure 2–15% → P=.98–.85 | .95 |
| Wozniak | shared stall 2%, home exclusion 1%; LEAP 25% | liability/evaluation campaigns; LEAP 0–50% → 2027.68–2028.98 | .97 |
| Fukushima | shared stall 2%, no qualifying venue 3% | competitions; own failure 10% → P=.88 | .95 |
| Blue Collar | shared stall 2%, unverifiable logs 3%; disclosure .75 | missing deployment logs; own failure 10% → P=.88 | .95 |
| Dark Line | stall 2%, uneconomic showcase 8%, disclosure 2%; setup .4 | purpose-built alternatives; own failure 5–25% → P=.93–.73 | .88 |
| Deluge | demand/cap/access 8/3/1% | historic plateau/debris; total 5–25% → P=.943–.744 | .87 |
| Homestead | abandonment US/China 30/25%; habitation/cost/access 4/3/1%; base 7.5 | cancelled programmes/stations; base 3–12 → 2034–2042 | .89 |
| Export | pharma success 50%; economics/access failure 5/2%; materials hazard 5%/yr | reformulations/materials history; hazard 1.25% → P=.749 | .92 |
| First Watt | physics/funding 3/4%; fast path 40% | energy analogues; fast 25–55% → 2037–2031 | .93 |
| Grid Parity | fission-like nonlearning 20%; FOAK $170 | one of five generator classes; nonlearning 10–35% → P=.84–.61 | .75 |
| Cancer | plateau 10%; 5→10-year survival mapping | stalled cancer sites; plateau 5–20% → P=.915–.831 | .886 |
| Screening | ceiling .15%, slow diffusion 6.2%; assumed baseline/rates | screening retrenchment; rates ×.5 → P=.597 | .937 |
| Mind | stall 15%, prevention regime 40%; age-rate transfer | demographic/prevention reasoning; transfer ×.75 → P=.474 | .683 |
| Middle Age | surrogate/safety 15/12%; development 8, validation 6 | surrogate failures/oncogenicity; safety 5–25% → P=.804–.635 | .747 |
| Bend | decarbonisation stall 5%; recognition 3 years/1% | false plateaus; stall 2–10% → P=.979–.899 | .95 |
| Balance | shared stall 5%, removal stall 10%; residual floors | CCS history; removal stall 5–25% → P=.096–.076 | .09 |
| Ceiling | same stalls; carbon-budget mapping | CCS/IPCC; removal stall 5–25% → P=.041–.033 | .04 |

Disclosure risks cluster at 1–3%; shared risks match. Dark Line’s showcase-economics risk explains lower P than First Watt; clinical surrogate/safety risks differ. No unjustified disparity found.

**RUBRIC-WIDE, minor:** incomplete sensitivities: software groups failures; fusion omits schedule/FOAK-spread and successor-timing low/high effects. Inputs are disclosed.

## Rule 7: every threshold move

Every move is attributed in `change_note`; “—”=none.

| Target | v4→v5 moves | Attributed cause |
|---|---|---|
| Kernel | p10 2027→2028; p50 2028→2029 | transfer |
| Nature | p90 2033→2035 | failures/transfer |
| Solopreneur | p50 2028→2029; p90 2031→2032 | transfer/ramp |
| Robotaxi | p90 2033→2031 | reading/scenarios |
| Wozniak | — | — |
| Fukushima | p50 2028→2027; p90 2031→2030 | attempts/odds/manual-tail fix |
| Blue Collar | p50 2028→2027; p90 2032→2030 | components/scenarios |
| Dark Line | p10 2028→2029; p50 2030→2031 | explicit faults/attempts |
| Deluge | — | — |
| Homestead | p10 2037→2035; p50 2041→2038 | interval/clock/encoding |
| Export | p10 2029→2028; p90 2073→2080 | encoding/hazard |
| First Watt | p50 2034→2035; p90 2062→2061 | weight/clock/MC |
| Grid Parity | p10 2040→2034; p50 2061→2047 | analogue window |
| Cancer | p10 2051→2053; p50 2077→2068; P .697→.886 | rate/plateau/lag |
| Screening | p50 2061→2058; p90 null→2091; P .824→.937 | duplicate failure removed |
| Mind | p10 2075→2053; p50 null→2080; P .306→.683 | prevalence/fade/stall |
| Middle Age | — | — |
| Bend | p90 2047→2050 | components/width/encoding |
| Balance | p10 2090→null; P .23→.09 | components/residual consistency |
| Ceiling | p10 2095→null; P .12→.04 | components/budget |

**MILESTONE, minor — First Watt:** .50→.40 re-elicitation looks judgment-driven despite attribution; p90 includes MC noise, not new evidence.

**RUBRIC-WIDE, minor — encoding:** fusion/health round; others floor. Standardise to prevent artificial rule-7 moves.

## Probability sanity

All 20 pass ordering, ≤2100 and probability/null checks. Parity follows First Watt; Blue Collar precedes Dark Line; Balance follows CO₂ net zero. Low climate/high screening P reflect model assumptions, not contradictory probabilities.
