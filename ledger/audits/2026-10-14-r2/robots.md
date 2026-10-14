# Round-2 robotics ETA audit

Scope: software `assess:20261014T143724Z`, hardware `assess:20261014T145110Z`, versus each target’s latest v4 record and working notes. Read RUBRIC v5 and all four relevant round-1 reports. **Five MAJOR findings** below; unresolved definitions are not counted.

## Findings

1. **MILESTONE — MAJOR: Fukushima invents a measured navigation failure count.** The effective `2026-04-18-beijing-robot-warrior-challenge-tien-kung-autonomous` records eight autonomous-navigation rounds and identifies Tien Kung’s successful completion; it does not give outcomes for the other seven. The new notes and `calc` turn this into exactly one success in eight and label `Beta(2,8)` measured. Neither seven failures nor the implicit prior is measured. This also undermines the claimed evidence-based repair of round-1 finding 3 and the attribution of p50 2028→2027. Use an explicitly assumed navigation baseline with sensitivity, or gather round-level outcomes. The correction removing Gemini novelty support and the hand-widened p90 is otherwise implemented.

2. **MILESTONE — MAJOR: Solopreneur’s corrected cohort still enters the qualifying gap.** Although the caveats now correctly describe Levels as revenue across businesses and Base44 as a run rate with unverified solo status, §1 and `calc` still compute an AI-era solo gap of 2.9–3.3× from $3–3.5M. §3 then uses the remaining 1.5–1.7 revenue doublings and Base44’s six-month ramp to motivate the qualifying solo firm’s lag. Round-1 finding 1 explicitly required removing these records from qualifying ARR-gap calculations. Keep them as nonmatching analogies, separately label any transfer, and anchor any provisional solo-ARR gap to the explicitly legacy HeadshotPro record instead. The longer lag is disclosed and sensitivity-tested; that judgment alone is not a finding.

3. **MILESTONE — MAJOR: Dark Line still omits required throughput.** Round-1 finding 4 requested separate treatment of throughput, maintenance and changeover. The replacement model adds finite spares, task/assist rates, attempts and software changeover, but its successful-week predicate only requires no unabsorbed events, enough spares and successful changeover. It never requires ≥90% line throughput or explicitly registers that condition as assumed nonbinding. A slow, failure-free line qualifies in the simulation but not the framework. Add a throughput link and its sensitivity; clarify how routine maintenance is included in the assist model. The otherwise explained p10/p50 +1-year moves do not repair this omission.

4. **MILESTONE — MAJOR: Wozniak’s three-home sensitivity computes the wrong event.** The base model now correctly forecasts first success. However, the advertised LEAP-style alternative sets `theta=.794,m=3` while retaining campaign success `1−(1−p)^m`: at least one successful home, not all three. At the threshold this gives 99.1% rather than 50.1%. Re-running with `p^3`, otherwise unchanged, moves this sensitivity’s median from 2029.70 to 2029.93. This is an implementation error, not a definition disagreement; the base milestone median is unaffected.

5. **RUBRIC-WIDE — MAJOR: assumed forecast uncertainty is labelled measured.** All three software registers label the entire doubling-time distribution measured. Its chosen fast quantile combines a confidence bound with a half-window fit; assigning that value p10 and the long-run fit p90 is judgment, not an observed distribution. Robotaxi similarly labels growth including SD 0.30 and floor 0.15 measured, although two ride-count endpoints do not measure those parameters. Split empirical estimates from assumed forecasting distributions and register their sensitivities. This does not invalidate the reproduced central fits.

## Checks and round-1 closure

Re-executed both notes’ base models and previous-model reproductions in memory under a 1.5-GiB limit. All eight base outputs reproduce. New decimal medians: solo 2029.21, kernel 2029.12, Nature 2029.94; taxi 2028.62, Blue Collar 2027.85, Dark Line 2031.21, Fukushima 2027.78, Wozniak 2028.03.

Ledger spot-checks confirm METR 1,044.78/185.91 minutes and 3.45/4.09-month fits; Waymo 250k→450k weekly rides and 2,500 vehicles across six cities; Dyna 75→93% quality passes, 106% throughput and 7.62/6.52-month fraction/odds halvings; Longcheer 55,107 operations, 99.987%, eight robots; Helix 56% across 30 homes; LEAP 2032/2034; Sakana workshop review/withdrawal and AlphaEvolve’s 48 multiplications.

All selected evidence IDs are effective. Kernel’s tombstone/size errors, Nature’s obsolete citation/median extraction, taxi’s Tesla claim, and Blue Collar’s Optimus inference are fixed. Shared fits now agree. Every threshold-sized ETA move has an explicit attribution; none of the probability moves reaches 0.05. Registers and named failure scenarios exist throughout. Minor: some individual assumed-input sensitivities remain missing or grouped; Blue Collar openly labels its denominator reinterpretation assumed, so it is not hidden measurement.

## DEFINITION — owner decisions, not MAJOR

Solo contractors/accounting/hours; Nature venues/contributions; taxi denominator/L5; Wozniak home selection/maps/retries; Fukushima human-time comparator/site protocol; Dark Line general-purpose robots/remote assistance. Readings and alternatives are now substantially documented.
