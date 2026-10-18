# World coverage check — 2026-10-18

Applied the supplied R1–R3 rules strictly: announcements, planned rollouts and demonstrations do not qualify absent reported customer-operational work; the source must identify the task and not indicate teleoperation. The pair is attributed to the named end-customer’s parent organization. “Earliest” below means earliest located source meeting those conditions, not a claim that no earlier source exists.

## Qualifying non-China pairs

| Vendor | Platform | Customer (parent) | Work | Earliest source meeting R1–R3 (opened) | Robots disclosed | Confidence |
|---|---|---|---|---|---:|---|
| Sanctuary AI | General-purpose humanoid (model not specified) | Canadian Tire Corporation (Mark’s store) | One-week live-store pilot; picking/packing merchandise, cleaning, tagging, labelling and folding | [Sanctuary AI, 2023-03-07](https://sanctuary.ai/news/sanctuary-ai-deploys-first-humanoid-general-purpose-robot-commercially/): “week-long pilot at the CTC-owned store successfully tested the general-purpose robot in a ‘real-life’ store environment with 110 retail-related tasks completed correctly.” Autonomy is not explicitly labelled; report contains no teleoperation indication. | 1 implied (singular robot; exact fleet not stated) | Medium-high (R1–R2 explicit; R3 inferred under rule) |

## Existing non-China pairs: earliest located evidence

| Vendor | Platform | Customer | Earliest source meeting R1–R3 (opened) | Robots disclosed | Confidence |
|---|---|---|---|---:|---|
| Figure AI | Figure 02 | BMW Group | [BMW Group, 2024-09-11](https://www.bmwgroup.com/en/news/general/2024/humanoid-robots.html): reports a weeks-long trial at Plant Spartanburg and robots performing production tasks; says the robot “can perform fully autonomously” manipulation tasks. | Not stated in that source | High |
| Agility Robotics | Digit | GXO Logistics | [Agility, 2024-06-27](https://www.agilityrobotics.com/content/gxo-signs-industry-first-multi-year-agreement-with-agility-robotics): GXO deployed Digit at the SPANX fulfillment facility for tote handling; source describes Digit handling totes in live fulfillment operations. The customer pair is GXO (not SPANX). | “Small fleet”; no number | High |
| Agility Robotics | Digit | Schaeffler Group | [Schaeffler Tomorrow, 2026 (page opened; publication date not shown)](https://schaeffler-tomorrow.com/en/article/welcome-aboard-robo): “since the beginning of 2025, Digit has been loading and unloading a washing machine at Schaeffler’s American plant in Cheraw”; further says it autonomously navigates the environment. This is the earliest located source with task plus autonomy; the 2024 agreement is not itself a qualifying work report. | Not stated | High for qualification; date of earliest source uncertain |

**Important date caveat:** The Schaeffler article gives the work start (early 2025) but the page does not expose a publication date in the extracted page, so an exact earliest-publication date cannot be responsibly assigned. The 2024 agreement announcement is not R2 evidence. GXO’s 2024-06-27 announcement explicitly documents its commercial deployment; a June 5 “first day” is mentioned in a video, but publication metadata for the video was not established here. Figure’s BMW source establishes the production trial and autonomous manipulation; I did not locate a qualifying earlier report than 2024-09-11.

## Scope checks and near-misses

- **Amazon / Agility:** Amazon’s 2023 announcement described a test at its robotics R&D facility, not customer production work. The Guardian’s 2023-10-19 report states Amazon’s “initial use” would be tote recycling, but describes planned work, not confirmed completed work. No Amazon pair added.
- **Toyota TMMC / Agility:** 2026 commercial agreement follows a successful pilot, but located announcement describes plans/rollout and does not itself supply the earlier pilot’s task-and-autonomy evidence. Not added on this evidence.
- **Schaeffler other than Cheraw:** the named group pair already counts once; the located Cheraw report meets R1–R3. Other sites/announcements do not create another pair.
- **Apptronik / Mercedes-Benz:** 2024 commercial agreement and 2025 reporting describe pilots/training and intended tasks, but the located sources did not clearly establish completed operational work meeting all R1–R3. No pair added.
- **Apptronik / Jabil:** 2025 collaboration says Apollo robots “will be used” for manufacturing/intralogistics tasks and describes a pilot/collaboration, but located material does not verify qualifying completed customer work. No pair added. **GXO:** no qualifying completed-work evidence located.
- **Figure other customers, logistics and homes:** no additional named external customer meeting all three rules located. BMW is the qualifying relationship; staged household videos/demos are not customer production work.
- **Boston Dynamics Atlas / Hyundai:** future deployment and manufacturing plans, not verified customer production work as of the cutoff. No pair.
- **Tesla Optimus:** no qualifying external-customer deployment located.
- **1X NEO / homes and EQT:** NEO home availability/orders and EQT’s “up to 10,000” partnership are not reports of a robot doing work in a paying home or portfolio company. No pair.
- **Sanctuary / Magna:** investment/partnership is not operational deployment evidence. Canadian Tire is the qualifying customer above.
- **Reflex Robotics, Persona AI, Humanoid (UK):** no sufficiently evidenced named customer operation located.
- **Dexterity Mech:** R1 yes: it is described as a dual-armed mobile manipulator/mobile robot, capable of moving through logistics facilities while manipulating boxes. However, sources found were launch/capability/marketing material, not evidence of Mech doing production work for a named external customer; no pair.
- **Hello Robot Stretch in care homes:** mobile manipulation is R1, but located evidence is research/assistive scenarios, not production work for a named paying-care customer. No pair.
- **Diligent Moxi:** R1 is met: its own page describes a compliant arm/hand, “mobile manipulation,” grabbing/pulling/opening objects without human assistance, and autonomous end-to-end tasks. Hospitals use it for supply/sample/medication delivery. However, the general vendor page does not identify a named hospital customer plus its specific work in one source; this check did not establish the earliest qualifying named-hospital pair. Do not count this as a blanket “hospital” customer.
- **Everyday Robots:** no additional qualifying named customer operation located.
- **Spot with arm:** arm-equipped Spot can manipulate, but located customer deployments were inspection/sensing or lacked reported manipulation work; no pair.
- **Unitree, UBTech, AgiBot abroad; Korean Rainbow/Samsung/LG; Japanese Kawasaki/Toyota humanoids:** located items were sales, pilots, announcements, demonstrations, supplier relationships, or China-based operations; no named non-China customer deployment meeting R1–R3 found. Kawasaki’s relationship to Dexterity is as a component supplier, not proof of a customer deployment.

## Final JSON

```json
{
  "as_of": "2026-10-18",
  "new_pairs": [
    {
      "vendor": "Sanctuary AI",
      "platform": "general-purpose humanoid (model unspecified)",
      "customer": "Canadian Tire Corporation",
      "job": "one-week Mark's retail-store pilot: merchandise picking/packing, cleaning, tagging, labelling and folding",
      "earliest_source": "https://sanctuary.ai/news/sanctuary-ai-deploys-first-humanoid-general-purpose-robot-commercially/",
      "publication_date": "2023-03-07",
      "quote": "week-long pilot at the CTC-owned store successfully tested the general-purpose robot in a ‘real-life’ store environment with 110 retail-related tasks completed correctly",
      "robots_disclosed": 1,
      "confidence": "medium-high; autonomy inferred from no teleoperation indication"
    }
  ],
  "known_non_china_pairs_earliest_sources": [
    {"vendor":"Figure AI","platform":"Figure 02","customer":"BMW Group","publication_date":"2024-09-11","url":"https://www.bmwgroup.com/en/news/general/2024/humanoid-robots.html","robots_disclosed":null,"confidence":"high"},
    {"vendor":"Agility Robotics","platform":"Digit","customer":"GXO Logistics","publication_date":"2024-06-27","url":"https://www.agilityrobotics.com/content/gxo-signs-industry-first-multi-year-agreement-with-agility-robotics","robots_disclosed":null,"confidence":"high"},
    {"vendor":"Agility Robotics","platform":"Digit","customer":"Schaeffler Group","work_started":"early 2025","publication_date":null,"url":"https://schaeffler-tomorrow.com/en/article/welcome-aboard-robo","robots_disclosed":null,"confidence":"high qualification; publication date unavailable"}
  ],
  "near_misses": ["Amazon/Agility","Toyota TMMC/Agility","Apptronik/Mercedes-Benz","Apptronik/Jabil","Apptronik/GXO","Boston Dynamics/Hyundai","1X/EQT portfolio companies","1X/paying homes","Sanctuary/Magna","Dexterity Mech (no named customer work evidence)","Hello Robot Stretch (no named paying care customer)","Diligent Moxi (customer-specific named-hospital pair not established)","Everyday Robots","Spot arm manipulation at customer sites","Unitree/UBTech/AgiBot abroad","Rainbow/Samsung/LG","Kawasaki/Toyota humanoids","Humanoid UK","additional Figure customers"],
  "coverage_limit": "No claim that every possible global deployment has been discovered; this is a targeted source-based review of the requested leads."
}
```
