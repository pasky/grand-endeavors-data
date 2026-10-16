# Findings: the robots-software milestone ETAs need a new basis (owner request, 2026-10-16)

The 2026-10-16 records (and their v6 predecessors) model each milestone as "the task horizon reaches a
target" plus a lag. The target was a guessed human-effort figure times an uncalibrated transfer factor
of 2. The owner rejected that basis: the hour targets were not derived from evidence, precursor events
never updated them, and the domain and reliability choices were ad hoc. Rebuild each ETA on the
structure below. Earlier records are context only; do not carry their effort constants or the ×2 factor
forward.

The ledger now holds a targeted intake for 2025-07 to 2026-10 (gather run of 2026-10-16, FOCUS on
precursor ladders), the 80% KPI series and the new task-horizon driver.

## 1. Driver, success level and domain (owner decision)

All three milestones use the task-horizon driver at **80% success**: the milestones are about autonomy,
not assistance. Do not use the 50% horizons, except as a labelled sensitivity. Sample the driver's draws
in order (`ledger.py driver-draws task-horizon --as-of <made_at>`). The *_draw parameters already carry
the conversion errors.

| Milestone | Domain (central) | Driver draws | Why |
|---|---|---|---|
| the-linux-kernel-patch | software | `h80_software_draw`, `doubling_software_months` | the work is software engineering |
| the-nature-author | blended | `h80_blended_draw`, `doubling_blended_months` | research spans code and analysis plus writing, figures and judgement |
| the-10m-solopreneur | blended | `h80_blended_draw`, `doubling_blended_months` | a business spans code plus marketing, support, design and finance, the remote-work side of the KPI |

Give the ETA under each of the other two domains as a sensitivity.

## 2. The mapping: calibrated on precursor ladders, not guessed

For each milestone, define a **ladder** of observable rungs that lead up to the milestone, on the
milestone's own scale:

- **Kernel patch:** the size (lines) of the largest substantially AI-written contribution accepted into
  critical infrastructure, then into major open-source projects.
- **Nature author:** the venue tier of the best accepted, substantially AI-generated paper: workshop,
  then main track or mid-tier journal, then top field journal, then Nature/Science.
- **Solopreneur:** the highest verified recurring revenue of a genuinely one-person company. The
  oversight half is section 4.

Place the ledger's evidence on the ladder. A rung that has been **reached** gives the date it was
reached and the horizon at that date, read from the collector's 80% series for the chosen domain (cite
the metric id and value). A rung that has **not** been reached is **censored**: it has not happened
although the horizon has already reached its value today. Estimate the mapping from both kinds:

- the doublings of horizon per rung (or per doubling of size or revenue);
- equivalently, the horizon needed for the milestone rung.

Give it as an interval with its sources. Censored rungs yield lower bounds; say so instead of inventing a
point. Where the rung structure needs a human-effort figure, take it from a sourced reference class in
the ledger, with counts. Do not use rules of thumb such as lines per day.

Note where a ladder is censored by policy rather than by capability, for example venues withdrawing or
banning AI-generated papers. The milestones assume such gates away, so weigh those rungs accordingly and
state how.

## 3. Cross-checks, not the central case

- **Benchmarks with human-time estimates** (e.g. MirrorCode, SWE-Marathon) show that oracle-checked,
  well-specified work can succeed far beyond the METR-style horizon. Use them as the optimistic bound and
  quantify the gap. Do not use them as the central mapping for review-gated milestones.
- **External forecast anchors:** `ledger.py anchors robots-software`; none are approved yet.

## 4. Process lags and the solopreneur's two conditions

- **Lags from reference classes with counts,** not invented triangles:
  - Kernel: review-to-merge times of large new kernel series or drivers.
  - Nature: submission-to-acceptance times at Nature/Science.
  - Solopreneur: revenue ramp times of the fastest AI-native companies, plus the qualifying quarter and
    disclosure.
  - If the ledger lacks the class, say so, and widen the lag rather than narrowing it.
- **The solopreneur needs both $10M ARR and under 10 hours a week of oversight.**
  - Model them separately: revenue from the verified solo-revenue ladder (direct extrapolation, with its
    verification quality), and oversight from the capability gate on the blended 80% horizon.
  - Derive the gate from the oversight budget and the amount of work in a $10M business (sourced revenue
    per employee for small software or online businesses), not from a guessed work interval.
  - The ETA is the later of the two conditions, not their sum.

## 5. Update channels and failure scenarios

- **Update channels:** list in the record which observations would move the ETA, and by roughly how
  much. Examples: the next rung reached or still missing at a later date; a new verified ARR; the
  horizon's pace.
- **Failure scenarios:** keep them as in v6, each of 10% or more with its reference class and counts.

## 6. Review focus

The reviewer checks four things:
- no guessed effort constant or unexplained transfer factor survives;
- every reached or censored rung cites a ledger event or series value;
- the domain and the 80% level follow section 1;
- the ETA's sensitivity to the mapping interval is stated.
