# Lab Activity: Module 11 - Network Hardware & Connectors

**Course:** CIS-2320 Hardware Fundamentals
**Certification Alignment:** CompTIA A+ Core 1 (220-1101) — Domain 2.1, Domain 2.2
**Texas Wesleyan University | Professor Nash**
**Total Points: 100**

---

## Overview

This lab reinforces the physical identification and wiring skills tested on the CompTIA A+ Core 1 exam. You will examine Ethernet cable category specifications, identify copper and fiber connector types from descriptions and diagrams, complete a T568A vs T568B wiring diagram exercise, and work through a simulated cable tester output analysis. No physical crimping tools are required — all exercises use observation, reference materials, and structured written responses.

**Learning Objectives:**

- Identify Ethernet cable categories by speed, distance, and physical characteristics
- Distinguish RJ-45 from RJ-11 connectors and state their correct applications
- Name and describe ST, SC, and LC fiber optic connectors
- Complete a T568B and T568A pin-out table from memory and verify it
- Analyze a cable tester result and diagnose the likely fault

**Estimated Completion Time:** 60-90 minutes

**Submission:** Submit your completed lab document (typed responses) to Canvas by the posted due date.

---

## Part 1 — Ethernet Cable Category Identification (30 points)

### Part 1A — Cable Category Specification Fill-In Table

Using your Reading Guide and video notes, complete the following table. Do not look at the completed version in the Reading Guide until after you have attempted the table from memory.

| Category | Max Data Rate | Max Distance at Max Rate | 10 Gbps Capable? | Connector Type |
|----------|--------------|--------------------------|-----------------|----------------|
| Cat5e | | | | |
| Cat6 | | | | |
| Cat6a | | | | |

After filling in the table, answer the following questions in complete sentences.

**Question 1A-1:** A facilities manager tells you that a new wing of the building has Cat6 cable already installed in the walls. All runs are 90 meters from the wiring closet. The company plans to deploy 10 Gbps switches next quarter. Will the existing Cat6 cabling support 10 Gbps on those 90-meter runs? Explain why or why not, and state what would need to change if the answer is no.

*Your answer:*

**Question 1A-2:** A contractor proposes running Cat5e cable for a new office build-out because it is less expensive than Cat6a. The runs will all be under 50 meters and the network will use standard 1 Gbps switching. Is Cat5e acceptable for this installation? Justify your answer using the specification table above.

*Your answer:*

**Question 1A-3:** Describe one physical difference you can observe between a Cat6 cable and a Cat6a cable when the outer jacket is cut open. Explain why that physical difference exists.

*Your answer:*

---

### Part 1B — Cable Jacket Rating Identification

Match each installation scenario to the correct jacket rating. Write the letter of the correct rating next to each scenario.

**Jacket Ratings:**

- A) PVC (standard)
- B) Riser (CMR)
- C) Plenum (CMP)

**Scenarios:**

| Scenario | Rating (A, B, or C) |
|----------|-------------------|
| Running cable through the air-handling space above a drop ceiling | |
| Running cable vertically through a conduit between two floors inside a wall | |
| Running cable under a raised floor in a data center that does not serve as an air return | |
| Running cable in a ceiling plenum space in a building covered by fire code requiring low-smoke materials | |

---

## Part 2 — Connector Identification and Wiring Standards (40 points)

### Part 2A — Connector Identification Exercise

For each connector description below, write the connector name (RJ-45, RJ-11, ST, SC, or LC) and a one-sentence explanation of how you identified it.

**Description 1:** An 8-position modular plug with eight visible gold pins. It is 11.7 mm wide with a retaining tab on one side. Found on the end of a gray Ethernet patch cable.

*Connector Name:*
*How Identified:*

**Description 2:** A small modular plug with only two active contacts in the center of a 6-position housing. It is narrower than the Ethernet connector. Found on a telephone handset cable.

*Connector Name:*
*How Identified:*

**Description 3:** A fiber optic connector with a round body and a bayonet twist-lock coupling mechanism. The ceramic ferrule protrudes from the center. Found on a patch cable in a wiring closet installed in 1999.

*Connector Name:*
*How Identified:*

**Description 4:** A fiber optic connector with a square, rectangular body that uses a push-pull mechanism. Commonly found on older data center fiber patch panels and ISP fiber terminations.

*Connector Name:*
*How Identified:*

**Description 5:** A small fiber optic connector with a push-pull latch that is approximately half the size of Description 4. It is the connector type used on SFP transceiver modules in modern switches.

*Connector Name:*
*How Identified:*

---

### Part 2B — T568A and T568B Wiring Diagram Exercise

Complete both wiring tables below from memory, then verify against your Reading Guide.

**T568B Pin-Out (complete from memory first):**

| Pin Number | Wire Color |
|------------|-----------|
| Pin 1 | |
| Pin 2 | |
| Pin 3 | |
| Pin 4 | |
| Pin 5 | |
| Pin 6 | |
| Pin 7 | |
| Pin 8 | |

**T568A Pin-Out (complete from memory first):**

| Pin Number | Wire Color |
|------------|-----------|
| Pin 1 | |
| Pin 2 | |
| Pin 3 | |
| Pin 4 | |
| Pin 5 | |
| Pin 6 | |
| Pin 7 | |
| Pin 8 | |

**Question 2B-1:** Which pins differ between T568A and T568B? List the pin numbers and describe what changes.

*Your answer:*

**Question 2B-2:** A technician is building a cable to connect two PCs directly without a switch. Which wiring standard should be used on each end? Identify the cable type this produces.

*Your answer:*

**Question 2B-3:** A technician builds a patch cable using T568B on both ends. Which device connections is this cable appropriate for? Name at least two valid use cases.

*Your answer:*

---

## Part 3 — Cable Tester Simulation and Fault Analysis (30 points)

### Part 3A — Reading a Cable Tester Result

A technician crimps a Cat6 patch cable intended as a straight-through T568B cable. The cable is tested and the tester reports the following results:

| Pin | Result |
|-----|--------|
| Pin 1 | PASS |
| Pin 2 | PASS |
| Pin 3 | FAIL — Open |
| Pin 4 | PASS |
| Pin 5 | PASS |
| Pin 6 | FAIL — Open |
| Pin 7 | PASS |
| Pin 8 | PASS |

Answer the following questions based on the tester output.

**Question 3A-1:** Which wire color pair failed according to the T568B standard? Identify both the solid and stripe wire color for the failing pins.

*Your answer:*

**Question 3A-2:** What is the most likely physical cause of the open circuit on pins 3 and 6? Describe what likely happened during the crimping process.

*Your answer:*

**Question 3A-3:** What should the technician do to resolve the fault? Describe the corrective action step by step.

*Your answer:*

---

### Part 3B — Scenario Analysis

Read the following two scenarios and answer the question for each.

**Scenario 1:**
A user in a new office reports that their computer shows "No network connection" even though it appears to be plugged into the wall jack. The office was just wired by a contractor, and both telephone and data jacks are installed on the same wall plate using matching faceplates. The technician can see that a cable is plugged into the left jack, which the contractor labeled as the data port.

Describe two possible connector-related causes for this symptom. For each cause, state how you would confirm it and what the fix would be.

*Your answer:*

**Scenario 2:**
An organization is planning a new inter-building fiber link. The two buildings are 350 meters apart. The link must carry 10 Gbps. A vendor proposes using multimode fiber with SC connectors.

Evaluate the vendor's proposal. Is multimode fiber appropriate for this distance and speed requirement? What fiber type and connector would you recommend instead, and why?

*Your answer:*

---

## Deliverables and Grading Rubric

Submit your completed lab responses as a single typed document to the Canvas assignment portal.

| Component | Points |
|-----------|--------|
| Part 1A — Specification table (3 rows complete and correct) | 15 pts |
| Part 1A — Written questions 1A-1, 1A-2, 1A-3 (5 pts each) | 15 pts |
| Part 1B — Jacket rating matching (4 items, 1 pt each, up to 4) | 0 pts (bonus — included in Part 1 total) |
| Part 2A — Connector identification (5 items, 4 pts each) | 20 pts |
| Part 2B — T568A/B tables and questions (10 pts table accuracy, 10 pts questions) | 20 pts |
| Part 3A — Tester analysis (3 questions, 5 pts each) | 15 pts |
| Part 3B — Scenario analysis (2 scenarios, 7.5 pts each) | 15 pts |
| **Total** | **100 pts** |

**Grading Notes:**

- Tables must be complete. Partial rows receive partial credit at the instructor's discretion.
- Written responses must use correct technical terminology. Vague answers ("the cable was bad") receive no credit.
- Scenario responses must identify the correct component and explain the technical reasoning, not just state the answer.

---

## Part 9 — Challenge Exercise

These advanced steps are optional and are not included in the standard grading rubric.

### Challenge Step 1 — Cable Termination Practice

Purchase or borrow the following consumables and tools for hands-on cable termination practice (approximate cost: $15–25 for a full practice kit):

1. Using a length of Cat5e or Cat6 bulk cable (at least 2 meters), a crimping tool, RJ-45 plugs, and a wire stripper, terminate both ends of the cable using the T568B pinout. Then use a wire map tester (or a basic continuity tester with a known-good reference) to verify all eight conductors are correctly mapped. Document your results: which pairs passed, whether any pairs were open (missing continuity) or crossed (swapped between pins), and what physical error in termination would cause each failure type (open, crossed, and miswire — describe each in one sentence).
1. Re-terminate the same cable with T568A on one end and T568B on the other end to create an intentional crossover cable. Verify with the tester that pins 1/2 and 3/6 are crossed as expected. Document the tester output and explain in 2–3 sentences why a crossover cable was historically needed for direct device-to-device connections before auto-MDI/MDIX became standard.
1. Research and document the differences between a basic wire map tester (continuity only) and a professional cable certifier (Fluke DSX series or equivalent) — specifically which measurements only the certifier can perform (insertion loss, NEXT, return loss, propagation delay skew) and why these measurements are required for a Cat6a installation to be certified compliant with TIA-568-C.2.

### Challenge Step 2 — Network Switch Configuration Research

Using GNS3 (free network simulation software at gns3.com) or Cisco Packet Tracer (free at netacad.com with a free account), or by researching switch documentation:

1. Set up or research the configuration steps to create two VLANs on a managed switch: VLAN 10 for workstations and VLAN 20 for VoIP phones. Document the CLI commands (or menu steps) required to: create each VLAN, assign access ports to each VLAN, and configure a trunk port that carries both VLANs to the router. Explain in 2–3 sentences why separating VoIP traffic into its own VLAN simplifies QoS configuration compared to a flat single-VLAN network.
1. Research the IEEE 802.1p priority standard and document: the number of priority levels it defines (0–7), which priority level is recommended for VoIP traffic, and how a managed switch uses these priority values to make forwarding decisions when multiple traffic types are queued on the same port simultaneously.
1. Research PoE (Power over Ethernet) standards — IEEE 802.3af (PoE), 802.3at (PoE+), and 802.3bt (PoE++) — and build a comparison table with columns: Standard, Max Power per Port, Maximum Cable Distance, and Typical Use Case. Explain in one sentence why a PoE budget calculation is required before deploying multiple PoE devices on a single switch.

### Challenge Step 3 — Fiber Optic Research and Connector Identification

Using the Fiber Optic Association free reference guide (thefoa.org) and manufacturer documentation:

1. Build a fiber optic cable comparison table with the following columns: Cable Type, Core Diameter, Jacket Color Convention, Maximum Distance at 1 Gbps, Maximum Distance at 10 Gbps, and Primary Use Case. Include at minimum: OM1, OM2, OM3, OM4, OM5 multimode, and OS1/OS2 single-mode.
1. Research and document the physical identification characteristics that distinguish LC, SC, and ST connectors from each other (body shape, coupling mechanism, ferrule diameter, whether it is simplex or duplex by default). A field technician identifying an unknown fiber connector on a legacy building installation should be able to determine connector type from these characteristics alone without seeing product documentation.
1. Calculate the maximum supportable fiber run for a 10GBASE-SR transceiver (supports 10 Gbps over multimode fiber) connecting two data center switches. The existing fiber plant uses OM3 multimode cable. Research the maximum distance for 10GBASE-SR over OM3 and determine whether the 285-meter run between the two buildings can be supported. If not, identify the minimum fiber upgrade (OM4 or single-mode with appropriate transceiver) that would support the distance.
