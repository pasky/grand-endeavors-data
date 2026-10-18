# KPI candidate A — counting rules (draft, 2026-10-17)

**Headline:** cumulative number of distinct (vendor, customer organization) pairs for which a
verified source documents a general-purpose robot doing production work for that named external
customer, autonomously as reported.

A pair counts when one source documents ALL of R1-R3; the pair's date is the earliest such
source's publication date.

**R1 General-purpose robot.** A humanoid (legged, wheeled or column-based) or a mobile
manipulator: a robot that can move itself between workstations AND physically manipulates objects
in the counted work. Excluded: fixed arms and cells (whatever AI model runs them), vehicles and
AMRs/forklifts without manipulation, legged/wheeled robots used only as sensor carriers
(inspection with no manipulation), exoskeletons, purpose-built machines.

**R2 Production work for a named external customer.** The robot does part of the customer's real
operations (a live production line, a working warehouse/logistics flow, a store or restaurant
open to its customers, a home of a paying owner) — a trial or pilot inside live operations
counts. Not counted: the vendor's own or affiliated facilities (e.g. a vendor's parent group's
factory), the vendor's labs or showrooms, non-production tests, trade-show or livestream
demonstrations outside live operations, training/testbed centres, orders/contracts/MOUs/plans
without reported work, units delivered with no reported work. The customer must be named
(an organization, not "a Tier-1 supplier"), and the source must say what job the robot does
there (a bare mention of the customer in a list of sites, users or hours does not count).

**R3 Autonomy as reported.** The source (or the deployment's other sources) describes the robot
doing the work itself/autonomously, or describes the robot's work with no indication of
teleoperation. If a source says the work is teleoperated/remote-controlled, the pair does not
count on that source.

**R4 Identity.** vendor = the robot maker (not the model provider); customer = the parent
organization (CATL's bases count as CATL; China Post's centres as China Post). One pair per
(vendor, customer) however many sites, robots, jobs or robot generations.

**R5 Cumulative.** Pairs never leave the count; an ended deployment stays, annotated `ended`
with its source.

**Side columns (not in the headline):** robots (disclosed count, else null), hours/throughput
disclosed, autonomy evidence class: `claimed` (vendor/customer/press says so) or `evidenced`
(a disclosed intervention rate, or independent observers reporting on control/interventions),
and whether the same vendor's platform is documented doing a different job elsewhere
(`redeployed`).
