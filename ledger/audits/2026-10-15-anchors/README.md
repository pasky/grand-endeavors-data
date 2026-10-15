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
