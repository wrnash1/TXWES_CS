# Discussion Forum: Module 03 – IP Addressing: IPv4, Subnetting, CIDR
## CIS-3321 Network Administration | CompTIA Network+ (N10-008)
## Texas Wesleyan University | Professor Nash

---

### Overview

This week's discussion applies subnetting and IP addressing concepts to realistic network design and troubleshooting scenarios. You will choose one of three scenarios below and respond with a substantive initial post of 175–225 words. After posting, respond to at least two classmates who chose different scenarios.

---

### Choose One Scenario

#### Scenario A: IP Address Design for a Growing Office

A startup company is moving into a new office building and needs you to design an IP addressing scheme. The company has four departments:

- Sales: 45 workstations
- Engineering: 28 workstations
- Finance: 12 workstations
- Administration: 6 workstations

Management has provided the network block 192.168.100.0/24 and requires that each department be on its own subnet. They also want to use the most efficient (smallest) subnets possible to avoid wasting addresses, and they want room to grow by at least 20% in each department.

Respond to all three questions:

1. For each department, identify the smallest CIDR prefix that accommodates the current workstation count plus 20% growth. State the subnet mask and number of usable hosts for each.
2. List the network address, broadcast address, and usable host range for each department's subnet, assuming you allocate them sequentially starting from 192.168.100.0.
3. After subnetting, could a workstation in the Sales subnet communicate with a workstation in the Engineering subnet without a router? Explain why or why not, referencing the subnet boundaries you calculated.

---

#### Scenario B: Diagnosing an IP Addressing Conflict

A junior technician calls you for help. She has two workstations that are supposed to be on the same subnet and able to communicate directly, but pings between them are failing. Here are the configurations:

- Workstation 1: IP 192.168.5.66, Mask 255.255.255.192, Gateway 192.168.5.65
- Workstation 2: IP 192.168.5.129, Mask 255.255.255.192, Gateway 192.168.5.65

Respond to all three questions:

1. Calculate the network address and subnet range for each workstation using the given mask. Show the block size calculation and the network address for each.
2. Based on your calculations, explain specifically why the ping fails. Are these workstations on the same subnet? What is the gateway address 192.168.5.65 — is it valid, and for which subnet?
3. Propose two different ways to fix this issue. For each option, describe the specific IP address changes needed and explain the trade-off between the two approaches.

---

#### Scenario C: VLSM Address Planning for a Multi-Site Network

A network engineer is designing an address plan for a company with three remote sites connected by point-to-point WAN links. The company has been allocated the 10.1.0.0/24 block. Requirements:

- Site A LAN: 60 workstations
- Site B LAN: 28 workstations
- Site C LAN: 12 workstations
- WAN link between Site A and Site B: 2 endpoints
- WAN link between Site B and Site C: 2 endpoints

The engineer plans to use VLSM to allocate subnets of different sizes.

Respond to all three questions:

1. For each site LAN and each WAN link, identify the minimum CIDR prefix needed. List the prefix, subnet mask, and usable host count for each requirement.
2. Explain what VLSM is and why it is necessary in this scenario compared to using a single fixed prefix for all subnets. What would happen to address efficiency if all five subnets used the same /26 prefix?
3. Identify one routing protocol consideration that applies when using VLSM. Why do older protocols like RIPv1 not support VLSM, and what must the routing protocol include in its updates for VLSM to work correctly?

---

### Response Requirements

**Initial Post (due Wednesday at 11:59 PM):**

- Choose exactly one scenario (A, B, or C)
- Write 175–225 words
- Identify which scenario you chose in your first sentence
- Answer all three sub-questions for your chosen scenario
- Show subnet calculations when asked; be specific with network addresses and masks

**Peer Responses (due Sunday at 11:59 PM):**

- Reply to at least two classmates who chose different scenarios than you
- Each reply must be at least 60 words
- Offer a specific technical addition, a check of their subnet math, or an alternative perspective

---

### Grading Rubric (10 Points Total)

**Initial Post — 6 Points:**

- 5–6 points: All three sub-questions answered with accurate subnet calculations, correct CIDR notation, appropriate use of terminology, and meets the 175–225 word count.
- 3–4 points: Addresses most sub-questions but contains a calculation error or lacks sufficient technical detail.
- 1–2 points: Post is incomplete, off-topic, or contains significant errors in subnet math.
- 0 points: No initial post submitted.

**Peer Responses — 4 Points:**

- 4 points: Substantive responses to two classmates who chose different scenarios, each at least 60 words, with meaningful technical contributions.
- 2 points: Only one peer response, or both responses lack technical substance.
- 0 points: No peer responses submitted.

---

### Professor Nash's Note

Subnetting is a skill that network administrators use constantly. Every time a new branch opens, a new VLAN is created, or a new device is added to the network, someone has to calculate the correct subnet. The scenarios this week reflect the kinds of requests that come across a network administrator's desk regularly. Getting comfortable with these calculations now will save you significant time when the same situation comes up during the lab midterm and on the exam. If you found a classmate's subnet math to be different from yours, check your work carefully — sometimes both approaches are valid if different starting assumptions are made. That conversation is worth having in the peer response thread.

---

*CIS-3321 Network Administration | Texas Wesleyan University | Professor Nash*
