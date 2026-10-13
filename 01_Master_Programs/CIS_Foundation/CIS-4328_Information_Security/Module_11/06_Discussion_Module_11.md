# Discussion: Module 11 — Incident Response

## Course: CIS-4328 Information Security

**Certification Alignment:** CompTIA Security+ (SY0-701)

---

## Discussion Overview

**Forum Title:** When the Plan Meets Reality — IR Decisions Under Pressure

**Points:** 50 points total (Initial post: 30 points | Two peer responses: 10 points each)

**Deadline:** Initial post due by Day 4 of the module week; peer responses due by Day 7

---

## Background

The 2020 SolarWinds supply chain attack is considered one of the most sophisticated cyber espionage campaigns in history. Attackers compromised SolarWinds' software build system and inserted malicious code into Orion software updates. Approximately 18,000 organizations installed the compromised update, giving attackers a foothold. The attackers remained undetected for approximately nine months. Among the victims: the US Treasury Department, the Department of Homeland Security, and numerous Fortune 500 companies.

FireEye (now Mandiant) discovered the attack not because of automated detection, but because an attacker registered a second device for MFA on an employee's account — and a security engineer noticed. FireEye's CISO Kevin Mandia published a detailed account of their discovery and response, noting that the attackers had specifically designed their malware to evade existing detection tools.

The SolarWinds attack raises profound questions about the limits of preparation, the challenge of detecting sophisticated adversaries, and the organizational decisions made under pressure during a large-scale incident.

---

## Initial Post Prompt

Choose ONE of the two scenarios below. Identify your choice at the top of your post.

### Scenario A — The Long Dwell Time Problem

SolarWinds attackers remained undetected for approximately nine months. The MTTD in this case was roughly 270 days. During that time, attackers exfiltrated sensitive government and corporate data at will.

Address all of the following in your post:

1. The SolarWinds MTTD was 270 days. What does this tell you about the limits of signature-based detection tools (like traditional IDS/AV) versus behavioral anomaly detection? Use specific examples of what each type of tool would and would not have caught.

2. The attack was ultimately discovered by a human security engineer noticing an unexpected MFA device registration — not by any automated tool. What does this suggest about the role of human judgment in security monitoring versus automated detection? Is there a lesson here for how security operations centers should be structured?

3. When FireEye discovered the attack, they had a decision to make: contain immediately (potentially alerting the attackers to detection and losing the ability to gather intelligence) or delay containment to observe attacker behavior. Using the IR concepts from this module, explain the tradeoffs in this decision. Which approach would you recommend for a company that is a victim, versus a government agency with a national security interest in the attacker's methods?

4. How does the nine-month dwell time relate to the Post-Incident Activity phase? What specific lesson should organizations derive from this MTTD for their own preparation activities?

### Scenario B — Communication Failures During Large-Scale Incidents

When a major ransomware attack hits an organization with 5,000 employees across 30 locations, the communication challenge becomes as difficult as the technical response. In the Colonial Pipeline ransomware attack (2021), communication failures contributed to panic buying, fuel shortages, and reputational damage that extended far beyond the actual operational impact of the breach.

Address all of the following in your post:

1. Colonial Pipeline shut down their pipeline operations even though it was the IT network, not the OT (Operational Technology) pipeline control network, that was compromised. From an IR communication perspective, who should have been involved in making this shutdown decision, and what information would they have needed? Use IR team roles from this module.

2. Colonial Pipeline paid the $4.4 million ransom. Evaluate this decision from an IR perspective. What guidance does NIST SP 800-61 provide about ransom payment decisions? What are the arguments for and against paying? (Note: the FBI generally advises against ransom payment.)

3. The Colonial Pipeline incident caused widespread public concern. Design a communications plan for the first 48 hours of a similarly high-profile ransomware incident at a utility company. Address: who communicates internally, who communicates with regulators, how customer/public communications are handled, and what the organization should and should not disclose at each stage.

4. What specific preparation activities, if in place before the Colonial Pipeline incident, would most likely have reduced the operational and reputational impact? Reference at least one concept from NIST SP 800-61.

---

## Initial Post Requirements

- Minimum length: 400 words
- Maximum length: 700 words
- Use proper paragraph structure — bullet lists alone do not earn full credit
- Reference at least one assigned reading from the Module 11 Reading Guide
- Factual accuracy about the SolarWinds and Colonial Pipeline incidents is expected

---

## Peer Response Requirements

Respond substantively to two classmates. Each response must:

- Minimum length: 150 words
- Either (a) add a point or example the original poster did not consider, OR (b) respectfully challenge a recommendation or conclusion the poster made
- Responses that only agree without adding substance earn zero points

---

## Grading Rubric

### Initial Post (30 points)

| Criterion | Excellent (Full Credit) | Satisfactory (Partial) | Insufficient |
|---|---|---|---|
| Detection / communication analysis (Q1 + Q2 / Q1 + Q2) | Uses module vocabulary accurately; demonstrates analytical depth (8 pts) | Correct concepts without depth (5 pts) | Vague or incorrect (0–2 pts) |
| Decision analysis under pressure (Q3 / Q2) | Considers tradeoffs explicitly; references IR framework (7 pts) | States a position without analysis (4 pts) | Missing (0–2 pts) |
| Strategic recommendation (Q4 / Q3) | Specific, actionable, grounded in course content (8 pts) | Correct direction without specifics (4 pts) | Missing (0–2 pts) |
| NIST connection (Q4) | Names specific NIST concept; connects to scenario (7 pts) | NIST referenced but loosely connected (4 pts) | Not referenced (0–2 pts) |

### Peer Responses (10 points each)

| Criterion | Full Credit | Partial | Minimal |
|---|---|---|---|
| Substantive extension or challenge | New point or reasoned challenge (7 pts) | Minor addition or restatement (4 pts) | Compliment only (0 pts) |
| Length and professionalism | 150+ words, professional tone (3 pts) | Under 150 words or informal (1 pt) | Under 75 words (0 pts) |

---

## Instructor Notes

Scenario A works best for students with an interest in threat intelligence and detection engineering. Scenario B works best for students interested in management and communications. Both scenarios avoid having a single "correct" answer — the goal is analytical rigor, not agreement with a predetermined conclusion. The ransom payment question in Scenario B reliably generates productive debate in peer responses. Encourage students to engage with that debate substantively rather than simply repeating government guidance.

---

*Texas Wesleyan University | CIS-4328 Information Security | Module 11*
