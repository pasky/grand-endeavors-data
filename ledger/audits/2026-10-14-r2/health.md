# Health round-2 ETA audit — 2026-10-14

Compared run `20261014T155116Z` with v4 run `20261013T135523Z`, their notes, rubric v5, framework wording and round-1 health/cross-section findings. **3 MAJOR findings.**

## Verification

Reran both embedded scripts and attribution chains in memory under a 512 MiB limit. All reported distributions, sensitivities and arithmetic reproduce. Unconditional quantiles/nulls are consistent. There are 77 effective health events; all latest evidence citations and event references in the notes are effective. Spot-checks confirm PATHFINDER’s >7×/53.5%/73.7%, NHS trial 140,000, ACS 69%/13%/86%, ADAMS 24.19%/37.36% (2002), Fitzgerald’s between-group 3.23 years and Buck’s 2.61 years. Registered health series remain HALE, not milestone outcomes.

## Findings

**MILESTONE — MAJOR 1: taming-cancer, unlabelled endpoint-rate mapping.** The sourced 1.69% rate measures decline in **five-year** relative non-survival. `Can.run()` applies it directly to **ten-year** non-survival. The register labels the rate sourced and discusses national transfer, but never labels or tests this endpoint transfer. The assumed q=.85–.95 converts the initial level, not the subsequent rate. Keeping q constant across future cohorts instead gives `T=2017+ln[q(1−S5)/(q−.8)]/r+12.9`. With otherwise identical draws/plateau treatment, this alternative yields **P=.5636, p50=2094.29**, versus .8861/2068.41. Neither mapping is mandated; the latter cannot masquerade as a sourced ten-year trend. Round-1 rate calibration is therefore only partly fixed.

**MILESTONE — MAJOR 2: taming-cancer, lag provenance and false rubric attribution.** The change note attributes 2→2.9 years to a supposed v5 requirement that durations be measured. V5 explicitly permits assumed core durations. The 2.9-year value combines a single-cohort five-year reporting interval with a pooled-cohort midpoint calculation; applying it to future ten-year publication is an assumed transfer, not a measured structural floor. Relabel and justify that transfer rather than calling the previous assumption an error. This step adds 0.9 years to every finite draw, including rounded p10 2052→2053. The zero-lag sensitivity is useful but does not fix the false attribution.

**MILESTONE — MAJOR 3: unbroken-mind, assumed baseline distribution labelled measured.** The P0 register labels `U(.2419,.28)` measured ADAMS plus sourced WHO weights. ADAMS measures two broad age-band estimates, not this uniform distribution or its .28 upper limit. WHO weights also cannot resolve the unobserved within-band age pattern. The narrative acknowledges broad-band uncertainty, but the input classification still presents a judgmental distribution as measured and provides no baseline sensitivity. Retain the measured points; label/test the standardisation approximation and uncertainty prior as assumed.

**RUBRIC-WIDE — minor: incomplete input registers.** All four have tables and substantial sensitivity work, but not every parameter is registered/tested: screening’s Dirichlet concentration and class-specific rate spread; cancer’s plateau-year range; mind’s additional-regime rate/start range; middle-age’s stage-A minimum and stage-B spread. Disclosed assumptions themselves are not MAJOR findings.

## Disposition and provenance

**Precise-screening — pass:** round-1 generic failure mass is removed, baseline/rates remain explicitly assumed, and CVD sensitivity is prominent. Removing 12% reproduces every material move: p50 2061→2058, P .824→.937, p90 null→2091.

**The-long-middle-age — pass:** prior model retained; named failure scenarios, stage-A sensitivities and assumed trial floor address round 1. No material ETA/probability move.

**Unbroken-mind — mapping passes, baseline issue above:** −2.3%/yr is **not in the ledger**. Newly fetched RAND/Hudomiet data give ln(12.2/8.5)/16=.022586 for 65+; I verified the cited page. Transfer to 80+ is explicitly assumed, first crux, with ×.75 yielding P=.474/p50 null: acceptable under v5, not measured validation. The complete move is attributed and reproduces. Cancer’s sourced SEER table also checks out, but 2019–2023 survival values are modelled, not observed. These are newly sourced inputs, not new ledger events.

**DEFINITION — owner decision, not MAJOR:** cancer relative versus observed survival and independent metastatic-control requirement; dementia CDR≥1 versus consensus-dementia alignment. Alternative readings and sensitivities are supplied.
