# Discussion Forum: Module 08 - OSPFv2 Routing Concepts and Setup

**Course:** CIS-3322 Advanced Networking
**Certification Alignment:** Cisco CCNA 200-301 (Domain 3: IP Connectivity - 25%)
**Prepared by:** Professor Nash | Texas Wesleyan University

---

## Instructions

Read all three scenarios below and choose ONE to respond to. Identify your chosen scenario (A, B, or C) at the top of your initial post. Your post must address all three sub-questions for the scenario you select.

Initial posts are due Wednesday at 11:59 PM. Peer responses are due Sunday at 11:59 PM.

---

## Scenario A: Campus Network OSPF Deployment

A regional university is migrating from static routing to OSPFv2. The campus has a core router (R-CORE), four distribution routers (R-D1 through R-D4), and eight access routers (R-A1 through R-A8). Each access router has a LAN segment facing student devices. The network team is designing the OSPF deployment strategy before touching any production configuration.

Sub-questions:

1. Explain the Router ID selection process and why the design team should manually configure Router IDs on all routers rather than letting OSPF select them automatically. Include in your explanation what happens if the Router ID changes after OSPF is already running.

2. Each access router has one LAN interface facing student devices and one WAN interface facing the distribution layer. The team wants to prevent OSPF Hello packets from being sent onto the student LAN segments while still advertising those subnets to OSPF neighbors. Describe the exact configuration approach and explain why this is the correct practice.

3. The design team is debating whether to put all routers in Area 0 (single-area) or to use multiple areas with the distribution routers as ABRs. Identify one advantage and one disadvantage of multi-area OSPF compared to single-area OSPF at this scale, and state which approach you would recommend for this campus and why.

Write an initial post of 175-225 words addressing all three sub-questions.

---

## Scenario B: OSPF Neighbor Troubleshooting

A network engineer receives a trouble ticket: R1 and R2 were just connected via a new serial link, OSPF was configured on both routers, but `show ip ospf neighbor` shows no neighbors after five minutes. Both serial interfaces show up/up. The engineer runs the following commands and collects this output.

On R1:

```text
R1# show ip ospf interface Se0/0/0
Serial0/0/0 is up, line protocol is up
  Internet Address 10.0.12.1/30, Area 0
  Process ID 1, Router ID 1.1.1.1, Network Type POINT_TO_POINT, Cost: 64
  Timer intervals configured, Hello 10, Dead 40
```

On R2:

```text
R2# show ip ospf interface Se0/0/0
Serial0/0/0 is up, line protocol is up
  Internet Address 10.0.12.2/30, Area 0
  Process ID 1, Router ID 2.2.2.2, Network Type POINT_TO_POINT, Cost: 64
  Timer intervals configured, Hello 30, Dead 120
```

Sub-questions:

1. Based on the output above, identify the specific configuration mismatch causing OSPF neighbor failure. Explain exactly why this parameter must match on both ends for OSPF to form an adjacency.

2. Write the exact IOS commands to fix the mismatch on R2 so its OSPF timers match R1. Then explain what the Dead interval value must be relative to the Hello interval and why.

3. After fixing the timer mismatch, the engineer discovers a second problem: R2's Serial0/0/0 is in OSPF Area 1, not Area 0. Explain what happens at the OSPF neighbor state level when area IDs do not match, and write the command to correct R2's area assignment using the `ip ospf` interface command.

Write an initial post of 175-225 words addressing all three sub-questions.

---

## Scenario C: DR/BDR Election Design

A network operations team is deploying three routers (R1, R2, R3) on a shared Ethernet segment (a broadcast multi-access network). They need R1 to always be the Designated Router, R2 to always be the Backup Designated Router, and R3 to be a DROther. The default OSPF interface priority is 1 on all three routers.

Sub-questions:

1. Explain the two factors OSPF uses to elect the DR and BDR on a broadcast segment, in the order they are evaluated. Without any configuration change from defaults, which router becomes the DR and why?

2. Write the exact IOS commands to configure each router's OSPF interface priority to guarantee the desired election outcome (R1 = DR, R2 = BDR, R3 = DROther). Assign specific priority values and explain why priority 0 is appropriate for R3.

3. After the DR/BDR election is complete, R1 fails and R2 becomes the DR. A new router R4 is added to the segment with a higher priority than all others. Explain whether R4 will become the new DR immediately when it comes online, and why OSPF DR election behaves this way. Include the term "non-preemptive" in your answer.

Write an initial post of 175-225 words addressing all three sub-questions.

---

## Discussion Rubric (10 Points Total)

| Component | Points | Criteria |
|---|---|---|
| Initial Post - Technical Accuracy | 3 | All three sub-questions answered with correct OSPF terminology and accurate concept application |
| Initial Post - Depth and Analysis | 2 | Responses analyze operational scenarios, diagnose failures, or evaluate design trade-offs |
| Initial Post - Word Count | 1 | Post falls within the 175-225 word range |
| Peer Response 1 | 2 | Substantive reply (50+ words) that adds a technical detail, corrects an error, or extends the scenario analysis |
| Peer Response 2 | 2 | Substantive reply (50+ words) meeting the same criteria as Peer Response 1 |

---

## Professor Nash's Note

OSPF is the protocol I see most often misconfigured in production environments, not because it is complicated, but because there are several configuration elements that must match on both ends — and there is no error message when they do not. The router simply does not form a neighbor relationship and sits quietly. Mismatched timers, mismatched areas, mismatched subnet masks — none of these generate alerts. The network just silently stops converging. That is why reading `show ip ospf neighbor` and `show ip ospf interface` fluently is not optional. It is your primary diagnostic tool, and understanding exactly what each field means is what separates an engineer who troubleshoots in five minutes from one who spends five hours.
