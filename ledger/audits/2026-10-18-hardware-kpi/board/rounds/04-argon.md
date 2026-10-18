# Round 4 — Final Debate & Convergence (`argon`)

## 1. Concessions on `argon-6` & Merger into `fable-5`

- **Answer to `astra` and `fable` on `argon-6`'s `"Physical Task"` key & `"Active"` status:**
  - **Concede `"Physical Task"` boundary:** `astra` is right that `2025-11-20-digit-100k-totes-gxo-r2` (`L185`) describes two tote activities at GXO and `2026-06-29-agibot-six-day-factory-livestream` (`L210`) claims `>4 production workflows` at Longcheer. Keeping `"Physical Task"` in the dedup key re-introduces boundary calls that entity-only deduplication avoids.
  - **Concede `"Active"` inference:** Both `astra` and `fable` are right that deployments are never proved active, only proved ended (`2026-10-07-forbes-bmw-figure-scope`). The headline series must be **cumulative documented deployments**, with known ended runs (`1 ended: Figure/BMW`) annotated in the label.
- **Merger of `argon-6` into `fable-5`:** With `"Physical Task"` and `"Active-only"` dropped in favor of cumulative `(GP platform, named customer)` pairs, **`argon-6` is identical to `fable-5`**. By mutual agreement with `fable` (`03-fable.md`: *"argon: drop SOC and argon-6 = fable-5"*), **we merge `argon-6` into `fable-5`**.

---

## 2. Non-Author Audit of `astra-5` & Condition Between `fable-5` and `astra-5`

- **Audit of `astra-5` (*distinct named customer organizations ever documented*, today `7` incl. DTF / `6` humanoid):**
  - **What holds:** `astra-5` is reproducible across all 3 seats (`GXO, BMW, CATL, Schaeffler, Longcheer, China Post` [+ `Din Tai Fung`]), eliminates task-boundary calls, and uses clean prospective `published` dating.
  - **Edge case found:** Corporate-hierarchy consolidation (`China Post Group` spans 31 provincial corporations and 10+ logistics centres; `CATL` has separate bases in Luoyang and Ningde). In `robots-hardware.jsonl`, CATL deployed **Spirit AI's Xiaomo** at Luoyang for fine **HV connector insertion** (`2025-12-17`) and **Galbot's S1** at Ningde for **50 kg inter-station bin transport** (`2026-06-24`). Collapsing both to `1` customer (`astra-5`) means once top industrial conglomerates (CATL, BYD, Amazon, China Post) each run one pilot, additional robot makers winning completely different jobs and factories inside those enterprises register as zero progress.
- **Decision rule (`fable-5` vs `astra-5`):**
  - **If the owner wants multi-vendor / multi-job diffusion inside large enterprises to register** $\to$ **`fable-5` (`(GP platform, named customer)` pairs: `8` incl. `C007` DTF, `7` humanoid)**.
  - **If the owner wants each enterprise buyer counted at most once regardless of how many robot platforms it adopts** $\to$ **`astra-5` (`named customer organizations`: `7` incl. `C007` DTF, `6` humanoid)**.

---

## 3. Reconciling the History Series & Dating Rule (`fable` vs `argon`)

Why `fable` had `1 (2024) → 5 (2025) → 8 (2026-Q3)` while `argon` had `1 (2025-Q2) → 3 (2025-Q4) → 4 (2026-Q1) → 7/8 (2026-Q3)`:
- **`fable` used retrospective operation-start dates** mentioned inside later articles: GXO RaaS start (`2024-06`), Din Tai Fung Dyna-1 launch (`2025-06`, first published `2026-08-27`), and Robotera's initial arrival at China Post (`2025-11` at 100 parcels/hr before 6 months of night-shift engineering support, first published `2026-06-02`).
- **`argon` used ledger `published` (`known_at`) dates (`DESIGN.md §2`):**
  1. `Figure 02 / BMW` (`C032`): `2025-04-06` (*Fortune* confirming live-line work) $\to$ **1**
  2. `Digit / GXO` (`C086`): `2025-11-20` (`100k totes` ledger record; `2024-06-27` if GXO's 2024 RaaS release is backfilled) $\to$ **2**
  3. `Xiaomo / CATL` (`C005`): `2025-12-18` $\to$ **3** (end-2025)
  4. `Digit / Schaeffler` (`C087`): `2026-03-25` $\to$ **4** (2026-Q1)
  5. `AgiBot G2 / Longcheer` (`C001`): `2026-04-15` $\to$ **5**
  6. `Robotera / China Post` (`C096`): `2026-06-02` $\to$ **6**
  7. `Galbot S1 / CATL` (`C097`): `2026-06-24` $\to$ **7** (2026-Q2, humanoid-only)
  8. `Dyna / Din Tai Fung` (`C007`): `2026-08-27` $\to$ **8** (2026-Q3, incl. stationary VLA)
- **Recommended dating rule:** Date each pair by **`first_published` (`known_at` of the first qualifying ledger event)** (with GXO's `2024-06-27` release backfilled so 2024 = `1`), because under `DESIGN.md §2` retrospective start-dates revealed a year later would otherwise rewrite frozen `--as-of` period snapshots.

---

## 4. Evidence on the Autonomy Verification Crux (`fable-5`/`astra-5` vs `astra-2`)

Auditing corroboration across the 8 admitted deployments in `robots-hardware.jsonl`:
- **7 of 8** (all except vendor-reported `C007` Dyna/DTF) have **customer statements** (BMW, Longcheer, GXO, CATL ×2) or **independent press reporting** (*WSJ*, *Fortune*, *Forbes*, *Economic Observer*, *Xinhua*).
- **4 of 8** (`C032` BMW, `C001` Longcheer, `C096` China Post, `C087` Schaeffler) have **critical third-party journalism or 6-day public livestreams** that independently verified physical production work while exposing caveats (1 robot at BMW, maintenance team/collisions at Longcheer, 6-month support at China Post).
- **0 of 8** publish **third-party audited intervention logs** (which `milestone:the-blue-collar-shift` already gates on).

---

## 5. Position Block

- **Champion: `fable-5` (merged with `argon-6`: Cumulative Verified `(GP Platform, Named Customer)` Production Deployments — `8` incl. `C007` / `7` humanoid, with `1 ended` noted).**
  - *Drop-condition:* Drop to `astra-5` (`7` / `6` customers) if the owner prefers one count per customer organization; drop to `astra-2` (`unknown`) if the owner requires audited intervention logs before counting any deployment.
- **Compatible co-picks (≤ 2):**
  1. **`astra-2`'s truthfulness clause** in the KPI label (*"Economy-wide labor share: not yet measurable"*).
  2. **`argon-2` precursor records** (tagged *"vendor/media-reported"*) as milestone context.
- **Dead items:** `fable-4` (1/7 instance agreement); `argon-6` workflow-key variant (merged into `fable-5`); `argon-1`, `fable-1`, `astra-1` (transfer judgments + cost); `fable-2` (citation contamination); `fable-3` (60h schedule); `argon-3/4/5` (withdrawn); `astra-3/4` (conceded).
- **Open cruxes for owner:** (1) `fable-5` (`platform × customer`, `8`/`7`) vs `astra-5` (`customer org`, `7`/`6`) vs `astra-2` (`unknown`); (2) Stationary VLA dual-arm (`C007` Dyna) included (`8`) or humanoid/mobile-manipulator only (`7`).

### Champion Pitch (`fable-5`, ≤ 80 words)
`fable-5` tracks the **count of verified `(GP platform, named customer)` production deployments** in our ledger where an autonomous GP robot performs a concrete workplace job (`8` today incl. Dyna/DTF, `7` humanoid-only, `1` marked ended; rising from `1` in 2024 to `3` in 2025 to `8` in 2026-Q3). In our 3-lab blind test, this was the **only** metric with 100% inter-rater agreement (7/7 humanoid, 8/8 with `C007`), requiring zero LLM pipeline, zero O*NET transfer rules, and `<5 min/quarter`.

### Strongest Objection to `fable-5` (Stated Fairly)
Counting documented `(platform, customer)` deployments measures the **breadth of commercial pilot/production adoption**, not the volume of human labor displaced or audited intervention-free autonomy (`0 of 8` disclose audited intervention logs, and a 1-robot trial ticks the counter the same as a 100-robot fleet).
