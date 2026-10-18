# Rating protocol v2 (partial credit): how much of this job task can a GENERAL-PURPOSE robot do autonomously? (prototype, Oct 2026)

You rate US job tasks (O*NET task statements, as split into concrete "instances" by Anthropic's
2026 robot-exposure study) for one question: **what is the strongest public evidence that a
general-purpose robot has performed this instance autonomously, and how mature is it?**
Today is 2026-10-17. Use web search; verify every source you cite by opening it.

## Definitions

**General-purpose (GP) robot**: hardware not built for this task, that software alone could move
to other jobs. Record the form factor:
- `humanoid` (legged or wheeled humanoid, e.g. Figure, Digit, Optimus, Atlas, Walker S, G1, AgiBot, NEO)
- `mobile_manipulator` (mobile base + arm(s), e.g. Hello Robot Stretch, Galbot, pi0.5 mobile robot,
  Everyday Robots, Reflex)
- `stationary_generalist` (fixed general arms driven by a generalist robot model rather than a
  task-specific program, e.g. a bimanual ALOHA-style station running pi0/Gemini Robotics, Dyna's
  folding station). Counted separately; it is a borderline case.
NOT general-purpose: machines or cells built for a task (dishwashing robot, floor scrubber, robotic
welding cell, autonomous tractor, warehouse picking arm with a task-specific gripper/program,
Boston Dynamics Stretch, Spot used only as a camera carrier is `mobile_manipulator` only if it uses its arm).

**Autonomous**: the robot executes the instance with no human teleoperation or physical help
during the task. A human may give a high-level instruction ("fold the laundry"), start it, or stand
by for safety. If the source says or shows teleoperation, or autonomy is unstated and unclear,
record `autonomy: "teleop"` / `"unclear"`; such evidence does NOT count for the tier.

**Fraction** (the core rating): the share of the instance's working time made up of sub-steps
that a GP robot has demonstrably performed autonomously, end-to-end for each counted sub-step,
at a usable speed (at least 1/10 of human speed). Break the instance into its main sub-steps,
estimate each sub-step's share of the instance's time, and sum the shares of the sub-steps with
qualifying evidence. Round to one of 0, 0.05, 0.1, 0.25, 0.5, 0.75, 1. Example: "warehouse worker
receives totes, moves them to the conveyor, checks labels, handles exceptions": a humanoid moving
totes from an AMR to a conveyor at a customer site may cover the moving sub-step (~0.25), not the
label checks or exception handling. A sub-step shown only in a much easier version does not count.

**Tier** (maturity of the strongest evidence behind the counted fraction; `none` iff fraction = 0):
- `none`: no qualifying sub-step.
- `demo`: a GP robot autonomously completed the counted sub-steps at least once, in a lab,
  company facility or public demo (company video/blog/paper is enough; note if edited/sped up).
- `pilot`: done at a real customer/work site (not the developer's own facility) in a trial,
  pilot or limited deployment.
- `deployed`: in routine, ongoing paid/production use at a customer site (or the robot is sold
  and used by customers for this, e.g. a home robot doing it for paying owners).
A task done in a much easier version does not count (e.g. folding pre-flattened towels does not
cover "fold assorted laundry"). Close transfer counts only if the physical activity, object class
and setting type are the same (state it in `note`). Speed: if the source states the robot is
slower than 1/10 of human speed, record it in `note` and use at most `demo`.

**Environment** where the cited robot did it (Anthropic's tiers): `E1` purpose-built robot
setting (fixtures, fenced cell, set up around the robot); `E2` structured human workplace (factory
floor, warehouse, hospital, hotel kept to a standard); `E3` unstructured (homes, construction
sites, outdoors as found, unseen environments).

`anthropic_leads` are sources Anthropic's rater cited for the task (any robot, GP or not). They are
leads only; most are not GP. Search beyond them (e.g. Figure/Helix, Physical Intelligence pi0.5/
pi0.6, Google DeepMind Gemini Robotics, Agility, 1X, Tesla Optimus, UBTech, AgiBot, Unitree,
Galbot, Dyna, Sunday, Skild, Apptronik, Boston Dynamics Atlas, Robotera, Toyota Research).
Be skeptical and do not stretch evidence, but search properly: for each task run at least 3
distinct searches aimed at GP robots doing its sub-steps, and record them in `searches`.
Autonomous road vehicles (trucks, robotaxis, tractors) are purpose-built, not GP.

## Output

Write ONE JSON file (path given in your task) containing a list with one object per task:

```json
{
  "key": "<task key as given>",
  "instances": [
    {
      "instance": 0,
      "fraction": 0.0,
      "substeps_covered": "<which sub-steps count, with their time shares, or null>",
      "tier": "none|demo|pilot|deployed",
      "env": "E1|E2|E3|null",
      "form": "humanoid|mobile_manipulator|stationary_generalist|null",
      "system": "<robot/model or null>",
      "developer": "<company/lab or null>",
      "evidence_date": "YYYY-MM or null (when the cited demo/deployment happened)",
      "url": "<verified source URL or null>",
      "quote": "<short verbatim quote from the source supporting autonomy + the activity, or null>",
      "earliest": {"demo": "YYYY-MM|null", "pilot": "YYYY-MM|null", "deployed": "YYYY-MM|null"},
      "rejected": "<best GP evidence you rejected and why (teleop, not end-to-end, easier version...), or null>",
      "note": "<transfer argument, speed, caveats; or null>"
    }
  ],
  "searches": ["<the web search queries you ran for this task (at least 3)>"],
  "task_note": "<optional one-line summary>"
}
```

`earliest` = the first month (to your knowledge) a GP robot met each tier for this instance
(null if never). Validate the file with `python3 -m json.tool <file>` before finishing. Reply with
only a 2-3 line summary (counts of tiers) and the file path.

## Searching (mandatory, audited)

Search tools: `/home/pasky/.pi/agent/packages/pi-amplike/skills/web-search/search.py "<query>"`
and `/home/pasky/.pi/agent/packages/pi-amplike/skills/visit-webpage/visit.py <url>`.
Your tool log is audited afterwards. For EACH task: run at least 3 searches and READ their
results (never redirect output to /dev/null or discard it), follow up promising leads, and open
(visit.py) every URL you cite. A rating of 0 must rest on searches you actually read: put the
best GP lead you found and why it fails in `rejected`. Ratings without real searching are void.
