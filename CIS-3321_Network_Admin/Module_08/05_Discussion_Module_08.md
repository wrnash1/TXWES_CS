# Discussion Forum: Module 08 — Network Security Concepts

## Course: CIS-3321 Network Administration

**Certification Alignment:** CompTIA Network+ (N10-008)

---

### Overview

This week's discussion applies the network security concepts from Module 08 to real-world organizational decision scenarios. You will select one of three scenarios and write a substantive initial post of 175–225 words. After posting, reply to at least two classmates who chose different scenarios.

---

### Choose One Scenario

#### Scenario A: Designing a Secure Network Architecture for a Healthcare Clinic

A regional healthcare clinic is building its first IT infrastructure from scratch. The clinic will have a public patient portal website, an internal electronic health records (EHR) system, a billing database containing payment card data, and general staff workstations. The CISO has identified three security requirements: (1) the patient portal must be accessible from the public internet without exposing the EHR or billing systems to direct internet access; (2) all staff workstations must be verified for OS patch compliance before connecting to the network; (3) unauthorized changes to patient records must be detectable.

Respond to all three questions:

1. Describe the network architecture you would design to satisfy requirement 1. Specifically identify which systems belong in the DMZ and which belong inside the internal LAN, and explain what type of firewall design (two-firewall DMZ or three-legged single-firewall) you would recommend and why.

2. Identify the technology framework that satisfies requirement 2. Explain what a posture assessment checks, what happens to a non-compliant device, and which authentication protocol the enforcement switch uses to challenge a connecting device.

3. Requirement 3 addresses which component of the CIA triad? Identify at least two specific security controls — one preventive and one detective — that protect the integrity of electronic health records.

---

#### Scenario B: Responding to a Network Security Incident

A corporate security operations center (SOC) analyst receives an alert from the IPS at 2:47 AM: a server in the accounting VLAN is sending outbound connections to a known malicious IP address on port 443, transmitting approximately 50 MB of data every 20 minutes. No legitimate business process should be running on that server at that hour. The server handles accounts payable data including vendor banking information.

Respond to all three questions:

1. Based on the traffic pattern described (outbound to a known-bad IP, recurring data transfers at unusual hours), what type of attack or compromise is most likely occurring? Identify the specific attack stage this represents in an attacker's lifecycle (initial access, lateral movement, command and control, exfiltration, etc.).

2. The analyst wants to immediately stop the data transfer without taking the server fully offline — it is needed for an early-morning payroll run. Identify two specific network-level controls the SOC team can use to block the outbound traffic while leaving the server accessible to internal accounting systems. Be specific about where each control is applied.

3. The post-incident investigation reveals the attacker accessed the server using a valid service account password obtained by monitoring network traffic. The account used Telnet for management access. Identify the CIA triad component that was violated by this credential theft, and describe two specific hardening changes that would have prevented the credential capture.

---

#### Scenario C: Security Awareness — Evaluating Common Attack Defenses

A mid-sized retail company's IT manager presents a proposed security architecture to the board of directors. She states: "We have a perimeter firewall, which stops all attacks. We also have antivirus on every endpoint. We do not need additional controls." A security consultant in the meeting disagrees and recommends layering additional controls.

Respond to all three questions:

1. The IT manager's claim that a perimeter firewall stops all attacks is incorrect. Identify two specific attack types covered in Module 08 that a perimeter firewall cannot prevent, and explain in technical terms why each bypasses perimeter firewall controls.

2. The consultant recommends adding an IPS inline behind the firewall and Dynamic ARP Inspection on all access-layer switches. Explain in your own words what specific threat each of these two additional controls addresses that the firewall does not. Why is the IPS positioned behind the firewall rather than replacing it?

3. The board asks: "What is the value of a honeypot if it does not prevent attacks?" Write a 3–4 sentence response that explains the strategic value of honeypot deployments from a defense-in-depth perspective, specifically addressing what information a honeypot provides and how that information benefits the organization's security posture.

---

### Response Requirements

Initial Post (due Wednesday at 11:59 PM):

- Choose exactly one scenario (A, B, or C)
- Write 175–225 words
- Identify which scenario you chose in your first sentence
- Answer all three sub-questions for your chosen scenario
- Use correct terminology: CIA triad, DMZ, stateful/stateless, IDS, IPS, NAC, 802.1X, RADIUS, DoS, DDoS, MITM, ARP poisoning, DAI, honeypot, defense in depth, least privilege

Peer Responses (due Sunday at 11:59 PM):

- Reply to at least two classmates who chose different scenarios than you
- Each reply must be at least 60 words
- Add a specific technical point, correction, or alternative approach — do not simply agree or summarize

---

### Grading Rubric (10 Points Total)

Initial Post — 6 Points:

- 5–6 points: All three sub-questions answered with accurate technical terminology, correct security concept application, and meets 175–225 word count.
- 3–4 points: Addresses most sub-questions but lacks technical depth or contains a specification error.
- 1–2 points: Post is incomplete, off-topic, or contains significant inaccuracies.
- 0 points: No initial post submitted.

Peer Responses — 4 Points:

- 4 points: Substantive responses to two classmates who chose different scenarios, each at least 60 words, adding genuine technical value.
- 2 points: Only one peer response, or both responses lack technical substance.
- 0 points: No peer responses submitted.

---

### Professor Nash's Note

The scenarios this week reflect situations you are likely to encounter in your first few years in networking. Healthcare and finance are the two most heavily regulated industries for data security — and they are also among the largest employers of network administrators. The incident response scenario (B) asks you to think under pressure: when the threat is active and the business clock is ticking, what do you do first? That kind of prioritized, clear thinking is what separates a competent network administrator from an exceptional one. There is rarely one perfect answer — but there are always wrong answers, and understanding why they are wrong is part of the learning.

---

CIS-3321 Network Administration | Texas Wesleyan University | Professor Nash
