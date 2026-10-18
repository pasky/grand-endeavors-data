# Context for the Robots/Hardware KPI board (written 2026-10-17 by the convener)

All paths are absolute and in the main checkout; your worktree does NOT contain the research or
prototype files (they are uncommitted scratch under `.pi/scratch/`, gitignored, and the data repo
is a separate repo). Read them from these paths.

ROOT = /home/pasky/projects/hai/grand-endeavors-agent-worktree-0002
SCR  = ROOT/.pi/scratch/hw-kpi

## The project
- "Five Grand Endeavors" (ROOT/README.md, ROOT/DESIGN.md): an AI-run pipeline producing a
  trustworthy periodic report to "the Board of Humanity" on Robots, Rockets, Fusion, Health,
  Climate. ROOT/framework.yaml defines each section's KPI, milestones and challenges.
- A KPI is ONE numeric series with history from a trustworthy recurring source; its status is
  judged as pace vs a benchmark/own trend (ROOT/gather/RUBRIC.md §3, "KPI rules"). Registered in
  ROOT/data/metrics/kpi-assessment.csv (one row per section; robots-hardware has none today).
  Other sections: robots-software = METR 80% time horizon (capability frontier, third-party);
  rockets = best $/kg to LEO; fusion = world household electricity price (an outcome the
  frontier doesn't move yet); health = median-country HALE (WHO); climate = CO2 ppm trend (NOAA).
- News events are collected into a verified ledger (ROOT/data/ledger/events/robots-hardware.jsonl,
  231 events, schema in ROOT/DESIGN.md). Milestones for this section (framework.yaml): Robotaxi
  Saturation, Wozniak coffee test, Fukushima test, Blue Collar Shift, Dark Line.
- Pipeline agents are `pi` LLM agents (ROOT/core/lib.sh pi_run); LLM calls are cheap-ish but not
  free; the owner runs it himself.

## The section's goal and the owner's preferences (verbatim-ish)
- The point is GENERAL-PURPOSE AUTONOMOUS physical automation: robots that software alone could
  redeploy to other jobs (humanoids, mobile manipulators), with autonomy verified (no teleop).
- Current KPI "Largest Active Commercial Fleet of General-Purpose Humanoids (Single Site)" failed:
  no disclosures, contracted != active, PR-driven; no data ever collected.
- Rejected by owner: IFR industrial robot stock/density ("general purpose autonomous automation
  is the whole point so [IFR] can't be it"); a plain FTE-equivalent count ("isn't actually
  checking autonomy").
- Owner likes the outcome angle "how much human labor has been taken over by robots".
- Owner liked a "bracket" for deployment: lower bound = disclosed autonomous productive robot-hours
  (e.g. Agility Digit 65,000 h cumulative), upper bound = shipments x productive-use share.
- On the prototype: "19/30 is not great .. make it good, without any weird arbitrary rules that
  would break over time"; latest: "this still feels arbitrary and half-baked, figure out efficient
  way (trustworthy and reliable and ~cheap-ish and fast, in the order of priority) ... as simple
  as possible".

## Research done (web, Oct 2026) — read SCR/0-synthesis.md first
- SCR/1-others-ideas.md, 2-unit-data.md, 3-deployments.md, 4-economics.md, 5-autonomy.md,
  6-deployment-sources.md, 7-deployment-constructions.md (research subagent reports; some errors
  noted in 0-synthesis.md).
- Key facts (spot-checked by convener): no public recurring series of autonomous GP robot work
  exists. Humanoid shipments 2025: ~13k (Omdia) to >18k (IDC); IDC: >85% of 2025 deployments in
  performances/education/data collection/guided tours (method unpublished, paywalled
  CHC53325326). Unitree (STAR-listed Aug 2026) Jan-Sep 2025 humanoid revenue 73.6% research/
  education, 17.4% demos/display, 9.01% industrial — from a one-off IPO inquiry response, not a
  recurring disclosure. Deployments rarely disclose robots x hours x throughput or interventions.
- Epoch AI "Where autonomy works" (Feb 2026): 14 fixed tasks x 5 maturity stages, autonomy
  required; one-off, no stated cadence.
- Anthropic "What work can robots do?" (30 Sep 2026) + CC BY 4.0 data
  (huggingface Anthropic/EconomicIndex robot_exposure; local copy SCR/proto/rx_tasks.csv):
  7,594 physical O*NET tasks, each split into weighted "instances", rated E0-E3 (E1 purpose-built
  robot setting, E2 structured human workplace, E3 unstructured) by Claude with web search; every
  cited source has system, developer, date, maturity (deployed/commercial/demo), autonomy_status.
  Any robot, any environment: 74-76% of physical work time; robots cost-competitive for 0.3%.
  "Periodic updates" hoped for, no committed cadence. Convener reproduced their headline with
  OEWS May 2024 employment weights (45% of work time physical; E0/E1/E2/E3 = 24/50/23/2%).
- LEAP Wave 7 (Apr 2026) expert forecasts: Coffee Test median 2034 (experts), 2032 (supers).

## Prototype history (all in SCR/proto/ and SCR/catalog/; summary SCR/proto/RESULTS.md)
Goal: KPI = share of US physical work time that GP robots can do autonomously, tiered
demo/pilot/deployed, on Anthropic's task set. Stratified PPS sample (SCR/proto/sample.py).
- v1 (binary "whole instance end-to-end", research-mode agents with web search, 137 tasks):
  ~0; INVALID — tool logs showed raters skipped searching.
- v2: raters ran the mandatory searches with output to /dev/null; INVALID.
- v3 (partial credit = time share of sub-steps covered; 3 tasks per agent; audited real search):
  ~0.55%; two raters on 15 tasks: every non-zero rating contradicted (raters found different
  robots, judged transfer differently).
- v4: a capability CATALOGUE (SCR/catalog/catalog_v1.json, 98 entries: what GP robots have done
  autonomously, built by agents from the ledger + Anthropic's GP sources; curators did ~1 search
  each) + mapping-only raters with transfer rules T1-T5 (SCR/proto/RATER3.md). 30 tasks x 2 raters:
  2.8% vs 3.9%; zero/non-zero agreement 19/30, Pearson 0.53; raters broke rules (lab demos credited
  for workplaces); enforcing "evidence transfers only to easier environments" mechanically: 1.3% vs
  1.8%, 19/30, r=0.59. Owner: "19/30 is not great", "no weird arbitrary rules".
- v5 (SCR/proto/v5.py): fixed per-task sub-step decomposition (1 LLM call/task), 2 high-recall
  shortlists per task (union) -> 2,861 (sub-step, catalogue entry) pairs, filtered by
  env-downhill; each task's pairs judged in ONE batched call by 6 independent samples of the same
  model (gpt-6-luna), plain-language criterion (= definition). Pair agreement 2,855/2,861; task
  zero/non-zero 29/30, r=0.97; level ~0.2% (0.09-0.33% across 3-vs-3 splits). Only 17 pairs got
  any yes.
- v5b (SCR/proto/v5b.py): those 17 pairs re-judged one pair per call, 7 samples x 2 models:
  batching biased judgments (5/6 batched vs 1/7 single); Opus near-deterministic, Luna noisy on
  borderline; models disagree SYSTEMATICALLY on transfer calls (Galbot S1 "carries heavy bins
  between stations" covering "carry tote to a machine feed hopper": Opus 7/7 yes, Luna ~1/7).
  Level: Luna 0.11%, Opus 0.32%, mean 0.19% of US physical work.
- Convener's open worries: the level hinges on ~a dozen borderline transfer judgments; catalogue
  completeness depends on agent curation; sampling error from few positive tasks (30-task sample,
  ~150 needed); the decomposition and catalogue are themselves LLM artifacts; model drift.

## What the board should weigh
Priorities: trustworthy > reliable > cheap-ish > fast; as simple as possible; no arbitrary rules
that break over time. Options may keep, simplify, or abandon the coverage approach (e.g. adopt an
external series as-is, rate a small fixed benchmark like Epoch's tasks, a milestone-ladder index,
the deployment bracket as the KPI, Anthropic's own index restricted to GP sources, human expert
spot checks, a different KPI entirely). Be concrete about what number would appear on the
dashboard today and how next quarter's number would be produced.
