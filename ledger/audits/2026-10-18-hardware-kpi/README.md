# Robots/hardware KPI: how gp-deployment-pairs was chosen (2026-10-16 .. 2026-10-18)

The old KPI ("largest active commercial fleet of general-purpose humanoids, single site") never
had data. Owner constraints: the point is general-purpose AUTONOMOUS physical automation (IFR
industrial robot counts rejected); a plain FTE count does not check autonomy; no arbitrary rules
that break over time; trustworthy > reliable > cheap > fast; as simple as possible.

1. research/ — web research (Oct 2026): no public series measures autonomous general-purpose
   robot work. Humanoid shipments 2025 ~13k (Omdia) to >18k (IDC), >85% to performances,
   education, data collection and guided tours (IDC, method unpublished); Unitree Jan-Sep 2025
   humanoid revenue 9% industrial (IPO inquiry response, one-off); deployments rarely disclose
   robots x hours x interventions. 0-synthesis.md has the spot checks and the reports' errors.
2. prototype/ — a capability-coverage KPI (share of US physical work time, O*NET tasks after
   Anthropic's 2026 robot-exposure data, that general-purpose robots can do autonomously).
   v1/v2 rater runs were void (raters skipped or faked searching: tool-log audit); v3 ~0.55%
   with contradicting raters; v4 catalogue mapping 19/30 agreement; v5 atomic pair judgments
   agreed (29/30) but the level depended on the judging model (Luna 0.11%, Opus 0.32%) because
   capability transfer is not decidable. RESULTS.md.
3. board/ — an advisory board (Fable, GPT Astra, Gemini Argon; memo.md): coverage killed (a blind
   3-lab test mapped the same deployments onto task instances with 1-2/7 agreement); the list of
   verified named-customer deployments was reproducible. Fork A (count them) vs Fork B (no KPI).
4. Owner decisions (2026-10-18): Fork A, framed as a provisional pioneering-stage KPI; fixed
   arms do not count even with a generalist model (mobility is the line: otherwise every AI
   picking cell would qualify, e.g. Dyna's napkin station); positive autonomy statement required
   (silence about teleoperation is not enough); claims trusted unless credibly disputed; the
   dashboard lists every counted case.
5. coverage/ — RULES.md (the draft rules, now the registry definition of gp-deployment-pairs);
   repro_*.json: three independent roster derivations from the ledger (2x Opus, GPT Astra) agreed
   on the same 7 pairs and dates; the divergences were rule gaps (a bare customer-list mention,
   'practical training' 实训), now closed in the definition; coverage_*.md: a web check found
   qualifying cases the ledger had missed (UBTech/Dongfeng Liuzhou, possibly Sanctuary/Canadian
   Tire) and earlier first sources (GXO 2024-06-27); beyond_dark_factories.md: the 'dark
   factory' claims checked (purpose-built automation, viral numbers inflated, no general-purpose
   robots).
6. Pipeline (2026-10-18, gather.sh/assess.sh, data commits of that day): a KPI backfill gather
   (SINCE 2023-01-01, a focus brief with the coverage leads) staged 14 cases, verified to 11 (the
   verifier dropped Schaeffler: no statement that Digit does that job autonomously; and Leju at
   Zhaofeng on its 实训 label); the definition then got its agreed 'unless the work is part of the
   actual output' clause and a targeted re-check counted Leju (12). repro-final/: three models of
   three labs (Opus, GPT Astra, Gemini Argon) derived the roster from the ledger with the
   pipeline's deployment fields and verifier notes stripped: Opus and Argon matched the pipeline's
   12 pairs and dates exactly; Astra excluded Robotera's M7 at China Post as not self-moving,
   correctly (a torso on a stand; the R1 text had listed 'column-based' humanoids). R1 was fixed
   and a pipeline mobility audit of all cases removed only China Post: 11 pairs, assessed green
   (+8 in the last 12 months vs +3 before; small counts, one retrospective sweep). A beyond gather
   added 10 verified dark-factory records.
