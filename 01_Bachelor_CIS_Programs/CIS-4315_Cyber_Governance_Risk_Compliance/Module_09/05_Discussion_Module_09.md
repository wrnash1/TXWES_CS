# Discussion Forum: Module 09 — Security Monitoring, Metrics, and Reporting

## Course: CIS-4315 Cyber Governance, Risk, and Compliance

## Texas Wesleyan University | Professor Nash

## CISM Domain Alignment: Domain 3 — Information Security Program

---

## Discussion Overview

This discussion forum asks you to apply Module 9 concepts to realistic security management scenarios. You will analyze situations involving metrics design, SIEM operations, and executive reporting — all core competencies in CISM Domain 3. Your posts should demonstrate critical thinking, use module vocabulary correctly, and connect your analysis to specific frameworks or principles covered in the reading guide and lecture.

---

## Forum Instructions

**Initial Post**: Respond to your assigned scenario (or any scenario if not assigned) with a response of **175–225 words** in complete, well-formed sentences. Do not use bullet points as your primary structure — write in paragraphs. Demonstrate that you have engaged with the module material by referencing specific frameworks, criteria, or concepts.

**Peer Responses**: Reply to **at least two classmates** who responded to a different scenario than your own. Each peer response must be a minimum of **60 words** and must add substantive engagement — ask a follow-up question, respectfully offer a counter-perspective, or extend their analysis with an additional example. "Great post, I agree" is not acceptable peer engagement.

**Due Dates**: Initial post due by Thursday 11:59 PM. Peer responses due by Sunday 11:59 PM.

---

## Scenario A — The Vanity Metrics Problem

FinServe Credit Union recently hired Marcus, a new Information Security Manager, away from a large enterprise bank. On his first day reviewing the existing security metrics program, Marcus finds a monthly executive report that includes the following metrics:

- Total firewall events blocked: 4,218,704

- Total security awareness emails distributed: 847

- Total number of security tools currently deployed: 23

- Total log entries processed by the SIEM: 186,000,000

The current CISO considers this report a strength of the program, pointing out that "the numbers show how active and engaged the security team is."

Marcus disagrees and wants to redesign the metrics program before next month's board meeting.

**Discussion Prompt**: Evaluate the four metrics listed in the report. Using NIST SP 800-55 criteria and the KPI/KRI framework from Module 9, explain specifically why each metric is or is not an effective security metric. Then, propose one replacement metric for any two of the four listed metrics, explain why your replacement metrics are more effective, and describe how Marcus should frame this redesign conversation with a CISO who believes the current metrics reflect program strength.

---

## Scenario B — Alert Fatigue Crisis

Nightwatch Insurance has operated a SIEM for two years. The platform ingests logs from 340 data sources and runs 87 active correlation rules. The SOC team of four analysts receives an average of 2,900 alerts per day. Analysts have responded by triaging alerts using only the alert title — reading neither the supporting log data nor the alert details — and closing approximately 2,700 alerts per day as "resolved" without investigation.

Last month, a threat actor compromised a privileged service account, moved laterally across three internal systems, and exfiltrated 40,000 customer records before being detected — not by the SIEM, but by a customer complaint about fraudulent activity. A post-incident review determined that the SIEM had generated a relevant privilege escalation alert on the first day of the attack. The alert was closed without investigation.

**Discussion Prompt**: Analyze the root cause of this SIEM failure. Explain the specific role that alert fatigue played in the breach going undetected and connect your analysis to the alert tuning principles covered in Module 9. Then, propose a concrete, phased plan for Nightwatch Insurance to reduce false positive alert volume over the next 90 days without sacrificing detection coverage for high-priority threat scenarios. Be specific about the types of tuning actions you would prioritize first.

---

## Scenario C — Executive Report Disconnect

Priya is the Information Security Manager for a regional hospital network operating under HIPAA. She has prepared her first quarterly security report for the board of directors. The report is 22 pages long and includes detailed vulnerability scan output, a complete list of SIEM correlation rules and their fire rates, a technical architecture diagram of the new firewall deployment, and an appendix listing every security incident with associated CVE numbers.

After the board meeting, the board chair sends Priya a note: "I appreciate the thoroughness, but honestly, I am not sure what you need from us or whether we should be concerned about anything. Can you simplify next quarter?"

The CFO adds separately: "I could not find anything about our HIPAA compliance status or what we would be fined if something went wrong."

**Discussion Prompt**: Diagnose the specific problems with Priya's executive report using the reporting principles and anti-patterns covered in Module 9. Explain what was missing and why those omissions made the report ineffective for a board governance audience. Then, outline the revised structure you would recommend for Priya's next quarterly report, including the specific content each section should contain and how each section addresses the concerns raised by the board chair and CFO.

---

## Peer Response Guidelines

When responding to a classmate, consider the following engagement approaches:

- If your classmate proposed a replacement metric in Scenario A, evaluate whether it meets all five NIST SP 800-55 criteria or whether any criterion is debatable.

- If your classmate described a SIEM tuning plan in Scenario B, ask a follow-up question about a specific tuning action — what data would they use to establish the new threshold? How would they validate the tuning was successful?

- If your classmate outlined a revised report structure for Scenario C, consider whether the structure they proposed would work equally well for a hospital board versus a financial services board, and note any differences.

Peer responses that simply summarize what the classmate said without adding new analysis or a question will receive partial credit only.

---

## Grading Rubric — 10 Points Total

| Criterion | Points | Description |
|---|---|---|
| Content accuracy | 3 | Response accurately applies module concepts, frameworks, and terminology |
| Depth of analysis | 3 | Response moves beyond surface description to evaluate, diagnose, or recommend with reasoning |
| Specific framework reference | 2 | Response explicitly references at least one named framework, criterion, or principle (NIST SP 800-55, CISM Domain 3, alert tuning principles, etc.) |
| Peer engagement quality | 2 | Both peer responses meet 60-word minimum and add substantive new content rather than agreement only |
| **Total** | **10** | |

### Grade Descriptors

**9–10 points**: Initial post demonstrates thorough understanding of module concepts, applies frameworks correctly, and provides specific actionable analysis. Peer responses meaningfully extend the conversation.

**7–8 points**: Initial post applies most concepts correctly with minor gaps. Peer responses are substantive but may lack depth or specificity.

**5–6 points**: Initial post shows basic familiarity with concepts but lacks framework application or specific analysis. Peer responses meet minimum length but add limited value.

**Below 5 points**: Post does not meet length requirement, uses no module vocabulary, or does not respond to the scenario prompt.

---

## Professor Nash — Closing Note

Security metrics and executive reporting may not be the most technically exciting topic in this course — but I would argue they are among the most professionally consequential. I have seen excellent security programs lose funding because the CISO could not communicate value to the board. I have seen organizations with mediocre technical controls survive audits and earn executive trust because they measured, reported, and communicated effectively.

The CISM exam tests this domain heavily because ISACA recognizes that governance-level security management requires communication skills that are distinct from — and in many roles more important than — technical skills. Your ability to tell a coherent, data-driven security story to a non-technical audience is a career-defining competency.

In your posts this week, resist the temptation to be purely theoretical. The scenarios are realistic. Engage with them as if you are the person in the room who has to make the argument, redesign the program, or deliver the board report. That is the frame of mind you need both for the CISM exam and for the work itself.

See you in the forum.

— Professor Nash
