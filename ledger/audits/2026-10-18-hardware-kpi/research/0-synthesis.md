# Robots/Hardware KPI — research synthesis (2026-10-17)

Inputs: 1-others-ideas.md, 2-unit-data.md, 3-deployments.md, 4-economics.md, 5-autonomy.md
(research-mode subagents, web sources to Oct 2026), plus own spot checks and an analysis of
Anthropic's robot-exposure data release (rx1-4.py).

## Spot-checked (verified by fetching the source)
- IDC (Apr 2026): 2025 humanoid shipments >18,000; >85% of deployments in performances,
  education, data collection, guided tours.
- Unitree exchange response (via The Robot Report, 25 Mar 2026): Jan-Sep 2025 humanoid revenue
  73.6% research/education, 17.4% demos/display, 9.01% industrial.
- Agility Digit 5 release (Sep 2026): Digit 4 has logged 65,000+ hours across customer sites
  (no autonomy share, intervention or unit breakdown).
- Epoch AI "Where autonomy works" (10 Feb 2026): 14 tasks x 5 stages (early research ...
  production deployment); autonomy required; one-off report, no stated update cadence.
- Anthropic "What work can robots do?" (30 Sep 2026) + CC BY 4.0 data (HF
  Anthropic/EconomicIndex/robot_exposure): 7,594 physical O*NET tasks rated E0-E3; every cited
  source has system, developer, date, maturity (deployed/commercial/demo), autonomy_status.
  "Periodic updates to this work can track robot capabilities" (no committed cadence).
  Backcast: ~2%/yr of not-yet-doable physical work becomes doable (1977 -> 2026).
- LEAP Wave 7 (Apr 2026) robotics questions: IFR stock, US labor share, Coffee Test (expert
  median 2034, superforecasters 2032), robotic appendectomy, Amazon sales per distribution employee.
- NOT verified: Reuters "7,000 humanoid sales in 2025" (CAPTCHA); conflicts with IDC/Omdia.

## Research-report errors noticed
- 3-deployments and 5-autonomy call Robotera/China Post, Dyna/Din Tai Fung and Figure's
  200h livestream "unverified"; all three are verified events in our ledger. 3-deployments'
  12-row inventory is thin; its 0/12 disclosure figure is directionally right, not a census.

## Reproduction of Anthropic headline (OEWS May 2024 employment x time_share)
physical = 45% of work time (paper: 46%); of physical: E0 24.4%, E1 50.2%, E2 23.4%, E3 2.0%
(paper: 24 / 50 / 22 / 2). Reproduces.

## Crude general-purpose-only cut (developer/system regex; instance counts if any cited source
is GP + autonomous; task tier by the paper's >50% majority rule)
- deployed/commercial GP evidence: ~0.5% of physical work time (>=E1), ~0.08% (>=E2)
- incl. demos: ~1.7% (>=E1), ~0.11% (>=E2)
- by source date (strict): 2023-12 0.01% -> 2024-12 0.03% -> 2025-06 0.33% -> 2026-06 0.51%
Caveats: the instance tier may come from a non-GP co-cited robot (e.g. Waiters "prepare
tables" credited via pi0 but driven by Chef Robotics; "substitute teachers distribute tests" via
Figure package sorting), Claude cited the decisive robot rather than searching for GP robots, and
dates reflect what was cited in 2026 (backcast bias). Order of magnitude only.
