# Discussion Forum: Module 05 - Network Traffic Analysis and Packet Inspection

## Course: CIS-4332 Cyber Analyst | Texas Wesleyan University

## Instructor: Professor Nash

## CySA+ CS0-003 Domain: Domain 1 - Security Operations (33%)

---

## Overview

Network traffic analysis requires you to reason about what data means even when you cannot see the payload — especially as encryption becomes ubiquitous. This week's discussion asks you to apply traffic pattern analysis, IDS/IPS placement reasoning, and encrypted traffic investigation techniques to realistic scenarios. Strong initial posts cite specific protocols, port numbers, and traffic characteristics as evidence. Vague references to "suspicious traffic" without technical specificity will not earn full credit.

Initial Post: Due Wednesday at 11:59 PM

Peer Responses: Due Sunday at 11:59 PM (minimum two responses)

---

## Scenario A: The Encrypted Blind Spot

Your organization's CISO reviews a security incident report and asks a pointed question: "Our entire network is now HTTPS. If everything is encrypted, what exactly is our network monitoring team watching?" The security manager replies that the team has full visibility because they can see all connections in the firewall logs. You disagree with both the CISO's implication and the security manager's answer.

In 175-225 words, address all three of the following points:

1. Explain what network metadata remains visible for encrypted HTTPS connections — be specific about at least three distinct data elements — and why this metadata still has investigative and detection value.
2. Identify two specific attack techniques that can be detected using only encrypted traffic metadata, without decrypting the payload. Reference the specific metadata field that reveals each technique.
3. Describe one detection capability that metadata alone cannot provide, and identify the security architecture investment that would restore that capability.

---

## Scenario B: The Beaconing Investigation

The SIEM generates a Medium-severity alert: "Potential C2 Beaconing — Internal host 10.0.7.33 making repeated outbound connections to 198.51.100.200:443 at 180-second intervals." Your asset inventory shows 10.0.7.33 is a developer workstation running Windows 11. The destination IP resolves to a domain registered 6 months ago that does not appear in any known-malicious threat feed.

In 175-225 words, address all three of the following points:

1. Identify what additional network-level evidence you would collect to determine whether this is a true positive or a false positive. Name at least two specific data sources or metadata fields beyond what the alert already contains.
2. Explain why the absence of a known-malicious TI hit for the destination IP does not rule out malicious activity. What other characteristics of the destination would you investigate?
3. Describe the ATT&CK tactic and technique this traffic pattern maps to if it is confirmed as malicious, and explain what a Tier 1 analyst should include in the escalation note to Tier 2.

---

## Scenario C: The Lateral Movement Evidence

During a threat hunting exercise, your team analyzes NetFlow data and discovers that over the past 48 hours, a single internal workstation (10.0.4.88) has made successful TCP connections to port 445 on 31 different internal hosts. The workstation is assigned to an account manager with no administrative privileges or legitimate need to access other users' workstations.

In 175-225 words, address all three of the following points:

1. Explain the significance of workstation-to-workstation port 445 traffic and why this is anomalous compared to normal SMB usage in a domain environment. Name the ATT&CK technique this most likely represents.
2. Identify two additional log sources beyond NetFlow data that you would examine to determine whether this represents an active compromise or a legitimate but unusual activity, and describe what specific evidence you would look for in each source.
3. Assume this is a confirmed lateral movement attempt. Describe the immediate response steps a Tier 2 analyst should take, and explain what network-layer control could be implemented to prevent this type of lateral movement across the environment.

---

## Peer Response Guidelines

When replying to classmates, your response must be at least 75 words and must do one or more of the following:

- Identify a metadata field or network indicator the original post did not mention
- Challenge an ATT&CK mapping with a more specific technique or sub-technique
- Propose an alternative detection rule or network control
- Connect the scenario to a real-world attack pattern or published incident report

Responses consisting only of agreement without technical substance will receive no credit.

---

## Discussion Rubric (10 Points Total)

### Initial Post (6 Points)

- 5-6 points: All three prompt points addressed with technical precision. Specific protocols, port numbers, and traffic characteristics cited as evidence. ATT&CK techniques referenced where applicable. Meets 175-225 word count.
- 3-4 points: Most prompt points addressed. Some technical specificity. Meets minimum word count.
- 1-2 points: Fewer than two points addressed, lacks technical specificity, or below minimum word count.
- 0 points: No initial post submitted.

### Peer Responses (4 Points)

- 4 points: Two or more substantive responses of 75 words each with specific technical additions.
- 2 points: One qualifying response or both are superficial.
- 0 points: No responses submitted.

---

## A Note from Professor Nash

The best network analysts I have known can look at a flow record and tell you in seconds whether something is wrong — not because they have a checklist, but because they understand what normal traffic looks like and immediately notice when something deviates from that pattern. The skills you practice here — reading flow records, recognizing beaconing signatures, understanding what metadata survives encryption — are the same skills that will let you find an attacker who has been hiding in your network for weeks. That matters.
