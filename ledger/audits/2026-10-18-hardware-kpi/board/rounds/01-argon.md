# Round 1 — Cross-Examination (`argon`)

## 1. Factual Audits Performed on Ledger, Catalogue & O*NET Data

- **Why `v5b`'s hopper pair swung the US headline (`v5.py:183`, `items.json`):** The contested task `51-9196.00_12691` (*Paper Goods Machine Setters*, carrying totes to a feed hopper) is only **0.0039% (`3.9e-5`) of US physical work**. Because `v5.py` averages 15 PPS draws in Stratum A equally (`20.16% / 15 = 1.344%` each), that lucky 1-in-5,000 draw was upweighted **345×**, letting one sub-step judgment on paper machines move the national estimate by ~0.20 pp.
- **Audit of `catalog_v1.json` (16 `deployed`, 8 `pilot`) vs `robots-hardware.jsonl` (powers `fable-4` & `argon-3`):**
  - Only **8 `deployed` customer cases** and **1 factory `pilot`** (Xiaomi `C027`) in `catalog_v1.json` have verified `ledger_ids` in `robots-hardware.jsonl`.
  - `C005` and `C010` are **duplicate `deployed` entries** for CATL's Xiaomo battery-connector robot (`C086`/`C088` also duplicate Digit).
  - Three of `fable-4`'s 11 named examples (`C004` Galbot pharmacy, `C091` OPG Spot, `C021` UBTech inspection) have `ledger_ids: []` (unverified Anthropic scrape), and `C021` has `customer: null` (a generic vendor solutions URL).
  - `C018` (`deployed`) is a pre-programmed nursing-home bingo/sing-along bot (`Dexie`); `C092` is a stationary industrial robot arm.
  - Figure 02 at BMW (`C032`) was corrected by `2026-10-07-forbes-bmw-figure-scope`: only 1 robot worked at a time in 2025, and the 2026 test **ended with 0 robots operating**.
- **Audit of `argon-3` (`0.14%`) & `fable-4` (`0.1–0.5%` share) against OEWS (`national_M2024_dl.xlsx`) + `rx_tasks.csv`:**
  - Across the 8 ledger-verified deployments, unadjusted share is **1.34% full-task / 0.34% literal-instance** (~**0.14%** throughput-discounted).
  - **Crucial finding:** **90% of that share (`0.306%` of `0.340%` instance-level)** comes from **one O*NET code**: `53-7062.00_10781` (*Hand Freight/Material Movers*, `TOT_EMP = 2,982,530`). Mapping Digit/Galbot tote/bin moves instead to `53-7064.00_3215` (*Hand Packers*, `601,440`) or `53-7063.00_14587` (*Machine Feeders*, `46,690` — 64× smaller!) drops the national share **7× (from 0.34% to 0.05%)**.
  - Also, `fable-4`'s quoted instance *"move totes at a pack station"* does not exist in `rx_tasks.csv`: `53-7064.00_3215` inst 2 is carton removal + parcel diversion + dock staging, where both Opus and Luna scored Digit `0/7` in `v5b`.
- **Audit of `fable-3` (`60 h`):** In `2026-06-28-agibot-longcheer-whole-section-8-robots` and `2026-06-29-agibot-six-day-factory-livestream`, Longcheer reported *54–64 cumulative robot-hours* across 8 robots over 6×10 h day-shifts, explicitly noting **robot-to-robot collisions, arm clashes, a supporting maintenance team, and unquantified interventions** — not a 60 h intervention-free autonomous run.
- **Audit of `argon-4` (`~620 FTE-yr`) & `argon-5` (`[17.5, 1,800]`):** Confirmed in `2-unit-data.md`/`4-economics.md`, but UBTECH's RMB 820.6M 2025 revenue has no audited industrial vs education/exhibition split (`~$15M` industrial was an unverified assumption), and Agility's `65,000 h` (`2026-09-15-agility-digit-65000-hours`) is cumulative multi-year operating hours without an autonomous-vs-teleop breakdown.

---

## 2. Cross-Examination of `fable` and `astra` Items

| Item | Fatal Flaw (if any) | Upside | Prob | Cost |
|---|---|---:|---:|---:|
| **`fable-1`** (v5 + chain-link) | **Fatal:** PPS upweights a `0.0039%` paper-machine task 345× (`v5.py:183`), and CPI chain-linking locks in arbitrary 3× Opus/Luna transfer splits (`v5b.py`). | 7 | 2 | 6 |
| **`fable-2`** (Anthropic GP-filter) | **Fatal:** In `rx_tasks.csv`, Claude cited Digit at GXO (`C086`) to credit *Probation Officers doing drug tests* (`21-1092.00`), *Coaches traveling with teams* (`27-2022.00`), and *Vet Techs assisting with animal euthanasia* (`29-2056.00`), and cited CATL's Xiaomo (`C010`) for *Elementary Teachers plugging in classroom AV cables* (`25-2021.00`). Also no update cadence. | 5 | 1 | 1 |
| **`fable-3`** (60h witnessed horizon) | **Non-fatal flaw (fixable):** Today's `60 h` (`2026-06-28-agibot-longcheer...`) had collisions, a human maintenance team, and undisclosed interventions. Must require **0 human interventions** (today: **24 h**, `2025-04-29-dyna-1-24h-99pct`, or **4 h** customer shift). | 7 | 7 | 1 |
| **`fable-4`** (Literal instance count) | **Same item as `argon-3`** (literal deployment-to-O*NET mapping, zero transfer). No fatal flaw once fixed: (1) restrict to ledger-verified *active* customer deployments (BMW Figure ended, `2026-10-07-forbes-bmw-figure-scope`; 3 of 11 listed items aren't in ledger), and (2) use instance *count* as primary number to avoid the 64× OEWS employment cliff (`53-7062` vs `53-7063`). | 9 | 9 | 2 |
| **`astra-1`** (Human-adjudicated v5) | **Fatal:** Swapping LLM judges for the owner adjudicating 2,861 speculative cross-occupation pairs cannot fix a 345× PPS sampling multiplier (`51-9196.00_12691`) or invented sub-step weights, and fails priority #3/#4 (~1 reviewer-day/quarter). | 6 | 2 | 8 |
| **`astra-2`** (No KPI / 0/4 milestones) | **Fatal vs `RUBRIC.md §3`:** Leaves `kpi-assessment.csv` empty (`status: unknown`) indefinitely when verified literal deployment counts (`fable-4`/`argon-3`) and endurance records (`fable-3`/`argon-2`) are already measurable in the ledger. | 3 | 9 | 1 |
| **`astra-3`** (Dyna napkin sentinel) | **Fatal:** Requires private quarterly vendor/customer outreach (violates autonomous public-data pipeline in `DESIGN.md §4`) and tracks a single stationary dual-arm robot (`C007`) on one restaurant task, not general-purpose automation. | 3 | 2 | 7 |
| **`astra-4`** (Redeployment certificates) | **Fatal:** Value is `0` today and requires unobtainable customer-signed hardware-unchanged certificates; `RUBRIC.md §3` cannot score trend/pace on a constant zero series. | 4 | 1 | 7 |

---

## 3. Position Block

- **Are `argon-3` and `fable-4` the same item?** **Yes.** Both discard `v5`'s PPS sampling and cross-occupation transfer speculation in favor of **1-to-1 literal mapping of ledger-verified GP customer deployments onto Anthropic/O*NET tasks**. Combining them cures both halves' bugs: **`fable-4`'s unweighted instance count** avoids the 64× OEWS employment cliff (`53-7062` vs `53-7063`) that hits `argon-3`'s `0.14%` share, while **`argon-3`'s strict ledger-verification + active-status + human-parity throughput gate** cleans up `fable-4`'s unverified catalogue rows and ended BMW trial.
- **Champion:** **Unified `fable-4` / `argon-3` (Verified Active GP Customer Deployment Instances)** — count of distinct O*NET/Anthropic task-instances where a GP robot is actively operating autonomously in a named customer's production workflow (today: **7 active instances** across 8 verified customer deployments, or **8** if counting BMW's completed 2025 run; employment-weighted share **0.05–0.34%** reported in the label).
  - *Drop-condition:* Drop if two raters mapping the 8 ledger-verified customer deployments to `rx_tasks.csv` instances disagree on >1 instance count.
- **Compatible co-picks (≤ 2):**
  1. **`fable-3` / `argon-2.1` (Longest Verified Zero-Intervention Autonomous Run)** as a companion tile/label metric (strictly intervention-free: **24 h** today).
  2. **`argon-4` (Audited Commercial GP Robot Revenue in Filings)** as a secondary commercialization check once ≥3 issuers disclose industrial segment splits.
- **Dead items:** `fable-1`, `astra-1`, `argon-1` (345× PPS upweighting of tiny tasks + unidentifiable transfer judgments); `fable-2` (Anthropic's citations credit GXO Digit for Probation Officers and Vet Tech euthanasia, and no cadence); `astra-3`, `astra-4` (private outreach required, single-task or constant-zero series).
- **Open cruxes:**
  1. Should ended customer runs (Figure 02 at BMW, `2026-10-07-forbes-bmw-figure-scope`) stay in the cumulative capability count (`8` instances) or drop out of an active-deployment count (`7` instances)?
  2. Should stationary dual-arm generalists (Dyna at Din Tai Fung, `C007`) count alongside humanoids/mobile manipulators?
