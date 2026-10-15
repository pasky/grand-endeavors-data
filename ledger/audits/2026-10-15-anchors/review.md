# External forecast anchor review — 2026-10-15

## Decision

Reviewed all **16 supplied candidates** and **5 additional Manifold candidates** selected from live search: **2 weaker, 16 reject, 3 unverifiable; no same or stronger anchors**. Both accepted anchors concern **fusion/the-first-watt**, so only **1 of 20 milestones** has coverage, and only by lower-bound events. Approval here is semantic and evidentiary, **not permission to launch a stored/redisplayed weekly feed**.

## Method

- Read the complete binding framework at `/home/pasky/projects/hai/grand-endeavors-agent-worktree-0005/framework.yaml`, including every `details:` and `assumes:` clause, all four candidate JSON files and summaries, and `api.md`.
- Fetched every supplied Manifold candidate and each of the five additions with `curl https://api.manifold.markets/v0/market/<id>`. Read the full `textDescription`, including embedded creator updates, and checked title, closeTime, isResolved, outcomeType, probability and uniqueBettorCount. All 18 fetched Manifold parent markets are unresolved with closing dates after today; the added multi-answer Coffee Test market has two already-resolved past answers, which are not prospective anchors.
- Tested both implications independently. For weaker, our milestone by date D must imply the market event by D, hence **P(ours by D) ≤ P(market YES)** and the external event date is a lower bound on ours. For stronger, the market event must imply ours by D, hence **P(ours by D) ≥ P(market YES)** and its event date is an upper bound. A plausible technological sequence, shared subject or usually-correlated result is insufficient.
- Policy-conditioned capability milestones are not interchangeable with unconditional markets on actual journal policy. Moon-or-Mars cannot be narrowed to Moon for a weaker bound; a high output threshold cannot compensate for insufficient duration; an aggregate disease outcome need not improve every subtype. The metastatic-cancer clause is explanatory, **not an additional survival test**.
- Loaded all three Metaculus question pages live through Jina. Forecasts were visible, but complete resolution criteria were not. A no-cache/query retry for 11933 still lacked full criteria and its current forecaster count; direct access returned 403. A fresh unauthenticated posts/45167 request also returned 403. All three receive **unverifiable**, with the relation that would follow from the visible text stated separately; API inaccessibility is not itself used as proof that their events differ.
- Brief anonymous Manifold searches used `search-markets?term=...&limit=40` for fusion, lunar, robotaxi, coffee, Nature, manufacturing and greenhouse. An initial multiword commercial-fusion search returned 503; the subsequent fusion search succeeded. Five promising results were promoted to full-market review and are included even where rejected; unpromoted search hits are not claimed as verified candidate anchors. Search was deliberately limited, not exhaustive.
- Followed the engineering-breakeven market’s linked [definition](https://en.wikipedia.org/wiki/Fusion_energy_gain_factor) to confirm that engineering breakeven is distinct from scientific gain and from economic profitability.

### Data conventions

`verdicts.json` is the authoritative list. Probabilities are raw current API values on a 0–1 scale, or the live page’s displayed binary percentage for Metaculus; they are not probability estimates for our event. Date questions and the multi-answer parent have `probability: null`, with visible date estimates or answer probabilities preserved separately. Parent-market bettor counts are not per-answer counts.

`thin` is true exactly when the verified count is below 20, not an automatic veto. Metaculus 11933 has `forecasters: null` and `thin: null`: the research claim of 24 was not exposed in either live extract and is not silently reused. The other two Metaculus pages visibly show 18 and 20 forecasters. Metaculus status/timestamps not independently exposed are also null, not guessed.

Deadlines refer to the event, not settlement or trading close. “Before 2029” becomes 2028-12-31; “before 1 January 2030” becomes 2029-12-31. A bare “by YEAR” is normalized to that year’s end where consistent with the market, with ambiguity called out. In particular, net-zero carbon “by 2060” closes on 2060-12-31, so the supplied 2059-12-31 deadline is not supported. The cancer-shift market retains a **nominal** 2030-12-31 deadline but is rejected in part because its 2035 close-date update leaves the event cutoff unclear. A date question or multi-answer parent has no single binary deadline; each Coffee Test answer records its own cutoff. Day-level dates do not authorize trading through the whole UTC day where a market closes earlier.

Raw fetched evidence is under `/tmp/ge-anchors/live/`; each verdict points to its evidence file and URL. Metaculus HTML extraction may be cached or incomplete and is not an authenticated aggregate feed. No repository was modified and no git add/commit was run.

## Accepted anchors

| Milestone | Anchor | Relation | Event deadline | Current YES | Bettors | Thin |
|---|---|---|---|---:|---:|---|
| `fusion/the-first-watt` | [pR0QngELPh](https://manifold.markets/GordanKnott/will-there-be-a-fusion-reactor-gene) — Will there be a fusion reactor generating electricity commercially by the end of 2035? | weaker | 2035-12-31 | 36.78% | 11 | yes |
| `fusion/the-first-watt` | [iuBCRicRjrIzUshZxq97](https://manifold.markets/BoltonBailey/will-any-fusion-reactor-project-dem-9695cf9c60e0) — Will any fusion reactor project demonstrate engineering breakeven before the end of 2040? | weaker | 2040-12-31 | 87.10% | 56 | no |

These supply only **P(First Watt by 2035-12-31) ≤ 36.78%** and **P(First Watt by 2040-12-31) ≤ 87.10%**, respectively, when treating the market quotes as external forecast constraints. Do not label either quote as our ETA probability, interpolate them into a same-event CDF, or infer a precise median ETA from them. The 2040 engineering-breakeven event is substantially easier than our sustained-commercial-export target, so the bound is loose.

Liquidity and freshness matter: the 2035 commercial market has only eleven bettors (about M$396 total volume). The 2040 engineering market has 56 bettors (about M$14,380 total volume), but its latest recorded bet is **2025-06-19**, so the live quote is stale in activity terms; collection does not mean recent updating. Keep an explicit stale-price warning and do not treat these two correlated fusion markets as independent votes.

## Per-milestone verdicts

### The Linux Kernel Patch — `robots-software/the-linux-kernel-patch`

**No reviewed candidate.** No candidate supplied or promoted from the brief search. A valid anchor must preserve the 10k+ diff and critical-infrastructure scope, with maintainer policy assumed away.

### The Nature Author — `robots-software/the-nature-author`

**UNVERIFIABLE — [metaculus 45167](https://www.metaculus.com/questions/45167/will-a-published-paper-list-an-ai-author-before-2030/): Will at least one paper published in Nature, Science, or Cell list an AI system as a formally credited author before January 1, 2030?**

Event deadline: 2029-12-31; 80.00% YES; forecasters/bettors: 18; thin: yes.

The live page shows 80% and 18 forecasters but omits the full resolution criteria, so verification is incomplete and API collection is unavailable. Any credited author in Nature, Science, or Cell would be weaker than actual primary-authored publication, but our binding assumes clause instead measures capability with the authorship-policy barrier removed. That capability does not imply real-world formal credit, while merely crediting an AI does not establish its independent conception, analysis and writing; thus the visible event would not bound the actual framework milestone.

**REJECT — [manifold t8UnRsQcOg](https://manifold.markets/KalvinMizzi/will-an-ai-system-be-credited-as-th): Will an AI system be credited as the lead author of a paper in Nature or Science before 1 January 2030?**

Event deadline: 2029-12-31; 31.75% YES; forecasters/bettors: 3; thin: yes.

The market requires actual first/lead/primary credit in a published Nature or Science paper but does not require the AI to originate the question, design and analyse the research, and write it without human intellectual contributions. Our milestone assumes away the journal-authorship ban, whereas this unconditional market can remain NO because of that policy even when the capability milestone is met. Conversely, editorial credit alone could produce YES without the required AI-only research; neither implication holds, and three bettors also make this exceptionally thin.

**REJECT — [manifold HNcseAG6s5KybMEMQNEt](https://manifold.markets/AmmonLam/will-a-paper-fully-created-by-ai-be) (review addition): Will a paper fully created by AI be accepted into Nature by 2030?**

Event deadline: 2030-12-31; 55.07% YES; forecasters/bettors: 28; thin: no.

Despite its promising title, the criteria describe a researcher using AI to invent research data and get a fabricated paper through Nature, followed by disclosure of the stunt. Acceptance of fraudulent AI-generated data does not establish the milestone’s independently AI-conceived and executed scientific research, while genuine qualifying work need not involve fabricated data or a subsequent confession. The market also excludes a Science-only success, so neither implication holds.

### The $10M Solopreneur — `robots-software/the-10m-solopreneur`

**REJECT — [manifold dgfhEfuYxLHFBpV4zsKX](https://manifold.markets/SimoneRomeo/will-there-be-a-oneperson-unicorn-b): Will there be a one-person unicorn by 2030?**

Event deadline: 2030-12-31; 51.62% YES; forecasters/bettors: 91; thin: no.

A billion-dollar valuation is neither necessary nor sufficient for $10M recurring revenue with less than ten total human operating hours per week averaged over a quarter. The market explicitly permits operating contractors and its 2026 update also accepts $1.8B in sales as valuation evidence, neither of which enforces recurring revenue or the oversight cap. Our qualifying business could be worth much less than $1B, while a qualifying unicorn could employ substantial contractor labour and have no recurring revenue.

### Robotaxi Saturation — `robots-hardware/robotaxi-saturation`

**No reviewed candidate.** No candidate supplied or promoted. Brief robotaxi search mainly returned named-company deployments, fleet rankings and resolved rollout questions, not peak in-service vehicle majority including ride-hail across a major metro; those titles were discovery results, not approved anchors.

### The Wozniak Test — `robots-hardware/the-wozniak-test`

**REJECT — [manifold 92RpIcOUn9](https://manifold.markets/AlanTuring/will-a-robot-be-created-that-is-cap-NLNg8RtPug): Will a robot be created that is capable of passing Steve Wozniak's "The Coffee Test" before 2029?**

Event deadline: 2028-12-31; 81.17% YES; forecasters/bettors: 27; thin: no.

An unfamiliar residential environment need not be randomly selected by someone other than the developer, and the market does not expressly rule out advance mapping/scanning or require independent verification rather than credible public reporting. Its added 20-minute limit also excludes a slower, independently verified, unaided success that satisfies our milestone. Thus a developer-selected demonstration could satisfy the market without our event, while our event need not satisfy the market; the mixed requirements prevent both weaker and stronger classifications.

**REJECT — [manifold ZA8292N5QC](https://manifold.markets/AlanTuring/will-a-robot-be-created-that-is-cap-l92Q228LNL): Will a robot be created that is capable of passing Steve Wozniak's "The Coffee Test" before 2027?**

Event deadline: 2026-12-31; 33.29% YES; forecasters/bettors: 23; thin: no.

This has the same substantive criteria as the 2029 Coffee Test market: an unfamiliar home and credible public documentation, not an explicitly developer-unselected, never-mapped home with independent verification. A selected-home demonstration can meet those criteria without meeting our test, while a valid but slower-than-20-minute success meets our test without meeting this market. Neither implication holds, and before 2027 means an event deadline of December 31, 2026, consistent with the live API close date.

**REJECT — [manifold 1Qu473ClJCmQqbyB4TH3](https://manifold.markets/OlegEterevsky/when-will-a-robot-reliably-pass-the) (review addition): When will a robot reliably pass "The Coffee Test"?**

Event deadline: not a single binary deadline; no single binary probability; forecasters/bettors: 91; thin: no.

Independent control and at least 50% success across three or more different homes improve the verification standard over the supplied Coffee Test markets. Nevertheless, the text does not require homes to be selected independently of the developer or forbid prior visiting, mapping or scanning, so several supervised successes in prepared homes could still fail our random-unseen-home event. Conversely, our single successful trial need not achieve the market’s repetition threshold; neither implication holds, and these are separate deadline answers rather than one categorical event-date distribution.

The live unresolved answer quotes are Before 2027 (2026-12-31): 20.40%; Before 2028 (2027-12-31): 58.57%; Before 2029 (2028-12-31): 60.09%; Before 2030 (2029-12-31): 69.46%. The before-2025 and before-2026 answers are already resolved NO; none of these answers is approved.

### The Fukushima Test — `robots-hardware/the-fukushima-test`

**No reviewed candidate.** No candidate supplied. Disaster repair must be autonomous and within human time limits; a realistic unscripted staged site is allowed.

### The Blue Collar Shift — `robots-hardware/the-blue-collar-shift`

**No reviewed candidate.** No candidate supplied. General-purpose robots must meet the 30 consecutive working-day, 8h+, 90% throughput and intervention restrictions, not merely be deployed at work.

### The Dark Line — `robots-hardware/the-dark-line`

**No reviewed candidate.** No candidate supplied. Purpose-built lights-out factories are not substitutes for a five-station general-purpose robotic line with maintenance, software-only changeover, throughput and no remote fault-fixing.

### The Deluge — `rockets/the-deluge`

**No reviewed candidate.** No candidate supplied. Launch counts and orbital objects do not establish 100,000 tonnes of cargo plus tanker propellant delivered in a year, excluding launch vehicles.

### The Export — `rockets/the-export`

**No reviewed candidate.** No candidate supplied or promoted. Recurring functional commercial sales from repeated space production, not a one-off batch or clinical-trial supply, are required.

### The Homestead — `rockets/the-homestead`

**REJECT — [manifold zdP3PSEkxlyzV9lpvN9D](https://manifold.markets/IsaacKing/will-there-be-a-lunar-base-by-the-e): Will there be a lunar base by the end of 2029?**

Event deadline: 2029-12-31; 9.94% YES; forecasters/bettors: 69; thin: no.

The market permits an unoccupied lunar installation merely habitable for a few weeks, so YES does not imply twelve continuously crewed months of locally supplied air, water and food. It is not a weaker bound either: our milestone explicitly allows Mars, which could qualify without any lunar base. It would be weaker only for a separately defined Moon-only branch, not for the binding Moon-or-Mars milestone.

### The First Watt — `fusion/the-first-watt`

**WEAKER — [manifold pR0QngELPh](https://manifold.markets/GordanKnott/will-there-be-a-fusion-reactor-gene): Will there be a fusion reactor generating electricity commercially by the end of 2035?**

Event deadline: 2035-12-31; 36.78% YES; forecasters/bettors: 11; thin: yes.

Three consecutive months of net electricity export under commercial operation to a public grid entails grid connection, commercial electricity sales and net-positive energy operation as required here. The market imposes no three-month minimum and does not require the same explicit net-electrical accounting, so a shorter commercial delivery can resolve YES before our milestone. It is a lower-bound event and supplies P(our milestone by 2035-12-31) ≤ 0.3678032316, not an estimate of our milestone probability; eleven bettors warrant a thin-market warning rather than automatic rejection.

**REJECT — [manifold jqEkQKsK0FxFNXDN0lBy](https://manifold.markets/MatthewBarnett/will-helion-energy-deliver-50-mw-of): Will Helion Energy deliver 50 MW of fusion-generated electricity to Microsoft before 2029?**

Event deadline: 2028-12-31; 11.44% YES; forecasters/bettors: 45; thin: no.

A different company, customer or lower-output plant could satisfy our milestone without Helion delivering 50 MW to Microsoft, so this is not weaker. It is not stronger either: the written criteria require neither three consecutive months of delivery nor net electrical export after all facility loads, defining gain instead against energy needed for the fusion reaction. A short 50 MW delivery meeting those criteria could therefore leave our sustained commercial-export milestone unmet.

**REJECT — [manifold 82qnCgcqPl](https://manifold.markets/Ronan/by-dec-31-2035-will-any-nuclear-fus): By Dec 31, 2035, will any nuclear fusion power plant have delivered at least 100 MW of net electrical power, 30 day ave.**

Event deadline: 2035-12-31; 10.57% YES; forecasters/bettors: 5; thin: yes.

A small plant exporting commercially for three months can meet our milestone without achieving this market’s 100 MWe average, so our event does not imply its YES. Conversely, 100 MWe averaged for just 30 days can satisfy the market without three consecutive months of export, and dedicated external end-users can qualify without a public grid. Neither the higher power threshold nor the explicit parasitic-load accounting repairs the duration and destination mismatches.

**REJECT — [manifold 6FErOD68cyROtqzCoUPk](https://manifold.markets/nick/will-fusion-power-be-commercially-a) (review addition): Will fusion power be commercially available by 2035?**

Event deadline: 2035-12-31; 29.40% YES; forecasters/bettors: 35; thin: no.

The live market has no description or operational resolution criteria beyond commercial availability. That could mean electricity sold to an offtaker, a purchasable reactor, or an economically viable power source, without specifying net output, public-grid delivery or duration. A loose electricity-sales reading would be weaker, but that interpretation is not secured by the market text, so it is not approved as a bound despite its 35 bettors.

**WEAKER — [manifold iuBCRicRjrIzUshZxq97](https://manifold.markets/BoltonBailey/will-any-fusion-reactor-project-dem-9695cf9c60e0) (review addition): Will any fusion reactor project demonstrate engineering breakeven before the end of 2040?**

Event deadline: 2040-12-31; 87.10% YES; forecasters/bettors: 56; thin: no.

The market defines engineering breakeven as enough fusion-derived energy to power the reactor itself, and its linked explanation explicitly distinguishes this from plasma/scientific breakeven and commercial profitability. A plant exporting net electricity commercially for three months necessarily demonstrates at least engineering breakeven by then, while an experimental breakeven demonstration need not export or operate commercially at all. Thus this non-thin market supplies P(our milestone by 2040-12-31) ≤ 0.8710319010, a loose lower-bound event rather than a same-event forecast.

**REJECT — [manifold mB2V6ms5NXizKE4bXIqf](https://manifold.markets/dpm2222/will-we-have-a-functioning-energypr) (review addition): Will we have a functioning, energy-producing, nuclear fusion reactor by 2033?**

Event deadline: 2033-12-31; 28.50% YES; forecasters/bettors: 66; thin: no.

The live market has no description defining energy-producing, functioning or the energy-system boundary. Literal fusion energy production already occurs in research machines, while alternative readings could require net engineering gain, commercial electricity or something else entirely. Our event would imply the ordinary loose readings, but an unresolved market on this already-achieved literal event is too underspecified to provide a dependable future bound.

### Grid Parity — `fusion/grid-parity`

**No reviewed candidate.** No candidate supplied. Commercial operation or engineering breakeven does not establish LCOE below $100/MWh in constant 2025 USD.

### Taming Cancer — `health/taming-cancer`

**REJECT — [manifold lUIuPpzc8N](https://manifold.markets/kamn/will-there-be-a-major-shift-in-canc): Will there be a major shift in cancer survival rates by 2030?**

Event deadline: 2030-12-31; 33.31% YES; forecasters/bettors: 9; thin: yes.

The market asks for a roughly twenty-point change in five-year survival across all cancers, with no settled source, baseline or resident-population definition; our test is an absolute 80% ten-year net survival level for solid tumours in a whole population of at least 50M. Five-year improvement does not entail the ten-year threshold, and our frontier could meet that threshold without the specified all-cancer change. A creator update moves closing to 2035 without cleanly reconciling the title’s 2030 event cutoff, adding a resolution ambiguity rather than a usable bound.

Deadline caveat: Nominal title deadline, using end-of-year interpretation of by 2030; not a verified unambiguous cutoff. A creator update extends closing to 2035 and allows earlier resolution but does not clearly reconcile the event deadline, baseline or data source.

**UNVERIFIABLE — [metaculus 21079](https://www.metaculus.com/questions/21079/when-cancer-survival-rate-exceeds-95/): When will the average five-year survival rate of all cancers exceed 95%?**

Event deadline: not a single binary deadline; displayed date estimate 2057-02, displayed interval 2043-08 to 2068-11; forecasters/bettors: 20; thin: no.

The live page displays a February 2057 estimate and twenty forecasters but does not expose the full population/statistic/resolution rules, so this is unverifiable. From the visible title, 95% five-year survival across all cancers does not guarantee 80% ten-year net survival for solid tumours, because deaths after year five can still be substantial. Conversely, 80% ten-year solid-tumour survival does not require 95% five-year all-cancer survival; the relation would be reject, not stronger, even before the unresolved geography and averaging rules.

**REJECT — [manifold 3etXCqMlDdVaNIuYyQZQ](https://manifold.markets/chrisjbillington/will-glioblastoma-an-aggressive-bra): Will glioblastoma (an aggressive brain cancer) have a 5-year relative survival rate greater than 15% in the US in 2035?**

Event deadline: 2035-12-31; 41.34% YES; forecasters/bettors: 14; thin: yes.

A US glioblastoma five-year relative survival point estimate above 15% is compatible with poor overall solid-tumour survival, so it does not imply our aggregate ten-year threshold. Our aggregate can exceed 80% while a small difficult subtype remains below 15%, and the qualifying frontier need not be the US, so our milestone does not imply this event either. Resolution uses the 2035 CBTRUS report’s earlier diagnosis cohorts, with discretionary substitution or interpolation, not a 2035 treatment cohort or an independent metastatic-cancer requirement.

Deadline caveat: The nominal event is the statistic in the CBTRUS 2035 report, not survival of people newly diagnosed in 2035; the criteria allow later substitute reports or interpolation if that report is absent.

### Precise Screening — `health/precise-screening`

**No reviewed candidate.** No candidate supplied. Diagnosis must precede symptoms, exclude risk factors alone, and be case-weighted across the four classes for a whole resident population of at least 50M.

### Unbroken Mind — `health/unbroken-mind`

**No reviewed candidate.** No candidate supplied. The endpoint is age-standardized dementia prevalence below 5% among all residents aged 80+ in a region or country of at least 50M, not drug approval or risk reduction.

### The Long Middle Age — `health/the-long-middle-age`

**REJECT — [manifold 60N0viOTdZfv1F9jMM1Q](https://manifold.markets/MatthewBarnett/will-a-therapy-that-substantially-s): Will a therapy that substantially slows down or reverses the aging process in humans be developed before 2040?**

Event deadline: 2039-12-31; 60.12% YES; forecasters/bettors: 27; thin: no.

The market permits a composite of aging-associated biomarkers without mandating epigenetic clocks, and its two 25% clinical-endpoint or physiological-function improvements need not be reductions in disease incidence. Therefore a qualifying therapy can fail our clocks-plus-functional-biomarkers-and-incidence test. Conversely, our milestone does not stipulate 100 participants, two 25% improvements, or validation by two separate entities, so it need not satisfy the market’s added thresholds; explicit creator discretion adds uncertainty but the mixed endpoints already defeat both implications.

### The Bend — `climate/the-bend`

**UNVERIFIABLE — [metaculus 11933](https://www.metaculus.com/questions/11933/global-co2-emissions-peak-year/): Global CO2 Emissions Peak Year**

Event deadline: not a single binary deadline; displayed date estimate 2031-11, displayed interval 2027-06-21 to 2038-12; forecasters/bettors: unverified; thin: unknown.

The live extract shows a November 2031 estimate and a moderator clarification that the metric is CO2 including land-use change, but not the complete resolution criteria or a current forecaster count. A CO2 peak need not occur before the peak of all GHGs, since non-CO2 gases can offset CO2 changes in either direction. Nor is the physical CO2 peak date the date when an all-GHG inventory establishes a peak at least three years back with the latest year at least 1% lower; the visible relation would be reject, and API access remains blocked.

**REJECT — [manifold 6EOLzz9h9A](https://manifold.markets/JZB/will-global-carbon-emissions-from-a-Is9SggCpdp): Will global carbon emissions from all sources peak before 2030?**

Event deadline: 2029-12-31; 76.90% YES; forecasters/bettors: 8; thin: yes.

The description simultaneously specifies IEA energy-related CO2 and all-source CO2-equivalent GHGs, so the measured quantity is not coherent. A single annual fall in 2025–2029 need not establish our three-year-old all-GHG peak and 1% reduction; in the other direction, an earlier qualifying peak need not produce a fall specifically within this window. If the scope and time window matched, a mere fall could be weaker than confirmation, but those mismatches prevent that implication here.

Deadline caveat: The event window is 2025–2029; the end-of-2030 data/resolution cutoff is not the event deadline.

### The Balance — `climate/the-balance`

**REJECT — [manifold 3H7q6U4GYUnDcl4fB9CU](https://manifold.markets/kian_spire/will-the-world-achieve-netzero-carb): Will the world achieve net-zero carbon emissions by 2060?**

Event deadline: 2060-12-31; 53.93% YES; forecasters/bettors: 22; thin: no.

Exact net-zero carbon can coexist with substantial positive methane, nitrous oxide and other GHG emissions, so it does not imply our all-GHG GWP100 balance within ±5% of 2025 gross emissions. Conversely, our tolerance band can be reached while net carbon emissions remain positive, without satisfying this market’s exact carbon condition. Its allowance for unspecified natural removals and a NO on significant delay or retraction also fails to enforce our durable anthropogenic accounting; neither implication holds.

Deadline caveat: By 2060 is treated as through the end of 2060, consistent with closing on December 31, 2060; the supplied 2059-12-31 cutoff is not stated by the market. Intraday timezone is unspecified.

### The Ceiling — `climate/the-ceiling`

**No reviewed candidate.** No candidate supplied. A temperature crossing forecast does not identify ten years at or below a stopped long-term human-induced warming peak below 2°C.

## Coverage gaps and next actions

**19 of 20 milestones remain without an accepted anchor.** Rejected neighbours are not backfilled as bounds. There are no reviewed candidates at all for Linux Kernel Patch; Robotaxi Saturation; Fukushima Test; Blue Collar Shift; Dark Line; Deluge; Export; Grid Parity; Precise Screening; Unbroken Mind; and Ceiling. Nature Author, $10M Solopreneur, Wozniak Test, Homestead, Taming Cancer, Long Middle Age, Bend and Balance have reviewed candidates but none approved. First Watt still lacks a same-event or stronger anchor.

For follow-up, seek or commission questions that explicitly include the binding scope and threshold, especially a **policy-conditioned AI research capability** question, a **developer-unselected and never-mapped home** test, a **Moon-or-Mars** habitation question, and **three months of commercial net public-grid fusion export**. Health questions need the exact survival/prevalence/incidence endpoints and population, while climate questions must distinguish CO2 from all GHGs and achievement from later confirmation. No claim is made that better existing markets cannot be found.

## API and reuse caveats

These are the access/terms findings **as stated in `api.md`**, not independent legal advice or a new terms audit:

- **Manifold:** [public market reads](https://docs.manifold.markets/api) require no authentication; the stated limit is 500 requests/minute/IP. Public read access does not authorize unrestricted database building: the [terms](https://manifold.markets/terms) prohibit systematic retrieval to compile a database without written permission, commercial use needs approval, and commercial AI training requires a data licence. Obtain written permission for weekly persistent storage and public redisplay, even for accepted anchors; attribution alone is not a substitute.
- **Metaculus:** anonymous API access returns 403 and requires a token. The [March 9, 2026 API announcement](https://www.metaculus.com/notebooks/42554/changes-to-the-metaculus-api/) says community predictions and other aggregates are no longer generally available through the API; a token alone does not demonstrate entitlement. Noncommercial users are asked to get in touch and commercial arrangements are case-by-case. The [terms](https://www.metaculus.com/terms-of-use/), reported updated September 21, 2026, grant a limited personal noncommercial viewing licence and restrict copying/extraction except through an API on its terms or written authorization; no open-data/CC licence was established. A readable Jina page is **not** a substitute entitlement to scrape and republish weekly aggregates.
- Before implementing collection, obtain source-specific written storage/redisplay authorization, document attribution and permitted retention, and for Metaculus obtain explicit aggregate access in addition to credentials. Current permission status blocks treating this report as a launch approval for a public weekly dataset.
