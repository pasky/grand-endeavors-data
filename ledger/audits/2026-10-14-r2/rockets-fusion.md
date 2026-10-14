# Round-2 ETA audit: rockets and fusion

**Result: 1 MAJOR finding.** Reviewed rubric v5, round-1 README/fusion-rockets/cross-section reports, latest assessments and their v4 predecessors, and both generations of working notes. Current runs: rockets `20261014T153125Z`; fusion `20261014T154252Z`.

## MILESTONE — MAJOR: First Watt’s changed prior is not a demonstrated correction

The clock correction is justified, but changing the fast-path weight **.50→.40** is renewed elicitation on unchanged evidence. Round 1 identified .50 as the biggest assumption; it did not find it numerically erroneous. The cross-section findings require explicit elicitation, scenarios and sensitivities, not a different successful-path weight. The v4 notes already identify .50 as judgment rather than measurement.

The new .5×.8 decomposition explains the new choice but does not establish an error in the old one. In particular, the suggested old .6×.85 factorisation and unsupported rounding were not in the previous working. Thus the change_note’s attribution to fixing the old prior is insufficient under rule 7, notwithstanding excellent disclosure and sensitivities. This is a stability finding, **not** an objection to using an assumed probability. On identical draws, retaining .50 with the corrected clock gives p50 **2032.18**; changing it produces **2035.21**. Retain the prior or identify a substantive reason it fails. Grid Parity inherits these altered draws.

## MILESTONE — remaining checks

- **Deluge: pass.** All stored quantiles and P2100 remain unchanged. The withdrawn launch-count citation is removed; failure scenarios, transition-stall sensitivity and unit boundaries address round 1. Series values **797.4/2625.9/3194.0 tonnes** for 2021/24/25 reproduce log slope **.369541**, annual growth **44.7%**, and deterministic crossing in 2035. Model output reproduces **.873; 2033/2035/null**. The measured slope is a genuine series fit, not an assumed transfer.
- **Export: pass, with definition pending.** Corrected `varda-five-missions-rv` supports a handful of missions, not five successful returns; the latter is no longer used. W-1’s **February 2024** return and **>12 km ZBLAN** agree with effective records. Hazard **6→5%**, the anchored trial clock, earlier hazard start and calendar encoding explain **p10 2029→2028**, unchanged p50 2033, and **p90 2073→2080**. Reproduction gives **.919; 2028/2033/2080**. Keeping the prior programme duration/probability rather than another unsupported re-elicitation is an explicit, reasonable response to that round-1 criticism.
- **Homestead: pass.** Restoring the **9→7.5-year** interval and **.10→.08** common risk directly addresses the audited unjustified changes; clock and encoding corrections complete the attribution of **2037/2041→2035/2038**. Full closure is no longer required, and LEO mass no longer establishes surface-logistics sufficiency. MOXIE **12 g/h**, Lunar Palace **four crew/year**, and SpaceX’s **September 2028/up-to-12-refuellings** claim match effective evidence. Output reproduces **.886; 2035/2038/null**.
- **Grid Parity: pass apart from inherited First Watt issue.** The **2061→2047**, **2040→2034** moves explicitly reverse the audited analogue-rate substitution. Offshore **208/89/79** in 2010/20/24 and the full fit **.076107/year** check; **ln(1.7)/r=6.97 years**. Lindley supports **>$150**, while $170 is explicitly assumed. The mapping is also assumed, with recent-rate sensitivity restoring 2061. CFS aspirations supply no invented parity date. Output reproduces **.748; 2034/2047/null**.

First Watt’s **8.6/2.08 MJ=4.13 target gain**, July **22** earthworks date and early-2030s ARC target check. Its **.9305; 2029/2035/2061** output reproduces; the p90 move is attributed to clock/Monte-Carlo rounding, not setbacks.

## RUBRIC-WIDE — minor

Registers exist, but low/high sensitivity coverage is incomplete: fusion schedule/cost spreads and successor timing; rockets level noise and Homestead’s fallback-programme parameters. Homestead’s landing claims should be labelled sourced projections rather than measured claims; no assumed numerical value was found hidden as measured. Rockets uses floor-year encoding, fusion nearest-year rounding: standardise this convention.

All five evidence lists and calc citations use effective records. Shared fits/draws are consistent. Embedded model/attribution scripts reproduce under a 1-GiB memory cap.

## DEFINITION — owner decisions, not MAJOR

Deluge: ton units/tanker propellant. Export: paid trial materials and historical microspheres. Homestead: continuous versus intermittent occupation/local-resource scope. First Watt: sustained-operation duration. Grid Parity: dollar vintage and fixed-$100 versus gas comparator.
