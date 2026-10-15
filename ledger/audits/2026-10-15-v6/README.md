# Audit of the rubric v6 ETAs (2026-10-15)

An independent deep-mode audit (openai-codex/gpt-6-astra) of the 20 milestone ETAs re-assessed
under rubric v6 on 2026-10-15 (runs 20261015T093430Z robots-software, 20261015T100057Z
robots-hardware, 20261015T103105Z rockets, 20261015T105338Z fusion, 20261015T110538Z health,
20261015T113313Z climate), after each run's own review stage. It reran every model with the
shared driver draws (data drivers.yaml) and checked anchors, failure-scenario counts and rule 7.

Result (report.md): 18 milestones OK or minor; 2 MAJOR, both in health:
- M1 taming-cancer: the notes and calc state a solid-tumour adjustment of the all-cancer
  survival anchor that the script does not apply (p_achieved .834 vs .833 with it).
- M2 the-long-middle-age: the failure inputs F1/F2 were changed (.15/.12 to .18/.11, p_achieved
  .747 to .728) and attributed to rubric v6, which asks for counted reference classes but does
  not itself require replacing a disclosed judgment that the counts bracket (rule 7).
Health was re-assessed with AUDIT=2026-10-15-v6 for these two targets.
