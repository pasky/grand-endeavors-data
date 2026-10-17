# Task-horizon calibration: option D (owner, 2026-10-17)

## Decision
The owner chose option D for the software side of the task-horizon driver (data drivers.yaml):
keep the METR-only ECI -> METR-hours calibration (frozen constants unchanged; horizon-80-software-eci
and the KPI horizon-80-blended are unchanged), add a cross-check panel and a tripwire, and widen the
software conversion error. The robots-software KPI's definition and data did not change (no
re-assessment needed; it is not stale).

## What changed in the driver
1. `software_conversion_doublings`: normal sd 0.553 -> 0.70 doublings (the calibration's prediction
   error at ECI 166.82, plus an assumed allowance for the calibration slope's form over the 10 ECI
   points beyond METR's data). Anchors, doubling times and the remote side are unchanged. The draws
   of `h80_software_draw`, `h80_blended_draw` and `h50_software_draw` are therefore wider (re-run
   `ledger.py driver-draws task-horizon`).
2. The earlier fit text said the pace converted from ECI "may be too fast at the frontier" because
   SWE-Marathon's 80% horizon barely rises with ECI. The review found that this is a resolution
   limit of that suite (6 of its 20 tasks almost always solved by frontier models, 7 almost never),
   not evidence of a slower pace: it is no longer a reason to lean slower than the driver.
3. Cross-check series (not KPI inputs): horizon-80-gap-swe-marathon and horizon-80-gap-metr
   (measured minus converted 80% horizon at the ECI frontier, doublings; SWE-Marathon +0.01 in
   2026-09 and 2026-10, earlier months +1.05 to +2.23 with only older models in the window; METR's
   ends 2026-03), terminal-bench-4-pass-by-release (frontier resolution rate 23.64% 2026-05-28 ->
   64.85% 2026-09-22). The tripwire (two gap series beyond one doubling, same side, two consecutive
   months) has not fired.
4. Pace cross-checks recorded in the driver's fit text: UK AISI's cyber 80% horizon doubling time
   (4.7 months, its 2026-02 estimate, newer models above it), METR's own trend (128.7 days at 50%
   since 2023) and METR's last 80% point projected at 4.2 months per doubling (7.7 h by 2026-09-22
   against the 7.930 h anchor). All lie inside the driver's doubling-time spread (p10 2.75, p50
   3.755, p90 6.365 months); none argues for moving it.

## Findings (each milestone sampling task-horizon)
- milestone:the-linux-kernel-patch, milestone:the-nature-author, milestone:the-10m-solopreneur:
  (a) recompute the ETA from the current driver draws: the wider software conversion error changes
  the spread of every quantity derived from the software horizon; state the new p10/p50/p90 and how
  much the change moved them; (b) drop any reliance on the superseded "converted pace may be too
  fast" caveat (finding 2); (c) these milestones are also stale on their precursor series
  (framework.yaml precursors:), which were backfilled after their last assessment: address them.
