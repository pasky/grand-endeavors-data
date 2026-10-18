# Rating protocol v3 (catalogue mapping): how much of this job task can a GENERAL-PURPOSE robot do autonomously?

You rate US job tasks (O*NET task statements, split into concrete "instances" by Anthropic's 2026
robot-exposure study). You do NOT search the web. All evidence comes from the capability
catalogue `catalog_v1_compact.json`: verified autonomous activities of general-purpose (GP)
robots (humanoids, mobile manipulators, stationary generalist arms), each with maturity
(demo/pilot/deployed), setting and environment tier. Your job is only to MAP catalogue entries
onto the sub-steps of each task instance, using the transfer rules below.

## Procedure per instance
1. Split the instance into its main sub-steps and estimate each sub-step's share of the instance's
   working time (shares sum to 1).
2. For each sub-step, find catalogue entries that cover it under the transfer rules. A sub-step
   is covered or not (no partial sub-steps).
3. `fraction` = sum of the time shares of covered sub-steps, rounded to 0, 0.05, 0.1, 0.25, 0.5,
   0.75 or 1.
4. `tier` = the maturity that applies to the covered sub-steps (the strongest one that carries
   over per rule T5); `none` iff fraction = 0.

## Transfer rules
- **T1 Same activity.** The entry must show the same manipulation/action (pick-and-place,
  carry/transport, insert/connect, fold, wipe/clean surface, open/close, operate an appliance or
  machine control, sort/inspect, use a hand tool, navigate) applied end-to-end to the sub-step.
  Fragments of the sub-step do not count.
- **T2 Same object class.** Rigid boxes/totes/cartons; small rigid parts; tableware/glassware;
  cloth/deformables; food; liquids/pouring; heavy items (>15 kg); people/animals (never covered by
  a non-people entry). Instances within a class transfer (another tote, other dishes); classes do
  not (towels do not cover buttoned shirts; boxes do not cover poly bags unless the entry includes them).
- **T3 Environment only downhill.** Evidence in a harder environment covers easier ones for the
  same activity: E3 (unstructured/unseen homes) covers E2 and E1; E2 (structured workplace) covers
  E1. Never uphill: a lab/E1 demo does not cover an E2 workplace or an E3 home.
- **T4 Pace.** If the instance is paced work (production line, service during business hours,
  throughput quotas), the entry must show at least ~1/3 human speed or be pilot/deployed doing it
  at work pace. Unpaced work needs at least 1/10 human speed (assume OK if not stated for demos
  of unpaced work, and say so in `note`).
- **T5 Maturity carries over only within the same domain.** A pilot/deployed entry keeps its tier
  for instances in the same domain (warehouse→warehouse, auto plant→other factory line of the same
  kind, restaurant→restaurant, home→home); across domains it counts as `demo`.
- **T6 Catalogue only.** Count only catalogue entries (cite their ids). If you believe an
  important capability is missing from the catalogue, write it in `missing`, but do not count it.

## Output
Write ONE JSON file (path in your task): a list, one object per task:
```json
{
  "key": "<task key>",
  "instances": [
    {"instance": 0,
     "substeps": [{"step": "<sub-step>", "share": 0.3, "covered_by": ["C012"], "rule_note": "<why T1-T5 hold, or null>"}],
     "fraction": 0.25, "tier": "none|demo|pilot|deployed", "note": "<or null>"}
  ],
  "missing": "<capabilities you think the catalogue lacks for this task, or null>"
}
```
List every sub-step, including uncovered ones (`covered_by: []`). Validate with
`python3 -m json.tool`. Reply with a 2-line summary and the path.
