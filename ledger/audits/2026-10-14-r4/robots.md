# Round-4 robotics ETA audit

**0 MAJOR findings. Both round-3 findings are fixed; no new MAJOR issue found in this narrow verification.**

Scope: latest Nature record `assess:20261014T180343Z` and Dark Line record `assess:20261014T180732Z`, both tagged `2026-10-14-r3`, compared with r2 runs `20261014T164549Z` and `20261014T165450Z`. Checked rubric v5 §4.1 step 7 and §5 rule 7, working notes, assessment fields, effective cited events and driver series.

- **Nature:** §5 now separates historical OLS estimates and confidence bounds from the assumed 2.53/3.45/5.97-month forecast distribution. The judgmental 2.53-month fast case is explicitly assumed, including in the assessment calc. Fixed-rate and alternative-spread sensitivities reproduce.
- **Dark Line:** `shared(..., s0=0.08)` changes the shared-stall threshold while retaining own failure at 0.10 and the same random draws. The corrected 50,000-draw sensitivity reproduces **p_achieved 0.828, p10 2029.06, p50 2031.48, p90 null**; survival analytically is 0.92 × 0.90 = 0.828. Tables and assessment calc agree. The old wrong-input result remains only as an explicitly identified comparison.

**Reproduction/stability:** Executed both current software scripts and hardware `meta dark`, plus both r2 base models, in memory through `uv`, under a **1.5-GiB address-space limit**. Hardware grids use 1,500-draw chunks; observed peak RSS stayed below 300 MiB. Current script outputs match the stored output blocks exactly. Nature reproduces 0.908 and 2028.68/2029.94/2035.43; Dark Line reproduces 0.881 and 2029.04/2031.28/null. Stored probabilities, calendar-year quantiles and statuses remain unchanged versus r2; change notes correctly attribute the corrections without changing base assumptions.

Minor wording: Nature’s post-register discussion calls the future rate measured; “historical fitted rate” would be more precise. The register and model explicitly identify the forecast distribution as assumed, so this does not reopen the resolved finding.
