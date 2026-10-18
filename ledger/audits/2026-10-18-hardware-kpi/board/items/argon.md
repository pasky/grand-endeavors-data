# Robots/Hardware KPI — Options (`argon`)

### `argon-1` (Baseline, simplified): Frozen-Panel O*NET Sub-Step Coverage (`v5b` Ensemble)
- **What:** Share of US physical work hours (`rx_tasks.csv` × OEWS May 2024 employment, ~116B h/yr) covered by autonomous GP robots in our capability catalogue (`catalog_v1.json`, 98 entries). **Today:** **0.19% incl. demos** (`0.11%` gpt-6-luna, `0.32%` claude-opus-5-5; **~0.08% deployed/pilot**). Simplifies `v5`/`v5b`: freeze a 150-task PPS panel (~600 sub-steps) once; filter `(sub-step, entry)` pairs mechanically by `entry.env >= instance.setting_tier`; judge only *new* quarterly catalogue entries one pair per call (removing `v5`'s 5/6 vs 1/7 batching bias) with 1 Opus + 1 Luna call/pair (`~$3/quarter`, 10 min, quarterly).
- **Why:** Broad capability coverage over a national labor denominator with incremental updates.
- **How it could fail:** Synthetic LLM artifact: the non-zero level hinges on ~15 borderline cross-occupation transfer calls where Opus and Luna disagree 3× (e.g., Galbot carrying battery bins at CATL covering a bakery hopper), sub-step weights are LLM-invented, and model updates drift the series.

### `argon-2` (Reframe / Zero-Pipeline): Milestone-Precursor Records Only (Retire Section KPI)
- **What:** Set `robots-hardware` `kpi:` to `null` until an official survey (Census ABS/BTOS) tracks autonomous GP robot hours, and surface **four deterministic milestone-precursor series** from verified ledger events (mirroring `robots-software`'s precursor records):
  1. `gp-continuous-shift-max`: longest verified continuous autonomous workplace run (**24 h** Dyna Din Tai Fung / **200 h** Figure HQ sort),
  2. `gp-single-site-fleet-max`: largest verified concurrent autonomous GP fleet on one production section (**8 units**, AgiBot G2 at Longcheer; Figure/BMW corrected to **1 unit** active at a time by Forbes Oct 2026),
  3. `gp-unseen-home-success-max`: zero-shot multi-task success across ≥20 unseen homes (**56%**, Figure Helix 2.5 in 30 homes),
  4. `robotaxi-weekly-paid-rides-max`: peak weekly paid driverless rides (**500,000/wk**, Waymo).
- **Why:** Zero arbitrary rules, `$0` cost, 0 min extra runtime (event-driven during `gather.sh`), 100% grounded in verified ledger events, and each metric directly drives a milestone ETA under `RUBRIC.md`.
- **How it could fail:** Leaves the overview KPI slot empty and steps up discretely on showcase records rather than measuring aggregate economic diffusion.

### `argon-3` `[novel]`: Inverted Direct O*NET Task Footprint (`gp-direct-onet-work-share`)
- **What:** Invert `v5`: instead of sampling 30 random O*NET tasks and asking LLMs whether a battery-factory robot could work in a bakery, map each verified `deployed`/`pilot` GP capability in the ledger (**24 entries** today) directly to the **1–2 exact O*NET `task_id`s of the workplace job actually performed** (Digit/GXO → `53-7062.00` freight/tote moving; Dyna-2/Din Tai Fung → linen folding; AgiBot G2/Longcheer → electronics test loading; Robotera/China Post → parcel sorting), discounted by verified human-parity `min(1.0, speed_vs_human × reliability)` (default `0.3` when undisclosed, per UBTech's 30–50% disclosure) across the **full census of 7,594 O*NET physical tasks**. **Today:** **0.14% of US physical work hours** (**0.28%** unadjusted across 18 directly demonstrated O*NET tasks; up from **0.02%** in 2024-H1 and **0.07%** in 2025-H2).
- **Why:** Eliminates both fatal flaws of `v5`: **zero sampling error** (full 7,594-task census) and **zero speculative cross-domain transfer** (a robot only credits the exact occupation/task it actually worked in). Next quarter's update tags only **2–5 new `deployed`/`pilot` ledger events** (`<$0.20/quarter`, 1 min, quarterly), checked deterministically by `ledger.py`.
- **How it could fail:** O*NET task statements are broader than single workstation duties (tote-to-conveyor is one slice of "move freight, stock, or other materials"), overstating coverage unless paired with a within-task breadth cap.

### `argon-4` `[novel]`: Audited Commercial GP Robot Revenue in Wage Equivalents (`gp-audited-commercial-fte-equiv`)
- **What:** Customer-paid **industrial/commercial** GP robot revenue from audited public filings (excluding research, education, and entertainment/display via disclosed end-use splits), divided by US median production/material-moving annual compensation ($45,000/yr, BLS OEWS) to yield **Paid Commercial Robot-Years**. Sources: UBTECH (HKEX:9880, 2025 full-size humanoid revenue RMB 820.6M; H1 2026 RMB 590M), Unitree (STAR IPO: RMB 867.8M × **9.01% industrial** = RMB 78.2M), Agility (SEC S-4: $1.8M). **Today:** **~620 FTE-years** (`~$28M/yr` verified industrial revenue ÷ $45k, up from **~110 FTE-years** in 2024; **~2,800 FTE-years** unadjusted).
- **Why:** Press releases lie (BMW ran 1 Figure robot; Musk admitted 0 useful Optimus work), whereas falsifying HKEX/STAR/SEC revenue tables is a securities felony. Zero LLM judgment; semi-annual/quarterly filing cadence (`<$0.50/quarter`, 5 min).
- **How it could fail:** Misses private Western vendors (Figure, Apptronik) until IPO and counts hardware bought for factory trials before full autonomy is proven.

### `argon-5`: Disclosed Autonomous Work-Hours Bracket (`[Verified Hours, Shipments × Productive Share]`)
- **What:** Two paired ledger series in FTE-years (2,000 h/yr):
  - **Lower bound (`gp-verified-work-fte`)**: annualized customer-site autonomous GP robot hours from verified ledger disclosures (**~17.5 FTE-years** = ~35,000 h/yr today: Agility Digit 65,000h cumulative over ~2.5 yrs + Figure/BMW 1,250h + AgiBot Longcheer + Dyna Din Tai Fung + Robotera China Post).
  - **Upper bound (`gp-shipment-work-fte-cap`)**: global humanoid shipments (Omdia/IDC median **15,500** in 2025; **~40,000/yr** in H1 2026) × disclosed industrial share (**9.0%**, Unitree filing; IDC `<15%`) × 0.5 FTE-yr/unit = **700 FTE-years** (2025) → **1,800 FTE-years** (2026-H1). **Today (geometric midpoint):** **~110 FTE-years** (`[17.5, 1,800] FTE-yr`).
- **Why:** Directly tracks human labor taken over while bounding the 100× disclosure gap. Refreshed quarterly from ledger events (`<$0.50`, 2 min).
- **How it could fail:** Lower bound jumps when vendors sporadically publish cumulative hour milestones; upper bound relies on fixed utilization assumptions.

---

## Ranking and Preference

1. **`argon-3` (`[novel]` Inverted Direct O*NET Task Footprint) — Preferred capability KPI:** Reproducible % of US physical work (`0.14%` today) with **zero sampling error**, **zero speculative transfer rules**, and `O(new events)` maintenance.
2. **`argon-5` (Disclosed Autonomous Work-Hours Bracket) — Preferred outcome KPI:** Bounds human labor taken over (`~110 FTE-yr` midpoint, `[17.5, 1,800]` bracket). *(Best hybrid: `argon-3` as primary KPI + `argon-5` lower bound as companion tile.)*
3. **`argon-4` (`[novel]` Audited Commercial Revenue in FTE-Equivalents):** Hardest anti-PR verification via securities filings (`~620 FTE-yr`).
4. **`argon-2` (Milestone-Precursor Records Only):** Best zero-pipeline fallback.
5. **`argon-1` (Simplified `v5b` Coverage Panel):** Dominated by `argon-3` due to transfer disagreement and sampling noise.
