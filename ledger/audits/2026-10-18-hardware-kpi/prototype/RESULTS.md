# GP robot coverage prototype — results (2026-10-17)

Design: Anthropic robot-exposure task set (7,594 physical O*NET tasks with instance splits),
weights time_share x OEWS May 2024 employment. Strata: A = tasks whose Anthropic sources include a
GP-looking robot (20.2% of physical work time), B = other E1+ tasks (61.2%), C = E0 tasks (18.6%).
PPS samples (sample.py, seed 20261017). Raters: research-mode subagents, RATER.md (v1, binary
end-to-end per instance) and RATER2.md (v2/v3, partial credit = share of the instance's time in
sub-steps a GP robot has demonstrably done autonomously).

## Runs
- v1: 137 tasks / 768 instances, batches of 8-9 tasks. 1 instance non-none. INVALID: tool logs show
  several raters made 0 web calls; others few.
- v2: 30 tasks x 3 raters, batches of 10. INVALID: raters ran the 3 required searches with output
  sent to /dev/null and never read them; one rater refused, saying it had not done the research.
- v3: same 30 tasks, batches of 3, explicit searching rules; 10 raters (r1) + 5 replicate raters
  (r2, 15 tasks). Tool logs: 10-14 search calls and 5-13 page visits per rater, no discarded output.

## v3 results
- Mean instance-weighted coverage (r1): stratum A 1.63%, stratum B 0.35% (C not sampled in v3; 0 in v1).
- Implied GP share of US physical work time: 0.202*1.63% + 0.612*0.35% ~= 0.55% (order of
  magnitude 0.1-1%; nearly all `demo` tier, 1 `pilot` (Digit at GXO), 0 `deployed`).
  Compare: any robot, any environment 76% (Anthropic, reproduced).
- Reliability: 15 double-rated tasks; 11 agree on zero/non-zero, but all 4 non-zero ratings are
  contradicted by the other rater (e.g. restaurant table clearing 0.325 vs 0: pi0 bussing demo vs
  Sunday Memo home clearing judged non-transferable; pack-station removal 0 vs 0.0625: Digit
  tote-to-conveyor transfer accepted vs rejected). Disagreement sources: (1) evidence discovery
  (raters find different robots), (2) transfer judgments.

## Lessons
1. Rater diligence must be mechanically audited (tool-log search/visit counts, no discarded output),
   and batches kept small (<=3 tasks).
2. Separate evidence discovery from mapping: a curated GP capability catalogue (verified autonomous
   GP robot capabilities with dates, maturity, sources: what our gather pipeline's events already
   are) as shared input; raters only map catalogue entries to task sub-steps.
3. Explicit transfer rules (object class x manipulation x setting type) with worked examples, plus
   two raters + adjudication (as in the assess review stage).
4. Partial credit is necessary: binary end-to-end coverage is ~0 and has no pace.
5. Sampling precision: with coverage concentrated in few tasks, a stable estimate needs a larger
   A-stratum sample (100+) or a census of tasks the catalogue can plausibly touch.

## v4: capability catalogue + mapping-only raters (2026-10-17)
Catalogue (../catalog/, CURATE.md): 6 research curators consolidated 124 current ledger robot events
+ 1,062 Anthropic GP-looking autonomous sources (grouped by URL) into 92 entries; a gap pass over 77
unreferenced ledger events added 6 entries and 8 links (63 skipped as non-capability) -> 98 entries
(74 demo / 8 pilot / 16 deployed; 39 humanoid, 38 mobile manipulator, 15 stationary generalist).
Caveat: curators did ~1 search each; coverage is what the ledger + Anthropic's citations contain.

Raters: RATER3.md (no web; sub-steps with time shares; transfer rules T1 activity, T2 object
class, T3 environment only downhill, T4 pace, T5 maturity only within domain), same 30 tasks, 2
independent raters each (20 agents, 3 tasks each). score_v4.py.
- As rated: implied GP share of US physical work r1 2.79%, r2 3.88%; per-task Pearson 0.53;
  zero/non-zero agreement 16/30.
- Raters broke T3 often (lab/E1 demos credited for restaurant/E2 work); enforcing T3 mechanically
  (entry env >= instance setting_tier from Anthropic data) dropped 33 sub-step citations:
  r1 1.27%, r2 1.83%; Pearson 0.59; agreement 19/30.
- Rater-average 1.55%, PPS bootstrap 90% CI 0.87-2.30% (30 tasks; sampling error dominates).
- vs v3 (independent web search per rater): 0.55%, every non-zero rating contradicted.
Remaining noise: T4 (pace) and T5 (domain) judgments, sub-step time shares. Next: label catalogue
entries and instances with domain + paced flags so T4/T5 are also mechanical; adjudication pass
for per-task disagreements; larger sample (~150 tasks) to bring sampling CI to about +/-0.3pp.

## v5: fixed decomposition + shared shortlist + atomic pair judgments (v5.py)
No agent tools; every LLM decision is one cached `pi -p --no-tools` call (gpt-6-luna:high), prompts
kept in v5/prompts/. Rules left: (1) the judging question is the definition itself (same kind of
action on the same kind of objects, whole sub-step, setting at least as demanding, well enough for
the job); (2) evidence transfers only to easier environments (mechanical, catalogue env vs
Anthropic setting_tier); (3) average independent judges. Dropped: pace thresholds, domain rule,
rounding grid, majority cutoffs.
- 30 tasks -> fixed sub-steps (1 call/task); 2 independent high-recall shortlists/task, union ->
  2,861 (sub-step, entry) pairs; 6 independent judges per task call.
- Pair agreement judge 0 vs judge 3: 2,855/2,861. Task level: zero/non-zero 29/30 (single judges),
  Pearson 0.97 (vs v4 19/30, 0.59). Rejections inspected: correct (e.g. table wiping does not cover
  carpet vacuuming; tote-to-conveyor does not cover inducting totes into storage pods). Positives:
  Digit/Galbot tote and bin carrying, China Post parcel sorting, Spot door/breaker tasks.
- Soft score (share of judges saying yes; max over candidates per sub-step): 6-judge estimate 0.21%
  of US physical work time; 3-vs-3 split-halves range 0.09-0.33% (one lenient judge); sampling
  error larger still (few positive tasks) -> needs a ~150-task panel.
- v4's 1.5% was inflated by lenient holistic mapping (lab demos credited for workplaces etc.).
Incremental property: a new catalogue entry only needs shortlist + judge calls against existing
sub-steps; the panel definition (sub-steps) is frozen per version.
