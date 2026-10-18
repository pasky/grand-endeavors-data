# Board charter: the Robots/Hardware KPI

**Question.** What is the simplest way to produce the Robots/Hardware KPI of "Five Grand
Endeavors" (one recurring numeric series tracking progress in general-purpose AUTONOMOUS physical
automation) that is, in priority order, (1) trustworthy, (2) reliable/reproducible, (3) cheap-ish,
(4) fast — and is the "capability coverage of O*NET work" approach we prototyped the right one at
all, or should the framing change?

**Feeds.** The owner's decision on what KPI to write into `framework.yaml` for robots-hardware and
what pipeline (if any) to build for it. The owner's verdict on the current state: "this still
feels arbitrary and half-baked". He wants it "as simple as possible", with no weird arbitrary
rules that would break over time.

**Shape: decide.** Each seat proposes 3-5 options (complete designs: what number, from what
source/method, how it is produced and refreshed, why it is trustworthy, cost/cadence), always
including the baseline (the current v5 prototype design, possibly simplified) and a "reframe" or
do-nothing-like option (e.g. a plain external series, a milestone-style tracker instead of a KPI).
At least two options per seat should be ones you expect the other seats won't propose.

**Seats.** fable (anthropic/claude-fable-5-1:high), astra (openai-codex/gpt-6-astra:high),
argon (openrouter/google/gemini-4-argon:high).

**Context.** `/home/pasky/.pi/boards/20261017-hw-kpi/context.md` (read it first; it lists absolute
paths to all research and prototype files).
