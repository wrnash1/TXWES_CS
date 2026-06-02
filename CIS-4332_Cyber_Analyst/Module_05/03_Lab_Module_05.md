# Lab Activity: Module 05 - Network Traffic Analysis and Packet Inspection

## Course: CIS-4332 Cyber Analyst | Texas Wesleyan University

## Instructor: Professor Nash

## CySA+ CS0-003 Domain: Domain 1 - Security Operations (33%)

---

## Lab Overview

In this lab you will analyze network flow data and packet-level descriptions to identify suspicious traffic patterns, classify attack types, and recommend detection and response actions. All data is provided within this document. No network capture tools or external connectivity are required.

Total Points: 100

Estimated Completion Time: 75-90 minutes

Submission: Upload your completed Lab Report to the Canvas Module 05 Lab assignment.

---

## Learning Objectives

By completing this lab you will be able to:

- Interpret NetFlow records and identify suspicious communication patterns
- Classify TCP flag combinations and their security significance
- Identify network-level indicators of port scanning, beaconing, DNS tunneling, and lateral movement
- Recommend IDS/IPS rule logic to detect identified patterns
- Connect observed traffic patterns to ATT&CK tactics and techniques

---

## Exercise 1: NetFlow Analysis (30 points)

### Exercise 1 Overview

The following NetFlow records were collected over a 6-hour monitoring window from an organization's perimeter router. Review all records and complete the tasks below.

### NetFlow Records

```text
Flow ID | Src IP         | Dst IP         | Src Port | Dst Port | Proto | Bytes  | Packets | Duration | Interval from prev same pair
F-01    | 198.51.100.22  | 10.0.1.5       | 54001    | 22       | TCP   | 512    | 8       | 0.4s     | N/A (first)
F-02    | 198.51.100.22  | 10.0.1.5       | 54002    | 22       | TCP   | 512    | 8       | 0.4s     | 2.1 seconds
F-03    | 198.51.100.22  | 10.0.1.5       | 54003    | 22       | TCP   | 512    | 8       | 0.4s     | 2.0 seconds
... [entries F-04 through F-52 follow identical pattern -- source port increments by 1, all other fields identical] ...
F-52    | 198.51.100.22  | 10.0.1.5       | 54052    | 22       | TCP   | 512    | 8       | 0.4s     | 2.1 seconds

F-53    | 10.0.8.44      | 93.184.216.34  | 51200    | 443      | TCP   | 1,248  | 12      | 3.2s     | N/A (first)
F-54    | 10.0.8.44      | 93.184.216.34  | 51201    | 443      | TCP   | 1,247  | 12      | 3.1s     | 300.0 seconds
F-55    | 10.0.8.44      | 93.184.216.34  | 51202    | 443      | TCP   | 1,249  | 12      | 3.2s     | 300.2 seconds
F-56    | 10.0.8.44      | 93.184.216.34  | 51203    | 443      | TCP   | 1,248  | 12      | 3.1s     | 299.8 seconds
... [pattern continues for 48 total flows over 4-hour window, intervals all within 300 +/- 1 second] ...

F-100   | 10.0.3.77      | 10.0.3.12      | 49200    | 445      | TCP   | 82,400 | 290     | 45.2s    | N/A
F-101   | 10.0.3.77      | 10.0.3.18      | 49201    | 445      | TCP   | 79,100 | 275     | 42.1s    | 12.3 seconds
F-102   | 10.0.3.77      | 10.0.3.24      | 49202    | 445      | TCP   | 81,200 | 280     | 43.5s    | 11.7 seconds
F-103   | 10.0.3.77      | 10.0.3.30      | 49203    | 445      | TCP   | 80,500 | 279     | 43.9s    | 12.1 seconds
F-104   | 10.0.3.77      | 10.0.3.36      | 49204    | 445      | TCP   | 78,900 | 272     | 41.8s    | 11.9 seconds

F-200   | 10.0.5.99      | 8.8.8.8        | 54321    | 53       | UDP   | 847    | 1       | 0.1s     | N/A
F-201   | 10.0.5.99      | 8.8.8.8        | 54322    | 53       | UDP   | 831    | 1       | 0.1s     | 0.3 seconds
F-202   | 10.0.5.99      | 8.8.8.8        | 54323    | 53       | UDP   | 792    | 1       | 0.1s     | 0.3 seconds
... [entries F-200 through F-530 follow this pattern -- 331 DNS queries in 2 minutes, all to 8.8.8.8 port 53] ...
```

### Task 1A — Pattern Identification (15 points)

For each flow group (F-01 to F-52; F-53 to F-100; F-100 to F-104; F-200 to F-530), identify the suspicious traffic pattern, name the likely attack or malicious behavior, and identify the ATT&CK tactic and technique. Answer in 3-4 sentences per group.

### Task 1B — Flow Data Questions (15 points)

Answer each question in 3-4 sentences, referencing specific flow fields as evidence.

Flow Question 1: Flows F-53 through the 48-flow series show connections to port 443 (HTTPS) at exactly 300-second intervals. A colleague says: "This can't be malicious — it's encrypted HTTPS traffic to a known IP. We can't see the payload, so there's nothing to investigate." How do you respond? What does the flow data reveal about this traffic even without payload visibility?

Flow Question 2: Flows F-100 through F-104 show one internal host (10.0.3.77) making SMB connections (port 445) to five other internal hosts in rapid succession. Your asset inventory shows 10.0.3.77 is a standard employee workstation. What does this pattern indicate, and what ATT&CK technique does it map to?

Flow Question 3: Flows F-200 through F-530 show 331 DNS queries in approximately 2 minutes from one internal host. Each query is over 800 bytes — significantly larger than a typical DNS query. What does this pattern indicate, and what two specific DNS log fields would you examine to confirm your hypothesis?

---

## Exercise 2: TCP Flag and Packet Analysis (30 points)

### Exercise 2 Overview

The following packet descriptions represent captured traffic during a monitoring window. For each scenario, analyze the TCP flags or packet characteristics and answer the questions.

### Packet Scenario 2-A

A network analyst captures the following sequence from external IP 203.0.113.5 to internal web server 10.0.1.100 over a 45-second window:

```text
203.0.113.5 -> 10.0.1.100:21    TCP [SYN]        -> RST from server
203.0.113.5 -> 10.0.1.100:22    TCP [SYN]        -> SYN-ACK from server (port open)
203.0.113.5 -> 10.0.1.100:23    TCP [SYN]        -> RST from server
203.0.113.5 -> 10.0.1.100:25    TCP [SYN]        -> RST from server
203.0.113.5 -> 10.0.1.100:53    TCP [SYN]        -> RST from server
203.0.113.5 -> 10.0.1.100:80    TCP [SYN]        -> SYN-ACK from server (port open)
203.0.113.5 -> 10.0.1.100:110   TCP [SYN]        -> RST from server
203.0.113.5 -> 10.0.1.100:143   TCP [SYN]        -> RST from server
203.0.113.5 -> 10.0.1.100:443   TCP [SYN]        -> SYN-ACK from server (port open)
203.0.113.5 -> 10.0.1.100:445   TCP [SYN]        -> RST from server
[...continues through port 1024, total of ~1000 port probes in 45 seconds]
```

Packet Scenario 2-A Questions (10 points):

2-A-1: What type of scan does this traffic represent? Name it using the correct technical term. (3 points)

2-A-2: Why is this scan type less likely to appear in many firewall logs compared to a full connect scan? What specific TCP characteristic allows it to evade some older detection systems? (4 points)

2-A-3: What three open ports were identified by this scan, and what services do they represent? What security implication does having port 22 (SSH) open on an internet-facing server have? (3 points)

### Packet Scenario 2-B

An analyst reviews ICMP traffic from internal host 10.0.4.22 to external IP 185.220.101.90. The ICMP type is 8 (echo request) in all packets. However, the payload size field is consistently 1,420 bytes instead of the typical 32-64 bytes of a standard ping. The traffic occurs at 60-second intervals, 24 packets per day.

Packet Scenario 2-B Questions (10 points):

2-B-1: What does the unusual ICMP payload size suggest about the nature of this traffic? What attack technique does this most closely represent? (4 points)

2-B-2: Calculate the approximate data volume that could be transmitted per day using this ICMP channel (24 packets x 1,420 bytes). How does this compare to the data volume of normal ping traffic? Express your answer in KB and interpret what this volume could represent. (3 points)

2-B-3: Write a Wireshark display filter that would isolate large ICMP echo requests (payload greater than 100 bytes) from a specific source IP to help investigate this pattern. (3 points)

### Packet Scenario 2-C

During a TLS session analysis, a security tool extracts the following JA3 hash from an outbound TLS connection from workstation 10.0.9.55:

JA3: `769,47-53-5-10-49161-49162-49171-49172-50-56-19-4,0-10-11,23-24-25,0`

The security team's threat intelligence database returns a match: this JA3 hash is associated with a known remote access trojan that uses TLS 1.0 with a specific cipher suite pattern.

Packet Scenario 2-C Questions (10 points):

2-C-1: Explain in 3-4 sentences what a JA3 hash is, what parameters it is derived from, and why knowing the JA3 hash of a known malware family is valuable even when the payload is encrypted. (5 points)

2-C-2: The connection from 10.0.9.55 is going to an HTTPS server on port 443. Your colleague says "it is obviously just web browsing — HTTPS is normal traffic." Explain in 3-4 sentences why this reasoning is flawed and what the JA3 match tells you that inspecting the port number alone cannot. (5 points)

---

## Exercise 3: IDS/IPS Analysis (25 points)

### Exercise 3 Overview

You are designing detection coverage for the traffic patterns identified in Exercises 1 and 2.

### Task 3A — IDS vs. IPS Placement Decision (10 points)

For each deployment scenario below, recommend whether you would use a NIDS (passive, SPAN port) or a NIPS (inline, blocking) and justify your recommendation in 3-4 sentences.

Scenario 3-A-1: You want to monitor all traffic entering and leaving the organization's primary data center without any risk of impacting network availability. The data center handles 40 Gbps of peak traffic.

Scenario 3-A-2: You want to block known malware C2 communication patterns in real time before they can exfiltrate data from compromised endpoints.

### Task 3B — Detection Rule Design (15 points)

Write detection rule descriptions (in plain English) for three of the patterns identified in Exercise 1. For each rule, specify:

- The traffic pattern being detected (which exercise flow group)
- The detection method: signature-based, anomaly-based, or behavioral
- The specific fields and thresholds the rule uses
- What the alert message should say
- One false positive scenario the rule might trigger and how you would tune it

Format each rule description using this template:

```text
Rule Name:          [Descriptive name]
Pattern Targeted:   [Which flow group from Exercise 1]
Detection Method:   [Signature / Anomaly / Behavioral]
Trigger Condition:  [Fields, thresholds, time windows]
Alert Message:      [What the analyst sees in the alert queue]
False Positive Risk:[What legitimate activity could trigger this rule]
Tuning Suggestion:  [How to reduce false positives]
```

---

## Exercise 4: Encrypted Traffic Investigation (15 points)

### Exercise 4 Overview

Your organization's security operations team has determined that inspecting encrypted traffic payloads is not currently feasible due to privacy policy constraints and technical complexity. You need to build detection capabilities using only the metadata available without decryption.

### Task 4A — Metadata-Only Detection Capability (10 points)

For each of the following attack scenarios, describe in 3-4 sentences what specific network metadata (flow data, TLS handshake fields, DNS logs) you would use to detect or investigate the activity without decrypting payloads.

Attack Scenario 1: An attacker using HTTPS over port 443 to beacon to a C2 server every 5 minutes.

Attack Scenario 2: An attacker using DNS queries to exfiltrate data from an air-gapped segment via an internal DNS resolver.

Attack Scenario 3: A malware sample using TLS 1.0 with a non-standard cipher suite for C2 communication.

### Task 4B — Visibility Gap Analysis (5 points)

In 4-5 sentences, describe the most significant investigative limitation created by the inability to inspect encrypted payloads, and recommend one organizational security architecture investment that would provide payload visibility into the highest-risk network segments without requiring full decryption of all enterprise traffic.

---

## Grading Rubric

| Exercise | Points | Grading Criteria |
|---|---|---|
| Exercise 1A — Pattern Identification | 15 | Correct pattern named; ATT&CK tactic/technique accurate; evidence-based reasoning |
| Exercise 1B — Flow Data Questions | 15 | Technically accurate; references specific flow fields; 3-4 sentences each |
| Exercise 2A — Scan Analysis | 10 | Correct scan type; evasion characteristic; open port identification |
| Exercise 2B — ICMP Analysis | 10 | Correct technique identification; calculation accurate; valid Wireshark filter |
| Exercise 2C — JA3 Analysis | 10 | Accurate JA3 definition; correct reasoning about port vs. TLS fingerprint |
| Exercise 3A — IDS/IPS Placement | 10 | Correct recommendation; accurate justification based on placement characteristics |
| Exercise 3B — Rule Design | 15 | All template fields complete; detection logic accurate; false positive awareness |
| Exercise 4A — Metadata Detection | 10 | Specific metadata fields identified; accurate detection reasoning |
| Exercise 4B — Visibility Gap Analysis | 5 | Honest assessment of limitation; practical, specific recommendation |
| Total | 100 | |

---

## Submission Instructions

1. Use the Lab Report Template from Canvas or a clearly labeled document matching this lab's section structure.
2. Include your full name, student ID, course section, and submission date.
3. Present all code or filter syntax in code-formatted blocks.
4. Submit to the Canvas Module 05 Lab assignment by the posted deadline.

---

## Academic Integrity Notice

All network data in this lab is fabricated for educational purposes. No real systems are involved. All work must be your own. Reference professormesser.com and comptia.org for additional study context.
