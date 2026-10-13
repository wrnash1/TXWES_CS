# Discussion Forum: Module 12 — WAN Technologies and Remote Access

## Course: CIS-3322 Advanced Networking

## Texas Wesleyan University | Professor Nash

## Certification Alignment: Cisco CCNA 200-301

---

## Instructions

Read all three scenarios below and choose ONE to respond to. Identify your chosen scenario (A, B, or C) at the top of your initial post. Your post must address all three sub-questions for the scenario you select.

Initial posts are due Wednesday at 11:59 PM. Peer responses are due Sunday at 11:59 PM.

---

## Scenario A: Enterprise WAN Migration Decision

A regional logistics company currently operates a hub-and-spoke MPLS WAN connecting its headquarters in Dallas to 12 branch offices across Texas. Monthly WAN costs are $18,000. The IT director is evaluating a migration to SD-WAN with broadband internet replacing MPLS circuits. Several branch managers are pushing back, citing concerns about internet reliability and voice call quality for their VoIP systems.

### Sub-questions for Scenario A

1. Explain the specific SD-WAN capability that directly addresses the branch managers' concern about VoIP quality over internet links. Name the feature, describe how it works at the technical level (what metrics are measured and what action is taken), and identify which SD-WAN component enforces this policy at each branch.

2. The IT director asks how the SD-WAN deployment would handle internet outages at individual branches. Describe how SD-WAN's transport independence supports failover scenarios. Include in your answer: what happens to existing VoIP sessions during an automatic failover event and what secondary transport options could be configured as failover paths.

3. The network team proposes a hybrid migration: keep MPLS for the five largest branch offices (highest traffic volume, most VoIP sessions) and use SD-WAN with broadband for the seven smaller branches. Evaluate this hybrid approach. Identify one operational benefit and one operational challenge of running MPLS and SD-WAN simultaneously in the same enterprise WAN.

Write an initial post of 175–225 words addressing all three sub-questions.

---

## Scenario B: GRE Tunnel Troubleshooting

A network engineer is troubleshooting a GRE tunnel between the headquarters router (R1, WAN IP 203.0.113.1) and a branch router (R2, WAN IP 203.0.114.2). The following conditions have been confirmed:

- The GRE tunnel is configured correctly on both routers (source, destination, tunnel IP)
- `show interface Tunnel0` on R1 shows `up/up`
- `show interface Tunnel0` on R2 shows `up/down`
- R1 can ping R2's tunnel IP (172.16.0.2) successfully
- R2 cannot ping R1's tunnel IP (172.16.0.1)
- `show ip ospf neighbor` on both routers shows no neighbors

### Sub-questions for Scenario B

1. The asymmetry is notable: R1's tunnel is `up/up` but R2's is `up/down`. Given what you know about the specific condition that causes `up/down` on a GRE tunnel, explain what this asymmetric state tells you about the routing configuration on R2 specifically. What IOS command would you run on R2 to confirm your hypothesis, and what would the output look like if your hypothesis is correct?

2. After restoring R2's routing, the tunnels both show `up/up` but OSPF neighbors still do not form after five minutes. Describe three possible causes for OSPF neighbor failure on a functioning GRE tunnel. For each cause, write the specific IOS command you would run to confirm it.

3. A junior engineer suggests bypassing GRE and configuring IPsec-only site-to-site VPN to avoid the complexity of running two overlay protocols. Explain specifically why IPsec alone cannot support the OSPF neighbor requirement in this design and what fundamental protocol behavior makes GRE necessary in this use case.

Write an initial post of 175–225 words addressing all three sub-questions.

---

## Scenario C: Remote Access vs Site-to-Site VPN Design

A mid-size architecture firm has 45 employees. Fifteen employees work permanently from remote locations. The other 30 work from two offices (Main and Satellite). All employees need access to a CAD server and file server at the Main office. The IT manager is designing the VPN architecture.

### Sub-questions for Scenario C

1. Identify which VPN type is appropriate for each connectivity requirement: (a) connecting the Satellite office to the Main office, and (b) connecting the 15 remote employees to the Main office. For each, explain why the other VPN type would not be the correct choice. Be specific about what makes each scenario different in terms of duration, endpoints, and user experience.

2. The IT manager is considering IPsec with AH for the site-to-site VPN between the offices because "authentication is enough — nobody is capturing our traffic." Evaluate this statement. Describe a specific realistic threat scenario involving traffic capture that demonstrates why ESP rather than AH should be used, even for corporate internal traffic over the internet.

3. The 15 remote workers use Cisco AnyConnect for remote access VPN. A security engineer notes that split tunneling is currently enabled, meaning remote workers' non-corporate internet traffic does not go through the corporate VPN. Identify one security benefit and one security risk of split tunneling, and describe the operational trade-off the IT manager must weigh when deciding whether to enable or disable it.

Write an initial post of 175–225 words addressing all three sub-questions.

---

## Sample Peer Response

The following is an example of a substantive peer response that meets the minimum standard.

"Your analysis of the GRE multicast requirement was correct and I want to build on it. The reason OSPF specifically needs multicast is that it uses 224.0.0.5 (AllSPFRouters) and 224.0.0.6 (AllDRRouters) to send Hello packets on broadcast networks. The GRE tunnel interface creates a point-to-point network type by default in OSPF, which actually changes the neighbor formation behavior — on a point-to-point link there is no DR/BDR election and hellos are sent to 224.0.0.5 only. This is worth knowing because if you accidentally configure the GRE tunnel as an OSPF broadcast network type, the behavior changes. The default point-to-point type is actually more efficient for tunnel interfaces."

---

## Discussion Rubric

| Component                         | Points | Criteria                                                                                      |
|-----------------------------------|--------|-----------------------------------------------------------------------------------------------|
| Initial Post — Technical Accuracy | 3      | All three sub-questions answered with correct WAN terminology and accurate concept application |
| Initial Post — Depth and Analysis | 2      | Responses analyze operational scenarios, evaluate design trade-offs, or diagnose failures      |
| Initial Post — Word Count         | 1      | Post falls within the 175–225 word range                                                      |
| Peer Response 1                   | 2      | Substantive reply (50+ words) that adds a technical detail, corrects an error, or extends the scenario analysis |
| Peer Response 2                   | 2      | Substantive reply (50+ words) meeting the same criteria as Peer Response 1                    |

---

## Professor Nash's Note

The GRE and IPsec relationship is one of the most practically important concepts in this module — and one of the most misunderstood. Students often ask why we need GRE at all if IPsec provides secure tunneling. The answer is always multicast. OSPF and EIGRP cannot form neighbor relationships over IPsec because those protocols use multicast for Hello packets and IPsec only carries unicast traffic. GRE provides the virtual point-to-point link that multicast can cross, and IPsec encrypts the GRE-encapsulated traffic. Neither technology alone solves both problems. When you see a question that mentions both dynamic routing protocols and encrypted WAN in the same sentence, the answer is almost always GRE over IPsec. Remember that combination.

For SD-WAN: you will see vManage, vSmart, vBond, and vEdge on the exam. The most commonly missed one is vBond — its authentication and orchestration role is tested in scenario questions about how new sites come online. Know all four cold.
