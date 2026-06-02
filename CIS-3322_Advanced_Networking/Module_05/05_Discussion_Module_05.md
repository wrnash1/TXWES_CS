# Discussion Forum: Module 05 - Spanning Tree Protocol (STP & RSTP)

**Course:** CIS-3322 Advanced Networking
**Certification Alignment:** Cisco CCNA 200-301 (Domain 2: Network Access - 20%)
**Prepared by:** Professor Nash | Texas Wesleyan University

---

## Instructions

Read all three scenarios below and choose ONE to respond to. Identify your chosen scenario (A, B, or C) at the top of your initial post. Your post must address all three sub-questions for the scenario you select.

Initial posts are due Wednesday at 11:59 PM. Peer responses are due Sunday at 11:59 PM.

---

## Scenario A: Campus Network Broadcast Storm

A university campus network went down during finals week. IT staff observed 100% CPU utilization on all switches and thousands of duplicate frames appearing simultaneously across all segments. The network had no STP configured on several Access layer switches that were recently added to expand capacity in a dormitory building. When the switches were added, the installing technician connected them to the existing network using two uplinks each to improve redundancy.

Sub-questions:

1. Explain precisely why a broadcast storm occurs when redundant switch links exist without STP. Include in your explanation what happens to a single ARP broadcast frame when it enters a loop and why the problem escalates so rapidly rather than stabilizing.

2. After STP is enabled on all switches, describe how the spanning tree algorithm determines which port to block on the newly added dormitory switches. What information does each switch examine to make that decision, and what port role is assigned to the port that gets blocked?

3. The campus network has 15 distribution-area VLANs. The network team wants each of the two core switches to be the root bridge for roughly half the VLANs to distribute traffic load. What Cisco STP feature supports per-VLAN root bridge assignments, and what specific commands would configure Core-SW1 as root for VLANs 10, 20, 30, 40, and 50?

Write an initial post of 175-225 words addressing all three sub-questions.

---

## Scenario B: STP Security Hardening

An enterprise security audit identified two STP vulnerabilities in the campus network. First, several access ports in conference rooms and open office areas had PortFast enabled but no BPDU Guard. Second, some distribution-layer uplink ports did not have Root Guard configured. The security team is concerned that an attacker with physical access to a conference room port could disrupt the entire network's Layer 2 topology.

Sub-questions:

1. Describe two specific attacks an attacker could execute from a conference room access port that does not have BPDU Guard. For each attack, explain how the attacker's device interacts with STP and what network disruption results.

2. Explain the difference between BPDU Guard and Root Guard in terms of where each is configured, what event triggers each, and what state the affected port enters. Include the Cisco IOS commands for enabling each feature.

3. A junior engineer suggests enabling Root Guard globally on all ports using `spanning-tree portfast bpduguard default`. Evaluate this suggestion. Is it correct, and if not, what is the correct global command for BPDU Guard and what is the correct placement for Root Guard?

Write an initial post of 175-225 words addressing all three sub-questions.

---

## Scenario C: RSTP Migration Planning

A regional bank is upgrading its campus switching infrastructure. The current environment runs 802.1D classic STP, and users frequently complain about 30-45 second network outages when a switch fails or a port goes down and STP reconverges. The bank's operations team has calculated that each minute of network downtime costs approximately $12,000 in lost transactions.

Sub-questions:

1. Quantify the difference in convergence time between 802.1D STP and 802.1w RSTP. Explain the specific RSTP mechanism that enables faster convergence on point-to-point links (hint: it involves a BPDU handshake between switches). What is this mechanism called?

2. The bank's Cisco switches currently show `spanning-tree mode pvst` in their running configuration. What command changes the STP mode to Rapid PVST+, and does this change require any additional per-VLAN or per-interface configuration, or is it a single global command?

3. During the RSTP migration planning, an engineer notes that some older Access layer switches in the branch offices may not support 802.1w. When an RSTP switch connects to an 802.1D switch on a segment, how does RSTP handle this compatibility? Does RSTP fall back to 802.1D behavior on that link, and does this affect other RSTP switches in the topology?

Write an initial post of 175-225 words addressing all three sub-questions.

---

## Discussion Rubric (10 Points Total)

| Component | Points | Criteria |
|---|---|---|
| Initial Post - Technical Accuracy | 3 | All three sub-questions answered with correct STP terminology and accurate concept application |
| Initial Post - Depth and Analysis | 2 | Responses go beyond definitions to analyze root causes, evaluate configurations, or apply business impact reasoning |
| Initial Post - Word Count | 1 | Post falls within the 175-225 word range |
| Peer Response 1 | 2 | Substantive reply (50+ words) that identifies an error, adds a security consideration, or extends the scenario with a related technical detail |
| Peer Response 2 | 2 | Substantive reply (50+ words) meeting the same criteria as Peer Response 1 |

---

## Professor Nash's Note

STP failures are among the most dramatic network incidents you will ever respond to. A broadcast storm does not degrade gradually — it collapses the network almost instantly, and diagnosing it under pressure requires exactly the kind of systematic thinking we have been building this semester. When you respond to peers who chose Scenario C, think about whether their RSTP convergence explanation captures the proposal/agreement handshake accurately — that mechanism is what the CCNA exam tests, and getting it wrong in a job interview costs you the job.
