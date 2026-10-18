# Rating protocol: can a GENERAL-PURPOSE robot do this job task autonomously? (prototype, Oct 2026)

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

**Tier** (strongest autonomous GP evidence for the instance):
- `none`: no GP robot has autonomously done it (or only fragments of it).
- `demo`: a GP robot autonomously completed the instance end-to-end at least once, in a lab,
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
Be skeptical: most tasks will be `none`. Do not stretch evidence to fill a tier.

## Output

Write ONE JSON file (path given in your task) containing a list with one object per task:

```json
{
  "key": "<task key as given>",
  "instances": [
    {
      "instance": 0,
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
  "task_note": "<optional one-line summary>"
}
```

`earliest` = the first month (to your knowledge) a GP robot met each tier for this instance
(null if never). Validate the file with `python3 -m json.tool <file>` before finishing. Reply with
only a 2-3 line summary (counts of tiers) and the file path.
