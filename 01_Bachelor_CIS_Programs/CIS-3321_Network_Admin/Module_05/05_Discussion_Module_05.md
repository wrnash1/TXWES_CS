# Discussion Forum: Module 05 – Network Infrastructure: Cables, Switches, Routers
## CIS-3321 Network Administration | CompTIA Network+ (N10-008)
## Texas Wesleyan University | Professor Nash

---

### Overview

This week's discussion connects network infrastructure concepts — cabling, switching, and routing — to practical deployment and troubleshooting scenarios. You will choose one of three scenarios below and respond with a substantive initial post of 175–225 words. After posting, respond to at least two classmates who chose different scenarios.

---

### Choose One Scenario

#### Scenario A: New Office Network Infrastructure Design

A growing company is moving 80 employees into a new three-story office building. Each floor has 25–30 workstations, 4 IP phones, and 8 wireless access points. The IT director asks you to design the physical cabling infrastructure. The wiring closet is on the second floor, and the maximum cable run to any device on the third floor is 85 meters. The budget allows for Cat6a throughout, and the switches must support the wireless APs without separate power adapters.

Respond to all three questions:

1. What cable category would you specify for horizontal runs from the wiring closet to each workstation and AP? Is Cat6a necessary given the 85-meter maximum distance, or would a less expensive option work? Justify your choice using speed and distance specifications.
2. What PoE standard is required to power the wireless APs without separate adapters, assuming they are dual-radio enterprise-grade APs requiring approximately 25 watts each? Which PoE switch specification would you require in the purchase order?
3. The third floor will have a distribution switch connected back to the main switching core on the second floor. The run between the floors is 60 meters. Would you use copper or fiber for this inter-switch uplink, and what specific standard or cable type would you specify? Explain your reasoning.

---

#### Scenario B: Switch Troubleshooting — Asymmetric Traffic and MAC Table Issues

A network administrator reports a problem on a floor of the corporate office. Several users have been complaining of slow network performance during certain hours. A network capture shows large amounts of traffic being delivered to workstations that should not be receiving it — specifically, unicast frames addressed to other devices are arriving at unintended workstations. The switch is a managed Cisco 2960 with default settings.

Respond to all three questions:

1. Explain the MAC address flooding attack (also called CAM table overflow or MAC flood attack). How does an attacker cause this condition on a switch, and why does it cause unicast frames to be delivered to all ports?
2. How does the normal switch MAC address aging process differ from the behavior seen during a MAC flood attack? What is the typical default aging timer, and why does the attacker need to continuously generate traffic to maintain the attack?
3. What two switch security features would you configure to mitigate this attack? For each, briefly describe what it does and at which OSI layer it operates. Include the specific name of each feature.

---

#### Scenario C: Hub vs. Switch Performance Analysis

A small manufacturing company still uses hubs at several production floor workstations because "they still work." The network administrator has observed that whenever multiple workstations transmit simultaneously, the network slows dramatically and several machines lose connectivity temporarily. Management wants a justification to replace the hubs with switches.

Respond to all three questions:

1. Explain technically why simultaneous transmissions on a hub cause the observed slowdown and temporary connectivity loss. Use the terms "collision domain," "CSMA/CD," and "collision" correctly in your explanation.
2. A switch would eliminate this specific problem because it creates one collision domain per port. Explain the MAC address learning and unicast forwarding process that makes this possible. How does a switch know which port to forward a frame to, and what does it do when it does not yet know the destination?
3. The company's IT manager asks whether replacing hubs with switches could create any new network issues that did not exist before. Identify one potential issue that can arise from increased switch interconnectivity (hint: think about Layer 2 loops) and name the protocol designed to prevent it.

---

### Response Requirements

**Initial Post (due Wednesday at 11:59 PM):**

- Choose exactly one scenario (A, B, or C)
- Write 175–225 words
- Identify which scenario you chose in your first sentence
- Answer all three sub-questions for your chosen scenario
- Use correct infrastructure terminology (cable category names, PoE standard numbers, OSI layer references)

**Peer Responses (due Sunday at 11:59 PM):**

- Reply to at least two classmates who chose different scenarios than you
- Each reply must be at least 60 words
- Offer a specific technical addition, correction, or alternative design perspective

---

### Grading Rubric (10 Points Total)

**Initial Post — 6 Points:**

- 5–6 points: All three sub-questions answered with accurate technical detail, correct cable/PoE specifications, appropriate terminology, and meets the 175–225 word count.
- 3–4 points: Addresses most sub-questions but lacks technical detail or contains a specification error.
- 1–2 points: Post is incomplete, off-topic, or contains significant inaccuracies.
- 0 points: No initial post submitted.

**Peer Responses — 4 Points:**

- 4 points: Substantive responses to two classmates who chose different scenarios, each at least 60 words, adding technical value.
- 2 points: Only one peer response, or both responses lack technical substance.
- 0 points: No peer responses submitted.

---

### Professor Nash's Note

The infrastructure choices you make in network design have consequences that last for years. Choosing Cat6 instead of Cat6a might save a small amount per foot in materials, but it means you cannot support 10 Gbps at full distance when the network upgrades. Deploying a switch instead of a hub eliminates collision domains immediately, but creates the possibility of Layer 2 loops if redundant links are added without proper protocol support. Every design decision has trade-offs. The discussions this week should reflect that nuance — there is rarely one single correct answer when it comes to infrastructure design, but there are always specifications and standards that constrain the options.

---

*CIS-3321 Network Administration | Texas Wesleyan University | Professor Nash*
