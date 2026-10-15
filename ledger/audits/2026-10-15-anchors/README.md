# External forecast anchors: candidate search and approval (2026-10-15)

Rubric v6 (gather/RUBRIC.md §4.1 step 4) compares each milestone ETA with community forecasts of
the same or a bounding event, listed as `anchors:` in framework.yaml. The owner was away, so a
deep-mode reviewer (openai-codex/gpt-6-astra) approved or rejected the mappings in the owner's place.

- `candidates/*.json`: candidates found by four research agents (Manifold and Metaculus, ids fetched
  live, with their proposed relation).
- `api-and-terms.md`: API access and terms of use (research agent). Metaculus: the API needs a
  token, and since March 2026 community aggregates are not generally available through it
  (non-commercial users are asked to get in touch). Manifold: public read API, no auth, 500
  requests/min; its terms forbid systematic compilation of a database without written permission
  but its API docs allow non-commercial and personal use.
- `review.md`, `verdicts.json`: the reviewer's verdict per candidate (same / weaker / stronger /
  reject / unverifiable), checked live against each market's resolution criteria, with reasons.
  The standard is strict implication: `weaker` only if our milestone implies the market's event,
  `stronger` only if the market's event implies ours.

Outcome: 2 anchors accepted, both `weaker` bounds for fusion/the-first-watt (Manifold pR0QngELPh,
commercial fusion electricity by 2035, 11 bettors (thin); Manifold iuBCRicRjrIzUshZxq97,
engineering breakeven by 2040, 56 bettors). All other candidates were rejected (resolution
criteria that neither imply nor are implied by the milestone wording) or unverifiable (Metaculus,
no API access); 17 of 18 milestones have no anchor yet.

## Addendum: `similar` anchors (same day)

The owner added a fourth relation, `similar`: the same underlying capability or outcome under
resolution criteria that neither imply nor are implied by ours, compared at wider thresholds
(10 years / 0.35) with a note on the wording differences. A second deep-mode review
(`similar-review.md`, `similar-verdicts.json`) re-examined the rejected candidates (Manifold
binary markets only) and searched briefly for more. Accepted as `similar`:
- robots-hardware/the-wozniak-test: Manifold 92RpIcOUn9 (Coffee Test before 2029, 27 bettors)
  and ZA8292N5QC (before 2027, 23 bettors);
- health/the-long-middle-age: Manifold 60N0viOTdZfv1F9jMM1Q (a therapy that substantially slows
  or reverses human ageing before 2040, 27 bettors);
- rockets/the-homestead: Manifold InfkbfL3uNM9GNq9qgKy (a relatively self-sustaining
  extraterrestrial colony before 2050, 53 bettors).
Rejected again: the CO2-peak, net-zero, one-person-unicorn and lunar-base markets, among others.
Coverage: 5 of 20 milestones.

**Finding for re-assessment (AUDIT=2026-10-15-anchors):** these three milestones now have
anchors (framework.yaml; `ledger.py anchors <section>`). Their current v6 forecasts were made
without reading them: state that forecast as the pre-anchor p50 in the notes, then compare it
with the anchors under RUBRIC.md §4.1 step 4 (discuss the wording differences of each similar
anchor and explain any gap; do not move the forecast toward a market without a reason you would
accept without it).
