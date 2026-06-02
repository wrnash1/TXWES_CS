# Discussion Forum: Module 06 - EtherChannel Link Aggregation

**Course:** CIS-3322 Advanced Networking
**Certification Alignment:** Cisco CCNA 200-301 (Domain 2: Network Access - 20%)
**Prepared by:** Professor Nash | Texas Wesleyan University

---

## Instructions

Read all three scenarios below and choose ONE to respond to. Identify your chosen scenario (A, B, or C) at the top of your initial post. Your post must address all three sub-questions for the scenario you select.

Initial posts are due Wednesday at 11:59 PM. Peer responses are due Sunday at 11:59 PM.

---

## Scenario A: Data Center Uplink Capacity Planning

A regional bank's data center has three distribution switches that connect to the core. Each distribution switch currently has a single 10G uplink to the core, and traffic analysis shows these uplinks are saturating at 80-90% utilization during business hours, causing latency spikes on trading applications. The network team is evaluating whether to add EtherChannel bundles or upgrade to higher-speed individual links.

Sub-questions:

1. Explain how EtherChannel increases effective bandwidth between two switches. Be specific about how traffic is distributed across member links and whether a single application session can exceed one link's throughput. Use the term "flow" in your explanation.

2. The network team is considering bundling four 10G links between each distribution switch and the core switch. Compare the use of LACP active/active versus static (on/on) EtherChannel for this scenario. What does the static mode lack that LACP provides, and in what operational scenario does this difference matter most?

3. The trading application generates large sustained transfers between two specific servers. A network engineer notices that even after configuring a four-link EtherChannel, these transfers still only use approximately 25% of the total bundle bandwidth. Explain why this happens and what change to the EtherChannel load-balance configuration would help distribute this traffic more effectively across all four links.

Write an initial post of 175-225 words addressing all three sub-questions.

---

## Scenario B: EtherChannel Failure Analysis

A university's network team received a trouble ticket reporting intermittent packet loss and reduced bandwidth on the link between the Library building's access switch (SW-LIB) and the distribution switch (SW-DIST-1). The EtherChannel between them was configured using PAgP. When the engineer runs `show etherchannel summary` on SW-LIB, the output shows: Po1(SU) PAgP Fa0/23(P) Fa0/24(s).

Sub-questions:

1. Based on the `show etherchannel summary` output, explain what each flag (SU, P, and s) indicates. What does the suspended port (s) mean in terms of traffic flow, and why might this explain the reported intermittent packet loss and reduced bandwidth?

2. List three specific configuration parameters you would check on Fa0/24 to find the mismatch causing the suspension. For each parameter, describe what command you would use to inspect it and what mismatched value would cause a port to be suspended.

3. After identifying and fixing the configuration mismatch on Fa0/24, the port remains suspended. A colleague suggests removing the port from the channel-group and re-adding it to force re-negotiation. Write the exact IOS commands to remove Fa0/24 from channel-group 1 and re-add it in PAgP desirable mode. Then explain whether PAgP desirable on SW-LIB requires PAgP desirable or PAgP auto on SW-DIST-1 for the channel to form.

Write an initial post of 175-225 words addressing all three sub-questions.

---

## Scenario C: Multi-Vendor EtherChannel Design

A technology company is deploying a new campus network with a mixed-vendor environment: the Core layer uses Cisco Nexus switches, the Distribution layer uses Cisco Catalyst 9300s, and the Access layer uses a competing vendor's switches that support LACP but not PAgP. The network architect must choose the correct EtherChannel protocol for each tier of the design.

Sub-questions:

1. Identify which EtherChannel protocol must be used on the Access layer uplinks (between the competing vendor's switches and the Cisco Catalyst Distribution switches) and explain why PAgP cannot be used in this scenario. What happens if the Distribution switch's Access-to-Distribution EtherChannel is configured with PAgP desirable while the competing vendor's switch is configured with LACP active?

2. The architect wants the Distribution-to-Core EtherChannels to use LACP and wants the Cisco Nexus (Core) to always initiate negotiation while the Catalyst 9300 (Distribution) passively responds. Write the LACP mode configuration for both the Core switch and the Distribution switch to achieve this behavior.

3. The IT manager asks whether EtherChannel requires the two ends of a bundle to be directly connected or whether traffic can traverse an intermediate switch between the two EtherChannel endpoints. Explain the EtherChannel direct-connection requirement and what the practical consequence is if an intermediate switch is accidentally inserted between two EtherChannel member ports.

Write an initial post of 175-225 words addressing all three sub-questions.

---

## Discussion Rubric (10 Points Total)

| Component | Points | Criteria |
|---|---|---|
| Initial Post - Technical Accuracy | 3 | All three sub-questions answered with correct EtherChannel terminology and accurate concept application |
| Initial Post - Depth and Analysis | 2 | Responses analyze operational scenarios, diagnose failures, or evaluate design trade-offs |
| Initial Post - Word Count | 1 | Post falls within the 175-225 word range |
| Peer Response 1 | 2 | Substantive reply (50+ words) that adds a technical detail, corrects an error, or extends the scenario analysis |
| Peer Response 2 | 2 | Substantive reply (50+ words) meeting the same criteria as Peer Response 1 |

---

## Professor Nash's Note

EtherChannel misconfigurations are extremely common in production environments — and they are one of the few things that can silently reduce your network's bandwidth by half without triggering any alarms. A suspended port passes no traffic, the port-channel stays up, and monitoring tools show green. Only when someone notices the throughput ceiling do they realize half the bundle is gone. That is why reading `show etherchannel summary` fluently is not optional — it is one of the most practical skills in this course.
