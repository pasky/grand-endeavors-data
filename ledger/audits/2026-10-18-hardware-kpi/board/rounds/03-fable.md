# Round 3 — fable

## Concession: fable-4's instance layer is dead
My drop-condition was ">2 of 8 disagree on the instance"; the result is 1/7 pairwise agreement.
astra's counterexamples (10781/4 bundles dock hauling; 12119/0 bundles sort/count; 14587/2 says
"boxes vary") are correct: "whole-instance" semantics are not shared across raters; argon's "2–3 equally
literal instances per deployment" is the same fact from the other side. The Anthropic instance
taxonomy adds noise to a count, nothing else. **fable-4 as specified is
dead** (named flaw: rx_tasks instance mapping not reproducible). Accepted astra's wording fix: Dyna's
24-h site is *undisclosed*, not "lab".

What the test *did* establish: the deployment list is reproducible — 7/8 unanimous, the 8th a
declared crux. Build on that.

## Fork: fable-5 — Verified GP customer deployments (platform × customer), no taxonomy
**What.** Count of distinct (GP platform, named customer) pairs for which a verified/corrected
ledger event describes the production work the robot does autonomously. Dedup by named
entities only — the one step all three seats performed identically. No O*NET, SOC or
"workflow" boundary. Label: list of the pairs, ended ones marked; astra-2's clause "economy-wide
labor share: not yet measurable".
**Today (ledger dates):** Digit/GXO, Digit/Schaeffler, Figure/BMW (ended 2025-11), Dyna/Din Tai
Fung, Xiaomo/CATL, Galbot/CATL, AgiBot/Longcheer, Robotera/China Post = **8 cumulative, 7
active**. History: end-2024 **1** (GXO), end-2025 **5** (+BMW, DTF Jun, China Post Nov arrival,
CATL Dec), 2026-Q3 **8**.
**Why over argon-6.** argon's (SOC, workflow) dedup re-imports the 53-7062/53-7063 cliff as a
dedup key, and "workflow" is itself a boundary: AgiBot says Longcheer spans ">4 production
workflows" (`2026-06-29`), Robotera has "10+ logistics centres" (`2026-05-31`). Platform×customer
makes both 1 and needs no decision. argon: drop SOC and argon-6 = fable-5.
**Fail.** Vendor-only sources (GXO rests on agilityrobotics.com, ledger-verified as *accurately
reported*); name-drop lists don't qualify (Agility's "Amazon, Toyota" in `2026-09-15` describe
no work → excluded, a crisp but real gate); "active" = "not reported ended" (biased up →
headline cumulative, ended annotated); C007 crux unchanged; small count, PR-paced.

## Non-author premise audits
**argon-6** (deployment list reproducible; dedup judgment-free): first half *established* by the
three tables; second half *not* — SOC and "workflow" are judgments (above). "Active" is only
ever disproved (BMW/Forbes), never proved.
**argon-2 records** (sources read):
- *Single-site fleet 8 units*: Xinhua `2026-06-28` (verified) — 8 G2 on one real test section,
  6 days × 10 h, public livestream. Establishes concurrent fleet size on a production section;
  **not** intervention-free operation (same source: collisions, lidar drops, maintenance team).
  Fleet-size record, not autonomy evidence.
- *56% Helix 2.5 / 30 homes*: figure.ai `2026-09-17` (verified = accurately transcribed).
  Vendor-run evaluation, no third party, no per-home log: a *vendor-reported* number.
- *24 h zero interventions*: PR Newswire `2025-04-29` (corrected); site and log undisclosed.
  Vendor claim.
  → argon-2 = vendor-reported records, consistently transcribed. Label context with a
  "vendor-reported" tag; not a scored series.

## astra-2 vs footprint: the factual residue, one line each
- Factual, settled: the count is not labor displaced; autonomy is vendor-claimed (third-party
  witness in 4 of 8: Xinhua, WSJ, Economic Observer, Forbes/Fortune).
- Factual, now evidenced: a deployment-level list is reproducible (7/8); an instance-level one is
  not (1/7).
- Preference: whether a reproducible footprint count merits the KPI slot vs `unknown` (astra:
  RUBRIC permits `unknown`, doesn't command it). Owner decides.

## Pressed
- **astra**: astra-3 — "not a mathematical ceiling" accepted; but the requirement is met, so
  what moves the series next quarter? If nothing, it's a milestone.
- **argon**: argon-6 history "1 → 3 → 6" — your 2025 value omits DTF (Jun 2025, verified
  `2026-08-27`) and China Post's Nov-2025 arrival; is 3 a gate choice or an omission?

## Position
- **Champion: fable-5** (switched from fable-4; reason: drop-condition triggered, 1/7 instance
  agreement). Drop-condition: a seat shows two raters producing different (platform, customer)
  lists from the same 8 admitted entries, or the owner wants an economy-wide quantity.
- **Co-picks:** astra-2's clause in the label; argon-2 records in the label with
  "vendor-reported" tags.
- **Dead:** fable-4 (instance mapping irreproducible); fable-1/argon-1/astra-1 (definitional
  transfer; cost); fable-2; fable-3 as scored; argon-3/4/5 (conceded by author); astra-3
  (sufficiency reached); astra-4.
- **Cruxes:** C007 in/out; cumulative vs active; vendor-only sourcing (GXO); multi-site vendors
  (Robotera) — one pair or one per verified site.
