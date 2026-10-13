# Discussion Forum: Module 16 — Security+ SY0-701 Exam Preparation and Capstone

## Course: CIS-4328 Information Security

## Texas Wesleyan University | Professor Nash

## Certification Alignment: CompTIA Security+ (SY0-701)

---

## Discussion Prompt

This final discussion asks you to apply all five Security+ exam domains to a realistic, multi-layered security incident. Rather than answering a single-domain question, you will reason across the entire course — threat identification, architecture response, operations, and program management — and then engage critically with your classmates' analyses.

The SY0-701 exam is 90 questions of scenario-based reasoning. This discussion builds exactly that cross-domain reasoning skill.

---

### Scenario

A regional hospital network with 12 facilities operates a cloud-hosted patient records system (SaaS), an on-premises radiology imaging server, and a corporate email platform. The hospital has approximately 3,400 employees.

On a Monday morning, the following events occur nearly simultaneously:

- The radiology imaging server stops responding. A technician rebooting it discovers all image files have been encrypted and a ransom note demands $850,000 in Bitcoin within 72 hours.
- Three executives receive emails appearing to come from the hospital's CFO asking them to approve wire transfers to a new vendor. The emails contain the CFO's signature block and reference a real ongoing contract.
- The SaaS patient records vendor calls to report "unusual API access patterns" from the hospital's IP range over the weekend — specifically, bulk record downloads between 2:00 AM and 4:00 AM on Saturday and Sunday.

The hospital has a cybersecurity team of four analysts and a CISO. They have a SIEM, endpoint detection and response (EDR) on all workstations, and a basic incident response plan that has not been tested in two years.

---

### Your Tasks

#### Initial Post (Due Wednesday at 11:59 PM)

In 300–375 words, analyze this incident using the five Security+ domains as your analytical framework. Your post must address all five areas:

**Domain 1 — General Security Concepts**: Identify the authentication or cryptography-related weakness most likely exploited in at least one of the three attack vectors. Specify which control (e.g., MFA type, PKI element, or access model) would have reduced the risk.

**Domain 2 — Threats, Vulnerabilities, and Mitigations**: Name the specific threat actor type and attack techniques being used across the three attack vectors. Map at least one technique to a MITRE ATT&CK tactic by name (not just technique number).

**Domain 3 — Security Architecture**: The radiology server is on-premises while patient records are SaaS. Identify one architectural weakness visible in this incident and describe a specific architectural control (network segmentation, Zero Trust principle, or cloud security configuration) that would have reduced the blast radius.

**Domain 4 — Security Operations**: The team of four analysts faces three simultaneous incidents. Describe how they should prioritize and triage using the NIST IR lifecycle. Which incident should be contained first and why? What specific evidence should be preserved immediately before any eradication begins?

**Domain 5 — Program Management and Oversight**: This incident almost certainly triggers at least one regulatory notification obligation. Identify the specific regulation(s) that apply to a US hospital and state the notification timeline requirement. Also identify which risk treatment strategy the hospital apparently relied on for the on-premises radiology server, and evaluate whether that was appropriate given the asset's value.

Use correct, specific Security+ terminology throughout.

---

#### Peer Responses (Due Sunday at 11:59 PM)

Write substantive replies of at least 80 words each to at least two classmates. For each reply, evaluate one of the following aspects of your peer's analysis:

- Did your peer correctly identify the MITRE ATT&CK tactic for at least one of the three attack vectors? If they named the wrong tactic or confused a tactic with a technique, explain the distinction.
- Did your peer correctly identify which regulation applies and state the correct notification timeline? HIPAA has a specific breach notification deadline — evaluate whether your peer stated it accurately.
- Did your peer's Domain 4 triage prioritization hold up under scrutiny? The correct priority order has a defensible rationale — evaluate the reasoning, not just the conclusion.

---

## Instructor Notes for Grading

Strong initial posts will demonstrate the following:

**Domain 1**: The BEC email attack exploits missing DMARC/DKIM email authentication and the lack of MFA on the CFO's account (or email impersonation bypassing MFA entirely). The bulk API download exploits inadequate session token controls or missing MFA on API access. Full credit requires naming a specific control, not just "add MFA."

**Domain 2**: All three vectors are consistent with a coordinated APT or organized crime campaign. The ransomware maps to MITRE ATT&CK Tactic: Impact (T1486 — Data Encrypted for Impact). The BEC maps to Tactic: Initial Access or Collection via social engineering. The bulk download maps to Tactic: Exfiltration. Full credit requires at least one tactic named correctly.

**Domain 3**: The radiology server should be on an isolated network segment (air-gapped or micro-segmented) that cannot be reached from workstations that handle email. A Zero Trust architecture would require re-authentication for lateral movement from a compromised endpoint to the imaging server. Shared network segments without micro-segmentation are the visible weakness.

**Domain 4**: Correct prioritization is: (1) contain the radiology ransomware — it is active, spreading, and directly impacting patient care; (2) investigate the BEC emails — at least three executives may authorize fraudulent transfers; (3) work with the SaaS vendor on the API exfiltration — the attack window is closed (weekend), so immediate containment is lower urgency than the active ransomware. Forensic images of the radiology server and SIEM log export must occur before any reimaging.

**Domain 5**: HIPAA Breach Notification Rule requires notification to HHS within 60 days of discovery for breaches affecting 500 or more individuals; media notice if the breach affects 500+ individuals in a state; and individual notification without unreasonable delay. The risk treatment for the on-premises radiology server appears to have been risk acceptance (no encryption at rest, no network isolation) — likely inappropriate given that radiology servers store PHI and are critical to patient care continuity.

Common errors to watch for:

- Misidentifying BEC as "phishing" without the more specific term (whaling or BEC)
- Stating GDPR notification timelines (72 hours) instead of HIPAA (60 days) for a US hospital
- Prioritizing the API exfiltration over the active ransomware
- Confusing risk transference (cyber insurance) with risk acceptance
- Stating "encrypt the drive" as the Domain 3 architectural fix without addressing network segmentation

---

## Discussion Rubric

| Component | Points | Criteria |
|---|---|---|
| Initial Post — Domain 1 | 2 | Specific auth/crypto weakness named; specific control recommended |
| Initial Post — Domain 2 | 2 | Threat actor type correct; at least one MITRE ATT&CK tactic named accurately |
| Initial Post — Domain 3 | 2 | Architectural weakness identified; specific control named (not generic "add firewall") |
| Initial Post — Domain 4 | 2 | Triage prioritization with defensible rationale; specific evidence preservation named |
| Initial Post — Domain 5 | 2 | Correct regulation named; correct notification timeline; risk treatment evaluated |
| Peer Response 1 | 2 | Substantive evaluation of tactic, regulation, or triage reasoning |
| Peer Response 2 | 2 | Substantive evaluation of tactic, regulation, or triage reasoning |
| Word count and terminology | 1 | 300–375 words initial post; 80+ words per peer reply; Security+ terms used correctly |
| Total | 15 | |

---

## Course Closing Note

This is the final discussion for CIS-4328 Information Security. Over sixteen modules, you have built a rigorous foundation in the five domains of the CompTIA Security+ SY0-701 certification: General Security Concepts, Threats and Vulnerabilities, Security Architecture, Security Operations, and Security Program Management.

The scenario in this final discussion reflects the reality of security work — incidents are rarely clean, single-domain problems. They arrive simultaneously, involve multiple attack vectors, and demand decisions under pressure with incomplete information. Your ability to reason across all five domains at once is exactly what the certification exam — and your future employers — will require.

The SY0-701 exam measures whether you can do what you just did in this discussion prompt: read a situation, apply the right framework, select the right control, and justify the reasoning.

You are ready. Good luck on the exam.

— Professor Nash

---

*Proprietary and Confidential. Not for disclosure outside of Texas Wesleyan University.*
