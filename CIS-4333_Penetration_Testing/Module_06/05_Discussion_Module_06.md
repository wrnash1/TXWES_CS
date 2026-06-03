# Discussion Forum: Module 06 — Scanning and Enumeration

## Course: CIS-4333 Penetration Testing

## Texas Wesleyan University | Professor Nash

## Certification Alignment: CompTIA PenTest+ (PT0-002)

---

## Professor Nash's Note on Professional Ethics

Port scanning and enumeration tools are powerful and — in the wrong hands or without authorization — illegal. The Computer Fraud and Abuse Act does not make exceptions for "learning" or "curiosity." There are documented cases of individuals being prosecuted for port scanning networks they did not own, even when no exploitation followed.

The skills you are building in this module are in high demand in the security industry precisely because they must be exercised responsibly. Every scenario below asks you to think like a professional: What are my obligations? What are the boundaries? How do I add value while protecting both the client and myself? This is the mindset that separates a security professional from someone who just runs tools.

---

## Discussion Scenario 1 — The Overeager Intern

A junior penetration tester at a consulting firm is assigned to assist on an engagement with a large regional hospital. The scope document specifies testing of `192.168.50.0/24` — the hospital's general IT network. While running a broad Nmap discovery scan, the tester notices that the hospital's network also includes subnets `192.168.100.0/24` and `192.168.200.0/24`. Curious about what is on those subnets, the tester runs a quick ping sweep against both — just to see.

The next day, the lead tester receives an urgent call from the client: biomedical devices in the cardiac care unit briefly stopped responding, and the incident correlates exactly with the unauthorized ping sweep timestamp. The devices were on `192.168.200.0/24` — the biomedical device network, explicitly excluded from scope.

**Discussion Prompt:**

In 175–225 words, address the following:

- What professional and ethical failures occurred in this scenario?
- What should the junior tester have done when noticing the additional subnets?
- What real-world harm resulted from the out-of-scope scan, and who bears responsibility?
- What controls — both technical and procedural — should a penetration testing firm have to prevent this type of incident?

**Initial Post Due:** Wednesday at 11:59 PM

**Peer Responses Due:** Sunday at 11:59 PM (minimum two responses, 75+ words each)

---

## Discussion Scenario 2 — SNMP on a Production Router

During an authorized internal penetration test at a manufacturing company, a tester discovers that all 47 network switches and routers respond to SNMP queries using the community string "public." Running snmpwalk against the core router reveals the complete routing table, all interface IP addresses, connected device hostnames, and — remarkably — the SNMP write community string stored in plaintext within the MIB: "private." The tester confirms that SNMP write access is enabled.

The client's network manager, when informed of the finding during the daily check-in call, says: "SNMP is just for monitoring. Nobody can actually do anything with read access. And write access would require someone to know our network topology anyway."

**Discussion Prompt:**

In 175–225 words, address the following:

- Is the network manager's assessment accurate? What specific attacks become possible with SNMP read and write access?
- How should the tester communicate the actual severity of this finding to a non-technical stakeholder?
- What CVSS components (Attack Vector, Complexity, Privileges Required, Impact) would you assign to the SNMP write access finding, and why?
- What remediation steps should be recommended?

**Initial Post Due:** Wednesday at 11:59 PM

**Peer Responses Due:** Sunday at 11:59 PM (minimum two responses, 75+ words each)

---

## Discussion Scenario 3 — Noisy Tools in a Stealth Engagement

A penetration tester is hired for a red team engagement. The rules of engagement specify that the test should simulate an advanced persistent threat actor — meaning the tester should attempt to remain undetected throughout the engagement. The client's security operations center (SOC) is specifically tasked with detecting and responding to the simulated attacker as part of a parallel blue team exercise.

The tester begins scanning by running `nmap -A -p- --script=vuln 192.168.1.0/24` from their attack VM. Within 90 seconds, the SOC calls the tester's point of contact to report that they have detected and blocked the attack machine. The entire red team exercise is effectively over.

**Discussion Prompt:**

In 175–225 words, address the following:

- What scanning choices led to immediate detection, and what does this reveal about the relationship between tool selection and operational security?
- How should a tester approach scanning differently in a stealth engagement compared to a standard penetration test?
- What Nmap options and alternative techniques would reduce detection likelihood during a red team engagement?
- What does this scenario teach about the importance of understanding the engagement type before selecting tools and techniques?

**Initial Post Due:** Wednesday at 11:59 PM

**Peer Responses Due:** Sunday at 11:59 PM (minimum two responses, 75+ words each)

---

## Discussion Rubric (10 Points Total)

| Component | Points | Criteria |
|-----------|--------|---------|
| Initial Post — Technical Accuracy | 3 | Demonstrates accurate understanding of scanning/enumeration concepts from Module 06 |
| Initial Post — Ethical Reasoning | 2 | Addresses scope, authorization, and professional obligations with specificity |
| Initial Post — Word Count and Format | 1 | 175–225 words, organized response, professional tone |
| Peer Response 1 | 2 | Minimum 75 words, adds substantive analysis or challenges a point with reasoning |
| Peer Response 2 | 2 | Minimum 75 words, introduces a new consideration or connects to course concepts |

---

**Proprietary and Confidential. Not for disclosure outside of Texas Wesleyan University course use.**
