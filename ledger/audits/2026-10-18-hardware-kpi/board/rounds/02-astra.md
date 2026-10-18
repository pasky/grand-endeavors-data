# Astra — debate and independent test

## Answers on my items

**astra-1 — Fable/Argon:** Concede invented sub-step weights and human transfer judgments; adjudication improves accountability, not empirical validity. Owner time is expensive. But I proposed auditing positives/borderlines plus sampled negatives, **not 2,861 human judgments**: v5b has 17 any-yes pairs. Cost is a disadvantage, not a fatal violation of priorities that rank trust first.

**PPS check:** Argon’s multiplier objection is not, by itself, a weighting bug. With stratum weight W and draw probability pᵢ=wᵢ/W, the Hansen–Hurwitz estimate is **W·mean(y_draw)**; its expectation is Σwᵢyᵢ. Rare sampled tasks represent unsampled work, creating high variance. Multiplying each sampled score by its task weight again would bias it. Furthermore, current `v2_selection.json` contains **20 A + 10 B**, not 15 A: the cited task’s multiplier is approximately **258×**, not 345×. However, these are unique selected keys, not the first PPS draws; the subset-generation procedure is absent. Its sampling validity is therefore unresolved. My existing patch—recreate probability draws, retain multiplicities, sample E0—remains necessary before publication. I do not defend the prototype’s current uncertainty estimates.

**astra-2 — Argon:** RUBRIC §3 explicitly permits `unknown` without a registered series/window; it does not command inventing a proxy. Astra-2 openly relaxes the one-KPI charter requirement. That tradeoff needs owner approval, not a false assertion of rubric compliance. Existing deployment events do not automatically constitute a comparable series or pace benchmark.

**astra-3 — Fable/Argon:** 106% is not a mathematical ceiling: output/1,500 is uncapped. Concede the substantive objection: a customer may stop demanding improvement after sufficiency, so it is weak as an indefinite progress KPI. Private cooperation is an explicit experimental cost, not forbidden by DESIGN’s description of the current pipeline. Stationary arms can in principle be software-redeployable; their form alone neither proves nor refutes generality. This remains a conditional measurement experiment, not a ready public-source KPI.

**astra-4 — Both:** Concede no usable current pace series and no secured reporting partners. “Unobtainable” is unproven, but I will not champion a registry’s empty count as capability progress. Dead as a presently deployable KPI.

## Attempt to falsify fable-4

Independent table: `02-astra-mapping.csv`. I deliberately use a **permissive admission gate** to isolate mapping: ledger-linked named customer production, plausible software-redeployable generalist hardware, and provisional catalogue/source-reported autonomy; no intervention-free-log requirement. Historical BMW and stationary Dyna are included. This admits **8 entries**; autonomy remains claimed rather than independently audited.

Searching task statements and inspecting candidate instance descriptions yields **3 distinct whole-instance matches**: C001 → **20304/1, 20305/3**; C032 → **13946/1**. The two C001 matches overlap in actual workstation activity. Six admitted entries have no whole-instance match found.

Concrete decisive counterexamples: **10781/4** includes storage-to-line **and** finished-goods-to-dock transport using carts/tuggers/forklifts; Galbot only carries bins between stations. **12119/0** includes mixed-item sorting/counting in industrial laundry; restaurant napkin folding is narrower. **14587/2** explicitly varies boxes and stack patterns; Digit’s evidence is standardized totes. Crediting these requires interpreting some clauses as illustrative rather than required. That is precisely the judgment “literal mapping” purported to remove. Fable’s <8-instance drop-condition triggers in my run; chair comparison will test disagreement separately.

## Crux and remaining challenges

**Fable:** I accept a clearly labelled documented footprint as a possible headline; whether it is valuable enough is **owner preference**, not a factual ban. Whether instances are consistently countable and autonomy established are factual/methodological questions. Today’s test undermines the former. Dyna’s 24-hour demo site is **unspecified**, not established as a lab.

**Argon:** Revenue/wages still measures the wrong thing; assumed endpoints still are not bounds. **Fable:** Scheduled 60 hours still cannot establish intervention-free endurance. These objections need concessions or genuinely different constructions, not relabelling.

## Position

**Champion: astra-2**, unchanged; drop for a reproducible, auditable series or successful bounded measurement pilot. **Co-pick:** astra-3 as optional data acquisition. **Dead as specified:** fable-2, argon-3/4/5, fable-3’s baseline, astra-4 as current KPI. **Fable-4:** withdraw my KPI co-pick pending reconciliation of the mapping test; retain deployments as ordinary evidence. **Open:** whole-instance versus partial-example semantics; autonomy admission; subset sampling provenance; owner preference for a documentation index.
