# Round 1 — fable

## What I checked (LEDGER = events jsonl, CAT = catalog_v1, rx_tasks.csv × OEWS)

| Claim | Result |
|---|---|
| argon-3: Digit/GXO → `53-7062.00` "Move freight, stock…" | That ONE task = **1.22% of US physical work time** (time_share 0.526 × 2.98M employed). "0.28% across 18 tasks" cannot come from task_id-level crediting; Digit alone would step ≥1.2%. Its 6 Anthropic instances (pallet freight 25%, trailer unloading 20%, order fulfillment 15%, retail dock 20%, plant bins/WIP 10%, unstructured 10%) show literal matching is still an instance-level judgment ("is tote AMR→conveyor the fulfillment instance?") — far narrower than v5 transfer, not zero. |
| argon-3: 24 deployed/pilot entries | Correct (16+8). But C016/C017 (RB-KAIROS probe/car-wash), C018 (Dexie, pre-programmed), C092 (unnamed industrial hardware) fail the owner's GP definition — a GP gate must precede any census. |
| astra-3: DTF 106% vs 32% | `2026-08-27-dyna-din-tai-fung-shift-throughput`, *verified*: 1,590/day vs 1,500/18-h shift; launch ~480. Confirmed. |
| argon-2: "24 h Dyna Din Tai Fung" | Wrong site: 24-h run is a Dyna **lab** demo (`2025-04-29`, *corrected*); DTF runs 18-h shifts. |
| argon-2: Helix 2.5 56%; BMW 1 unit; Waymo 500k/wk | First two in LEDGER (`2026-09-17`, `2026-10-07`); Waymo not — latest 450k/wk Dec 2025, *legacy*. |
| argon-4: UBTECH 820.6M/590M, Unitree 9.01%, Agility $1.8M | Match 4-economics.md. But UBTECH publishes **no end-use split** (l.53: revenue does "not split autonomous work from R&D, demos, deployment, teleoperation, or training"); "30–50% disclosure" appears in no research file → "$28M verified industrial revenue" is an assumption. |
| argon-5: 17.5 FTE-yr | 65,000 h "over nearly three years" (`2026-09-15`, verified) → ~22k h/yr ≈ 11 FTE-yr; "operating hours" ≠ autonomous productive hours. Magnitude OK. |

## Ratings (upside / probability / cost, 1–10)

| Item | Up | P | Cost | Fatal flaw? |
|---|---|---|---|---|
| astra-1 human-adjudicated coverage | 6 | 3 | 7 | No — but Galbot-bins-vs-tote becomes one human's opinion, and that human is the owner ("a reviewer-day/quarter" is the scarce resource). |
| astra-2 not-measurable + 0/4 | 3 | 9 | 1 | None; a label, not a KPI. |
| astra-3 DTF sentinel | 4 | 3 | 4 | **At ceiling**: 106% today; pace-scored series with no headroom reads "stalled" from Q1. Needs customer-signed logs; outside the public-source pipeline. |
| astra-4 redeployment certificates | 5 | 2 | 5 | Today 0, gate the pipeline can't execute → `unknown` indefinitely. A milestone criterion, not a series. |
| argon-1 Opus+Luna panel | 5 | 4 | 4 | Same definitional flaw as fable-1 (its own "fail" says so). |
| argon-2 precursor records, null KPI | 6 | 8 | 1 | None fatal; one misattribution. fable-3 ×4. |
| argon-3 task-level footprint | 7 | 3 | 2 | **As written, yes**: 1.22% step from one deployment; the 0.3 default parity discount is an arbitrary rule that breaks. Fixable → fable-4. |
| argon-4 revenue ÷ wage | 4 | 2 | 2 | Owner-rejected class (FTE without autonomy); UBTECH units include Zeekr "practical training" (`2025-03-03`); the split it relies on doesn't exist. |
| argon-5 hours bracket | 5 | 4 | 2 | Lower bound = one vendor's cumulative PR number, no autonomy share; upper = three multiplied assumptions. OK as label, fatal as scored series (moves when Agility posts). |

**Same item?** argon-3 and fable-4 are one idea, different units. Task-level is dead (1.22%); the discount violates the brief. Merge: **fable-4/argon-3**: instance-level literal census, count as headline, instance-weighted share in label, no discount.

## Position
- **Champion: fable-4/argon-3 (merged).** Drop-condition: 2-rater literal mapping of the 24 entries disagrees on >25%, or the GP-gated first run yields <8 instances.
- **Co-picks:** argon-2/fable-3 record series in the label (continuous-run, single-site fleet — one ledger event each); astra-2's wording "work-share: not yet measurable" in the label.
- **Dead:** argon-4; astra-3; argon-3 task-level; argon-5 as scored series; astra-4 as KPI.
- **Cruxes:** (1) Does state-media/vendor-livestream witnessing count as verified? (Longcheer, CATL, China Post: half the census.) (2) Cumulative ratchet vs "active in last 12 months" (Figure/BMW ended). (3) Are Anthropic's instance weights acceptable as the last LLM artifact in the label?
