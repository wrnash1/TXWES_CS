# Discussion Forum: Module 11 — Switching: VLANs, STP, and EtherChannel

## Course: CIS-3321 Network Administration

## Texas Wesleyan University | Professor Nash

Certification Alignment: CompTIA Network+ (N10-008)

---

### Overview

This week's discussion applies VLAN design, STP behavior, and EtherChannel concepts to real-world switching scenarios. You will select one of three scenarios and write a substantive initial post of 175–225 words. After posting, reply to at least two classmates who chose different scenarios.

---

### Choose One Scenario

#### Scenario A: VLAN Design for a Hospital Network

A regional hospital is redesigning its network. The current flat network (all devices on one VLAN) has experienced performance issues and a recent security audit found that biomedical devices (infusion pumps, patient monitors) share a broadcast domain with administrative PCs and the cafeteria guest Wi-Fi. The IT director has approved a VLAN redesign. The hospital has approximately 600 wired devices and 200 wireless devices across four floors, with a data center in the basement.

Respond to all three questions:

1. Propose a VLAN segmentation design for this hospital. Identify at least four VLANs, assign a meaningful name and VLAN ID to each, and explain the security or operational justification for each segment. Specifically address why biomedical devices must be isolated in their own VLAN separate from administrative PCs.

2. The hospital has 12 access layer switches on patient floors connecting to two distribution switches in the IDF closets, which connect to a core switch in the basement data center. Identify which links in this topology must be configured as trunk ports and explain what would happen if a trunk port between an access switch and the distribution switch were misconfigured as an access port.

3. The guest Wi-Fi VLAN must allow internet access but must be completely prevented from reaching any clinical or administrative systems. Identify two specific Layer 2 and/or Layer 3 mechanisms that enforce this isolation, and explain where in the topology each mechanism is applied.

---

#### Scenario B: STP Root Bridge Placement Gone Wrong

A network administrator at a medium-sized law firm inherits a network with 15 switches. Investigation reveals that the current STP Root Bridge is an unmanaged 8-port switch in a conference room that happens to have the lowest MAC address on the network. All access switches on the three office floors are forwarding traffic through this conference room switch as the Root Bridge. The intended Root Bridges (two enterprise-grade distribution switches in the server room) are not the Root Bridge for any VLAN.

Respond to all three questions:

1. Explain why the conference room switch became the Root Bridge. Your answer must reference the Bridge ID components and the STP election process. Why is this a performance and reliability problem for the network?

2. Describe the steps the administrator should take to permanently correct Root Bridge placement. Identify the specific STP configuration command, explain what priority value to use, and explain why the administrator should configure both distribution switches (primary and secondary) rather than only one.

3. The administrator considers enabling PortFast and BPDU Guard on all access switch ports connected to end-user PCs. Explain what each feature does independently and what they accomplish together. Then identify the one port type where PortFast must never be enabled and explain what would happen if it were accidentally configured there.

---

#### Scenario C: EtherChannel Troubleshooting Between Distribution Switches

A network engineer is called to troubleshoot an intermittent connectivity issue between two distribution switches. Users report that file transfers between VLANs hosted on different switches drop randomly every few hours. Investigation reveals that the two distribution switches are connected by a 4-port LACP EtherChannel. The show etherchannel summary output shows two ports as (P) bundled and two ports as (D) down — but the physical cables are intact and the link lights are green on all four ports. The ports on Switch-B are configured with channel-group 2 mode active while ports on Switch-A are configured with channel-group 1 mode active.

Respond to all three questions:

1. Identify the specific configuration error causing two ports to appear as (D) in the EtherChannel. Explain why the channel-group number difference between switches is or is not the problem, and identify what configuration mismatch most commonly causes individual ports to fail to join an existing LACP bundle.

2. The show interfaces trunk output shows that the Port-Channel interface is correctly configured as a trunk with VLANs 10, 20, and 30 allowed. However, a user on VLAN 40 (which was added last week) cannot communicate between the two switches. What is the additional configuration needed and where must it be applied?

3. The network engineer proposes replacing the 4-port 100 Mbps FastEthernet EtherChannel with a 2-port 1 Gbps GigaEthernet EtherChannel for better performance. Calculate the maximum available bandwidth for both options and explain whether the switch from four 100 Mbps links to two 1 Gbps links is a worthwhile upgrade. Consider both aggregate bandwidth and redundancy in your answer.

---

### Response Requirements

Initial Post (due Wednesday at 11:59 PM):

- Choose exactly one scenario (A, B, or C)
- Write 175–225 words
- Identify which scenario you chose in your first sentence
- Answer all three sub-questions for your chosen scenario
- Use correct terminology: VLAN, trunk port, access port, 802.1Q, native VLAN, STP, Root Bridge, Bridge ID, PortFast, BPDU Guard, Root Guard, EtherChannel, LACP, PAgP, port-channel, show etherchannel summary, show vlan brief, show spanning-tree, broadcast domain

Peer Responses (due Sunday at 11:59 PM):

- Reply to at least two classmates who chose different scenarios than you
- Each reply must be at least 60 words
- Provide a specific technical addition, correction, or alternative design consideration — do not simply agree or summarize

---

### Grading Rubric (10 Points Total)

Initial Post — 6 Points:

- 5–6 points: All three sub-questions answered with accurate technical terminology, correct switching concept application, and meets the 175–225 word count.
- 3–4 points: Addresses most sub-questions but lacks technical depth or contains a specification error (such as incorrect STP election logic or incorrect EtherChannel mode pairing).
- 1–2 points: Post is incomplete, off-topic, or contains significant inaccuracies.
- 0 points: No initial post submitted.

Peer Responses — 4 Points:

- 4 points: Substantive responses to two classmates who chose different scenarios, each at least 60 words, adding genuine technical value.
- 2 points: Only one peer response, or both responses lack technical substance.
- 0 points: No peer responses submitted.

---

### Professor Nash's Note

The scenarios this week are drawn directly from real network environments. The flat hospital network is not a hypothetical — regulatory frameworks like HIPAA require isolation of clinical systems, and network segmentation is the technical mechanism. The misplaced Root Bridge at the law firm is one of the most common findings when an engineer takes over an inherited network: nobody ever configured STP explicitly, so the switch with the lowest MAC address (often a forgotten device in a closet) runs the tree. And EtherChannel mismatches are among the top causes of intermittent trunk failures — the links look fine, the lights are green, but two of the four ports are silently doing nothing. These are the problems that senior engineers get called in to solve. Your job this week is to demonstrate that you understand not just what went wrong but why, and exactly what to do to fix it.

---

CIS-3321 Network Administration | Texas Wesleyan University | Professor Nash
