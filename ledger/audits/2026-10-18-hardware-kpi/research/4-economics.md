# Robots/HARDWARE KPI research (4/5): economics as a proxy for robot labor

**Research date: 17 October 2026.** Scope: general-purpose autonomous physical automation (humanoids/mobile manipulators), not industrial arms/cells or robotaxis. Prices below are not directly comparable: research platforms, home robots, deployments, and event appearances are different products. “Not found” means no verifiable public figure in the sources reviewed, not that no private quote exists.

## Bottom line

Economics supplies useful evidence, but not yet a robust standalone KPI for autonomous robot labor.

* **Robot prices** are easy to quote and increasingly public, but mainly measure the cost of buying a platform, not its autonomous productive work. Cheapest listed humanoids are expressly consumer/research/education products; many capable commercial systems are custom-quoted. List-price series can track access/capital cost, not substitution.
* **Robot-hour rates** would be the closest economic signal. For the requested general-purpose products, however, published rates are sparse, usually monthly or event-rental prices, and typically omit utilization, support labor, deployment, and teleoperation. Agility’s reported monthly RaaS figure appears to be an access charge, not verified autonomous productive hours. 1X’s official offer explicitly includes remote “Expert” supervision for hard tasks, a clear warning against equating subscription price with autonomous labor.
* **Financial filings offer the best recurring hard evidence.** UBTECH reports full-size humanoid product/service revenue and units; Unitree’s 2026 IPO prospectus reportedly breaks humanoid sales down by end use, showing a large research/education share. But revenue is not labor displaced, and the disclosures do not quantify autonomy or customer-side human support. Tesla’s 10-K does not disclose Optimus revenue. AgiBot remains private / IPO reporting is not a standardized, audited time series available in filings reviewed.
* **BOM/cost estimates** are scenario-based analyst estimates, not audited realized costs, and the samples are too sparse and inconsistent for a dependable KPI.
* No credible, recurring estimate was found of aggregate wages actually displaced or labor value autonomously performed by general-purpose robots.

**Recommendation:** Do not adopt “$ per robot-hour” or aggregate robot revenue as the sole KPI today. If the section wants economics, track **annual commercial full-size humanoid revenue and units from audited issuer filings, with end-use split where disclosed** as a secondary commercialization indicator—not as autonomy or labor displacement. The stronger future KPI would be **verified customer-paid autonomous productive hours / robot**, net of remote operator and onsite support hours, but no public recurring dataset currently supports it.

## A. Disclosed robot prices and service rates

### List / purchase prices and company targets

| Company / model | Disclosed figure and date | What it is / limitation |
|---|---|---|
| **Unitree G1** | Official store currently lists **from $13,500 USD** (accessed 17 Oct 2026); official model page says from $13.5k, excluding tax/shipping. | “From” price; options/EDU variants differ. Not a demonstrated turnkey labor service. [Official product listing](https://shop.unitree.com/products/unitree-g1) |
| **Unitree H1** | Store lists **$90,000**, while labeling “Contact us for the real price” (accessed 17 Oct 2026). | Treat as a storefront placeholder, not verified transaction price. [Official listing](https://shop.unitree.com/products/unitree-h1) |
| **Unitree H2** | Official store: **$29,900** (accessed 17 Oct 2026). H2 Plus: $100,000. | Listed retail amounts, tax/shipping/availability unclear; not demonstrated labor economics. [Official collection](https://shop.unitree.com/collections/humanoid-robot) |
| **Unitree R1** | Official store: **from $4,900** (accessed 17 Oct 2026). | Starting price; configuration/skills and availability matter. [Official listing](https://shop.unitree.com/products/unitree-r1) |
| **UBTECH Walker S2** | **No public list price verified** (Oct 2026). | Sales/contracts are not equivalent to public price. Avoid repeating unsourced “price” estimates. |
| **AgiBot / Zhiyuan** | **No official public purchase price verified** (Oct 2026). | A public rental offer is not a purchase price; see below. |
| **Tesla Optimus** | Elon Musk described a future target of **$20,000–$30,000** in 2024/25 public statements; no consumer sale/list price was verified by Oct 2026. | Target, not offer, quote, or realized transaction. Tesla’s 2025 10-K describes development plans, not Optimus sales revenue. [Tesla 2025 Form 10-K](https://ir.tesla.com/_flysystem/s3/sec/000162828026003952/tsla-20251231-gen.pdf) |
| **Figure** | **No public purchase price verified** (Oct 2026). | Figure’s commercial arrangements are not disclosed as a generally available price sheet. |
| **1X NEO** | Official order page: **$499/month subscription** or **$20,000 ownership**, $200 fully refundable deposit; US deliveries stated to start in 2026 (page published 10 Sep 2025; checked 17 Oct 2026). | Home robot, not workplace labor. Importantly, early owners get “basic autonomy”; complex tasks can use a scheduled remote 1X Expert, and app/VR remote piloting is described. The offer does **not** establish labor delivered per dollar. [Official order page](https://www.1x.tech/order) |
| **Agility Digit** | **No official public purchase price verified.** Secondary reporting around 2026 repeatedly gives about **$8,500/month**, sometimes plus a **$25,000 deployment fee**; Agility’s FAQ does not give a public price. | Treat $8.5k as reported, not an official rate card or verified per-hour work price. The number’s source is an investor-deck/reporting trail, not a published tariff. [Agility FAQ](https://www.agilityrobotics.com/faq); [The Robot Report, 7 Sep 2026](https://www.therobotreport.com/agility-robotics-reports-18m-revenue-ahead-of-humanoid-spac/) |

### RaaS, hourly/monthly and rental prices

| Provider / product | Public rate evidence | Interpretation / autonomy check |
|---|---|---|
| **Agility Digit RaaS** | Approximately **$8,500 per robot per month** (about $102,000/year), reported 7 Sep 2026; sometimes reported with $25,000 deployment charge. | Secondary reports describe RaaS access; no verified official hourly tariff, uptime/utilization basis, included support scope, or disclosure that customer supplies no operator. Dividing monthly fee by 730 hours would be a false “robot-hour” rate: scheduled work hours and autonomous productive hours are unknown. [The Robot Report](https://www.therobotreport.com/agility-robotics-reports-18m-revenue-ahead-of-humanoid-spac/) |
| **Formic** | Formic advertises robotics-as-a-service with usage/hourly or monthly payment structures, but **no general-purpose humanoid robot hourly/monthly price** was found. Its business is chiefly application-specific industrial automation. | Exclude from this KPI’s target population; a price for a robot cell would violate the stated scope. [Formic RaaS explainer](https://formic.co/resources/articles/robots-as-a-service-raas) |
| **Reflex Robotics** | Company site describes its general-purpose mobile manipulator, but **no public hourly/monthly rate or verified list price** found (Oct 2026). | Unpriced claims about affordability or labor cost are not observed transactions. [Company](https://reflexrobotics.com/) |
| **Robotera** | **No public purchase or RaaS tariff** found on company site (Oct 2026). | No verifiable price series. [Company](https://www.robotera.com/en/) |
| **China humanoid rentals—event use** | Contemporary 2025 reporting put event rentals at around **RMB 10,000–20,000/day** (reported 16 Mar 2026 as the 2025 spring peak); later reports give mid-range **RMB 2,800–5,000/day** (~$400–700) and premium AgiBot A2 around **$1,000–$1,380/day** (2026). | These are event/show appearance prices, with transport, staff, and scripted performance often bundled or unspecified—not productive work hours. A provider’s operator and robot at an event may be the thing being rented. Sources: [Hello China Tech, 16 Mar 2026](https://hellochinatech.com/p/robots-for-rent-humans-included); [Forbes, 2 Mar 2026](https://www.forbes.com/sites/johnkoetsier/2026/03/02/you-can-now-rent-this-robot-for-1000-per-day/). |
| **China humanoid rentals—work** | **No reliable, comparable day/hour rate for unsupervised general-purpose work verified.** | Event rental rates should not be recast as work rates. No source establishes that rental includes autonomous labor without human attendants/teleoperators. |

**Can a $/robot-hour versus human wage series be built?** Not credibly from these figures. Monthly RaaS is a price for access, not an observed hours denominator; acquisition prices require lifespan, financing, utilization, maintenance, integration and labor-support assumptions. Event-day rates buy entertainment and often human service. Even a defensible cost/hour series measures cost competitiveness, not autonomy. A valid metric would require: customer invoice; actual robot-on-task hours; task output/quality; human onsite hours and remote operator minutes; intervention rate; and consistent task/wage benchmark. No public recurring dataset reviewed reports all of these.

## B. Revenue in filings and revenue by end use

### UBTECH (HKEX: 9880): strongest disclosed issuer data

UBTECH’s **2025 annual report**, published 21 Apr 2026, is primary evidence. It reports **RMB 2.001 billion total 2025 revenue**; full-size embodied-AI humanoid robots’ product-and-service revenue was about **RMB 820.6 million** (reported 41% of total), versus **RMB 35.6 million in 2024**; full-size robot sales reached **1,079 units in 2025**, versus 3 in 2024. The report separately says sales of *non-embodied intelligent humanoid robot products and services* reached **12,759 units**—do not merge these categories or claim that all units were full-size working robots. [UBTECH 2025 annual report (PDF)](https://owebsite-cdn.ubtrobot.com/resources/file/2026/04/21/797179114676293.pdf) (published 21 Apr 2026).

UBTECH’s 2026 interim reporting is summarized by company materials as full-size embodied-AI humanoid revenue up 1,445% to **RMB 590 million**; exact interim-period accounting/category should be taken from the underlying official interim report before using it as a continuing series. The currently available signal demonstrates a reporting cadence (annual and interim), but these revenues include products **and services**, and do not split autonomous work from R&D, demos, deployment, teleoperation, or training. [UBTECH investor/company releases](https://www.ubtrobot.com/en/investor) (the specific interim report was not independently inspected here; mark that figure provisional).

### Unitree: prospectus end-use mix, not “all labor”

Unitree’s investor-relations page links its **2026 prospectus** and periodic reports. The prospectus disclosures, reported by The Robot Report on **25 Mar 2026**, indicate that for the **first nine months of 2025**, **73.6% of humanoid revenue was from research and education**, while **9.01%** was from industrial applications. This is valuable because it warns that headline humanoid sales are not synonymous with industrial labor substitution; the residual end-use categories are not silently assignable to productive work. Use the underlying prospectus tables and definitions for a formal series. [Unitree investor relations / filings](https://www.unitree.com/investor); [The Robot Report, 25 Mar 2026](https://www.therobotreport.com/unitree-ipo-shows-a-real-hardware-business-the-humanoid-case-is-still-early/).

**Limitation:** the reported mix is for nine months, and the exchange response/prospectus classification is revenue by customer/application, not measured hours, operational status, or autonomy. Unitree is listed in 2026 and its filings could form a recurrent issuer series, but historical prospectus periods and future reporting need harmonized scope.

### Other companies

* **AgiBot:** 2025 reports cite company revenue around **RMB 1.05–1.1 billion**, and third-party market research says 2025 humanoid sales revenue exceeded **$140 million**. These are not the same measure (company revenue vs estimated robot sales revenue); they do not form an audited filing-based series or a validated end-use split. As of this review, an official standardized public filing with an audited revenue breakdown was **not verified**. [Counterpoint Research, 23 Feb 2026](https://counterpointresearch.com/en/insights/Chinese-Enterprises-Leading-Global-Commercialization-Wave-of-Humanoid-Robots); [Reuters on planned IPO, 10 Oct 2025](https://www.reuters.com/world/asia-pacific/chinese-robot-maker-agibot-plans-hong-kong-ipo-next-year-sources-say-2025-10-10/).
* **Tesla:** the 2025 Form 10-K, dated for year ended 31 Dec 2025, discusses Optimus as a general-purpose autonomous humanoid and development/manufacturing plans, but does **not** report Optimus product revenue or units sold. Tesla’s broad segment financials cannot be used to infer robot labor. [Tesla 2025 Form 10-K (PDF)](https://ir.tesla.com/_flysystem/s3/sec/000162828026003952/tsla-20251231-gen.pdf).
* **Hyundai / Boston Dynamics:** Hyundai’s consolidated filings do not provide a separately quantified Boston Dynamics humanoid (Atlas) revenue or labor-output series verified here. Boston Dynamics has had robot sales/services (notably Spot and Stretch) but those are not a public revenue breakout for general-purpose humanoids. **No comparable humanoid revenue figure verified.**
* **Agility Robotics:** Sep 2026 reporting says Agility reported **$1.8 million revenue** in the context of its planned SPAC. This is company-level revenue, not verified Digit-only revenue and not a disclosed autonomy-adjusted wage-saving amount. [The Robot Report, 7 Sep 2026](https://www.therobotreport.com/agility-robotics-reports-18m-revenue-ahead-of-humanoid-spac/).
* No other issuer reviewed furnished a public, recurring general-purpose humanoid revenue series with end-use split and human-support disclosure.

**Assessment:** UBTECH’s audited product/service revenue + units is the most promising recurring **commercialization** series. Unitree’s revenue end-use breakdown is arguably even more diagnostic of whether sales are to real industry versus labs, but the reported mix is not an autonomy measure and requires table-level extraction each reporting period. Neither revenue nor shipment numbers validate that the machines performed work without human labor.

## C. Humanoid BOM / cost-down estimates

| Source and date | Estimate | Caveat |
|---|---|---|
| **Goldman Sachs**, updated humanoid market research, **2024** | Manufacturing cost estimate roughly **$30,000–$150,000 per robot**, reported as about a 40% reduction from its prior estimate. [Goldman article](https://www.goldmansachs.com/insights/articles/the-global-market-for-robots-could-reach-38-billion-by-2035) | Wide modeled range, not cost of a standardized robot; the linked article foregrounds market forecast and does not provide a simple, annual realized-BOM series. The $30k–$150k estimate is reported in secondary summaries of Goldman’s research; exact original table/assumptions not verified. |
| **Morgan Stanley**, **14 May 2025** | Estimated a humanoid cost around **$200,000 in 2024 in high-income countries**; forecast substantial decline over time. [Morgan Stanley](https://www.morganstanley.com/insights/articles/humanoid-robot-market-5-trillion-by-2050) | Broad estimate of robot cost, not clearly equivalent to factory BOM; geography and product capability affect comparability. Forecasts are not observed prices. |
| **Bank of America Global Research**, **12 Mar 2026** | Estimates a “built-in-China” humanoid BOM of **$35,000 in 2025**, expected to be roughly halved to **below $20,000 by 2028**. [BofA report PDF](https://institute.bankofamerica.com/content/dam/transformation/physical-ai-part-2.pdf) | Analyst BOM model/forecast; “China-built” assumptions and component scope differ from Morgan Stanley/Goldman; below-$20k is forecast, not actual cost. |

**KPI suitability: low.** This is a short, heterogeneous, analyst-estimate history with infrequent publications and different definitions (manufacturing cost, BOM, market price, income-country build). Estimates can show directional cost-down, but cannot be assembled into a trustworthy annual global series without adopting one analyst’s methodology and accepting proprietary assumptions. It also says nothing about autonomous task performance or labor displacement.

## D. Wages displaced / labor value performed

No trustworthy recurring estimate was found for **total wages displaced by general-purpose robots**, nor a direct measure of labor value autonomously performed by them. The commonly cited headline “robot market size,” TAMs (Goldman $38bn humanoid market by 2035; Morgan Stanley trillion-dollar long-run scenarios), and robot sales revenue are forecasts or vendor revenue—not wages displaced. Company/customer announcements about pilots, contracts, units, or “worker-equivalent” capacity do not establish net displacement, hours of autonomy, or the labor cost of supervisors and maintenance.

A credible labor-value estimate would require an agreed counterfactual: task output actually completed, quality and throughput, paid hours removed or avoided, robot runtime and downtime, operator/babysitter/repair hours, and the wage for that task/location. No source here reports those elements on a comparable time series. Hence **no defensible $ total** is offered.

## KPI verdict

| Candidate | History / cadence | Trustworthiness | Autonomy verification | Verdict |
|---|---|---|---|---|
| Listed robot price / cheapest available humanoid | Several current prices; historic comparable basket weak | Official offer for some models, target/placeholder for others | None | Useful context chart only; changes product/config mix and price is not work. |
| RaaS $/robot-month or $/hour | Very sparse, often secondhand; no uniform rate | Weak/moderate | At most weakly suggestive if customer pays recurring fee; cannot infer labor hours/operator burden | Not yet a series. |
| Robot sales/revenue | Annual/interim filing cadence for UBTECH, emerging Unitree; fragmented elsewhere | Best where audited filings and product category available | No: research sales, demos, service, and supervised operation can all earn revenue | Best secondary commercialization KPI; always annotate end-use and units. |
| Analyst BOM / cost estimates | 2024–26 snapshots | Method-dependent estimates | None | Research context, not KPI. |
| Wages displaced / autonomous labor value | No credible public series located | Low | Would be ideal if directly measured | No usable current data. |

**Interpretation of “payment verifies autonomy”:** a customer’s repeated payment for a robot is evidence of willingness to pay and deployment, but it does not alone imply autonomy. It becomes meaningful autonomy evidence only when contracts/invoices are explicitly for delivered task-hours/output and vendor/customer disclosures state operator staffing and interventions. None of the public pricing evidence above meets that bar. The 1X NEO order page actually cautions that the $499/$20k product can rely on remote experts for complex tasks.

## Sources (deep links; accessed/reviewed 17 Oct 2026 unless publication date shown)

1. [Unitree official humanoid store collection](https://shop.unitree.com/collections/humanoid-robot); [G1](https://shop.unitree.com/products/unitree-g1), [R1](https://shop.unitree.com/products/unitree-r1), [H1](https://shop.unitree.com/products/unitree-h1).
2. [Unitree Investor Relations / prospectus and reports](https://www.unitree.com/investor).
3. [UBTECH 2025 Annual Report (PDF; published 21 Apr 2026)](https://owebsite-cdn.ubtrobot.com/resources/file/2026/04/21/797179114676293.pdf).
4. [UBTECH Investor Relations](https://www.ubtrobot.com/en/investor).
5. [1X NEO official order / autonomy and price page (published 10 Sep 2025)](https://www.1x.tech/order).
6. [Agility FAQ](https://www.agilityrobotics.com/faq); [The Robot Report, Agility revenue/RaaS report, 7 Sep 2026](https://www.therobotreport.com/agility-robotics-reports-18m-revenue-ahead-of-humanoid-spac/).
7. [Formic RaaS description](https://formic.co/resources/articles/robots-as-a-service-raas); [Reflex Robotics](https://reflexrobotics.com/); [Robotera](https://www.robotera.com/en/).
8. [Hello China Tech, “Robots for Rent, Humans Included,” 16 Mar 2026](https://hellochinatech.com/p/robots-for-rent-humans-included); [Forbes, AgiBot rental, 2 Mar 2026](https://www.forbes.com/sites/johnkoetsier/2026/03/02/you-can-now-rent-this-robot-for-1000-per-day/).
9. [The Robot Report, Unitree IPO prospectus analysis, 25 Mar 2026](https://www.therobotreport.com/unitree-ipo-shows-a-real-hardware-business-the-humanoid-case-is-still-early/).
10. [Tesla 2025 Form 10-K (PDF)](https://ir.tesla.com/_flysystem/s3/sec/000162828026003952/tsla-20251231-gen.pdf).
11. [Counterpoint Research, Chinese humanoid commercialization, 23 Feb 2026](https://counterpointresearch.com/en/insights/Chinese-Enterprises-Leading-Global-Commercialization-Wave-of-Humanoid-Robots); [Reuters on AgiBot IPO plans, 10 Oct 2025](https://www.reuters.com/world/asia-pacific/chinese-robot-maker-agibot-plans-hong-kong-ipo-next-year-sources-say-2025-10-10/).
12. [Goldman Sachs humanoid market research](https://www.goldmansachs.com/insights/articles/the-global-market-for-robots-could-reach-38-billion-by-2035); [Morgan Stanley, 14 May 2025](https://www.morganstanley.com/insights/articles/humanoid-robot-market-5-trillion-by-2050); [BofA Global Research PDF, 12 Mar 2026](https://institute.bankofamerica.com/content/dam/transformation/physical-ai-part-2.pdf).
