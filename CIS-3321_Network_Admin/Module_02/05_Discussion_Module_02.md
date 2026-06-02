# Discussion Forum: Module 02 – TCP/IP Model and Network Protocols
## CIS-3321 Network Administration | CompTIA Network+ (N10-008)
## Texas Wesleyan University | Professor Nash

---

### Overview

This week's discussion connects the TCP/IP model and protocol fundamentals to real-world network administration scenarios. You will choose one of three scenarios below and respond with a substantive initial post of 175–225 words. After posting, respond to at least two classmates who chose different scenarios.

---

### Choose One Scenario

#### Scenario A: The DHCP Outage

On Monday morning, approximately 200 employees arrive at work and find that their computers will not connect to the network. The help desk receives a flood of tickets describing "no network access." A technician checks one of the affected workstations and notices the IP address is 169.254.14.9. Pinging the default gateway fails. Another technician checks the network server room and notices the DHCP server is offline due to a failed hard drive.

Respond to all three questions:

1. Explain the DHCP DORA process and identify specifically at which step the failure occurred in this scenario. Why did the workstations end up with 169.254.x.x addresses instead of their normal IP configuration?
2. As an emergency temporary fix, a technician manually assigns a static IP address to one workstation. What four pieces of network configuration information must be manually entered for the workstation to have full network access, and at which TCP/IP model layer does each piece of information operate?
3. What long-term solution would you recommend to prevent a single DHCP server failure from taking down the entire network? Describe the concept briefly.

---

#### Scenario B: Protocol Identification Under Audit

A security auditor at a healthcare company runs a port scan on the network and provides the following report to the network administrator: Port 23 is open on three network switches. Port 80 is open on the internal web server. Port 110 is open on the mail server. The auditor flags all three as security risks and recommends replacements.

Respond to all three questions:

1. For each of the three flagged ports, identify the protocol name and explain specifically why the auditor considers it a security risk. What information is exposed if these protocols are used?
2. For each flagged port, identify the recommended secure replacement protocol and port number. Explain what security mechanism (specifically TLS, encryption, or authentication) the replacement provides.
3. The auditor also noted that DNS (port 53) is open on multiple internal servers and uses UDP. Is this a security concern? Explain when DNS uses UDP versus TCP and whether UDP-based DNS represents a risk in this environment.

---

#### Scenario C: Troubleshooting with ICMP

A network administrator at a university receives a complaint that students in one building cannot access external websites, but they can access the internal student portal. The administrator opens a terminal on the affected network segment and runs the following tests:

- ping 8.8.8.8 — Request timed out (100% packet loss)
- ping 10.0.1.1 (default gateway) — 4/4 replies received
- tracert 8.8.8.8 — first hop (10.0.1.1) responds, second hop times out

Respond to all three questions:

1. Based on the ping and tracert results, at which network boundary is connectivity failing? Be specific about which device is the likely point of failure and explain your reasoning using the test results.
2. The administrator confirms the internal gateway is functional. What is the most likely next device to investigate, and what type of configuration problem might be causing the failure at that device? Use proper TCP/IP model layer terminology in your response.
3. The administrator successfully pings 8.8.8.8 after the issue is resolved, but students still cannot browse websites by name. What additional protocol might now be misconfigured, and how would you test it using the command-line tools covered in this module?

---

### Response Requirements

**Initial Post (due Wednesday at 11:59 PM):**

- Choose exactly one scenario (A, B, or C)
- Write 175–225 words
- Identify which scenario you chose in your first sentence
- Answer all three sub-questions for your chosen scenario
- Use correct networking terminology (protocol names, port numbers, TCP/IP layer names)

**Peer Responses (due Sunday at 11:59 PM):**

- Reply to at least two classmates who chose different scenarios than you
- Each reply must be at least 60 words
- Offer a specific technical addition, correction, or alternative perspective — do not simply agree or summarize

---

### Grading Rubric (10 Points Total)

**Initial Post — 6 Points:**

- 5–6 points: All three sub-questions answered with technical accuracy, correct protocol names and port numbers, appropriate terminology, and meets the 175–225 word count.
- 3–4 points: Addresses most sub-questions but lacks technical depth or contains a protocol/port error.
- 1–2 points: Post is incomplete, off-topic, or contains significant technical inaccuracies.
- 0 points: No initial post submitted.

**Peer Responses — 4 Points:**

- 4 points: Substantive responses to two classmates who chose different scenarios, each at least 60 words, adding technical value.
- 2 points: Responded to only one classmate, or both responses lack technical substance.
- 0 points: No peer responses submitted.

---

### Professor Nash's Note

Network protocols are the language devices use to communicate, and port numbers are the addresses within a device that determine which service receives the data. Every troubleshooting scenario you will encounter in your career will require you to know which protocol is involved, which port it uses, and whether it is TCP or UDP. This week's discussion is an opportunity to apply that knowledge to situations you will actually face. The scenarios above are based on real events. Read them carefully and think through the protocol layer by layer.

---

*CIS-3321 Network Administration | Texas Wesleyan University | Professor Nash*
