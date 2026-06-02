# Discussion Forum: Module 04 - Switching Concepts & VLANs

**Course:** CIS-3322 Advanced Networking
**Certification Alignment:** Cisco CCNA 200-301 (Domain 2: Network Access - 20%)
**Prepared by:** Professor Nash | Texas Wesleyan University

---

## Instructions

Read all three scenarios below and choose ONE to respond to. Identify your chosen scenario (A, B, or C) at the top of your initial post. Your post must address all three sub-questions for the scenario you select.

Initial posts are due Wednesday at 11:59 PM. Peer responses are due Sunday at 11:59 PM.

---

## Scenario A: Healthcare Network Segmentation

A regional medical center is redesigning its campus LAN. The IT security officer requires strict traffic segmentation between three groups: clinical workstations accessing the electronic health record (EHR) system, guest Wi-Fi users, and administrative staff. All three groups connect to Access layer switches in patient care areas, nursing stations, and administrative offices. The hospital uses Cisco Catalyst 2960 switches throughout the Access layer.

Sub-questions:

1. Explain how VLANs provide the required traffic segmentation between the three groups without requiring separate physical switches for each group. Include in your answer whether Layer 2 broadcast traffic from the EHR VLAN can reach the guest Wi-Fi VLAN, and why or why not.

2. The hospital's networking staff notices a CDP log message appearing repeatedly on the Core switch: `%CDP-4-NATIVE_VLAN_MISMATCH`. Describe exactly what caused this message, what risk it introduces, and the specific IOS command to resolve it on the trunk interface.

3. A nurse practitioner reports that their workstation can communicate with other clinical workstations on the same floor (same switch) but cannot reach clinical workstations on the floor above (different switch). Both workstations should be in VLAN 10. List three things an engineer should check to diagnose this connectivity failure.

Write an initial post of 175-225 words addressing all three sub-questions.

---

## Scenario B: VLAN Security Hardening

An enterprise network security audit has identified several vulnerabilities in the company's campus switching environment. The audit found: (1) all Access layer switches still use VLAN 1 as the native VLAN on trunks; (2) many Access layer ports are in `dynamic auto` mode; and (3) some access ports have been found with multiple MAC addresses associated with them, suggesting unauthorized devices or hubs have been plugged in.

Sub-questions:

1. For each of the three audit findings, explain the specific security risk it creates. For findings 1 and 2, name the specific type of network attack that each vulnerability enables.

2. For each finding, provide the specific Cisco IOS command or command sequence that remediates the vulnerability. Be specific about which mode (global config, interface config, VLAN config) each command is entered in.

3. After remediating all three findings, the security team suggests also moving all unused switch ports to a "black-hole" VLAN (a VLAN that has no routing and is not trunked to any other switch). Explain the security benefit of this configuration and identify the two IOS commands needed to implement it on an unused port.

Write an initial post of 175-225 words addressing all three sub-questions.

---

## Scenario C: Multi-Department Office Deployment

A growing technology company is moving into a new office building with three floors. The IT team must design a VLAN scheme for 150 employees spread across Engineering (60 employees on floor 1), Product Management (40 employees on floor 2), and Sales (50 employees on floor 3). The building has one Access layer switch per floor and one Distribution layer switch in the network closet that connects all three floor switches via trunk uplinks.

Sub-questions:

1. Design the VLAN scheme for this company. Specify: VLAN IDs, VLAN names, which switch ports on each floor switch should be access ports, which port is the trunk uplink, and which VLANs should be allowed on each trunk. Explain your native VLAN choice for the trunk links.

2. An employee on floor 2 (Product Management) needs to collaborate with an Engineering team member on floor 1. Their workstations cannot ping each other even though the trunk links are all active. What Layer 3 component is missing from the topology, and where should it be implemented for a best-practice campus design?

3. The IT team wants to add a fourth VLAN for IP phones. The office uses Cisco IP phones that connect between the switch port and the PC, carrying voice and data on the same physical cable. What Cisco switch feature allows a single physical port to carry both voice (VLAN 40) and data (VLAN 10-30) simultaneously, and what two commands implement this?

Write an initial post of 175-225 words addressing all three sub-questions.

---

## Discussion Rubric (10 Points Total)

| Component | Points | Criteria |
|---|---|---|
| Initial Post - Technical Accuracy | 3 | All three sub-questions answered with correct VLAN, trunking, and security terminology |
| Initial Post - Depth and Analysis | 2 | Responses go beyond definitions to diagnose problems, recommend configurations, and explain trade-offs |
| Initial Post - Word Count | 1 | Post falls within the 175-225 word range |
| Peer Response 1 | 2 | Substantive reply (50+ words) that evaluates the peer's VLAN design, corrects a technical error, or adds a security consideration |
| Peer Response 2 | 2 | Substantive reply (50+ words) meeting the same criteria as Peer Response 1 |

---

## Professor Nash's Note

VLAN design mistakes in production networks are among the most common and costly configuration errors. An improperly configured native VLAN or a forgotten `switchport mode access` command can expose entire network segments to attacks. As you respond to your peers, evaluate their security hardening steps carefully — good peer feedback here is practice for the kind of configuration review that network engineers perform on each other's work before changes go into production.
