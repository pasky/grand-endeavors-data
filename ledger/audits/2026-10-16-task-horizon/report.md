# Findings

## milestone:the-10m-solopreneur (MAJOR, documentation)

The record's `basis.path` still gives the two sensitivities of the previous (metr-horizon) model:
counting professional-services time adds about 0.19 years and portfolio overhead about 0.37 years to
the ETA. The record's own `calc` and the run's notes, on the canonical task-horizon draws, give
+0.17 and +0.34 years; an independent re-computation from the canonical draws reproduces 0.167 and
0.337 years. Fix: state the current values (and keep `path`, `calc` and the notes consistent).
No change to p10/p50/p90, p_achieved or the status is expected (the effects are a fraction of a year
and already in the central model); keep the model, only correct the text.
