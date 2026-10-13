# Discussion Forum: Module 01 – Networking Fundamentals and the OSI Model
## CIS-3321 Network Administration | CompTIA Network+ (N10-008)
## Texas Wesleyan University | Professor Nash

---

### Overview

This week's discussion connects the theoretical OSI model to real-world networking practice. You will choose one of three scenarios below and respond with a substantive initial post of 175–225 words. After posting, respond to at least two classmates who chose different scenarios.

---

### Choose One Scenario

#### Scenario A: The Mystery Outage

A junior network technician at a small company reports that three workstations in the accounting department suddenly lost all network connectivity. The rest of the building is unaffected. The technician notices the link lights on all three switch ports are dark. After replacing the cables, two workstations come back online but the third still shows no link light even with a new cable.

Respond to all three questions:

1. Using the bottom-up OSI troubleshooting approach, describe the first two layers you would check and what specific steps you would take at each layer to diagnose the problem.
2. The third workstation still has no link light after a cable replacement. What is the most likely next component to investigate, and why does this point to a specific OSI layer?
3. How does understanding the OSI model help a technician avoid "jumping to conclusions" and attempting higher-layer fixes (such as reconfiguring IP addresses) before confirming lower-layer issues?

---

#### Scenario B: Encapsulation in Practice

A network trainer is preparing a demonstration for new hires at a managed service provider. She wants to show how a single HTTP request from a browser generates multiple protocol headers before the data ever leaves the workstation. She uses Wireshark to capture the traffic and shows the team what each layer adds.

Respond to all three questions:

1. Describe the headers added at Layer 4 (Transport), Layer 3 (Network), and Layer 2 (Data Link) when the browser sends an HTTP GET request. What specific information does each header contain?
2. Explain what happens to those headers when the HTTP response arrives at the browser. Use the term "decapsulation" correctly in your response.
3. Why is it important for every device along the network path (switches, routers) to understand only the specific layer header it is responsible for, rather than reading all headers? How does this design principle improve network efficiency?

---

#### Scenario C: Physical vs. Logical Topology Mismatch

A college campus has a wiring closet where all cables from individual classrooms terminate into a large Cisco switch. From a physical standpoint, this looks like a classic star topology. However, the network administrator has configured the switch with VLANs that create separate logical segments — Faculty, Students, and Administration — that cannot communicate directly with each other without going through a router.

Respond to all three questions:

1. Explain the difference between the physical topology and the logical topology in this campus scenario. Are they the same or different? Justify your answer.
2. Which OSI layers are primarily involved in implementing VLANs (logical separation) versus which layers are involved in the physical star wiring? Identify the specific layers and explain why.
3. A student in the Students VLAN says they can reach a server in the Students VLAN but cannot reach a printer in the Faculty VLAN. Using the OSI model, explain at which layer the traffic is being blocked and what type of device would need to be involved to allow cross-VLAN communication.

---

### Response Requirements

**Initial Post (due Wednesday at 11:59 PM):**

- Choose exactly one scenario (A, B, or C)
- Write 175–225 words
- Identify which scenario you chose in your first sentence
- Answer all three sub-questions for your chosen scenario
- Use correct networking terminology (OSI layer names and numbers, PDU names, protocol names)

**Peer Responses (due Sunday at 11:59 PM):**

- Reply to at least two classmates who chose different scenarios than you
- Each reply must be at least 60 words
- Offer a specific technical addition, correction, or alternative perspective — do not simply agree or summarize their post
- If a classmate made a technical error, politely correct it with an explanation

---

### Grading Rubric (10 Points Total)

**Initial Post — 6 Points:**

- 5–6 points: All three sub-questions answered with technical accuracy, correct OSI layer references, appropriate terminology, and meets the 175–225 word count requirement.
- 3–4 points: Addresses most sub-questions but lacks technical depth, misidentifies an OSI layer, or is significantly under the word count.
- 1–2 points: Post is incomplete, off-topic, or contains significant technical inaccuracies.
- 0 points: No initial post submitted.

**Peer Responses — 4 Points:**

- 4 points: Substantive responses to two classmates who chose different scenarios, each at least 60 words, adding technical value to the conversation.
- 2 points: Responded to only one classmate, or both responses lack technical substance ("Great post!" does not qualify).
- 0 points: No peer responses submitted.

---

### Professor Nash's Note

The OSI model can feel abstract at first, but the scenarios above reflect actual situations network technicians face every week. As you work through your response, think about how knowing which layer a problem lives at changes your troubleshooting strategy entirely. A Layer 1 problem and a Layer 3 problem require completely different tools and fixes. The ability to quickly map a symptom to a layer is one of the most valuable skills you will build in this course.

---

*CIS-3321 Network Administration | Texas Wesleyan University | Professor Nash*
