# Board memo — Robots/Hardware KPI (2026-10-17)

Seats: **fable** (anthropic/claude-fable-5-1), **astra** (openai-codex/gpt-6-astra), **argon**
(openrouter/google/gemini-4-argon); all three participated in every phase (phase 1 + 5 debate
rounds, the cap). Shape: *decide*. Files: `items/<seat>.md`, `rounds/NN-<seat>.md`,
`rounds/02-*-mapping.csv`.

**Short answer to the charter's second half:** the O*NET capability-coverage approach did not
survive. All three seats ended up treating it as dead as a KPI (unidentifiable transfer
judgments). A literal "no-transfer" re-mapping onto Anthropic's task instances also failed a
blind 3-lab reproducibility test. The thing that *was* reproducible is the list of verified
named-customer GP deployments. The board splits on whether to publish a count of that list
(fable, argon) or no KPI at all (astra).

## Bottom line — finalists

### Fork A: fable-5 — cumulative count of verified (vendor, customer-org) GP production deployments
*Champion: fable, argon (argon-6 merged into it by mutual agreement in round 4).*

- **Number today:** **8** (7 if stationary dual-arm Dyna/Din Tai Fung is excluded). 1 of them is
  marked ended (Figure/BMW). Roster: Agility/GXO, Agility/Schaeffler, Figure/BMW (ended),
  Dyna/Din Tai Fung, Spirit AI (Xiaomo)/CATL, Galbot/CATL, AgiBot/Longcheer, Robotera/China Post.
- **History:** dated by the ledger `published` date of the first qualifying event.
  0 (2024) → 1 (2025-Q2) → 3 (end-2025) → 4 (2026-Q1) → 7 (2026-Q2) → 8 (2026-Q3). argon derived
  it and astra independently reproduced it. With a one-time source-dated backfill of GXO's
  2024-06-27 release, 2024 becomes 1.
- **Production:** the gather pipeline already verifies ledger events. A new (vendor, customer)
  pair adds 1. Estimated cost ~zero, under 5 min/quarter. No O*NET, no sampling, no LLM judging
  stage.
- **Rules it needs:** (1) GP gate per the owner's definition; (2) a named external customer's
  production flow, so a vendor's own factory doesn't count (Xiaomi); (3) parent-company
  normalisation (CATL bases, China Post branches); (4) cumulative headline with ended runs
  annotated, because "active" can only ever be disproved; (5) label: "autonomy as reported;
  economy-wide labor share not yet measurable".
- **Pitch (fable, verbatim):** "Count the distinct (vendor, customer) pairs where a
  ledger-verified event documents a general-purpose robot doing a named customer's production
  work, autonomously as reported. Today 8 (7 active). No taxonomy, no transfer rules, no
  sampling, no LLM judgment: three seats produced the same list independently. Updated by the
  gather pipeline at ~zero cost; history fixed by publication date so it never rewrites itself.
  The smallest number that is both true and about what the section is for."
- **Downside (fable's own statement of the strongest objection):** "Every entry's autonomy is
  vendor- or customer-reported — none has audited intervention logs — so the count can rise on
  PR alone; and eight is a case register with a trend, not a measurement of work done."
  argon adds that 1 robot counts the same as 100. fable adds that there is no tier-1/2 pace
  benchmark, so for its first years the status can only be judged against its own short trend.
- **Tags:**
  - `[Disputed: trend mixes real adoption with ledger discovery coverage — astra's objection,
    ruled *sustained* by argon as a seed-backfill requirement, not fatal]`
  - `[Disputed: documentary roster, not verified autonomous work — astra; conceded by the
    authors as scope; the label must say "as reported"]`
- **Premise audit:** the decisive premise is that the deployment list is reproducible. It was
  checked by all three seats in a blind mapping test (`rounds/02-*-mapping.csv`):
  - 7 entries were admitted unanimously, the 16 rejects were unanimous, and the 24th (C007,
    stationary) is a declared scope crux.
  - That does **not** establish autonomy. 0/8 have audited intervention logs. 4/8 have
    independent deployment reporting (Xinhua, WSJ, Economic Observer, Fortune/Forbes), 2/8 only
    a customer statement (CATL ×2), and 2/8 are vendor-only (GXO, DTF). fable conceded these
    are deployment reporting, not checks of control authority.
  - It also does not establish that rosters stay reproducible on future cases. astra: the test
    ran on catalogue rows that were already grouped, so it did not test how new aliases would
    be resolved.
  - Note: argon's pitch says "100% inter-rater agreement". That holds for the 7 humanoid
    entries, not for C007.

### Fork B: astra-2 — no KPI; declare the measurement gap and keep milestones
*Champion: astra.*

- **Dashboard:** "Autonomous GP work: not yet measurable". Status stays `unknown`. A
  provisional "0/4 GP milestones" count is allowed for navigation only, never as "% solved".
  The existing ledger and milestone assessments stay as they are. ~1 h/quarter.
- **Pitch (astra, verbatim):** "Keep the verified evidence and clearly scoped milestone
  observations; say that general-purpose autonomous work lacks a trustworthy recurring
  measure. Our independent test defeated the sophisticated coverage index. A transparent
  missing KPI is preferable to converting reporting frequency into technological progress.
  Adopt a documentation count only if its narrower meaning is explicitly wanted."
- **Downside (astra's own statement of the strongest objection):** "This sacrifices the requested
  single numeric series when a simple, inspectable customer or vendor/customer roster could
  already provide a useful commercialization signal."
- **Premise audit:** the decisive premise is that RUBRIC §3 permits `unknown`. argon checked it
  (non-author) against RUBRIC.md and `assessments/robots-hardware.jsonl`: confirmed legal today.
  The check does not establish a trend-scorable series. It openly relaxes the charter's
  one-KPI requirement.
- **Tags:** none. argon's round-1 "fatal vs RUBRIC §3" objection was refuted by argon's own
  round-3 audit.

### Fork C: astra-5 — count of distinct named customer organizations ever documented
*Co-pick of astra only, as an optional fallback; nobody champions it.*

- **Number today:** 7 (6 without DTF); CATL counts once. History by published date:
  0 → 1 → 3 → 4 → 6 → 7.
- **Premise audit:** fable and argon checked the premise that a named customer organization is
  a judgment-free unit. It holds given a parent-company rule and a deployer ≠ customer rule.
- **Tags:** `[Disputed: saturates on multi-vendor customers — a second vendor/job at CATL adds
  0; raised by fable and argon, accepted by astra as deliberate scope ("unsuitable as a
  comprehensive technology-progress index")]`

### Slate items compatible with fable-5 (co-picked by all three seats)

- **astra-2's truthfulness clause in the KPI label:** "economy-wide labor share: not yet
  measurable; autonomy as reported". fable and argon co-picked it; it is astra's own text.
- **argon-2 precursor records** as label/milestone context, not scored:
  - largest single-site section fleet: 8 AgiBot G2 at Longcheer, with a human maintenance team
    on the floor;
  - Figure Helix 2.5: 56% full-task success in 30 unseen homes, vendor-administered;
  - Dyna: 24 h zero-intervention run, vendor-claimed, site undisclosed (not Din Tai Fung).
  - Audits: fable and astra (non-authors) re-read the sources. They are records reported by
    vendors or media, consistently transcribed. The 8-unit fleet is **not** evidence of
    intervention-free operation. Must carry a "vendor/media-reported" tag.

## Cruxes for the user (preference only)

1. **Should a roster of documented deployments occupy the KPI slot, with autonomy as reported?**
   - If you'd rather have an honest small trend number than an empty slot → **fable-5**.
   - If you won't count deployments whose autonomy rests on vendor/customer/press statements
     without audited intervention data → **astra-2** (`unknown`).
   - Both fable-5 seats name exactly this as their drop-condition.
2. **Technology progress or buyer adoption?**
   - If a second robot vendor winning a different job at CATL should register → **fable-5**,
     keyed by (vendor, customer).
   - If each buyer should count at most once → **astra-5**.
3. **Is a stationary, software-redeployable dual-arm generalist (Dyna/DTF) "general-purpose"?**
   This is the owner's definition, which says "humanoids, mobile manipulators". In → 8; out → 7.
4. **Evidentiary bar for vendor-only deployments (GXO, DTF).** Including them is the default
   above; excluding them today gives 6 (DTF is also C007).

Factual cruxes, settled in the debate (not for the user):

- **Instance-level O*NET mapping is not reproducible.** Pairwise agreement was 1/7, 1/7 and 2/7,
  and the three independent tables gave counts of 5, 7 and 3. The deployment-level list is
  reproducible.
- **argon's "345× PPS bug" is not a bug.** It is the Hansen–Hurwitz inverse-probability weight
  working as designed, so the cost is variance, not bias. fable and astra both showed this,
  argon conceded, and the actual factor is ~258× with 20 stratum-A draws. astra noted that the
  provenance of the subset in `v2_selection.json` is undocumented.
- **GXO's first published date** in the current ledger is 2025-11-20 (L185, `published_basis
  source`). L101 is `seen` 2026-01-04. All three seats checked.
- **Blue Collar Shift** requires a *disclosed average intervention rate*, not specifically
  third-party audited logs (astra's correction of argon).
- **"Active" status is unobservable.** Deployments are only ever reported ended (BMW, Forbes
  2026-10-07). All seats converged on a cumulative headline with ended runs annotated.

## Killed

| Item | Fatal flaw | Raised by |
|---|---|---|
| fable-1, argon-1, astra-1 (v5/v5b coverage, incl. human-adjudicated variant) | The level rests on unidentifiable transfer judgments (Galbot bins → tote-to-hopper: Opus 7/7 vs Luna 1/7) plus invented sub-step weights. Adjudication adds accountability, not validity. | fable (phase 1), argon, astra; conceded by all authors (fable-1 kept only as a research note) |
| fable-2 (Anthropic index, GP-filtered) | The filter cannot remove co-cited contamination. Examples: Digit/GXO cited for probation officers' drug tests; tiers from non-GP co-cited robots. No cadence. | argon, astra; conceded |
| fable-3 (longest witnessed production run, scored) | The 60 h baseline was a livestream schedule with collisions, a maintenance team and unquantified interventions (L209–210). Endurance ≠ METR-like horizon. | argon, astra; conceded |
| fable-4 (literal census on rx_tasks instances) | Instance mapping is not reproducible: 1/7 pairwise agreement in the blind 3-seat test. | astra (counterexamples), chair's comparison; conceded by fable via his own drop-condition |
| argon-3 (task-level, parity-discounted share) | Whole-task crediting steps by 1.22% from one deployment. Slice ≠ task. The 0.3 default parity discount is arbitrary. | fable, astra; conceded |
| argon-4 (audited revenue ÷ wage) | Wrong estimand: trial hardware with zero autonomous output raises it. UBTECH publishes no end-use split, so the "$28M" was an assumption. | astra, fable; conceded |
| argon-5 (hours bracket as scored series) | Neither endpoint bounds the outcome: cumulative operating hours ≠ autonomous annual hours, and the upper bound is assumptions multiplied together. Midpoint arithmetic error: √(17.5×1800)=177.5, not 110. | astra, fable; conceded |
| argon-6 (task-keyed workflow count, "active") | The "physical task" key reintroduces boundary calls (GXO 2 activities, Longcheer ">4 workflows"). "Active" is unobservable. | astra (audit), fable; conceded and merged into fable-5 |
| astra-3 (Dyna/DTF acceptance-test sentinel) | Commercial sufficiency already reached (106%), so the series may never move. Needs private customer logs. | fable, argon; conceded as a headline |
| astra-4 (software-redeployment certificates) | Zero series with no reporting partners; not pace-scorable. | argon, fable; conceded |

## Dissent

Strongest unresolved objection to the majority champion (fable-5), in astra's words:

- "A transparent missing KPI is preferable to converting reporting frequency into technological
  progress."
- "That backfill would change the historical series, demonstrating why publication dating
  alone does not eliminate discovery revisions. Frozen published bulletins and a reconstructed
  historical chart are different objects."
- "Patched vendor/customer fable-5 is a viable documentary alternative, … not verified
  autonomous-work measurement."

## Next step (cheapest)

1. **Owner rules on crux 1** (count reported-autonomy deployments, or not). It is both
   champions' drop-condition and costs nothing.
2. **If fable-5 / astra-5: a 30-min reproducibility check on the untested part.**
   - Have a fresh agent and one seat derive the (vendor, customer-org) roster and its
     published-date history **directly from `data/ledger/events/robots-hardware.jsonl`**,
     without the pre-grouped catalogue.
   - Use the five written rules above.
   - Any roster difference triggers fable-5's own drop-condition ("two raters produce different
     (vendor, customer) rosters from the same ledger").
3. **Do the one-time backfill at registration.** Ingest a source-dated record for each seed
   pair's earliest primary announcement (e.g. GXO 2024-06-27), so the registered history isn't
   a ledger-coverage artifact. Then go prospective.

*Process note:* seats ran as side agents at nesting depth 3. To allow this, the chair raised
`MAX_AGENT_DEPTH` 2→3 in `pi-side-agents` (commit `edb041d`, unpushed); the earlier subagent
attempt was aborted.
