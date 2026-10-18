# China coverage check (2026-10-18)

Scope: production work in mainland China/HK/Taiwan, applying R1–R3 in `RULES.md`. I counted a pair only where the opened source identifies the maker, named customer, concrete live work and no teleoperation; planned deployments and test/training activity are excluded. “Earliest found” is bounded by this search, not a claim that no earlier qualifying publication exists.

## Additional qualifying pair

### UBTech / Dongfeng Liuzhou Motor (东风柳汽)
- **Platform:** Walker S1 industrial humanoid.
- **Customer:** Dongfeng Liuzhou Motor Co., Ltd. (Dongfeng Liuzhou / 东风柳汽).
- **Work:** production-floor sorting, binning and parts handling in the commercial-vehicle assembly shop.
- **Earliest qualifying source found:** 2025-06-19, [Dongfeng Motor company news](https://www.dfmc.com.cn/news/company/news_20250619_0945.html) (opened). It reports the Walker S1 robots “在东风柳汽商用车智能制造工厂总装车间” and says eight units perform sorting/boxing; the described on-floor work is more than an order or testbed. Reported as a live post-deployment operation. The source is customer-side, hence strong identity evidence.
- **Robots disclosed:** 8 in the described operation (later order/deployment announcements mention 20 planned; not counted as deployed here).
- **Confidence:** High. Mobile humanoids manipulate parts/packages; production shop and named customer are explicit. Autonomy is not explicitly quantified, but no teleoperation is indicated.

### RobotEra / China Post (中国邮政)
- **Platform:** Star Motion M7 (星动M7), humanoid logistics robot.
- **Customer:** China Post Group, at Guangzhou Postal District Center.
- **Work:** parcel singulation/sorting supply—identify, grasp, turn labels face-up, and place parcels for downstream automation.
- **Earliest qualifying source found:** 2026-05-15, [IT之家/Sina Finance](https://finance.sina.com.cn/tech/digi/2026-05-15/doc-inhxxwvn8147060.shtml) (opened). Quote: “此次在中国邮政广州邮区中心正式上岗的‘机器人分拣员’，来自星动纪元的自研人形机器人星动M7”; it also describes autonomous parcel recognition and handling.
- **Robots disclosed:** not stated in this source.
- **Confidence:** High. Source explicitly says formally on duty at a live postal centre and gives the manipulation job; autonomous recognition is described. This is the already-listed Robotera/China Post pair (星动纪元), not an additional pair.

### RobotEra / SF Express (顺丰)
- **Platform:** Star Motion M7 / RobotEra humanoid logistics platform (exact model not disclosed for the initial SF site).
- **Customer:** SF Express / 顺丰 (parent operating company; source calls the client a major logistics company and identifies SF elsewhere, but does not name it in the described site).
- **Status: provisional, not counted.** The opened [Economic Observer, 2026-06-02](https://m.eeo.com.cn/2026/0602/900202.shtml) describes actual sorting at a second unnamed major logistics company, but the passage does not name SF; it says the vendor partnered after a site competition. A separate source reports a signed partnership, which alone does not establish the named customer’s operating site. Excluded under R2’s named-customer requirement.

## Earliest qualifying sources for specified Chinese ledger pairs

| Pair | Earliest qualifying source found | Evidence / robots | Confidence |
|---|---|---|---|
| Spirit AI / CATL (宁德时代) | 2025-12-18, [IT之家](https://www.ithome.com/0/905/841.htm) (opened by visit tool; page extraction returned unrelated current links, so corroborate with [Spirit AI official news](https://www.spirit-ai.com/news/22), search result date 2025-12-18; URL opened via search result). The source reports the CATL Zhongzhou PACK line running and “小墨” accurately inserting battery connectors. | Xiao Mo humanoid; count undisclosed. Production operation and physical manipulation explicit; no remote control reported. | Medium-high (official vendor source; third-party report supports). |
| AgiBot / Longcheer (龙旗科技) | **No qualifying source established in this coverage pass.** Searches found order/strategic cooperation reports (e.g. [STCN, 2025-10-09](https://www.stcn.com/article/detail/3370102.html)), but those describe future deployments, not reported production work. Therefore no earliest qualifying date can responsibly be assigned here. | — | Low / unresolved |
| Robotera / China Post (中国邮政) | 2026-05-15, [IT之家/Sina Finance](https://finance.sina.com.cn/tech/digi/2026-05-15/doc-inhxxwvn8147060.shtml) (opened). Quote and details above: M7 “正式上岗” at Guangzhou Postal District Center, autonomous parcel handling. | M7; count not disclosed. | High on deployment; vendor-name collision/identity requires ledger verification. |
| Galbot / CATL (宁德时代) | 2026-06-25, [Beijing News](https://www.bjnews.com.cn/detail/1782365499129699.html) (opened). Quote: “目前已在宁德时代量产线上7×24小时工作超过3个月”; describes module/battery-pack material transfer and states “零遥操、全自主连续作业.” Acceptance was in March 2026, but the source’s publication date is the earliest qualifying source located. | Galbot S1; count not disclosed. | High |

## Near-misses / exclusions

- **UBTech / Zeekr:** Walker S Lite’s 21-day搬运 stint was described as “实习” and other Zeekr work as实训; excluded as training/testing, not demonstrated production work ([Jiefang Daily, 2025-04-23](https://www.jfdaily.com/wx/detail.do?id=898000); opened via search results, not relied on for count).
- **UBTech / NIO:** 2024 coverage calls its factory activity 实训; not enough to establish production work. NIO’s later statement mentions humanoid inspection but does not identify UBTech. Excluded.
- **UBTech / Foxconn:** 2025 announcement is strategic cooperation/testing and validation in real manufacturing scenarios, not reported production work; excluded.
- **SmartMore / HKC (惠科):** September 2025 reports more than 1,000 robots to be deployed over three years and specifies tasks, but these are purchase/deployment plans, not evidence of work already performed; excluded.
- **AgiBot / Longcheer:** near-miss as above; 2025-10 partnership/orders are not execution evidence. Later April 2026 reports of production-line work postdate this pass’s uncovered earliest date; source search did not establish a qualifying pre-existing report.
- **Spirit AI / CATL and Galbot / CATL:** CATL investment, validation/acceptance, and partnership announcements alone do not count; use the operational reports cited above.
- **China Post / RobotEra:** pre-May announcements and broad lists of sites/hours do not independently meet R2; the May 15 article is the earliest located with a named China Post operation and task.

## Search limitations

Search used the prescribed Jina search and visit scripts with Chinese-language queries covering factory/line deployment and major named vendors. Several reported deployments are behind reposts or terse vendor press releases, so “every” is necessarily limited by public indexed evidence. The strongest additional finding is UBTech/Dongfeng Liuzhou. Do not count RobotEra/SF until an opened source explicitly names SF as the operating customer and gives the work.

```json
{
  "as_of": "2026-10-18",
  "new_qualifying_pairs": [
    {"vendor": "UBTech", "customer": "Dongfeng Liuzhou Motor", "platform": "Walker S1", "earliest_source_date": "2025-06-19", "robots_disclosed": 8, "confidence": "high"}
  ],
  "new_provisional_not_counted": [
    {"vendor": "RobotEra / Xingdong Jiyuan", "customer": "SF Express", "reason": "operating customer not named in the opened production-work passage"}
  ],
  "known_china_pairs_earliest_found": [
    {"vendor": "Spirit AI", "customer": "CATL", "earliest_source_date": "2025-12-18", "platform": "Xiao Mo", "robots_disclosed": null, "confidence": "medium-high"},
    {"vendor": "AgiBot", "customer": "Longcheer", "earliest_source_date": null, "status": "not established; available 2025 source describes future order/deployment"},
    {"vendor": "Robotera", "customer": "China Post", "earliest_source_date": "2026-05-15", "platform": "Star Motion M7", "robots_disclosed": null, "confidence": "high", "identity_note": "vendor alias may overlap with Xingdong Jiyuan; verify ledger identity"},
    {"vendor": "Galbot", "customer": "CATL", "earliest_source_date": "2026-06-25", "platform": "Galbot S1", "robots_disclosed": null, "confidence": "high"}
  ],
  "near_misses": ["UBTech/Zeekr: training", "UBTech/NIO: training; later source lacks maker attribution", "UBTech/Foxconn: validation/cooperation only", "SmartMore/HKC: planned deployment", "AgiBot/Longcheer: order/plan not work", "RobotEra/SF: customer unconfirmed"]
}
```
