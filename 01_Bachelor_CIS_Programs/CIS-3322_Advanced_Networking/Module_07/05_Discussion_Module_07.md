# Discussion Forum: Module 07 - Inter-VLAN Routing Solutions

**Course:** CIS-3322 Advanced Networking
**Certification Alignment:** Cisco CCNA 200-301 (Domain 3: IP Connectivity - 25%)
**Prepared by:** Professor Nash | Texas Wesleyan University

---

## Instructions

Read all three scenarios below and choose ONE to respond to. Identify your chosen scenario (A, B, or C) at the top of your initial post. Your post must address all three sub-questions for the scenario you select.

Initial posts are due Wednesday at 11:59 PM. Peer responses are due Sunday at 11:59 PM.

---

## Scenario A: Enterprise Campus Inter-VLAN Design

A university IT department is redesigning its campus network. The current network has VLANs for Faculty (VLAN 10), Students (VLAN 20), Administration (VLAN 30), and Voice (VLAN 40) spread across three buildings. The distribution layer currently uses Cisco 1941 routers with router-on-a-stick. The team is evaluating whether to migrate to Catalyst 3850 multilayer switches using SVIs.

Sub-questions:

1. Explain what makes router-on-a-stick a bandwidth bottleneck in this environment. Be specific about what physical path inter-VLAN traffic takes and why the single trunk link becomes a limiting factor as VLAN count and traffic volume increase.

2. Describe what changes would be required to migrate from ROAS to Layer 3 SVIs. Your answer should address which hardware is replaced, which IOS commands are removed, which commands are added, and what must happen to each VLAN's default gateway setting on end-user devices.

3. After migrating to SVIs, the network team discovers that Faculty VLAN 10 hosts cannot ping the 192.168.10.1 gateway. `show ip interface brief` shows Vlan10 is `up/down`. Describe two specific things you would check and the exact IOS command you would use to diagnose each one.

Write an initial post of 175-225 words addressing all three sub-questions.

---

## Scenario B: ROAS Troubleshooting in a Branch Office

A small branch office has a Cisco 1941 router and a Catalyst 2960 switch. The network engineer configured router-on-a-stick to route between VLAN 10 (Engineering, 192.168.10.0/24) and VLAN 20 (Sales, 192.168.20.0/24). After configuration, Engineering hosts can ping the router's Gi0/0.10 subinterface at 192.168.10.1 but cannot reach any Sales hosts. Sales hosts cannot ping anything beyond their own VLAN.

Sub-questions:

1. The engineer runs `show ip interface brief` on the router and sees: Gi0/0.10 is up/up with 192.168.10.1, and Gi0/0.20 is up/up with 192.168.20.1. Given that both subinterfaces are up and addressed, identify two other configuration elements you would check and explain how each could cause the specific symptom described — reachability within each VLAN but not between VLANs.

2. Write the exact IOS commands to verify the trunk configuration on the switch, and describe what specific output would confirm the trunk is correctly passing both VLANs 10 and 20.

3. On the router, the engineer checks the subinterface configuration and finds: Gi0/0.20 is configured with `encapsulation dot1Q 10` instead of `encapsulation dot1Q 20`. Explain exactly what happens to traffic when two subinterfaces share the same VLAN encapsulation value, and what the fix is.

Write an initial post of 175-225 words addressing all three sub-questions.

---

## Scenario C: Multi-VLAN Retail Network Design

A retail chain is deploying a new store network with four VLANs: POS (VLAN 10, 192.168.10.0/24), Inventory (VLAN 20, 192.168.20.0/24), Guest WiFi (VLAN 30, 192.168.30.0/24), and Management (VLAN 99, 192.168.99.0/24). The network architect must choose between deploying a Cisco 1941 router with router-on-a-stick or a Cisco Catalyst 3650 with SVIs. Security policy requires Guest WiFi to be blocked from reaching POS systems.

Sub-questions:

1. The security requirement to block Guest WiFi from reaching POS systems must be enforced at Layer 3. Explain which inter-VLAN routing method — ROAS or Layer 3 SVIs — makes it easier to apply this restriction, and describe at a high level where and how you would implement the restriction (no need to write a full ACL, just identify the enforcement point and why).

2. The architect selects a Cisco Catalyst 3650 with SVIs. Write the complete SVI configuration for VLAN 30 (Guest WiFi, IP 192.168.30.1/24) and VLAN 99 (Management, IP 192.168.99.1/24), including the global command required to enable routing and the access port assignment for at least one port per VLAN.

3. After deployment, the store manager reports that the management interface (VLAN 99 SVI at 192.168.99.1) cannot be reached from POS systems in VLAN 10. `show ip route` on the Catalyst 3650 shows connected routes for all four VLANs. Identify two possible causes of this specific failure that are NOT related to the routing table, and describe how you would verify each one.

Write an initial post of 175-225 words addressing all three sub-questions.

---

## Discussion Rubric (10 Points Total)

| Component | Points | Criteria |
|---|---|---|
| Initial Post - Technical Accuracy | 3 | All three sub-questions answered with correct inter-VLAN routing terminology and accurate concept application |
| Initial Post - Depth and Analysis | 2 | Responses analyze operational scenarios, diagnose failures, or evaluate design trade-offs |
| Initial Post - Word Count | 1 | Post falls within the 175-225 word range |
| Peer Response 1 | 2 | Substantive reply (50+ words) that adds a technical detail, corrects an error, or extends the scenario analysis |
| Peer Response 2 | 2 | Substantive reply (50+ words) meeting the same criteria as Peer Response 1 |

---

## Professor Nash's Note

One of the most common support tickets I see in production networks goes like this: "We added a new VLAN last week and now nobody in that VLAN can reach anything." Nine times out of ten, the engineer created the VLAN, assigned ports to it, maybe even created the SVI — but forgot `ip routing` on the multilayer switch, or forgot to add the VLAN to the trunk allowed list, or left the SVI in `up/down` because no port was actually active. These are not complex problems. They are checklist problems. The engineer who diagnoses them in two minutes is the one who has memorized exactly which `show` commands to run and in what order. That is what this week is about.
