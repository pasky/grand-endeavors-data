# Climate round-3 verification

**0 MAJOR findings.** Reviewed rubric v5 in full, round-2 README/climate findings, current Balance/Ceiling records and notes (`20261014T172622Z`), and their round-1 predecessors plus unchanged Bend (`20261014T161054Z`). Some non-blocking presentation/diagnostic issues remain.

## Previous findings and attribution

**Balance: fixed.** The assessor explicitly withdraws the claim that separate residual-floor attainment is physically necessary. Both milestones now subtract the same removals from gross CO₂; Balance tests total net GHG, permitting offsets above either floor. The new removal saturation is explicitly an assumed deployment constraint, with named resource constraints and substantial sensitivities—not another claimed accounting identity. This addresses round 2’s alternative of justifying a deployment restriction.

The rule-7 chain reproduces: probability **.091 → .5525** with unrestricted net-flow accounting, then **.1533** with the removal S-curve; p10 becomes **2094.6 → 2094**. The change_note identifies both changes and their audit connection. Existing rates, floors, uncertainties and named failure probabilities are retained.

**Ceiling: fixed.** Achievement is now computed from the maximum of cumulative net CO₂ plus trajectory-dependent non-CO₂ warming equivalent, with a held-peak condition. GWP*’s aggregate application is labelled assumed and sensitivity-tested. It no longer identifies CO₂ neutrality with the temperature peak: successful peaks precede neutrality by a median 16.8 years. Removing non-CO₂ deceleration changes probability from .0740 to .0025, unlike the previous insensitive calculation.

Its attributed chain reproduces: **.0392 → .1673 → .0980 → .0755 → .0740** (net flows, removal saturation, physical-peak calculation, removal of the redundant non-CO₂ uncertainty term). No unexplained ETA move remains.

## Reproduction and consistency

Executed both archived model scripts in memory using independently retrieved effective ledger series: all 50,000 draws, 2,000-draw batches, 2-GiB address-space limit; peak resident memory approximately 350 MiB. Central results, attribution chains, diagnostics and sensitivity tables reproduce. Balance is .1533 with p10 2094.6; Ceiling is .0740 with all quantiles null.

Bend retains precisely the same emissions fit and results: .9496; decimal quantiles 2031.4/2036.9/2050.6, stored as **2031/2036/2050**. Balance’s 2094 encoding and all null quantiles follow the rubric. Evidence arrays contain no ineffective IDs; checked climate calculation citations also pass.

## Minor follow-ups

- Ceiling’s reported .9498 probability of a pre-terminal maximum is inflated by a duplicate final cumulative value: the integration weight is zero at the last grid point. Excluding that artificial endpoint plateau gives **.70156**; the held-peak filter leaves the actual Ceiling probability and timing **unchanged**.
- AR6 WG3 SPM C.3.5 supplies cumulative pathway ranges, not proof that every pathway excludes 20–40 Gt/year removals. Soften that universal claim. Also distinguish the assumed Gaussian/linear reference-path construction from its genuinely sourced endpoints (C.2.3). These do not invalidate the disclosed, sensitivity-tested assumptions.

Tolerance/GWP convention and physical peak versus recognition/permanence remain owner-pending definition questions, not MAJOR findings.
