# Grand Endeavors — data

The canonical, append-only **ledger** of Grand Endeavors: what is known about
humanity's progress on the endeavors, and when it became known. Also holds the
metric registry and the period bulletins. This repo is written by the pipeline
in the *mechanism* repository (github.com/pasky/grand-endeavors: `gather.sh`,
`assess.sh`, `bulletin.sh`, `roundup.sh`, `ledger.py`), which also defines the
schemas (DESIGN.md), the status rubric (gather/RUBRIC.md) and the endeavor
framework (framework.yaml). The published view is https://pasky.or.cz/grand-endeavors/.

    ledger/events/<section>.jsonl        news/claims (verified at ingest; legacy = converted from pilot-2025)
    ledger/observations/<section>.csv    KPI datapoints (collectors + verified intake)
    ledger/assessments/<section>.jsonl   milestone/KPI status judgments (gather/RUBRIC.md)
    ledger/rejected/, ledger/state/      failed-verification records; gather watermarks
    metrics/                             metric registry + per-KPI assessment spec
    pilot-<period>/                      bulletins, frozen snapshots, gaps, manifests; the frozen
                                         period page index.html + the framework.yaml in force

Validate: `uv run <mechanism>/core/ledger.py check` (with GE_DATA=<this repo>).
History before 2026-09-30 was extracted from the mechanism repo (git filter-repo).
