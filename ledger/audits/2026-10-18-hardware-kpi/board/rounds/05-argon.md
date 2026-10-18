# Round 5 — Final (`argon`)

## 1. Requested Ruling & Key Alignment

- **Ruling on `astra`'s Round 4 objection to `fable-5` (*"even publication-dated growth mixes real adoption with our discovery/ledger coverage (2024 = 0 is a coverage artifact)"*):** **Sustained (as a seed-backfill requirement, not a fatal flaw):** `2024 = 0` on the current ledger is indeed a `published_basis: "seen"` / coverage artifact on `L101` (`published: "2026-01-04"`), so `fable-5`'s series mixes adoption with ledger discovery unless the 8 seed deployments' earliest primary announcement dates (e.g. GXO `2024-06-27`) are backfilled with `published_basis: "source"` once at setup.
- **Alignment on `(vendor, customer organization)` key:** We adopt `fable`'s Round 4 patch replacing `(GP platform, named customer)` with **`(vendor, customer organization)`**, eliminating model-version boundary calls (`Digit 4 vs 5`, `Figure 02 vs 03`, `DYNA-1 vs 2`).

## 2. GXO First-Documentation Date Check (`robots-hardware.jsonl`)

- **`L101` (`2025-01-01-digit-gxo-raas-deployment-rv`):** `date: "2025"`, `published: "2026-01-04"`, `published_basis: "seen"`, `status: "verified"` (claim states RaaS deployment only, not the physical task; `fable`'s "Jan 2025" read the `id` prefix `2025-01-01`, not `published`).
- **`L185` (`2025-11-20-digit-100k-totes-gxo-r2`):** `date: "2025-11-20"`, `published: "2025-11-20"`, `published_basis: "source"`, `status: "corrected"` (states AMR-to-conveyor tote transfer and floor stacking).
- **Result under `published`-date rule:** On the unmodified ledger today, GXO's first qualifying `published` date is **`2025-11-20` (`L185`)**, yielding **`0 (2024) → 1 (2025-Q2) → 3 (2025-Q4) → 4 (2026-Q1) → 7 (2026-Q2) → 8 (2026-Q3)`** (`7` humanoid-only). Superseding `L101` with GXO's dated `2024-06-27` investor release (`published_basis: "source"`) moves GXO to `2024-06-27` (`1 (2024) → 2 (2025-Q2) → 3 (2025-Q4) → 4 (2026-Q1) → 7 (2026-Q2) → 8 (2026-Q3)`).

---

## 3. Final Position Block

- **Champion: `fable-5` (merged with `argon-6`: Cumulative Verified `(Vendor, Customer Organization)` GP Production Deployments — `8` incl. `C007` DTF / `7` humanoid, `1 ended` annotated).**
  - *Drop-condition:* Drop to `astra-5` (`7` / `6` customers) if the owner wants one count per buyer organization; drop to `astra-2` (`unknown`) if the owner refuses to count deployments whose autonomy is customer/vendor/press-reported without audited intervention logs.
- **Compatible co-picks (≤ 2):**
  1. **`astra-2` truthfulness clause** in the KPI label (*"Economy-wide labor share: not yet measurable; autonomy as reported"*).
  2. **`argon-2` precursor records** (tagged *"vendor/media-reported"*) as milestone context.
- **Dead items:** `fable-4` (instance mapping 1/7 agreement); `argon-6` task-keyed variant (merged into `fable-5`); `argon-1`, `fable-1`, `astra-1` (unidentifiable transfer judgments + cost); `fable-2` (citation contamination); `fable-3` scored (no intervention logs); `argon-3/4/5` (withdrawn); `astra-3/4` (withdrawn).
- **Open cruxes for owner:** (1) `fable-5` (`vendor × customer`, `8`/`7`) vs `astra-5` (`customer org`, `7`/`6`) vs `astra-2` (`unknown`); (2) Stationary VLA dual-arm (`C007` Dyna) in (`8`) or humanoid/mobile-manipulator only (`7`).

### Champion Pitch (`fable-5`, ≤ 80 words)
`fable-5` tracks the **cumulative count of verified `(vendor, customer organization)` production deployments** in our ledger where a general-purpose robot performs a named customer's real workplace job, autonomously as reported (`8` today incl. Dyna/DTF, `7` humanoid-only, `1` marked ended). In our 3-lab blind test, this was the **only** metric with 100% inter-rater agreement, requiring zero LLM pipeline, zero O*NET transfer rules, and `<5 min/quarter`.

### Strongest Objection to `fable-5`
Every entry's autonomy is customer-, vendor-, or press-reported (`0 of 8` publish audited intervention logs), and counting documented `(vendor, customer)` relationships measures commercial deployment breadth rather than total labor hours displaced (`1` robot counts the same as `100`) or completeness of our ledger's historical search coverage.
