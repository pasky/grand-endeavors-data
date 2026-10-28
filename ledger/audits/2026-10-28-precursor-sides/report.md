# Finding: the precursor records counted cases the milestones exclude (owner, 2026-10-28)

## Owner decisions

1. **solo-company-arr-max**: "one person" means nobody else builds the product or runs
   operations (contractors, an agency, another company's staff). Polsia's 2026-09-15 $10.98M
   row is withdrawn: its founder said on 2026-10-16 that engineers of Sapiom were pulled into
   the product to fix bugs and harden the platform (event 2026-10-16-polsia-founder-20m-run-rate).
   The record is back to $3M (Polsia, 2026-03-23, investor-reported); no source puts the outside
   engineers that early. The revenue reading itself (event 2026-09-15-polsia-subscription-mrr-10-98m)
   is not disputed and stays as evidence of what a small AI-heavy team earns, not of a solo path.
2. **ai-contribution-lines-merged-max** (the human side of the kernel patch): only independent
   acceptance counts (approved by maintainers other than the submitter, in a project neither the
   submitter nor the AI developer controls), and only work whose contributor or project says an AI
   wrote most of the code. Withdrawn: Ladybird 30,550 (its lead merged his own PR), Bun 1,009,257
   (self-merged, Anthropic-owned), Node.js node:vfs 10,859 (the author: "created by me with massive
   help from @claude. The design of this feature is mostly mine": AI-assisted). **The series has
   no qualifying row.** The previous rationale's "AI-written contributions far above 10,000 lines
   are already accepted (Ladybird, Bun, Node.js)" no longer holds under the definition.
3. **New AI-side series** (registered, no qualifying row yet):
   - **unattended-business-arr-max** (the-10m-solopreneur): annualized revenue of a real business
     an AI runs on under 10 h/week of total human time (people doing tasks the AI directs count),
     covering its costs (AI costs included) over the period.
   - **ai-submitted-lines-merged-max** (the-linux-kernel-patch): the largest contribution an AI
     agent opened and saw through review itself, approved by someone other than whoever tasked
     it, in a project neither they nor the agent's developer controls.
4. **Status rubric unchanged** (owner chose to keep RUBRIC §4: a driver-based ETA ≤ 10 years with
   measurable driver progress stays yellow; precursors are not required for yellow). Do not
   argue for green on either milestone: neither has a demonstrated precursor at relevant scale.
5. **Don't over-index on the AI side**: AI-run businesses today are lab experiments whose scale
   the experimenters choose. Use unattended-business-arr-max as evidence on (and a cross-check
   of) the oversight gate, not as a path extrapolated to $10M.

## Research pass (2026-10-28, three research agents; not ledger events)

- **unattended-business-arr-max**: nothing qualifies. Closest: Project Vend phase two
  (https://www.anthropic.com/research/project-vend-2: agents "still needed a great deal of
  human support"; purchases need human approval), Andon Market (two hired staff; unprofitable),
  Andon café ($38k spent vs $9k sales). No Polsia-hosted company publishes revenue, hours and
  profit together; no crypto agent meets the conditions.
- **solo-company-arr-max**: nothing above $3M qualifies. Postiz (https://trustmrr.com/startup/postiz,
  Stripe-verified $326,687 MRR = $3.92M annualized, 2026-10-28) fails one-person: in its public
  repo (gitroomhq/postiz-app) a second developer authored 70 commits since 2026-07-01 against the
  founder's 24. Pieter Levels (~$200-250K/month total revenue) states no recurring figure.
- **ai-contribution-lines-merged-max**: nothing qualifies; near-misses as withdrawn above, plus
  OCaml #14369 (13,323 lines, Claude-written, closed unmerged 2025-11-20).
- **ai-submitted-lines-merged-max**: nothing qualifies. Nearest: Home Assistant core #168855
  (Copilot agent, 1,638 lines, merged 2026-05-18; fails: the merging maintainer authored code
  commits in it), #166247 (31 lines; the maintainer who directed it merged it); Copilot agent PRs
  in dotnet/runtime are excluded (Microsoft controls both).

## What to do

- Keep each milestone's model, draws and structure from the previous records (rule 7); change
  only the inputs these decisions change, and say which.
- **the-10m-solopreneur**: Polsia does not qualify from mid-2026, so the revenue condition's
  measured start is the $3M record (2026-03-23), not $10.98M; re-weigh path A (Polsia as a
  qualifying company, prev q 0.5) accordingly (its only route back is dropping the outside
  engineers) and path B. Cite the empty AI-side series in the oversight half.
- **the-linux-kernel-patch**: both of its series are empty. The size rung is no longer shown passed
  by independently accepted AI-written work; restate the crux and the path accordingly (the
  milestone still assumes maintainers judge openly AI-submitted patches on merit).
- Labels and rationales must not present Polsia's ~$11M, Bun or Ladybird as qualifying.

## Addendum (2026-10-28, after the first re-assessment, run 20261028T182049Z)

A code review of the change found two problems for the-linux-kernel-patch:

1. **ai-contribution-lines-merged-max is not empty.** The research pass missed a known case in the
   ledger: Sasha Levin's Linux tracing patch (+7 lines, committed 2025-03-23 by tracing maintainer
   Steven Rostedt, merged for 6.15), which LWN (https://lwn.net/Articles/1026558/, 2025-06-26)
   reports was "entirely written by an LLM, changelog included. Levin reviewed and tested it, but
   did not write the code" (event 2025-06-01-lwn-llm-patch-merged-615-rv). It is now the series'
   row: 7 lines. The human side's rung is therefore demonstrated at 7 lines, 0.07% of the 10k
   threshold, not absent. Larger qualifying cases may exist (the search was not exhaustive).
2. **Independence was stated the wrong way round.** Run 20261028T182049Z's cruxes, blockers and
   update channels ask for acceptance by "maintainers who do not control the project". The rule
   restricts the SUBMITTER (or whoever tasked the agent) and the AI developer: they must not
   control the project. A project lead independently accepting someone else's contribution is
   fine. Correct this wherever it appears.

Also clarified (definition): a human may have designed the work; only a claim of most of the
writing, or a statement that AI merely helped, disqualifies it.

What to do: re-assess the-linux-kernel-patch only, under rule 7: keep the model and draws, cite
the 7-line row as the human side's current rung, and fix the independence wording.
