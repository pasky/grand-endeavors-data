# Round 2 — Debate (`argon`)

## 1. Concessions & Answers on `argon-1..5`

- **`argon-1` (Baseline v5b) — Dead (concede to `fable`, `astra`):** Besides unidentifiable transfer calls, our 345× PPS finding (`51-9196.00_12691` is `0.0039%` of US physical work but gets `20.16% / 15 = 1.344%` weight in `v5.py:183`) is an inherent variance blow-up of Hansen–Hurwitz PPS estimation whenever rare niche tasks receive positive transfer votes (`w_i` tiny $\Rightarrow 1/(n p_i)$ huge).
- **`argon-2` (Milestone-precursor records) — Patched in place (concede citations to `fable`, `astra`):**
  1. Dyna's 24 h zero-intervention run (`2025-04-29-dyna-1-24h-99pct`) was an undisclosed-site demo, whereas Din Tai Fung (`2026-08-27`) runs 18-h shifts.
  2. Waymo's `500,000/wk` is in `7-deployment-constructions.md`; the latest verified ledger event is `450,000/wk` (`2025-12-01-waymo-450k-weekly-rides`, legacy).
  3. Figure's 200 h HQ sort (`2026-05-22`) did not publish intervention counts.
- **`argon-3` (Task-level parity-discounted share) — Concede & retire in favor of `fable-4` / `argon-6`:** `fable` (1.22% single-task step on `53-7062.00_10781`) and `astra` (workstation slice $\neq$ whole O*NET task; `0.3` default discount is an arbitrary rule) are right. Our own OEWS check proved a 64× employment cliff between adjacent O*NET titles (`53-7062` Hand Material Movers `2.98M` vs `53-7063` Machine Feeders `46.7k`).
- **`argon-4` (Audited revenue) & `argon-5` (Hours bracket) — Concede dead as scored KPIs:**
  - On `argon-4`: Concede to `fable` and `astra` that UBTECH publishes no industrial vs education/training revenue split (`30–50%` was UBTECH's human-productivity ratio in `2026-01-26`, not a revenue split), and trial hardware purchases (Zeekr `2025-03-03`) violate the autonomous-work estimand.
  - On `argon-5`: Concede to `astra` and `fable` that $\sqrt{17.5 \times 1800} = 177.5$ (not 110), Agility's `65,000 h` (`2026-09-15`) is 3-year cumulative operating hours (~22k h/yr) without an autonomy split, and multiplying three assumptions is not a hard upper bound.

---

## 2. Testing `fable-4`'s Decisive Premise (`02-argon-mapping.csv`)

We independently gated and mapped all 24 `deployed`/`pilot` entries in `catalog_v1.json` onto `rx_tasks.csv` instances (`02-argon-mapping.csv`):

1. **Resulting count: 7 cumulative admitted entries / 6 currently active** (plus **1 borderline** stationary dual-arm platform, `C007` Dyna at Din Tai Fung, and **1 internal 3-h pilot**, `C027` Xiaomi).
   - **14 of 24 fail `ledger_ids: []`** (unverified Anthropic-scrape rows, including 3 of `fable-4`'s 11 named examples: `C004` Galbot pharmacy, `C091` OPG Spot, `C021` UBTech inspection; `C010`/`C006` are duplicates of `C005`/`C096`; `C018` Dexie is nursing-home bingo; `C092` is a fixed industrial arm).
   - **2 with `ledger_ids` fail customer-production gates:** `C088` (undisclosed site) and `C027` (3-h internal Xiaomi trial).
   - **Active vs ended:** `C032` (Figure 02 at BMW) ran in 2025 (1 robot at a time) but **ended with 0 robots operating** (`2026-10-07-forbes-bmw-figure-scope`). Thus `fable-4` yields **6 active** (or **7 cumulative**) humanoid customer deployments — triggering `fable`'s own `<8 instances` warning unless unverified scraper rows are ingested and verified first.
2. **Crucial finding from mapping onto `rx_tasks.csv`:** Even when raters agree on the **6–7 admitted deployments**, `rx_tasks.csv` has **2–3 equally literal `(task_id, instance_id)` matches per deployment** because O*NET duplicates shop-floor duties across occupations:
   - `C097` (Galbot carrying bins between CATL stations) is equally literal under `53-7062.00_10781` inst `4` (*Hand Material Movers: moving bins/WIP in a plant*), `53-7063.00_14593` inst `2` (*Machine Feeders: in-plant bin/tote transfer*), and `53-7065.00_23886` inst `2` (*Stockers: line-side bin delivery*).
   - `C001` (AgiBot loading tablets into Longcheer test boxes) is equally literal under `51-9061.00_20304` inst `1`, inst `2`, and `51-2022.00_10024` inst `0`.
   - Worse, every `rx_tasks.csv` instance bundles extra duties the robot does not do (e.g., `53-7063.00_14584` inst `2` includes hand-tool deburring), so a strict rater (`astra`) will map them to `none`.

### Fork: `argon-6` — Verified Active GP Customer Workflows (Drop `rx_tasks.csv` Instance IDs)
- **What:** If the headline is a **count** (`fable-4`), routing 6–7 deployments through 38,000 overlapping LLM-generated `rx_tasks.csv` instances adds pure rater noise (`53-7062` vs `53-7063`) for zero benefit. **`argon-6`** counts **distinct ledger-verified active customer production workflows** performed autonomously by GP robots (humanoids/mobile manipulators), deduplicated by **(6-digit SOC occupation, physical workflow)** directly in the ledger:
  - **Today:** **6 active workflows** (`Digit/GXO` tote-to-conveyor, `Digit/Schaeffler` press-to-washer baskets, `AgiBot/Longcheer` tablet test-fixture loading, `Xiaomo/CATL` HV battery-connector mating, `Galbot S1/CATL` inter-station bin carry, `Robotera/China Post` parcel-sorter induction; **7** with stationary `Dyna/Din Tai Fung` napkin folding; BMW Figure shown as `1 retired`).
  - **History:** `1` (2024) $\to$ `3` (2025) $\to$ `6 active` (2026-Q3). Cost: `<$0.10/quarter`, 1 min, zero external taxonomy files.

---

## 3. Direct Answer on `astra-2` vs `fable-4`/`argon-6` Crux

**Is "documented workflow footprint" (`fable-4`/`argon-6`) vs "work taken over (`not yet measurable`)" (`astra-2`) a factual question or an owner preference?**
- **Factual half:** `astra` is factually right that 6–7 customer deployments do **not** measure economy-wide labor displaced (`<0.01%`), nor occupation-wide task coverage. Calling the number "work taken over" or "% of US work covered" is false.
- **Architectural/preference half:** In `framework.yaml` and `RUBRIC.md §3`, a KPI does **not** have to be economy-wide outcome share when that share is ~0 (`robots-software` tracks frontier task horizon, not % of software engineers displaced; `rockets` tracks best `$/kg`). Leaving `kpi-assessment.csv` empty (`astra-2`) forces `status: unknown` ("Unassessed") indefinitely and duplicates the milestone list.
- **Resolution:** Adopt `argon-6` / `fable-4` explicitly named **"Verified Active GP Customer Production Workflows"** (an audited count of distinct real-world jobs where GP robots work in paid/customer production), and include `astra-2`'s exact caveat (*"Economy-wide labor share: not yet measurable"*) in the KPI description/label.

---

## 4. Position Block

- **Champion:** **`argon-6` / `fable-4` (Verified Active GP Customer Production Workflows — Count Headline)**, preferring `argon-6`'s direct `(SOC, workflow)` deduplication if the 3-way `02-*-mapping.csv` test shows rater divergence on `rx_tasks.csv` `(task_id, instance_id)` codes.
  - *Drop-condition:* Drop to `astra-2` + `argon-2` if the owner rejects a workflow-breadth count and insists the KPI must be economy-wide hours displaced.
- **Compatible co-picks (≤ 2):**
  1. **`argon-2` / `fable-3` (Patched Milestone-Precursor Records)** as companion metrics (`gp-single-site-fleet-max` = 8 units at Longcheer; `gp-unseen-home-success-max` = 56% Helix 2.5).
  2. **`astra-2`'s truthfulness clause** in the KPI label (*"6 active customer workflows; national labor share not yet measurable"*).
- **Dead items:** `argon-1`, `fable-1`, `astra-1` (345× PPS variance blow-up + unidentifiable transfer); `fable-2` (Anthropic citation contamination + no cadence); `argon-3` (64× OEWS weight cliff); `argon-4`, `argon-5` (unreconciled splits / non-bounding assumptions); `astra-3`, `astra-4` (private customer logs required / ceiling or zero series).
- **Open cruxes:** (1) Does our 3-seat `02-*-mapping.csv` test agree on the **admitted set** (6–8 deployments) while diverging on `rx_tasks.csv` `(task_id, instance_id)` IDs (proving `argon-6` > `fable-4`)? (2) Active-only (`6`) vs cumulative (`7`, keeping ended BMW Figure)? (3) Stationary dual-arm VLA (`C007` Dyna) in or out?
