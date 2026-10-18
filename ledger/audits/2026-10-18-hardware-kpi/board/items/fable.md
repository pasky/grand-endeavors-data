# Seat fable — Phase 1 options

Common finding: v5b shows the coverage level is a *definition* problem, not a sampling one. The
pairs carrying the whole 0.2% are "Galbot S1 carries heavy bins between stations" vs
"carry tote to feed hopper": Opus 7/7 yes, Luna 1/7. More judges cannot settle a question with no
fact of the matter. Options below remove transfer judgments or accept them as a band.

## fable-1 — Baseline: v5 coverage, simplified and chain-linked
**What.** "Share of US physical work time a GP robot has done autonomously (demo/pilot/deployed)",
today **0.2% (band 0.1–0.3%)**. Panel frozen at ~150 Anthropic tasks; catalogue from ledger; pairs
triaged batched, any-yes pairs re-judged one-per-call by two frozen models; dashboard = mean, band
= per-model. Quarterly: only new catalogue entries get shortlist + judge calls (~200), all cached.
Model upgrade = re-judge all once, publish both values that quarter (CPI-style chain-linking).
**Why.** Only option measuring *capability* breadth against the whole labor denominator;
backcasts by entry date.
**Fail.** Level is a model opinion (see above); catalogue completeness is agent curation; 4 LLM
stages nobody can audit by eye; initial run ~3k calls; still arbitrary, just better hidden.

## fable-2 — Reframe: Anthropic's index, GP-filtered (plain external series)
**What.** Anthropic robot_exposure (CC BY) with one deterministic filter: instance counts only if a
cited source has maturity deployed/commercial, autonomy_status autonomous, and developer on a short
named GP-platform list in `framework.yaml`. Today **~0.5% (≥E1), 0.08% (≥E2)** (convener's rx3).
Refresh when Anthropic re-releases; until then status `unknown`, honestly. 50-line script, zero
LLM calls.
**Why.** Third-party, bit-reproducible, cheapest.
**Fail.** No committed cadence — may never get a second point; instance tier can come from a
co-cited non-GP robot; the GP list is our rule; a release-to-release trend conflates Anthropic's
method changes with progress.

## fable-3 [novel] — Autonomy horizon: longest witnessed autonomous production run
**What.** Record series (like rockets' best $/kg): longest publicly witnessed (livestream or
reporter present) run of a GP robot/fleet doing a workplace's real job, no teleop, in shift-hours
over consecutive days. Today **60 h** (8 AgiBot G2, Longcheer tablet-test section,
10 h × 6 days, Xinhua, June 2026); label lists the own-facility record (Figure 03, 200 h parcel
sort, May 2026). Ledger history: 24 h Dyna lab (2025-04) → 8 h customer shift (2026-04) → 60 h.
Refresh: does a verified ledger event beat the record — one line of judgment.
**Why.** Hardware twin of the software section's METR horizon; milestones sit on the same axis (Blue
Collar Shift = 240 h at a customer, Dark Line = 168 h continuous) → tier-2 pace benchmark for
free; every point is one checkable event; no pipeline.
**Fail.** Vendor-stunt genre (livestreams); throughput unenforced unless we add "line kept its
takt" (the milestone's rule, still a rule); few points → rubric reads quiet quarters as
"stalled"; endurance, not breadth.

## fable-4 [novel] — Literal deployment census (no transfer judgments)
**What.** Count of distinct Anthropic task-instances for which a ledger-verified event shows a GP
platform (humanoid / mobile manipulator) doing *that exact work* autonomously in a named
customer's production flow. Literal match only: Digit moving totes AMR→conveyor at GXO counts for
"move totes at a pack station", not for "carry tote to hopper". Dashboard = the count; label =
employment-weighted share. Today from the v4 catalogue: **~12 deployments ≈ 10–12 instances**
(GXO/Schaeffler Digit, BMW Figure, Longcheer AgiBot, CATL Xiaomo + Galbot, China Post Robotera,
Din Tai Fung Dyna, OPG Spot, Galbot pharmacy, UBTech inspection); by date 2 (2024) → 6
(2025) → 12 (2026); share order 0.1–0.5%. Refresh: each new deployed ledger event → one LLM call
"which instance, literally?" + human glance at a ~15-row table. Cumulative ratchet.
**Why.** Trustworthy: every unit is a named customer + third-party report, auditable in an hour;
reliable: literal mapping has no borderline class (verify with 2 raters × 16 entries); cheap: ~5
calls/quarter; it *is* "which human work have robots taken over", verified, not promised.
**Fail.** Breadth not depth (one site = one count); "production vs pilot" gate needs a sentence
(BMW's single off-hours robot); vendor PR decides what we see — but customer deployments
are what vendors over-disclose, unlike fleet sizes; small count, so a quiet quarter looks stalled.

## Ranking
1. **fable-4** — simplest thing that is actually verified; matches the owner's outcome angle.
2. **fable-3** — best frontier signal, aligned with milestones; would pair with 4 as label context.
3. **fable-1** — most meaningful number, least trustworthy; keep as a yearly research note, not KPI.
4. **fable-2** — adopt only if Anthropic commits to a cadence.
Preferred: fable-4 as the KPI, fable-3 reported in its label.
