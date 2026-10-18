# The robots-software KPI's pace: components, METR's break, and the status benchmark (2026-10-18)

Owner question (2026-10-18): the KPI (blended 80% horizon) was green for doubling faster than
METR's ~7-month long-run pace, but the blend is not on METR's scale. What are the components'
paces, and what should the status compare against?

Script: pace.py (reads the ledger as of 2026-10-18); output: output.txt.

## Findings

1. **Components over the KPI's window (2025-06-05..2026-09-22):** software (ECI) doubles every
   3.6 months, remote work (RLI) every 2.5, the blend every 2.9 (about the harmonic mean). The
   software pace is ECI's pace (1.25 points per month) divided by the conversion's 4.49 points per
   doubling. Halves: blend 3.0 -> 2.6, software 3.6 -> 3.7, remote 2.2 -> 2.1 months.
2. **METR's own pace broke in spring 2024.** A two-segment fit of its frontier puts the break at
   2024-05 for both p50 and p80: about 8-9 months per doubling before, 3.4-3.5 after (OLS from
   2024-05-01: p50 3.25, p80 3.40). METR's ~7 months is the 2019-2025 average (our p80 frontier,
   2019..2025-03: 8.1; all: 6.4); METR's own file gives 6.2 all-time and 4.2 from 2023 (p50).
3. **The software side keeps METR's post-break pace** (3.5 months since 2024, 3.6 since 2025-06).
   Up to the top calibration model (GPT-5.3 Codex, released 2026-02-05) this follows from the fit;
   after it, it says ECI kept its rate.
4. **The remote side's pace rests on BETA**, the assumed slope of METR's success-vs-length curve:
   roughly proportional to it (BETA 0.5 / 0.6 / 0.7: 2.2 / 2.55 / 2.9 months; 0.4-1.0: 1.8-3.6).
   The framework's "its trend is less affected" understated this. BETA scales both halves of the
   window alike, so a first-vs-second-half comparison is largely free of it (likewise of the ECI
   conversion slope).

## Decision (owner, 2026-10-18)

- The KPI status no longer compares the blend with METR's 7 months (not on the blend's scale, and
  not METR's current pace). It judges whether the blend keeps its own pace: second half vs first
  half (registry row in metrics/kpi-assessment.csv; RUBRIC §3 tier 3 clarified for short
  histories).
- The task-horizon chart gives each line's pace in the legend and draws METR's trend since the
  break (dashed), so the software line can be seen to follow it.
