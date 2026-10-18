# Curating the GP robot capability catalogue (prototype, 2026-10-17)

Goal: a deduplicated catalogue of what GENERAL-PURPOSE robots have demonstrably done
AUTONOMOUSLY, so that later raters map catalogue entries onto job tasks instead of each searching
the web on their own. Today is 2026-10-17.

## Input (your group file)
- `ledger`: events from our verified news ledger (claim text already checked against the source;
  `verification` = verified/corrected/legacy). Trust their wording; it is the ground truth.
- `anthropic`: sources cited by Anthropic's 2026 robot-exposure rater (Claude), pre-filtered to
  GP-looking developers and `autonomy_status: autonomous`, grouped by source URL: `claims` are that
  rater's summaries (up to 4), `systems`/`dates`/`maturity` its labels, `n` how often it was cited. Some are not GP (e.g. trucks, fixed task cells) or overstate the source.

## Definitions
- **GP robot**: hardware not built for one task, that software alone could move to other jobs.
  `form`: `humanoid`, `mobile_manipulator`, or `stationary_generalist` (fixed general arms run by a
  generalist robot model, e.g. ALOHA-style stations running pi0/Gemini Robotics, Dyna stations).
  Exclude purpose-built machines (vehicles, trucks, floor scrubbers, dish machines, picking cells,
  Boston Dynamics Stretch, Spot without manipulation), and drop such inputs.
- **Autonomous**: no teleoperation or physical human help during the activity (high-level
  instruction, start, safety standby are fine). Teleoperated or unclear → drop, or keep with
  `autonomy: "unclear"` only if it is a prominent claim worth flagging.
- **Maturity**: `demo` (lab, developer facility, public demo, paper), `pilot` (customer/real work
  site, trial or limited), `deployed` (routine ongoing paid/production use at a customer, or a
  product used by paying customers for this activity).
- **env**: `E1` purpose-built robot setting (fixtures, set up around the robot), `E2` structured
  human workplace (factory floor, warehouse, hotel, hospital), `E3` unstructured (homes, unseen
  environments, outdoors as found).

## What an entry is
One entry = one distinct ACTIVITY one system (or model family) has done, at its best maturity.
Merge all sources about the same activity. Split different activities even for one robot (e.g.
Figure: "sheet-metal part loading at BMW" vs "parcel orientation on a conveyor" vs "dishwasher
loading in a home"). Describe the activity concretely and narrowly enough that a rater can judge
transfer: the verb, the object class, the setting, end-to-end scope (what it did NOT do).

## Checking
- Ledger-based entries need no re-check.
- Open the source (visit.py) for every Anthropic-only entry whose maturity would be `pilot` or
  `deployed`, and for any claim that looks overstated. Set `checked: true` if you opened it.
- You may add important missing capabilities of your group's developers found by search (at most
  10; mark `basis: "added"`, open the source).

Tools: `/home/pasky/.pi/agent/packages/pi-amplike/skills/web-search/search.py "<query>"`,
`/home/pasky/.pi/agent/packages/pi-amplike/skills/visit-webpage/visit.py <url>`. Read what you fetch.

## Output: a JSON list, one object per entry
```json
{
  "developer": "...", "system": "...", "form": "humanoid|mobile_manipulator|stationary_generalist",
  "activity": "<concrete: what it did end-to-end, objects, setting; and what it did not do>",
  "objects": "<object classes handled>",
  "setting": "<where>", "env": "E1|E2|E3",
  "maturity": "demo|pilot|deployed", "customer": "<customer/site or null>",
  "autonomy": "autonomous|unclear",
  "speed_vs_human": "<e.g. '~0.25x', '~1x', or null>", "reliability": "<stated success rate or null>",
  "date": "YYYY-MM (first time at this maturity)",
  "basis": "ledger|anthropic|both|added", "checked": true,
  "ledger_ids": ["..."], "urls": ["..."],
  "caveats": "<company claim only, edited video, unseen environments or not, etc.>"
}
```
Validate with `python3 -m json.tool`. Reply with the number of entries by form and maturity, plus
the output path.
