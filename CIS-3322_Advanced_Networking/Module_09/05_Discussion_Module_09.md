# Discussion Forum: Module 09 - WAN Technologies and VPNs

**Course:** CIS-3322 Advanced Networking
**Certification Alignment:** Cisco CCNA 200-301 (Domain 4: IP Services / Domain 5: Security Fundamentals)
**Prepared by:** Professor Nash | Texas Wesleyan University

---

## Instructions

Read all three scenarios below and choose ONE to respond to. Identify your chosen scenario (A, B, or C) at the top of your initial post. Your post must address all three sub-questions for the scenario you select.

Initial posts are due Wednesday at 11:59 PM. Peer responses are due Sunday at 11:59 PM.

---

## Scenario A: Branch Office WAN Design

A logistics company has a headquarters in Dallas and four branch offices in Houston, Austin, San Antonio, and El Paso. Each branch connects to headquarters via the company's internet connections. The network team is evaluating two options: (1) configure individual IPsec site-to-site VPNs between each branch and HQ, or (2) deploy DMVPN with IPsec across all five sites.

Sub-questions:

1. The team currently uses OSPF as their routing protocol. Explain why a standard IPsec tunnel (without GRE) would cause OSPF neighbor formation to fail between branch routers and the HQ router. Be specific about which characteristic of OSPF creates this problem with IPsec.

2. Explain the primary scalability advantage of DMVPN over individual site-to-site IPsec VPNs in this five-site scenario. Your answer should address what happens at the HQ router configuration as the number of sites grows, and what NHRP enables in the DMVPN design.

3. The team decides to use GRE over IPsec for each branch connection rather than full DMVPN. Describe the security limitation of a GRE tunnel configured without IPsec, and explain what IPsec ESP adds when combined with GRE. Use the terms "confidentiality" and "integrity" in your answer.

Write an initial post of 175-225 words addressing all three sub-questions.

---

## Scenario B: Metro Ethernet Service Selection

A regional healthcare organization is deploying a new network to connect its main hospital (HQ) with three clinics (Site A, Site B, Site C). The organization's IT director is evaluating Metro Ethernet service options from their carrier. Requirements are: (1) HQ must be able to communicate directly with all three clinics, (2) the clinics should not be able to communicate directly with each other without routing through HQ, and (3) the provider must handle the underlying transport infrastructure.

Sub-questions:

1. Based on the requirements, which Metro Ethernet service type (E-Line, E-LAN, or E-Tree) best fits this design? Explain your reasoning, specifically addressing why the other two service types do not satisfy all three requirements.

2. The IT director asks why Metro Ethernet is preferred over deploying individual internet connections with site-to-site VPNs for this healthcare network. Identify two advantages of Metro Ethernet over internet-based VPNs in this context, and one scenario in which internet-based VPNs would be the better choice.

3. If the organization adds a fifth site (Site D) six months after initial deployment, describe what changes are required on the customer side and on the provider side for each of the three Metro Ethernet service types (E-Line, E-LAN, E-Tree). Which service type requires the most customer-side configuration changes to add the new site?

Write an initial post of 175-225 words addressing all three sub-questions.

---

## Scenario C: IPsec VPN Troubleshooting

A network engineer is troubleshooting a site-to-site IPsec VPN between HQ (R1) and a branch office (R2). Users report they cannot reach branch servers. The engineer investigates and finds:

- R1 and R2 can ping each other's WAN interfaces successfully
- The IPsec security association is established (visible in `show crypto ipsec sa`)
- Traffic from the HQ LAN (192.168.1.0/24) to the branch LAN (192.168.2.0/24) is not reaching the branch
- Traffic from the branch LAN to the HQ LAN is not reaching HQ either

Sub-questions:

1. The engineer checks R1's routing table and finds no route to 192.168.2.0/24. Given that the VPN tunnel appears to be up, explain why a routing entry is still required and where it should point. Write the static route command that would send traffic for 192.168.2.0/24 through the tunnel interface.

2. The engineer also needs to verify that the IPsec VPN is using ESP rather than AH. Explain why ESP is the correct protocol for this deployment from a security standpoint, and describe what command output would confirm which IPsec protocol is in use.

3. After adding the static routes, a security audit reveals that the VPN tunnel is using AH instead of ESP. The auditor flags this as a compliance failure because protected health information (PHI) is transmitted between HQ and the branch. Explain specifically why AH fails to meet the compliance requirement, and identify which IPsec component must be changed to resolve it.

Write an initial post of 175-225 words addressing all three sub-questions.

---

## Discussion Rubric (10 Points Total)

| Component | Points | Criteria |
|---|---|---|
| Initial Post - Technical Accuracy | 3 | All three sub-questions answered with correct WAN/VPN terminology and accurate concept application |
| Initial Post - Depth and Analysis | 2 | Responses analyze operational scenarios, evaluate design trade-offs, or diagnose failures |
| Initial Post - Word Count | 1 | Post falls within the 175-225 word range |
| Peer Response 1 | 2 | Substantive reply (50+ words) that adds a technical detail, corrects an error, or extends the scenario analysis |
| Peer Response 2 | 2 | Substantive reply (50+ words) meeting the same criteria as Peer Response 1 |

---

## Professor Nash's Note

The AH versus ESP question comes up on nearly every CCNA attempt I have seen students struggle with, and the confusion is understandable — both protocols sound like they provide security. The key word is confidentiality. AH authenticates traffic, which means you know where it came from and that it was not modified. But it does not hide the content. Anyone who captures the packet can read it. ESP adds encryption — the payload is ciphertext. In healthcare, finance, or any environment transmitting regulated data, AH alone is never compliant. This is not an abstract exam question. It is a real deployment mistake people make. Know the distinction cold.
