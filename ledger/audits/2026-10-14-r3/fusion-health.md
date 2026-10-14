# Round-3 ETA verification: fusion and health

**0 MAJOR findings.** Reviewed rubric v5 in full, round-2 reports, the r1/r2 records and both generations of notes. Current runs: fusion `20261014T171348Z`; health `20261014T171831Z`.

## Findings resolved

- **First Watt / Grid Parity:** The unsupported fast-path re-elicitation is reversed: A .40→.50, B .45→.35. Other central inputs and random draws are retained. First Watt’s numerical median changes 2035.21→2032.18; Grid Parity inherits exactly those draws, changing 2047.01→2045.63. The .40 alternative remains an explicitly assumed sensitivity, not an alleged correction.
- **Cancer endpoint mapping:** Five-year and ten-year non-survival are now explicitly linked through elasticity ε. I checked Coleman’s [Table 2](https://pmc.ncbi.nlm.nih.gov/articles/PMC12859600/#tbl2): the transcribed values and calculated .887 historical elasticity reproduce. Transfer from the England/Wales standardised index to US outcomes and the forecast spread are disclosed assumptions; partial modelling of later source estimates is acknowledged. The constant-q alternative reproduces P=.5636/p50=2094.29 and is retained as a prominent sensitivity. This fixes the unlabelled endpoint transfer without requiring that alternative as the median.
- **Cancer lag:** The 2.9-year lag is no longer called measured or mandated by v5. Notes explicitly concede that the earlier 2-year assumption was not erroneous. Keeping 2.9 is justified as an assumed transfer from publication intervals newly sourced in r1, with 0/2/4-year sensitivities. This is a defensible evidence-based attribution, not another judgment-only replacement; no lag change occurs in r2.
- **Dementia baseline:** Measured ADAMS estimates, sourced WHO weights and assumed within-band standardisation/uniform prior are separated. WHO weights check against SEER’s table. Baseline sensitivities are added without changing the prior or model.

## Reproduction and stability

Executed all five current embedded scripts, including attribution and sensitivity runs, in memory under a **1-GiB address-space cap**; peak RSS approximately **124 MiB**. All printed outputs reproduce after whitespace normalisation. Independently executed the r1 model definitions and SEER fit script.

Current unconditional results (P; p10/p50/p90):

| Target | Reproduced result |
|---|---|
| First Watt | .9305; 2028.52 / 2032.18 / 2060.88 |
| Grid Parity | .7480; 2033.08 / 2045.63 / null |
| Cancer | .8343; 2055.63 / 2073.78 / null |
| Dementia | .6829; 2052.52 / 2079.61 / null |

Every material r1→r2 move is accounted for by restored fusion weights, cancer elasticity/its spread, or calendar-year encoding. Cancer’s P chain is .8861→.8407→.8343. Dementia’s changes are encoding only. All stored quantiles and labels correctly use floor-year encoding; nulls agree with probabilities.

Effective-event checks confirm 72 fusion/77 health records and no ineffective citations in current evidence, calc or notes. IRENA and HALE series match; no new ledger evidence is claimed.

**Minor:** Some health sensitivity/crux prose still rounds years (e.g. cancer’s fast-rate 2059.98 becomes 2060, and its central crux says 2074). Standardise those too; stored forecasts and reproducible calculations are unaffected. Owner-pending definitions remain disclosed, not MAJOR.
