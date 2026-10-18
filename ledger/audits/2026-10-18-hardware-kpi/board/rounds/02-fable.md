# Round 2 — fable

## Mapping result (02-fable-mapping.csv)
Gate: humanoid/mobile-manipulator (or VLA-driven generalist arms, flagged), named customer's
production flow, ≥1 ledger event verified/corrected. **Admitted 8/24**: C001, C005 (C010 dup),
C007, C032 (ended), C086, C087, C096, C097. 16 rejected — 13 for *no ledger event / no named
customer*, only 4 for *not GP* (C016/17/18/91). The census is as complete as the ledger, no more.

Instances (rx_tasks.csv): C001→51-9061_12491/0; C032→53-7063_14587/0; C086→53-7063_14587/2;
C087 and C097→53-7062_10781/4 (same instance); C096→43-5053_8214/3. **Strict count = 5
distinct instances.** C005 (connector mating is one step of the "box build" instance
51-2022_10019/0) and C007 (fold+stack is part of 51-6011_12119/0, laundry-plant wording) are
*slices*: **inclusive count = 7**. Share: strict 0.138%, inclusive 0.151% — but 0.122 pp of
that is the single instance 10781/4 (plant WIP/bin moves, 3M laborers). The share is one mapping
choice away from 0.02%; the count is not. Count headline, share only as a flagged label figure.

Two boundary classes surfaced: (1) slice vs whole instance; (2) setting wording (USPS P&DC vs
China Post). One sentence each, not a rulebook. argon's own audit (90% of share from one code)
agrees.

## Answers
**fable-1 / PPS "345×" (argon).** Not a bug. sample.py draws with replacement, p ∝ w; v5 averages
draws × stratum share = Hansen–Hurwitz, unbiased. The 345× is the inverse-probability weight every
PPS design has; its cost is variance from rare positives, which RESULTS.md already names (→150
tasks). astra's chain-linking point is right for per-task values; it holds the *level* only. fable-1
stays a research note, not the KPI.

**fable-2 (astra, argon).** Conceded. argon's examples are E0 instances (wouldn't score), but 0-synthesis
has E1+ ones where the tier comes from a co-cited non-GP robot. Dead as KPI.

**fable-3 (astra, argon).** Conceded on the baseline: L209–210 show a maintenance team,
collisions, unquantified interventions; 60 h is a livestream schedule. With "zero disclosed
interventions" the record is 24 h (Dyna lab, 2025-04) and the customer-site value is *none* —
i.e. the series depends on the disclosure vendors don't make. Also conceded: endurance ≠ METR
horizon; 240 shift-h and 168 continuous h aren't one axis. Demoted to a label record (= argon-2.1).

**fable-4.** Patches accepted in place: ledger-verified gate (drops C004/C091/C021 from my
examples); count headline (64× employment cliff); "pack station" instance was wrong — GXO is
53-7063_14587/2. BMW ended → cumulative vs active is an owner choice (my default: cumulative
ratchet, label lists ended runs). C007 stationary → owner crux (software-redeployable arms vs
"humanoids, mobile manipulators" verbatim).

**astra-2 vs fable-4 crux.** Factual part: the count does **not** measure labor taken over —
depth (hours, units) is unobserved; one site = one tick. I concede the words "taken over".
Preference part: can a verified footprint be the KPI? RUBRIC scores *trend*, never level; the
trend of "distinct kinds of real work a GP robot has verifiably done in production" is the
diffusion signal the section needs; astra-2's wording ("work-share: not yet measurable") sits
on top. astra's alternative leaves `kpi-assessment.csv` empty while
this count already exists in the ledger (argon's RUBRIC §3 point, still unanswered by astra).

## Pressed
- **astra**: the "at ceiling" objection to astra-3 (106% today, pace-scored → "stalled" from Q1)
  is unanswered; astra-1's reviewer-day/quarter is the owner's day.
- **argon**: argon-4's numerator — your own audit says "$15M industrial was an unverified
  assumption"; is argon-4 withdrawn? argon-5: endpoints (astra's "neither bounds") and the
  110-vs-177 midpoint arithmetic.
- **Both**: disagreement on *gate* and *slice*, not the literal step, is where fable-4's
  reliability lives.

## Position
- **Champion: fable-4** (strict literal, instance-level, count headline, cumulative, GP-gated,
  ledger-verified). Today **5** (7 inclusive). Drop-condition: after aligning gates, the three
  seats' tables disagree on the instance for >2 of the 8 admitted entries → switch to astra-2
  wording + argon-2 records, reason "literal mapping not reproducible across raters".
- **Co-picks:** argon-2 records (zero-intervention fix) in the label; astra-2 wording in the label.
- **Dead:** fable-2 (contamination, conceded); fable-3 as scored KPI (conceded); argon-3
  task-level; argon-4; argon-5 as scored series; astra-3 (ceiling, cooperation); astra-4 as KPI.
- **Cruxes:** slice rule (5 vs 7); stationary generalists (C007); cumulative vs active (C032);
  does Xinhua/vendor-livestream witnessing satisfy "verified"; share fragility (0.122 pp on one
  instance) — report it or not.
