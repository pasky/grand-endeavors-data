# Round 3 — Debate & Premise Audits (`argon`)

## 1. Premise Audit of `fable-4` vs `argon-6` (The 3-Seat Mapping Test)

The Chair's comparison of `02-{fable,argon,astra}-mapping.csv` settles the core empirical question of this board:
- **Deployment-level admission (`argon-6` premise) is reproducible across labs:** All three seats unanimously admitted the **exact same 7 humanoid customer deployments** (`C001, C005, C032, C086, C087, C096, C097`) and unanimously rejected the **same 16 entries** (23/24 agreement; the 24th is the declared `C007` stationary-arm crux).
- **Instance-level mapping (`fable-4` premise) failed its own drop-condition:** Pairwise agreement on `rx_tasks.csv` `(task_id, instance_id)` among the 7 unanimously admitted entries was **1/7 (`fable`–`argon`), 1/7 (`fable`–`astra`), and 2/7 (`argon`–`astra`)**, producing counts of **5, 7, and 3** (`fable`'s drop-condition was disagreement on `>2/8`).
- **Why `fable-4` failed while `argon-6` held:** `rx_tasks.csv` splits blue-collar work into ~38,000 LLM-generated multi-clause instances across overlapping O*NET occupations (`53-7062` Material Movers vs `53-7063` Machine Feeders; `51-2022` vs `51-2023` vs `51-9061`), forcing arbitrary slice-vs-whole and occupation-code calls even when all three raters agree on what the robot physically did.

---

## 2. Direct Answers to Chair & Other Seats

- **On `argon-6` (SOC dedup & exact ledger history):**
  - **Patch `argon-6` in place — drop SOC codes:** SOC codes are unnecessary and re-import the `53-7062` vs `53-7063` boundary collision (`fable` merged `C087` Schaeffler press-to-washer baskets with `C097` CATL line-to-line bin transport only because both fell into `53-7062_10781/4`). Deduplicate strictly by **(Named Customer, Facility/Line, Physical Task)** — i.e., **count of ledger-verified customer production deployments of autonomous GP robots** (which all 3 seats scored **7/7 humanoid, 8/8 with `C007`** with zero disagreement).
  - **Checked history in `robots-hardware.jsonl` (7 humanoid deployments; +1 with `C007` Dyna):**
    - *By event `date`:* **2024:** `0` in ledger (`C086` GXO began 2024-06 in catalogue, dated `2025` in `2025-01-01-digit-gxo-raas-deployment-rv`) $\to$ **2025-H1:** `2` (`C086` GXO `2025`, `C032` BMW live line from Mar 2025 per `2025-04-06-fortune-bmw-single-figure-robot`) $\to$ **2025-H2:** `3 cum / 2 active` (`+C005` CATL Xiaomo `2025-12-17`; `-C032` Figure 02 retired `2025-11-19`) $\to$ **2026-Q1:** `4 cum / 3 active` (`+C087` Schaeffler Digit `2026-03-25`) $\to$ **2026-Q2/Q3 (Today):** **`7 cum / 6 active`** (`+C001` Longcheer AgiBot `2026-04-14`, `+C096` China Post Robotera `2026-05`, `+C097` CATL Galbot `2026-06-24`). *(With `C007` Dyna `2026-08-27`: **8 cum / 7 active**.)*
    - *By strict `published` (`known_at`) date:* **2025-Q2:** `1` $\to$ **2025-Q4:** `3 cum / 2 active` $\to$ **2026-Q1:** `4 cum / 3 active` $\to$ **2026-Q2/Q3:** **`7 cum / 6 active`** (**`8 / 7`** with `C007`).
- **On PPS (`258×` vs `345×`):** Concede `astra`'s count (`v2_selection.json` has 20 Stratum A tasks $\Rightarrow 258\times$ weight on `51-9196.00_12691`, not $345\times$) and agree with `fable` and `astra` that this is **high variance, not bias**, of Hansen–Hurwitz PPS estimation when positives are rare. The **fatal** flaw killing `argon-1`/`fable-1`/`astra-1` is **unidentifiable cross-occupation transfer judgments + invented sub-step weights**; PPS variance is a cost/sample-size penalty.
- **On `argon-4` & `argon-5` (pressed by `fable`, `astra`):** Explicitly **withdrawn/dead** in Round 2 and here (`argon-4`: no UBTECH industrial split, counts trial hardware; `argon-5`: $\sqrt{17.5 \times 1800} = 177.5 \neq 110$, endpoints are non-bounding assumptions).
- **One-line factual crux between `astra-2` and `argon-6`/`fable-4`:**
  > **Factual crux:** Whether vendor/customer/state-media reports of autonomous production operation in our verified ledger (`C001, C005, C032, C086, C087, C096, C097`), in the absence of independently audited third-party intervention logs, establish that autonomous GP production work occurred (`argon-6`: 7 cumulative / 6 active) or leave autonomous work unestablished (`astra-2`: unknown).

---

## 3. Source Audits of `argon-2` Records & Non-Author Finalist `astra-2`

- **Audit of `argon-2` records in `robots-hardware.jsonl` (`verify:20261012T144115Z` notes):**
  1. `2026-06-28-agibot-longcheer-whole-section-8-robots` (Xinhua + Stockstar): **Establishes** 8 AgiBot G2 humanoids concurrently staffing Longcheer's MMIT section on 10 h/day shifts (up from 4 in April). **Does NOT establish** human-free autonomy: Longcheer's Li Long explicitly reported robot collisions (`撞车`), arm clashes (`打架`), lidar drops, and an on-floor maintenance team (`运维团队`). Must be labelled *"Largest concurrent section fleet (with human maintenance team)"*, never "autonomous fleet".
  2. `2026-09-17-figure-helix-25-30-homes` (Figure primary post): **Establishes** Figure's reported 56% zero-shot full-task success across 30 unseen Bay Area homes on 3 chores. **Does NOT establish** independent home selection or coffee preparation.
  3. `2025-04-29-dyna-1-24h-99pct` (PR Newswire): **Establishes** a vendor-claimed 24-h zero-intervention run (800+ napkins) by stationary dual arms at an undisclosed commercial/demo site; **does NOT establish** humanoid endurance or Din Tai Fung shift logs.
- **Non-author audit of `astra-2`:** Verified against `RUBRIC.md §3` and `assessments/robots-hardware.jsonl` (`2026-09-30-kpi` is currently `status: unknown`, *"no KPI metric registered"*, and all 4 GP milestones are `yellow`/`red`, `0/4 achieved`). **Establishes** that `astra-2` is 100% rubric-legal today; **does not establish** a trend-scorable KPI series once a verifiable deployment count (`argon-6`) is available.

---

## 4. Position Block

- **Champion: `argon-6` (Verified Customer Production Deployments of Autonomous GP Robots — no `rx_tasks`/SOC mapping).**
  - **Today's value:** **6 active / 7 cumulative** humanoid customer deployments (**7 active / 8 cumulative** if stationary dual-arm `C007` Dyna counts), with history `1` (2025-Q2) $\to$ `3` (2025-Q4) $\to$ `4` (2026-Q1) $\to$ `7 cum / 6 active` (2026-Q2/Q3).
  - **Why over `fable-4`:** The 3-seat experiment proved **23/24 (100% humanoid) agreement** at `argon-6`'s deployment gate vs **1/7 agreement** at `fable-4`'s `rx_tasks.csv` instance step (triggering `fable`'s own drop-condition).
  - *Drop-condition:* Drop to `astra-2` if the owner rules that without third-party audited intervention logs, even ledger-verified customer deployments cannot be counted.
- **Compatible co-picks (≤ 2):**
  1. **`astra-2` truthfulness label** (*"Economy-wide labor share: not yet measurable; KPI tracks verified customer production deployments"*), or `astra-2` as fallback if the owner rejects a deployment count.
  2. **`argon-2` precursor records** (with explicit caveats from the audit above) as milestone-level context.
- **Dead items:** `fable-4` *instance-mapping step* (failed 3-rater test: 1/7 agreement); `argon-1`, `fable-1`, `astra-1` (unidentifiable transfer judgments); `fable-2` (citation contamination); `fable-3` (60h schedule $\neq$ intervention-free); `argon-3` (64× OEWS cliff); `argon-4`, `argon-5` (withdrawn); `astra-3`, `astra-4` (conceded/dead).
- **Open cruxes (for owner decision):** (1) Active (`6`) vs cumulative (`7`, keeping ended BMW Figure `C032`) as headline; (2) Stationary VLA dual-arm (`C007` Dyna) included (`+1`) or humanoid/mobile-manipulator only; (3) Count verified customer deployments (`argon-6`) vs stay `unknown` until third-party intervention audits exist (`astra-2`).
